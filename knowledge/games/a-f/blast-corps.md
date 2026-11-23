---
game_id: GAME-0539
slug: blast-corps
game_title: Blast Corps
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-201
    - ACT-610
  system:
    - SYS-037
    - SYS-386
    - SYS-1560
  constraint:
    - CON-426
  information:
    - INF-523
  objective:
    - OBJ-181
    - OBJ-299
  time:
    - TIM-003
---

# Game: Blast Corps

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Ramdozer, Simian Acres, obstacle count, travel speed and route width are
scenario parameters.

## Analysis scope

- Version / ruleset: original English North American 1997 Nintendo 64
  release identified by `NUS-NBCE-USA`, ordinary first Simian Acres carrier
  mission on fresh progression, default controls and an installed Controller
  Pak for optional progress persistence. Cartridge ROM revision and exact
  timing are unverified.
- Entry: select Simian Acres on a new file. Start at the first controllable
  Ramdozer state after the fly-by. Use the bulldozer throughout the demolition
  route and standard camera controls as needed.
- Primary decision loop: identify the buildings intersecting the carrier's
  corridor, line up the bulldozer and drive its blade into the obstruction.
  Choose the next target according to approach time and the carrier's
  advancing position. Drive past useful roadside dispersal units when they
  are on the way, without making their total a clearance prerequisite.
- Positive exit: eliminate the obstructions before the carrier reaches
  them. Wait for its safe arrival or stop, dismount and enter the enabled
  Blast Corps semi for early closeout. Stop after the primary commendation
  and return to the map. Negative exit: the carrier reaches a remaining
  blocker, the collision ends the mission, and a new attempt is needed.
- Included: steering, seated and on-foot control, camera, driving impact
  on simple structures, activation of units on the primary route, obstacle
  marks, carrier motion, terminal collision, gated exit and primary award.
  Excluded: train and American Dream detour, full optional cleanup, timed
  medal replays, training, later missions, TNT tactics, exact speed, impact
  thresholds, non-Pak retention, Switch and Rare Replay.
- Direct-play status: the original cartridge, emulator, ROM and save were
  not opened. Nintendo's instruction booklet and contemporary route feature,
  two written N64 walkthroughs and one static screenshot were checked.
  No video or audio playback was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BC-001 | The North American English Nintendo 64 version is NUS-NBCE-USA. The first live carrier mission is Simian Acres and starts in Ramdozer. The booklet specifies A forward, B reverse, local left/right turning, Z stop and dismount and C-button rotation and zoom. | Confirmed | Corroborated | High | P1, P2, P3, S1, S2, S3 |
| BC-002 | The transport's advance depends on its fixed corridor rather than player pace, camera or a target steering command. The demolition vehicle can move ahead and approach the corridor from the side. | Observation | Corroborated | High | P1, P2, S1, S2, S3 |
| BC-003 | Impact from Ramdozer clears simple buildings; the route includes metal sheds, houses, the gas station and a red barn beyond the pond. Flashing arrows distinguish blockers on the carrier's route. The drivable ground survives removal. | Observation | Corroborated | High | P2, S1, S3 |
| BC-004 | Contact between the carrier and an uncleared blocker causes immediate attempt failure; the obstacle's arrival window depends on the carrier's position. A stopped player does not suspend that advance during live play. | Observation | Corroborated | High | P1, P2, P3, S2, S4 |
| BC-005 | Path clearance earns its own gold commendation, separate from the award for the full destruction, survivor and dispersal-unit set. Units are activated on nearby passage; a route row can guide navigation. | Observation | Corroborated | High | P1, P2, S1, S2 |
| BC-006 | Safe carrier arrival closes the primary stage. After clearance the separate staff semi can close it early when entered on foot. Its radar indication is a bearing. Use the semi and Controller Pak for the documented retained optional progress. | Observation | Corroborated | High | P1, P2, P4, S2 |

## Basic data

- Rare, published by Nintendo, Nintendo 64, North American 1997 release.
  Single-player route demolition with an independent moving objective.
- Families: physics and object manipulation, real-time system pressure,
  and agent routing and coordination.
