---
game_id: GAME-0551
slug: ridge-racer-type-4
game_title: "R4: Ridge Racer Type 4"
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-608
    - ACT-609
  system:
    - SYS-320
    - SYS-369
    - SYS-515
    - SYS-516
    - SYS-1595
    - SYS-1596
  constraint:
    - CON-068
    - CON-183
    - CON-438
    - CON-818
  information:
    - INF-204
    - INF-205
    - INF-206
    - INF-208
  objective:
    - OBJ-304
  time:
    - TIM-003
---

# Game: R4: Ridge Racer Type 4

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A qualifying heat is not a cumulative-points cup. A stage machine is not yet
an owned Garage car, and a tail slide is not a stored Mini-Turbo charge.

## Analysis scope

- Version / ruleset: original English North American PlayStation main game,
  1999, catalogue target `SLUS-00797`. The Japanese game first appeared in
  1998; that origin is not assigned to the later North American disc. Exclude
  the bonus Ridge Racer Turbo Mode disc, PlayStation Classic and modern
  wrappers with rewind or instant-save features. No disc, native executable,
  installed checksum, purchase entitlement or exact revision was inspected.
- Structured analysis target: `PLAT-PLAYSTATION`, original single-player
  Grand Prix. Prescribe a fresh Real Racing Roots '99, Pac Racing Club
  Normal tuning, Assoluto, initial Promessa, AT and an ordinary DualShock.
  This is a reproducible chosen setup, not authentication of the public
  capture's exact controller, transmission, disc or input configuration.
- Entry: commit the team, manufacturer and automatic transmission before
  the first grid, without acquired cars, cheats or an imported save.
- Primary decision loop: read course shape, speed, gear, lap, place and
  remaining time; steer, accelerate or brake to choose a racing line. With
  the supplied drift-profile Assoluto, steer inward while lifting throttle,
  then reapply it to initiate the tail slide and counter-steer toward a usable
  exit. Complete two Helter Skelter laps and then two Wonderhill laps, each
  classified third or better before its deadline. Accept the manager's
  performance-dependent vehicle assignment for Heat 2 instead of treating the
  first finish as the whole stage or treating every qualifying finish as a win.
- Positive exit: settle both first-heat classifications, accept the manager's
  next-machine or old-machine-tune handoff and stop before live control on
  Edge of the Earth. No best variant is guaranteed. The remaining six races,
  whole-GP victory and Garage ownership are outside this terminal.
- Failure and recovery: missing a race's place cut or exhausting its timer
  retires that race attempt. Retry repeats that race within the finite
  declared chance allowance, not from an arbitrary mid-lap position. The
  manual calls it four chances; the native initial-attempt versus retry
  counter, off-by-one convention and refill between races were not measured.
  No available continuation means Game Over; End abandons the GP. No
  deletion of an earlier Memory Card file is inferred from Game Over.
- Retention qualification: the original booklet offers GP saving after Heat 1.
  The handoff is documented campaign continuation, not an executed save/load
  experiment or a measured list of restored fields. New cars become
  registerable in Garage only after completing the entire Grand Prix.
- Included: supplied setup selection, direct driving and view switching,
  throttle-release drift preparation, vehicle contact, ordinary computer
  rivals, ordered two-course/lap progress, individual place qualification,
  the deadline, same-race retry, results, manager evaluation and successor
  vehicle assignment. Team tuning is documented; exact opponent coefficients
  and any rubber-banding algorithm remain unmeasured.
- Excluded: manual live shifts, fourth-gear launch tricks, nitro or Mini-Turbo,
  weapons, combat damage pools, fuel or repair spending, exact traction/AI
  coefficients, second heat, final races, the full 320-variant formula,
  Extra Trial, Garage registration, decals, PocketStation, VS, Time Attack,
  Jogcon/neGcon inputs, other regions and wrapper save states. A Grip setup,
  a manual-gear run, Jogcon, later qualification and full ownership/registration
  each requires its own bounded packet.
