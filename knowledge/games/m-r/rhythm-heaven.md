---
game_id: GAME-0454
slug: rhythm-heaven
game_title: Rhythm Heaven
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-603
  system:
    - SYS-822
    - SYS-1197
  constraint: []
  information:
    - INF-437
  objective:
    - OBJ-258
  time:
    - TIM-003
---

# Game: Rhythm Heaven — first Built to Scale on Nintendo DS

Use the [canonical vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Plate shape, musical phrase, gesture direction, timing tolerances and grade names are parameters, not independent genes. No song, notation or full chart is reproduced.

## Analysis scope

- Version / ruleset: original English North American 2009 Nintendo DS *Rhythm Heaven*, the first ordinary Built to Scale, not Built to Scale 2, Wii *Rhythm Heaven Fever* or 3DS *Megamix*. Nintendo's contemporary US manual establishes controls and result progression; a contemporary first-hand authorized-demo account establishes the first exercise's action and geometry. A later original-DS written guide corroborates local outcomes. A Japanese first-person DS-stage analysis corroborates authored tempo variation and late visibility reduction, not exact US/Japanese chart parity. Cartridge revision, complete event chart, input latency, timing windows and scoring thresholds were not inspected.
- Structured analysis target: `PLAT-NINTENDO-DS` in [`knowledge/platforms/games.json`](../../platforms/games.json); no new platform or cross-release audit is inferred.
- Primary decision loop: hear a short musical approach and watch two moving holed plates; prepare touch contact and flick the stylus to send a rod at their joining moment; observe connection or miss, then retime the next response while the authored performance continues.
- Entry: select the first Built to Scale on an ordinary profile before its optional exercise practice. Initial system-wide flick training is outside the packet. Practice can be repeated or skipped; it does not itself constitute the graded performance.
- Positive terminal: finish the authored performance and receive OK or Superb, retaining the result and opening the next ordinary game, Glee Club. Superb additionally yields a medal; it is not required for the ordinary clear.
- Negative terminal: finish with Try Again and remain without this ordinary clear. Local misses are not asserted to empty a health meter or abort the song. Deliberate quit is abandonment rather than a grade; pause alone is not a terminal.
- Included: practice-to-performance entry, touch/flick control, a fixed musical event sequence with tempo variation, plate approach and rod contact, timing-sensitive local feedback, late reduced visual approach information, terminal evaluation, result autosave, next-game legality and the Superb medal as a grade consequence.
- Excluded: exact note count/BPM/offsets, measured tolerance or grade formula, a claimed compulsory last-note rule, Perfect challenge attempts, Café skip assistance, global Flow, medal-shop rewards, other exercises and their tap/hold/release tasks, remixes, later sets, full-campaign completion, speed manipulation and touchscreen calibration measurements.
- Potential scoped modules: Glee Club's release/held-vocal action; Fillbots' filling duration; Built to Scale 2's changed patterns; Perfect eligibility and limited challenges.
- Reproducible parameterisation: record cartridge region/revision, profile progression, practice choice, audio route, gesture contact/stroke/release timestamps, cue and plate alignment times, local outcome, visibility phase, terminal grade, newly legal stage and retained result after reload. No such executed trace is claimed here.
- Direct-play status: no DS, cartridge, ROM, save, input trace, gameplay video or audio was opened or played. Original-manual diagrams were visually inspected. Written source observations are evidence, not our play results; the late-stage detail is corroborating original-DS testimony with unmeasured regional parity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RH-001` | Book-style DS use supports a rapid upward stylus stroke/release; a short or slow stroke may not register the intended flick. | Observation | Direct | High | P1 pp. 6–9; P2 |
| `RH-002` | In the first exercise a timed rod joins two approaching plates; mistiming or missing produces distinct failed assembly feedback. | Observation | Corroborated | High | P3; P4, G01-1 |
| `RH-003` | The authored musical sequence continues between responses rather than waiting for the player to choose a world action. | Observation | Corroborated | High | P1 pp. 14–15; P3; P4 |
| `RH-004` | Original-DS first-stage accounts report tempo variation and late narrowed visual approach information while musical cues remain useful. Exact US/Japanese parity is not measured. | Observation | Corroborated | Medium | P5; P4, G07-1 explicitly contrasts the first-stage spotlight |
| `RH-005` | Optional practice precedes the graded game; OK/Superb opens the next game, Superb grants a medal, and completed-game results save automatically. | Observation | Direct | High | P1 pp. 14–15; P4 rankings and G01-1 |
| `RH-006` | This packet's ordinary positive terminal is a passing result, not a live survival gauge, Perfect challenge or complete collection. | Observation | Corroborated | High | P1 pp. 14–15; P4 |
| `RH-007` | Exact timing windows, terminal thresholds and a special last-event failure predicate are unresolved; written advice does not establish executable rules. | Observation | Limited | Medium | P4's qualified last-note advice; no binary trace |
| `RH-008` | Audio-led retiming can compensate for reduced visual preview, but it does not prove an optimal policy or an observed player result. | Hypothesis | Limited | Medium | Source-led interpretation of RH-002–004 |

## Basic data

- Release / origin: Nintendo DS, North American release 2009; Japanese original *Rhythm Tengoku Gold* 2008 is corroborating context, not the declared cartridge target.
- Platform or physical form: one player using DS touch control and audiovisual cues; the exact target belongs to the structured platform registry.
- Puzzle family: `FAM-010`, real-time system pressure. Musical arrivals constrain when an intervention succeeds; this is not free-form factory construction.
- Primary sources:
  - P1: [Nintendo original US manual, 67861A](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/DS_Rythm_Heaven?_a=DATAg1AAZAA0), printed English pp. 6–9 and 14–15. The official support [manual index](https://en-americas-support.nintendo.com/app/answers/detail/a_id/16905/) establishes provenance. Scanned diagrams were viewed locally.
  - P2: [Nintendo Iwata Asks, The DS Challenge](https://www.nintendo.com/en-za/Iwata-Asks/Iwata-Asks-Rhythm-Paradise/Iwata-Asks-Rhythm-Paradise/3-The-DS-Challenge/3-The-DS-Challenge-238799.html), creator account of developing the DS flick; design intent is not a timing coefficient.
  - P3: [Eric's first-hand Nintendo Channel demo preview, 26 March 2009](https://www.nintendolife.com/news/2009/03/preview_rhythm_heaven), personally played authorized demo. It establishes the initial action/cue, not the complete retail chart or later progression.
  - P4: [Matthew Tabuchi's original-DS written guide, revised 10 March 2012](https://www.neoseeker.com/rhythm-heaven/faqs/191087-walkthrough.html), publicly indexed G01-1, rankings and relevant G07-1 contrast only. The full page was not retrieved; indexed excerpts were read. No access restriction was bypassed, and the author's qualified grade advice remains unresolved.
  - P5: [P. Onozuka's first-person original-DS Built to Scale analysis](https://note.com/p_onozuka/n/naff33d6fb2dc?hl=en), 12 July 2026. The served English text is labelled automatic translation; broad tempo/visibility testimony is corroborating, while exact notation, numerical timings and opinions are not admitted as rules.
- Secondary sources: community walkthroughs were search leads only, not an authority for new boundaries. No modern series edition is substituted for the DS packet.
- All sources checked: 2026-09-30. Claim IDs: `RH-001`–`RH-008`.

## Mechanical decomposition

### Action Genes

- New `ACT-603`: prepare touch contact, make a rapid directed stroke and release to commit a rhythmic response. The player chooses when, not a free world target or separate arbitrary projectile aim.
- A gentle contact can prepare the gesture without scoring a shot. Shape/duration eligibility belongs to the gesture definition and resolution parameters; it is not a second independent constraint gene. Menu selection, optional practice skip and Start pause remain packet controls, not invented universal actions.
- `ACT-261` explicitly excludes note sequences that are the whole objective; `ACT-533` requires instructor-led symbol reproduction; `ACT-572` addresses current food/utensil tasks. None owns this action. Claim IDs: `RH-001`, `RH-002`.

### System Behaviour Genes

- New `SYS-1197`: advance the fixed musical approach events, judge the registered gesture's timing against the expected joining event, animate a connection or failed contact, and continue to the next event. This is not free physical aim or a live health-gauge failure system.
- Reuse `SYS-822`: settle the completed activity into a performance grade. Timing quality is the evaluated property; OK/Superb, retention, medal consequence and next-stage legality are parameters already within its boundary. Do not add another gene merely for this result's autosave/unlock.
- Resolution order: practice ends or is skipped; authored cues advance; contact/stroke/release may register a flick; its temporal relation produces local feedback; further events continue; song closure evaluates the attempt; result consequences and save follow. Exact internal frame order remains unmeasured. Claim IDs: `RH-001`–`RH-007`.

### Constraint Genes

- No independent admitted Constraint. Input recognition and timing tolerance instantiate ACT-603 / SYS-1197, while terminal grade legality instantiates SYS-822 / OBJ-258. Do not duplicate these as generic timing constraints.
- No finite ammunition, spendable stock, directional note choice, arbitrary target selection, disclosed exact hit window or continuous health gauge is established. Claim IDs: `RH-001`, `RH-002`, `RH-006`, `RH-007`.

### Information Genes

- New `INF-437`: musical approach and moving alignment disclose a response moment, local assembly feedback exposes its outcome, and the final grade discloses the attempt's result. Late visual restriction changes the amount of approach preview, not the song's underlying event sequence.
- Not `INF-001`: complete current state is not always visibly available. Not `INF-194`: Geometry Dash's soundtrack cues obstacle traversal but explicitly excludes graded beat presses. Not `INF-299`: a plain ordinal result is not a disclosed category-and-aggregate report. Exact thresholds remain hidden. Claim IDs: `RH-002`, `RH-004`–`RH-007`.

### Objective Genes

- New `OBJ-258`: finish one authored rhythmic exercise with a passing terminal quality grade to obtain its ordinary clear/next-stage transition.
- Try Again is a completed but unsuccessful attempt. Superb/medal is optional higher quality, not necessary passage; Perfect is a separately excluded challenge. No continuous survival meter is inherited from Guitar Hero or DanceDanceRevolution, nor PaRappa's live Good instructor rating. Claim IDs: `RH-005`, `RH-006`.

### Time Genes

- Reuse `TIM-003`: cues and movement progress while input is prepared or withheld. Explicit pause suspends ordinary play; quitting abandons the attempt. Authored tempo changes are parameters of the live sequence, not another time model. Claim IDs: `RH-001`, `RH-003`, `RH-004`.

## Reproducible transitions

| Before | Action/event | Source-derived resolution | Boundary | Claim ID |
|---|---|---|---|---|
| First-game practice available | Skip practice | Proceed to the graded exercise; practice is not the terminal | Training versus attempt | `RH-005` |
| Touch contact prepared | Hold without an upward stroke | No completed flick is asserted | Preparation versus response | `RH-001` |
| Plates approach their joining event | Complete a registered flick at its expected moment | Rod connects both plates | Timed assembly | `RH-002` |
| Same approach | Complete flick early/late | Failed contact feedback instead of a correct connection | Input existence versus quality | `RH-002` |
| Plates arrive without a successful shot | Withhold response | Failed assembly occurs; later events continue | Miss versus song abort | `RH-002`, `RH-003` |
| Intended stroke too short/slow | Release stylus | Intended flick may not be recognized | Gesture recognition versus scoring | `RH-001` |
| Authored tempo changes | Repeat old fixed delays | Old timing need not fit the new cue; adjust to the current approach | Relative cadence, not constant stopwatch | `RH-004`, `RH-008` |
| Late visual preview reduced | Continue listening before plates become visible | Musical timing evidence remains; no omniscient view is supplied | Audio versus visual preview | `RH-004` |
| Running performance | Press Start to pause | Ordinary progression suspends until resume or quit | Explicit pause versus withheld input | `RH-001` |
| Performance reaches end | Receive Try Again | No passing clear is established | Completion versus success | `RH-005`, `RH-006` |
| Performance reaches end | Receive OK | Result saves and next ordinary exercise opens | Passing grade versus optional medal | `RH-005` |
| Performance reaches end | Receive Superb | Passing result and medal settle | Higher quality, not separate campaign win | `RH-005` |

These are falsifiable documentation-derived cases, not executed tests. Exact strokes, regional event parity, save reload and evaluation coefficients need an original-cartridge trace.

## Strategic and experiential structure

The actionable choice is response timing and gesture preparation, not aiming at a selected enemy. A recognized but mistimed flick differs from an unrecognized stroke; correct identification of the cue alone therefore does not guarantee success. Retiming the next event remains possible after a miss. Reduced visual approach makes listening useful without establishing a universally superior strategy. Terminal grade separates reaching the end from earning passage. These interpretations inherit `RH-001`–`RH-008`, not measured player performance.

## Replay and variation

The declared exercise repeats authored cues, not a claimed randomized chart. Player timing, gesture recognition and resulting grade can vary. Practice, retry and optional higher-grade pursuit do not admit a whole collection of other tasks. No random generator, chart seed, difficulty selector or exact score distribution was observed.

## Adjacent systems and history

Cooking Mama shares timed touch performance and terminal quality evaluation, but cooking acts on an addressed ingredient/utensil through task completion, not a music-led rod assembly event. PaRappa alternates instructor/player phrases and can fail through its live rating; Guitar Hero and DanceDanceRevolution use chart-specific commands and survival gauges. Geometry Dash times avatar traversal against geometry rather than grading a stylus response. Built to Scale 2 and Wii factory geometry remain distinct future targets.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-603` | contact, directed stroke and release |
| System Behaviour | `SYS-822`, `SYS-1197` | live event judgement, terminal grade and retained consequences |
| Constraint | none | no independent duplicated timing restriction |
| Information | `INF-437` | audio/visual approach, local feedback, terminal rank |
| Objective | `OBJ-258` | passing ordinary stage result |
| Time | `TIM-003` | continuous progression with explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `453` (`GAME-0001`–`GAME-0453`).
- Exact genome matches: none.
- Tied near matches: `GAME-0434` — Cooking Mama (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0434` Cooking Mama | `SYS-822` graded activity closure and `TIM-003` live time | Cooking progresses food/utensil tasks under task instructions and recipe completion. Built to Scale judges a flick against continuing musical alignment, restricts late visual preview and requires a passing terminal grade for the next exercise. Neither task union nor Cooking Mama's medal formula transfers. | Near 0.181818; not exact. |

## Taxonomy impact

`TAXONOMY_CHANGE_191` admits four Active boundaries; SYS-822 and TIM-003 transfer unchanged. Grade retention and next legality do not warrant another system gene because SYS-822 already owns those parameters. The named GAME-0454 salience review rereads this entire scope and partitions all six uses with bilingual plain-language examples. Earlier signatures, definitions and verified combinations remain unchanged.

## Negative results

- No teacher-response symbol action, food manipulation, fret/foot command, Rock/Dance Gauge, fully visible state, ammo limit, complete chart, exact grade formula or last-note-only failure predicate is inherited.
- Indexed guide excerpts and automatically translated first-person testimony are explicitly bounded sources, not a claim to have retrieved restricted material or measured US/Japanese parity.
- Artwork is an original mechanics illustration, not an observed successful attempt or licensed Nintendo screenshot.

## Delta summary

## New facts

- [Observation | Corroborated | High] First-stage flick timing connects moving plates; continuing events and terminal passing grade distinguish gesture execution from ordinary clear (`RH-001`–`RH-006`).

## New genes

- [Observation | Corroborated | High] `ACT-603`, `SYS-1197`, `INF-437`, `OBJ-258`; no timing coefficient or chart value is invented.

## New combinations

- [Observation | Limited | Medium] No new combination; all 274 existing proper subsets are checked against the complete signature.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_191`; no older canonical boundary changes.

## New questions

- How does an exact original US cartridge trace resolve gesture recognition, tempo/visibility event parity, terminal grade thresholds and saved result after reload?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0455` *Soulcalibur* on Dreamcast, next approved unit after complete acceptance and the stop window.
- Optimisation criterion: alternate prompted rhythm and free arena combat on a different platform.
- Expected information gain: directed attacks, defence and ring-boundary outcomes rather than fixed musical event judgement.
- Backlog impact: five approved games remain; no push, public publication or deployment is authorised.
