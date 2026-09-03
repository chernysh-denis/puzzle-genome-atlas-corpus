---
game_id: GAME-0163
slug: ea-sports-fc-26
game_title: EA SPORTS FC 26
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0161
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-267
    - ACT-268
    - ACT-269
  system:
    - SYS-457
    - SYS-458
    - SYS-459
    - SYS-460
    - SYS-461
    - SYS-462
    - SYS-463
  constraint:
    - CON-398
    - CON-399
    - CON-400
    - CON-401
  information:
    - INF-116
    - INF-178
  objective:
    - OBJ-090
  time:
    - TIM-003
---

# Game: EA SPORTS FC 26

## Analysis scope

- Version / ruleset: PC Title Update `v1.6.6`; offline Kick Off, Classic Match,
  one local human controlling the home side against a CPU away side, Authentic
  Gameplay preset, default assists and sliders, default three-minute halves,
  no extra time and no penalty shoot-out.
- Primary decision loop: read the live ball, team shape, score and clock;
  directly move or switch the controlled player; dribble, pass, cross, shoot or
  challenge; let ball physics, assistance, team AI, goalkeeping and the referee
  settle the phase; then reorganise for continuing play or the prescribed restart.
- Entry and exit: begins when the referee starts the first-half kick-off with
  both selected elevens in legal formation; ends at the second-half final
  whistle with the regulation score classified as a home win, away win or draw.
- Included: one spatial ball; two eleven-player sides; direct movement and
  dribbling; player switching; ground, through and lofted passes; crosses;
  shots; standing and sliding challenges; assisted target/contact resolution;
  off-ball support, runs, positioning and marking; possession changes; saves;
  ball in/out, offside, fouls, advantage, sanctions and set-piece restarts;
  valid goals, score, two halves, added time and regulation settlement.
- Excluded: Ultimate Team, Career, Clubs, Rush, World’s Game tournament,
  online play, local two-human play, training, roster construction, transfers,
  progression, economy, packs, cosmetics and esports; custom sliders or tactics;
  manual substitutions and injuries; extra time and penalty shoot-outs.
- Potential scoped modules: a local two-human Classic Match; Competitive
  Gameplay; manual tactical and substitution control; Rush; Clubs; Ultimate
  Team squad construction and economy; Career season progression.
