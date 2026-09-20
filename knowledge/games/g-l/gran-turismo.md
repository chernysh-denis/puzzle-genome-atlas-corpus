---
game_id: GAME-0316
slug: gran-turismo
game_title: Gran Turismo
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-290
  system:
    - SYS-320
    - SYS-914
  constraint:
    - CON-647
  information:
    - INF-204
    - INF-205
    - INF-251
  objective:
    - OBJ-184
  time:
    - TIM-003
---

# Game: Gran Turismo

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Mazda Demio,
licence B-1, 1,000 metres and 36 seconds are parameters, not gene names.

## Analysis scope

- Version / ruleset: the North American English original-PlayStation release
  `SCUS-94194`, published by Sony Computer Entertainment America on
  1998-05-12. The packet reconstructs launch-disc licence test B-1 from the
  original manual text, contemporary guides and official series history. No
  later Greatest Hits pressing, regional release, demo, sequel or remaster is
  treated as mechanically identical.
- Structured analysis target: original North American PlayStation optical disc
  `SCUS-94194`; see `GAME-0316` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the fixed straight, speed, elapsed time and
  stopping zone; accelerate the supplied Mazda Demio; choose the braking point;
  let vehicle speed, traction and stopping distance resolve; settle only when
  the complete car is stationary inside the goal area before the limit.
- Entry: licence centre B-1 immediately after the test releases direct control,
  with the supplied Mazda Demio stationary at the start and the timer beginning.
- Positive terminal: the first attempt in which the complete car stops inside
  the goal area 1,000 metres away at or before 36 seconds. The test reports an
  accepted result and returns to the licence-test result/menu state. This is
  one passed test, not the complete B licence.
- Negative terminal: exceeding 36 seconds, overrunning the goal area or
  otherwise leaving the declared test-valid state produces disqualification;
  an unfinished moving car has no accepted result.
- Included: direct throttle, brake, steering and camera-capable dedicated-car
  control; automatic transmission as fixed setup; continuous speed, traction
  and road contact; live speed, gear, course cue and timer; the 1,000-metre
  stopping area; binary pass/disqualification settlement; reported elapsed
  result.
- Excluded: tests B-2 through B-8 and complete B-licence award; A and
  International A licences; Quick Arcade; Sunday Cup and every rival race;
  purchasing, selling, garage, credits, tuning, car collection, prize cars,
  replays and repeat optimisation; manual transmission, neGcon, multiplayer;
  memory-card save/reload; all other regions, revisions, demos and sequels.
- Reproducible parameterisation: use North American `SCUS-94194`, English,
  original PlayStation rules, licence centre B-1, supplied Mazda Demio,
  automatic transmission and ordinary controller mapping. Accelerate from
  rest, release or brake at a chosen point and reach complete rest wholly
  inside the marked zone before the 36-second limit. Exact throttle modulation,
  braking point, steering correction and achieved time remain attempt
  parameters.
- Potential scoped modules: the complete B licence, Sunday Cup, simulation
  economy and tuning, Quick Arcade and memory-card persistence each require a
  separate entry, loop, terminal and evidence boundary.
