---
game_id: GAME-0216
slug: trackmania
game_title: Trackmania
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0214
gene_ids:
  action:
    - ACT-290
  system:
    - SYS-320
    - SYS-516
    - SYS-628
    - SYS-711
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-251
  objective:
    - OBJ-133
  time:
    - TIM-003
---

# Game: Trackmania

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `2225070`, public Build ID `21751642`, built 2026-02-02 and published
  2026-02-04, checked 2026-09-01; `Trackmania Update 2026`, Starter Access.
- Platform and mode: Windows, online Ubisoft-account session, Solo official
  seasonal campaign. Account/network state is fixed entry context, not an
  analysed economy or social system.
- Entry: choose `Play` → `Solo` → `Summer 2026` → `01`; retain the countdown
  and begin at the first accepted car input after release on official map
  `Summer 2026 - 01`, UID `buNzfsVlp2NF2oWtHM3729dEylg`.
- Primary decision loop: read the authored road, next ordered waypoint, speed,
  gear, running time and medal target; steer, accelerate, brake or release
  input; let continuous traction and collision resolve; cross each required
  checkpoint in order; revise line and braking for the remaining route.
- Positive terminal: the first valid crossing of the finish after every
  required ordered checkpoint. The clock stops, the elapsed time is retained
  and the result is classified against the fixed Author `00:23.144`, Gold
  `00:25.000`, Silver `00:28.000` and Bronze `00:35.000` thresholds. A valid
  slower finish still completes the packet without awarding a new medal.
- Negative terminal: no separate evidence-backed loss grade is imported. A
  restart, abandonment or attempt that has not crossed every ordered waypoint
  is non-completion and produces no positive result for this packet.
- Included: one default Stadium/CarSport solo attempt; dedicated car input;
  road contact and collision; ordered Start, Checkpoint and Finish waypoint
  validity; live speed, gear, progress and clock; retained elapsed result; the
  four fixed medal thresholds and the highest threshold reached.
- Excluded: the other nine free Summer 2026 tracks and campaign aggregate;
  tracks 11–25; weekly Shorts and Grand Track; Arcade, Ranked, Royal, Stunt and
  live rooms; Club Access; community maps, editor, replays, ghosts, world/
  regional records and leaderboard history; repeated time optimisation after
  the first valid result; earlier campaigns; cosmetics, trophies and prestige;
  other environments, cars, platforms and the complete product history.
- Reproducible parameterisation: use Steam app `2225070`, public branch Build
  `21751642`, Starter Access, Solo, official `Summer 2026 - 01`, UID
  `buNzfsVlp2NF2oWtHM3729dEylg`, ordinary default controls and assists. Start
  from the countdown, finish one valid ordered run, retain the first result and
  stop before retry, leaderboard or another track.
- Potential scoped modules: one repeated personal-best/ghost optimisation
  loop, one official live room, one other environment/car, the map editor or a
  complete seasonal progression each needs its own entry and terminal.
