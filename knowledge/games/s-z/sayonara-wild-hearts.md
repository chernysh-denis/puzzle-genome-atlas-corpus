---
game_id: GAME-0556
slug: sayonara-wild-hearts
game_title: Sayonara Wild Hearts
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-232
  system:
    - SYS-037
    - SYS-369
    - SYS-496
    - SYS-1610
    - SYS-1611
    - SYS-1612
    - SYS-1613
    - SYS-1614
  constraint:
    - CON-113
  information:
    - INF-179
    - INF-194
    - INF-533
  objective:
    - OBJ-002
    - OBJ-181
  time:
    - TIM-003
---

# Game: Sayonara Wild Hearts

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Heart sizes, square-coin positions, style bonuses, rank cutoffs and touch
sensitivity parameterise the rules; they are not separate genes.

## Analysis scope

- Version / ruleset: original full English iOS Apple Arcade release from
  19 September 2019, standard individual-song play with touchscreen steering,
  complete third level Doki Doki Rush. The creator confirms the iOS launch
  and removal from Apple Arcade on 15 August 2024. This is an evidenced
  historical released target, not a promise of current App Store access.
  No installed version, binary checksum, entitlement, device, personal save
  or native execution was verified. Current PS5/Switch 2 Remix Arcade and
  an announced or later standalone iOS edition are not silently substituted.
- Primary decision loop: steer the rider laterally with relative touch motion
  while the authored course carries her forward; choose between collectible
  lines and safe gaps, obtain eligible Slide or Risky style credits, and
  preserve pickup multiplication by avoiding collision. Retry from a short
  checkpoint after failure or answer the optional Magician offer, then reach
  the song endpoint and inspect retained rank, best score and square credits.
- Entry and exit: after ordinary completion/unlock of Clair de Lune and
  Heartbreak I, select Doki Doki Rush from its card with initial live score
  and its introductory motorcycle transformation. Include the complete city
  route through ordinary song-end closeout and the selectable result with
  Fighting Hearts available, before that next stage's live action.
- Failure and retry: collision with an eligible building/traffic obstacle
  interrupts the current section and restores a nearby authored checkpoint;
  collection multiplication resets. Repeated failures can offer a local
  assistance skip, which can be accepted, declined or suppressed. The skipped
  opportunity is not performed or awarded as a clean traversal. The packet
  does not certify field-by-field score/coin/cooldown rollback, a failure-count
  threshold or a native save/reload experiment. It excludes duplication and
  pause exploits rather than assuming every restored field is identical.
- Included: direct lateral rider placement, automatic longitudinal route and
  dynamic camera; small/large heart and square contact collection; separate
  class-specific collection multiplication; sustained sideways Slide credit;
  collision-free Risky credit with rearm; visible hazard contact, short retry
  and optional assistance conversation; stage-local score, rank/best-result
  settlement and separately retained square credits; present route and style
  feedback; common music/level clock and live input with pause available.
- Excluded: treating this as an endless runner, free throttle/brake racing,
  tilt-to-turn Temple Run or free two-axis flight; independent rhythmic jump,
  combat, sword, button-mash and bow prompts introduced in other songs; car
  drift, world switching, teleport exploits and later boss transformations;
  the Zodiac meta-riddle objective; whole-album, Yolo, Wild and Remix modes;
  mandatory Gold, every pickup or twenty near misses as ordinary clear gates.
  Do not infer an explicit multiplier HUD from score changes. The soundtrack
  supports route cadence; the developer explicitly distinguishes this arcade
  structure from making every steering input a rhythm-graded note.
- Potential scoped modules: Fighting Hearts timed actions; later bow targeting;
  Night Drift car control; Parallel Universes switching; whole-album modes.
