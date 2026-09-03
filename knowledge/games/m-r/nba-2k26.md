---
game_id: GAME-0241
slug: nba-2k26
game_title: NBA 2K26
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0239
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-411
    - ACT-412
    - ACT-413
    - ACT-414
    - ACT-415
  system:
    - SYS-757
    - SYS-758
    - SYS-759
    - SYS-760
    - SYS-761
    - SYS-762
    - SYS-763
  constraint:
    - CON-582
    - CON-583
    - CON-584
    - CON-585
    - CON-586
  information:
    - INF-116
    - INF-289
    - INF-290
    - INF-291
  objective:
    - OBJ-149
  time:
    - TIM-003
---

# Game: NBA 2K26

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: **NBA 2K26 Standard Edition**, current unmodified English
  Windows Steam app `3472040`, public branch observed at Build ID `24237529`
  (built 2026-07-16, published 2026-08-07), checked 2026-09-03; offline `Play
  Now` → `Quick Play`, one local human controlling the Oklahoma City Thunder
  against CPU-controlled New York Knicks, Pro difficulty, five-minute quarters,
  game speed 50, otherwise default controller/rules settings and automatic
  substitutions/timeouts.
- Primary decision loop: read the ball, control marker, team spacing, score,
  game clock and shot clock; move or switch the controlled player; dribble,
  pass, call/use a screen or commit a timed shot; on defence move, switch,
  contest, block or steal; let shared-ball motion, team AI, attempt resolution,
  rebounds and officiating settle the phase; reorganise for the next live or
  dead-ball possession until final score.
- Entry and exit: entry is confirmation of the named teams and fixed settings,
  followed by the opening tip at `0–0`. The positive evaluative exit is the
  final-result/box-score surface with the human side ahead after four quarters
  or required overtime; the same surface with the human side behind is a
  reproducible negative evaluation. A tie at regulation expiry is intermediate
  and must continue into overtime.
- Reproducible route: select offline Play Now Quick Play; choose Thunder as the
  home controlled side and Knicks as CPU away side; set Pro, five-minute
  quarters and game speed 50; leave ordinary rules/controller assistance and
  automatic coaching at defaults; confirm; play every possession without
  manually changing line-ups, tactics or timeouts; after the final horn advance
  to the result and box score and record win/loss plus final period totals.
- Included: team/match commitment; one ball; two five-player court sides; one
  transferable direct-control locus; locomotion and legal dribble; passes;
  called screens; timed shots, layups and dunks; steals, blocks and contests;
  off-ball team AI and automatic rotation; loose balls, misses and rebounds;
  court/basket geometry; weighted one-, two- and three-point scoring; game and
  shot clocks; fouls, violations, inbounds and free throws; four quarters,
  required overtime, final score and box score.
- Excluded: manual coaching, playbook editing, manual substitutions and manual
  timeouts; custom sliders, rosters, teams or rules; injuries as a chosen
  strategy; local two-human and online play; `NBA Today`, `Eras Quick Play`,
  `Blacktop`, `Learn2K`, training and other Play Now variants; MyCAREER, MyTEAM,
  MyNBA, The W, seasons, drafts, persistent rosters, online competition, VC,
  account progression, rewards, Season Pass, DLC, other editions, consoles,
  mobile products and the wider NBA 2K series.
- Potential scoped modules: any named Play Now variant, online head-to-head,
  manual coaching, MyCAREER, MyTEAM, MyNBA or The W requires a separate build,
  entry, decision loop and terminal. None is combined here.
