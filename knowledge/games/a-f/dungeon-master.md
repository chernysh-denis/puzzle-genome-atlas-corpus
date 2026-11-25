---
game_id: GAME-0699
slug: dungeon-master
game_title: "Dungeon Master"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-072
    - ACT-089
    - ACT-920
  system:
    - SYS-112
    - SYS-1979
  constraint:
    - CON-892
  information:
    - INF-638
  objective:
    - OBJ-026
  time: []
---

# Game: Dungeon Master

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Inspect the champions where they stand, choose how to bring them into
the party, and lead the group past a floor-triggered barrier to the stairs.

## Analysis scope

- Version / ruleset: FTL's original English 1987 Atari ST commercial
  release. The catalogue records the 1.0 release family separately from
  later ST revisions. The evidence does not establish the exact edition
  of either recording's disk or their executable revisions.
- Structured analysis target: PLAT-ATARI-ST in
  [platform coverage](../../platforms/games.json).
- Entry: a fresh visit to the Hall of Champions after using Enter on
  the front door. Walk to an occupied mirror and select it before
  committing the first candidate.
- Primary decision loop: inspect equipment and skills, commit or
  cancel, and make further admissions only while the party has room.
  Move the party as one first-person position. With champions
  recruited, advance over the plate to open the iron grate. Read
  ordinary passage controls and optionally pick up provisions.
- Positive terminal: step onto the first downward stairs and arrive
  in Welcome. Stop at the arrival before the first fight.
- Included: candidate inspection, both documented intake options,
  the four-member cap, the visible leader hand, shared step and facing
  controls, the floor plate and linked grate, local wall-button doors,
  optional manual item pickup and first descent.
- Excluded: route before the first visited mirror, exact minimum-party
  plate test, the merits of individual champion builds, provision use,
  equipment swapping, formation and leader reassignment, spells,
  combat, saves, later floors, ports and differences between revisions.
- Potential scoped module: the first encounter in Welcome and the
  consequences of relocating party members within the shared formation.
- Direct-play status: no personal Atari ST session, binary comparison
  or input telemetry. The manual and the licensed guide were checked
  against a contemporary play account and short silent frame sequences.
  W1 is a French interface witness for route geometry only. W2 shows
  the English interface. Neither authenticates a retail disk revision.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DM-001 | Dungeon Master originated as a commercial Atari ST release by FTL in 1987. The original printed manual is in English. Neither video establishes its executable revision. | Confirmed | Corroborated | High | P1; S1, S2 |
| DM-002 | Selecting a particular champion mirror opens a preview with possessions and paired resource figures. Holding the eye control with an empty hand shows skills and attributes before a recruitment choice. | Observation | Corroborated | High | P1 pp. 2–4; W2 0:58–1:07 and 1:13–1:21 |
| DM-003 | Resurrection restores the authored identity and acquired skills. The manual documents reincarnation as trading those skills for physical attributes and requiring a new name. Cancel leaves the candidate unadmitted. | Observation | Corroborated | High | P1 pp. 2–4; S2; W2 1:01–1:11 and 2:30–2:39 for the offered modes and resurrection |
| DM-004 | Up to four champions may join the party. The handbook states that the fourth admission closes further candidate inspection. From the first admission the dungeon cursor becomes the leader's hand. | Observation | Corroborated | High | P1 pp. 2, 5; P2 p. 14; W2 1:06–1:11 and 2:30–2:42 |
| DM-005 | The shared position turns in quarter turns and steps one space along its current local axes. The party can use a nearby door control and pick up addressed objects, as separate inputs. | Observation | Corroborated | High | P1 pp. 5, 7; W2 3:00–3:07 and 4:27–4:36 |
| DM-006 | Advancing a recruited party over the Hall's floor plate opens its linked iron grate and allows the party to pass. No inventory key is used at that grate in the observed route. | Observation | Corroborated | High | P2 Level 1 map and solution A; S2; W2 2:55–3:01 |
| DM-007 | Reaching the first descending stairs beyond the grate brings the group out of the Hall and into the next floor named Welcome by the guide. | Observation | Corroborated | High | P2 pp. 14–15; W1 6:44–6:52 |

## Basic data

- Release / origin: FTL Games, original Atari ST commercial release,
  1987. English manuals and recordings supply the target interface.
- Mechanical families: FAM-017 for the authored dependency from
  recruiting a party through plate activation and passage to the stair.