- Direct-play status: no PlayStation, disc, executable, controller, save or
  native input session was used. Read the official-hosted English rules and
  the publicly visible text of an original Namco booklet. Eight public
  storyboard sheets, at ten-second sampling, were inspected from a declared
  NTSC longplay without audio/video playback or foreground windows. They
  corroborate the route, HUD and handoff, not exact native inputs or physics.
  Blocked secondary pages supply only their readable search excerpts.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RR4-001 | The original game has two qualifying heats of two races followed by four finals; this packet ends after the first heat and successor-machine handoff. | Observation | Corroborated | High | P1 pp. 2–3, P2 pp. 8–15, R1 |
| RR4-002 | Team/manufacturer and transmission assign a supplied machine. PRC is Normal; Assoluto and Lizard are Drift, while Age Solo and Terrazi are Grip. | Observation | Direct | High | P1 pp. 2–5, P2 pp. 12–14; S2 names Promessa |
| RR4-003 | In the documented Drift method, lifting throttle and steering inward prepares a slide resolved on reapplication; a longer release/turn gives a stronger slide, and counter-steering settles the exit. | Observation | Corroborated | High | P1 p. 6, S2; exact coefficients unmeasured |
| RR4-004 | Heat 1 orders Helter Skelter then Wonderhill, two laps each; each result must be third or better before its race deadline. Earlier success cannot compensate for a later failed cut. | Observation | Corroborated | High | P1 general qualification, P2 pp. 10–11, S1 first-heat table, R1 |
| RR4-005 | At stage boundaries the manager evaluates performance and supplies a new variant or tunes the current machine; Garage registration waits for the whole GP win. | Observation | Corroborated | High | P2 pp. 14–15, P1 Garage boundary, R1 57:40–58:20 |
| RR4-006 | The stated four-chance limit bounds same-race retry; exhausted continuation ends the GP. Exact native counter conventions and race-to-race replenishment remain unmeasured. | Observation | Direct | Medium | P1 p. 2, P2 pp. 10–11 and 15 |
| RR4-007 | Driving views expose speed/gear, course/lap, place, timing and nearby rivals; the original booklet distinguishes Driver's View and Overhead Cam. | Observation | Corroborated | High | P2 pp. 10–11, R1 |
| RR4-008 | A documented save opportunity follows Heat 1, but no native save/load or disc authentication was performed. | Observation | Direct | High | P2 p. 15; method qualification |

## Basic data

- Release / origin: Namco, original PlayStation game first issued in Japan
  on 3 December 1998. The selected English North American main game is the
  1999 release; day-of-month catalogues disagree, so none is used as a build
  identity. The fiction's May 1999 race dates are not distribution metadata.
- Platform or physical form: original PlayStation, English main game,
  prescribed AT and DualShock, not an arcade cabinet or a modern port's wrapper.
- Mechanical families: `FAM-007` for a momentum-bearing vehicle/traction
  problem and `FAM-010` for live rivals and a failure deadline.
