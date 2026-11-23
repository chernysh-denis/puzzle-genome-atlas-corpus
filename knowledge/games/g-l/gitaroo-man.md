---
game_id: GAME-0663
slug: gitaroo-man
game_title: "Gitaroo Man"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids:
  - COMB-0270
gene_ids:
  action:
    - ACT-879
    - ACT-880
  system:
    - SYS-578
    - SYS-822
    - SYS-1905
    - SYS-1906
  constraint:
    - CON-877
  information:
    - INF-299
    - INF-611
  objective:
    - OBJ-352
  time:
    - TIM-003
---

# Game: Gitaroo Man

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The instrument, song, symbols and displayed point totals are scoped
parameters. No song audio, lyrics or full note chart are reproduced.

## Analysis scope

- Version / ruleset: original English North American PlayStation 2
  commercial disc SLUS-20294, published by Koei in 2002. Use
  Normal Single Play with a DualShock or DualShock 2 in the
  default Type-A control preset. Exact image identity, hardware
  and controller setup on the recorded plays were unverified.
- Structured analysis target: PLAT-PLAYSTATION-2 in
  `knowledge/platforms/games.json`. The legal Sony listing is
  for a later PS4/PS5 port and is outside the ruleset.
- Entry: start a Normal run, pass the separate tutorial and
  enter the first live Charge chart of Stage 1, Twisted Reality,
  with U-1 facing Panpeus. Prior story scenes and memory-card
  contents are setup rather than stage state.
- Primary decision loop: steer the blue sector to follow the
  trace and time the strum or hold against the central point.
  Switch to typed face-button responses when Guard cues arrive.
  Read the role and both power gauges, complete the closing
  phrases, then dismiss the graded success result and decline
  a replay to reach Flying-O.
- Exit: the attempt shows You Win and the stable Stage 1
  report; carry on past the replay and any save choices to
  the next stage. In the primary trace Flying-O is named and
  the first live Charge input is accepted. Stop there.
- Included: Charge, Battle with Attack and Guard, and the
  closing Harmony and End labels; live power across phases;
  timed directional and typed inputs; accepted clear and
  rank breakdown; replay choice and immediate successor.
- Excluded: measuring music or lyrics, full note transcription,
  calibration, exact timing bands, formula coefficients and
  sustained-note penalties, deliberate failing tests, mastery
  of Stage 2, collection thresholds, later modes, regional
  variants, the Japanese trial, PSP and the modern console port,
  and persistence after a save reload.
- Potential scoped modules: the separate opening tutorial,
  a loss and replay of Panpeus, a Master's Play chart, or an
  alternate final depending on documented performance.

## Direct-play status

