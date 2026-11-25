---
game_id: GAME-0701
slug: warcraft-ii-tides-of-darkness
game_title: "Warcraft II: Tides of Darkness"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-139
    - ACT-189
    - ACT-316
    - ACT-318
  system:
    - SYS-549
    - SYS-550
    - SYS-551
    - SYS-553
  constraint:
    - CON-292
    - CON-467
    - CON-469
  information:
    - INF-131
    - INF-224
    - INF-225
  objective:
    - OBJ-368
  time:
    - TIM-003
---

# Game: Warcraft II: Tides of Darkness

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first Alliance mission teaches construction as a win condition.
Workers gather and build, and completed Farms allow a larger workforce.
Victory follows the last completed required structure.

## Analysis scope

- Version / ruleset: the original commercial English MS-DOS base game
  from Blizzard Entertainment, December 1995. Start a new Human
  campaign and use Act I, Hillsbrad. The exact executable revisions
  of the sampled DOS-labelled recordings are unverified.
- Structured analysis target: PLAT-DOS in
  [platform coverage](../../platforms/games.json).
- Entry: accept the first mission briefing. Start with one Town Hall,
  one completed Farm, one Peasant and three Footmen on the winter map.
- Primary decision loop: read stock and assign Peasants to gold and
  wood. Use Town Hall training if additional builders or gatherers
  are useful and food headroom permits. Commit clear Farm and
  Barracks footprints. Leave the builders time to finish them
  while the other workers and units continue their assigned actions.
- Positive terminal: own at least four completed Farms and one
  completed Barracks and observe the Victory dialog. Confirm that it
  leads to the results screen. Stop before playing the second mission.
- Included: clear construction sites and progress, the alternative
  observed completion orders, finite resource extraction and return
  to the Town Hall, paid Peasant recruitment and food headroom,
  nearby Footman orders, the local field and fog, and the victory gate.
- Excluded: a requirement to train Footmen or eliminate enemies,
  detailed combat and AI patrol rules, exact scenario polling delay
  and fastest completion, cheats, the shareware campaign, Mac ports,
  later missions, Beyond the Dark Portal, Battle.net Edition and
  Remastered.
- Potential scoped module: contrast Hillsbrad with the next mission's
  rescue and destination objective under the same original controls.
- Direct-play status: no personal MS-DOS session or executable
  inspection. The original printed tutorial explains the economy and
  placement rules. Two independent DOS-labelled sessions corroborate
  the starting layout, alternate construction orders and victory by
  completing the outpost. Short frame sequences were inspected in the
  background without playing their audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WCT-001 | Blizzard published the original commercial game in December 1995. The sampled sessions identify DOS and show the English base campaign and the first Human mission. | Confirmed | Corroborated | High | P1, P2; W1, W2 |
| WCT-002 | Hillsbrad starts with a Town Hall, one Farm, one Peasant and three Footmen. The briefing requires four Farms and a Barracks. The starting Farm contributes toward the four. | Observation | Corroborated | High | P2 p. 8; W1 3:16–3:46 and 15:46–15:52; W2 4:01 and 10:30 |
| WCT-003 | Assigning a selected Peasant to a mine or trees starts a repeated extraction-and-carry loop. Returning to the Town Hall deposits the load. Depletion or reassignment can interrupt it. | Observation | Corroborated | High | P2 pp. 10–11; W2 8:45–8:57 |
| WCT-004 | The player selects a building and an explored footprint. A blocked tile can prevent placement, and a worker must reach the construction site before work starts. The scaffold and a progress indicator precede the completed structure. | Observation | Corroborated | High | P2 pp. 9–10; W2 8:51–9:33, 10:03–10:06 |
| WCT-005 | Town Hall training spends gold and finishes over time. A completed Farm supplies four places and the Town Hall one. If food headroom is absent, further training is refused. | Observation | Corroborated | High | P2 pp. 8–10; W2 4:35–4:42 and 8:45 |
| WCT-006 | Selected units can move to ordered locations while worker activity continues. The command view identifies the acting unit, stock, orders and construction state. Explored ground persists in fog even when current opposing units are concealed. | Observation | Corroborated | High | P2 pp. 7, 10–13; W2 4:08–4:25 and 8:45–9:33 |
| WCT-007 | Four finished Farms alone leave the mission active until the Barracks is completed. A second route has the Barracks first and completes the final Farm as the last listed requirement. | Observation | Corroborated | High | W2 8:45, 10:03–10:13; W1 15:33–15:53 |
| WCT-008 | Victory is signalled by a dialog and results. The zero-kill DOS route wins with six completed buildings and with original Footmen and trained Peasants visible, without any observed new Barracks unit. | Observation | Corroborated | High | W2 10:06–10:13 and 10:30; W1 15:52–16:08 |

## Basic data

- Release / origin: Blizzard Entertainment, English commercial
  MS-DOS original, December 1995.
