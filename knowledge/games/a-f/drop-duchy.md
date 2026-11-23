---
game_id: GAME-0649
slug: drop-duchy
game_title: Drop Duchy
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-005
    - ACT-021
    - ACT-127
    - ACT-722
    - ACT-861
  system:
    - SYS-1872
    - SYS-1873
    - SYS-1874
    - SYS-1875
    - SYS-1876
  constraint:
    - CON-001
    - CON-007
  information:
    - INF-005
  objective:
    - OBJ-029
  time: []
---

# Game: Drop Duchy

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English Windows base game on Steam app 2525310,
  commercially released 5 May 2025. The primary recording is from launch
  week. Neither recording identifies its Steam depot manifest.
- Entry: after the separate tutorial, in The Duchy's Classic Normal run,
  elect the first observed ordinary hostile Wooded Region and reach its
  Preparation Phase. The player enters with 50 of 50 defence.
- Primary decision loop: select allowed building cards, steer and rotate the
  emerging pieces, commit drops to complete rows or recruit from the right
  terrain, and then order the deployed friendly and enemy groups before
  starting automatic combat.
- Exit: the combat overview reports 40 player units, 28 enemy units and
  four friendly survivors. The next screen credits four gold for the
  survivors. Proceed through the card offer to the live map and visit
  the Trading Fair.
- Included: the hostile node, paid selection capacity, visible queue and
  Reserve use, row exploration, terrain-sensitive recruitment, combat
  ordering, group merging and counters, proceeds and the map return.
- Excluded: tutorial battle settlement, full runs, bosses as objectives,
  the exact shuffle and fall timers, local restart or save persistence,
  other factions, DLC, Complete Edition, later updates and non-Windows ports.
- Suggested later scope: test the same formation across victory and loss
  to isolate reserve rules, defence deductions and precise rounding.

## Direct-play status

No direct play was performed. The commercial Steam listing, launch
announcement and publisher press kit establish the edition and broad
rules. MasakoTeam's 8 May 2025 opening supplies the target outcome.
RonEmpire attributes a separate recording to the Windows full release.
Its later combat and resource screens corroborate the shared rules,
rather than serving as a second replay of the same Wooded Region.
Frames and visible text were inspected in the background without audio.
The Steam depot, physical inputs, random seed and save state are unknown.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DD-001 | Sleepy Mill Studio's base game launched commercially on Windows via Steam on 5 May 2025. | Confirmed | Direct | High | P1, P2, P3. W1 and W2 are release-week or release-attributed footage, not a demo certification. |
| DD-002 | After the stand-alone tutorial the player starts a Classic Normal Duchy run. Choosing a hostile Wooded Region opens a preparation panel with a three-card enemy deck and a selectable player building subset. The player adds a slot at a cost of 50 food. | Observation | Corroborated | High | W1 18:50–20:15 and 23:43–24:08. The balance drops from 119 to 69. W2 5:30–6:10 corroborates the ordinary run boundary. |
| DD-003 | Terrain and buildings share the finite grid. The player changes the active piece's pose and commits a fall onto unoccupied supported cells. Upcoming pieces and the Reserve are shown. A Rally Point is set aside and is still in Reserve at building settlement. | Observation | Corroborated | High | P1, P3, W1 24:18–25:14, 25:50–26:50 and 27:50–28:29. W2 7:30–9:30 supplies ordinary placement. Exact eligibility for repeated Reserve changes is untested. |
| DD-004 | Filling a row explores it and grants terrain-dependent resources while the cells remain. Exploring two rows together shows an extra bonus. | Observation | Corroborated | High | W1 26:00 and 28:05–28:09; P1, P3. The capture shows intact occupied rows, and the multi-exploration banner indicates +1 each. Exact bonuses for other row counts are outside scope. |
| DD-005 | A level-one Wooden Fortress starts with 10 swordsmen. It turns adjacent forest into plain and gains three swordsmen per such tile. The first Fortress turns two orthogonal forest neighbours into plain and rises to 16. | Observation | Corroborated | High | W1 24:52–24:57 card text and on-board values. W1 28:56 settlement lists two Fortress groups at 10 + 6 each, and a Watchtower group of 8. R1 separately reports the forest conversion. |
| DD-006 | Combat planning orders deployed forces from both sides in one sequence. Start Battle becomes available when all groups are present. The game resolves the sequence automatically. Same-side groups combine and take the larger group's type, or the destination type on equal size. An advantageous type receives 50% additional strength. | Observation | Corroborated | High | W1 28:29–28:53 on-screen Combat Rules and committed outcome; W2 44:50–45:10 corroborates the same planning panel in a later encounter. The rounding of fractional advantages is not measured. |
| DD-007 | The scoped result is 40 friendly against 28 enemy, with 4 friendly survivors. The four survivors grant four gold, defence stays 50/50, and the player passes the card offer and reaches the Trading Fair from the live map. | Observation | Corroborated | High | W1 28:55–29:36. W2 shows similar settlement and map return after a different encounter around 46:20–48:20. W1 is the source for this packet's exact numbers. |

