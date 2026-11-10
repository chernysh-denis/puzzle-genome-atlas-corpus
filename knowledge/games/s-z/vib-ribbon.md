---
game_id: GAME-0467
slug: vib-ribbon
game_title: Vib-Ribbon
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-617
  system:
    - SYS-1219
    - SYS-1220
    - SYS-1221
  constraint: []
  information:
    - INF-192
    - INF-444
  objective:
    - OBJ-002
    - OBJ-264
  time:
    - TIM-003
---

# Game: Vib-Ribbon — one custom-CD track

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The selected song, CD identity, button labels, exact timing windows and score values are parameters, not separate genes. No music or lyrics are reproduced.

## Analysis scope

- Version / ruleset: original English PAL PlayStation *Vib-Ribbon* retail rules, `Play With Own Choice Of CD` → `Single Track`, one selected ordinary audio-CD track. The European disc identifier `SCES-02873` is a cataloguing lead, not a locally verified disc hash. The exact executable revision, CD, track audio and game-generated obstacle list were not obtained.
- Structured analysis target: `PLAT-PLAYSTATION` in [platform coverage](../../platforms/games.json), not later PSN wrappers or a port.
- Entry: after the game has loaded and the player selects one track from an inserted audio CD, at the first ordinary control of Vibri on that track's ribbon before its first obstacle.
- Primary decision loop: listen to the selected track and read the approaching ribbon shape; press the mapped button for block, loop, pit or wave, or press the two mapped buttons together for a composite, at the obstacle's arrival; observe pass or mistake, the current character form and accumulated score, then adapt before the next shape while the track continues.
- Positive terminal: reach the end of the selected track without the final form failing, then receive the run's result and score. No particular high-score rank or Queen form is required.
- Negative terminal: repeated misses can step the character downward from rabbit through frog to worm; continued mistakes at the lowest form end the run before the track ends. One miss is not instant Game Over. The exact thresholds and all possible partial states are not verified from an executable.
- Included: track selection from an inserted audio CD; music-conditioned custom-course construction with a pattern-script contribution; four basic ribbon obstacles and their pairwise composites; mapped timed single and simultaneous inputs; local pass/miss response; clear/mistake sequences changing form and score; bounded visual lookahead and audible rhythm; track-end result and early failure.
- Excluded: the six built-in tracks and their authored pattern scripts, `All Tracks`, `Speed`, `Auto`, language menu, specific high-score thresholds, freestyle bonus inputs, exact generator algorithm, exact timing window, precise score formula, disc-swapping hardware timing, later releases, copyrighted audio and song lyrics. Exclusion does not assert these features are absent from the complete game.
- Reproducible parameterisation: record the original retail disc revision, compatible console, audio CD identity and PCM hash, selected track index and duration, control configuration, input timestamps, generated obstacle sequence, form after each judgement and terminal score. These are requirements for a future executed replication; no such trace was available here. Because the custom script can begin at a selected start segment, identical song input alone is not asserted to reproduce the same obstacle sequence.
- Potential scoped modules: one specific built-in Bronze track, `All Tracks` carry-over, `Speed`, optional freestyling, region comparison and direct executable analysis.
- Direct-play status: no PlayStation, disc, executable, controller trace, audio CD, game screenshot, video or audio was played or inspected. This is a bounded documentary reconstruction from PlayStation's product-history description, a contemporary PAL player guide and independently documented original-disc script structure.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VR-001` | The original PlayStation version accepts a player's audio CD; the PAL menu offers `Play With Own Choice Of CD` and `Single Track`. | Observation | Corroborated | High | P1, S1 |
| `VR-002` | The ribbon contains block, pit, loop and wave obstacle classes plus pairwise combinations; each class maps to a timed button or two-button chord. | Observation | Corroborated | High | S1, R1 |
| `VR-003` | The original PAL script contains distinct built-in and custom-CD tracks; custom-CD pattern and control segments admit variation including a selected start position, so a single fixed authored chart is not established for this mode. | Observation | Corroborated | Medium | R1 |
| `VR-004` | Miss sequences degrade Vibri through rabbit, frog and worm; successful sequences restore form, and continued mistakes at worm end the attempt. | Observation | Corroborated | Medium | S1, P1 |
| `VR-005` | Successful obstacle responses contribute to score, with improved form changing scoring; finishing the selected track reaches a scored result. | Observation | Limited | Medium | S1 |
| `VR-006` | Exact audio-to-obstacle mapping, event timestamps, input tolerances, form thresholds and score coefficients remain unmeasured for this edition. | Observation | Limited | High | R1, R2 |
| `VR-007` | The bounded decision problem is a music-conditioned, forward-moving obstacle run with form-dependent survival, not a fixed chart copied from the built-in songs. | Strong Pattern | Corroborated | Medium | `VR-001`–`VR-005` |

## Basic data