- Direct-play status: not conducted. Official Trackmania product, access,
  campaign, map and documentation pages establish the bounded rules; SteamDB
  fixes the public build. The one inspected visual was an official static map
  thumbnail. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TM-001` | The current official product title is `Trackmania`, available on Windows through Steam with free Starter Access | Confirmed | Direct | High | P1, P2 |
| `TM-002` | Steam app `2225070` currently exposes public Build `21751642`; the later hotfix branch is opt-in preview state | Confirmed | Corroborated | High | P1, S1 |
| `TM-003` | Starter Access includes the first ten official seasonal campaign tracks in Solo and Live | Confirmed | Direct | High | P2, P3 |
| `TM-004` | `Summer 2026 - 01` is a Nadeo official Summer 2026 map with UID `buNzfsVlp2NF2oWtHM3729dEylg` | Confirmed | Direct | High | P3, P4 |
| `TM-005` | Trackmania race maps validate Start, Checkpoint and Finish waypoint triggers | Confirmed | Direct | High | P5 |
| `TM-006` | The scoped map publishes fixed Author, Gold, Silver and Bronze times of 23.144, 25.000, 28.000 and 35.000 seconds | Confirmed | Direct | High | P4 |
| `TM-007` | A valid run produces an elapsed result and retained personal result/medal information distinct from the live HUD | Confirmed | Direct | High | P4, P6 |
| `TM-008` | The car is steered under live speed, traction and road-contact consequences toward the next authored waypoint | Observation | Corroborated | High | P1, P4 |
| `TM-009` | Summer 2026 launched 2026-07-01 and is the current named campaign on the checked date | Confirmed | Direct | High | P3, P7 |

## Basic data

- Release / origin: Ubisoft Nadeo; Ubisoft. The current free Trackmania product
  launched on PC in 2020 and remains a live seasonal service.
- Platform or physical form: real-time solo precision driving on Windows; only
  one declared official Summer 2026 Starter Access map is scoped.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/2225070/Trackmania/),
    for title, Windows, Nadeo/Ubisoft, Starter Access, car control, surfaces,
    official seasonal tracks and medal/leaderboard framing.
  - **[P2]** [official Starter Access announcement](https://www.trackmania.com/news/7739?lang=en),
    for the first ten campaign tracks in Solo and Live.
  - **[P3]** [official 2026 campaign catalogue](https://www.trackmania.com/campaigns/2026?lang=en),
    for the current Summer 2026 campaign and map membership.
  - **[P4]** [official `Summer 2026 - 01` map page](https://www.trackmania.com/tracks/buNzfsVlp2NF2oWtHM3729dEylg?lang=en),
    for Nadeo authorship, official campaign identity, map UID and medal times.
  - **[P5]** [official waypoint documentation](https://doc.trackmania.com/create/nadeo-importer/07-how-to-make-a-waypoint-item/),
    for Start, Checkpoint and Finish waypoint roles and trigger detection.
  - **[P6]** [official map-page documentation](https://doc.trackmania.com/web/tm-com/map-page/),
    for medal times, personal best and result/ranking presentation.
  - **[P7]** [official Summer 2026 announcement](https://www.trackmania.com/news/9251?lang=en),
    for the 2026-07-01 seasonal launch.
- Corroborating source:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/2225070/depots/),
    for public Build `21751642` and exclusion of opt-in preview Build
    `24354606`.
- Claim IDs: `TM-001`–`TM-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: the player directly steers, accelerates and brakes the
  dedicated CarSport vehicle from countdown release to finish.
- Parameters: steering, throttle, brake, camera, input device, assistance and
  transmission state. Car selection and entering/exiting a seat are absent.
- Claim IDs: `TM-001`, `TM-008`.

### System Behaviour Genes

- Existing `SYS-320`: speed, traction, terrain contact and collision resolve
  continuously for the dedicated vehicle; damage and fuel parameters are not
  exposed by this packet.
- Existing `SYS-516`: the route accepts progress through ordered waypoints and
  settles elapsed time only at a valid finish.
- Existing `SYS-628`: the first valid finish stops and retains the completed
  elapsed Time Trial result; an unfinished/restarted attempt does not.
- New `SYS-711`: the valid elapsed result is compared with four fixed map
  thresholds and assigned the highest reached Author/Gold/Silver/Bronze class,
  or no new medal when slower than Bronze.
- Resolution order: accept live car input; integrate motion and road contact;
  validate the next ordered waypoint; update live progress/time; validate the
  finish; stop/retain time; classify the fixed medal threshold.
- Claim IDs: `TM-005`–`TM-008`.

### Constraint Genes

- Existing `CON-438`: the finish is valid only after the dedicated vehicle has
  crossed every required checkpoint in authored order.
- Scarce strategic resources: remaining road distance, speed carried into the
  next corner and elapsed margin to the chosen medal threshold. These are
  parameters, not new inventory genes.
- Claim IDs: `TM-005`–`TM-008`.

### Information Genes

- Existing `INF-204`: the live driving view exposes speed, gear and authored
  road/waypoint guidance needed to judge braking and steering.
- Existing `INF-205`: the race surface exposes checkpoint/course progress,
  running time and timed target without requiring a rival field.
- Existing `INF-251`: the finish transition exposes completed elapsed time,
  retained personal result and the map's fixed medal classification separately
  from the live clock.
- World-record history, ghosts and remote rival traces are excluded even if the
  product can display them elsewhere.
- Claim IDs: `TM-004`–`TM-008`.

### Objective Genes

- New `OBJ-133`: complete one valid ordered run of official `Summer 2026 - 01`
  and reach its retained elapsed/medal evaluation once.