- Direct-play status: not conducted. Current official EA rules, settings and
  gameplay notes establish the software boundary; IFAB 2025/26 laws establish
  the association-football rule predicates represented by the simulation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FC26-001` | Title Update v1.6.6 is the scoped current PC ruleset | Confirmed | Direct | High | P1, P2 |
| `FC26-002` | Kick Off supports one offline Classic Match and Authentic Gameplay is available for single-player play | Confirmed | Corroborated | High | P3, P4, S1 |
| `FC26-003` | One human directly controls and switches among one eleven-player side while team AI positions the remaining players and the CPU opponent | Confirmed | Corroborated | High | P3, P5 |
| `FC26-004` | Direction, power, assistance, pose and context resolve passes, crosses and shots into one live spatial ball | Confirmed | Corroborated | High | P3, P5 |
| `FC26-005` | Authentic Gameplay changes movement, positioning, defending, ball behaviour, fatigue and match tempo rather than creating a separate objective | Confirmed | Direct | High | P3 |
| `FC26-006` | Field boundaries, last touch, offside and illegal contact select stoppage, sanction and restart states | Confirmed | Corroborated | High | P5, P7–P11 |
| `FC26-007` | A whole-ball legal goal increments one side and restarts from the opponent's kick-off | Confirmed | Corroborated | High | P9, P10 |
| `FC26-008` | The scoped default fixture uses two three-minute halves and accepts a regulation draw | Confirmed | Corroborated | High | S1, P5 |
| `FC26-009` | The HUD and broadcast view expose the ball, control locus, score, clock, nearby team shape and restart context | Confirmed | Corroborated | High | P4, P5 |

## Basic data

- Release / origin: EA SPORTS; EA SPORTS FC 26 released in September 2025.
- Platform or physical form: real-time association-football simulation viewed
  from a broadcast-style camera and controlled by gamepad or keyboard.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; physics and object manipulation.
- Primary and reproducible sources:
  - **[P1]** [Title Update v1.6.6](https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc%E2%84%A2-26--title-update-v1-6-6/13614472),
    for the scoped current update boundary.
  - **[P2]** [EA SPORTS FC 26 news index](https://www.ea.com/games/ea-sports-fc/fc-26/news),
    for update ordering and current official notes.
  - **[P3]** [Gameplay Deep Dive](https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive),
    for Authentic and Competitive presets, movement, passing, shooting,
    defending, AI positioning, physicality and goalkeepers.
  - **[P4]** [FC 26 accessibility and settings](https://www.ea.com/able/resources/ea-sports-fc/fc-26),
    for pass assistance, defending help, switching and goalkeeper assistance.
  - **[P5]** [EA SPORTS FC 26](https://www.ea.com/games/ea-sports-fc/fc-26),
    for the released product and match presentation.
  - **[P6]** [FC 26 Showcase](https://www.ea.com/games/ea-sports-fc/fc-26/fc26-standard-showcase),
    for Kick Off and Learn To Play mode evidence.
  - **[P7]** [IFAB Laws 2025/26](https://downloads.theifab.com/downloads/laws-of-the-game-2025-26-single-pages),
    for the contemporary association-football laws boundary.
  - **[P8]** [ball in and out of play](https://www.theifab.com/laws/latest/the-ball-in-and-out-of-play/),
    for whole-ball boundary predicates.
  - **[P9]** [determining the outcome](https://www.theifab.com/laws/latest/determining-the-outcome-of-a-match/),
    for valid goals and score settlement.
  - **[P10]** [offside](https://www.theifab.com/laws/latest/offside/),
    for position, involvement and restart exceptions.
  - **[P11]** [fouls and misconduct](https://www.theifab.com/laws/latest/fouls-and-misconduct/),
    for challenge legality, sanctions and penalties.
- Secondary source:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/games/sports/ea-sports-fc-26-review/),
    for single-player Authentic Kick Off and the default six-minute match.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P11` and `S1`; rules reasoning, not a claim of direct play.