- Primary sources, checked 2026-11-19:
  - **P1** [English R4 rules on PlayStation's official server](https://secure.cdn.us.playstation.com/manuals/classic/games/r4-ridge-racer-type-4-manual-en.pdf),
    eight-page reissued booklet: control classes and qualification on PDF p. 2,
    Garage on p. 3, manufacturers/teams on pp. 3–5, cornering on p. 6.
    It is documentary rules evidence; it does not authenticate a 1999 binary
    or grant the later wrapper's rewind to the original game.
  - **P2** [Original Namco booklet, publicly visible transcription](https://www.scribd.com/document/876606634/R4-Ridge-Racer-Type-4-1998-Namco-JP-SCPS-45356),
    printed pp. 8–15 and 21–23: view/HUD, same-race Retry, team/maker selection,
    stage investment, GP save opportunities and deferred Garage registration.
    The upload title attributes SCPS-45356, not the selected SLUS disc. Shared
    rules are corroborated by P1 and the English visual route; exact regional
    binary and button-label parity are not asserted. Only its openly visible
    transcription was read; no paywall or download restriction was bypassed.
  - **P3** [Namco release catalogue](https://www.bandainamcoent.co.jp/corporate/press/namco/51/51-022refer.pdf),
    search-visible historical table gives the Japanese 1998-12-03 release.
    Direct PDF retrieval was blocked; no unseen pages or revision are claimed.
  - **P3** [Namco historical product table](https://www.bandainamcoent.co.jp/corporate/press/namco/51/51-022refer.pdf),
    readable search listing identifies the original PlayStation date as
    1998-12-03. Direct PDF retrieval was blocked; it does not authenticate
    the later North American disc.
- Visual evidence:
  - **R1** [LongplayArchive, declared NTSC PlayStation route](https://www.youtube.com/watch?v=tEpkmjYldqc),
    first-heat sheets at 0:00–16:30 and 45:50–62:20, ten-second cells.
    The first sequence shows both heat races and a next-machine transition;
    the PRC portion introduces a supplied yellow/red car before 49:12,
    Wonderhill begins around 53:49 and the next-stage investment/save interface
    appears around 57:40–58:20. Its author names a 1999 NTSC release, but
    provides no disc checksum or native controller proof. The precise car,
    gearbox, interpolation and patch are not authenticated from tiny cells.
- Secondary sources:
  - **S1** [StrategyWiki first-heat route table](https://strategywiki.org/wiki/R4%3A_Ridge_Racer_Type_4/Walkthrough),
    readable search rendering: third-place cut, two laps and ordered courses.
    Direct retrieval was blocked; no full-page review is claimed.
  - **S2** [First-hand Drift/Grip and car guide](https://www.speedrun.com/rrt4/guides/0k29s),
    read drift paragraphs and maker table; initial Assoluto is Promessa.
    Its exact speed table and fourth-gear start procedure are outside this
    automatic-gear packet, not a source of free nitro or a certified optimum.
  - **S3** [North American disc catalogue](https://psxdatacenter.com/games/SLUS-00797.html),
    identifies the English `SLUS-00797` main disc and distinct bonus disc.
    Its printed day differs from other catalogues; no exact day-to-binary map.
- Claim IDs: RR4-001–RR4-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-608` for committing a supplied team/maker/transmission profile,
  `ACT-290` for direct steering, throttle and brake, and `ACT-609` for choosing
  the fixed driver's/chase viewpoint. Automatic shifts belong to the prescribed
  machine profile, not an invented player gear action.
- Drift preparation uses these ordinary inputs; no handbrake, charged drift
  button, boost-spend action or owned-Garage selection is added.
- Claim IDs: RR4-002, RR4-003, RR4-007.

### System Behaviour Genes

- Reuse `SYS-320` for vehicle motion/contact without a persistent damage or
  fuel pool. Reuse `SYS-515` for the ordinary configured computer race field;
  team tuning does not prove a particular rubber-banding equation or an
  independently selected AI slider. Native pace coefficients are unmeasured.
- Reuse `SYS-516` to classify required laps and finish order and `SYS-369`
  for returning a failed attempt to that race's authored starting state.
  Completed earlier races do not become arbitrary mid-lap return anchors.
- Add `SYS-1595` for the preparation/reapplication drift transition, which is
  different from Mario Kart's charged-and-released acceleration award.
- Add `SYS-1596` for the next supplied machine's performance-based assignment,
  including a tune of the current body. `SYS-519`'s ordinary completion/reward
  transfer does not specify that pre-successor selection protocol; it is not
  double-counted as a second car award. Stage supply and later Garage
  ownership remain separate.
- Claim IDs: RR4-003–RR4-006.

### Constraint Genes

- Reuse `CON-438` for valid ordered course/lap completion, `CON-068` for
  terminal race-clock expiry and `CON-183` for a finite disclosed continuation
  stock. Its carrier is race chances rather than body lives; neither an exact
  unobserved counter convention nor automatic file deletion is inherited.
- Add `CON-818`: each race must independently meet its qualifying-place cut
  before the successor is legal. First-heat third place is accepted; earlier
  first place cannot buy forgiveness for later fourth place. This is neither
  a cumulative cup score nor a generic shared progression currency.
- Claim IDs: RR4-004, RR4-006.

### Information Genes

- Reuse `INF-204` for speed/gear/road cues, `INF-205` for place, lap, time and
  local rivals, `INF-206` for the selected stage's route and entry terms, and
  `INF-208` for the classified result and subsequent manager handoff.
  There is no disclosed complete future AI path or a numeric investment
  formula. Music changes are presentation, not a new timing mechanic.
- Claim IDs: RR4-001, RR4-004, RR4-005, RR4-007.

### Objective Genes

- Add `OBJ-304` for both individually qualifying races and the stage handoff.
  `OBJ-150` settles one race; `OBJ-226` demands one first place plus Cup points;
  `OBJ-146` reduces a cross-country campaign rank. None is this complete
  per-race-cut heat, and `OBJ-180`'s cumulative trophy would be incorrect.
- Claim IDs: RR4-001, RR4-004, RR4-005.

### Time Genes

- Reuse `TIM-003`: rivals, motion and the authoritative race timer advance
  while steering and throttle choices are made. Paused menus are not live
  progression; no rhythm score, turn budget or measured native frame window.
- Claim IDs: RR4-003, RR4-004, RR4-007.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Fresh GP, no owned racing collection required | Commit PRC, Assoluto and AT | Assign the initial supplied Promessa profile | Team/brand/transmission is not a Garage purchase | RR4-002 |
| Drift-profile car approaches a bend | Steer inward while reducing throttle, then accelerate | Prepared steering resolves into a tail slide | Not a held drift-button Mini-Turbo | RR4-003 |
| Same eligible curve, longer released-throttle steering | Reapply throttle and counter-steer | Stronger documented slide, then controlled exit | Qualitative preparation matters; no fitted coefficient | RR4-003 |
| A narrow bend requires a different line | Brake or adjust steering | Ordinary motion/contact changes speed and position | No fuel price or combat-health inference | RR4-003, RR4-007 |
| First required Helter Skelter lap is complete | Cross its line again after lap two | Classify the complete race | One circuit alone is not the two-lap result | RR4-004 |
| Valid first race before timeout | Finish third or better | Continue to Wonderhill in the same first heat | First place is not the only accepted result | RR4-004 |
| A classified finish is fourth or lower, or time expires | Accept retirement and eligible Retry | Repeat the same race within declared remaining chances | No arbitrary mid-lap restore or compulsory new GP on every mistake | RR4-006 |
| No legal remaining continuation | Fail qualification again | Game Over ends the current GP | No unlimited free retries; no save-file destruction claimed | RR4-006 |
| Helter Skelter first place but Wonderhill fourth | Settle the second result | No Heat 2 qualification from the earlier first | Individual cuts differ from cumulative-points compensation | RR4-004 |
| Both two-lap race cuts satisfied | Accept the manager's review | Supply a performance-dependent next variant or old-car tune | Qualification and machine quality are different outcomes | RR4-005 |
| New stage machine is supplied | Reach the Heat 2 handoff/save opportunity | Retain documented GP continuation before Edge of the Earth | Stage assignment is not yet Garage registration | RR4-005, RR4-008 |
| Current driving state uses the rear viewpoint | Switch the fixed view | Same car state, different visible framing | Not a changed physical route | RR4-007 |

Documentary checks, not a claimed native playthrough. Exact initial timer,
retry arithmetic, investment cutoffs and save/load state sets remain unmeasured.

## Strategic and experiential structure

Throttle preparation trades immediate forward speed against the yaw needed
for a bend. A longer slide is not automatically a faster line. Qualifying
third can preserve the campaign while first-place results may improve the
next assignment; the stage therefore separates minimum acceptance from
subsequent machine quality. Finite chances price repeated failed attempts.
No exact optimal line, AI compensation or complete variant-unlock table is
claimed. Claim IDs: RR4-003–RR4-008.

## Replay and variation

The first-heat courses and two-lap contracts are authored. Timing, place,
remaining chances and the subsequent investment can vary. Another manufacturer
changes the handling class; another team changes the declared tuning context.
The later stages, full win and Garage registration form distinct continuation
and collection questions, not a reason to stop after one race. Claim IDs:
RR4-001–RR4-008.

## Adjacent systems and history

This is the PlayStation R4 campaign, not the original 1993 arcade Ridge Racer,
Rage Racer or the supplied Turbo Mode bonus disc. The 1998 origin and 1999
English North American target are separately recorded. A modern official
manual republishes rules but does not prove a particular original binary or
supply wrapper save states. Claim IDs: RR4-001, RR4-008.

## Normalised genome

| Type | Active genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-290`, `ACT-608`, `ACT-609` | Supplied setup, direct driving and fixed view |
| System Behaviour | `SYS-320`, `SYS-369`, `SYS-515`, `SYS-516`, `SYS-1595`, `SYS-1596` | Motion, same-race retry, rivals, classification, drift and stage investment |
| Constraint | `CON-068`, `CON-183`, `CON-438`, `CON-818` | Deadline, finite chances, valid laps and individual cuts |
| Information | `INF-204`, `INF-205`, `INF-206`, `INF-208` | Driving, course terms, race and stage results |
| Objective | `OBJ-304` | Complete the whole first qualifying heat |
| Time | `TIM-003` | Live input against ongoing motion and rivals |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `550` (`GAME-0001`–`GAME-0550`).
- Exact genome matches: none.
- Tied near matches: `GAME-0457` — Sega Rally Championship (`11 / 24 = 0.458333`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0457` — Sega Rally Championship | `ACT-290`, `ACT-608`, `ACT-609`, `CON-068`, `CON-438`, `INF-204`, `INF-205`, `SYS-320`, `SYS-515`, `SYS-516`, `TIM-003` | Both select a supplied car, directly drive against rivals, switch fixed views and classify ordered laps with driving/race feedback. Sega Rally uses a manual Celica through Desert, Forest and Mountain, preserving checkpoint time credits and a conditional hyper course. R4 uses AT Assoluto, two independent third-place cuts, finite same-race chances and performance-based stage supply; no Sega checkpoint-time credit, hand shifting or hyper-course branch transfers. | Near, `0.458333` |

### Preserved research notes

- New genes: `SYS-1595`, `SYS-1596`, `CON-818`, `OBJ-304`.
- Classification result: New gene.
- Evidence and reasoning: fifteen existing boundaries transfer unchanged;
  throttle-return drift, stage-supplied performance investment and the complete
  per-race-cut qualifying heat require separate operational statements.

## Taxonomy impact

- Fifteen Active definitions are reused and four are added; nineteen in total.
- Registry changes: four new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_297](../../../research/taxonomy-changes/TAXONOMY_CHANGE_297.md).
- Candidate terms affected: none.

## Negative results

- none. Qualified uncertainties are not negative registry decisions.

## Delta summary

## New facts

- [Observation | Corroborated | High] The two first-heat races each require
  qualification; the manager's next-machine outcome is distinct from that cut.

## New genes

- [Observation | Corroborated | High] Four definitions separate throttle-return
  slide, next-stage machine assignment, per-race legality and whole-heat success.

## New combinations

- [Observation | Corroborated | High] No new recurring combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_297`.

## New questions

- How do native retry counters treat the initial attempt and replenish at a new race?
- Which exact first-heat result/timing predicates select each successor variant?

## Next recommended game

- [Hypothesis | Limited | Medium] Jusant, `GAME-0552`, from
  [Selection 044](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_044.md).
- Optimisation criterion: alternate era, platform and control problem.
- Expected information gain: compare rope-supported ascent with timed racing.
- Backlog impact: seven approved subjects remain; no push or publication.

## Why this game

- [Hypothesis | Limited | Medium] A recognised PlayStation racer tests distinct
  throttle-mediated handling and qualification without importing modern racing
  economies, drift boosts or a complete car-collection campaign.
