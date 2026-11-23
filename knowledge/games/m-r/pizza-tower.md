---
game_id: GAME-0640
slug: pizza-tower
game_title: "Pizza Tower"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-852
  system:
    - SYS-037
    - SYS-1846
    - SYS-1847
    - SYS-1848
    - SYS-1849
  constraint: []
  information:
    - INF-192
    - INF-594
  objective:
    - OBJ-345
  time:
    - TIM-003
---

# Game: Pizza Tower

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English commercial Windows Steam
  application 2231450, released on 26 January 2023 by
  Tour De Pizza. The selected behavior is supported by the
  original 2023 release window. Exact installed build
  and capture hardware are unverified.
- Primary decision loop: build running speed, direct Peppino
  through an authored route, break its terminal fixture, then
  manage the changed return passages and score while going
  back to the original entrance.
- Entry: the John Gutter gate in Tower Lobby with Peppino
  under player control and the route in its outbound state.
- Exit: the first return through the reopened entrance,
  the settled letter rank and the active hall outside
  the same course. Pizzascape entry is corroboration only.
- Included: run-up, supported movement and attack, point and
  Toppin pickups, local view, breakable route blocks, the
  one-way phase change, active clock and point debit, exit
  settlement and visible combo feedback.
- Excluded: pre-release and console versions, the tutorial
  as a separate course, other playable characters, optional
  second lap, complete secret and treasure contracts, P-rank
  requirements, campaign spending, exact move thresholds and
  hidden scoring coefficients. Timeout pursuit is documented
  as a boundary outside the observed clear.
- Suggested later scope: test whether late escape remains
  possible under pursuit and what ends that attempt.

## Direct-play status

No direct play was performed. The Steam listing identifies
the released Windows product. An explicitly PC-labelled
recording provides the initial gate, Pillar John, the running
return, A-rank settlement and return to active hall movement.
A separate 2023 recording supplies the same transition with
clearer local HUD frames. A verified Peppino PC run returns
with B after a fast first lap. The exact binaries and input
hardware are unverified. Research used silent static frames.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PT-001 | Tour De Pizza released the commercial English Windows Steam game on 26 January 2023. John Gutter is an ordinary selectable Tower Lobby stage in the recorded PC campaign. | Confirmed | Direct | High | P1 listing, Windows system requirements and release date. W1 15:10–15:20. W3 PC verification. |
| PT-002 | Peppino directly runs, jumps and attacks. A sustained run-up changes the contact behavior of eligible blocks, allowing him to break through a cheese-block row. Adjacent geometry and local pickups are visible as the side view follows him. | Observation | Corroborated | High | W3 notes and start from 0:11–0:25, including the dash into the cheese blocks in the second room and the subsequent ground pound. W2 0:25–0:55 and 3:41–3:44 show active movement, local geometry and pickups. |
| PT-003 | The original entrance is open at first appearance, but closes on the outbound leg. The player attacks and removes the designated Pillar John at the far end. The in-game Pizza Time announcement follows the hit. | Observation | Corroborated | High | W1 15:20–15:40 and 20:30–20:32. W2 0:25–0:35 and 3:45–3:50. W3 0:52–0:54. |
| PT-004 | The trigger starts the countdown while Peppino stays controllable. Some phase-linked passages change from the outbound configuration. The original entrance is open again at the return, with active time remaining. | Observation | Corroborated | High | W1 20:33–20:40 displays the clock on the return and 23:19–23:21 the open exit. W2 3:50–4:00 shows the changed route then 5:50–5:52 the open gate. W2's run description also explains the swapped John Blocks. |
| PT-005 | The escape clock continues while movement remains available. A positive remaining clock coexists with a small point debit and the visible letter tier and combo. The score can still rise after earning additional points. | Observation | Corroborated | High | W2 5:44–5:52 shows the clock passing 0:50, the visible −5 and changes to points during movement. W1 23:15–23:21 shows separate points, rank, combo and an active clock while approaching the exit. The exact loss cadence was unmeasured. |
| PT-006 | Using the reopened entrance produces a clear and a letter-rank result. Lower performance and skipping the extra lap are compatible with completion. The hall records the grade beside the entrance. | Observation | Corroborated | High | W1 23:19–23:43 shows escape, A, HIGHSCORE 10416 and the hall marker. W2 5:50–6:15 shows A, HIGHSCORE 12549, damage 3 and highest combo 26. W3 1:32–1:52 shows B, HIGHSCORE 4592, damage 0, highest combo 27 and the hall return. |
| PT-007 | The observer account describes a pursuer appearing after expiry and a capture ending the attempt. The examined clears do not cross zero. | Observation | Limited | Medium | W2 creator description of post-timeout pursuit. No timeout, exact catch timing or post-expiry clear was measured. |

## Basic data

- Analysis target: `PLAT-WINDOWS-PC`.
- Developer and publisher: Tour De Pizza.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Tour De Pizza's Steam listing](https://store.steampowered.com/app/2231450/Pizza_Tower/),
  application 2231450, release date, Windows requirements and
  movement, exploration and score-attack focus.