- Direct-play status: none. Primary creator explanation, the 2019 controls
  interview and Apple's 2020 design interview establish the route clock and
  relative touch design. Inspected three 160×90 static sheets at five-second
  steps from Pocket Gamer's release-day iPhone montage, and three 160×90 sheets
  at ten-second steps from rrvirus's labelled release-period iOS recording.
  The latter includes the complete Doki Doki Rush route/result around
  05:30–07:20; adjacent sampled stages provide context, not extra admitted
  systems. Small static frames cannot establish exact hitboxes, native timing
  or point coefficients. No stream/audio playback or foreground window.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SWH-001` | The original iOS release launched on Apple Arcade on 19 September 2019; later availability and Remix modes are separate targets. | Observation | Direct | High | P1, P2 |
| `SWH-002` | Relative finger movement steers local placement while a master animation carries the route, camera and musical events; Doki Doki Rush is the first motorcycle city level. | Observation | Corroborated | High | P1, P2, P3, V1, V2 |
| `SWH-003` | Contact pickups contribute increasing values through separate small-heart, large-heart and square-coin sequences; collision resets collection multiplication. | Observation | Corroborated | Medium | S1, S2, S3, V2 |
| `SWH-004` | Long lateral movement can score Slide; eligible collision-free proximity can score Risky; neither style credit is the pickup multiplier. | Observation | Corroborated | Medium | S1, S2, S4, V1, V2 |
| `SWH-005` | The song settles stage-local points/rank and a retained best result; ordinary completion does not require Gold or every pickup. | Observation | Corroborated | High | S1, S3, S4, V2 |
| `SWH-006` | Nearby checkpoint retry and optional repeated-failure Magician skips support continuation; accepting a skip misses that section's earning opportunities. | Observation | Corroborated | High | S3, S4, S5, S7 |
| `SWH-007` | Exact independent-counter formulas, style rearm and advanced frame techniques come from a Mac tool-assisted account, not authenticated iOS execution; broad advice conflicts on shared multiplication. | Observation | Limited | Medium | S1, S2, S6 |
| `SWH-008` | Square-coin credits appear separately above the best result on selection cards; full clear and optional collection are different predicates. | Observation | Corroborated | Medium | S4, V2 |
| `SWH-009` | This stage does not introduce the later QTE combat; song synchronisation is not a universal note-hit or survival-gauge rule. | Observation | Corroborated | High | P1, P3, S1, V2 |

## Basic data

- Release / origin: Simogo; published by Annapurna Interactive. Initial
  iOS/Apple Arcade release 19 September 2019. The creator names Star Fox,
  Space Harrier, Rez and other arcade inspirations; none proves an identical
  genome. Contemporary genre shorthand is not a rule source.
- Platform or physical form: historical original iPhone/iOS, English, one
  player, touchscreen; structured target `PLAT-IOS`. Device/os build, touch
  sensitivity and frame-rate coefficients were not independently measured.
- Puzzle family: live system pressure from the advancing authored route.
  No one-game family or genre-only rhythmic classification is created.
- Primary sources:
  - P1: [Simogo game/development page](https://simogo.com/work/sayonara-wild-hearts/),
    original release and delisting dates; direction/button simplicity; master
    level animation, road, camera and event values; distinction from universal
    rhythm-note play. Its current later-platform sections remain separate.
  - P2: [Apple, Behind the Design, 7 August 2020](https://developer.apple.com/news/?id=33kvkagk),
    creator testimony about finger-motion-based steering, camera compensation,
    legible shapes and approachable arcade design. No personal audio analysis.
  - P3: [Simon Flesser controls interview, 22 October 2019](https://www.gamedeveloper.com/design/paring-down-the-elegant-control-scheme-of-i-sayonara-wild-hearts-i-),
    authored rail progression and prompts in the wider game; removed free
    exploration and simultaneous clones are rejected prototypes, not rules.
- Secondary sources:
  - S1: [ikuyo's Mac tool-assisted submission](https://tasvideos.org/7974S),
    explicit executable/platform/method provenance, class-specific pickup
    multiplication, reset, Doki Doki Rush, style thresholds/rearm and stage
    rank. Its Gold 30,000 report is a reference parameter, not certified iOS
    parity. Slide chaining, pause rearm and later duplication are excluded.
  - S2: [release-period Touch Tap Play guide](https://www.touchtapplay.com/sayonara-wild-hearts-cheats-tips-tricks-guide-to-getting-all-gold-ranks/),
    14 November 2019, ordinary pickups and style bonuses. Its statement that
    collecting hearts increases a later diamond multiplier is broader than
    S1's separate-class description; do not collapse the counters or infer a
    missed-note timeout from the phrase about collecting at a good rate.
  - S3: [MacStories Apple-platform account](https://www.macstories.net/reviews/arcade-highlights-sayonara-wild-hearts/),
    actual iPhone touch/sensitivity use, frequent checkpoints, ranks and skip.
  - S4: [TheSixthAxis release-period Zodiac guide](https://www.thesixthaxis.com/2019/09/28/sayonara-wild-hearts-zodiac-riddles-guide-trophies-ps4/),
    28 September 2019, Doki Doki Rush hazards/near passes, square-credit row,
    unranked clear and optional skip. It is console corroboration, not native
    iOS coefficient verification or a claim to have completed Zodiac riddles.
  - S5: [TouchArcade original iOS review](https://toucharcade.com/?p=260745),
    public indexed touch/sensitivity and skip account. Direct retrieval is
    restricted; no bypass or claim of reading a fetched complete page.
  - S6: [general Xbox walkthrough](https://www.trueachievements.com/game/Sayonara-Wild-Hearts/walkthrough/2),
    public indexed same-class pickup increments and flat style values. Direct
    access requires payment; it was not bypassed. Used only as corroboration.
  - S7: [accessibility study, Figure 16, printed p. 59](https://repositorio.unb.br/bitstream/10482/44828/1/2022_VictoriaAlbuquerqueSilva.pdf),
    public indexed caption/text explicitly documents the three Magician
    response choices, including suppression. Full PDF retrieval returned 503;
    no claim of a fetched or visually inspected complete PDF, or native iOS
    binary parity. Used only for the offered-response boundary.
  - V1: [Pocket Gamer iPhone montage](https://www.youtube.com/watch?v=JWMR6eKuLZM),
    375 seconds; inspected three static sheets, five-second sampling,
    160×90 cells. This is an edited montage, not a continuous complete stage.
    [Companion release-day article](https://www.pocketgamer.com/sayonara-wild-hearts/sayonara-wild-hearts-gameplay-video-a-genre-bending-synth-explosion/)
    establishes the iPhone/Apple Arcade context.
  - V2: [rrvirus labelled iOS Apple Arcade recording](https://www.youtube.com/watch?v=YRAjLj0VwrE),
    1,155 seconds, 27 September 2019. Three inspected static sheets cover
    0–740 seconds, including Doki Doki Rush selection, motorcycle route,
    closeout and successor card. No playback, personal input or audio claim.
- Claim IDs: `SWH-001`–`SWH-009`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, direct local rider placement across the current
  traversable course with relative finger displacement. Longitudinal motion
  is authored, not a free forward/back axis or remote destination command.
  `ACT-232` selects the Magician's offered authored response, changing section
  continuation or further offers; it is not a new attack/weapon control.
- Candidate genes: none. Input modality, sensitivity and camera compensation
  parameterise placement rather than create a new per-device verb.
- Parameters: lateral offset, touch motion, authored width, current assistance
  speaker/response and offered continuation; `SWH-002`, `SWH-006`.

### System Behaviour Genes

- Existing gene IDs: `SYS-037` contact collection; `SYS-369` latest authored
  section restoration; `SYS-496` the shared song/road/event clock.
- Candidate genes: accepted `SYS-1610` per-class pickup multiplication,
  `SYS-1611` lateral-distance style credit, `SYS-1612` rearmed near-pass
  credit, `SYS-1613` song rank/best-result settlement and `SYS-1614`
  optional repeated-failure assistance.
- Resolution order: local placement → contact or safe proximity → corresponding
  pickup/style credit; collision → interrupted section, collection reset and
  checkpoint retry → optional skip after repeated failures; authored endpoint
  → level score/rank, retained best/square credits and selectable next stage.
- Parameters: small/large/square classes, base values, collection count,
  lateral travel, safe-pass band, rearm, checkpoint and rank cutoffs. Exact
  iOS constants and field-by-field rollback remain unmeasured; `SWH-002`–`SWH-008`.

### Constraint Genes

- Existing gene IDs: `CON-113`, visible collision is terminal for the current
  local section attempt before its ordinary continuation; there is no player
  health pool that simply absorbs the collision.
- Candidate genes: none. Do not import Temple Run's corner-swipe versus tilt
  distinction or Geometry Dash's checkpoint-free whole-level retry.
- Scarce strategic resources: one live opportunity to enter each pickup line
  or safe gap, plus collection multiplication at risk; no finite lives or
  fuel budget is invented; `SWH-002`, `SWH-003`, `SWH-006`.

### Information Genes

- Existing gene IDs: `INF-179`, visible local rider, road, collectibles and
  hazards; `INF-194`, soundtrack/visual cadence of authored route events.
- Candidate genes: `INF-533`, live score/style and card rank/best/square
  information without inventing a complete explicit multiplier readout.
- Information boundary: dynamic camera does not expose the entire future
  course, and a score delta is not an authoritative visible counter;
  `SWH-002`–`SWH-005`, `SWH-007`–`SWH-009`.

### Objective Genes

- Existing gene IDs: `OBJ-002`, maximise this run's points; `OBJ-181`, finish
  the selected authored stage, settle its closeout and return to selection
  with completion/credited optional squares retained. Neither requires the
  whole square roster, Gold, every riddle or a no-death whole album.
- Candidate genes: none. The score chase and ordinary route clear are distinct.
- Success, evaluation and failure: reach Doki Doki Rush's end and successor
  selection; compare score/rank separately. A crash retries the local section,
  and a skip omits earning opportunities rather than performing the route;
  `SWH-003`, `SWH-005`, `SWH-006`, `SWH-008`.

### Time Genes

- Existing gene IDs: `TIM-003`, steering remains available while the authored
  course and song advance; pause/retry are explicit parameters. No universal
  per-note timing grade or call-and-response rhythm phase is admitted here.
- Candidate genes: none; `SWH-002`, `SWH-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A small heart line approaches on the authored route | Move the finger laterally toward it | Rider placement changes; course still advances | Direct offset rather than steering route time | SWH-002 |
| Eligible item intersects the rider | Continue through its contact region | Item is credited once and its own class sequence advances | Contact action and scoring response are different | SWH-003 |
| Two item classes have different prior counts | Collect another small heart, then a square | Each uses its own class state | No shared chart-note multiplier is assumed | SWH-003, SWH-007 |
| A pickup is missed without collision | Continue the route | Its points are missed; no mistimed-note penalty is invented | Missing an optional item differs from crashing | SWH-003, SWH-009 |
| Eligible long sideways bike movement | Complete the lateral relocation | Separate Slide style credit when its predicate is met | A bonus is not a brake/drift command | SWH-004 |
| An obstacle passes close without contact | Keep a safe gap through the encounter | Eligible Risky credit subject to rearm | Near miss differs from taking damage | SWH-004, SWH-007 |
| Bike actually hits a traffic hazard | Retry after interruption | Nearby checkpoint restores the section; pickup multiplication resets | Local retry, not whole-level life-stock loss | SWH-003, SWH-006 |
| Repeated section failures expose the Magician | Accept, decline or suppress its offer | Skip the section, retry it or prevent further offers | Assistance is opt-in and misses earning opportunities | SWH-006 |
| Ordinary authored endpoint reached | Accept song closeout | Points/rank, best/square credits and next selectable card | Clear and optional score grade differ | SWH-005, SWH-008 |