- Direct-play status: not conducted. No original PlayStation, `SCUS-94194`
  disc, controller trace, memory card or installed/emulated executable was
  available. No ROM, disc image, video or audio was downloaded, opened, played
  or analysed. This is a source-bounded reconstruction, not a claimed run or
  save/reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GT1-001` | The first Gran Turismo launched for the original PlayStation in North America on 1998-05-12 | Confirmed | Direct | High | P1, P2 |
| `GT1-002` | The North American release identity is `SCUS-94194` | Observation | Corroborated | High | P3, S1 |
| `GT1-003` | The original manual exposes Gran Turismo and Quick Arcade as separate modes and maps steering, acceleration, braking, shifting, handbrake, view and pause controls | Confirmed | Direct | High | P3 |
| `GT1-004` | Licence B-1 supplies a Mazda Demio and requires starting, accelerating and stopping completely inside a goal area 1,000 metres away | Observation | Corroborated | High | S2, S3 |
| `GT1-005` | Overrunning the goal area or exceeding 36 seconds disqualifies B-1 | Observation | Corroborated | High | S2, S3 |
| `GT1-006` | The packet does not establish a complete B licence, Sunday Cup result or memory-card reload | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Polyphony Digital / Sony Computer Entertainment America;
  North American original PlayStation release on 1998-05-12.
- Platform or physical form: English North American PlayStation optical disc
  `SCUS-94194`, licence B-1 only.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [Gran Turismo official tenth-anniversary notice](https://www.gran-turismo.com/us/news/02_0004970.html),
    for the North American 1998 release and original-PlayStation identity.
  - **[P2]** [PlayStation history timeline](https://www.playstation.com/en-us/playstation-history/1994-ps-one/),
    for the original product's platform and driving-simulation identity.
  - **[P3]** [transcribed original Gran Turismo instruction manual](https://www.gamesurge.com/playstation/strategy/psx_man/Grant.shtml),
    for disc startup, modes, controller mappings and live driving display.
- Corroborating sources, accessed 2026-09-20:
  - **[S1]** [PSX DataCenter `SCUS-94194` catalogue record](https://www.psxdatacenter.com/games/U/G/SCUS-94194.html),
    for the printed serial, NTSC-U region and 1998-05-12 release date.
  - **[S2]** [contemporary Gran Turismo licence-test guide](https://gamefaqs.gamespot.com/ps/197468-gran-turismo/faqs/3913),
    for B-1's supplied car, distance, stopping-area condition and 36-second
    disqualification limit.
  - **[S3]** [Gran Turismo B-Class licence guide](https://gamefaqs.gamespot.com/ps/197468-gran-turismo/faqs/3919),
    for the B-test sequence and its separation from the later Sunday Cup.
  - **[S4]** [Prima's Official Strategy Guide catalogue](https://books.google.com/books/about/Gran_Turismo.html?id=ADNLj0J_lRoC),
    for the licensed contemporary guide identity and licence/racing coverage.
- Research record: **[R1]** local preflight on 2026-09-20 found no lawful
  original disc, console, installed executable, memory card or controller
  trace; direct play and reload were not performed.
- Claim IDs: `GT1-001`–`GT1-006`.

## Mechanical decomposition

### Action Genes

- `ACT-290` owns direct control of the assigned Mazda Demio: throttle, brake,
  steering and declared camera/handbrake controls. Automatic transmission is a
  fixed parameter rather than a separate action. Claims: `GT1-003`, `GT1-004`.

### System Behaviour Genes

- `SYS-320` integrates speed, traction, road contact and stopping distance.
  New `SYS-914` evaluates the bounded driving test: it accepts a fully stopped
  in-zone result within the limit and otherwise reports disqualification.
- Resolution order: accepted input changes throttle/brake state; vehicle motion
  and contact advance in real time; the timer advances; complete rest checks
  the car's relation to the zone and elapsed limit; the attempt then settles.
  Claims: `GT1-003`–`GT1-005`.

### Constraint Genes

- New `CON-647` requires the entire car to be stationary inside the marked goal
  area before the 36-second deadline. Crossing the zone without stopping,
  overrunning it or timing out cannot satisfy the test. Claims: `GT1-004`,
  `GT1-005`.

### Information Genes

- `INF-204` exposes speed, gear and the authored straight/goal cues; `INF-205`
  exposes live timed progress toward the fixed target; `INF-251` exposes the
  settled elapsed result separately from the running display. Claims:
  `GT1-003`–`GT1-005`.

### Objective Genes

- New `OBJ-184` owns the first accepted B-1 result: accelerate the supplied car
  across the fixed distance, stop wholly inside the goal area within the limit
  and reach the pass state. It does not grant the complete B licence. Claims:
  `GT1-004`–`GT1-006`.

### Time Genes

- `TIM-003` owns continuous vehicle motion and the running test clock while
  acceleration and braking decisions remain open. Claim: `GT1-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Mazda Demio is stationary at the B-1 start | Hold accelerate | speed rises under the assigned car's motion model while elapsed time advances | direct input and simulated acceleration | `GT1-003`, `GT1-004` |
| Car approaches the marked area at speed | Release throttle and brake | speed falls according to current motion until the car stops or passes the zone | braking point converts speed and distance into stopping position | `GT1-004` |
| Complete car stops inside the goal area by 36 seconds | Keep it stationary | the spatial and time predicates are accepted and a passed elapsed result is reported | positive test terminal | `GT1-004`, `GT1-005` |
| Car crosses beyond the goal area before complete rest | Continue or brake too late | the attempt is disqualified even if it later stops | crossing is not enough; full in-zone rest is required | `GT1-005` |
| Timer exceeds 36 seconds before a valid stop | Remain unfinished | the attempt is disqualified regardless of later position | fixed deadline bounds the test | `GT1-005` |

## Strategic and experiential structure

- Local decision: choose when to stop accelerating and how hard to brake.
- Medium-term planning: infer stopping distance from current speed and remaining
  straight rather than chasing speed alone.
- Long-term structure: none inside one attempt; the broader licence sequence is
  excluded.
- Common heuristics: accelerate cleanly, begin braking before the goal, avoid
  steering corrections that add distance, and prioritise valid rest over a
  faster overrun.
