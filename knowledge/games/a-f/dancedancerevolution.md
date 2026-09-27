---
game_id: GAME-0406
slug: dancedancerevolution
game_title: "DanceDanceRevolution"
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-545
  system:
    - SYS-1013
    - SYS-1085
  constraint: []
  information:
    - INF-299
    - INF-402
  objective:
    - OBJ-239
  time:
    - TIM-003
---

# Game: DanceDanceRevolution

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Song, chart,
cabinet setting, step-panel direction and rank are parameters, not genes.

## Analysis scope

- Version / ruleset: Konami's original 1998 `GN845-UC` four-panel arcade
  cabinet as described by its contemporary operator's manual. The manual
  identifies hardware, not an exact software-ROM revision or licensed song
  inventory; neither was inspected. This packet does not import later DDR
  arrow types, scoring rules or console editions.
- Structured analysis target: `PLAT-ARCADE-CABINET` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the next arrow or simultaneous arrow set
  scrolling upward to fixed step zones, place the corresponding foot or feet
  on the four floor panels at the musical beat, observe Perfect/Great/Good/
  Boo/Miss and the changing Dance Gauge, then prepare the next step while
  the song continues.
- Entry: one player has inserted the required credit, chosen one currently
  displayed music number and begun its single-player chart. The operator
  settings are difficulty level 4/Medium, maximum stage count one and
  `GAME OVER DURING SONG` Off. These are reproducible permitted settings,
  not a claim about every cabinet's factory state. The song title and chart
  sequence must be logged from the observed cabinet; this manual does not
  establish a region-invariant song title.
- Positive terminal: retain a nonzero Dance Gauge through the selected
  song's end and observe the song results, including the count of each timing
  judgement and an `SS` through `E` ranking. This is one song, not completion
  of the whole series or a high-score name-entry requirement.
- Negative terminal: at the selected Off setting, the gauge reaching zero
  ends play before the song is over. The separately available On setting
  continues until the song ends despite zero; that variant is excluded.
- Included: four directional foot panels; upward scrolling chart arrows and
  fixed step zones; foot-panel timing, simultaneous steps where charted,
  five named judgements, Perfect/Great gauge gain, Boo/Miss gauge loss,
  Danger warning at a low gauge, zero-gauge failure, and song-end judgement
  summary and rank. The manual does not quantify Good's gauge effect, so
  none is asserted.
- Excluded: exact note timing windows, unseen chart notes, score formula,
  gauge coefficients, hidden song inventory, licensed music or lyrics,
  doubles/two-player and join-in behaviour, multiple stages, high-score
  initials, later hold/freeze arrows, modifiers, unlocks and home versions.
- Potential scoped modules: a two-player attempt with separate gauges; the
  operator's continue-through-zero setting; a different documented song,
  difficulty or multi-stage credit.
- Reproducible parameterisation: record cabinet model and ROM/revision,
  operator setting values, displayed music number, chart difficulty and
  every visible arrow event, foot contact time, judgement, gauge change,
  Danger cue and final failure or rank. No perfect chart trace is asserted.
