---
game_id: GAME-0710
slug: racing-destruction-set
game_title: "Racing Destruction Set"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-926
    - ACT-927
  system:
    - SYS-036
    - SYS-515
    - SYS-1992
    - SYS-1993
    - SYS-1994
  constraint:
    - CON-895
  information:
    - INF-131
    - INF-208
  objective:
    - OBJ-257
  time:
    - TIM-003
---

# Game: Racing Destruction Set

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Prepare a circuit, set the next race's gravity and lap count, and
drive through ramps and changes of surface to the classified result.

## Analysis scope

- Version / ruleset: English 1985 Electronic Arts commercial Commodore
  64 disk. Manual rules and C64-attributed footage delimit the
  version. Exact disk signatures, clock rate and joystick inputs are
  unverified. Normal, Racing, Earth and three laps in the main witness.
  Novice is the displayed setting for the yellow computer opponent.
- Structured analysis target: PLAT-COMMODORE-64 in
  [platform coverage](../../platforms/games.json).
- Entry: pre-race options with a course in memory. Set three laps
  and leave the observed Earth gravity and Normal Racing settings in
  force. The main witness does not show the loaded course name.
- Primary decision loop: prepare a connected course and its race
  options, start the selected route, then adjust speed and side
  steering for bends, ramps and road surfaces. Complete the required
  crossings of the start and finish section before the rival.
- Positive terminal: the results screen reports a red win and separate
  times. Stop before answering the replay prompt.
- Included: the active course's height, surface and route, pre-race
  configuration, live lane guidance and loss of alignment, separate
  laps and normal result. The custom-course witness establishes the
  preceding editing and preparation rules on a different circuit.
- Excluded: damage and item rules in Destruction, a disabled rival's
  exceptional finish rule, vehicle tuning, persistent time records
  after reload, handling coefficients, two-player controls, the
  Atari version and tape-specific distribution behaviour.
- Potential scoped module: use the same car, tyres and layout at
  two gravity settings and compare its response at one selected jump.
- Direct-play status: no personal Commodore 64 or emulator session,
  disk validation or input telemetry. The manual supplies rules and
  two complementary C64-attributed traces show an edited course and
  one completed race. The editor trace has cut loading breaks and
  ends during driving. The separate extreme jump witness changes
  several settings at once. All frame inspection excluded the audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RDS-001 | Electronic Arts released the English Commodore 64 game in 1985. The original disk rules use one or two players and red and yellow split views. | Confirmed | Direct | High | P1 pp. 1–2; P2 |
| RDS-002 | Before the race, the options expose separate difficulty, computer pace, rules, gravity, lap target and graphics. W1 shows the lap target change to three with Earth, Normal and Racing retained. | Observation | Corroborated | High | P1 pp. 2–3; W1 0:03–0:16 |
| RDS-003 | Select a reusable section, change its permitted height, width or surface and place it on the course. The editor flags incompatible joins and allows a temporary placement. The finished route needs connected ends with matching width and height and a start and finish section with cars. | Observation | Corroborated | High | P1 pp. 5–7; W2 3:20–3:34, 5:37–5:46 |
| RDS-004 | The game prepares the custom layout accepted in the editor before its cars can drive it. The manual also assigns saved gravity, laps and graphics to a loaded course while leaving current difficulty, rival pace and rules in force. That setting restoration is documented, without a controlled save/load comparison in the footage. | Observation | Corroborated | High | P1 p. 5; W2 5:37–7:44, 7:44–8:10 |
| RDS-005 | Forward and back control acceleration and braking. Side input addresses a lane relative to the driver when one exists. Straight-ahead lane following can fail at speed on bends and jumps. Surface grip and race gravity affect jump and landing response. | Observation | Corroborated | High | P1 pp. 1–4; W1 0:52–1:07; W3 0:05–0:24 under several changed variables |
| RDS-006 | On W1's configured run the two cars take separate paths through the raised section and the pale panel; they re-encounter the panel on a later pass. Captured heading and path change with the geometry. The footage cannot isolate the effect of one material or one control. | Observation | Direct | High | W1 0:53–1:06 and 1:47–1:55; P1 pp. 1, 3 |
| RDS-007 | Each car has its own lap count and a start and finish crossing reduces it. One car can stop after finishing while the other is still driving. In the ordinary case both finishes precede the result. | Observation | Corroborated | High | P1 pp. 1–3; W1 3:06–3:16 |
| RDS-008 | W1 classifies red first at 2:13.40 and yellow at 2:20.00. The best-time field equals the red time in this result. The screen offers another race. | Observation | Direct | High | W1 3:16–3:21 |

## Basic data

- Release / origin: Electronic Arts, 1985 Commodore 64 disk. The
  original box and manual credit Rick Koenig, Connie Goldman and
  David Warhol.
- Families: FAM-005 for building a connected race route and FAM-007
  for ramp, gravity and contact effects on a moving car.