- A checkpoint, partial route or countdown start is intermediate. A medal is a
  quality grade, not a prerequisite for the positive completion terminal.
- Claim IDs: `TM-004`–`TM-007`.

### Time Genes

- Existing `TIM-003`: vehicle motion, road contact, collision and elapsed
  attempt time continue while the player judges and provides live input.
- Claim IDs: `TM-005`–`TM-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| `Summer 2026 - 01` is selected | Accept the countdown and hold/adjust throttle and steering after release | The dedicated car begins one live timed attempt | exact bounded entry and direct control | `TM-004`, `TM-008` |
| A corner approaches at current speed | Brake, release throttle or revise steering | Traction and road contact change speed and line continuously | motion consequence and local planning | `TM-008` |
| The next ordered checkpoint is crossed | Continue through its trigger in the required sequence | Course progress advances and the next waypoint becomes authoritative | ordered-route validity | `TM-005` |
| A later gate is reached without required prior progress | Cross its geometry | The skipped route does not become a valid finished result | checkpoint constraint | `TM-005` |
| Every required checkpoint has been accepted | Cross the Finish trigger | The clock stops and the elapsed result is retained | positive terminal and retained time | `TM-005`, `TM-007` |
| Retained time is `00:24.500` | Settle the fixed map thresholds | Gold is reached; Author is not | highest fixed medal classification | `TM-006`, `TM-007` |
| Retained time exceeds `00:35.000` | Settle the fixed map thresholds | The run remains a valid completion but earns no new medal | medal is evaluation, not completion gate | `TM-006`, `TM-007` |

## Strategic and experiential structure

- Planning horizon: read the visible road and next checkpoint, choose entry
  speed and line, and preserve enough stability for the following corner while
  comparing the running clock with a medal target.
- Local tactics: brake before the turn, minimise corrective steering, carry
  usable exit speed and avoid collision that adds time.
- Long-term structure: one authored route converts a continuous line of local
  control decisions into a single retained time and fixed medal class.
- Reversible versus irreversible: steering corrections are local; crossed
  ordered checkpoints and the final retained time advance the attempt; a new
  retry belongs to another run and is excluded after the first result.
- Failure attribution: speed/gear, visible road, checkpoint progress, live
  clock and final medal thresholds distinguish late braking, missed order,
  collision and a valid but slower finish.
- Player trust: fixed route identity and published thresholds make the first
  terminal reproducible without relying on volatile world-record comparison.

## Replay and variation

- What changes between attempts: steering/braking trace, contact, checkpoint
  splits and elapsed result. Route identity, order and medal thresholds remain
  fixed for this unit.
- Randomness or procedural generation: none is admitted; the official map and
  thresholds are authored.
- Multiple viable strategies: several clean racing lines can finish; their
  elapsed classifications may differ.
- Typical replay motive: improve line and medal. The canonical packet stops
  before that repeated optimisation loop begins.

## Adjacent systems and history

- Direct predecessor corridor: earlier Trackmania seasonal campaigns share the
  official Time Attack grammar but are unavailable in Starter Access after
  their season and are excluded from this current track identity.
- Similar games: BeamNG.drive Road Master shares direct car control, ordered
  checkpoints, live timing and a retained result; Forza Horizon 6 shares race
  validation and driving information but adds rivals, selection and campaign
  settlement in its scoped opening.
- Important differences: this Trackmania packet has no admitted soft-body
  damage, recovery, rivals, traffic or campaign reward. Its distinctive
  terminal is a valid retained time classified against four immutable map
  medal thresholds.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290` | direct dedicated-car steering, throttle and brake |
