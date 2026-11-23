---
game_id: GAME-0578
slug: outrun-2
game_title: OutRun 2
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-290
  system:
    - SYS-045
    - SYS-320
    - SYS-1204
    - SYS-1256
    - SYS-1698
  constraint:
    - CON-068
  information:
    - INF-204
    - INF-456
  objective:
    - OBJ-002
    - OBJ-270
  time:
    - TIM-003
---

# Game: OutRun 2

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Read the road while the clock runs, carry speed through bends, and
choose the next timed section by steering into its branch.

## Analysis scope

- Version / ruleset: English North American 2004 retail disc for the
  original Xbox. Select solo OutRun Arcade, then OutRun Mode, with
  automatic transmission and ordinary unmodified local settings.
  The Ferrari 360 Spider is the declared reproducible car selection.
  Installed executable revision and fine handling constants are unverified.
- Structured analysis target: PLAT-XBOX in
  [platform coverage](../../platforms/games.json).
- Entry: from the ordinary Palm Beach grid after choosing the mode,
  car, transmission and music. Music and paint are cosmetic parameters.
  The witnessed reference is the all-left Goal A route through Deep
  Lake, Castle Wall and Cloudy Highland to Tulip Garden. The alternative
  branch input is within scope at each junction.
- Primary decision loop: read remaining time, upcoming curvature and
  traffic, then steer, accelerate, brake or start a slide. Choose the next
  section by driving through the fork and reach the ordered checkpoint to
  extend the running allowance. Repeat through the fifth section.
- Positive exit: reach the selected fifth-section goal while time
  remains and show the route and performance result. There is no required
  place among surrounding cars.
- Negative exit: exhaust the authoritative time allowance before a qualifying
  checkpoint or final goal. A collision slows the drive and can cause
  later expiry, rather than directly deciding failure. Exact same-tick
  ordering and the last displayed second are not established.
- Included: direct steering and speed control, the automatic-transmission
  drift sequence, reversing a live slide, road and traffic contact,
  live fork selection, ordered time additions, time failure, steering
  telemetry and route/performance reporting.
- Excluded: OutRun Challenge missions and unlocks, Heart Attack requests,
  Time Attack ghosts, local and Xbox Live opponents, bonus racecourses,
  manual-shift techniques, arcade operator settings, OutRun 2 SP and
  OutRun 2006: Coast 2 Coast.
- Potential scoped modules: one authored Heart Attack request sequence
  or a complete OutRun Mission with a distinct success rule.
- Direct-play status: not conducted. The English Xbox booklet establishes
  mode, input and expiry; same-platform storyboard stills corroborate the
  route, time extensions, visible slide and finish. The recording has
  no verified disc region, patch identifier or input trace. No console,
  motion playback or audio playback was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| OX-001 | The original Xbox retail port shipped in North America in October 2004. The English booklet distinguishes solo OutRun Arcade and its OutRun Mode from Challenge and Xbox Live. | Observation | Corroborated | High | P1, P2, R1 |
| OX-002 | The run begins at Palm Beach. Four live fork commitments lead to the fifth section and one of five goals. Goal A's all-left path is Palm Beach, Deep Lake, Castle Wall, Cloudy Highland and Tulip Garden. | Observation | Corroborated | High | P1, P3, R1, R2, W1 |
| OX-003 | The controller steers, brakes and accelerates. With automatic transmission, the authored steer-and-reapply sequence following accelerator release and braking produces a controllable slide. | Observation | Corroborated | High | P1, P3, R3, W1 |
| OX-004 | Opposite steering while sliding plus a throttle release and reapplication redirects the slide. A better line and conventional deceleration can be preferable in a bend. | Observation | Direct | High | P1 |
| OX-005 | Autonomous traffic shares the road as a contact and line-selection problem. A collision slows the car and costs time along the route. | Observation | Corroborated | High | P1, R3, W1 |
| OX-006 | A reached checkpoint extends the live allowance. Remaining time counts down through road sections and a missed deadline ends the run. Still sampling does not establish exact grant sizes, caps or equality-ordering. | Observation | Corroborated | High | P1, P3, R1, W1 |
| OX-007 | The scoped run presents driving telemetry, time, score and route feedback and emits a selected-goal result with separable elapsed time and score. There is no scored rival place required for that clear. | Observation | Corroborated | High | P1, P3, R1, W1 |

## Basic data

- Sega AM2 arcade design, Sumo Digital Xbox conversion and Microsoft Game
  Studios North American publishing. The commercial Xbox disc is the target.