- Direct-play status: not conducted. Current official product, mode, offline
  availability, gameplay descriptions and NBA rules plus one current build
  observation and written control reference establish the trace. It is an
  evidence-based reconstruction, not a captured match. No video or audio was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NBA26-001` | App `3472040` is the current Windows Standard product; Play Now is separable and available offline | Confirmed | Direct | High | P1, P2 |
| `NBA26-002` | The observed public Windows branch is Build `24237529`; official support exposes a current patch-note hub without a stable numeric patch label | Confirmed | Corroborated | High | P1, P3, S1 |
| `NBA26-003` | Quick Play allows team choice and match-parameter commitment before one local match | Confirmed | Direct | High | P4 |
| `NBA26-004` | Direct movement, switching, passing, shooting, screening, steals, blocks and contests are live player commands | Confirmed | Corroborated | High | P5, S2 |
| `NBA26-005` | Timing, aim, coverage, movement and attributes contribute to attempt resolution; misses expose rebound timing | Confirmed | Direct | High | P5 |
| `NBA26-006` | Team AI continuously coordinates off-ball motion, defence, spacing and transition around possession | Confirmed | Direct | High | P5 |
| `NBA26-007` | Legal scoring yields one, two or three points; four regulation periods and required overtime settle an unequal score | Confirmed | Direct | High | P6, P7 |
| `NBA26-008` | A possession must release a rim-touching or scoring attempt before shot-clock expiry | Confirmed | Direct | High | P8 |
| `NBA26-009` | Contact, handling and boundary offences select dead-ball remedies, turnovers, inbounds or free throws | Confirmed | Direct | High | P6, P8–P11 |
| `NBA26-010` | The broadcast view and HUD expose the ball, control, team shape, scores, period, game clock, shot clock and result | Observation | Corroborated | High | P4, P5, S2 |
| `NBA26-011` | One complete fixed exhibition can be bounded from team/settings confirmation to final result without importing persistent modes | Confirmed | Corroborated | High | P1–P11, S1, S2, V1 |

## Basic data

- Release / origin: Visual Concepts / 2K, released 2025-09-04/05.
- Form: real-time five-on-five basketball simulation; only the declared current
  Windows Steam offline Quick Play exhibition is admitted.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; physics and object manipulation.
- Primary and official sources:
  - **[P1]** [Steam product](https://store.steampowered.com/app/3472040/NBA_2K26/),
    for title, app, developer/publisher, release, Windows, Standard product,
    named modes and explicit offline availability of Play Now.
  - **[P2]** [2K game-mode breakdown](https://support.nba2k.com/hc/en-us/articles/42585904403987-NBA-2K26-Game-Mode-Breakdown),
    for separating Play Now, MyCAREER, MyTEAM, MyNBA, The W and Learn2K and for
    current shooting/gameplay feature descriptions.
  - **[P3]** [2K patch-note hub](https://support.nba2k.com/hc/en-us/articles/44436762032147-NBA-2K26-Patch-Notes),
    for current official update authority without importing a marketing season.
  - **[P4]** [official PlayStation beginner guide](https://www.playstation.com/en-us/games/nba-2k/nba-2k-beginners-guide/),
    for Play Now Quick Play team selection, local play and match parameters and
    for separating NBA Today, Eras Quick Play and Blacktop; it corroborates mode
    rules but does not redefine the scoped Windows platform.
  - **[P5]** [2K gameplay report](https://newsroom.2k.com/news/nbar-2k26-debuts-new-gen-9-gameplay-improvements-including-an-all-new-dynamic-motion-engine-powered-by-proplay),
    for Windows Gen 9, movement, timing, shooting, layups, defence, collisions,
    rebounds, passing, screens and game-speed control.
  - **[P6]** [NBA official rulebook](https://official.nba.com/rulebook/), for
    the contemporary basketball rules represented by the simulation.
  - **[P7]** [NBA Rule 5 — scoring and timing](https://official.nba.com/rule-no-5-scoring-and-timing/),
    for one/two/three-point values, four periods and required overtime.
  - **[P8]** [NBA Rule 7 — 24-second clock](https://official.nba.com/rule-no-7-24-second-clock/),
    for release-before-expiry, rim contact and possession-change predicates.
  - **[P9]** [NBA Rule 6 — live/dead ball](https://official.nba.com/rule-no-6-putting-ball-in-play-live-dead-ball/),
    for opening tip, inbounds, live/dead transitions and free throws.
  - **[P10]** [NBA Rule 10 — violations](https://official.nba.com/rule-no-10-violations-and-penalties/),
    for handling, travelling, boundary and backcourt predicates.
  - **[P11]** [NBA Rule 12 — fouls](https://official.nba.com/rule-no-12-fouls-and-penalties/),
    for contact, screening, shooting-foul and penalty remedies.
- Secondary textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/3472040/depots/), observed
    2026-09-03, for public Build ID `24237529` and timestamps.
  - **[S2]** [NBA2KW controls guide](https://nba2kw.com/nba-2k26-controls-guide-playstation-xbox),
    for an independent written control map; it corroborates inputs but is not
    used for product, edition, build or official rules.
- Reproducible control: **[V1]** repository transition trace under fixed
  product, build, platform, mode, teams and settings; no direct-play or
  audiovisual claim.
- Claim IDs: `NBA26-001`–`NBA26-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate the controlled player; `ACT-052`:
  transfer the unique control locus to an eligible on-court teammate.