| System Behaviour | `SYS-320`, `SYS-516`, `SYS-628`, `SYS-711` | live vehicle motion, ordered finish, retained time and fixed medal class |
| Constraint | `CON-438` | every required checkpoint before finish |
| Information | `INF-204`, `INF-205`, `INF-251` | driving cues, live progress/time and retained result/medal |
| Objective | `OBJ-133` | one valid evaluated Summer 2026–01 finish |
| Time | `TIM-003` | continuous motion and attempt clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `215` (`GAME-0001`–`GAME-0215`).
- Exact genome matches: none.
- Tied near matches: `GAME-0195` — BeamNG.drive (`9 / 15 = 0.600000`).
- Supported combination subsets: `COMB-0214`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0195` — BeamNG.drive | `ACT-290`, `SYS-320`, `SYS-516`, `SYS-628`, `CON-438`, `INF-204`, `INF-205`, `INF-251`, `TIM-003` | Both directly control one assigned car through live ordered checkpoints into a retained elapsed Time Trial result. BeamNG adds mission-authorised recovery, node-beam/pressure-tyre deformation, visible distributed damage and a Road Master-specific objective. Trackmania instead fixes an official seasonal map and classifies the valid result against published Author/Gold/Silver/Bronze thresholds without importing recovery, damage, traffic, rivals or campaign rewards. | Near, `0.600000` |

### Preserved research notes

- New genes: `SYS-711` and `OBJ-133`.
- Reused genes: `ACT-290`, `SYS-320`, `SYS-516`, `SYS-628`, `CON-438`,
  `INF-204`, `INF-205`, `INF-251` and `TIM-003`.
- Classification result: `New gene`, supported reuse and new verified
  interaction combination.
- Evidence and reasoning: direct assigned-car control, continuous motion,
  ordered route validity, live driving information and retained standalone
  time reuse lower-ID boundaries. A fixed four-threshold medal classification
  and the exact one-map positive terminal do not.

## Combination status

- `COMB-0214` is a verified strict subset of this genome. It couples direct car
  control, ordered waypoint validity and a retained elapsed result with fixed
  medal classification; generic speed/gear guidance stays outside the subset.
- All `213` earlier verified combinations are tested mechanically against this
  genome; none is assumed from brand or racing similarity.

## Taxonomy impact

- Registry changes: `SYS-711`, `OBJ-133`, `COMB-0214` and relevant existing
  family memberships; existing gene records gain Trackmania evidence only.
- Taxonomy-change record: none; no previous reviewed-game signature or gene
  lifecycle changes.
- Candidate terms affected: official map UID, waypoint, retained Time Trial,
  Author time and fixed medal threshold.

## Negative results

- `ACT-350`, `SYS-627` and `INF-250` are rejected: no mission-authorised
  recovery or decision-relevant soft-body/pressure-tyre deformation is admitted.
- `SYS-515` is rejected because no rival field is included; `INF-205` is reused
  only for its explicitly optional timed-target/course-progress boundary.
- `INF-208` is rejected: this packet has no Festival reward or campaign-point
  settlement.
- Ghosts, leaderboards and current world record are volatile comparison layers,
  not causal requirements for the first valid map result.
- Restart and respawn are not silently inferred from product familiarity. They
  remain non-completion/retry state outside the retained first-result packet.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Starter Access currently exposes official
  `Summer 2026 - 01` with stable map UID and four published medal times
  (`TM-001`–`TM-006`).
- [Confirmed | Direct | High] One ordered waypoint run becomes a retained time
  and fixed medal evaluation without requiring a leaderboard (`TM-005`–`TM-007`).

## Нові гени

- [Confirmed | Direct | High] `SYS-711` and `OBJ-133` isolate the fixed medal
  evaluator and this exact one-map terminal.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0214` captures the direct-car, ordered-route,
  retained-time and fixed-medal interaction.

## Зміни таксономії

- [Confirmed | Direct | High] Жодну сигнатуру раніше перевіреної гри не
  змінено; до перевикористаних генів додано лише доказову підтримку Trackmania.

## Нові питання

- Чи утворює окремий повторний заїзд із привидом нову петлю оптимізації, чи
  лише додає інформаційний шар до цього самого медального оцінювання?

## Наступна рекомендована задача

- [Confirmed | Direct | High] `SEARCH_DEMAND_BATCH_009_AUDIT`.
- Optimisation criterion: незалежно перевірити всі дев’ять ігрових units,
  локалізації, artwork, індекси, порівняння та фінальні totals.
- Expected information gain: відрізнити локальні помилки інтеграції від
  валідних міжжанрових відмінностей Batch 009.
- Backlog impact: завершити активний пакет без push, corpus publication,
  revision/tag або deploy.

## Чому саме вона

- [Confirmed | Direct | High] `GAME-0216` є останньою записаною грою Batch 009;
  наступний дозволений unit — лише незалежний batch audit.
