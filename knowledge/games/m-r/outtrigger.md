---
game_id: GAME-0605
slug: outtrigger
game_title: "Outtrigger"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-037
    - SYS-1029
    - SYS-1779
  constraint:
    - CON-068
  information:
    - INF-569
    - INF-570
  objective:
    - OBJ-328
  time:
    - TIM-003
---

# Game: Outtrigger

This scope follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Course, scene, medal count and displayed score values are route parameters.

## Analysis scope

- Version / ruleset: full North American Sega Dreamcast commercial disc,
  Sega product `51102`, released in July 2001. The English US instruction
  booklet supplies the device and mission rules. A US-identified Redream
  capture corroborates the route. An independent English capture supplies
  the same demonstration, failure and result states; its exact media
  revision and physical execution are unverified.
- Primary decision loop: choose the standard pad and a default fighter
  in offline Mission Mode. Select the first Novice mission and read its
  collection rule. Once the clock starts, follow the available pickup cue,
  run into all three medals and settle the score before timeout. If time
  expires, choose whether to leave or start the same challenge again.
- Entry: the Dreamcast mode menu with Mission Mode available; choose the
  standard Dreamcast controller and a regular fighter, as in the sampled
  Lina route. No optional character edit is needed.
- Exit: after a valid clear, read the Mission 001 result, choose Exit and
  verify the mission's completion emblem on the grid before beginning
  another attempt. The timeout-and-retry route is a bounded negative case.
- Included: device and fighter setup, the mission grid and briefing,
  clearly labelled pre-attempt demonstration, directly controlled movement,
  contact pickup, live countdown, failed-time settlement, retry, successful
  collection, score and the completion mark.
- Excluded: later circle-collection and weapon exercises, Arcade courses,
  NAOMI, online and split-screen Versus, weapon discharge and damage,
  alternate device combinations, character unlocks, full course mastery,
  modified releases and proof of persistence after a power cycle.
- Suggested later scope: the second medal mission's longer loop, or one
  complete local Versus rule in a specifically documented edition.

## Direct-play status

No direct play was performed. Sega's US booklet establishes the
commercial console target and documented menu semantics. Static frames
from the region-attributed WORG capture and the English Zedra capture
reconstruct the first mission. The latter shows failure, a fresh retry
and an actual result. Input calibration, exact binary revision, all
layouts, maximum possible score and VMU persistence were not measured.
No video or audio playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| OT-001 | Sega's US Dreamcast product supports standard controller setup, character selection and identification before Mission Mode. Device and player setup are distinct surfaces. | Confirmed | Corroborated | High | P1 printed pp. 3–6, 9, 15, 26; R1; W1 12:50; W2 2:18:30–2:18:50. |
| OT-002 | Select Novice Mission 001 in the offline grid. It briefs full medal collection and a 30-second limit before OK. The walkthrough also shows a labelled demonstration distinct from the live attempt. | Observation | Corroborated | High | P1 p. 15; H1; W2 2:18:50–2:19:10, 2:22:00–2:22:10. |
| OT-003 | The live route starts at a station with floor tracks and the marked medals ahead. Directly navigating the fighter into each medal credits it; the mission's documented count is three. | Observation | Corroborated | High | H1; W1 13:00–13:20; W2 2:21:00, 2:21:20, 2:22:10–2:22:20. Exact pickup radius was not measured. |
| OT-004 | The authoritative clock ticks while the fighter can move. The live state uses a local medal cue, separately from the countdown. | Observation | Corroborated | High | P1 pp. 7–8, 15; W1 13:10; W2 2:21:00 and 2:21:20; H1. No complete off-screen radar rule is inferred. |
| OT-005 | Waiting through the allowance with the medals outstanding yields Mission Failed / Time Over. Exit is offered alongside Retry. Retry returns to the same station and a fresh attempt. | Observation | Corroborated | High | P1 p. 15; W2 2:21:20–2:22:10. Exact simultaneous expiry and acquisition ordering are untested. |
| OT-006 | Acquiring the complete set before expiry leads directly to the Mission 001 score without a separate exit marker. The sampled result shows 600 stage points, 26.00 seconds at a factor of 100, and 3,200 total points. | Observation | Corroborated | High | W2 2:22:10–2:22:20; H1; W1 moves beyond the station after 13:10. The values describe one observed attempt. |
| OT-007 | The sampled run proceeds from the result to a top-score notice, then to the grid with an emblem under mission 1. The different mission 2 briefing is visible at that boundary. | Observation | Corroborated | High | P1 p. 15; W2 2:22:20–2:22:40. VMU reloading and all conditions for a top score are outside scope. |

## Basic data

- Release / origin: Sega AM2, published by Sega in 2001 on Dreamcast.
  The scoped North American release is distinct from the 1999 cabinet
  game and from the Japanese console release.
- Platform: `PLAT-DREAMCAST`, English offline one-player Mission Mode.
- Puzzle family: real-time system pressure (FAM-010), because the timed
  route requires movement while the operative deadline decreases.
