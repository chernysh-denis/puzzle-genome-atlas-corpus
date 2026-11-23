---
game_id: GAME-0595
slug: rhythm-doctor
game_title: "Rhythm Doctor"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-791
  system:
    - SYS-736
    - SYS-822
    - SYS-1455
    - SYS-1755
  constraint: []
  information:
    - INF-559
  objective:
    - OBJ-258
  time:
    - TIM-003
---

# Game: Rhythm Doctor

Use the [canonical vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The ordinal of the response, pulse spacing, sound, judgement tolerance and
grade letters are parameters. This record reproduces no audio or event chart.

## Analysis scope

- Version / ruleset: English commercial base game on Xbox Series X|S,
  Microsoft product 9PHVMW9R92FX, listed for 18 December 2025. Solo Story
  Mode, ordinary difficulty and speed, first Day Shift case 1-1, Samurai
  Techno. Microsoft lists 18 December; the 29 December developer notice
  refers to earlier customers. A purchase and play-through on Series X
  was already reported on 21 December. Exact installed console build,
  package hashes and one-to-one chart parity with Steam are unverified.
- Structured analysis target: `PLAT-XBOX-SERIES` in
  [platform coverage](../../platforms/games.json).
- Entry: on a new solo Story slot, after accepting startup settings and
  completing any offered latency setup, take Paige's first seventh-beat
  lesson. The preceding setup aligns feedback to sound and input. Keep
  its settings fixed while testing the timing rule.
- Primary decision loop: take the phase from the sequence of lead
  pulses, let those pulses go by, and press A once on the anticipated
  seventh beat. Read the heart and the response, then find the phase
  again for the next group. The phrase can start at a different point
  in the music, so holding a count anchored only to the first phrase
  can put the response out of time.
- Positive exit: finish the first song with the ordinary passing grade
  of B or better, accept the result, and reach the ward with 1-2
  Intimate now available. Stop before entering 1-2.
- Negative exit: an early lesson miss brings guidance and another
  opportunity. A local miss during the tracked performance contributes
  to its evaluation and does not itself clear or terminate the chart.
  A settled grade below the ordinary passing threshold does not open
  the fresh-slot successor. Do not interpret an F as evidence of a
  separate live survival meter in 1-1.
- Included: the coached first responses and their correction, lesson
  completion, single-button seventh-beat input, lead and judgement
  cues, authored real-time performance and phase changes, terminal
  evaluation and the ordinary successor.
- Excluded: numerical latency or judgement windows, exact miss
  thresholds or pause/restart persistence on Xbox, save-file internals,
  modifier difficulties and speeds, skipped-beat rules introduced in
  1-2, bosses, Night Shift, multiplayer, editor and custom levels,
  console patches beyond the evidence, PC and Xbox One as targets.
- Potential scoped modules: the first skipped-beat lesson; a later
  chart with a separate boss health condition or multiple rows.
- Direct-play status: no console or executable was operated. A
  firsthand Series X review establishes the A input and console
  experience. Static release-window PC story traces corroborate the
  shared sequence through the first post-rank ward. The Xbox launch
  montage is first-party context and does not present a continuous
  first-case run. No audio or video was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RD-001 | Microsoft lists the commercial Xbox build for 18 December 2025. The December 6 PC timing did not apply to Xbox. A December 21 Series X owner report predates the December 29 console announcement. | Confirmed | Direct | High | P1–P3, X1, R1 |
| RD-002 | Playing the chart on Xbox uses one button, A on the documented controller; the ordinary Story menus can require further buttons. Story Mode is a released console feature. The developer says that the custom editor is absent on console. | Confirmed | Direct | High | P1, P3, X1 |
| RD-003 | The first lesson teaches a seventh-beat response after six lead pulses. The written lesson branches provide a corrective reminder when the early response misses, and repeated valid hits lead to the final response with reduced counting help, then automatic entry to 1-1. | Observation | Corroborated | Medium | P1, W1 0:45–2:00, W2 2:30–3:20, C1, C2 |
| RD-004 | During the solo 1-1 chart one rhythmic row identifies the target. Players withhold input during its lead pulses, then hit the seventh. The row displays a pulse travelling toward the heart and local hit or miss feedback. Timing differs with the phase of the current pulse group. | Observation | Corroborated | Medium | P1, P3, X1, W1 2:00–3:05, W2 3:20–4:20, C2, C3 |
| RD-005 | The song progresses while input is available and settles to a result. 1-1 may show a grade below S while still granting the ordinary clear; a recorded full-release A+ is followed by Paige's confirmation and an available next patient. | Observation | Corroborated | High | W1 3:15–3:55, W2 4:20–5:40, W3 0:15–1:38 |
| RD-006 | The developer's documented ordinary story rule requires B or above. Later documentation corroborates it for Act 1. 1-1's grade list includes below-B outcomes; a low result is distinct from a failed teaching prompt. Exact boundary miss counts and an Xbox-native failed-attempt trace remain unverified. | Observation | Corroborated | Medium | P4, C3, C4, RD-005 |
| RD-007 | After the accepted case the ward now offers Logan's case, 1-2 Intimate. The pager exposes the state of the case and the written post-clear result, while top-grade indicators are distinct from ordinary progress. | Observation | Corroborated | Medium | W1 3:20–3:55, W2 4:40–5:35, C3, C4 |

## Basic data

- 7th Beat Games, with console port work credited by the developer. The
  North American Xbox product establishes the Series X|S target.
  `FAM-010` applies because authored opportunities advance independently
  of the player's response.
- P1: [Microsoft Store official game entry](https://www.xbox.com/en-US/games/store/Rhythm-Doctor/9PHVMW9R92FX).
  Date, product, platforms, solo play and the basic seventh-beat rule.
- P2: [7th Beat Games' 5 December notice](https://www.youtube.com/watch?v=D9bseUbE534).
  Description documents the late console certification delay and the
  separate Steam launch.
- P3: [7th Beat Games' 29 December Xbox announcement](https://www.youtube.com/watch?v=rsE1SQFCMdw).
  Description confirms Story Mode, supported controllers, consoles and
  earlier purchases. The announcement does not reset the release date.
  Silent stills establish the look of the heart row and timing flash
  across the launch examples.
- P4: [Developer fizzd on ordinary story progression](https://steamcommunity.com/app/774181/discussions/0/3172198151258798308/).
  Earlier Steam statement, used with release-era observations and the
  later Act 1 rank description. The comment does not prove Xbox values
  for a particular miss count.
- X1: [Leo Macleod's firsthand Series X review](https://majesticaccessibility.substack.com/p/rhythm-doctor-accessibility-review),
  21 December 2025. English game from a paid purchase, with A on
  Xbox Adaptive Controller, audio-led timing and optional settings.
- R1: [Pure Xbox contemporaneous availability check](https://www.purexbox.com/news/2025/12/rhythm-doctor-has-outstanding-reviews-and-its-just-launched-as-an-xbox-console-exclusive),
  19 December 2025. Reports live availability and the revised 18
  December launch.

### Reproducible route evidence

- W1: [TNT Dragon's full-release Act 1 trace](https://www.youtube.com/watch?v=Zw9Rh067byk),
  8 December 2025. Status and dialog at 0:45–1:55, 1-1 at 1:57,
  A+ near 3:20, then 1-2 Intimate in the ward near 3:50. The
  pictured spacebar and earlier calibration state are PC evidence.
- W2: [DaftHusky's 1.0 story run](https://www.youtube.com/watch?v=rf6mWbB_H6M&t=150s),
  9 December 2025. Stills corroborate the coached section, heart row,
  environmental changes, successful handoff and new pager case. A
  displayed PC prompt is not an Xbox binding.
- W3: [terux's release-window perfect route](https://www.youtube.com/watch?v=3Z8jRtJR4bg&t=16s),
  10 December 2025. A separate scoring case for 1-1, followed by
  a Night Shift replay in the recording. Its already populated
  profile is not evidence of the fresh-slot unlock order.
- C1: [Act 1 lesson transcript](https://wiki.rhythm.cafe/index.php?title=Act_1&oldid=4039).
  Includes the offered calibration, reminders after misses and
  the final response followed by direct entry to the performance.
- C2: [Classic beat structure](https://wiki.rhythm.cafe/index.php?title=Classic_Beats&oldid=4345).
  Documents the phase-relative input. The full list of alternate
  pulse patterns is not imported here.
- C3: [1-1 position in story and result bands](https://wiki.rhythm.cafe/index.php?title=Samurai_Techno&oldid=4505).
  Identifies Day Shift and describes the shift of rhythmic phase and
  post-clear handoff.
- C4: [In-game rank and Act 1 progression documentation](https://wiki.rhythm.cafe/page/Achievements).
  Supports B or higher as the ordinary passing grade and distinguishes
  the pager's clear mark from a perfect one.

## Mechanical decomposition

### Action Genes

- ACT-791 commits one press to the terminal pulse of the heard phrase.
  No target movement, button selection or maintained contact is
  required in this case (RD-002–RD-004).

### System Behaviour Genes

- SYS-736 keeps the introductory teaching stage until the required
  responses are performed, then enters the scored case. SYS-1455
  provides further practice after the prompt is missed (RD-003).
- SYS-1755 advances successive scheduled pulse groups and judges
  their expected response times. It does not treat the regular lead
  pulses as independent notes (RD-003–RD-005).
- SYS-822 settles the finite performance into its aggregate
  letter grade (RD-005–RD-006).

### Constraint Genes

- No separate constraint is needed. The local response predicate is
  in SYS-1755 and the terminal qualification in OBJ-258.

### Information Genes

- INF-559 combines the lead rhythm and local heart-row cue with
  response feedback. Early instruction uses counting help and then
  removes it. The hit location is inferred from the current phrase,
  while the terminal grade settles the complete activity
  (RD-003–RD-005).

### Objective Genes

- OBJ-258 requires completing the case with a passing terminal grade
  to release the ordinary next case (RD-005–RD-007).

### Time Genes

- TIM-003 applies during the running chart; each opportunity retires
  as the next scheduled group approaches (RD-004–RD-005).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| New slot, initial configuration accepted | Confirm the available setup and advance to Paige's first lesson | The instruction introduces one response after a six-pulse lead-in. This teaching sequence precedes the graded chart | RD-002, RD-003 |
| Coached phrase before a valid late response | Omit a response while reminders remain active | The lesson has a corrective reminder branch and presents another chance. The graded 1-1 result has not started | RD-003 |
| Practised seventh-beat rule with counting help | Complete the required guided responses and then match the pulse without the final counting help | The lesson settles and goes directly to Samurai Techno | RD-003 |
| Live single row in 1-1 | Let the lead pulses pass, then press A when their response beat is due | A judged hit resolves that phase. A shifted next phrase must be read again, and an isolated miss leaves later opportunities | RD-004, RD-005 |
| End of the chart | Accept the ordinary passing result, documented as A+ in one full-release trace | Paige confirms the treatment and the ward offers 1-2 Intimate. A perfect mark is not required | RD-005, RD-007 |
| First clear still pending and settled grade below B | Attempt to progress with that result | The ordinary story boundary remains unmet. This row describes the documented threshold, not a verified Xbox failure recording | RD-006 |

## Strategic and experiential structure

The player has one timing decision. Signals at the start of each
group establish a clock against which waiting and the final press make
sense. An incorrect phase can explain a miss even if the player
maintains an even beat. The early lesson evaluates progress separately
from the chart: correcting a rehearsal response enables entry, while
recovering within a song can still produce a passing result.

## Replay and variation

One trace ends with A+ and an ordinary handoff instead of a perfect
result. A second performance can improve the rank without changing the
prerequisite for the first handoff. Exact miss cutoffs, early termination
at the lowest band and persistence after a failed Xbox run need a native
trace. The turn from a room to a space background in the story trace
changes the presentation while the heart-row control remains.

## Adjacent systems and history

The December full-release store entry distinguishes console Story play
from the older Flash and PC prerelease forms. Later patient cues, the
Night Shift variant and console modifier settings do not extend the
present genome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-791 | Single input on the expected last pulse |
| System Behaviour | SYS-736, SYS-822, SYS-1455, SYS-1755 | Gated practice, result aggregation, guided correction and live group judgement |
| Constraint | None | Local and terminal predicates are captured by their owning rules |
| Information | INF-559 | Rhythmic lead, current target response and changing counting help |
| Objective | OBJ-258 | Complete the first chart with a passing grade |
| Time | TIM-003 | Continual chart advancement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `594` (`GAME-0001`–`GAME-0594`).
- Exact genome matches: none.
- Tied near matches: `GAME-0454` — Rhythm Heaven (`3 / 11 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [GAME-0454 Rhythm Heaven](rhythm-heaven.md) | SYS-822, OBJ-258, TIM-003 | Both settle a live rhythmic exercise with a grade that controls ordinary progression. Built to Scale asks for a spatial stylus flick to join plates. Samurai Techno needs one untargeted press at the terminal pulse of each group, following a staged lesson. | 3 shared of 11; Jaccard 0.272727 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_341](../../../research/taxonomy-changes/TAXONOMY_CHANGE_341.md)
  adds three bounded rules. It changes no existing signature.

## Negative results

- The ordinary ending requires a passing grade. Merely finishing the
  song or acknowledging a practice hint is insufficient.
- Introductory recovery is a further chance to answer, without evidence
  that every later missed button is refunded or causes a reset.
- There is no supported reason to add a separate spatial input, live
  reserve, sustained hold or chart-editor rule to this signature.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] The group-relative press can
  stay the same when the phrase shifts within the music. The coached
  lesson and the terminal grade use different advancement checks.

## New genes

- [Observation | Corroborated | Medium] ACT-791, SYS-1755 and INF-559
  capture a one-button response, a group judge and current rhythmic
  information, respectively.

## New combinations

- [Observation | Corroborated | High] No verified combination is a
  subset of the scoped signature. No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] Three definitions are added.
  The older definitions and signatures are preserved.

## New questions

- Measure an Xbox-native first play with an intentionally omitted
  series of responses and determine the retry and saved-case state.

## Next recommended game

- [Hypothesis | Limited | Medium] Custom Robo on the North American
  Nintendo GameCube release. Check an entire early Holosseum battle
  and its equipment and preparation decisions.

## Why this game

- [Hypothesis | Limited | Medium] A single input leaves room for a
  substantial timing decision when a series of pulses defines the
  response phase relative to each group.