- Direct-play status: none. No cabinet, ROM, video, audio, input trace or
  screenshot was opened. This is a manual-bound reconstruction from Konami's
  original operator documentation; individual chart timing and regional
  music availability remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DDR-001` | The 1998 Konami manual covers model `GN845-UC` and describes one or two players stepping on four arrow-matched floor panels while arrows rise on screen. | Confirmed | Direct | High | P1 |
| `DDR-002` | Music Select precedes the song; selected chart arrows are judged as Perfect, Great, Good, Boo or Miss according to step timing. | Confirmed | Direct | High | P1 |
| `DDR-003` | Perfect/Great raise the Dance Gauge, Boo/Miss lower it, Danger warns of low gauge and zero ends play with the Off setting. | Confirmed | Direct | High | P1 |
| `DDR-004` | A completed music number reports the judgement distribution, score/play condition and a rank from `SS` through `E`. | Confirmed | Direct | High | P1 |
| `DDR-005` | The operator can set eight difficulty levels, one to three stages, and whether a zero gauge ends a song or permits it to finish. | Confirmed | Direct | High | P1 |
| `DDR-006` | The one-song, one-stage packet is a reconstruction, not a played or instrumented chart trace; song identity and exact software revision are unresolved. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: original Konami arcade product, operator manual copyright
  1998. This record does not claim the exact launch day or a particular song.
- Platform or physical form: `GN845-UC` arcade cabinet, four arrow foot
  panels, single-player chart; not a home dance mat.
- Mechanical family: real-time system pressure.
- Primary source:
  - **P1:** [Konami, *Dance Dance Revolution* operator's manual for
    `GN845-UC`](https://www.hackmycab.com/downloads/manuals/Dance%20Dance%20Revolution%20(Operators%20Manual)%20(Model%20GN845-UC).pdf),
    ©1998, pp. 11 and 19. The mirrored publisher-authored manual establishes
    the four-panel loop, judgements, gauge, rank and operator controls; the
    hosting site's commentary is not evidence.
- Secondary sources: none needed for the scoped mechanics.
- **R1:** local bounded-scope, transfer and no-direct-play audit in this
  record.
- Claim IDs: `DDR-001`–`DDR-006`.

## Mechanical decomposition

### Action Genes

- New `ACT-545`: commit a corresponding foot-panel step, or a simultaneous
  pair when two arrows coincide, as the chart arrow reaches its step zone.
  Guitar Hero III's fret-plus-strum commitment (`ACT-508`) is not the same
  physical input, and a generic pointer skill check (`ACT-261`) explicitly
  excludes rhythm sequences that are the complete objective.
- Claim IDs: `DDR-001`, `DDR-002`.

### System Behaviour Genes

- New `SYS-1085`: advance the selected authored four-direction chart and
  classify timed foot contacts or misses into the five manual-named results.
  This is not Guitar Hero III's fret-strum note and sustain processing
  (`SYS-1010`); no later hold arrow is imported.
- Reused `SYS-1013`: successful and failed chart play moves a live survival
  gauge through warning to possible early song failure. DDR's meter is the
  Dance Gauge; its warning is Danger and zero is terminal only under this
  packet's Off operator setting. The shared mechanism is live chart survival,
  not a shared numeric formula or colour scheme.
- Resolution order: chart arrow approaches → floor-panel input or miss is
  timed and classified → applicable judgement changes the gauge → Danger or
  zero-fail check → next event or song-end result.
- Claim IDs: `DDR-002`–`DDR-005`.

### Constraint Genes

- No new independent constraint. The selected Off fail setting is the
  `SYS-1013` terminal parameter; the foot-panel correspondence and timing
  are jointly tested by `ACT-545` and `SYS-1085`. A separately named
  constraint would duplicate that causal rule.
- Claim IDs: `DDR-001`–`DDR-003`, `DDR-005`.

### Information Genes

- New `INF-402`: upward arrows in four lanes, fixed step zones, the current
  timing verdict and visible Dance Gauge/Danger state show both the next
  required foot placement and survival risk. Guitar Hero III's `INF-379`
  additionally bundles fret colours, held-note shapes, streak multiplier and
  Star Power charge that this packet does not have.
- Reused `INF-299`: the terminal results expose counts of the five
  judgement classes and an aggregate rank, rather than only an unlabeled
  score.
- Claim IDs: `DDR-001`–`DDR-004`.

### Objective and Time Genes

- New `OBJ-239`: finish one selected dance chart with a nonzero gauge and
  receive its rank. `OBJ-215` specifically requires Guitar Hero III's
  notes-hit rate, streak and star grade; DDR's result contract differs.
- Reused `TIM-003`: the music/chart progresses on a live schedule; the
  player cannot wait between arrows indefinitely.
- Claim IDs: `DDR-002`–`DDR-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Music Select and one-stage operator setting | Select an offered number and start | Its chart begins with four upward lanes | Fixed selected-song packet | `DDR-002`, `DDR-005` |
| Single arrow approaches its fixed zone | Step the matching floor panel in time | One of five timing labels is shown; Perfect or Great raises the gauge | Spatial and temporal input both matter | `DDR-001`–`DDR-003` |
| Two arrows align at one chart instant | Step the two matching panels together | The simultaneous arrow set is adjudicated at that instant | Not two deferred turns | `DDR-001`, `DDR-002` |
| Incoming arrow is not matched or is badly mistimed | Miss or receive Boo | Dance Gauge lowers; a sufficiently low state shows Danger | Visible live risk | `DDR-002`, `DDR-003` |
| Gauge reaches zero before the final chart event | Continue under `GAME OVER DURING SONG` Off | Play ends before the song completes | Negative terminal | `DDR-003`, `DDR-005` |
| Final chart event passes with gauge nonzero | Complete the music number | Judgement counts and `SS`–`E` rank are shown | Positive terminal | `DDR-004` |

## Strategic and experiential structure

- Local decision: identify the approaching direction or pair and time the
  corresponding physical step to the fixed zone, not merely tap any panel
  to the beat.
