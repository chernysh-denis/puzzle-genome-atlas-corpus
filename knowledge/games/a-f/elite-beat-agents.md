---
game_id: GAME-0566
slug: elite-beat-agents
game_title: Elite Beat Agents
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids:
  - COMB-0270
gene_ids:
  action:
    - ACT-766
    - ACT-767
    - ACT-768
  system:
    - SYS-369
    - SYS-822
    - SYS-1011
    - SYS-1013
    - SYS-1654
    - SYS-1655
    - SYS-1656
    - SYS-1657
    - SYS-1658
  constraint: []
  information:
    - INF-299
    - INF-542
  objective:
    - OBJ-309
  time:
    - TIM-003
---

# Game: Elite Beat Agents

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The three gestures, the chart judge, the draining reserve and the spin-event
quota are distinct causal boundaries. A song, performer, chart coordinate,
colour, point coefficient or difficulty name is a parameter, not a new gene.
No music, lyrics, complete chart or copyrighted game asset is reproduced.

## Analysis scope

- Version / ruleset: original English European Nintendo DS retail release,
  13 July 2007, ordinary single-player Cruisin' difficulty, default stylus
  controls. Target Makes No Difference, the Red Carpet Premiere! Smash Hit
  or Box Office Crash!! mission. This is not the US release date of 2006,
  Ouendan, Ouendan 2, osu!, a fan beatmap or multiplayer.
- Structured analysis target: PLAT-NINTENDO-DS in
  knowledge/platforms/games.json. Nintendo Europe's dated release and
  control explanations establish the selected platform, date and three
  gestures. Nintendo of America's original booklet 61310A is explicitly
  supporting common-rule documentation, not an inspected European cartridge.
  No ROM, hardware timing, exact revision or complete regional chart parity
  is certified.
- Entry: single-player Cruisin' with Walkie Talkie Man already cleared and
  the first ordinary song group open; select Chris Silverscreen's Makes No
  Difference mission and pass its introduction to the first active chart.
  Its prerequisite clear is setup, not an extra performance inside this unit.
- Primary decision loop: read the next numbered spatial target and its
  contracting ring, tap at the scheduled position/time, or maintain contact
  along a phrase ball at its pace. During a spin event repeatedly circle its
  centre. Observe local grade, group refill, combo and Elite-o-Meter risk,
  then reposition for the next event while the song continues.
- Positive exit: complete every section and the final spin/event sequence of
  this whole mission, satisfy the ending clearance condition, observe the
  final story outcome and reach the automatically saved results. Stop after
  the category/grade record is available and return to the map is possible.
  A top score, S rank, perfect combo or an O in every story section is not
  required for ordinary clearance.
- Negative exits: Elite-o-Meter reaches zero during active play, or the
  ending reserve is insufficient for the documented clear condition. Regroup
  Yes restarts the same mission; No returns to the map. An intermediate X
  story result is not by itself a retry checkpoint or automatic game over.
- Reproducible coverage: select the declared song/difficulty. Compare a
  centred timely tap with a mistimed or absent tap, follow a phrase at the
  ball's pace rather than drawing the route early, and retain contact through
  any displayed reversal. Compare a spinner stopped below its quota with a
  cleared spinner and extra rotations before its deadline. Let active time
  pass without a response to distinguish reserve drain from a miss debit.
  Follow a same-colour group through its bonus and distinguish that bounded
  group from the continuing combo. Complete the whole mission and inspect
  hit categories, maximum combo and grade; separately test Regroup and pause
  Retry. These are source-reconstructed test conditions, not a claimed input
  replay or owned execution.
- Included: all three native gesture families; authored chart progression,
  graded local scoring, contact continuity and declared reversal; timed spin
  quota and optional excess bonus; cross-group score streak, colour-group
  refill and elapsed-time reserve decay; section feedback, whole-song clear,
  aggregate performance evaluation, result categories, automatic record save
  and full-song retry/abort. An eligible gesture remains in scope even if a
  particular phrase does not instantiate its optional reversal parameter.
- Time boundary: chart time advances during ordinary play; it does not wait
  for a missed touch. START opens a paused Continue/Retry/Abort menu. Authored
  comic breaks have their own presentation pacing; no unmeasured drain rate
  during a break or frame-perfect resume latency is asserted. Pause does not
  turn a future contact into an already successful response.