## Strategic and experiential structure

- Local decision: choose a heart line, maintain a safe gap or spend lateral
  space on style; a confident near pass can score but collision breaks the run.
- Medium-term planning: learn the authored camera/traffic sequence and separate
  small-heart, large-heart and square routes rather than chase a fictional
  universal beat multiplier.
- Long-term structure: retained best score and square row invite replay;
  later album/riddle systems are acknowledged but excluded from this packet.
- Common heuristics: prioritise an ordinary clear, then improve optional
  collection/style routes. Gold is an evaluation goal, not a compulsory exit.
- Failure attribution: visible contact and short replay make the hazard local,
  while exact multiplier internals are less legible than the score feedback.
- Player-trust factors: retries and optional assistance preserve access to the
  next section; historical availability is not advertised as current access.
- Claim IDs: `SWH-002`–`SWH-009`.

## Replay and variation

- What changes between sessions: touch sensitivity, line choice, missed items,
  near passes, slides, collisions, assistance and final score.
- Randomness or procedural generation: no procedural level or randomly chosen
  traffic layout is inferred; authored progress and soundtrack recur together.
- Multiple viable strategies: safe clear, improved heart/square collection or
  riskier style optimisation. Exact tool-assisted maxima are not native goals.
- Typical replay motive: improve rank/best result and missing square credits;
  no personal replay record is claimed.