- Failure attribution: the visible clock, speed and stopping area make early
  braking, timeout and overrun legible consequences of the chosen timing.
- Player-trust factors: fixed car, distance, zone and deadline make the attempt
  comparable; exact hidden physics values are not claimed.
- Claim IDs: `GT1-003`–`GT1-005`.

## Replay and variation

- What changes between attempts: throttle duration, braking point, correction,
  elapsed time and final position.
- Randomness or procedural generation: none evidenced in the bounded test.
- Multiple viable strategies: several valid input timings may stop inside the
  area; only the first pass is in scope.
- Typical replay motive: improve the result or recover from disqualification,
  both excluded after the first accepted terminal.
- Claim IDs: `GT1-004`, `GT1-005`.

## Adjacent systems and history

- Direct predecessors: contemporary console circuit racers; no predecessor is
  claimed to share this exact licence-test boundary.
- Variants: Japanese and PAL releases, later pressings, demos and sequels are
  separate evidence targets.
- Similar games: *Trackmania* and *BeamNG.drive* also join direct car control,
  real-time physics and an elapsed result.
- Important differences: B-1 ends only when a fixed supplied car is fully
  stopped inside a spatial zone by a deadline; it has no route checkpoints,
  rivals, laps, seasonal medal map or campaign economy in scope.
- Claim IDs: `GT1-001`–`GT1-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290` | Mazda Demio; throttle/brake timing |
| System Behaviour | `SYS-320`, `SYS-914` | traction; stopping distance; pass/disqualification |
| Constraint | `CON-647` | 1,000 m zone; 36 s limit |
| Information | `INF-204`, `INF-205`, `INF-251` | speed; gear; timer; settled time |
| Objective | `OBJ-184` | first passed B-1 attempt |
| Time | `TIM-003` | real-time vehicle and clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `315` (`GAME-0001`–`GAME-0315`).
- Exact genome matches: none.
- Tied near matches: `GAME-0216` — Trackmania (`6 / 14 = 0.428571`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0216` — Trackmania | `ACT-290`, `SYS-320`, `INF-204`, `INF-205`, `INF-251`, `TIM-003` | Both directly drive one assigned car under a visible clock and report elapsed time. Trackmania validates ordered checkpoints and a finish, then maps any valid result to fixed map medals. Gran Turismo B-1 instead requires complete rest wholly inside one goal zone by a hard pass deadline; overrun or timeout disqualifies, and no full track, medal map or seasonal result enters scope. | Near, `0.428571` |

### Preserved research notes

- New genes: `SYS-914`, `CON-647`, `OBJ-184`.
- Classification result: `New gene`.
- Evidence and reasoning: existing timed-race genes require a finish or ordered
  route. B-1 evaluates a combined velocity-zero, spatial-containment and time
  predicate, and its positive objective is one passed skill test rather than a
  race or medal-bearing track finish.

## Taxonomy impact

- Registry changes: add `SYS-914`, `CON-647` and `OBJ-184`; extend supporting
  evidence for seven reused genes.
- Taxonomy-change record: none.
- Candidate terms affected: B-1, Mazda Demio, goal area and SCUS serial remain
  parameters or product labels.

## Negative results

- No separate negative-result record. `SYS-711`, `CON-438` and `OBJ-133` were
  tested and rejected: they require a valid track finish/waypoint sequence or
  treat slower finishes as completion, unlike B-1's stop-zone pass gate.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original North American PlayStation product and
  control identity are frozen as `SCUS-94194` (`GT1-001`–`GT1-003`).
- [Observation | Corroborated | High] B-1 requires the supplied Mazda Demio to
  stop completely in the 1,000-metre goal area within 36 seconds; overrun or
  timeout disqualifies (`GT1-004`, `GT1-005`).

## New genes

- [Observation | Corroborated | High] `SYS-914`, `CON-647` and `OBJ-184` isolate
  driving-test evaluation, the timed stopping-zone gate and the first passed
  test terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes.

## New questions

- Does completing all eight B tests retain one durable B licence identically
  across `SCUS-94194` pressings after a memory-card reload?
- Which tuning decisions remain mechanically distinct after a car is admitted
  to one Sunday Cup race?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0317` StarCraft II.
- Optimisation criterion: switch from a solo timed driving test to a real-time
  command-and-production mission.
- Expected information gain: test reuse around RTS production, fog, combat and
  mission settlement without extending Gran Turismo's career scope.
- Backlog impact: `GAME-0317` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Gran Turismo supplies a highly recognisable
  legacy PlayStation example and a compact licence-test boundary that is
  mechanically distinct from the corpus's complete race and time-trial routes.
