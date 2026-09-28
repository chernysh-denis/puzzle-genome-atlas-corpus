---
game_id: GAME-0439
slug: wii-fit
game_title: Wii Fit
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-575
  system:
    - SYS-045
    - SYS-1152
    - SYS-1153
  constraint: []
  information:
    - INF-424
  objective:
    - OBJ-251
  time:
    - TIM-003
---

# Game: Wii Fit — original Wii Beginner Ski Slalom

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Balance Board, Mii, 19 gates, blue balance zone and seven-second penalty are parameters or carriers, not stand-alone gene names.

## Analysis scope

- Version / ruleset: original English North American *Wii Fit* Wii Game Disc (2008), Beginner Ski Slalom in the Balance Games category, one completed run after a profile and Wii Balance Board have been registered. The original manual supplies the training and result lifecycle; a first-hand guide and direct experimental study supply activity-specific control, fixed route, feedback and penalty rules. The exact disc revision was not inspected.
- Structured analysis target: `PLAT-NINTENDO-WII` in [`knowledge/platforms/games.json`](../../platforms/games.json), with an ordinary registered Wii Balance Board and no emulated inputs.
- Primary decision loop: while standing on the board, shift weight left or right to steer the automatically descending Mii toward the next visible gate, and fore or aft to modulate speed. Read the current centre-of-balance dot, the Mii's response and each gate's immediate pass/miss feedback; adjust before the next gate. Finish the fixed Beginner slope. The final effective time is the actual downhill time plus seven seconds per missed gate; a cleaner and faster passage is better.
- Entry: the player selects Beginner Ski Slalom, the board recognises the person, and one run begins at the top of the slope before the first gate. Profile creation, registration, safety preparation and initial activity demonstration are prerequisites, not actions within this run.
- Positive terminal: the Mii reaches the end of this one slope and the game reports the run's performance/effective time. A missed gate worsens the evaluation but does not block the finish; no medal threshold or personal best is required for a completed packet.
- Negative terminal: this bounded activity does not have an evidenced death, zero-life or missed-gate failure state. Quitting or restarting from the pause menu abandons this attempt, rather than revealing a distinct downhill failure rule.
- Included: continuous physical left/right and forward/back weight shifts, board measurement mapped to lateral Mii steering and speed, automatic downhill progress, a fixed Beginner gate sequence, immediately visible/audible gate outcome, live centre dot and avatar response, elapsed course time, one seven-second addition per missed gate, finish evaluation and ordinary retry/quit offer after results.
- Excluded: Body Test, BMI, Wii Fit Age, yoga, strength and aerobic activities, Ski Jump, Snowboard Slalom, Advanced Ski Slalom, Fit Bank unlock progression, daily fitness goals, leaderboard optimisation, absolute sensor calibration values, exact steering gain and acceleration curves, exact medal cutoffs, Wii Fit Plus/U activity additions and any health-benefit claim. The score is not treated as a medical measurement.
- Reproducible parameterisation: use an original Wii disc and registered Balance Board, select Beginner Ski Slalom and stand on it when instructed. Shift laterally while the Mii descends and observe the Mii's sideways response; shift fore/aft and observe pace change. Complete at least one gate cleanly and deliberately miss another, keeping track of the feedback; reach the bottom and compare elapsed time with the reported penalty-adjusted result. The original Beginner course has 19 gates in the direct experimental report. A reproducible console replication would need the disc revision, board calibration, user weight, input trace and final screen; none was obtained here.
- Potential scoped modules: Advanced Ski Slalom, longitudinal training records, other balance games and comparative control fidelity against Wii Fit Plus/U.
- Direct-play status: no Wii console, disc, board, sensor trace, screenshot, video or audio was inspected for this research. The original Nintendo booklet was read directly; the game-specific loop is corroborated by a dated first-hand written guide, an experimental study using repeated Wii Fit Ski Slalom runs and Nintendo's developer interview. The illustration is original interpretive art, not a captured game frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WF-001` | The original game has Balance Games, prepares/recognises the board before training, and reports a performance score after an activity with Retry/Quit choices. | Confirmed | Direct | High | P1 |
| `WF-002` | Beginner Ski Slalom uses the Balance Board; weight shifts left/right steer the Mii, while forward/back shifts change pace. | Observation | Corroborated | High | P2, P3 |
| `WF-003` | The original Beginner course is a fixed 19-gate layout, and passing or missing a gate produces immediate visual/auditory feedback. | Observation | Direct | High | P3, P4 |
| `WF-004` | At the finish, effective time equals actual course time plus seven seconds for every missed gate; misses penalise rather than terminate the run. | Observation | Direct | High | P2, P3 |
| `WF-005` | The screen's live balance dot and Mii response help the player adjust the next weight shift; exact board-to-avatar coefficients are not published here. | Observation | Corroborated | Medium | P2, P3 |
| `WF-006` | Ski Slalom flag locations were intentionally placed and tested by a Wii Fit developer. | Confirmed | Direct | High | P4 |