- P1: Electronic Arts original English manual, scanned
  [driving and finish](https://c64sets.com/racing_destruction_set/rds_man01.jpg),
  [modes](https://c64sets.com/racing_destruction_set/rds_man02.jpg),
  [gravity, laps and vehicles](https://c64sets.com/racing_destruction_set/rds_man03.jpg),
  [course loading and placement](https://c64sets.com/racing_destruction_set/rds_man05.jpg),
  [joins and modification](https://c64sets.com/racing_destruction_set/rds_man06.jpg) and
  [course acceptance](https://c64sets.com/racing_destruction_set/rds_man07.jpg).
- P2: [Electronic Arts C64 package front](https://c64sets.com/racing_destruction_set/rds_pkg01.jpg)
  and the [original manual copyright page](https://c64sets.com/racing_destruction_set/rds_man00.jpg),
  cross-checked against the [C64 catalogue release record](https://www.mobygames.com/game/10399/racing-destruction-set/releases/).
- W1: [The Classic And Retro Gamer, C64 options and complete race](https://www.youtube.com/watch?v=yx9hxXN6vdE&t=4s).
  The opening settings, distinct terrain passes and race settlement
  are traceable. The starting course name and hardware are not shown.
- W2: [Ponder's Retro Goodness, MiSTer FPGA C64 track construction and race](https://www.youtube.com/watch?v=GEj8VyhTu8A&t=199s).
  A figure-like custom circuit inspired by Cruising on Broadway.
  The later save prompt shows the name cruising. The creator identifies
  red as the driven car and notes cuts during disk loading. The edited
  upload ends before the race result.
- W3: [Fred Sloniker, C64 extreme ramp capture](https://www.youtube.com/watch?v=VM_P39DM0pc).
  The creator reports low gravity, severe difficulty and a fast car.
  This supports the possibility of a long departure in that combined
  setup. No single-option comparison follows from it.
- Claim IDs: RDS-001–RDS-008.

### Reproducible fixture evidence

1. W1 at 0:03–0:16 shows the Race Options page and Earth, Racing,
   Normal and Novice selections. The selected lap target becomes 3.
   Start Race leads to the side-two disk prompt and the split
   views at about 0:22.
2. Follow the red and yellow cars through the approach at 0:53–1:06.
   The cars pass the inclined dark tiles, ochre sections and pale
   gridded section at different times. The path adjusts as the road
   bends. The same feature recurs at 1:47–1:55.
3. At 3:06–3:15 the red view is already stationary near the finishing
   straight while yellow still approaches its finish. At 3:16–3:21
   read red's 2:13.40, yellow's 2:20.00 and the replay question.
4. For the separate authoring fixture, select a jump at W2 3:20–3:24.
   Trying the flat replacement elicits Modify or Drop. The return to
   a shaped preview is visible at 3:28–3:34. The finished start piece
   has vehicles around 5:40. At about 6:02 the save prompt reads
   cruising and by 6:08 the race command is reached.
5. Continue W2 through the sequence of track parts drawn before
   the start, the computer checking jumps around 7:40 and the
   two live car views from approximately 7:44. The race uses the
   prepared section geometry. Use W1 for settlement.

## Mechanical decomposition

### Action Genes

- ACT-290: directly accelerate, brake and steer the assigned red car.
  Lane movement responds to the driver's left and right.
- ACT-926: configure global gravity and the required number of laps.
  The main witness raises the lap target to three.
- ACT-927: select, modify and place reusable straight, turn, crossing
  or jump sections while working on the editable circuit.

### System Behaviour Genes

- SYS-036: speed, collision and forces still affect motion as the
  car follows and leaves raised or curved road geometry.
- SYS-515: in the solo setup the yellow car drives the same course.
  The manual defines distinct pace settings for that opponent.
- SYS-1992: prepare the accepted section map for driving before
  installing the live competitors.
- SYS-1993: keeping a lane, running wide or leaving road contact
  depends on steering, speed, the configured gravity and the current
  geometry and surface. Ordinarily the road guides straight inputs.
- SYS-1994: separate lap counts advance on accepted crossings.
  The ordinary result follows both finishes.

### Constraint Genes

- CON-895: connected section ends need matching heights and widths.
  At least one start and finish section has to place the competitors.
  Mismatches can appear in intermediate drafts.

### Information Genes

- INF-131: the enlarged road preview and warnings expose how the
  selected section fits and which change can resolve an invalid join.
- INF-208: the post-race panel exposes the winner and both times
  alongside the current best-time value and replay choice.

### Objective Genes

- OBJ-257: finish one configured standalone race ahead of its
  rival and reach the classified result.

### Time Genes

- TIM-003: the cars continue through the route while steering and
  braking decisions are made. The editor can be used before starting
  the live simulation.

### Parameters

Section type, endpoint height and width, selected surface, starting
placement, shared gravity, selected difficulty and rival pace, lap
target, individual crossings and elapsed times. The exact lane count,
threshold speeds, traction coefficients, host timing and persistence
of best time beyond this result are unverified.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Active course in memory | Select three laps and return to Start Race | The next race uses the configured target with Earth gravity retained | RDS-002 |
| One planned custom join is incompatible | Attempt to place the selected section | The editor exposes the discrepancy and offers modification or temporary placement | RDS-003 |
| Accepted custom layout with starting cars | Request the race | The game processes each section, then starts driving on the prepared course | RDS-004 |
| Red car before a bend or raised segment | Steer and adjust speed as the surface changes | The car continues along the section with direction and contact affected by the local course | RDS-005–RDS-006 |
| Both cars hold their own unfinished lap count | Cross the start and finish section in an eligible pass | Only the passing car's count reduces | RDS-007 |
| Red has finished and yellow is still racing | Yellow finishes | Red Wins, separate times and the replay prompt appear | RDS-007–RDS-008 |

## Strategic and experiential structure

A road section is a decision in two places. In the editor it must
fit its neighbours. During a run its grade, turn and surface affect
the approach and the path taken by the car. The same geometry can
be tried with a different gravity option. Winning is a separate
condition evaluated from the configured laps and each car's finish.

## Replay and variation

The two main traces cover different layouts. W1 gives a completed
race on a mixed-surface layout. W2 shows a custom layout through
construction and the first driven pass. The absolute times apply
to W1 and do not transfer to the custom course or to other settings.

## Adjacent systems and history

The manual describes the Demo preset as Earth gravity with two laps.
The main witness's three-lap selection demonstrates an override.
The footage is missing the course name, so the main route is not
identified as Demo. Combat loadouts, persistent vehicle designs
and authored routes with additional start and finish sections
are separate modules.

## Normalised genome

- Action: ACT-290, ACT-926, ACT-927.
- System Behaviour: SYS-036, SYS-515, SYS-1992, SYS-1993, SYS-1994.
- Constraint: CON-895.
- Information: INF-131, INF-208.
- Objective: OBJ-257.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `709` (`GAME-0001`–`GAME-0709`).
- Exact genome matches: none.
- Tied near matches: `GAME-0677` — Stunt Car Racer (`4 / 20 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Stunt Car Racer (GAME-0677)](../s-z/stunt-car-racer.md) | ACT-290, INF-208, SYS-036, TIM-003 | Both directly control a car through live ramp and landing physics, then show a race result. The Little Ramp fixture uses a finite boost on a fixed elevated track and settles separate league credits for the win and best lap. Racing Destruction Set prepares the editable section map, applies configured race gravity and counts both cars' finishes in a standalone race. | Near, `0.200000`. |

## Taxonomy impact

Reuse direct driving, live physics, autonomous opponents, build and
result feedback, standalone placement and real time. Add six
boundaries for setting up the race, editing connected sections,
accepting geometry, preparing the course, resolving guided lanes
and counting both racers' laps through settlement.

## Negative results

- A stored or accepted layout is not yet a live race.
- An incompatible road join can appear before editor acceptance.
- Changing the scenery option supplies no evidence that gravity
  has changed. The options occupy distinct controls.
- The main witness ends with two elapsed times. No reward, trophy,
  continuation to another circuit or persistence after reloading
  is established by that screen.
- The extreme jump provides insufficient evidence for a gravity
  coefficient because several variables changed simultaneously.

## Delta summary

One course is a fitted circuit during editing and a sequence of
speed and contact decisions once prepared for racing. An explicit
lap target bounds the live race and its independent finish results.

## New facts

- Matching the heights and widths at adjoining ends is required
  when leaving the editor with a complete circuit.
- Normal lane following coexists with disrupted paths at high
  speed, ramps and bends.
- The ordinary results panel waits until both racers settle.

## Principles and design implications

Expose the geometry that makes a draft acceptable. Preserve that
geometry into a driving mode where the entrant can feel differences
between successive sections, then show each competitor's finish as
a separate measured result.

## Puzzle or game generation potential

Create a small track editor with recurring straight, turn and ramp
parts. Check neighbouring endpoints and a start section before
preparing the playable layout. Keep gravity and race length as
independent setup choices. Test one race that remains live after
the first racer finishes and then displays both times.

## New genes

- ACT-926
- ACT-927
- CON-895
- SYS-1992
- SYS-1993
- SYS-1994

## New combinations

None. The complete scan supports no verified subset.

## Taxonomy changes

[Taxonomy Change 456](../../../research/taxonomy-changes/TAXONOMY_CHANGE_456.md).

## New questions

- How does the same car land after one documented ramp at Earth
  versus another gravity setting with approach inputs held constant?
- Which combinations of surface and tyre selection change the
  onset of running wide on a fixed turn?

## Next recommended game

Continue Selection 061 with ELOH, the Android Google Play commercial
base game. Follow one early solution from repositioning percussion
blocks through the required projectile route to acknowledged completion.

## Why this game

The configurable length, fitted road joins and timed finishes make
it possible to trace an editable circuit into a complete driving event.
