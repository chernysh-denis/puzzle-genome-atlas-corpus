---
game_id: GAME-0448
slug: temple-run
game_title: Temple Run
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-588
    - ACT-589
  system:
    - SYS-037
    - SYS-045
    - SYS-1175
    - SYS-1176
    - SYS-1177
  constraint:
    - CON-723
  information:
    - INF-433
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Temple Run — one original iOS score run

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Gesture directions, coin values, speed and obstacle shapes are parameters, not separate genes.

## Analysis scope

- Version / ruleset: the original Imangi *Temple Run* released for iPhone in August 2011, limited to one fresh, unassisted classic run. The exact launch binary and its later update number were not inspected; contemporary first-hand accounts and the creators' retrospective bound the reconstruction.
- Primary decision loop: while the runner advances automatically, read the next visible bend, gap or obstacle; swipe left/right to turn or up/down to jump/slide at the right moment; tilt laterally to collect a coin line without leaving the path; continue until a fatal mistake ends the attempt and its accumulated score can be inspected.
- Entry and exit: tap to take the idol and begin a fresh run with no previously purchased upgrade or active rescue; the local packet ends at its first terminal fall, collision or pursuer capture, when that attempt's score is evaluated. There is no finish line or escape victory.
- Included: unavoidable forward motion, discrete touch gestures, independent lateral tilt, upcoming path/obstacle visibility, varying continuing route, optional coin contact, recoverable stumble with pursuer pressure, fatal failure and live distance/coin-related score accumulation.
- Excluded: Temple Run 2, Temple Run+, Android and browser control mappings; modern challenges, advertisements, revives and events; store purchases, metaprogression upgrades, objective-multiplier progression, characters, leaderboards and exact distance or score coefficients. Collecting an ordinary coin in the run is included; spending that coin afterward is not.
- Potential scoped modules: purchased power-up and revival rules in a specified original-game revision; objectives and multiplier progression across attempts.
- Direct-play status: no original iPhone installation, build, touch trace, screenshot, video or completed run was inspected. The founding developer's first-person account explains the controls, no-stop constraint and chase; a 2011 first-hand review documents the run and variable route. Exact sequence generation, collision tolerances, recovery duration and numeric score formula remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TR-001` | The 2011 iPhone original is an automatically advancing endless run that starts with an idol and ends through failure rather than a fixed goal line. | Observation | Corroborated | High | P1, P2, S1, S2 |
| `TR-002` | Left/right swipes request 90-degree turns; up/down swipes request a jump/slide, while the runner cannot stop. | Observation | Direct | High | P2, P3 |
| `TR-003` | Device tilt separately changes lateral position to follow coin lines; it is not the swipe-to-turn command. | Observation | Corroborated | High | P2, S1, S2 |
| `TR-004` | The path includes visible corners and hazards, and the continuing course varies between attempts; its exact generation algorithm is not established here. | Observation | Corroborated | Medium | P2, S2 |
| `TR-005` | A trip can leave the pursuers closer, while an uncaught edge/fatal obstacle or later capture terminates the run; exact stumble allowance is unmeasured. | Observation | Corroborated | Medium | P1, P2, S2 |
| `TR-006` | Running, coins and bonus items can contribute to score, and the original game offers a separate between-run coin upgrade economy; this packet uses no purchased aid. | Observation | Corroborated | Medium | P1, P4, S1, S2 |
| `TR-007` | No launch-build execution, exact path sample, speed trace, collision window or numeric score coefficient was verified. | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Imangi Studios' original 2011 iPhone release, not its later sequel or Apple Arcade variant.
- Platform: touchscreen/tilt iOS handset; the structured target is in `knowledge/platforms/games.json`.
- Mechanical families: real-time system pressure (`FAM-010`) and tactical forecast and counterplay (`FAM-009`) through short lookahead and committed evasion.
- **P1:** [Imangi's official classic-game description](https://imangistudios.zendesk.com/hc/en-us/articles/4995833305747-About-Temple-Run), inspected 2026-09-28; identifies the idol, Demon Monkeys, turns, jumps, slides, coins and endless-distance purpose. The current support page is used only for stable original-game mechanics, not later features.
- **P2:** [founding developer Natalia Luckyanova's 2012 first-person interview](https://venturebeat.com/ai/temple-run-developer-shares-a-behind-the-scenes-look-at-making-a-runaway-hit-ios-game), inspected 2026-09-28; states that the runner cannot stop, turns are limited to 90 degrees, tilt was selected for coin collection and trips bring the monkeys close.
- **P3:** [co-creator Keith Shepherd's control-design interview](https://gamesbeat.com/even-with-a-temple-run-empire-imangi-studios-wants-to-stay-indie-at-heart-interview/2/), inspected 2026-09-28; corroborates the four swipe directions and automatic walking.
- **P4:** [Imangi's scoring FAQ](https://imangistudios.com/faq/), inspected 2026-09-28; explains running, coin and bonus-item score and the separate objectives multiplier. The objective system is excluded from this first-run packet.
- **S1:** [Engadget's first-hand August 2011 iPhone account](https://www.engadget.com/2011-08-09-daily-iphone-app-temple-run.html), inspected 2026-09-28; corroborates tilt-collected coins, swipe controls, upgrades and score chase.
- **S2:** [Pocket Gamer's first-hand August 2011 review](https://www.pocketgamer.com/temple-run/review/), inspected 2026-09-28; describes the idol-tap entry, no speed control, corners, obstacles, lateral tilt, variable attempts and terminal failures.
- **R1:** local preflight found no original game installation or direct-play trace for this unit.

## Mechanical decomposition

### Action Genes

- `ACT-588` commits one context-sensitive directional swipe. Left/right ask for a 90-degree corner turn; up/down ask for a jump or slide. A gesture does not itself stop forward travel.
- `ACT-589` continuously tilts the device to shift the runner across the width of the present path, for a safe line or optional coins. This does not choose the next branch.

### System Behaviour Genes

- Reuse `SYS-045` for the runner's movement along the path without a forward command on every step.
- Reuse `SYS-037` for optional coin contact during the still-running attempt.
- `SYS-1175` extends a variable sequence of path, corners, gaps and obstacles ahead of the runner. This does not assert a specific random seed or algorithm.
- `SYS-1176` distinguishes a recoverable trip with pursuers closing in from terminal fall, collision or capture. The number and timing of tolerated stumbles are not quantified.
- `SYS-1177` advances a live score with continued distance and eligible pickups, then settles that attempt's value at failure. The objective-multiplier ladder and exact arithmetic are outside the packet.

### Constraint Genes

- `CON-723` forbids stopping or reversing ordinary forward travel: a left/right swipe changes heading only at a valid bend, whereas lateral tilt cannot substitute for that turn.

### Information Genes

- `INF-433` exposes a bounded forward view of the next bend, safe path, obstacle and coin line while later path segments remain unseen. It does not preview the exact rest of the endless run.

### Objective and Time Genes

- Reuse `OBJ-002`: maximise the score of this attempt, rather than reach an authored finish or defeat the monkeys permanently.
- Reuse `TIM-003`: forward travel and hazards continue while the player decides and inputs gestures.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Idol is available at a fresh start | Tap to begin | The character takes the idol and starts moving with pursuers behind | The entry starts one score attempt, not a fixed level | `TR-001` |
| Runner approaches a visible left bend | Swipe left before running beyond the corner | Heading changes by 90 degrees onto the continuing path | Tilt alone cannot replace a turn | `TR-002`, `TR-004` |
| A low barrier approaches on the current path | Swipe up with enough time to pass over it | The runner attempts a jump while forward travel continues | Vertical gesture and timing matter independently of lateral tilt | `TR-002` |
| A high barrier approaches on the current path | Swipe down before contact | The runner attempts a slide beneath it | Another hazard calls for a different vertical response | `TR-002` |
| A coin row lies to one side of a safe straight section | Tilt toward the row | Lateral position changes and contacted coins are credited without ending the run | Coin reward is a risk/reward line, not the required path | `TR-003`, `TR-006` |
| Runner clips a low obstacle but stays on the path | Continue running | The pursuers draw closer after a stumble; the attempt may still continue | One mistake need not be the terminal event | `TR-005` |
| Runner fails a corner or falls from the path | No viable recovery in the scoped run | The run ends and its accumulated score is inspected | The attempt has a failure terminal but no escape finish | `TR-001`, `TR-005`, `TR-006` |

## Strategic and experiential structure

The player reads only a short future slice, then chooses the correct gesture before it is too late. Tilting to gather coins can move the runner away from a safer line; the independently required corner swipe must still arrive in time. A stumble tightens pursuit pressure rather than necessarily erasing the attempt immediately. The payoff is a higher run score, not reaching a final temple exit. The sources do not establish exact swipe buffering, obstacle hitboxes, speed scaling or a guaranteed high-score route.

## Replay and variation

Contemporary first-hand accounts describe differing attempts in the continuing course. A new run reopens the timing and coin-line decisions from the idol entry, while the sampled future path is not fully known at the start. This packet does not claim a specific procedural generator, uniform obstacle distribution or exact repeatability under a seed.

## Adjacent systems and history

The authored *Geometry Dash* Stereo Madness route also auto-advances under live input, but it replays a fixed side-view song/obstacle timeline toward a 100% finish. Original *Temple Run* supplies a varying third-person corridor with distinct swipe and tilt channels, pursuer pressure and no ordinary finish. Later Temple Run sequels, Temple Run+ and current live-service features are not silently inherited by the 2011 packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-588`, `ACT-589` | swipe direction, tilt degree and lateral position |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-1175`, `SYS-1176`, `SYS-1177` | coin contact, auto-run, continuing path, failure, score |
| Constraint | `CON-723` | no stop or reverse, corner turn versus tilt |
| Information | `INF-433` | bounded visible forward corridor |
| Objective | `OBJ-002` | highest score before first failure |
| Time | `TIM-003` | uninterrupted automatic travel |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `447` (`GAME-0001`–`GAME-0447`).
- Exact genome matches: none.
- Tied near matches: `GAME-0445` — NiGHTS into Dreams (`4 / 22 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0445` NiGHTS into Dreams | `OBJ-002`, `SYS-037`, `SYS-045`, `TIM-003` | Both move autonomously in real time and can collect pickups for score, but NiGHTS is a bounded authored flight with a return-to-Palace objective, while Temple Run uses a changing corridor, distinct swipe/tilt inputs, a chase and no ordinary finish. | Near, `0.181818` |

## Taxonomy impact

`TAXONOMY_CHANGE_185` admits seven source-supported boundaries without revising earlier game signatures or combinations.

## Negative results

- No evidence justifies a fixed level finish, a universally fatal first stumble, an exact course generator or automatic transfer of Temple Run+ control and revival rules.
- `SYS-496` is fixed authored obstacle/music replay and does not model this varying endless corridor; `ACT-008` assumes ordinary directly advanced movement and does not express the independent swipe/tilt channels under forced forward travel.

## Delta summary

## New facts

- [Observation | Corroborated | High] The original run joins forced forward motion, discrete swipe responses and a separate lateral tilt line (`TR-001`–`TR-003`).
- [Observation | Corroborated | Medium] A recoverable trip can change the chase before a later terminal failure (`TR-005`).

## New genes

- [Observation | Corroborated | Medium] Seven typed boundaries isolate two input channels, a varying continuing route, chase-aware failure, live run scoring, no-stop corner control and local forward information.

## New combinations

- [Observation | Limited | Medium] None proposed; supported proper subsets are recomputed.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_185`; no earlier signature is changed.

## New questions

- Which original iOS build and visible obstacle sequence could be reproduced in a future device-based comparison without inheriting current live-service rules?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0449` *Paper Mario*, after this unit and the Goal stop window.
- Optimisation criterion: cross-platform and decision-structure diversity within the approved horizon.
- Expected information gain: separate partner choice and timing-gated turn combat from automatic survival motion.
- Backlog impact: none; the selected order is retained.

## Why this game

- [Hypothesis | Limited | Medium] Temple Run adds the original touch/tilt endless-chase relation missing from the previously reviewed fixed-course auto-runners, without presuming all later mobile content shares the 2011 rules.
