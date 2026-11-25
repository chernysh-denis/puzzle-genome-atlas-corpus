---
game_id: GAME-0674
slug: wave-race-blue-storm
game_title: "Wave Race: Blue Storm"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-720
    - ACT-899
  system:
    - SYS-1501
    - SYS-1935
    - SYS-1936
    - SYS-1937
    - SYS-1938
    - SYS-1939
  constraint:
    - CON-887
  information:
    - INF-208
    - INF-621
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Wave Race: Blue Storm

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Rider, track, point denominations and timing thresholds are instance parameters.

## Analysis scope

- Version / ruleset: English North American Nintendo GameCube disc rules,
  DOL-GWRE-USA, 2001. Solo Stunt Mode, Normal, Lost Temple Lagoon.
  The North American bilingual instruction booklet and the attributed
  English recordings delimit the rules. The installed revision, recording
  hardware and controller telemetry were not independently established.
- Structured analysis target: PLAT-NINTENDO-GAMECUBE in
  `knowledge/platforms/games.json`. Commercial disc. No championship
  play inside this attempt.
- Entry: select Normal and the already available Lost Temple Lagoon,
  take Nigel Carver in the primary trace and begin at the timed start
  line with a zero score. Track selection requires prior availability.
- Primary decision loop: steer and accelerate the watercraft over the
  live surface. Choose a line through the next scoring ring or ramp.
  Enter a context-appropriate stunt without spending too much of the
  current block's remaining time. Cross the required checkpoint arch
  before expiry, adding time credit and renewing the next time allowance.
  Preserve the consecutive ring bonus when practical and vary running stunts.
- Exit: cross the finish on the same lap with time remaining and
  inspect the ring, stunt and time subtotals, the new total and the
  name and record settlement. In the primary trace the result is
  11,149 points. The manual separately identifies expiry as an
  attempt-ending outcome that does not save accumulated points.
- Included: direct riding, the documented crouch for wave damping,
  moving water, context-specific stunt input, judged stunt score,
  reduced credit for repeated running stunts in a block, scoring-ring
  streaks, automatic turbo from Turbo Rings, timed physical gates,
  live feedback and the finished score breakdown.
- Excluded: unlock races, exact rider settings and physics constants,
  input timing calibration, complete stunt catalogue and point table,
  exact ring sensing volumes, Time Attack, multiplayer, reversed or
  other difficulty routes, Dolphin Park Trial, separately timed boundary
  recovery and persistent memory card format. Ordinary manual turbo
  meter management was not isolated from ring-triggered boosts here.
- Potential scoped modules: a reproduced expiry before a gate, a deliberate
  ring miss with the bonus reset measured, or a matched repeat of a surface
  trick to quantify the same-block penalty.
- Direct-play status: no personal console play or disc-byte verification.
  The North American booklet documents the controls and the Stunt Mode
  result rules. Good Old Days Gaming shows the complete primary Normal
  attempt, its score and the resulting local record. Zedra Psyborg
  independently reaches a score breakdown on the same Normal course.
  Still frames were read in the background without audio. The footage does
  not establish native input timing, capture hardware or regional binary parity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WBS-001 | The 2001 North American English GameCube edition is identifiable as DOL-GWRE-USA. It includes one-lap Stunt Mode distinct from the ordinary Championship and the Dolphin Park Trial. | Observation | Corroborated | High | P1 pp. 8, 21, 28, P2, P3, R1 |
