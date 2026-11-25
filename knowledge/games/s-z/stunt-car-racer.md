---
game_id: GAME-0677
slug: stunt-car-racer
game_title: "Stunt Car Racer"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-309
  system:
    - SYS-036
    - SYS-1946
    - SYS-1947
    - SYS-1948
    - SYS-1949
  constraint: []
  information:
    - INF-208
    - INF-624
  objective:
    - OBJ-226
  time:
    - TIM-003
---

# Game: Stunt Car Racer

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The circuit, opponents, reserve count, timer scale and awards are parameters.

## Analysis scope

- Version / ruleset: original English MicroStyle Amiga release, 1989.
  One Normal League Division 4 fixture on The Little Ramp. The primary
  trace is attributed to the Amiga release. Exact floppy revision and
  host configuration are unverified.
- Structured analysis target: PLAT-AMIGA in
  [platform coverage](../../platforms/games.json).
- Entry: select Single Player League from a fresh Division 4 position,
  enter a driver name and start the season. Continue from the first
  player fixture against Jumpin' Jack on The Little Ramp, shown as
  Race 3 of 6. The crane lifts the player's car onto the road.
- Primary decision loop: once released, steer and adjust acceleration
  or braking on the elevated course. Use the finite boost where the
  remaining road and next landing allow it. Read speed, reserve,
  lap pace, opponent distance and visible chassis condition, then
  adapt the next approach. Complete three laps and compare the
  winner and best-lap credits separately.
- Exit: the third lap produces a race win. Confirm the race time
  and best lap, the separate 2 and 1 league points, and the Division 4
  table after that fixture. Stop before driving The Hump Back.
- Included: single-rival driving, live steering and latched acceleration,
  limited boost, ramp and landing dynamics, crane release and documented
  fall response, two damage layers, relevant instruments, local race
  result and division credit.
- Excluded: practice, other tracks, later fixtures and promotion,
  Super League, other platforms, link play, saving or loading,
  precise control timing and physics coefficients, opponent steering
  code and exact rules for automatic alignment.
- Potential scoped modules: a deliberately failed landing followed
  by crane recovery, a race in which fastest lap and winner split,
  or the effect of carried chassis holes on a later fixture.
- Direct-play status: no personal execution or floppy inspection.
  The manual establishes controls, recovery, damage and points.
  AL82's Amiga-attributed trace shows the full race and standings.
  Gaming Exhibit's PAL Amiga 500 recording corroborates the initial
  fixture and visible race dynamics. Its track preview displays a
  Quartex marker, so it is corroboration for matching observed
  behaviour only. Neither recording verifies original disk bytes,
  hardware, control device or frame-accurate physical inputs.
  Frames were inspected in the background with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SCR-001 | The 1989 Amiga game is credited to Geoff Crammond and MicroStyle. The primary Amiga capture shows an English Single Player League menu, Division 4, and The Little Ramp against Jumpin' Jack. | Observation | Corroborated | High | P1, P2, W1 00:00–00:24, W2 00:35–00:57 |
| SCR-002 | Joystick direction steers the car and initially selects acceleration. The manual specifies that releasing the acceleration direction preserves propulsion until braking cancels it. It specifies a separate limited boost, and the recorded cockpit shows intermittent boost flames and a lower remaining reserve. | Observation | Corroborated | High | P1, W1 01:05–01:17 and 02:50–03:24 |
| SCR-003 | The opening crane moves the car from the side to a position above the starting road and releases it after a wait. The manual also specifies a crane return to a nearby suitable position after leaving the raised road, at a time cost. No fall was isolated in the primary run. | Observation | Corroborated | High | P1, P3, W1 00:23–00:47 |
| SCR-004 | Ramps and turns change the moving cockpit's attitude and road contact. The race progresses across the ramp and back onto a receiving section, with the rival visible ahead during the first pass. Exact launch speed and airborne steering limits are unknown. | Observation | Corroborated | High | P1, W1 01:10–01:19 and 03:00–03:10 |
| SCR-005 | The manual distinguishes a transient chassis crack from persistent holes caused by severe impacts. A hole increases crack progression when it meets the crack. A full-width crack wrecks the car. These failure and carryover branches were not deliberately exercised. | Observation | Direct | High | P1 |
| SCR-006 | The dashboard exposes the current lap, remaining boost, speed, signed relative distance, leader status, current lap time and observed best lap. The manual identifies the signs and indicators. | Observation | Corroborated | High | P1, P3, W1 01:05–01:19 and 03:36–03:44 |
| SCR-007 | AL82 beats Jumpin' Jack after three driven laps, with a recorded race time of 2:38.24 and best lap of 0:51.46. The result assigns both the 2-point race win and 1-point best lap to AL82, for 3 points and second place in the still-running division table. | Observation | Direct | High | W1 03:37–04:02 |
| SCR-008 | Race and best-lap credits can go to different drivers. The manual assigns both to the opponent of a driver who wrecks or retires before finishing. The ordinary trace shows the awards in separate result slots. | Observation | Corroborated | High | P1, W1 03:56–03:59 |