No direct play or physical-disc authentication. The scanned
North American booklet is the primary control and phase source.
Attributable English PS2 static frames bracket two finished
Stage 1 attempts and the route to Flying-O. The first is
attributed to the North American edition. The second's precise
region was unverified and only corroborates shared visible
mechanics. Frames were inspected in the background without
sound. No controller telemetry, lag or exact power threshold
was measured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GM-001 | The commercial English North American PS2 disc is SLUS-20294, with the printed North American manual. Stage 1 is Panpeus and Twisted Reality. | Observation | Corroborated | High | D1 label scan, P1 cover and p. 14, S1 Stage 1 and W1 10:03. |
| GM-002 | Under Type-A the left stick points the fan-shaped Blue Zone from the fixed Attack Point; time a separate face-button press and hold it for an authored long phrase while following the trace. Any of the four buttons is usable as the strum. | Observation | Corroborated | High | P1 pp. 5, 10, S1 controls, W1 10:30–11:01 and 11:19–11:28. No sustained-note penalty coefficients were measured. |
| GM-003 | Guard sends four kinds of symbols toward the point. Time the corresponding face-button press. Its symbol identity is required independently of direction, and no analog trace is required. | Observation | Corroborated | High | P1 pp. 5, 10–11, S1 phases, W1 11:16 and 11:25. |
| GM-004 | The opening Charge adds power to U-1 for successful phrases. Poor timing or lost alignment can fail to add power. Battle uses both Attack and Guard, with successful attacks reducing the opponent's power, failed attacks costing U-1 power and successful guards avoiding the incoming loss. | Observation | Corroborated | High | P1 pp. 9–11, S1 phases, W1 10:19–11:25. The readings are ordinal rather than fitted values. |
| GM-005 | The interface reports phase and the two live power gauges independently of the score. Charge, Attack, Guard and later Harmony and End visibly change cues across the same attempt. | Observation | Corroborated | High | P1 pp. 9–11, W1 11:04–11:28, 12:34–12:55 and 13:17–13:36. |
| GM-006 | The booklet ties defeat to depletion. In both accepted examples Panpeus weakens, the end chart stays live and U-1 retains power before the win message. A weak or blinking rival gauge does not by itself establish settlement. | Observation | Corroborated | High | P1 p. 11, W1 12:34–13:40, W2 13:35–13:56. The exact trigger for Harmony and the internal depletion threshold were unverified. |
| GM-007 | The report gives four labelled accuracy categories, total points and letter rank. W1 settles 18,005 points at C, with 23 Great, 45 Good, 47 OK and 9 Miss. W2 settles 28,259 points at A with 122 Great, 1 Good, 0 OK and 1 Miss. | Observation | Corroborated | High | P1 p. 10, W1 13:47–13:51, W2 14:03. The source percentages may animate after the counts. |
| GM-008 | Declining a replay can continue from either result to Flying-O. W1 shows an intervening save confirmation and a successful input in the next live Charge chart. | Observation | Corroborated | High | W1 13:54–14:11 and 16:04–16:19, W2 14:05–14:08 and 15:53–16:05. No reload was checked. |

## Basic data

- Release / origin: licensed North American PlayStation 2
  release, developed by iNiS and published by Koei. The
  target is the 2002 English DVD SLUS-20294. Disc catalogues
  disagree on the February day of release.
- Puzzle family: real-time system pressure (FAM-010). Opportunities
  for charge, offense and defense pass on the running chart
  while the player reads and responds to changing controls.