- Mechanical family: FAM-015. Assign separate workers to collection
  or building and move the existing units without stopping the economy.
- P1: [Blizzard's official Warcraft timeline](https://worldofwarcraft.blizzard.com/en-us/story/timeline/chapter-2).
  Identifies and dates the original game.
- P2: [Blizzard's original English manual, preserved scan and text](https://oldgamesdownload.com/manual/warcraft-ii-tides-of-darkness-dos-mac-windows-manual-english/).
  The opening tutorial on printed pp. 6–13 documents starting pieces,
  food, the footprint preview, builder travel, deposit and unit orders.
- P3: [Blizzard's official quickstart and later edition notes](https://news.blizzard.com/en-us/article/24055598/fight-for-honor-in-warcraft-ii-tides-of-darkness-now-available-on-battle-net).
  The legal publisher reference is marked as the later digital
  distribution. Its release contents do not identify a DOS binary.
- W1: [Major Thriftwood's DOS Act I recording](https://www.youtube.com/watch?v=Yseq0ex-zfg&t=196s).
  Shows the English briefing, completed Barracks with a final Farm
  still under construction, the Victory dialog and the results.
- W2: [King Toko's DOS recording](https://www.youtube.com/watch?v=n4a1P8YpTDY&t=241s)
  and [platform notes](https://kingtoko.com/2019/05/05/good-game-warcraft-ii-tides-of-darkness-dos/).
  Shows a new Farm opening, Peasant recruitment, all four Farms before
  the Barracks, and a victory with zero kills. Both footage editions
  are attributed by their authors. Their executable versions are unknown.
- Claim IDs: WCT-001–WCT-008.

### Reproducible fixture evidence

1. Start the Human campaign. Read the Hillsbrad briefing at
   W1 3:16–3:46. Count the Town Hall, single finished Farm, Peasant
   and three Footmen at W2 4:01. Keep the starting Farm standing.
2. Build or train in an order the stock permits. W2 shows the
   Farm choice at 4:01 with a displayed cost of 500 gold and
   250 lumber. After commitment, the selected Peasant moves to
   build it. There is a clear construction site at 4:08 and
   all stages precede the completed Farm by 4:42. Town Hall
   recruitment is observed around 4:35–4:42. The manual documents
   the food requirement and the capacity gain at Farm completion.
3. Assign a Peasant to each needed source as staffing and stock
   allow. Leave the worker returning to the Town Hall while
   directing other units. W2's gold readout goes from 1,100 to
   1,200 at 8:45–8:51 while the Barracks is not yet committed.
4. W2 has four full Farms at 8:45. Try a clear Barracks location.
   The partial red preview and rejection are visible at 8:51.
   W2 commits a new site by 9:03, shows an incomplete Barracks
   with progress at 9:33 and 10:03, then the full Barracks at 10:06.
   The Victory dialog is visible by 10:13. At 10:30 the board reports
   six buildings and zero kills. The final panel follows the result
   dialog and does not require the player to train a Footman there.
5. In the other order, W1 15:33 has the Barracks already finished
   while the bottom-right Farm is visibly incomplete. At 15:46
   four Farms are complete and by 15:52 the Victory dialog appears.
   Comparing these two orders verifies that the scenario does not
   fix a unique last building. The sampling does not measure the
   interval at which the mission evaluates the completed stock.

## Mechanical decomposition

### Action Genes

- ACT-139: choose Farm or Barracks and commit a compatible footprint.
- ACT-189: order the selected Footmen to new world positions while
  economic work continues.
- ACT-316: train a paid Peasant through the completed Town Hall.
- ACT-318: dispatch a selected Peasant to harvest or to construct
  an addressed site.

### System Behaviour Genes

- SYS-549: extracted gold or lumber is carried and deposited at
  the Town Hall, allowing repeated deliveries.
- SYS-550: the assigned worker advances the construction to its
  completed building once the site is reached.
- SYS-551: the Town Hall advances a paid training order and emits
  the finished unit after the measured progress.
- SYS-553: finished Farms add usable food capacity; the Town Hall
  contributes one. This capacity bounds additional unit creation.

### Constraint Genes

- CON-292: the authored winter terrain and occupied squares limit
  legal footprints. An overlapping or otherwise blocked footprint
  cannot be used as shown.
- CON-467: completed site, gold and food headroom bound Peasant
  training. A Farm is a provider rather than a Peasant producer.
- CON-469: a worker needs a reachable eligible source and Town Hall
  return to convert collection into usable shared stock.

### Information Genes

- INF-131: the tinted footprint and rejection feedback inform
  where the selected building can be committed.
- INF-224: economy, selected-unit orders and local building or
  recruitment progress appear in the live command screen.
- INF-225: explored geography remains on the map while current
  hostile units outside allied sight are unobserved.

### Objective Genes

- OBJ-368: satisfy both completed-building counts to settle the
  mission. Four Farms includes the starting Farm; one Barracks is a
  separate completion condition. A foundation does not count.

### Time Genes

- TIM-003: resource deliveries, construction and training progress
  while the player can issue orders elsewhere. No fixed terminal
  countdown is established for this mission.

### Parameters

Starting stock, cost and footprint per building, number of workers,
source locations, training slot, food provision, completion status,
fog coverage and the two authored counts are parameters.

## Reproducible transitions

| Entry state | Input | Expected next state | Evidence |
| --- | --- | --- | --- |
| One completed Farm and Town Hall | Assign a Peasant to a reachable mine or trees | The worker travels, extracts and returns loads to stock | WCT-003 |
| Sufficient stock and explored clear site | Choose a Farm or Barracks and commit a placement | The Peasant reaches the site and advances construction | WCT-004 |
| A Farm is still under construction | Wait while the builder finishes | The Farm is completed and four more food places are available | WCT-004, WCT-005 |
| Town Hall has food headroom and gold | Order a Peasant and allow training to complete | A new available worker appears at the site | WCT-005 |
| Exactly one building count remains short | Finish the last required structure | Victory dialog, then mission results | WCT-007–WCT-008 |

## Strategic and experiential structure

The farm supports two decisions. It contributes to the mission's
completed-building quota and lets the player field more workers.
Training more workers adds parallel capacity but spends gold that could
go into the remaining buildings. Fighting can secure space while the
work continues, but a zero-kill result confirms that fighting is not a
separate mission objective.

## Replay and variation

The two observed completion orders give the same terminal. Initial
unexplored terrain and rejected placements invite adjustments to the
build site. No exact fastest route, delayed evaluation constant,
or MS-DOS revision comparison is established.

## Adjacent systems and history

Later stages add naval resources, other units and different goals.
The current retail re-release and its bundled expansion are distinct
from this DOS fixture.

## Normalised genome

- Action: ACT-139, ACT-189, ACT-316, ACT-318.
- System Behaviour: SYS-549, SYS-550, SYS-551, SYS-553.
- Constraint: CON-292, CON-467, CON-469.
- Information: INF-131, INF-224, INF-225.
- Objective: OBJ-368.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `700` (`GAME-0001`–`GAME-0700`).
- Exact genome matches: none.
- Tied near matches: `GAME-0469` — StarCraft (`14 / 21 = 0.666667`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [StarCraft (GAME-0469)](starcraft.md) | ACT-139, ACT-189, ACT-316, ACT-318, CON-292, CON-467, CON-469, INF-224, INF-225, SYS-549, SYS-550, SYS-551, SYS-553, TIM-003 | Both pair worker deposits and timed construction with live unit orders. Wasteland requires a completed Barracks, a surviving Raynor and a live count of ordinary Marines. In Hillsbrad, the mission counts completed buildings of two specified types. A completed Farm contributes both food capacity and target stock. | Near, `0.666667`. |

## Taxonomy impact

Reuse the RTS command, resource, placement, construction, training,
information and running-time mechanisms. Admit an objective whose
thresholds count completed structures of specified types. The type
counts are scenario parameters. Learning the two thresholds does not
itself finish the mission.

## Negative results

- Starting with one complete Farm means three more suffice in the
  witnessed scenario.
- Four complete Farms and an unfinished Barracks are insufficient.
  A complete Barracks and an unfinished fourth Farm are insufficient.
- A witnessed zero-kill victory rules out compulsory enemy elimination
  for this scoped Human mission.
- The sampling does not establish exact terminal delay or whether
  different executable revisions evaluate the quotas identically.

## Delta summary

Sixteen genes represent the paid economy and authored construction
win with unrequired combat in a single opening mission.

## New facts

- The same Farm changes food capacity and contributes to a specific
  scenario requirement.
- Pre-existing completed structures count toward the observed quota.
- Both orders finish the same mission, and one leaves all enemy kills
  at zero.

## Principles and design implications

Let a building be useful before its final quota is satisfied so the
player has a reason to build it early. Keep construction progress
legible, distinguish a reserved site from a completed structure, and
show a terminal response when the authored thresholds are all met.

## Puzzle or game generation potential

Specify at least two structure types and independent target counts.
Seed one eligible structure at entry, and give the player one worker
and constrained materials. Test both completion orders and require the
terminal only after the last missing building is actually finished.

## New genes

- OBJ-368

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 447](../../../research/taxonomy-changes/TAXONOMY_CHANGE_447.md).

## New questions

- What happens if a required building is lost between completion
  and the next victory evaluation?
- How does the successor rescue objective change the value of
  fixed infrastructure and military-unit orders?

## Next recommended game

Continue Selection 060 with GAME-0702, Escaping Wonderland, on
Meta Quest 3.

## Why this game

The first mission isolates construction and workforce decisions as
a terminal goal within a familiar real-time strategy interface.