## Basic data

- Analysis target: `PLAT-WINDOWS-PC`, original Steam base game, app 2525310.
- Developer: Sleepy Mill Studio. Publisher: The Arcade Crew and Dotemu on
  the commercial listing.
- Mechanical families: `FAM-006`, spatial assembly and packing, and
  `FAM-009`, tactical forecast and counterplay.
- Checked: 2026-11-22.
- P1: [Commercial Steam listing](https://store.steampowered.com/app/2525310/Drop_Duchy/).
  Release date, platform and the terrain, building and recruiting loop.
- P2: [Publisher launch announcement](https://store.steampowered.com/news/posts/?enddate=1746457483&feed=steam_community_announcements).
  Commercial launch on 5 May 2025, distinguished from the earlier demo.
- P3: [Publisher press kit](https://www.thearcadecrew.com/PressKit/project/Games/DropDuchy).
  Full release and terrain/building interaction, kept separate from later
  Complete Edition and DLC material.
- W1: [MasakoTeam, release-week walkthrough](https://www.youtube.com/watch?v=VGex_7ahpok&t=1423s).
  Classic Normal route, 18:50–29:36, with the hostile Wooded Region from
  23:43 and its combat from 28:29.
- W2: [RonEmpire, full-release recording](https://www.youtube.com/watch?v=t1cRrmF_tdU&t=2690s).
  Independent ordinary play, and a different encounter's combat planning and
  aftermath from 44:50 to 48:20.
- R1: [The Guardian's release-week firsthand account](https://www.theguardian.com/games/2025/may/06/drop-duchy-review).
  Corroborates the rules of forest conversion and the layout-to-combat turn.

## Mechanical decomposition

### Action Genes

- ACT-005: move the active piece sideways or rotate it to engage useful
  neighbours while keeping fitting positions.
- ACT-021: select a bounded subset of visible building cards for the round.
- ACT-127: choose a connected hostile region and, after settlement, move
  along the revealed route to the next service.
- ACT-722: commit the active footprint through its unobstructed vertical
  drop to the support boundary.
- ACT-861: click the placed groups of both sides to prescribe one complete
  combat chain before execution.

### System Behaviour Genes

- SYS-1872: explore newly filled lines, credit their terrain yields and
  keep the footprints in place.
- SYS-1873: convert compatible neighbouring terrain on building placement
  and issue a troop increment for each tile converted.
- SYS-1874: combine same-side groups in the sequence, retaining the larger
  group's class or the destination class for a tie.
- SYS-1875: settle a hostile pair by strength subtraction after applying
  its declared type matchup.
- SYS-1876: convert remaining friendly troop count to spendable currency
  at successful settlement.

### Constraint Genes

- CON-001: fixed cells may hold at most one settled footprint.
- CON-007: the active translation and orientation obey the grid and
  obstruction limits before locking.

### Information Genes

- INF-005: upcoming block identities and their order are visible beside
  the active field.

### Objective Genes

- OBJ-029: remove the deployed enemy force and preserve surviving friendly
  strength through the bounded battle.

### Time Genes

No autonomous fall rate or lock delay is admitted for the scoped setting.
Combat runs after the separate planning commitment. Exact playback timing
does not determine the tested combat outcome.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Ordinary Classic Normal map at a route junction | Open the hostile Wooded Region, choose buildings and enable the fourth slot | Preparation displays the enemy deck. Food drops by 50 as the player adds selection capacity | DD-002 |
| Forest and plains support the lower grid | Drop the first Wooden Fortress beside the left forest and above another forest cell | Both adjacent cells become plains. A third diagonal forest remains. The group rises from 10 to 16 | DD-003, DD-005 |
| Field has nearly occupied rows | Close the gaps and store the unplaced Rally Point in Reserve | Completed rows grant resources and retain tiles. The stored enemy building contributes no deployed group in the shown settlement | DD-003, DD-004 |
| Final placement ends building | Include the three friendly and two enemy groups in the chain | Start Battle is enabled and the entire order is committed | DD-006 |
| Combat executes automatically | Allow ordered group merging and hostile exchanges | Four friendly units survive. Defence remains 50/50 | DD-006, DD-007 |
| Combat and exploration receipt displayed | Continue past the card offer and select the connected Trading Fair | A playable map and service panel replace the encounter grid | DD-007 |

## Strategic and experiential structure

A perfectly packed row can be a poor military placement if it leaves the
wrong terrain next to a building. Conversely, converting a forest to a
plain can add a group now and change the terrain later explored for
resources. The field therefore has two evaluations. Preparation trades
shape fit and terrain yield against recruitment on both sides. Combat
then trades the benefits of merging friendly groups against the classes
and order of the enemies. The raw numerical lead alone does not fix the
margin.

## Replay and variation

The second recording takes a longer route before showing its committed
battle order. Its battlefield, card mix and outcome differ. It supports the
shared preparation and combat structure without fixing a repeatable map
seed. The Wooded Region's exact total and payout belong to the W1 state.

## Adjacent systems and history

The launch package also offers faction progression, building upgrades,
route services and act bosses. The Trading Fair establishes that ordinary
control continues after the bounded fight. The later services and map
economy are not analysed beyond arrival.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-005, ACT-021, ACT-127, ACT-722, ACT-861 | Prepare cards, shape drops, choose a route and order the battle |
| System Behaviour | SYS-1872, SYS-1873, SYS-1874, SYS-1875, SYS-1876 | Explore, recruit, merge, resolve matchups and settle survivors |
| Constraint | CON-001, CON-007 | Keep fixed cells exclusive and active moves legal |
| Information | INF-005 | Expose scheduled upcoming elements |
| Objective | OBJ-029 | Defeat the bounded enemy force |
| Time | None | No admitted setting-specific timer |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `648` (`GAME-0001`–`GAME-0648`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`4 / 25 = 0.160000`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Tetris (GAME-0004)](../s-z/tetris.md) | ACT-005, CON-001, CON-007, INF-005 | Both reposition the incoming element under occupancy and collision constraints and show exact upcoming pieces. NES Tetris clears completed rows and lowers the stack. Drop Duchy retains rows and credits their terrain, then uses building adjacency and troop ordering in a separate fight. | Near, `0.160000` |

## Taxonomy impact

The new action assigns both sides’ settled groups to one chain. The
systems separate retained-row exploration, linked terrain conversion and
recruitment, allied group merging, strength matchup and survivor payout.
SYS-008 removes filled rows. SYS-1521 defers their removal to mode exit.
Here exploration remunerates the occupied terrain and leaves it on the
same battlefield. SYS-487 concerns a city district's yield rather than
immediate conversion and recruitment by a landed building footprint.

## Negative results

- A complete row is explored and kept. It does not collapse the stack.
- Unplaced Reserve cards do not count as deployed units in this receipt.
- The initial 12-unit numerical advantage does not equal the observed
  survivor count.
- Neither capture supplies an exact repeatable map seed or proves
  defence-loss rounding from the scoped victory.

## Delta summary

Fourteen scoped genes, with six additions and eight reuses. The packet
ends at the map service after the first observed ordinary hostile fight.

## New facts

- The same grid can contribute resource receipts and units through
  different rules.
- Completing lines preserves geometry required by later placements.
- Combat planning lets the player order both sides' troops, while
  matchup resolution and the payout remain automatic.

## Principles and design implications

Make support geometry persist so a finished line can still constrain
future choices. Let a close resource puzzle produce a tactical relation
that the player must order separately. Give a clear receipt for any
units that become currency at the transition.

## Puzzle or game generation potential

Give a compact board some pre-existing terrain and an incoming mix of
friendly and hostile building shapes. Credit filled rows once without
removing them. Convert typed neighbours into a declared troop increment
and allow ordering of the resulting groups before committed resolution.

## New genes

- ACT-861
- SYS-1872
- SYS-1873
- SYS-1874
- SYS-1875
- SYS-1876

## New combinations

None. No verified combination is a subset of the scoped genome.

## Taxonomy changes

[TAXONOMY_CHANGE_395](../../../research/taxonomy-changes/TAXONOMY_CHANGE_395.md).

## New questions

How does the exact combat advantage round, and how much defence is lost
if the chain leaves an equivalent enemy group? A matched counterfactual
would isolate these effects from deck shape and recruitment.

## Next recommended game

Einhänder on the original North American PlayStation disc. Trace one
weapon pickup and active use through the first stage's result.

## Why this game

The scoped fight connects visible packing decisions to a tactical
settlement with an independently checkable resource outcome.