- New `ACT-411`: commit the disposable matchup and parameters; `ACT-412`:
  direct a pass to a teammate; `ACT-413`: commit a release-timed basket attempt;
  `ACT-414`: commit a steal, block or contest; `ACT-415`: call and use one
  teammate screen.
- Exact teams, settings, mappings and attempt names are parameters.
- Claims: `NBA26-003`–`NBA26-005`, `NBA26-011`.

### System Behaviour Genes

- New `SYS-757`: resolve one shared ball between held/dribbled and free states;
  `SYS-758`: combine release timing and coverage into attempt outcome;
  `SYS-759`: coordinate non-controlled roles; `SYS-760`: resolve misses and
  rebounds; `SYS-761`: adjudicate fouls/violations; `SYS-762`: register weighted
  scoring; `SYS-763`: advance four periods and required overtime to settlement.
- Resolution order: clocks advance; direct input and team AI update positions;
  ball action releases or retains possession; collision, attempt or boundary
  resolves; adjudication chooses continuation; legal basket updates weighted
  score; period expiry advances or adds overtime; unequal final score settles.
- Claims: `NBA26-004`–`NBA26-011`.

### Constraint Genes

- New `CON-582`: one direct-control locus governs an on-court five; `CON-583`:
  court, basket and boundary geometry; `CON-584`: dribble, gather and progression
  legality; `CON-585`: release and rim-contact shot-clock requirement;
  `CON-586`: basketball contact and handling law.
- Scarce strategic resources: possession time, match time, court space, passing
  lanes, defensive position, foul exposure and score margin.
- Claims: `NBA26-003`, `NBA26-007`–`NBA26-009`.

### Information Genes

- Existing `INF-116`: expose live sides, score, time and phase state.
- New `INF-289`: expose the ball, control locus, court and local team shape;
  `INF-290`: jointly expose score, game clock, shot clock and adjudication;
  `INF-291`: expose final score and box-score settlement.
- Claims: `NBA26-010`, `NBA26-011`.

### Objective Genes

- New `OBJ-149`: complete one exhibition with more legally awarded points than
  the opponent. Human victory is positive evaluation; a final human loss is a
  valid negative terminal; regulation tie requires overtime.
- Claims: `NBA26-007`, `NBA26-011`.

### Time Genes

- Existing `TIM-003`: ball, actors and both clocks update in real time between
  stoppages; no turn grid structures player decisions.
- Claims: `NBA26-004`–`NBA26-011`.

## Reproducible transitions