| WBS-002 | Steering, acceleration and rider balance control the dedicated craft on a moving surface. Holding the crouch reduces wave effects. The first ring sits over the approach to a separate wooden ramp. | Observation | Corroborated | High | P1 pp. 6–7, P2, W1 00:52–00:56, W2 1:15:34–1:15:45 |
| WBS-003 | Passing a scoring ring pays its own value plus the current consecutive-pass bonus, which rises by 50 per prior consecutive ring. Missing resets the bonus and does not erase prior earned score. The first ring in W1 credits 50. | Observation | Corroborated | High | P1 pp. 21–22, W1 00:52–00:55 and 01:02–01:03 |
| WBS-004 | Passing the required arch while time remains renews the timer. Remaining time is credited at five points per tenth of a second. Failure to pass in time ends the attempt without saving its points. | Observation | Corroborated | High | P1 pp. 21–22, W1 00:58–00:59, 01:03–01:04, 01:19–01:21 |
| WBS-005 | The manual gives distinct running and airborne actions. A stick and sometimes B command produces a stunt in the relevant context. Successful execution pays by type and precision. W1's first ramp stunt adds 1,857 points. Repeating a running stunt in a block gives much less credit under the printed rule. | Observation | Corroborated | High | P1 pp. 22–25, P2, W1 00:54–00:57 |
| WBS-006 | A marked Turbo Ring can activate the temporary speed burst upon crossing, without waiting for a manual turbo command. One crossing leads into the next ramp approach. | Observation | Corroborated | High | P1 p. 21, W1 01:12–01:14 and 01:22–01:25 |
| WBS-007 | The live display identifies score, time and each class of credit, while the result separates rings, stunts and time. W1 shows 2,700 ring points, 7,164 stunt points and 1,285 time points. The ranked result saves the new 11,149 total after name entry. | Observation | Direct | High | W1 00:53–01:33 and 01:41–02:03, W2 1:16:55–1:17:06 |
| WBS-008 | The recorded finished runs establish the demonstrated route and outputs. They do not measure exact controller input, a controlled repeat penalty or the timer-expiry branch. | Observation | Limited | High | W1 and W2 scope, P1 pp. 21–25 |

## Basic data

- Release / origin: Nintendo Software Technology, published by Nintendo.
  English commercial North American Nintendo GameCube release, 2001.
- Families: FAM-007 for steering and launching a body on a moving
  surface and FAM-010 for the live deadlines on scoring decisions.