## Basic data

- Release / origin: Nintendo's original North American Wii *Wii Fit* (2008), not later *Wii Fit Plus* or *Wii Fit U*.
- Platform or physical form: Wii optical disc plus registered Wii Balance Board; Wii Remote is used for menu selection, not slalom steering.
- Mechanical family: real-time system pressure (`FAM-010`) from an automatically advancing descent and performance time; physical weight-sensing is the input channel, not a new one-game family.
- **P1:** [Nintendo, original *Wii Fit* instruction booklet](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_Wii_Fit?_a=DATAg1AAZAA0), English pp. 4–6, 15–16 (2008; accessed 2026-09-28). Nintendo's old [manual directory](https://en-americas-support.nintendo.com/app/answers/detail/a_id/16890/) still lists the game, although its legacy PDF target now returns 404; the cited Nintendo asset is reachable.
- **P2:** [Sky1993, *Wii Fit* first-hand guide](https://gamefaqs.gamespot.com/wii/942009-wii-fit/faqs/53123), begun June 2008, Beginner Ski Slalom section, current page updated 2012. It is a player's account, not Nintendo rule text.
- **P3:** [Jelsma et al., “Motor Learning: An Analysis of 100 Trials of a Ski Slalom Game...”](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0140470), *PLOS ONE* 10(10), 2015, Methods “Wii Fit ski slalom game”. This is original experimental observation of game runs, not direct inspection of our disc or hidden scoring code.
- **P4:** [Nintendo, Iwata Asks: *Wii Fit*, Vol. 4](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Wii-Fit/Volume-4-Sound-Design-and-Planning/4-Almost-like-Spinning-a-Real-Hoop/4-Almost-like-Spinning-a-Real-Hoop-204199.html), Hosaka's description of placing and repeatedly testing Ski Slalom flags.
- Claim IDs: `WF-001`–`WF-006`.

## Mechanical decomposition

### Action Genes

- Add `ACT-575`: deliberately shift body weight across a pressure-sensing board rather than press a directional button. Both lateral and fore/aft components are available while skiing (`WF-002`).

### System Behaviour Genes

- Reuse `SYS-045` for the Mii's autonomous downhill continuation while the player adjusts course. Add `SYS-1152` for the live translation of measured balance into lateral route and forward pace; movement is responsive rather than a discrete one-step hop (`WF-002`, `WF-005`).
- Add `SYS-1153`: each passed gate gives immediate success feedback; each missed gate increments a penalty count without blocking the remainder of the course. At the finish, seven seconds per miss is added to actual time (`WF-003`, `WF-004`).
- Resolution order: sample weight shift → update Mii steering/pace during descent → test each encountered gate for pass/miss and signal it → continue to the next gate → settle actual and adjusted time at the slope's finish.

### Constraint Genes

- None admitted. The Beginner route has a fixed authored gate order, but a miss does not invalidate course progress (`WF-003`, `WF-004`). This is neither the mandatory ordered-checkpoint legality of `CON-438` nor a terminal attempt deadline such as `CON-068`. Board registration and safe stance are hardware prerequisites outside the bounded downhill decision loop.

### Information Genes

- Add `INF-424`: show the moving Mii and nearby gates with a live balance-position dot, and give immediate pass/miss feedback at a crossed gate. This supports correction without revealing a solved future steering trace or numerical sensor coefficients (`WF-003`, `WF-005`). The final adjusted time is a result, not a pre-action forecast.

### Objective Genes

- Add `OBJ-251`: complete the one fixed slope and minimise the penalty-adjusted elapsed time. A valid but slower, gate-missing finish still completes the run; improving rank is optional (`WF-001`, `WF-004`).

### Time Genes

- Reuse `TIM-003`: the Mii continues downhill and elapsed time accumulates while weight shifts are made. The clock is a performance measure, not a countdown to automatic failure (`WF-002`, `WF-004`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Board has recognised a standing player; Mii approaches a gate left of its current line | Transfer weight left | Board samples balance, and Mii turns laterally toward the open gate | physical input becomes avatar steering | `WF-001`, `WF-002` |
| Mii approaches the next gate too quickly | Move centre of mass aft | Downhill pace reduces while lateral steering remains possible | fore/aft input is speed control, not a menu command | `WF-002` |
| Mii crosses between a pair of flags | Keep a matching weight shift | Pass feedback is issued and the descent continues | gate outcome is immediate; gate is not a level exit | `WF-003` |
| Mii passes outside the next gate | Continue down the slope | Miss feedback is issued; no automatic failed-run terminal occurs | miss adds a scoring penalty, not a traversal lock | `WF-003`, `WF-004` |
| Finish reached after one missed gate and actual descent time `T` | Complete the run | Result reports `T + 7 s`, and Retry/Quit is available | adjusted performance terminal | `WF-001`, `WF-004` |

## Strategic and experiential structure

- Local decision: read the next gate and current balance dot, then adjust lateral weight before the Mii reaches it; use fore/aft weight to avoid overshooting at speed.
- Medium-term plan: balance time-saving pace against turns precise enough to avoid seven-second misses. A fast but inaccurate run may evaluate worse than a slower clean run.
- Long-term boundary: finish one Beginner descent and inspect the effective time. The next training choice is outside this packet.
- Failure attribution: the interface gives immediate gate outcome, while exact sensor gain and body-weight normalisation were not measured with this repository's hardware.
- Player trust: the board-to-Mii response is observable during control, and the finish formula makes penalty accounting explainable.

## Replay and variation

The Beginner gate layout is fixed in the experimental report, so variation comes from the person's weight-transfer timing and pace, not random gate generation. A retry can improve effective time by reducing misses, improving actual descent time, or both. This analysis does not claim particular star thresholds or physiological training effects.

## Adjacent systems and history

*Wii Sports* Bowling (`GAME-0364`) also maps bodily motion to a scored activity, but its hand-held Wii Remote swing is a discrete release followed by ten-frame pinfall and deferred strike/spare arithmetic. *Wii Fit* Ski Slalom samples standing weight distribution continuously and adds missed-gate time to a single downhill finish. *Super Monkey Ball 2* (`GAME-0378`) also has real-time path control and a timed finish, but the player tilts a virtual platform using a Control Stick, may fall into a terminal, and can earn a remaining-time bonus; it does not sense the player's centre of pressure.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-575` | lateral and fore/aft weight transfer |
| System Behaviour | `SYS-045`, `SYS-1152`, `SYS-1153` | live skier motion, balance mapping, seven-second misses |
| Constraint | none | missed gates do not bar the finish |
| Information | `INF-424` | balance dot, Mii/gate positions and immediate feedback |
| Objective | `OBJ-251` | completed Beginner descent with minimal effective time |
| Time | `TIM-003` | continuous descent and elapsed clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `438` (`GAME-0001`–`GAME-0438`).
- Exact genome matches: none.
- Tied near matches: `GAME-0092` — Echochrome (`2 / 15 = 0.133333`); `GAME-0345` — Duck Hunt (`2 / 15 = 0.133333`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0092` *Echochrome* | `SYS-045`, `TIM-003` | Both keep an avatar moving while the player responds during live time. Echochrome rotates the camera so perspective joins or hides fixed paths for an autonomous Walker to collect echoes; this skier's own route and pace respond continuously to measured body balance, and missed flags change final time rather than the traversable geometry. | Tied-near maximum, not an exact match (`2 / 15 = 0.133333`). |
| `GAME-0345` *Duck Hunt* | `SYS-045`, `TIM-003` | Both expose a moving target or avatar under live time. Duck Hunt uses a physical light gun to hit one flying duck within a short shot budget and needs a first-round hit quota. Wii Fit instead senses standing weight to steer the Mii through a fixed downhill gate route and permits misses with an additive time cost. | Tied-near maximum, not an exact match (`2 / 15 = 0.133333`). |

## Taxonomy impact

`TAXONOMY_CHANGE_176` admits pressure-board input, measured weight-to-Mii mapping, additive missed-gate time, current balance/gate feedback and a completed minimum-time slope. `SYS-045` and `TIM-003` are reused. No earlier game signature or verified combination is changed.

## Negative results

- `ACT-519` tilts the simulated stage with an analogue stick to move a rolling ball, not the player's measured body weight to steer a skier.
- `SYS-516` and `CON-438` validate mandatory race checkpoints and laps; a missed Wii Fit gate is scored as a seven-second penalty rather than making the finish invalid.
- `CON-068` requires an expiry that ends the attempt unsuccessfully; the slalom uses elapsed performance time.
- `OBJ-133` requires a car through all mandatory waypoints and a retained medal for one official track; this activity tolerates missed gates and its bounded result is a penalty-adjusted time, not a required medal.
- Fit Bank unlocks, medical or BMI interpretation, other exercise categories and Wii Fit Plus/U content remain outside the selected downhill packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's original booklet establishes the board-recognition, training and activity-result lifecycle (`WF-001`).
- [Observation | Direct | High] Repeated experimental Wii Fit Ski Slalom runs establish fixed gate layout, live feedback and the `T + 7 s × misses` result (`WF-003`, `WF-004`).

## New genes

- [Observation | Corroborated | High] Five typed boundaries are admitted in `TAXONOMY_CHANGE_176`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_176`; earlier signatures remain unchanged.

## New questions

- What are the exact input-smoothing, sensitivity and lateral/fore-aft response coefficients on an original North American disc and calibrated board?

## Next game

`GAME-0440` *Scribblenauts* follows after the Goal stop window; its edition and one bounded word-created-object puzzle require separate research.