- W1: [Flembons, explicitly PC-labelled campaign capture](https://www.youtube.com/watch?v=s3Y3_0B9lUk&t=914s),
  John Gutter at 15:14.
- W2: [Carls493, John Gutter capture and route commentary](https://www.youtube.com/watch?v=huihbQnCj6I),
  13 April 2023. Platform is not explicitly identified in
  its description, so the PC-labelled traces bind the target.
- W3: [Rossiyan, continuous John Gutter Any% result](https://www.youtube.com/watch?v=vGJpLYX4kWQ&t=11s).
  The [submitted run](https://www.speedrun.com/pizza_tower/runs/zpgo5qnz)
  identifies Peppino and PC. The timing entry is independent
  of the in-game rank.

## Mechanical decomposition

### Action Genes

- ACT-008: directly steer Peppino through authored geometry.
- ACT-295: commit a character attack such as a ground pound.
- ACT-852: sustain a directional run to build the movement
  state used in the fast route.

### System Behaviour Genes

- SYS-037: physically contact stage collectibles to acquire them.
- SYS-1846: the qualified running contact breaks compatible
  obstacles and leaves the lane traversable.
- SYS-1847: breaking Pillar John changes the course phase,
  linked passages, original door and visible return clock.
- SYS-1848: the escape countdown comes with a periodic score
  debit while the stage remains live.
- SYS-1849: exit settles the score tier and the run report.

### Constraint Genes

No separate constraint gene is introduced. The eligible
contact state and exit state are integral to their transition rules.

### Information Genes

- INF-192: the side view exposes nearby route and hazards.
- INF-594: the HUD separates the live score and tier from
  the combo and contextual countdown.

### Objective Genes

- OBJ-345: act on the far-side trigger and get back through
  the original entrance to obtain a ranked clear.

### Time Genes

- TIM-003: accept active movement and attack while the running
  timer and the local stage activity continue.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Peppino is in the initial checkerboard room | Leave the starting gate rightwards | The door changes from lit to closed. The ordinary score HUD is already present, without an escape clock. | PT-001, PT-003 |
| An eligible block row occupies a lane | Take a run-up and dash into that lane | The blocks break and Peppino carries on across the lane. | PT-002 |
| Pillar John is intact in the far room | Strike the pillar | The pillar disappears. Pizza Time appears and the return countdown starts. | PT-003, PT-004 |
| Return is active and Peppino approaches earlier rooms | Navigate the changed route | Passage availability differs from the outbound leg. The live clock continues and points can be gained or debited. | PT-004, PT-005 |
| The original entrance is lit on the return | Use the door before the clock expires | The rank and report appear. Active play resumes outside the stage gate, marked with the result. | PT-006 |

## Strategic and experiential structure

The outbound trip gives the player time to read the room
and develop speed. The triggering strike changes the cost of
detours and some of the available travel lanes. On the
return, a route can trade score opportunities against time.
The ordinary exit and performance tier give separate goals.

## Replay and variation

Two ordinary captures settle A despite different damage and
combo totals. The 1:23.22 in-game PC report with zero recorded
damage settles B at 4,592 points, while the slower PC capture
settles A at 10,416. Arrival, time, combo and grade are
distinct observations. This comparison does not estimate a
threshold or isolate each score input.

## Adjacent systems and history

Toppins, secret rooms and Gerome's treasure can change a
run's result. The admitted route does not model their complete
requirements. W1 next enters Pizzascape. Its rules are outside
this packet. The publisher names Wario Land as an influence;
comparison below uses admitted gene signatures.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-295, ACT-852 | Steer, attack and build running speed |
| System Behaviour | SYS-037, SYS-1846, SYS-1847, SYS-1848, SYS-1849 | Acquire pickups, break blocks, switch return phase, debit score and settle the rank |
| Constraint | None | Contact and exit preconditions belong to their transitions |
| Information | INF-192, INF-594 | Disclose adjacent route and run counters |
| Objective | OBJ-345 | Activate the return and exit through the original entrance |
| Time | TIM-003 | Advance live states during input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `639` (`GAME-0001`–`GAME-0639`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`5 / 27 = 0.185185`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sonic the Hedgehog (GAME-0333)](../s-z/sonic-the-hedgehog.md) | ACT-008, ACT-295, INF-192, SYS-037, TIM-003 | Both allow live movement and attack through a nearby side view with contact pickups. The original Sonic's advance toward the signpost and its protective ring stock differ from the triggered return, changed passages and scored escape in John Gutter. | Near, `0.185185` |

## Taxonomy impact

Seven new definitions separate the sustained run action,
its collision outcome, return state and score pressure,
score-tier settlement, HUD and ranked return objective.
The five reused definitions retain their existing boundaries.

## Negative results

- Breaking the pillar starts the return and does not by
  itself produce a ranked clear.
- The completed A and B results do not require a second lap.
  Shorter time and zero damage are not sufficient for A.
- Combo count and grade are separate. The B trace has a
  higher maximum combo than the complete A comparison clips.
- Zero-clock pursuit was not measured in these clears.
  Do not use this record as proof that the clock is an
  immediate failure cutoff or as an exact post-expiry rule.

## Delta summary

Twelve genes include seven new definitions. All earlier
signatures and definitions are preserved.

## New facts

- One local strike changes both the available return passages
  and the time pressure.
- Completing the return carries the score tier into the
  result and marks the same entrance in the hall.
- Time pressure can debit the active score before expiry.

## Principles and design implications

- Change route affordances at the same time as a local
  return clock makes them urgent.
- Make the original safe entry a legible return destination.
- Provide a lower successful rank without requiring the
  highest-performance detours.

## Puzzle or game generation potential

Prototype a short two-leg course where the far trigger
changes the traversable passages. The old entrance becomes
the goal while a clock pressures the trip and a separate
score grades the result.

## New genes

ACT-852, INF-594, OBJ-345 and SYS-1846 through SYS-1849.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_386](../../../research/taxonomy-changes/TAXONOMY_CHANGE_386.md).

## New questions

Will a late first-lap return settle with Pizzaface present?
Which movement states can preserve speed across a turn?

## Next recommended game

Analyse Bushido Blade on the original North American
PlayStation release through an opening Story duel.

## Why this game

The same course has two materially different travel legs.
One reachable trigger makes speed, timing and score consequential
on the way back to a known point.