- Release / origin: original PlayStation *Vib-Ribbon* by NanaOn-Sha, English PAL edition. The exact PAL disc revision is not asserted.
- Puzzle family: `FAM-010`, real-time system pressure. The next input must be prepared while the track and obstacle approach continue.
- **[P1]** [PlayStation's retrospective on Vib-Ribbon](https://blog.playstation.com/archive/2014/10/06/ps-one-classic-vib-ribbon-arrives-ps3-ps-vita-next-week), for the original PlayStation identity, music-CD feature and changing character form; accessed 2026-10-01. The later availability announcement is not substituted for a PAL instruction manual.
- **[S1]** [Sophie Cheshire's contemporary European guide](https://gamefaqs.gamespot.com/ps/199188-vib-ribbon/faqs/10906), revised 2001, for PAL menu options, controls, obstacles, form progression and scoring description; accessed 2026-10-01. Player testimony corroborates rules but does not measure executable constants. Its reproduced lyrics were not used.
- **[R1]** [Open-Ribbon's original-disc FSL documentation](https://open-ribbon.github.io/documentation/file-types/fsl/), for PAL `SYSTEM3.FSL` track structure, four primitives and six pairs, fixed/distributed patterns and custom-CD segment selection; accessed 2026-10-01. This is independent reverse engineering, not our own disc extraction or a full audio analyser specification.
- **[R2]** No original disc, binary, music input or audiovisual gameplay trace was inspected locally.

## Mechanical decomposition

### Action Genes

- New `ACT-617`: a player presses the obstacle's mapped controller input at encounter time, using a simultaneous pair for a composite. The four button labels are parameters of one response vocabulary rather than four genes. Menu track choice selects the course source before the live loop and is recorded as a parameter, not another in-run action.
- `ACT-545` requires foot-panel chart steps; `ACT-533` requires echoing a teacher phrase; `ACT-603` requires a touchscreen flick. None represents Vibri's shape-conditioned single/chord response.

### System Behaviour Genes

- New `SYS-1219` couples the selected external audio track to a custom ribbon obstacle sequence using the original game's available pattern/control segments. The observed generated sequence is not claimed to be a deterministic function of audio alone; built-in fixed-song scripts are excluded.
- New `SYS-1220` advances each obstacle to Vibri and judges the current mapped input as pass or mistake on the running clock. Exact hit windows are parameters not measured here. A paired shape asks for its two-button chord; two obstacles drawn in separate positions do not require a simultaneous chord.
- New `SYS-1221` accumulates clear and mistake runs, moves the character up or down the rabbit/frog/worm/Queen form ladder, adjusts scoring opportunity and ends the attempt after enough further mistakes at the lowest form. Exact streak thresholds and point values remain secondary-source claims, not encoded constants.
- `SYS-496` explicitly requires one fixed authored song and route, so it does not transfer to a selected custom CD. `SYS-1013` describes a Rock Meter and is not the character-form ladder; `SYS-1197` judges a touchscreen assembly event, not traversal of musical ribbon geometry.

### Constraint Genes

- No separate Constraint is admitted. The input vocabulary and event timing are internal to `ACT-617` / `SYS-1220`; the failure predicate belongs to `SYS-1221` / `OBJ-264`. A particular disc format, controller and latency are replication parameters rather than new universal constraints.

### Information Genes

- Reuse `INF-192`: only the approaching slice of ribbon is visible, not the entire future course. The forward horizon may be projected differently from a platformer's camera, but the same local-obstacle information boundary holds.
- New `INF-444`: the distinct shape of each visible approaching obstacle informs the required single or paired input; Vibri's present form and response feedback expose the survival condition. The selected music supplies cadence without revealing an exact future sequence. `INF-194` presumes a fixed authored level soundtrack and therefore does not fit the custom-CD mode.

### Objective Genes

- New `OBJ-264`: survive one selected custom-CD track through its endpoint and receive a run result; a miss may reduce form without immediately failing. `OBJ-215` specifically requires a fixed chart and Rock Meter and is not widened here.
- Reuse `OBJ-002`: scoring successful shapes and form-dependent rewards creates an optional within-run score-maximising pursuit, while mere survival does not require a high-score threshold.

### Time Genes

- Reuse `TIM-003`: the music and obstacle approaches advance while the player chooses and presses a response. There is no opponent turn or self-paced placement phase in the bounded live run.

## Reproducible transitions

| Before | Input or event | Source-derived resolution | Boundary | Claim |
|---|---|---|---|---|
| Selected ordinary audio-CD track | Start `Single Track` | The custom course supplies a forward stream of ribbon obstacles for that track | External music and script selection, not a built-in fixed chart | `VR-001`, `VR-003` |
| Visible solitary block approaches Vibri | Press L1 at its encounter | A correctly timed mapped response passes the shape and can increase score | One shape, one mapped command | `VR-002`, `VR-005` |
| Visible solitary pit, loop or wave approaches | Press Down, R1 or X respectively at encounter | The matching response can clear the shape | Same response rule, not three extra genes | `VR-002` |
| One combined block-and-pit shape approaches | Press L1 and Down together at encounter | A timely chord passes the combined obstacle | Pair inside one obstacle, not two separate obstacles | `VR-002` |
| An obstacle arrives with no correct timely response | Miss or wrong/late input | Mistake contributes to downward form pressure; the track normally continues | One miss need not terminate the run | `VR-002`, `VR-004` |
| Successes accumulate after a form loss | Repeated correctly timed responses | Form can recover upward; the exact count is not locally measured | Reversible form, not a permanent lost life | `VR-004` |
| Lowest form is repeatedly missed | Continue incorrect responses | The attempt fails before track end | Survival threshold differs from track completion | `VR-004` |
| Track endpoint arrives with form surviving | Let result settle | The single-track run ends with a score; no fixed rank is necessary | Positive terminal | `VR-005` |

These are documentary rule cases, not executed test outcomes. No particular CD track, obstacle ordering, timing value or numeric score is asserted.

## Strategic and experiential structure

- The short forward horizon makes shape recognition and timing inseparable: a player can know the button yet press too early or too late. Pairwise shapes require a chord, but they are not two consecutive single-shape inputs.
- A mistake changes future risk by degrading the current form; a later clean sequence can restore it. Score pursuit and survival therefore interact without requiring a particular terminal score.
- Choosing another audio track can change the obstacle experience. The original-disc script also contributes patterns and segment selection, so “music creates a unique fixed chart” would overstate the evidence.

## Replay and variation

- Different selected CDs, track durations and custom segment starts can vary the route. Because no disc or input trace was captured, this record cannot identify a particular course as reproducible by name alone.
- Repeating to survive at a higher form or earn more points is an optional player motive, not a second required ending.

## Adjacent systems and history

- *Geometry Dash* uses fixed authored obstacles and soundtrack on one replayable timeline; that is not this custom-CD rule. *Guitar Hero III* judges charted fret/strum notes against a Rock Meter. *Rhythm Heaven* grades an authored touch-flick exercise. Vib-Ribbon instead connects an external music source to a moving, shape-coded ribbon and form-dependent survival.
- Later digital editions and the built-in six-song route are potential separate packets. They do not establish exact PAL custom-CD events or hardware behaviour here.

## Normalised genome

| Type | Active gene IDs | Boundary |
|---|---|---|
| Action | `ACT-617` | mapped timed single/chord response |
| System Behaviour | `SYS-1219`, `SYS-1220`, `SYS-1221` | custom course, obstacle judgement, form ladder |
| Constraint | none | input timing is in action/judgement |
| Information | `INF-192`, `INF-444` | local ribbon horizon, shape/form cues |
| Objective | `OBJ-002`, `OBJ-264` | optional score, required track survival |
| Time | `TIM-003` | ongoing audio/obstacle schedule |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `466` (`GAME-0001`–`GAME-0466`).
- Exact genome matches: none.
- Tied near matches: `GAME-0414` — Kinect Adventures! (`2 / 13 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0414` — Kinect Adventures! | `OBJ-002`, `TIM-003` | Both permit score pursuit while input and system state advance in real time. Kinect Adventures! uses tracked body placement to cover several simultaneously active leaks and seal connected cracks; Vib-Ribbon instead requires timed single/chord button responses to approaching music-conditioned ribbon obstacles, with reversible character-form survival. This weak overlap is not a shared rhythm or course-generation claim. | Tied near, `2 / 13 = 0.153846` |

### Preserved research notes

- New genes: `ACT-617`, `SYS-1219`, `SYS-1220`, `SYS-1221`, `INF-444`, `OBJ-264`.
- Reused genes: `INF-192`, `OBJ-002`, `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: a custom audio-CD course, shape/chord timing and reversible form ladder are not an authored note chart, fixed platform route or one-hit endless runner. No earlier signature changes.

## Taxonomy impact

- Six new Active definitions across four types; no previous genome or verified combination is changed.
- Taxonomy-change record: [`TAXONOMY_CHANGE_204`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_204.md).

## Negative results

- No disc, console, executable, CD audio, controller trace or direct play. Exact generator mapping, timestamps, hit windows and form/score coefficients remain unresolved.
- The built-in songs' fixed-pattern evidence does not make the selected custom-CD run a fixed chart.
- A skipped obstacle does not prove instantaneous failure, and a score is not a required fixed minimum.
- The original illustration is an abstract plausible obstacle sequence, not evidence of an actual generated track.

## Delta summary

## New facts

- [Observation | Corroborated | High] The English PAL `Single Track` option permits one selected audio-CD track with timed block, pit, loop, wave and composite responses (`VR-001`, `VR-002`).

## New genes

- [Observation | Corroborated | Medium] Six definitions isolate shape input, music-conditioned obstacle supply, judgement, form dynamics, shape/form information and track survival.

## New combinations

- [Observation | Direct | High] None claimed until the verified-subset scan is computed.

## Taxonomy changes

- [Observation | Corroborated | Medium] Six new definitions; no migration of older games.

## Open questions

- Direct original-disc execution could pin the precise audio analysis and obstacle sequence, form thresholds, score coefficients and regional differences.

## Next research candidate

- `GAME-0468` — *Gravity Rush*, original PS Vita, only after this game unit's acceptance and the Goal stop window.