## Basic data

- Release / origin: Geoff Crammond, MicroStyle, 1989. English Amiga
  original rules. The US label Stunt Track Racer and later collections
  are distinct distribution identities outside this observed scope.
- Puzzle families: FAM-007 for speed and trajectory over physical ramps
  and FAM-010 for rival progress and landing decisions under live time.
- P1: [1989 operating instructions, English transcription](https://www.c64x.no/games/stuntcarracer_manual.php).
  Credits the original and lists Amiga-specific equipment and keys as
  well as controls, crane, damage and separate league awards.
  [Amiga-indexed transcription](https://www.lemonamiga.com/doc/stunt-car-racer/1570)
  corroborates the rules.
- P2: [Centre for Computing History Amiga collection record](https://www.computinghistory.org.uk/det/9302/Stunt%20Car%20Racer/).
  Collection identity and year. The MicroStyle credit is visible in
  the primary capture and on the original materials.
- P3: [Retro Games' Stunt Car Racer instructions](https://retrogames.biz/games/amiga/stunt-car-racer/).
  Licensed reissue documentation corroborates the dashboard, finite
  turbo, fall delay and race structure. It does not establish 1989 build parity.
- W1: [AL82 Retrogaming Longplays, credited Amiga recording](https://www.youtube.com/watch?v=FbUNoIUZ9l8).
  Original game credits, first fixture, complete monitored race and
  settlement, approximately 00:00–04:02.
- W2: [Gaming Exhibit, attributed PAL Amiga 500 recording](https://www.youtube.com/watch?v=njba3VIftfE&t=35s).
  Comparable starting fixture, crane and road motion. The marked carrier
  is not the basis for an unmodified floppy claim.
- Claim IDs: SCR-001–SCR-008.

### Reproducible race evidence

1. Select Single Player League. Enter a driver name and choose
   Start the Racing Season. W1 shows the menu by about 00:16.
   The Little Ramp is previewed around 00:21. The first player
   result is labelled Race 3 of 6, which is consistent with the
   manual's two computer-only fixtures within the six-race season.
2. In W1 from 00:23 to 00:47, observe the changing cockpit view
   with chains visible, the suspended release cue and the live
   start. The opponent is ahead early. The initial player
   accelerator input and exact hold are not recorded.
3. Approach the live ramps in the flow of steering and boost.
   At about 01:07–01:10 the exhaust shows boost and the reserve
   decreases. From 01:11–01:19 the road crests, the forward
   view pitches, and the car continues on the next segment.
   At 03:00–03:10, the last lap again shows the ramp and the
   descending or receiving road. These frames support approach
   and landing as distinct states, not a numeric speed threshold.
4. The end of lap three enters the race-won state at about 03:40.
   Continue past the end prompt. Around 03:54 the local
   record screen shows race 2:38.24 and best lap 0:51.46.
   The result at 03:56 has separate winner and best-lap slots.
5. In the table at 04:00 AL82 has one race, one win, one best lap
   and three points. Road Hog leads with five, and Jumpin' Jack
   has one point. The next fixture preview is the boundary beyond
   this record.

## Mechanical decomposition

### Action Genes

- ACT-290: steer, accelerate and brake the assigned car directly.
  SCR-002, SCR-004.
- ACT-309: spend a finite boost reserve for directed acceleration
  on the route. SCR-002.

### System Behaviour Genes

- SYS-036: launch, continue moving and settle to a new road segment
  through continuous motion and contact. SCR-004.
- SYS-1946: retain an engaged forward throttle after the initiating
  acceleration command ends. Brake cancels it. SCR-002.
- SYS-1947: place and release the car by crane for the race start,
  and reuse spatial placement following an off-track fall under
  the documented fallback. SCR-003.
- SYS-1948: track reparable frame crack and persistent holes.
  A hole changes how quickly a passing crack grows. A completed
  crack retires the active car. SCR-005, SCR-008.
- SYS-1949: allocate independent win and fastest-lap points at a
  league result and apply the specified forfeit branch. SCR-007,
  SCR-008.

### Constraint Genes

None admitted. A safe approach depends on road geometry and driver
speed. Specific launch thresholds and checkpoint predicates are
not established for this Amiga fixture.

### Information Genes

- INF-624: show lap and rival separation, speed, remaining boost,
  live and best lap time and chassis damage during the active race.
  SCR-005, SCR-006.
- INF-208: present both recorded times and visible league result
  after the finish. SCR-007, SCR-008.

### Objective Genes

- OBJ-226: finish ahead of the opponent and carry local credits into
  the unresolved division season. SCR-007.

### Time Genes

- TIM-003: decide steering, braking and boost while both vehicles
  and the lap time progress. SCR-002, SCR-004, SCR-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| League start with the first player fixture | Begin the race on The Little Ramp | Crane brings the car above the circuit and releases it | SCR-001, SCR-003 |
| Forward motion selected | Release the initiating input without braking | Forward acceleration persists under the documented controls | SCR-002 |
| Moving on a suitable approach with boost remaining | Apply boost, cross a crest and return toward the road | Speed and trajectory change while the reserve decreases | SCR-002, SCR-004 |
| Active rival race after two completed laps | Complete the third lap ahead | Race-won state and record times | SCR-007 |
| Confirmed race result | Advance through the result panels | Independent win and best-lap credits, then the updated league table | SCR-007, SCR-008 |
| Car falls outside the elevated road | Documented crane placement and new drop | Nearby road position at a time cost | SCR-003 |
| Crack reaches the opposite side of the chassis | Terminal wreck under the manual's rule | Retire active car and route both awards to opponent | SCR-005, SCR-008 |

## Strategic and experiential structure

Boost trades a finite reserve for speed and changes the next ramp
approach. The fastest possible crest approach need not produce the
best next contact. In the observed race the quickest lap and the
win go to the same driver, and the league counts both separately.

## Replay and variation

The manual's fall recovery differs from a race restart because the
return is attached to the current road position and loses time.
The separate damage exception, in contrast, ends the attempt when
the chassis crack crosses the entire indicator. The primary witness
is a successful finish and is not a test of either failure path.

## Adjacent systems and history

The same division includes The Hump Back. Practice, persistent
Hall of Fame data, season promotion and Super League tuning are
outside this one league fixture, even if accessible from the menus.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-290, ACT-309 | Drive and spend finite boost |
| System Behaviour | SYS-036, SYS-1946, SYS-1947, SYS-1948, SYS-1949 | Simulate contact, retain throttle, crane-place, damage and award |
| Constraint | none | No separate checkpoint or speed threshold admitted |
| Information | INF-208, INF-624 | Expose results and the cockpit's live state |
| Objective | OBJ-226 | Win this fixture and carry the credit |
| Time | TIM-003 | Drive while rivalry and lap time progress |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `676` (`GAME-0001`–`GAME-0676`).
- Exact genome matches: none.
- Tied near matches: `GAME-0384` — F-Zero GX (`5 / 23 = 0.217391`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [F-Zero GX (GAME-0384)](../a-f/f-zero-gx.md) | ACT-290, ACT-309, INF-208, OBJ-226, TIM-003 | Both directly steer and spend finite boost in live time and carry the race win into a larger event. F-Zero GX gates boost until lap two and uses one energy reserve for boost and damage. Stunt Car Racer has a separate boost stock, crane placement and two chassis damage layers. Its league awards the fastest lap independently of the winner. | Near, `0.217391` |

## Taxonomy impact

Five admissions separate live cockpit information, retained throttle,
crane placement, layered chassis damage and independent league
awards. Six existing rules cover driving, boost, dynamics, result
display, local race success and live progression.

## Negative results

- A fastest lap is not the entire race result. The two awards are
  separate even when both go to one driver.
- An off-track recovery is not continuous safety. The documented
  delay leaves the rival race active.
- The successful race and its timer do not establish a universal
  minimum launch speed, frame timing or AI steering rule.

## Delta summary

Eleven genes, five new and six reused. The record follows the original
Amiga's first player fixture through the Division 4 points receipt.

## New facts

- A rising reserve cost and the next landing compete for the same
  decisions about speed.
- Unlike the race-local crack, structural holes can carry over and
  affect crack propagation, according to the original manual.
- The local win and best lap both credit the ongoing standings.

## Principles and design implications

Separate the fastest performance over a lap from winning the complete
fixture. A fast launch is only useful when landing geometry lets the
driver carry the speed into the next region.

## Puzzle or game generation potential

Design an original short elevated circuit with varied ramp angles and
a finite burst reserve. Compare safe high-speed routes, find the next
landing in each case, and track fastest-lap and race results separately.

## New genes

- INF-624
- SYS-1946
- SYS-1947
- SYS-1948
- SYS-1949

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 423](../../../research/taxonomy-changes/TAXONOMY_CHANGE_423.md).

## New questions

- Which collision classes in this fixture leave a permanent hole?
- When can a deliberately interrupted approach recover without losing
  the fastest-lap credit?
- How much time is lost to a crane recovery just after the last bend?

## Next recommended game

Continue Selection 058 with `GAME-0678`, Metroid Prime 4: Beyond,
Nintendo Switch 2 Edition. Isolate one early psychic interaction and
verify its effect on an authored fixture.

## Why this game

A bounded early race makes approach speed, support, damage and
two independent standings credits visible in one sequence.