- P1: [FTL's original Dungeon Master manual](https://www.mocagh.org/ftl/dm-manual.pdf).
  Printed pp. 2–7 cover portraits, inspection, both intake choices,
  the leader hand and six movement controls.
- P2: [Dungeon Master Adventurer's Handbook](https://www.mocagh.org/ftl/dm-hintbook1.pdf).
  Hall map and initial capacity on printed p. 14, Welcome on p. 15,
  and Level 1 Puzzle Solutions A on p. 47. Published guide independently
  specifies the plate-to-door dependency.
- S1: [Atari Legend release catalogue](https://www.atarilegend.com/games/dungeon-master).
  Lists FTL's 1987 original and distinguishes 1.0 and later ST versions.
- S2: [Michael A. Banks, Ancient Corridors, ST-Log 24](https://www.atarimagazines.com/st-log/issue24/48_1_ANCIENT.php).
  October 1988 play account, printed p. 48. Corroborates the choice
  of resurrection or reincarnation and stepping on the plate to admit
  the party past the iron grate.
- W1: [Wasabim's Atari ST route](https://www.youtube.com/watch?v=DGLkPY22pkg&t=404s).
  French interface, used to corroborate the geometry and arrival on the
  first stairs. Capture-specific language and revisions are distinguished.
- W2: [The Joy of Sticks' Atari ST session](https://www.youtube.com/watch?v=g3UdUWU4j1Y&t=58s).
  English interface. Shows the first candidate's review and resurrection,
  the growth of the party, the floor grate and optional preparations.
- Claim IDs: DM-001–DM-007.

### Reproducible fixture evidence

1. With the party still open, approach Halk's occupied mirror. W2
   shows the portrait at 0:58, the review near 1:01 and the skill and
   attribute panel near 1:04. Release the eye and compare the two
   recruitment choices. The different panels do not mean a second
   character has already joined.
2. Use resurrection. W2 shows the event and a named party status
   slot around 1:07–1:11. Continue until the desired party has been
   formed without exceeding four. W2 reviews Gothmog near 2:34 and
   resumes with four members by 2:38. The footage samples resurrection.
   For reincarnation and the fourth-member inspection restriction,
   follow the printed manual and handbook rather than inferring a
   visual experiment that those frames do not contain.
3. Turn and advance down the Hall route. At 2:57.0–2:57.5 in W2 the
   iron grate blocks the forward passage, with its plate in the
   approaching cell. It is visibly rising at 2:58.0–2:58.5 and the
   passage is clear by 2:59.0. At 3:00.0 the party has approached the
   wall beyond the open grate. P2 solution A and the period account
   supply the causal plate rule. This is not the later wooden door
   that W2 opens at its wall button around 4:30.
4. If preparing for the next floor, target reachable found objects
   with the leader hand and store them. W2 opens the party inventory
   after the grate and shows the collected food. The item pickup is
   optional for the transition under review.
5. Advance to the downward stairs. W1 shows the stair rails from
   above at 6:46 and the lower landing by 6:48. Step through only
   to the first landing and stop before the encounter in Welcome.

## Mechanical decomposition

### Action Genes

- ACT-008: advance the party's single position through corridor tiles
  using direct movement. A quarter-turn changes facing in place.
- ACT-072: press a reachable wall control on a normal door. This is
  separate from triggering the grate automatically with a floor step.
- ACT-089: select a reachable scene object such as food and carry it
  from the floor to the party inventory.
- ACT-920: inspect an occupied mirror and select an intake mode or
  cancel without taking that candidate.

### System Behaviour Genes

- SYS-112: the accepted floor contact opens the linked iron grate and
  permits the party to continue after leaving the trigger tile.
- SYS-1979: resolve the selected champion as their former identity and
  skill profile or as a newly named build with traded skills and attributes.

### Constraint Genes

- CON-892: the hall intake is capped at four; after filling the
  final slot the remaining champion reviews no longer open.

### Information Genes

- INF-638: inspect the candidate's equipment and resource values,
  and request the deeper view of skills and attributes before committing.

### Objective Genes

- OBJ-026: traverse the newly admitted route and reach the first
  landing in Welcome. Opening the gate is an intermediate condition.

### Time Genes

No separate time gene. The brief grate motion is not a documented
clock constraint for this fixture.

### Parameters

Champion identity, mode, starting attributes, number of open party
slots, local axes, fixture location, plate linkage and stair destination
are parameters.

## Reproducible transitions

| Entry state | Action | Expected next state | Evidence |
| --- | --- | --- | --- |
| Vacant party slot and reachable occupied mirror | Click mirror, then hold the eye | Candidate equipment and resource pairs, then deeper attributes and skills | DM-002 |
| Candidate preview open | Choose resurrection | Original identity and skill profile join the party | DM-003 |
| Candidate preview open | Choose reincarnation and confirm a new name | Renamed champion joins with reset proficiencies and changed attributes | DM-003, documented branch |
| Three members in the party | Admit the fourth member | Remaining candidate reviews become unavailable | DM-004 |
| Recruited party near the shut grate | Step onto the linked floor plate | Iron grate rises and allows further movement | DM-006 |
| Route past the grate is open | Advance onto the downward stairs | Arrival on the landing in Welcome | DM-007 |

## Strategic and experiential structure

Equipment and skill previews make an available body an informed
choice. Recruitment changes the party's later capabilities before any
fight occurs. The corridor then teaches different kinds of fixture
access: a direct wall action and a state change from movement itself.

## Replay and variation

A fresh front-door entry allows a different choice of initial champions
and modes. Their exact starting values, admission order, per-champion
bonuses and the empty-party result at the grate were not reproduced.

## Adjacent systems and history

The first arrival leads into equipment use, encounter timing and
formation positioning. The record stops before those systems determine
combat. The early ST evidence is not applied to later releases or ports.

## Normalised genome

- Action: ACT-008, ACT-072, ACT-089, ACT-920.
- System Behaviour: SYS-112, SYS-1979.
- Constraint: CON-892.
- Information: INF-638.
- Objective: OBJ-026.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `698` (`GAME-0001`–`GAME-0698`).
- Exact genome matches: none.
- Tied near matches: `GAME-0105` — Outer Wilds (`3 / 16 = 0.187500`); `GAME-0636` — The Dig (`3 / 16 = 0.187500`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Outer Wilds (GAME-0105)](../m-r/outer-wilds.md) | ACT-008, ACT-072, OBJ-026 | Both use direct movement and addressed controls before reaching a defined location. Outer Wilds requires learning the launch code from Hornfels and retains it after the world resets. Dungeon Master commits candidate choices, then opens the grate through local contact. | Near, `0.187500`. |
| [The Dig (GAME-0636)](../s-z/the-dig.md) | ACT-008, ACT-089, SYS-112 | Both control movement, collect addressed objects and operate a fixture with a retained effect. The Dig uses prepared objects and an authored mechanism to open the route. Dungeon Master fills a party from local candidates and advances onto the floor plate. | Near, `0.187500`. |

## Taxonomy impact

Reuse direct navigation, manual fixture activation, addressed pickup,
the persistent linked opening and reaching a designated location.
Add the candidate-specific intake action, inspection boundary, distinct
information preview and alternate intake consequences.

## Negative results

- Inspecting or cancelling the review leaves the slot uncommitted.
- The documented reincarnation branch is distinct from reviving a
  fallen member already in the party.
- No key or separate wall-button activation is evidenced for the iron
  grate. The later wooden door has a different control.
- The footage does not authenticate the exact revision or test the
  threshold for the smallest possible party at the grate.

## Delta summary

Nine genes cover an informed initial roster choice and two kinds
of local fixture access on the route to a clearly bounded arrival.

## New facts

- Two intake modes are offered for the same candidate with different
  starting proficiencies and identity.
- A full party also closes candidate-level information access.
- The plate-triggered grate and the manually addressed wooden door
  support different decisions during the same descent route.

## Principles and design implications

A capacity can govern information as well as admission. Before it is
filled, show the candidate-specific consequences of accepting a slot.
Follow that irreversible local choice with an observable fixture
dependency and a separate movement terminal.

## Puzzle or game generation potential

Place recruitable candidates at different reachable fixtures, each
with a pre-admission preview and two intake outcomes. Limit party
slots and model how the last slot affects preview availability.
Use a distinct movement-triggered barrier and a reachable next floor.

## New genes

- ACT-920
- CON-892
- INF-638
- SYS-1979

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 445](../../../research/taxonomy-changes/TAXONOMY_CHANGE_445.md).

## New questions

- Does each member's position change which first combat actions are
  legal after entering Welcome?
- Can the first grate be operated with the smallest legal party or
  with no champion in a separately reproduced original build?

## Next recommended game

Continue Selection 060 with GAME-0700, Planet of Lana II: Children of
the Leaf, on Nintendo Switch 2.

## Why this game

Its opening makes recruiting a character an embodied choice about
knowledge and capability before committing the party to its route.