- Excluded: completing earlier/later songs, the whole campaign, unlocking
  advanced difficulties or bonus songs, optional replay playback/storage,
  wireless Co-op/Versus/Ghost/Download Play, rumble hardware, manual save-data
  deletion, complete chart transcription, exact hit radii/windows, native
  sampling, scoring coefficients, reserve thresholds/rates and regional
  timing equivalence. Agent animations and O/X comic variants are described
  as feedback, not invented player-controlled movement or a separate attack.
- Potential scoped modules: shared-meter cooperative partitioning, versus
  attacks, saved-ghost competition, or the multi-song cumulative agent-rank
  unlock layer.
- Direct-play status: not conducted. Official control diagrams and original
  booklet pp. 8–17 were read and visually inspected; dated European Nintendo
  material corroborates the gestures and failure rule. Written player accounts
  and two static ten-second storyboard sheets around a later emulated Makes
  No Difference recording corroborate presentation only. They do not certify
  Cruisin', the European ROM or exact contacts. No video/audio was played,
  no emulator was launched and no desktop focus was taken.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| EBA-001 | Nintendo's English European retail release is 13 July 2007 on DS; the selected version is distinct from the 2006 US origin. | Confirmed | Corroborated | High | P1, P2, P3 |
| EBA-002 | Numbered spatial Hit Markers use contracting timing rings; correct timing changes local point grade, with 300 documented as the best ordinary hit. The chart continues past missed events. | Observation | Corroborated | High | P1, P4, P5 pp. 12–14, S1 |
| EBA-003 | Phrase Markers require following the moving ball while maintaining contact; a shown return arrow requires following it back rather than lifting at the first end. | Observation | Corroborated | High | P4, P5 pp. 14–15, S2 mechanics |
| EBA-004 | A spinner accepts either rotation direction; fill its separate timed quota, then extra rotations can earn bonus points. Expiring underfilled is not indefinite continuation. | Observation | Corroborated | High | P4, P5 p. 15, S1, S2 |
| EBA-005 | The song reserve drains with time, is affected by response quality and miss penalties, fails at zero and must be filled enough at the ending. No exact ending cutoff or decay rate is verified. | Observation | Corroborated | High | P2, P5 pp. 12–13, S1 |
| EBA-006 | Colour-bounded Beat/Elite Beat bonuses refill the reserve more than normal hits; the cross-group unbroken combo separately scales scoring. Exact coefficients and partial-phrase checkpoints remain unverified. | Observation | Corroborated | Medium | P5 pp. 12–15, S1, S3, S5 indexed only |
| EBA-007 | Story sections expose O/X results; a local X can continue while the reserve remains live. Whole-mission results expose hit classes, max combo and an aggregate grade, separately from cumulative agent rank. | Observation | Corroborated | Medium | P5 pp. 16–17, S1, S2; V1 illustrative only |
| EBA-008 | Regroup offers Yes/No; pause offers Continue, full-mission Retry or Abort. Section breaks are not retry checkpoints. | Confirmed | Direct | High | P5 pp. 8–9, 13, 17 |
| EBA-009 | Displaying single-player results auto-saves eligible score/ranking data for later Hi-Score access. No mid-song manual save or save-format guarantee follows. | Confirmed | Direct | High | P5 pp. 10–11, 16–17 |
| EBA-010 | Makes No Difference on Cruisin' is an early unlocked complete performance with phrase events and a final spinner. Walkie Talkie Man is not silently supplied with absent phrase events. | Observation | Corroborated | Medium | S4 indexed song section, S2 mission identity, P5 generic controls; V1 does not certify this difficulty |

## Basic data

- iNiS / Nintendo. The regional target and official dated statements are
  separate from the supporting 2006 US manual and early US-copy review.
- Family: real-time system pressure, FAM-010, reused from independent
  chart, traversal and live-simulation carriers.