- Medium-term planning: a visibly falling gauge makes accurate subsequent
  steps important for survival; the manual supports this qualitative
  recovery logic but not exact meter arithmetic.
- Long-term structure: different music numbers change authored chart events;
  this packet observes only one selection and no song-unlock progression.
- Failure attribution: wrong panel, missing contact or late/early contact
  can impair a judgement; without a cabinet trace, timing-window boundaries
  and hardware latency cannot be separated.
- Player-trust factor: the same screen communicates the next arrow and
  current danger. The post-song grade is not substituted for gauge survival.
- Claim IDs: `DDR-001`–`DDR-005`.

## Replay and variation

- The selected chart is authored, not a random note generator. Player steps,
  judgement mix, gauge path and terminal rank vary between attempts.
- Operator difficulty, stage count and continue-through-zero setting can
  alter outcomes; record them before comparing runs.

## Adjacent systems and history

- Guitar Hero III also has a scrolling authored chart and a live survival
  meter, explaining `SYS-1013` and `TIM-003` reuse. DDR commits a whole-body
  foot-panel direction at a top step zone and reports five named judgements;
  Guitar Hero III holds coloured frets, strums, sustains notes and can spend
  Star Power. Those latter mechanics cannot be inferred for this cabinet.
- PaRappa the Rapper alternates an instructor's call and a following player
  response. Here the chart continuously approaches and the song itself is
  judged footstep by footstep, not by teacher/student phrase turns.

## Normalised genome

The front matter is canonical: seven Active genes, one Action, two System
Behaviour, two Information, one Objective and one Time. Four boundaries
are new; `SYS-1013`, `INF-299` and `TIM-003` are reused.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `405` (`GAME-0001`–`GAME-0405`).
- Exact genome matches: none.
- Tied near matches: `GAME-0372` — Guitar Hero III: Legends of Rock (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0372` — Guitar Hero III: Legends of Rock | `SYS-1013`, `INF-299`, `TIM-003` | Both games keep an authored song moving while a live performance gauge can end it early, then report a classified result. Guitar Hero III requires frets plus strum, sustains, combo multiplier and optional Star Power, and ends in a star/streak report. The cabinet here requires physical directional steps at top arrow zones, uses Perfect/Great/Good/Boo/Miss and reports `SS`–`E`; neither input nor result may be substituted across the two. | Near, `3 / 15 = 0.200000` |

## Taxonomy impact

`TAXONOMY_CHANGE_144` records four additive distinctions. No lower-ID
signature or verified combination changes.

## Negative results

- The manual does not identify a single music number available in every
  `GN845-UC` software revision. No named song or precise chart is silently
  asserted.
- Good has a named judgement, but the manual does not state its exact Dance
  Gauge effect. No scoring table or timing window is invented.
- Operator difficulty level and continue-through-zero options are not
  assumed to be universal factory defaults.
- No authentic screenshot, audio or direct-play trace was inspected.

## Delta summary

The original arcade cabinet turns a continuously rising four-lane arrow
chart into timed whole-body steps. The visible Dance Gauge makes the song a
survival attempt as well as a post-song ranked performance.

## New facts

- An operator can choose one to three stages and independently allow or
  disallow play continuing after a zero gauge; this packet fixes one stage
  and disallows continuation for an unambiguous terminal.

## New genes

- [Confirmed | Direct | High] `ACT-545`, `SYS-1085`, `INF-402` and
  `OBJ-239` separate foot-panel step commitment, four-lane adjudication,
  visible step/gauge state and the ranked viable-gauge song endpoint.

## New combinations

- [Confirmed | Direct | High] None verified for this bounded packet.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_144` adds four Active
  boundaries without changing any earlier signature.

## New questions

- Which exact software-ROM revision and song list was installed in any
  particular `GN845-UC` cabinet?
- What are the exact judgement windows, gauge increments and Good effect?
- How does a two-player attempt resolve if one gauge fails while the other
  remains live? The manual gives a joint-zero rule, but this packet is solo.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0407` *Plants vs. Zombies*.
- Optimisation criterion: change from continuous body-timed chart reading
  to lane placement and sun-budget defence on PC.
- Expected information gain: distinguish resource-led wave planning from a
  rhythm-song survival gauge.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] The original arcade control makes
  musical timing spatial and physical, while the live meter and post-song
  rank separate survival from performance quality.

## Next test

Inspect an identified original cabinet and ROM revision with operator
settings logged, select a displayed song, capture synchronised chart/input
and gauge state, then test the one-song result and zero-gauge terminal.