- P1: [Koei's original US instruction booklet, scan](https://archive.org/download/kirklands-manual-labor-sony-playstation-2-usa-4k-version/Gitaroo%20Man%20%28USA%29.pdf).
  Printed p. 5 covers Type-A and the face buttons. Pages 9–11
  describe gauges and timing, the phrase and symbol modes,
  accuracy and stage phases. Its printed Panpeus profile is
  on p. 14.
- P2: [PlayStation's licensed product page](https://store.playstation.com/en-us/product/JP0106-PPSA34548_00-GITAROOMAN000000).
  Identifies the 2026 PS4/PS5 port from the original and
  explicitly notes possible content or function differences.
- D1: [North American disc catalogue and label scans](https://psxdatacenter.com/psx2/games2/SLUS-20294.html).
  Confirms the original media and SLUS-20294 through the
  physical-label images.
- S1: [jmdbcool's contemporary PS2 FAQ](https://gamefaqs.gamespot.com/ps2/469029-gitaroo-man/faqs/16055).
  The March 2002 record independently identifies the song,
  phase roles and controller identity rules. Its proposed
  scoring details and uncertain sustain claims are unverified.
- W1: [LongplayArchive, nikodem123asdf, English NTSC PS2](https://www.youtube.com/watch?v=i7MCB9SBqUQ&t=581s).
  Stage 1 begins after the tutorial. Still frames from 10:19
  through 16:19 establish the C result, replay prompt, save and
  live successor. The source's extra appendix is outside scope.
- W2: [Waxbits, English PS2 playthrough](https://www.youtube.com/watch?v=GkzthT2Pmlc&t=618s).
  Stage 1 frames show the same opponent and labels, an A result
  and Flying-O. Its region and save history are not declared.
- Claim IDs: GM-001–GM-008.

### Reproducible route evidence

1. In Normal Single Play with the Type-A preset, complete the
   separate training and begin Stage 1 against Panpeus. W1 10:03
   shows Intro and the named opponent. Charge becomes live at
   about 10:19, with U-1's visible power still below full.
2. As a phrase approaches, orient the sector along the trace with
   the left stick. Press one of the four face buttons when its
   onset reaches the point. For a long phrase, hold the button
   and follow the trace until release. Watch judgement feedback
   and the refilling player gauge during Charge. W1 10:30 shows
   the characteristic sector and W1 10:40 shows the outcome.
3. Read the change to Battle. In its Attack windows continue
   the traced strum. Successful play now harms the opponent.
   When Guard becomes current, read an arriving symbol and
   press the indicated button at the point, independently of
   the analog trace. W1 11:16 shows a cross during Guard;
   11:19 returns to a judged Attack. Hits and misses can
   affect the live gauges without ending the whole stage.
4. Follow the closing trace. Around W1 12:34 the rival gauge
   flashes with low power, before the Harmony label appears.
   Directional phrases are still present around 12:46. End also
   appears while inputs and accuracy feedback still occur around
   13:17–13:20. Wait for You Win after the chart, visible at
   13:38. Reaching Harmony or seeing a weak rival bar is not
   the accepted endpoint.
5. Read the Stage 1 report after its tally. At W1 13:47, the
   18,005-point result has rank C with 9 missed notes. W2 14:03
   reaches rank A with 28,259 points. Both progress through the
   replay prompt. W1 records a save on an existing card before
   Flying-O. By 16:19 the first charge notes are judged in the
   new stage. W2 independently shows the named next opponent
   with a new score at zero. Stop at the successor transition.

## Mechanical decomposition

### Action Genes

- ACT-879: hold the timed string input while separately steering the
  analog sector about the centre. GM-002, GM-004.
- ACT-880: time the matching face button for the incoming Guard symbol
  without a simultaneous steering requirement. GM-003.

### System Behaviour Genes

- SYS-578: U-1's continuing power acts as a shared health pool across
  the song. Charge recovers the same power reduced by mistakes in
  Battle. On depletion the booklet declares defeat. GM-004, GM-006.
- SYS-822: settle a letter rank from the achieved performance
  independently of the successful result. Two clears show different
  judgement distributions. GM-007, GM-008.
- SYS-1905: judge a phrase at the central point using time and
  compatible analog orientation, with long phrases supplying
  a held span. Penalties for partial holds are untested. GM-002.
- SYS-1906: advance the phase and change the recipient or purpose
  of each judgement while retaining two live gauges. GM-004–GM-006.

### Constraint Genes

- CON-877: the same four buttons are alternatives for a strum,
  but only the displayed symbol matches a Guard response. GM-002, GM-003.

### Information Genes

- INF-299: show the four accuracy categories and overall rank
  on the settled report alongside the point total. GM-007.
- INF-611: read the current role, the timing point, either
  directional or symbolic cues, and two separate gauges. GM-005.

### Objective Genes

- OBJ-352: defeat Panpeus while still viable at the song end, then
  take the accepted report and go on to Flying-O. GM-006–GM-008.

### Time Genes

- TIM-003: the song and current cues advance while the player
  steers, holds, releases or responds with typed Guard input. GM-002–GM-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Live initial Charge with power missing | Match a phrase's direction and timing | A graded response refills the player gauge | GM-002, GM-004 |
| Current Battle Attack | Perform the traced phrase | A judged result can harm the rival or cost the player power | GM-004 |
| Current Battle Guard | Match the symbol at the centre | The eligible attack is avoided or costs player power | GM-003, GM-004 |
| Low rival power and remaining chart | Continue through the closing trace | Visible win with player power remaining | GM-005, GM-006 |
| Accepted win | Let the report settle | Four accuracy counts, total and rank are visible | GM-007 |
| Report complete and replay offered | Decline replay and complete any save choice | Stage 2 with its own opponent and live charge chart | GM-008 |

## Strategic and experiential structure

Charge establishes a margin of error for the duel. During Battle,
the player must distinguish which information selects the input:
continuous direction for phrases, button identity for the
Guard symbols. The next task follows a C or A clear. A weak rival
still leaves enough chart to play.

## Replay and variation

The observed C and A runs clear the same stage despite different
judgement mixes. The game offers a replay before the successor.
The primary run records a save on an existing card. Neither a new
slot's retained data nor the result of selecting Replay was measured.

## Adjacent systems and history

The unnumbered tutorial teaches the input modes before Panpeus.
Later charts change the balance of Charge and Guard. Master's Play
and the 2026 port have distinct rules or availability boundaries.
The first stage's relative timing and motion cues are studied here
without reconstructing the copyrighted chart or listening to it.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-879, ACT-880 | Follow timed phrases with steering and answer specific Guard symbols |
| System Behaviour | SYS-578, SYS-822, SYS-1905, SYS-1906 | Retain the player pool, grade the duel, judge combined phrase input and apply phase-dependent feedback |
| Constraint | CON-877 | Match button identity only when the phase requires it |
| Information | INF-299, INF-611 | See the live cues and power, then inspect the result categories |
| Objective | OBJ-352 | Win the staged duel and proceed |
| Time | TIM-003 | Respond to the progressing chart |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `662` (`GAME-0001`–`GAME-0662`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`3 / 22 = 0.136364`).
- Supported combination subsets: `COMB-0270`.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cuphead (GAME-0277)](../a-f/cuphead.md) | INF-299, SYS-822, TIM-003 | Both act in real time and use a report to show the grade and how it was earned. Cuphead navigates a boss arena and evaluates actions, remaining health and time. Gitaroo Man evaluates judgement categories after a directional and symbol-timed melody battle. | Near, `0.136364` |

## Taxonomy impact

ACT-879 combines timed strum and angular steering during holds.
ACT-508 instead selects fixed frets, and ACT-767 follows a
touchscreen slider with contact. ACT-880 responds to live
converging cues, unlike ACT-533's remembered instructor phrase.
SYS-1905 judges timing plus steering. SYS-1906 changes the effect
of that judgement across combat roles. CON-877 identifies the
input-identity rule within one preset. INF-611 exposes the current
information boundary. The terminal OBJ-352 requires opponent defeat
and the successor, beyond the solo survival of OBJ-215. No earlier
definition or signature is changed.

## Negative results

- Entering Harmony with a flashing rival gauge is not the stage
  clear. Inputs and an End phase are visible before the result.
- A top rank or a clean, miss-free attempt is not mandatory.
- A face button that is interchangeable when strumming is not
  interchangeable for a Guard symbol.
- Exact scoring weights, partial sustain penalties, failure recovery
  and reload behaviour remain unverified.

## Delta summary

Eleven scoped genes include seven new boundaries and four reuses.

## New facts

- Type-A changes which role a face button serves inside one song.
- The opening performance improves the player's margin rather than
  directly damaging the opponent.
- The report grades the execution separately from a clear. A C
  result with nine misses resumes the campaign.

## Principles and design implications

Show the input identity rule where the action is judged. Reusing a
central point can make an interaction switch legible while a clear
role label tells the player which cue to follow. Let a graded result
distinguish quality from the required clear.

## Puzzle or game generation potential

One short original chart could alternate continuous steering and
symbol matching around a single readable point. Carry one margin
through both modes and grade its successful conclusion separately.

## New genes

- ACT-879
- ACT-880
- CON-877
- INF-611
- OBJ-352
- SYS-1905
- SYS-1906

## New combinations

Reuse [COMB-0270](../../combinations/COMB-0270.md). A Stage 1 clear exposes its
four joined accuracy categories and aggregate grade. All 274 verified
combinations were checked. No new definition is proposed.

## Taxonomy changes

[TAXONOMY_CHANGE_409](../../../research/taxonomy-changes/TAXONOMY_CHANGE_409.md).

## New questions

What exact rules make Harmony or End current? Which changes to
alignment inside a held phrase affect scoring, power or only sound?
What part of the saved progress is retained after a normal reload?

## Next recommended game

Dicey Dungeons, full commercial Android release. Trace a complete
early encounter from its dice and equipment through settlement and
the next playable decision.

## Why this game

The first numbered song contains directional timing, button identity
changes, two linked budgets and independently graded execution
within a reproducible first encounter.