- Primary sources, accessed 2026-11-20:
  - P1: [Nintendo UK product page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Elite-Beat-Agents-270660.html),
    release date, platform and the three touch-control classes.
  - P2: [The beat goes on!, 6 June 2007](https://www.nintendo.com/en-gb/News/2007/The-beat-goes-on--250122.html),
    European release, three markers, reserve failure and separate multiplayer.
  - P3: [In Shops Now, 13 July 2007](https://www.nintendo.com/en-gb/News/2007/In-Shops-Now-Elite-Beat-Agents-249706.html),
    dated European retail confirmation.
  - P4: [Feel the Beat!, 3 July 2007](https://www.nintendo.com/en-gb/News/2007/Feel-the-Beat--249574.html),
    ring target, 300 timing grade, paced phrase trace and timed spin bonus.
  - P5: [original Nintendo instruction booklet 61310A](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/DS_Elite_Beat_Agents?_a=DATC1RAAZAA0),
    pp. 8–17: controls, automatic save, HUD, grades, drain, marker types,
    difficulty/selection, section O/X, result and pause. Its printed-US identity
    is visible; its manual-production title is not a different game title.
- Supporting first-hand accounts, accessed 2026-11-20:
  - S1: Gavin MacDonald, [Pocket Gamer review, 12 December 2006](https://www.pocketgamer.com/elite-beat-agents/review/),
    relevant gameplay paragraphs read fully. It explicitly reviews a US copy;
    its then-predicted spring European date is superseded by P1–P3.
  - S2: Zach Long / Galcian, [FAQ mechanics and mission information](https://www.supercheats.com/nintendods/walkthroughs/elitebeatagents-walkthrough02.txt),
    full mechanics and relevant mission headings read. Its ASCII tutorials
    are Breezin', not the exact Cruisin' chart. No lyrics or chart is copied.
  - S3: [Gogglebob's cartridge account, 3 February 2017](https://www.gogglebob.com/2017/02/03/fgc-237-elite-beat-agents/),
    relevant full account read, corroborating combo-based score risk.
  - S4: gam3fr3ak13, [2007 guide](https://gamefaqs.gamespot.com/ds/933052-elite-beat-agents/faqs/47055),
    indexed passages only; the full page is restricted. The Cruisin' Makes No
    Difference section identifies its first phrase markers and later spinner.
  - S5: kaokengoku2, [Score FAQ](https://gamefaqs.gamespot.com/ds/933052-elite-beat-agents/faqs/46064),
    indexed passages only, distinguishing counted phrase subevents and combo
    scaling. Its numerical formula is not a native measured finding here.
  - V1: Emu Gamer, [later full playthrough](https://www.youtube.com/watch?v=QBPDw7C9T9M),
    6,151 seconds, Makes No Difference chapter at 17:16. Only sheets spanning
    approximately 16:40–22:30 were visually inspected at ten-second intervals.
    The 159×90 cells show song introduction, active three-agent chart,
    section panels and saved result before the next song. They cannot resolve
    exact input, difficulty, region or hardware. No audio/video playback.
- Claim IDs: EBA-001–EBA-010. Original pictures remain observation evidence,
  not artwork inputs or redistributed assets.

## Mechanical decomposition

### Action Genes

- ACT-766: time contact on the correct numbered spatial marker.
- ACT-767: sustain paced contact along the phrase ball's route and reversal.
- ACT-768: continuously circle an active spinner in either direction.
- These do not control an independent agent body or reproduce a teacher turn.
- Parameters: screen position, current chart event, contact, pace and direction.
- Claim IDs: EBA-002–EBA-004.

### System Behaviour Genes

- SYS-1654 judges the advancing authored touch chart and credits local grades.
- SYS-1013 is reused unchanged for graded-response reserve changes and live
  failure; SYS-1655 adds independent elapsed-time drain to that reserve.
- SYS-1656 awards a bounded colour-group reserve refill.
- SYS-1657 accumulates the separate spinner quota and optional excess bonus.
- SYS-1011 is reused unchanged for the unbroken note-streak score multiplier:
  the event-count steps and eligible note classes are parameters, not a claim
  that EBA uses Guitar Hero's specific 2×–4× plateaux. Exact scaling coefficients
  are not asserted. The coloured group is not the entire current combo.
- SYS-822 is reused for aggregate performance grading from how the song was
  performed. It is not SYS-1613's tier mapping from accumulated score alone.
- SYS-1658 commits settled mission/difficulty records. SYS-369 is reused for
  an explicit retry restoring the fixed authored mission-start anchor: no
  later comic section is assumed to become a checkpoint.
- Resolution order: scheduled eligible contact → local judgement/score and
  streak update → eligible group/spin credit and live reserve effects → next
  authored event or early failure → final clear/grade/record settlement.
  This is causal order, not a certified within-frame native callback order.
- Claim IDs: EBA-002–EBA-009.

### Constraint Genes

- No additional Constraint gene. Eligibility and path contact are expressed
  by the admitted action/judgement boundaries; reserve depletion belongs to
  its updating system and the ending condition to the Objective. Hardware
  having one stylus is not invented as a new strategic resource gene.
- Claim IDs: EBA-002–EBA-005.

### Information Genes

- INF-542 shows the local numbered timing surface, independent gauges, score,
  combo and section feedback without exposing future chart or exact windows.
- INF-299 is reused unchanged for hit categories, maximum combo and aggregate
  result together at the terminal report.
- Claim IDs: EBA-002–EBA-007.

### Objective Genes

- OBJ-309: complete the entire mission with a live and acceptable ending
  reserve. Early local success and high score are neither whole-song clears
  nor mandatory perfect outcomes. Manual wording supports an ending clearance
  requirement; no exact percentage is promoted into fact.
- Claim IDs: EBA-005, EBA-007.

### Time Genes

- TIM-003 is reused for fixed musical progress with concurrent timed input.
  The documented pause command is its pause parameter, not a new turn system.
- Claim IDs: EBA-002–EBA-005, EBA-008.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The next numbered hit's ring reaches its boundary | Touch that target at the eligible time | A local grade and points are credited; later chart time continues | Position and time jointly matter | EBA-002 |
| A scheduled target passes untouched | Provide no valid response | The event misses, reserve/streak consequences apply and the chart continues | The timeline does not wait | EBA-002, EBA-005, EBA-006 |
| A phrase start is due | Contact it and follow the ball at its pace | The path is evaluated through its timed traversal | Drawing it all early is not equivalent | EBA-003 |
| An admitted phrase shows a return arrow | Maintain contact and follow the reversal | The return traversal remains part of the same phrase | The first physical endpoint is not always release | EBA-003 |
| A spinner is below quota | Rotate in either accepted direction until full before expiry | Its event requirement clears | Local spin fill is not song health | EBA-004 |
| The spinner is already full but time remains | Continue rotating | Optional excess points can accrue | Clearance and optimisation are separate | EBA-004 |
| Active song time runs with no new hit | Wait | The reserve decreases even before the next missed-event penalty | Elapsed time itself has a cost | EBA-005 |
| A same-colour group reaches its eligible end with strong grades | Complete it accurately | The appropriate group bonus provides an enhanced refill | Colour-group quality differs from cross-group streak | EBA-006 |
| A section displays X but reserve remains live | Continue the next authored section | The performance can continue | Local comic failure is not automatically game over | EBA-007 |
| Reserve reaches zero | Select Regroup Yes | The same mission begins afresh, not at the last section | Whole-song retry is explicit | EBA-008 |
| A live performance is paused | Choose Retry rather than Continue | The current song restarts from its beginning | Pause is not a new note checkpoint | EBA-008 |
| The full song meets its clear condition | Observe final story and results | Hit categories/grade are shown and eligible record data auto-save | Complete performance has a retained terminal | EBA-007, EBA-009 |

## Strategic and experiential structure

- Local: place the stylus for the next active number, use the ring as timing
  information and avoid confusing upcoming targets with the current one.
- Medium horizon: preserve reserve through whole phrases and colour groups;
  a broken combo loses score scaling but need not end a still-live mission.
- Full loop: clear all sections, not only one comic panel; choose between
  ordinary passage and score/grade refinement over full-song retries.
- Failure attribution: local feedback, combo break and reserve decline make
  risk visible, but no exact native hit window is claimed. Small storyboard
  cells are not used to audit beat accuracy or latency.
- Trust: section X, grade, cumulative agent rank and best score are distinct
  outputs. Do not equate a lower grade with an already proven song failure.
- Claim IDs: EBA-002–EBA-009.

## Replay and variation

- The selected difficulty's authored chart is fixed, not procedurally
  generated after a miss. Contact timing and maintained gesture trajectories
  vary with execution. Other difficulties change the chart outside this unit.
- Replays improve survival, group refills, combo and final evaluation; saved
  replay playback is optional and not silently analysed as manual play.
- Claim IDs: EBA-002, EBA-006–EBA-010.

## Adjacent systems and history

- Ouendan is the related Japanese predecessor, not the same title, story or
  regional release. osu! is not a substitute implementation of this cartridge.
- Existing rhythm records are checked at their actual boundaries: teacher
  calls, floor directions, fret/strum notes and flicked assembly do not become
  spatial stylus taps merely because all use music.
- Claim IDs: EBA-001–EBA-004. Detailed corpus interpretation follows only
  mathematically selected neighbours, not a manually chosen genre list.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-766, ACT-767, ACT-768 | Chart geometry is a parameter |
| System Behaviour | SYS-369, SYS-822, SYS-1011, SYS-1013, SYS-1654, SYS-1655, SYS-1656, SYS-1657, SYS-1658 | Exact native rates and coefficients unmeasured |
| Constraint | none | No invented finite life stock |
| Information | INF-299, INF-542 | Ring radius and visible preview are parameters |
| Objective | OBJ-309 | Perfect score and S rank optional |
| Time | TIM-003 | Pause is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `565` (`GAME-0001`–`GAME-0565`).
- Exact genome matches: none.
- Tied near matches: `GAME-0372` — Guitar Hero III: Legends of Rock (`4 / 23 = 0.173913`).
- Supported combination subsets: `COMB-0270`.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0372` — Guitar Hero III: Legends of Rock | SYS-1011, SYS-1013, INF-299, TIM-003: chart-note streak scoring, response-driven survival gauge, a category-bearing result and musical-time input. | EBA times spatial taps, paced contact and a spin quota and adds independent reserve decay. The guitar packet uses fret/strum and sustain, Star Power and different gauge/scoring parameters; its score-tier stars are not EBA’s hit-quality grade or colour-group refill. | Tied near maximum, 4 / 23 = 0.173913. |

### Preserved research notes

- New genes: ACT-766–ACT-768, SYS-1654–SYS-1658, INF-542 and OBJ-309.
- Classification result: New gene.
- Evidence and reasoning: the complete performance separates timed spatial
  taps, paced retained contact and circular quota input from the chart,
  draining reserve, group refill and retained result. Six existing
  definitions remain unchanged. COMB-0270 is reused for aggregate performance grading plus its exposed contributing categories. No new combination is created.

## Taxonomy impact

- Registry changes: ten Active definitions; six reused unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_312](../../../research/taxonomy-changes/TAXONOMY_CHANGE_312.md).
- No previous signature, definition, lifecycle, history or published mapping
  is changed. No external novelty is claimed.

## Negative results

- None. Boundary-fit rejections are documented in TAXONOMY_CHANGE_312; no
  previously accepted claim is overturned and no new negative-result ID is
  manufactured from a local selection choice.

## Delta summary

## New facts

- [Observation | Corroborated | High] EBA-002–EBA-005 distinguish the three
  gestures, independent spin quota and actively draining survival reserve.

## New genes

- [Observation | Corroborated | Medium] Ten bounded additions in
  TAXONOMY_CHANGE_312. Historical native arithmetic remains outside certainty.

## New combinations

- [Observation | Corroborated | High] No new combinations; verified subset
  results are owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_312 adds the typed
  boundaries without revising any predecessor.

## New questions

- Exact European cartridge hit windows, score/partial-phrase arithmetic,
  ending clearance threshold and section-break reserve pacing require an
  authorised native instrumented test; current sources do not settle them.

## Next recommended game

- [Hypothesis | Limited | Medium] Original standalone Quest SUPERHOT VR,
  GAME-0567, completes the approved nine-game Selection 045.
- Optimisation criterion: contrast tracked embodied combat and movement-linked
  time with timed contact on an independently advancing musical chart.
- Expected information gain: distinguish native Quest VR input and fight
  scope from the existing flatscreen and PCVR interpretations.
- Backlog impact: stop after that ninth unit; no tenth title is selected.

## Why this game

- [Hypothesis | Limited | Medium] A complete DS touch-rhythm performance adds
  spatial approach judgement and sustained/circular gesture boundaries to an
  existing music corpus while reusing general streak, grading, report and
  real-time definitions. Exact chart certification remains a stated limit.
