---
game_id: GAME-0217
slug: need-for-speed-underground
game_title: "Need for Speed Underground"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0215
gene_ids:
  action:
    - ACT-290
    - ACT-292
    - ACT-293
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-519
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-206
    - INF-208
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Need for Speed Underground

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: original unmodified English Windows retail release,
  official Electronic Arts patch `1.4.0`, Underground Mode, Easy opponent
  difficulty, automatic transmission and ordinary default controls. The game
  is legacy physical software and is not currently sold through the EA app.
- Platform and lawful artefact boundary: Windows PC from an owned original
  retail disc and product key, updated only with the official `1.4.0` patch.
  No disc image, executable, crack, compatibility wrapper, community patch or
  other unauthorised copy was downloaded, opened, run or used as evidence.
- Entry: a fresh Underground Mode profile has completed the fixed introduction
  and selected a stock Honda Civic Si as its starter. Open the first available
  event, Race 1 `Jose's Got Your Back`, select Easy and commit its Circuit at
  Olympic Square. The decision packet begins at the first accepted driving
  input after the two-lap start releases.
- Primary decision loop: read the road, route arrows, speed, gear, current
  place, lap, rival spacing and race time; steer, accelerate, brake or use the
  handbrake; let arcade traction, collision and three Easy rivals resolve;
  choose between the ordinary line and visible shortcuts; cross the route and
  both laps in order; revise the next braking point and line until the finish.
- Positive terminal: cross the valid finish after two complete laps in first
  place. The result settles as a win, awards `375` Bank on Easy and retains
  Race 1 completion in Underground Mode before control returns to the career
  event surface.
- Negative terminal: finishing below first does not satisfy the event's win
  objective; quitting or restarting ends the current attempt without the
  positive retained result. A later retry is another attempt and lies outside
  the accepted trace.
- Included: the fixed stock starter; one Easy two-lap Circuit; direct car
  control; road contact and collision; three autonomous rivals; route and
  shortcuts; ordered lap/finish validation; live speed, gear, place, lap and
  time; first-place evaluation; `375` Bank and retained Race 1 completion.
- Excluded: the introductory loan-car race; choosing or changing the starter;
  garage tuning, performance parts, visual customisation and reputation style
  points; every later Underground event; Sprint, Drag, Drift, Lap Knockout,
  tournaments and Time Trial; Quick Race, split-screen and the discontinued
  online mode; Underground 2, other platforms, cheats, community fixes,
  compatibility modifications and the full 112-event career.
- Reproducible parameterisation: owned original English Windows retail copy,
  official patch `1.4.0`, fresh Underground Mode after the introduction, stock
  Honda Civic Si, automatic transmission, Easy, Race 1 `Jose's Got Your Back`,
  Circuit, Olympic Square, two laps and three rivals. Stop after the first
  winning result has credited `375` Bank and returned to the career surface.
- Potential scoped modules: starter selection, one upgrade decision, one Drag
  race with manual shifting, one Drift score event, one tournament, a later
  catch-up-enabled race or the whole career each needs a separate entry and
  terminal.
- Direct-play status: not conducted. The exact original-client packet is
  reconstructed from Electronic Arts' official availability statements, the
  preserved official `1.4.0` patch record, the licensed Prima Official
  Strategy Guide and a contemporary written GameSpot walkthrough. No video or
  audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NFSUG-001` | The reviewed product is the original 2003 Windows Need for Speed Underground, not Underground 2 or a later remaster | Confirmed | Corroborated | High | P1, S1 |
| `NFSUG-002` | Electronic Arts no longer sells Underground through its current digital store; an owned original physical PC copy is the lawful reproduction artefact | Confirmed | Direct | High | P1, P2 |
| `NFSUG-003` | Electronic Arts issued patch `1.4.0` as the final recorded stability and online update for the original PC game | Confirmed | Corroborated | High | S2, S3 |
| `NFSUG-004` | Underground Mode turns event wins into Bank and retained career unlock/progress state | Confirmed | Corroborated | High | P3, S4 |
| `NFSUG-005` | Race 1 is `Jose's Got Your Back`, a two-lap Circuit at Olympic Square with Easy/Medium/Hard Bank rewards `375/500/625` | Observation | Corroborated | High | P3, S4 |
| `NFSUG-006` | The first event admits an already selected starter and places the player against three rivals on an ordered two-lap course | Observation | Corroborated | High | P3, S4 |
| `NFSUG-007` | Live speed, gear, place, lap, elapsed time, road shape and shortcut visibility support steering and braking choices | Observation | Corroborated | High | P3, S4 |
| `NFSUG-008` | A first-place valid finish settles the event win, credits the selected difficulty reward and retains Race 1 completion | Observation | Corroborated | High | P3, S4 |
| `NFSUG-009` | Drag, Drift, Sprint, later circuits, tuning, online play and the remaining career are separable from this first Circuit packet | Confirmed | Corroborated | High | P3, S4 |