- Claim IDs: `SWH-002`–`SWH-008`.

## Adjacent systems and history

- Direct predecessors: the creator cites rail arcade games and a pop-album
  structure; a discarded prototype with free exploration/clones is not included.
- Variants: original iOS touch, console/controller, Mac tool assistance and
  later Remix are separately evidenced; no exact timing parity is asserted.
- Similar games: detailed numerical comparison is restricted to the selected
  complete signatures below; a music-game label is not a similarity algorithm.
- Important differences: lateral choice and near-pass risk are not a full
  note-chart objective, Rock Meter survival or prompted combat for this stage.
- Claim IDs: `SWH-001`, `SWH-002`, `SWH-007`, `SWH-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-232` | local offset, offered helper response |
| System Behaviour | `SYS-037`, `SYS-369`, `SYS-496`, `SYS-1610`, `SYS-1611`, `SYS-1612`, `SYS-1613`, `SYS-1614` | pickups, local retry, song clock, separate scores, rank, assistance |
| Constraint | `CON-113` | designated visible collision |
| Information | `INF-179`, `INF-194`, `INF-533` | current route, cadence, live/result feedback |
| Objective | `OBJ-002`, `OBJ-181` | maximise score and clear ordinary stage |
| Time | `TIM-003` | live authored progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `555` (`GAME-0001`–`GAME-0555`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`5 / 25 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0394` — LittleBigPlanet 2 | `ACT-008`, `SYS-037`, `SYS-369`, `INF-179`, `TIM-003` | Both combine local body movement, contact pickups, visible local geometry and authored checkpoint retry under live progression. LittleBigPlanet 2 uses player-driven platform traversal, object manipulation and optional prize bubbles; this song prescribes forward/camera time, distinguishes per-class pickup values and style, and offers local assistance before score/card settlement. The shared structure does not equate their movement freedom or musical demands. | Tied near; `5 / 25 = 0.200000` |

- New genes: six additions, eleven definitions reused unchanged.
- Classification result: `New gene`.
- Evidence and reasoning: complete prior-signature and verified-combination
  scan separates route/score decisions from a broad music-game label.

### Preserved research notes

- New genes: six additions, eleven definitions reused unchanged.
- Classification result: `New gene`.
- Evidence and reasoning: complete prior-signature and verified-combination
  scan separates route/score decisions from a broad music-game label.

## Taxonomy impact

- Registry changes: SYS-1610–SYS-1614 and INF-533.
- Taxonomy-change record: [TAXONOMY_CHANGE_302](../../../research/taxonomy-changes/TAXONOMY_CHANGE_302.md).
- Candidate terms affected: class-specific collection multiplication,
  independent lateral/near-pass style, song settlement and opt-in skip.

## Negative results

- No separate record. Rejected reuse boundaries are documented in the taxonomy
  decision; no prior gene or game signature is revised.

## Delta summary

The following compact ledger records changes rather than restating the analysis.

## New facts

- [Observation | Corroborated | High] Authored music-route movement differs
  from universal note grading; ordinary clear differs from optional Gold;
  SWH-002, SWH-005, SWH-009.
- [Observation | Limited | Medium] Exact class/rearm constants are cross-platform
  corroboration, not authenticated iOS coefficients; SWH-007.

## New genes

- [Observation | Corroborated | Medium] Six bounded additions; exact native
  coefficients and field-by-field rollback remain unmeasured.

## New combinations

- [Observation | Corroborated | High] No combination invented; deterministic scan owns support.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_302 adds definitions only.

## New questions

- [Hypothesis | Limited | Medium] A future authorised original iOS experiment
  could test separate counters, style rearm and every restored field; a
  platform difference would reject unverified coefficient parity.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0557 Boktai: The Sun Is in Your Hand, GBA.
- Optimisation criterion: retain Selection 044's platform and era alternation.
- Expected information gain: physical solar input and bounded stealth/combat.
- Backlog impact: preserve Moss as the final approved subject.

## Why this game

- [Hypothesis | Limited | Medium] A released iOS arcade route contrasts with
  the preceding GameCube housekeeping and tests score versus ordinary clear.