- Sources accessed 2026-11-17:
  - **P1** — [Nintendo North American instruction booklet](https://www.videogamemanual.com/n64/Blast%20Corps%20%28USA%29.pdf),
    the NUS-NBCE-USA cover, printed pages 7–8 and 20–21. Inspected
    Ramdozer controls and vehicle profile, display, progression, optional
    progress storage and the secondary award.
  - **P2** — [Nintendo Power 95, April 1997](https://www.scribd.com/document/780675105/Nintendo-Power-Issue-095-April-1997),
    the Simian Acres walkthrough and Demolition-stage rule. The
    [VGHF catalogue](https://library.gamehistory.org/repositories/2/archival_objects/1384)
    establishes Nintendo of America as the publisher. The text
    distinguishes normal arrival, early semi exit and optional cleanup.
  - **P3** — [Nintendo's official Switch collection notice](https://www.nintendo.com/en-ca/whatsnew/feb-update-see-what-games-were-added-to-the-nintendo-64-super-nes-and-nes-collections/),
    for original N64 year, runaway carrier objective and official
    availability of the separate re-release.
  - **P4** — [Nintendo FAQ, archived on GameFAQs](https://gamefaqs.gamespot.com/n64/196774-blast-corps/faqs/3155),
    for the semi's bearing and departure to save additional progress.
  - **S1** — [Rare Gamer's carrier-mission guide](https://www.raregamer.co.uk/blast-corps-carrier-mission-guide/)
    and [its static Simian Acres screenshot](https://www.raregamer.co.uk/staf/BL1.png),
    for the approach, pond, vulnerable shed sequence and actual road cues.
  - **S2** — [Marshmallow's N64 walkthrough](https://gamefaqs.gamespot.com/n64/196774-blast-corps/faqs/3154),
    for the first-mission order, moving carrier and separate train detour.
  - **S3** — [HonestGamers N64 play account](https://www.honestgamers.com/15414/nintendo-64/blast-corps/review.html),
    for bulldozer assignment and contact with simple farm structures.
  - **S4** — [Cubed3 N64 play account](https://www.cubed3.com/games/reviews/nintendo-64/blast-corps),
    for continuous carrier advance and terminal obstruction contact.
- Claim IDs: BC-001–BC-006.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: direct the operator on foot after leaving the
  bulldozer, for example to reach the accepted exit semi.
- Reuse `ACT-201`: steer and drive the occupied Ramdozer and use Z
  to stop and leave its seat. Re-entering a vehicle and directly
  operating it differs from the carrier's automatic motion.
- Reuse `ACT-610`: use the C buttons to rotate or zoom the following
  view while the bulldozer and route retain their positions.
- Claim IDs: BC-001–BC-003, BC-006.

### System Behaviour Genes

- Reuse `SYS-037`: approaching a compatible radiation dispersal unit
  activates it and advances its own attainment count during the route.
- Reuse `SYS-386`: a legal bulldozer impact removes eligible obstruction
  geometry and opens ground passage without removing the underlying route.
- New `SYS-1560`: the carrier advances independently and hitting
  an uncleared blocker ends the attempt immediately.
- Claim IDs: BC-002–BC-005.

### Constraint Genes

- Reuse `CON-426`: early departure via the terminal semi is only
  available when the route is cleared and the operator reaches it.
- Claim ID: BC-006.

### Information Genes

- New `INF-523`: local flashing arrows mark obstructions occupying
  the protected route separately from other destructible structures.
  The semi bearing and destruction tally are separate display parameters.
- Claim IDs: BC-003, BC-005, BC-006.

### Objective Genes

- Reuse `OBJ-181`: settle the first mission back onto the map, retaining
  primary completion and the credited optional subset using the documented
  Pak/exit configuration. The full optional set has a separate award.
- New `OBJ-299`: remove the finite blocking geometry before the protected
  independent transport encounters any of it, then settle by safe arrival
  or the enabled early exit.
- Claim IDs: BC-004–BC-006.

### Time Genes

- Reuse `TIM-003`: deciding to line up, move aside, drive or dismount
  takes place while the carrier proceeds in live play. The player can
  use the ordinary pause menu, which differs from simply stopping.
- Claim IDs: BC-001, BC-002, BC-004.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| First live control at the Simian Acres slope | Accelerate and steer Ramdozer toward the lane | Bulldozer position changes while the carrier moves independently | Different movement authority for the two bodies | BC-001, BC-002 |
| A marked corrugated shed blocks the corridor | Turn the camera if needed, line up and drive the blade into it before the carrier arrives | Shed geometry comes down and the path opens | World-guided impact alters the actual available route | BC-001, BC-003 |
| Dispersal units lie along the lane | Pass close enough while driving to the next blocker | Nearby units activate while the carrier and bulldozer continue | Activation is useful for guidance and optional credit | BC-005 |
| A marked obstruction remains ahead of the live carrier | Stop the player vehicle and allow the carrier to reach that obstruction | The collision terminates the attempt | A local contact deadline differs from wall-clock score | BC-002, BC-004 |
| The last obstruction on the route has been cleared | Leave other structures alone; wait for arrival or dismount and use the semi | Receive primary commendation without the optional complete-cleanup medal | Primary clearance is independent of the optional set | BC-005, BC-006 |

## Strategic and experiential structure

The demolition route cuts through the farm instead of following ordinary
road edges. The moving carrier gives each intact obstruction a different
deadline. Start with nearby marked blockers and use the view to line up
a clean strike. The additional environmental targets, damage tally and
dispersal units can distract from the urgent corridor. Once the corridor
is safe the player can choose between waiting and using the closeout semi.

## Replay and variation

- Repeat the approach on a fresh file, clear the marked route and leave
  optional off-route structures intact. Compare this with the separate
  cleanup award described in the booklet.
- Compare an early semi exit with a live wait after the final blocker
  is gone. A deliberate wait before clearing a constraint would instead
  permit a terminal collision.
- The authored starting assignments, corridor and marks are stable in
  the documented mode. Exact arrival time and failure tick are unverified.

## Adjacent systems and history

- The scoped *Super Mario 64* stage also gives the player local camera
  and movement authority in a live space with pickups. Its primary
  actor obtains the Star after a summit encounter. Simian Acres
  instead uses a seated demolition tool to clear a different body's route.
- Escorting a proximity-controlled payload such as Marvel Rivals'
  Convoy does not explain this carrier, which neither waits for escort
  actors nor uses a team-contested rollback rule.
- Timing precision changes when a fixed corridor is replaced by a race
  clock or a player-authored route. The scope does not transfer those
  mechanics from timed replays or other missions.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-201`, `ACT-610` | local walking, occupied bulldozer control, camera |
| System Behaviour | `SYS-037`, `SYS-386`, `SYS-1560` | local units, removed geometry, independent carrier and collision |
| Constraint | `CON-426` | clear path before optional semi extraction |
| Information | `INF-523` | marks identify route obstructions |
| Objective | `OBJ-181`, `OBJ-299` | retained settlement and safe carrier corridor |
| Time | `TIM-003` | live advance while driving |

Canonical signature:

`ACT-008,ACT-201,ACT-610; SYS-037,SYS-386,SYS-1560; CON-426; INF-523; OBJ-181,OBJ-299; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `538` (`GAME-0001`–`GAME-0538`).
- Exact genome matches: none.
- Tied near matches: `GAME-0460` — Super Mario 64 (`4 / 19 = 0.210526`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0460` — Super Mario 64 | `ACT-008`, `ACT-610`, `SYS-037`, `TIM-003` | Both allow local actor movement, camera reframing and contact collection in a live stage. Mario reaches the summit for a direct boss encounter and subsequent Star contact. Blast Corps controls a bulldozer and operator to remove marked barriers before a separately advancing carrier reaches them. | Tied near (`0.210526`) |

### Preserved research notes

- New genes: `SYS-1560`, `INF-523`, `OBJ-299`.
- Classification result: `New gene`.
- Evidence and reasoning: carrier movement and failure, identification
  of route obstructions, and the success predicate separate from ordinary
  destructibility and optional stage credit.

## Taxonomy impact

- Registry changes: eight definitions reused, three Active additions.
- Taxonomy-change record: [TAXONOMY_CHANGE_286](../../../research/taxonomy-changes/TAXONOMY_CHANGE_286.md).

## Negative results

- The carrier is not a player vehicle. Stopping the bulldozer without
  pausing the game does not turn the corridor into a patient queue.
- A clean corridor is sufficient for primary success. Clearing every
  building, finding every unit or retrieving the optional car are
  not required.
- The approach does not establish a fixed numeric countdown, an exact
  impact threshold, contact with the player vehicle or collision order
  under same-frame inputs.

## Delta summary

## New facts

- [Observation | Corroborated | High] Each required obstruction has
  a local deadline driven by the carrier's live progress.

## New genes

- [Observation | Corroborated | High] Three additions in
  `TAXONOMY_CHANGE_286`.

## New combinations

- [Observation | Corroborated | High] No existing verified combination
  is a proper subset of the recorded genome.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_286`.

## New questions

- What exact effect does a same-frame building break have on a
  simultaneously arriving carrier on original North American hardware?

## Next recommended game

- [Hypothesis | Limited | Medium] Scope the full iPhone release of
  *Afterplace* to an opening exploration and encounter under Selection 042.