## Basic data

- Release / origin: developed by EA Black Box and published by Electronic Arts
  in November 2003; the reviewed rules state is the original Windows retail
  game with official patch `1.4.0`.
- Platform or physical form: legacy Windows PC optical-disc software; only the
  declared single-player Underground Mode event is admitted.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and licensed sources:
  - **[P1]** [Electronic Arts forum availability answer](https://forums.ea.com/discussions/need-for-speed-franchise-discussion-en/where-would-i-download-need-for-speed-underground/9479444/),
    for the absence of Underground and Underground 2 from the current EA
    digital catalogue and the distinction between the original games.
  - **[P2]** [Electronic Arts staff follow-up](https://forums.ea.com/discussions/need-for-speed-franchise-discussion-en/re-need-for-speed-underground/9248528),
    for the publisher's statement that EA no longer sells the game and that
    physical single-player copies may still be obtained from retailers.
  - **[P3]** [Need for Speed Underground Prima Official Strategy Guide](https://www.scribd.com/doc/177212358/Need-for-Speed-Underground-Prima-Official-Game-Guide),
    produced with Electronic Arts access, for Underground Mode, controls,
    difficulties, race types, Olympic Square, progression, rewards and the
    complete event structure. The linked licensed preview was read as text;
    no unauthorised game asset was copied into the repository.
- Corroborating and preserved sources:
  - **[S1]** [MobyGames Windows release record](https://www.mobygames.com/game/11175/need-for-speed-underground/releases/),
    for original November 2003 Windows publication by Electronic Arts and EA
    Black Box attribution.
  - **[S2]** [preserved official EA patch record](https://www.nfs-cars.com/need-for-speed-underground/5/files/view/5110/),
    for patch author, version `1.4`, stability fixes and original-PC identity.
    The executable was not downloaded or run.
  - **[S3]** [contemporary patch announcement](https://www.nfsplanet.com/en/news/1639),
    for corroboration that `1.4.0` was the released update.
  - **[S4]** [GameSpot written walkthrough](https://www.gamespot.com/articles/need-for-speed-underground-walkthrough/1100-6085684/),
    for the event-one title, Circuit type, Olympic Square, two laps, three
    difficulty rewards, route advice and 112-challenge career context.
- Claim IDs: `NFSUG-001`–`NFSUG-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate, brake and handbrake the fixed
  stock Civic from grid release through the valid finish.
- Existing `ACT-292`: commit Easy opponent difficulty and automatic
  transmission before the event starts.
- Existing `ACT-293`: commit the available `Jose's Got Your Back` event with
  its Circuit route, two-lap rule and difficulty-linked reward.
- Parameters: starter, transmission, opponent difficulty, steering, throttle,
  brake, handbrake, route line and shortcut choice.
- Claim IDs: `NFSUG-004`–`NFSUG-007`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the dedicated car's arcade acceleration,
  steering, traction, road contact and collision without importing a fuel or
  persistent damage-management system.
- Existing `SYS-515`: continuously drive three autonomous course rivals under
  the selected Easy profile.
- Existing `SYS-516`: accept route progress through two ordered laps and settle
  the complete finish place only after a valid final crossing.
- Existing `SYS-519`: after a first-place result, retain Race 1 completion and
  transfer the declared `375` Bank reward to Underground Mode.
- Resolution order: lock event/profile/starter; release the grid; integrate
  car and rival motion; update road contact and collision; accept ordered lap
  progress; classify the finish; if first, credit Bank and retain completion;
  return control to the career event surface.
- Claim IDs: `NFSUG-004`–`NFSUG-008`.

### Constraint Genes

- Existing `CON-438`: the final finish is valid only after the controlled car
  completes both required laps through the authored course order.
- Scarce strategic resources: remaining course distance, speed carried into
  the next corner, current position and the finite opportunity to overtake
  before the final crossing. They are parameters, not inventory genes.
- Claim IDs: `NFSUG-005`–`NFSUG-008`.

### Information Genes

- Existing `INF-204`: the live driving view exposes speed, gear, visible road
  geometry and route arrows needed to judge braking and steering.
- Existing `INF-205`: the race interface exposes place, participant count,
  lap, elapsed time, course progress and nearby rivals.
- Existing `INF-206`: the pre-entry event surface exposes Race 1, Circuit,
  Olympic Square, two laps, difficulty choice and corresponding Bank reward.
- Existing `INF-208`: the post-finish transition exposes place, event success,
  credited Bank and retained career completion separately from the live HUD.
- Claim IDs: `NFSUG-004`–`NFSUG-008`.

### Objective Genes

- Revised `OBJ-134`: win one bounded rival race and retain its disclosed
  result/reward. In this packet the parameters are the opening `Jose's Got
  Your Back` Circuit, Easy, `375` Bank and Race 1 completion.
- Success, evaluation and failure: a first-place valid two-lap finish settles
  the positive terminal. Lower place, quit or restart does not. A shortcut is
  legal only insofar as the resulting course traversal still produces a valid
  finish.
- Claim IDs: `NFSUG-005`–`NFSUG-008`.

### Time Genes

- Existing `TIM-003`: the controlled car, three rivals, collision state and
  race clock advance continuously while steering and braking choices remain
  live.
- Claim IDs: `NFSUG-006`–`NFSUG-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Underground Mode has a stock Civic and exposes Race 1 | Open `Jose's Got Your Back`, choose Easy and commit | Olympic Square Circuit loads with two laps, three rivals and a `375` Bank win reward | exact event contract | `NFSUG-005`, `NFSUG-006` |
| Start releases all four cars | Apply throttle, steering, brake or handbrake | Arcade motion, road contact, collision and Easy rival paths advance continuously | live driving authority | `NFSUG-006`, `NFSUG-007` |
| A corner or visible shortcut approaches | Choose braking point and route line | The car preserves or loses speed and changes its next relation to rivals | local route consequence | `NFSUG-007` |
| First lap course order is complete | Cross the start/finish line | Lap display advances to the second lap; the event does not yet settle | ordered two-lap requirement | `NFSUG-005` |
| Second lap is valid and the player leads | Cross the final finish | First place is classified and the win transition begins | winning terminal predicate | `NFSUG-008` |
| Winning result is displayed on Easy | Accept the result transition | `375` Bank is credited, Race 1 completion persists and career control returns | explicit retained terminal | `NFSUG-005`, `NFSUG-008` |
| Final finish classifies below first place | Allow result resolution | The event objective remains incomplete; no accepted positive trace exists | lower place is not success | `NFSUG-008` |

## Strategic and experiential structure

- Local decision: brake before a corner or carry more speed, take the broad
  stable line or a shorter route, and time an overtake against nearby rivals.
- Medium-term planning: preserve exit speed for the following segment, avoid a
  collision that destroys overtaking position and decide when a shortcut's
  tighter entry is worth its distance gain.
- Long-term structure: one fixed first event converts repeated live line
  decisions into a binary career win, retained Bank and the next career state.
- Common heuristics: brake before turning rather than during the sharpest
  steering; use visible shortcuts only with a recoverable entry line; pass on
  corner exit when acceleration and road width are favourable.
- Failure attribution: place, lap, time, visible rivals, speed, road contact
  and final result distinguish an invalid course, slow line, collision and
  completed but non-winning finish.
- Player-trust factors: the event terms disclose type, lap count, difficulty
  and reward before entry; live place and lap explain progress; the result
  transition separates first-place success from lower-place completion.
- Claim IDs: `NFSUG-004`–`NFSUG-008`.

## Replay and variation

- What changes between attempts: driving line, shortcut use, contact, rival
  spacing, elapsed time and final place.
- Randomness or procedural generation: no procedural course or reward is
  admitted. Exact autonomous-rival trajectories may vary with live contact and
  pace, but the fixed route, lap count, difficulty and reward do not.
- Multiple viable strategies: ordinary road lines and visible shortcuts can
  both support a win when the player preserves enough speed and course order.
- Typical replay motive: recover from a lower-place finish or improve time.
  The canonical packet stops after the first retained win.

## Adjacent systems and history

- Direct successor: Underground 2 expands free-roam navigation, events,
  tuning and progression; none is imported into this original game's Race 1.
- Similar games: Need for Speed Unbound shares event commitment, three-level
  driving difficulty, rivals, ordered route validation and retained rewards;
  Forza Horizon 6 shares the same broad race foundation. Trackmania shares
  direct car control and ordered finishing but has no autonomous rival field
  or Bank settlement in its scoped map.
- Important differences: this unit ends at an ordinary first-place Circuit
  win and `375` Bank. It has no Burst Nitrous, police Heat, exposed cash,
  garage-gated escape, carrier combat, fixed medal threshold or open-world
  Festival progression.
- Claim IDs: `NFSUG-001`, `NFSUG-004`–`NFSUG-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-292`, `ACT-293` | direct stock-car control, Easy/automatic profile and first-event commitment |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519` | arcade car motion, three rivals, two-lap result and retained Bank/completion |
| Constraint | `CON-438` | both ordered laps before a valid final finish |
| Information | `INF-204`, `INF-205`, `INF-206`, `INF-208` | driving cues, race state, disclosed event terms and retained result |
| Objective | `OBJ-134` | win and retain the opening Circuit event |
| Time | `TIM-003` | continuous car, rival and race-clock progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `216` (`GAME-0001`–`GAME-0216`).
- Exact genome matches: none.
- Tied near matches: `GAME-0199` — Need for Speed Unbound (`13 / 25 = 0.520000`).
- Supported combination subsets: `COMB-0215`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0199` — Need for Speed Unbound | `ACT-290`, `ACT-292`, `ACT-293`, `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Both packets commit an automatic, difficulty-scaled street race, directly control one fixed car against autonomous rivals, validate ordered progress and retain a disclosed result. Underground ends immediately when first place in the opening two-lap Circuit credits `375` Bank and Race 1 completion. Unbound admits any classified place, technique-earned Burst, traffic, Heat, exposed cash and a mandatory police search/garage gate before its result persists. | Near, `0.520000` |

### Preserved research notes

- Reused genes: `ACT-290`, `ACT-292`, `ACT-293`, `SYS-320`, `SYS-515`,
  `SYS-516`, `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-206`,
  `INF-208` and `TIM-003`.
- Classification result: `New gene`, supported reuse and a new verified
  interaction combination.
- Evidence and reasoning: this packet reuses the established competitive
  driving vocabulary without importing newer-series resources or pursuit
  systems. Its exact one-event positive terminal is new.

## Combination status

- `COMB-0215` is a verified strict subset of this genome. It couples direct
  car control, first-event commitment, rival competition, two-lap validation,
  first-place settlement, Bank and retained career completion. Difficulty/
  transmission setup and generic speed/gear guidance stay outside the subset.
- All `214` earlier verified combinations are tested mechanically against this
  genome; none is assumed from franchise or racing similarity.

## Taxonomy impact

- Registry changes: `OBJ-134`, `COMB-0215` and relevant existing family
  memberships; reused gene records gain Need for Speed Underground evidence.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_017`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_017.md)
  generalises `OBJ-134` after a full racing-objective transfer scan. No game
  signature, combination set or lifecycle changes.
- Candidate terms affected: `Jose's Got Your Back`, Olympic Square, first
  Underground Circuit, Easy Bank reward and lawful legacy artefact boundary.

## Negative results

- Starter selection, tuning, style scoring and unlocking later cars/parts are
  excluded before or after the bounded event; no garage-action or progression
  gene is inferred from the wider career.
- Nitrous, traffic, police, catch-up, drag shifting and drift scoring are not
  evidenced as causally necessary in Race 1 and are rejected from its genome.
- Lower-place finish is an evidence-backed non-success state, not silently
  promoted to positive completion.
- No community patch, compatibility fix, crack, unauthorised download, sequel
  rule or discontinued online behaviour is used to fill an evidence gap.