- P1: [Sega's US instruction booklet](https://www.digitpress.com/library/manuals/dreamcast/out_trigger.pdf),
  printed pp. 3–9, 15, 18 and 26. Covers input setup, game display, mission
  selection, replay, results and the separate VMU procedures. Its credits
  identify the US localisation and manual.
- P2: [Sega's Japanese Dreamcast software archive](https://www.sega.jp/history/hard/dreamcast/software.html)
  independently places the regional console release in 2001. Its August date
  is for Japan and does not supply the North American ship date.
- R1: [North American release catalogue](https://gamefaqs.gamespot.com/dreamcast/366267-outtrigger-international-counter-terrorism-special-force/data).
  Documents Sega 51102 and 24 July 2001.
- H1: [AGBear's firsthand Dreamcast mission guide](https://gamefaqs.gamespot.com/dreamcast/366267-outtrigger-international-counter-terrorism-special-force/faqs/23477),
  Mission Mode, Novice missions 1–2. Independently states the three required
  medals and 30-second allowance in mission 1.
- W1: [WORG US Dreamcast capture](https://www.youtube.com/watch?v=_-PfjEq7qrs).
  The creator identifies the US game and Redream 1.5.0-1133. The device
  setup and English station mission appear around 12:50–13:20. Used as
  region-attributed frame evidence, without a hardware-parity claim.
- W2: [Zedra Psyborg Dreamcast sequence](https://www.youtube.com/watch?v=0m3DxjKUMtE).
  Static frames for the first Novice mission span 2:18:30–2:22:40. Shows
  the same briefing, timeout with outstanding medals, explicit retry and
  terminal score. Because the video does not verify the disc serial, it
  corroborates the rule rather than supplying the North American identity.

## Reproducible route evidence

1. Select Mission Mode. Use a standard Dreamcast pad and choose a default
   fighter. W1 12:50 shows Device Setup with the pad, control type 01,
   VIEW set to NORMAL and assist on. W2 2:18:40 shows a distinct character and
   initials selection surface. The selected settings are one observed
   example, not a dependency of medal eligibility.
2. Confirm the settings, pick Novice and choose tile 1. W2 2:19:00 shows
   the complete collection requirement and the 30-second limit. The
   initial demonstration is overtly labelled and is separate from live
   play. Confirm the briefing and wait for the opening count-in.
3. At Start, move from the near track side toward the medals along the
   available floor ahead of Lina. Contact picks up medals and reduces
   the outstanding requirement. The display supplies a local guidance
   marker and a separate live clock. No attack input is needed to
   register the scoped pickups.
4. The negative trace leaves the fighter near the start with the
   requirement unresolved. W2 2:21:00 and 2:21:20 show the falling
   clock, 2:21:30–2:21:50 shows failure and Retry. Choosing Retry
   revisits the same mission's demonstration/count-in and starts a
   fresh run at the station by 2:22:10.
5. Follow the available markers to acquire all three medals while
   time remains. The settled score at W2 2:22:20 is labelled Novice
   Mission 001, with 600 stage score and a time bonus based on 26.00
   seconds remaining. It shows 3,200 total points. Stop moving when
   the result appears; Exit here dismisses the score screen rather
   than demanding a second in-arena goal after the last medal.
6. The observed top-score message follows the result. On selecting
   Exit, verify the completed icon under tile 1 in the returned
   grid. W2 2:22:40 has moved the highlight to the separate mission
   2 briefing. Stop before pressing OK for that mission.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the active fighter directly across the floor, choosing
  the order and line of contact within the authored starting geometry.
- Claim IDs: OT-001–OT-004.

### System Behaviour Genes

- SYS-037: contact credits each earlier medal and leaves the live route
  available to collect the rest.
- SYS-1029: the clear contributes remaining-time points separately from
  the earned stage score. Both contributions are disclosed at settlement.
- SYS-1779: an explicit retry after settlement returns to the same
  authored trial with its opening state and current clock renewed.
- Claim IDs: OT-003–OT-007.

### Constraint Genes

- CON-068: attaining the complete collection must precede expiry.
  A failed attempt with medals outstanding is observed at the deadline.
- Claim IDs: OT-002, OT-004, OT-005.

### Information Genes

- INF-569: the briefing discloses full collection and the allowance.
  Follow the local mark to a visible medal while reading the live clock.
- INF-570: the result breaks out the score, while the grid reports
  completed status for one addressed mission.
- Claim IDs: OT-002–OT-004, OT-006, OT-007.

### Objective Genes

- OBJ-328: acquire the three medals in the same live attempt and settle
  successfully on complete collection, without a separate exit.
- Claim IDs: OT-003–OT-007.

### Time Genes

- TIM-003: input remains available while the live deadline decreases.
  Count-in and demonstration are outside the active allowance.
- Claim IDs: OT-002–OT-005.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Mode menu with pad and default fighters available | Choose Mission Mode, device and character | Confirm separate setup surfaces | Device and fighter are scoped setup, not mission progress | OT-001 |
| Novice tile 1 selectable | Read and accept the briefing | Demonstration and count-in before the live clock | Objective and time are disclosed before commitment | OT-002 |
| Live attempt with medals ahead | Navigate into a nonfinal medal | Credit it and continue | Contact is enough for pickup, not final completion | OT-003, OT-004 |
| Outstanding collection at expiry | Let the clock reach its end | Mission Failed with Exit and Retry | Waiting alone cannot clear the mission | OT-005 |
| Settled failed attempt | Select Retry | Return to the same mission with a new attempt | The active time and position are not resumed | OT-005 |
| Only the last required medal remains, time positive | Reach it | Mission 001 result with separate stage and time components | No later goal needs to be reached for the result | OT-006 |
| Successful result available | Exit to the mission grid | Observe the emblem under 1 | Recorded completion belongs to this slot | OT-007 |

## Strategic and experiential structure

The path is short, but a clear and a good result are different predicates.
All the tokens matter for the first. How much time remains at that point
matters for the score. The visible pickup cues aid routing while a
noninteractive demonstration and retry keep failure locally recoverable.
Claim IDs: OT-002–OT-007.

## Replay and variation

The observed timeout and successful retry use the same fixed start. The
booklet permits both Exit and Retry at success or failure. A new high
score is shown in one run; no performance with a deliberately suboptimal
completed route was measured. The user may select alternative devices
or fighter options, but their effect on this loop was not tested.
Claim IDs: OT-001, OT-005–OT-007.

## Adjacent systems and history

The home edition's selectable missions differ from its arcade-style
courses. The second Novice tile uses a separate layout and a longer
briefed limit, although it also asks for medals. VS and Network Battle
use distinct scoring and menu rules. A medal dropped by an opponent is
not evidenced as a source of an opening collectible here.
Claim IDs: OT-001, OT-002, OT-007.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008 | Direct movement across the station |
| System Behaviour | SYS-037, SYS-1029, SYS-1779 | Contact pickup, time-bonus settlement and fresh retry |
| Constraint | CON-068 | Terminal deadline |
| Information | INF-569, INF-570 | Live pickup and quota guidance, score and mission mark |
| Objective | OBJ-328 | Full collection before expiry settles directly |
| Time | TIM-003 | Continuous decision window |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `604` (`GAME-0001`–`GAME-0604`).
- Exact genome matches: none.
- Tied near matches: `GAME-0378` — Super Monkey Ball 2 (`4 / 14 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Monkey Ball 2 (GAME-0378)](../s-z/super-monkey-ball-2.md) | CON-068, SYS-037, SYS-1029, TIM-003 | Both score pickups and reward finishing before a live failure deadline. Super Monkey Ball 2 tilts a course to move the ball to a separate goal while bananas remain optional. Outtrigger directly moves a fighter and settles on the last required medal. | 4 shared of 14, Jaccard 0.285714 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_351](../../../research/taxonomy-changes/TAXONOMY_CHANGE_351.md)
  isolates the retry branch, live collection cues, result presentation
  and direct terminal collection without changing earlier definitions.

## Negative results

- OBJ-154, OBJ-310 and OBJ-311 all require a later exit or boundary.
  The final medal settles this objective before the optional result exit.
- SYS-1335 requires an optional timed detour with a restricted retry
  path. The present challenge is the whole selected attempt and can
  be retried directly from settlement.
- SYS-497 immediately restarts after lethal action. The observed failure
  is timer expiry followed by the user's explicit Retry choice.
- INF-067 includes promised rewards and declared threat consequences.
  Here the briefing announces the collection and limit, and the live
  guidance tracks what remains, while scoring is reported later.

## Delta summary

## New facts

- [Observation | Corroborated | High] The scoped Novice trial asks for
  all three medals in 30 seconds with direct movement and contact.
  OT-002–OT-004.
- [Observation | Corroborated | High] Timeout fails. An explicit retry
  starts again, and a complete pickup run settles a score with a
  distinct remaining-time bonus and a visible completion mark.
  OT-005–OT-007.

## New genes

- [Observation | Corroborated | Medium] SYS-1779, INF-569,
  INF-570 and OBJ-328.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_351.

## New questions

- Which clock or contact owns the edge case if acquisition coincides
  with the final tick?
- What remains after a confirmed VMU save and a full reload?
- How do optional controller and assistance settings alter the fastest
  route without changing the collection predicate?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0606`, The Séance of Blake Manor,
  on commercial Windows Steam. Reconstruct a complete early deduction
  from a clue or testimony to its accepted resolution.

## Why this game

- [Hypothesis | Limited | Medium] The opening sets a visible collection
  problem inside an arcade arena and separates full completion, remaining
  time and later replay without requiring combat.