- Claim IDs: `FC26-001`–`FC26-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the controlled player;
  `ACT-052`, switch the unique direct-control locus to an eligible teammate.
- New genes: `ACT-267`, direct a teammate-targeted ball delivery; `ACT-268`,
  direct an attempt at goal; `ACT-269`, commit a possession challenge.
- Parameters: direction, pace, sprint, dribble input, switch target, delivery
  family, power, assistance, shot family, challenge family and timing.
- Claim IDs: `FC26-003`, `FC26-004`, `FC26-006`.

### System Behaviour Genes

- New genes: `SYS-457`, resolve the live football; `SYS-458`, combine assisted
  intent with context into contact; `SYS-459`, coordinate off-ball team AI;
  `SYS-460`, adjudicate offences and restart; `SYS-461`, resolve goalkeeping;
  `SYS-462`, register a valid goal; `SYS-463`, advance halves and settle result.
- Resolution order: running time advances player and ball state; direct input
  and team AI update positions; an eligible contact produces a trajectory;
  collision, save or boundary crossing resolves; the referee applies advantage,
  stoppage or restart; a legal goal changes the score; half or match expiry
  advances the phase or settles the result.
- Parameters: physics, assistance, formation, role, difficulty, referee strictness,
  last touch, restart point, goalkeeper attributes, clock and score.
- Claim IDs: `FC26-003`–`FC26-009`.

### Constraint Genes

- New genes: `CON-398`, one direct-control locus governs an eleven-player side;
  `CON-399`, field and goal geometry bound live play; `CON-400`, offside bounds
  eligible attacking involvement; `CON-401`, football law bounds challenges.
- Scarce strategic resources: field space, possession, open passing lanes,
  defender cover, goalkeeper position, score margin and remaining regulation time.
- Claim IDs: `FC26-003`, `FC26-006`–`FC26-008`.

### Information Genes

- Existing gene: `INF-116`, expose live team, score, clock and phase state.
- New gene: `INF-178`, expose the ball, pitch, current control marker and local
  team shape through the broadcast view.
- Parameters: camera, radar, player label, control marker, score, clock, card,
  advantage, offside and restart notice.
- Claim IDs: `FC26-009`.

### Objective Genes

- New gene: `OBJ-090`, finish regulation with more valid goals than the opponent.
- Success, evaluation and failure: ahead at full time is a win, behind is a loss
  and level is a valid draw; the scoped unit records any terminal outcome rather
  than requiring the human side to win.
- Claim IDs: `FC26-007`, `FC26-008`.

### Time Genes

- Existing gene: `TIM-003`, ball, players, referee and match clock continue in
  real time while the human reads and acts.
- Claim IDs: `FC26-003`–`FC26-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening elevens are in formation at `0–0` | Start first-half kick-off | The designated side plays the stationary ball and the match clock enters live play | Explicit entry, one ball and running phase | `FC26-002`, `FC26-008` |
| Human controls an on-ball midfielder | Aim and power a ground pass | Assistance and context choose an eligible receiver/contact; ball motion and both teams continue | Delivery is an input-mediated physical transition | `FC26-004` |
| Human no longer controls the best defender | Trigger player switch | The control marker moves to one eligible teammate; the former body remains under AI | Unique transferable direct-control locus | `FC26-003` |
| Attacker is beyond the second-last opponent when a teammate passes | Become actively involved | Referee stops play and awards the defending indirect restart | Offside is a causal eligibility rule | `FC26-006` |
| Defender challenges late inside the penalty area | Commit tackle | Contact is adjudicated; play stops for penalty and may add a sanction | Challenge is constrained by law and location | `FC26-006` |
| Shot travels toward goal | Goalkeeper intervenes | Keeper may catch, parry or deflect; otherwise the ball remains live or exits | Keeper is an autonomous participant, not a guaranteed wall | `FC26-004`, `FC26-005` |
| Whole legal ball crosses between posts and under bar | Complete crossing | Scoring side increments; opponent restarts from kick-off | Goal geometry causally updates score | `FC26-007` |
| Ball wholly crosses touchline after defender's touch | Complete crossing | Play stops and the opponent receives a throw-in at the exit point | Boundary and last touch determine restart | `FC26-006` |
| First half reaches its bounded end | Let clock expire | Referee ends the half and second-half phase follows | Two-phase regulation horizon | `FC26-008` |
| Second half plus added time expires | Let final phase settle | Final whistle freezes the score as win, loss or draw | Explicit reproducible exit | `FC26-008` |

## Strategic and experiential structure

- Local decision: protect or contest the ball; carry into space or release it;
  select a safe receiver, penetrative run, shot window or challenge moment.
- Medium-term planning: preserve team compactness, create numerical overloads,
  switch play away from pressure and change risk according to score and clock.
- Long-term structure: no persistent campaign layer is admitted; the bounded
  strategy is to convert possession and field position into a superior score
  before the final whistle while preventing the opponent from doing the same.
- Common heuristics: keep passing triangles; avoid pulling one controlled
  defender out of shape; delay when unsupported; shoot only from viable angles;
  accept a restart instead of conceding a central transition.
- Failure attribution: ball, player indicator, pitch markings, score, clock,
  referee notices and visible team shape explain most consequences; assisted
  target choice and animation contact introduce bounded implementation opacity.
- Player-trust factors: consistent switching, readable contact, predictable
  advantage/offside calls, faithful boundary detection and credible saves.
- Claim IDs: `FC26-003`–`FC26-009`.

## Replay and variation

- What changes between sessions: teams, formations, player attributes, weather,
  score path, possession chains, fouls, deflections and CPU tactical responses.