| Before | Action | Resolution | Establishes | Claim |
|---|---|---|---|---|
| Offline Quick Play menu | Choose teams/settings and confirm | One disposable local-versus-CPU contest is instantiated | bounded entry | `NBA26-001`, `003`, `011` |
| Opening tip at `0–0` | Contest or await controlled possession | Shared ball enters live held or loose state and clocks begin | live entry | `NBA26-007`, `009` |
| Controlled possession | Move/dribble while reading both clocks | Carrier, spacing and remaining possession time update | spatial/time pressure | `NBA26-004`, `006`, `008` |
| Teammate route is available | Commit pass | Ball leaves held state; AI, collision and eligibility resolve reception or turnover | ball transfer | `NBA26-004`, `006` |
| Ball carrier and screener are eligible | Call screen, then choose route | Teammate establishes legal transient obstruction and defence reacts | routing fork | `NBA26-004`, `006`, `009` |
| Basket attempt is eligible | Begin/release shot | Timing, range, movement and coverage produce make, miss or block | attempt resolution | `NBA26-004`, `005` |
| Attempt enters legally | Await crossing | Location/attempt class credits one, two or three points | weighted score | `NBA26-007` |
| Attempt misses | Position and time rebound input | Rim/backboard trajectory and contest assign rebound, loose ball or boundary | possession continuation | `NBA26-005` |
| Opponent possesses | Move/switch, then contest, block or steal | Defence may force miss/turnover or incur foul/exposure | defensive trade-off | `NBA26-004`, `009` |
| Possession clock nears zero | Release eligible attempt | Rim touch/score preserves legal attempt; otherwise violation transfers possession | shot-clock terminal | `NBA26-008` |
| Offence or boundary predicate settles | Await dead-ball ruling | Play stops and selects inbound, turnover, free throws or continuation | adjudication | `NBA26-009` |
| Regulation expires tied | Continue | Required overtime starts with same accumulated score | nonterminal tie | `NBA26-007` |
| Required time expires with unequal score | Advance to result/box score | Winner, loser, final score and accumulated statistics are exposed | positive/negative terminal | `NBA26-007`, `010`, `011` |

## Strategic and experiential structure

- Local decisions balance pass lane, screen angle, rim pressure, release timing,
  rebound position and defensive intervention against the possession clock.
- Medium-term planning manages score margin, remaining match time, player
  spacing and foul exposure while automatic rotations vary the live five.
- Long-term structure accumulates differently weighted scoring events across
  four periods and extends a tied match rather than accepting a draw.
- Failure attribution is visible through the control marker, court state,
  shot feedback, clocks, whistle/violation notice, score and box score.
- The ordinary match UI discloses both the current decision window and final
  settlement; no external walkthrough or arbitrary sandbox stop is required.

## Replay and variation

- Variable: possession sequence, control switches, passes, screens, attempts,
  rebounds, fouls, score, overtime and final result.
- Fixed: product/build observation, mode, local-versus-CPU relation, teams,
  Pro difficulty, period length, speed and automatic coaching boundary.
- Other Play Now variants and persistent modes are explicitly separate packets.

## Adjacent systems and history

- Earlier NBA 2K games and other NBA 2K26 editions/modes are separate software
  or rulesets; no historical feature is imported merely because names recur.
- EA SPORTS FC 26 is the nearest sport corridor: both transfer direct control
  inside one AI-supported side and settle a real-time score. Football retains
  a continuously free ball, eleven-player side, offside, one-value goals and a
  permitted draw; this packet adds held possession, shot clock, weighted score,
  rebounds, free throws and required overtime.
- Rocket League supplies the collision-ball corridor but not carried dribble,
  five-player role coordination or basketball adjudication.