- Mechanical families: FAM-007, continuous control of a car with momentum
  and road contact, and FAM-010, real-time pressure from traffic and the clock.
- P1: [Original Xbox manual, X10-70278](https://www.manualslib.com/manual/379177/Games-Microsoft-Xbox-Out-Run-2.html).
  Checked its route planner, default controller diagram, race display,
  solo mode, car and transmission pages and steering advice. The
  [text mirror](https://manualzz.com/doc/68148686/games-microsoft-xbox-out-run-2--outrun-2-manual)
  includes the manual’s drift and direction-change instructions.
- P2: [North American launch announcement](https://worthplaying.com/article/2004/10/27/news/20176-outrun-2-xbox-in-stores-now/).
  Contemporary home release, date, publishing credit and platform.
- P3: [Sega arcade operator manual](https://www.arcade-museum.com/manuals-videogames/O/Outrun-2-DLX_00004.pdf),
  printed pp. 24–25, 27 and 32. Corroborates the shared moving fork,
  time extension and braking drift. Cabinet hardware, operators' time
  settings and linked play do not establish Xbox rules.
- R1: [GameSpot October 2004 Xbox review](https://www.gamespot.com/reviews/outrun2-review/1900-6111602/).
  Confirms the ordinary first section, five-section routes and separation
  from modes with hearts and race competition.
- R2: [Kikizo contemporary Xbox direct-feed index](https://games.kikizo.com/news/200409/018.asp).
  Labels five complete home Arcade routes. The all-left route and
  alternatives from the same start were checked from the index text.
- R3: [Kikizo contemporary Xbox hands-on review](https://games.kikizo.com/reviews/xbox/outrun2.asp).
  Describes drifting at speed, the risk of contacting traffic, and
  the boundary between the ordinary drive and Xbox-exclusive missions.
- W1: [RacingGameArchive’s Xbox playthrough](https://www.youtube.com/watch?v=4viF9zFtepc).
  Inspected static storyboard stills from 1:10 to 6:20, including Palm Beach
  traffic, the timer rising between 2:10 and 2:20, extension banners near
  3:20 and 4:20, an angled drive with tire smoke around 2:50, and a Goal A
  finish near 6:20. These frames confirm visible states, not the hidden
  checkpoint arithmetic, input timings, collisions between samples or
  North American build identity. Later Heart Attack footage is excluded.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-290 is continuous control of the dedicated car, including steering,
  accelerator and brake. The scoped automatic choice removes gear-shift
  decisions from the live control loop (OX-003).

### System Behaviour Genes

- SYS-045 models autonomous moving traffic. Passing or avoiding it serves
  the live drive without requiring a place finish (OX-005).
- SYS-320 resolves car motion and contact; poor positioning can cost
  speed and time without an independent compulsory damage objective
  (OX-003, OX-005).
- SYS-1204 is the checkpoint extension of the through-running allowance.
  Carry and addition are supported by the shared arcade explanation and
  the uninterrupted visible extension feedback; exact limits and amounts
  remain unmeasured (OX-006).
- SYS-1256 commits one authored road successor through the car's position.
  No route is freely constructed or switched after the branch (OX-002).
- New SYS-1698 is the automatic braking slide and its direction change.
  It reorganises the car's live trajectory during acceleration.
  No stored boost or drift-specific win condition follows (OX-003, OX-004).

### Constraint Genes

- CON-068 distinguishes failing on authoritative deadline expiry from
  merely reporting elapsed time. Its replenishable allowance differs from
  a whole-race clock that never receives additions (OX-006).

### Information Genes

- INF-204 covers driving telemetry for steering and speed choice. INF-456
  covers the countdown, accumulated score, current route and the result.
  The screenshot evidence does not disclose future traffic or clock bits
  (OX-007).

### Objective Genes

- OBJ-270 requires finishing one selected terminal of the timed fork route.
  OBJ-002 is performance score alongside clear, with no asserted formula
  for passes or remaining time (OX-002, OX-007).

### Time Genes

- TIM-003 captures real-time traffic, car movement and clock progression
  during the drive. An options pause is outside the continuous driving
  state (OX-003, OX-006).

## Reproducible transitions

| Before | Action or event | Result to check | Claim IDs |
| --- | --- | --- | --- |
| Start at Palm Beach grid | Accelerate and steer while monitoring nearby cars | Controlled motion during the running clock | OX-002, OX-003 |
| Approaching a sharp bend with automatic transmission | Release gas, brake briefly, turn decisively and reapply gas | A steerable lateral slide instead of finishing the corner under ordinary braking | OX-003 |
| Already sliding into the first bend | Steer opposite and release then reapply gas | Redirect the slide for a reversing bend; no automatic boost payout | OX-004 |
| Traffic ahead or beside the car | Keep the chosen line into contact, or leave clearance | Contact decreases speed; a clear line preserves more time for the checkpoint | OX-005 |
| Approaching the first live fork | Drive through the left branch | Continue toward Deep Lake; a separate right-branch attempt continues toward Alpine | OX-002 |
| After committing the fork with time still available | Reach the next ordered checkpoint | The countdown receives an extension and driving continues | OX-006 |
| Insufficient time remains before a required line | Let the allowance expire without crossing | The attempt ends without a goal clear | OX-006 |
| Four left choices completed, time still available | Finish Tulip Garden | Reach Goal A with an elapsed-time and score result | OX-002, OX-007 |

## Strategic and experiential structure

Read the bend and traffic before committing to a slide. It can preserve
more pace through winding sections, but a cleaner line avoids contact and
may take less time. Forks change the next driving section without a menu or
clock reset. Time spent correcting one mistake reduces the allowance
available before the next extension. The observed all-left route is a
specific successful example, not a requirement to clear via Tulip Garden.

## Replay and variation

The same clock and live fork rules allow a return run with a different
branch sequence. The recorded reference goes left four times. A run taking
different branches can reach some of the same late stages after different
setup, so ending name alone does not identify the whole route.

## Adjacent systems and history

The Xbox booklet gives a separate gear-down method for manual transmission
and separates solo OutRun Arcade from the new home modes. Neither the
original arcade game's shoulder shift technique nor any distinct mission
requirements are imported.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-290 | Steering, throttle and brake |
| System Behaviour | SYS-045, SYS-320, SYS-1204, SYS-1256, SYS-1698 | Traffic, motion/contact, checkpoint, fork and drift inputs |
| Constraint | CON-068 | Remaining allowance and terminal expiry |
| Information | INF-204, INF-456 | Driving telemetry and timed route result |
| Objective | OBJ-002, OBJ-270 | One terminal goal and a separate performance score |
| Time | TIM-003 | Clock, car and traffic during live input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `577` (`GAME-0001`–`GAME-0577`).
- Exact genome matches: none.
- Tied near matches: `GAME-0481` — Out Run (`10 / 16 = 0.625000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0481` *Out Run* | ACT-290, SYS-045, SYS-320, SYS-1204, SYS-1256, INF-204, INF-456, OBJ-002, OBJ-270 and TIM-003. Both drives use the live clock, moving traffic and road contact, visible feedback, fork commitment, checkpoint extension and a branching finish with score. | The original arcade case follows the two-gear shoulder technique and distinguishes displayed zero from underflow. The Xbox case uses a steerable braking drift with automatic gears and terminal clock expiry. It records score without transferring the original scoring predicates. | `10 / 16 = 0.625000`; closest earlier match, with a different drift and expiry boundary. |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_324](../../../research/taxonomy-changes/TAXONOMY_CHANGE_324.md)
  admits one steerable braking drift on automatic transmission. All
  earlier gene definitions and signatures are preserved.

## Negative results

- Do not import SYS-1257 or CON-745 from the original arcade Out Run.
  Its short off-road suppression after shifting and reconstructed
  displayed-zero grace are outside this automatic Xbox packet.
- SYS-1595 in Ridge Racer Type 4 requires coasting to prepare a slide,
  with held release duration affecting strength. OutRun 2's automatic
  manual procedure introduces a brake and a separate reversal sequence.
- ACT-468 and SYS-892's held charge and release boost do not follow from
  the steerable slide. Traffic does not establish SYS-515 ranked rivals.
  Do not infer finish-score conversion or completed-pass formulas from
  the visible score and result screen.
- No mode, route label, car model or seconds-per-checkpoint becomes a gene.

## Delta summary

## New facts

- [Observation | Corroborated | High] The home OutRun Mode combines live
  branch commitment and a replenishable deadline with a controllable
  braking drift. One witnessed all-left drive reaches Tulip Garden.

## New genes

- [Observation | Corroborated | High] One new automatic drift boundary;
  eleven existing boundaries reused.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. The comparison section owns supported subsets.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_324.

## New questions

- A pinned native input trace could settle the exact checkpoint addition,
  finish-score components, contact recovery and same-tick time expiry.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0579, Is This Seat Taken? on Android.
- Optimisation criterion: shift from live, time-constrained road choice
  to a seat assignment with multiple interacting preferences.

## Why this game

- [Hypothesis | Limited | Medium] A full run carries the consequences of
  steering, contact and checkpoint timing across authored route choices.