- Randomness or procedural generation: the stadium and laws are fixed; loose
  contacts, AI choices and animation/physics outcomes create bounded variation.
- Multiple viable strategies: possession, counterattack, crossing, central
  combinations, high pressure or compact defence can pursue the same score goal.
- Typical replay motive: different teams and matchups, difficulty, tactical
  approach, Authentic versus Competitive feel or improved execution.
- Claim IDs: `FC26-003`–`FC26-009`.

## Adjacent systems and history

- Direct predecessors: earlier FIFA and EA SPORTS FC games establish direct
  player control, assisted ball actions and broadcast match simulation.
- Variants: Competitive Gameplay prioritises online responsiveness; Rush changes
  field and team structure; Career and Ultimate Team add persistent selection,
  progression and economy.
- Similar games: Rocket League shares a single live ball, two opposing teams,
  spatial contact and goal scoring; Counter-Strike 2 shares a finite two-sided
  regulation score but resolves rounds, weapons and elimination instead.
- Important differences: FC 26 combines eleven-player role AI and transferable
  direct control with association-football offside, fouls, restarts and goalkeeping.
- Claim IDs: `FC26-002`–`FC26-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-052`, `ACT-267`–`ACT-269` | team, player, input assistance and action subtype are parameters |
| System Behaviour | `SYS-457`–`SYS-463` | attributes, formation, difficulty and exact physics are parameters |
| Constraint | `CON-398`–`CON-401` | field dimensions and referee strictness are parameters |
| Information | `INF-116`, `INF-178` | camera, indicator and HUD layout are parameters |
| Objective | `OBJ-090` | win/loss/draw result is the terminal value |
| Time | `TIM-003` | half length and clock rate are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `162` (`GAME-0001`–`GAME-0162`).
- Exact genome matches: none.
- Tied near matches: `GAME-0038` — The Swapper (`3 / 33 = 0.090909`).
- Supported combination subsets: `COMB-0161`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0038` — The Swapper | direct embodied navigation, transfer of one direct-control locus among persistent bodies and real-time input | FC 26 transfers control inside an eleven-player side whose remaining bodies use role AI, then resolves one shared ball, teammate deliveries, tackles, football offences, goalkeeping and a two-half score; The Swapper transfers consciousness among created bodies to solve authored traversal and gravity puzzles | Near, `0.090909` |

## Combination status

- `COMB-0161` is a verified strict subset coupling transferable control,
  teammate-targeted ball movement, off-ball team AI, football adjudication,
  valid goals and regulation score pressure.
- Earlier verified combinations will be tested deterministically after the
  complete genome is registered.

## Reuse and novelty decision

- Reused genes: `ACT-008`, `ACT-052`, `INF-116` and `TIM-003` retain their
  established parameterised boundaries.
- New genes: `ACT-267`–`ACT-269`, `SYS-457`–`SYS-463`, `CON-398`–`CON-401`,
  `INF-178` and `OBJ-090` isolate football-specific causal rules.
- Rejected near terms: `OBJ-002` maximises a score without requiring a relative
  opponent result; `CON-267` hard-codes Counter-Strike round halves and thirteen
  wins; combat genes use health and defeat rather than lawful ball possession.
- Registry changes: sixteen new stable genes and `COMB-0161`; existing
  multi-game family boundaries are reused.

## Taxonomy impact

- Registry changes: sixteen new stable genes, `COMB-0161`, evidence additions
  to four reused genes and memberships in `FAM-007`, `FAM-009`, `FAM-010` and
  `FAM-015`.
- Taxonomy-change record: none; no existing lifecycle, definition or earlier
  signature changes.
- Candidate terms affected: none.

## Negative results

- `OBJ-002` is not reused because raw accumulated score does not encode a
  two-sided regulation comparison or accepted draw.
- `CON-267` is not reused because its definition fixes Counter-Strike's
  twelve-round halves, thirteen-win clinch and twenty-four-round maximum.
- Health-based combat and projectile genes are not reused: football challenges
  transfer or interrupt possession under offence law, and the one ball persists.