- Distinguishing feature: every possession is a nested timed contest inside a
  four-period match, and a single target awards different point values from
  attempt class/location before mandatory tie-breaking.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-052`, `ACT-411`, `ACT-412`, `ACT-413`, `ACT-414`, `ACT-415` | teams, controls, pass/shot/defence family |
| System | `SYS-757`, `SYS-758`, `SYS-759`, `SYS-760`, `SYS-761`, `SYS-762`, `SYS-763` | ball, AI, scoring, adjudication, periods |
| Constraint | `CON-582`, `CON-583`, `CON-584`, `CON-585`, `CON-586` | five, court, handling, clocks, law |
| Information | `INF-116`, `INF-289`, `INF-290`, `INF-291` | camera, markers, scorebug, box score |
| Objective | `OBJ-149` | sides, final points, result |
| Time | `TIM-003` | game and possession cadence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `240` (`GAME-0001`–`GAME-0240`).
- Exact genome matches: none.
- Tied near matches: `GAME-0163` — EA SPORTS FC 26 (`4 / 41 = 0.097561`).
- Supported combination subsets: `COMB-0239`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0163` — EA SPORTS FC 26 | `ACT-008`, `ACT-052`, `INF-116`, `TIM-003` | FC 26 uses a free football, eleven-player side, offside, single-value goals and a valid draw. NBA 2K26 instead adds held/dribbled possession, five-player court geometry, a shot clock, release timing, rebounds, basketball remedies, weighted points and required overtime. | Near, `0.097561` |

### Preserved research notes

- New genes: `ACT-411`–`ACT-415`, `SYS-757`–`SYS-763`, `CON-582`–`CON-586`,
  `INF-289`–`INF-291`, `OBJ-149`.
- Reused genes: `ACT-008`, `ACT-052`, `INF-116`, `TIM-003`.
- Result: `New gene` and `New combination of known and new genes`. Product,
  teams, settings, controls and numeric values remain parameters.

## Taxonomy impact

- Twenty-one new Active portable genes; no prior definition, lifecycle or
  reviewed signature changes. No taxonomy-change record.

## Negative results

- Football-specific `ACT-267`–`ACT-269`, `SYS-457`–`SYS-463`, `CON-398`–
  `CON-401`, `INF-178` and `OBJ-090` are rejected: their boundary is a free
  football, eleven-player side, offside, goalkeeping and/or valid draw.
- `ACT-411` does not encode either team or five-minute value. `SYS-762` does not
  encode the point amounts in its label. The fixed matchup and numbers remain
  game parameters. Persistent rosters, economy, coaching and other modes are
  excluded rather than silently generalised.

## Combination subset scan

- All 238 pre-unit combinations were tested; none is a proper subset of this
  25-gene signature. `COMB-0239` reserves only the live five-player possession,
  adjudication, weighted-score and whole-match core. Scan date: 2026-09-03.

## Delta summary

## Нові факти

- [Confirmed | Direct/Corroborated | High] Product, offline Play Now boundary,
  current build observation, controls and official match law are fixed by
  `NBA26-001`–`NBA26-010`.
- [Confirmed | Corroborated | High] The bounded disposable exhibition and both
  evaluative terminals are fixed by `NBA26-011`.

## Нові гени

- [Confirmed | Direct/Corroborated | High] Twenty-one new genes isolate held/
  free ball state, five-player control, timed possession, contested weighted
  scoring, basketball adjudication and final settlement.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0239` joins the portable mechanics of
  one live five-player exhibition without importing named teams or values.

## Зміни таксономії

- No earlier reviewed definition, lifecycle or signature changed.

## Нові питання

- Which other reviewed basketball simulation supports the complete possession-
  clock and weighted-score boundary without persistent roster systems?
- How does a human-versus-human packet alter the information and control genes?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0242` — Asphalt Legends.
- Contrast nested possession pressure with a bounded live-service arcade race.

## Research artefacts

- `research/taxonomy-health/BASELINE_241.json`.
- `research/normalisation/GENE_DUPLICATE_QUEUE_091.md` and `.json`.
- `research/normalisation/GENE_LEXICAL_TOP_N_EXPERIMENT_091.md` and `.json`.

## Evidence gaps

- Build ID and timestamp are secondary observations; the official patch hub
  does not expose one stable numeric patch label. The fixed five-minute periods
  and Pro difficulty are reproducibility parameters, not claims about defaults.
- No direct play. The official mode and rules sources do not provide one
  complete static Windows control/HUD specification, so current written control
  material is used only as corroboration.
- No audiovisual evidence was used.

## Confidence

High for product/mode and official basketball-rule boundary; medium-high for
the reconstructed NBA 2K26-specific controls, UI and terminal trace.