- P1: [Nintendo North American bilingual instruction booklet](https://archive.org/details/wave-race-blue-storm-manual-canada).
  English printed pp. 6–7 for throttle, tilt and crouch, pp. 21–22 for
  the one-lap rules, timed gates, ring sequences, repeated running stunts
  and scoring, pp. 23–25 for surface, ramp and airborne commands.
  The Canadian packaging scan documents the scoped North American rules.
- P2: [Nintendo UK product description](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Wave-Race-Blue-Storm-269347.html).
  Corroborates the craft's response to waves and the split between water
  tricks and jump tricks. Its release date refers to the UK.
- P3: [Nintendo's Japanese mode overview](https://www.nintendo.co.jp/ngc/gwrj/menu/index.html).
  Confirms a single lap and scoring from rings, stunts and timely
  progress. Names and parameters below use the English rules.
- R1: [North American GameCube product and package identification](https://rfgeneration.com/cgi-bin/getinfo.pl?ID=U-076-S-03181-A).
  Lists the 2001 disc edition, DOL-GWRE-USA packaging and publisher.
- W1: [Good Old Days Gaming, one Normal Stunt Mode route](https://www.youtube.com/watch?v=OcwubncZeCk&t=25s).
  Course choice, timed launch, finish, result and record entry.
- W2: [Zedra Psyborg, independent Normal attempt](https://www.youtube.com/watch?v=YqsGyOovHk8&t=4450s).
  Same course choice and score categories; a different rider and result.
- Claim IDs: WBS-001–WBS-008.

### Reproducible route evidence

1. At about 00:25–00:35 of W1, select the Normal Lost Temple Lagoon
   attempt. The initial course view shows a 9,162-point best.
   Nigel Carver is the selected rider shown at the result. At 00:52
   the watercraft is accelerating from the checked line with zero points.
2. Aim through the blue-white first ring toward the wooden ramp.
   W1 00:53–00:55 crosses it for 50. A jumping stunt then shows a
   1,857 credit at 00:56; the live score rises from 50 to 1,907.
   The precise command is sourced from the booklet rather than inferred
   from an uninstrumented recording.
3. At 00:58–00:59 cross the first arch before the clock expires.
   The time renewal and separate 375 credit appear. At 01:02–01:03
   the third ring shows 150 credit, including its streak bonus. The
   next arch adds 230 around 01:04. Point rings and arches are
   separately addressed physical targets.
4. At 01:12–01:14 enter the distinct Turbo Ring and take the ramp
   approach. Another such ring appears before the final ramp at
   01:22–01:25. Finish the lap instead of lingering for another
   surface stunt as the time approaches zero.
5. W1 crosses the finish around 01:32. The clock stops at 3.16
   seconds and the final visible sum reaches 11,149. The player
   result at about 01:44 reports 2,700 + 7,164 + 1,285.
   Name entry, a memory card write notice and the new first-place
   local score table follow around 01:45–02:02. Stop at the table.
6. An independent Normal route in W2 crosses the finish near 1:16:10
   and shows the same result categories around 1:17:02–1:17:03. Ricky
   Winterborn earns 1,200 ring points, 1,660 stunt points and 1,660
   time points for 4,520. No saved record is claimed in W2.

## Mechanical decomposition

### Action Genes

- ACT-290: directly steer and accelerate the assigned watercraft on
  the authored course. WBS-002.
- ACT-720: command the documented crouch to damp wave effect during
  a crossing. Exact W1 button presses were not visible. WBS-002.
- ACT-899: enter a discrete ordered stick command, sometimes with B,
  selected for the current surface or launch context. WBS-005.

### System Behaviour Genes

- SYS-1501: live waves and rider balance alter supported pitch and
  bounce. A physical ramp supplies separate airborne opportunity. WBS-002.
- SYS-1935: each recognised ring contributes its value plus the
  escalating consecutive-pass credit. Missing clears the bonus for
  future rings. WBS-003.
- SYS-1936: crossing the required gate with positive time renews the
  clock and credits the remaining time. WBS-004.
- SYS-1937: completed stunts award points by kind and execution
  precision. The credited score is separate from ring and time credits.
  WBS-005, WBS-007.
- SYS-1938: repeated running tricks in the same timed block receive
  reduced credit. This is the documented scoring rule; the reduction
  coefficient is unmeasured. WBS-005.
- SYS-1939: crossing a Turbo Ring directly activates transient speed
  boost. WBS-006.

### Constraint Genes

- CON-887: reach each checkpoint arch before its block clock
  expires. A missed deadline ends the attempt without retaining
  the earned score. WBS-004.

### Information Genes

- INF-621: the rider sees the current total, countdown, current speed
  and immediate numbered ring/stunt or time credits. WBS-003–WBS-007.
- INF-208: after a valid finish the breakdown exposes the separate
  contributions and achieved local record. WBS-007.

### Objective Genes

- OBJ-002: maximise the summed score during the one classified lap.
  A new record is a comparison result, not a mandatory passing score.
  WBS-001, WBS-007.

### Time Genes

- TIM-003: its active clock and moving craft continue between inputs
  until a gate renewal or terminal result. WBS-002, WBS-004.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Normal course and starting trace | Begin the start approach | Actively moving craft, live clock and zero score | WBS-001, WBS-002 |
| Scoring ring lies ahead | Ride through the opening | Credit its base value plus any current streak bonus | WBS-003 |
| Ramp or qualifying surface approach | Enter a context-appropriate command and complete the stunt | Score feedback for the recognised stunt | WBS-005 |
| Timed block active | Cross its arch before expiry | Pay remaining-time points and renew the running clock | WBS-004 |
| Turbo Ring lies on the selected line | Ride through it | Immediate temporary speed burst | WBS-006 |
| Final valid line reached before expiry | Ride through the finish and confirm the qualifying record | Ring, stunt and time totals, then local result | WBS-007 |
| Next gate remains unpassed as time expires | Let the block clock reach zero | Attempt ends, points are not saved under the booklet rule | WBS-004 |

## Strategic and experiential structure

A ring route can protect its escalating bonus while also setting up a ramp.
Taking a slower line to perform a stunt may cost time points or gate
eligibility. Holding a posture and choosing a fresh running stunt have
different costs. Automatic speed from the distinctive ring can be used
immediately for the following line but does not advance the checkpoint by
itself.

## Replay and variation

The primary run establishes one complete scored line. The independent
run shows how a different driver and lower-scoring route can still
finish the same course with the same result categories. Comparing the
rider profiles, higher difficulty routes and individual jump execution
would require independent controlled play.

## Adjacent systems and history

The prior [Wave Race 64 record](wave-race-64.md) concerns a competitive
Championship heat. The watercraft relationship carries across the
analysed releases, but the scoped Blue Storm run prioritises rings,
timed gates and stunts. The latter mode's rules are not evidence about
directional buoy progression in the former.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-290, ACT-720, ACT-899 | Drive, damp waves and submit a context-specific trick command |
| System Behaviour | SYS-1501, SYS-1935, SYS-1936, SYS-1937, SYS-1938, SYS-1939 | Live wave response, ring bonus, gate settlement, stunt scoring, repeat penalty and turbo |
| Constraint | CON-887 | Beat each physically gated time limit |
| Information | INF-208, INF-621 | Expose live decisions and final result |
| Objective | OBJ-002 | Maximise the classified score |
| Time | TIM-003 | Real-time inputs before gate and lap closure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `673` (`GAME-0001`–`GAME-0673`).
- Exact genome matches: none.
- Tied near matches: `GAME-0524` — Wave Race 64 (`5 / 24 = 0.208333`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Wave Race 64 (GAME-0524)](wave-race-64.md) | ACT-290, ACT-720, INF-208, SYS-1501, TIM-003 | Both directly control a craft over live waves with wave damping and a classified result. The older packet uses required sides of buoys to build and preserve engine power against a rival field. The Blue Storm packet uses ring streaks, executed stunts and per-arch time credit in one solo lap. | Near, `0.208333` |

## Taxonomy impact

Eight explicit boundaries separate contextual input, consecutively passed
rings, checkpoint timing, judged stunts, block-local repeat reduction,
ring-triggered turbo, deadline eligibility and live feedback. Existing
vehicle control, wave response, damping, objective and result/timing
boundaries remain in use.

## Negative results

- Point rings are score targets. The timed gate is an arch with a
  separate deadline and renewal condition.
- The assigned score sums rings, stunts and time. A best score is
  not a prerequisite for a valid finish.
- The one attempt does not establish every jump command, repeat
  penalty magnitude, recovery branch or comparative regional timing.
- Dolphin Park Trial is outside this Normal Stunt Mode track selection.

## Delta summary

Fourteen admitted genes. One Normal Lost Temple Lagoon Stunt Mode
lap from the gate start to its retained result.

## New facts

- Ring streak bonus, stunt precision and remaining-time settlement
  operate on the same live score without sharing a trigger.
- The first ring and ramp can be chained into the first stunt.
  A Turbo Ring is a separate path opportunity.

## Principles and design implications

Place a visible reward line beside a required physical deadline.
Make the cost of dithering visible in both the current clock and
the later points. Let varied stunt choices and a precise ring line
each reward a different aspect of the same route.

## Puzzle or game generation potential

A short timed traversal could expose an ordinary route, a streak
line and a ramp line. Position the required gates so that those options
are compatible at some speeds and in tension at others. Score each
event explicitly and reveal which route tradeoff produced the result.

## New genes

- ACT-899
- CON-887
- INF-621
- SYS-1935
- SYS-1936
- SYS-1937
- SYS-1938
- SYS-1939

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_420](../../../research/taxonomy-changes/TAXONOMY_CHANGE_420.md).

## New questions

- Does skipping one particular optional ring reset the streak as soon as
  the rider passes its plane or at a later route trigger?
- What score reduction applies to each repeated running stunt in a block?
- How do visibly rougher surfaces change a matched ramp line?

## Next recommended game

Teeny Tiny Trains on iOS. Follow one completed level with multiple trains.

## Why this game

It joins a physically executed stunt and decision loop to a precise,
independently auditable score and deadline structure.
