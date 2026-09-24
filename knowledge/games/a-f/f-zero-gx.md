---
game_id: GAME-0384
slug: f-zero-gx
game_title: F-Zero GX
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-292
    - ACT-293
    - ACT-309
    - ACT-525
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-691
    - SYS-1040
  constraint:
    - CON-438
    - CON-689
  information:
    - INF-205
    - INF-208
    - INF-390
  objective:
    - OBJ-226
  time:
    - TIM-003
---

# Game: F-Zero GX

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Pilot, machine,
course, speed setting and numerical energy values are parameters, not genes.

## Analysis scope

- Version / ruleset: original English-language European GameCube disc, as
  described by Nintendo's contemporary instruction booklet and publisher
  page. This is a source-bounded reconstruction, not a measured disc run.
- Structured analysis target: original PAL GameCube Grand Prix, Novice Ruby
  Cup's opening Mute City: Twist Road race; see `GAME-0384` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup: select Novice, Ruby Cup and the available Blue Falcon; leave the
  acceleration/maximum-speed slider at its centre. These selections commit
  the race contract before direct control. No custom machine or unlock is
  assumed. The first race is one of five in the Cup, not a whole-Cup win.
- Primary decision loop: read place, lap, rival proximity, speed and the
  shared energy meter; steer, accelerate, brake and lean/slide through turns
  while the 29 rival machines continue racing. On the second and third laps,
  decide whether a manual burst is worth spending energy that also absorbs
  collision damage. Route through a pit strip to restore it or over a dash
  plate for speed; choose whether a side or spin attack is worth the contact
  risk. Complete the ordered three laps ahead of the field and read the
  classified place and carried Cup points.
- Entry: immediately before the first start signal on Twist Road after the
  stated settings are accepted. The first controllable frame begins the race.
- Positive terminal: on this race's first attempt, cross the valid finish
  after lap three in first place and reach its classified result/points
  surface. Those points continue into the unfinished Ruby Cup; no five-race
  trophy is asserted. The packet stops before course two begins.
- Negative terminal: a lower classified place fails the local first-place
  target; falling off the course or suffering damage with an already empty
  energy meter retires the machine. A retry consumes a Novice spare machine
  and constitutes another attempt, outside this first-attempt packet.
- Included: Novice difficulty and fixed machine setting; 30-machine field;
  direct hovercraft control, shoulder lean/slide and contact; optional side
  and spin attacks; first-lap boost gate; later energy-priced manual bursts;
  pit recharge, dash plates and course-edge danger; rank/lap/time/radar and
  energy displays; ordered three-lap validation and one-race points.
- Excluded: Ruby Cup courses two through five, cumulative Cup victory, Story
  Mode, Time Attack, VS, garage/custom machine economy, AX transfer, extra
  unlocks, difficulty classes beyond Novice, changing settings mid-race,
  deliberate retire/retry and later spare-machine economy. The booklet's
  ordinary five-spare Novice retry entitlement remains an adjacent rule,
  not a success path for the first attempt.
- Reproducible parameterisation: original English PAL disc, single player,
  Novice, Ruby Cup, Blue Falcon, centre machine setting, Twist Road, 29 CPU
  rivals and one start-to-result attempt. Record disc identity, initial grid,
  controller inputs, meter trace, rank/lap/time, contacts, pit crossings and
  final points for a future direct replication. No exact energy cost,
  opponent line or achieved race time is asserted here.
- Potential scoped modules: complete five-race Ruby Cup, higher difficulty,
  attack-oriented rival elimination with earned spare machines, Time Attack,
  Story mission, garage tuning or AX connectivity each requires a separate
  bounded packet.
- Direct-play status: none. Nintendo's original booklet and product page and
  SEGA's archived official course description were read as text. No disc,
  executable, save, controller trace, screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FZG-001` | Original GameCube F-Zero GX offers Novice Grand Prix and a Ruby Cup whose first Mute City course is Twist Road | Confirmed | Direct | High | P1, P2, P3 |
| `FZG-002` | A Grand Prix course has three laps, classified finish and place-dependent points, while Cup victory requires all five courses | Confirmed | Direct | High | P1 |
| `FZG-003` | Direct steering, throttle, brake, shoulder turning and side/spin attacks coexist against 29 rival machines | Confirmed | Direct | High | P1, P2 |
| `FZG-004` | Manual boosting is forbidden in lap one; after that it spends the same energy meter that damage lowers | Confirmed | Direct | High | P1, P2 |
| `FZG-005` | Pit time restores energy, a dash plate provides a short speed gain, and an off-course fall or damage after meter depletion retires the pilot | Confirmed | Direct | High | P1 |
| `FZG-006` | The live display exposes energy, position/lap, time, speed, radar and rival cues; the result reports classified finish | Confirmed | Direct | High | P1 |
| `FZG-007` | Novice begins with five spare machines, but a retire/retry is a new attempt outside this packet | Confirmed | Direct | High | P1 |
| `FZG-008` | The official Twist Road description identifies a broad course with a later 180-degree twisted segment and guardrail risk | Confirmed | Direct | High | P3 |
| `FZG-009` | No direct execution or numeric energy/handling trace was available | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Amusement Vision / SEGA developed F-Zero GX; Nintendo's
  UK product record identifies the GameCube European release as 2003-10-31.
- Platform or physical form: original English PAL GameCube disc, offline
  single-player Novice Grand Prix, first Ruby Cup race only.
- Puzzle family: `FAM-007` physics and object manipulation for momentum,
  grip and collision-dependent route choice; `FAM-010` real-time system
  pressure because the rank and shared survival/boost energy change while
  the rival field advances.
- Primary sources, checked 2026-09-24:
  - **[P1]** [Nintendo's original F-Zero GX instruction booklet,
    text-accessible reproduction](https://manualzz.com/doc/22999165/nintendo-gx-f-zero-gx-instruction-booklet),
    pp. 6–21, for controls, selectable Grand Prix parameters, official
    three-lap/five-course rules, retirement, first-lap prohibition, energy,
    pit, dash and HUD. The authored booklet is a primary artifact on a
    third-party host; no game asset was copied.
  - **[P2]** [Nintendo UK GameCube product page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/F-Zero-GX-267972.html),
    for platform/date, field size, direct controls and the shared boost/energy
    risk. The page's simplified zero-meter wording is resolved using P1's
    more precise damage-after-empty retirement rule.
  - **[P3]** [archived official SEGA F-Zero GX Mute City course
    page](https://backup.segakore.fr/f-zero.jp/f-zero_gx/planet_course/mutecity.html),
    for Twist Road's Ruby Cup position, broad road, later 180-degree twist
    and guardrail warning. Japanese course text was checked against its
    visible labels; no exact driving line is inferred.
- Research record **[R1]**: no original disc or direct play available.
- Claim IDs: `FZG-001`–`FZG-009`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-290` for one dedicated hover vehicle's direct steering,
  acceleration and braking; `ACT-292` for the Novice opponent profile;
  `ACT-293` for Ruby Cup event commitment; `ACT-309` for deliberately
  spending the bounded acceleration reserve after it becomes legal.
- New `ACT-525` distinguishes direct side/spin attack commands against nearby
  rival machines from mere steering contact or a carried item.
- Centre speed/acceleration tuning is a fixed setup parameter, not a new
  in-race build gene. Claims: `FZG-001`, `FZG-003`, `FZG-004`.

### System Behaviour Genes

- Reuse `SYS-320` for live machine motion, grip and collision; `SYS-515`
  for the Novice CPU field; `SYS-516` for ordered laps and race result;
  `SYS-691` for a requested burst that spends a bounded acceleration reserve.
- New `SYS-1040` makes energy one shared damage/boost reserve: contact lowers
  it, legal boost spends it, pit time replenishes it, and damage after it has
  emptied retires the machine. A rival attack's contact is resolved through
  vehicle collision, not as a random inventory item. We do not assert a
  precise damage or replenishment coefficient.
- Resolution: setup locks machine/Cup; start releases all vehicles; inputs
  and rivals update live; steering and attack contact alter position and
  energy; lap-one boost requests are rejected; later requests accelerate and
  debit energy; pit restores it; valid lap three classifies the finish and
  credits points. Claims: `FZG-002`–`FZG-006`.

### Constraint Genes

- Reuse `CON-438` for three valid ordered laps before finish acceptance.
- New `CON-689`: player-requested boost cannot fire on the first lap,
  regardless of energy; it becomes eligible after crossing lap one.
- Scarce resources: shared energy, race distance/time, rank opportunity and
  the first attempt. The five Novice spare machines are outside this attempt.
  Claims: `FZG-002`, `FZG-004`, `FZG-005`, `FZG-007`.

### Information Genes

- Reuse `INF-205` for place/lap/time/rival proximity and `INF-208` for the
  classified result and carried points. `INF-204` is rejected because its
  definition requires a gear display, which the booklet does not establish.
- New `INF-390`: a visible energy meter reports the shared survival/boost
  state and changes colour when the first-lap boost gate opens.
- Claims: `FZG-004`, `FZG-006`.

### Objective Genes

- New `OBJ-226` accepts first place in the first three-lap Cup race and
  carries that race's points into a still-unfinished championship.
- `OBJ-134` is not silently reused: it requires a completed rival-race event
  with its retained reward, whereas this is one course of an unfinished
  five-course Cup. The full-Cup `OBJ-180` is likewise excluded.
- Success/failure: first-place valid finish and result are positive; lower
  rank or retirement is not. Claims: `FZG-002`, `FZG-005`.

### Time Genes

- Reuse `TIM-003`: rival movement, collisions, lap time and energy risk
  progress while driving decisions are made. There is no turn pause.
- Claims: `FZG-003`–`FZG-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution or bounded branch | What it establishes | Claim ID |
|---|---|---|---|---|
| Novice Ruby Cup and Blue Falcon selected | Accept centred settings | The first Twist Road start grid releases the 30-machine field; no other course is selected mid-race | event and field | `FZG-001`, `FZG-003` |
| First lap, full energy | Press manual boost | No player booster effect; lap-one prohibition applies even with charge | boost legality is lap-gated | `FZG-004` |
| Second lap, energy available | Press manual boost | A short acceleration burst debits the shared meter; subsequent contact has less damage buffer | speed versus survival | `FZG-004` |
| Meter partly depleted | Cross a pit area | Meter replenishes in proportion to time inside the area; opponent race time continues | route for recovery has time cost | `FZG-005` |
| Nearby rival within attack reach | Request side/spin attack | Attack contact can displace or retire the rival; own machine remains exposed to collision risk | active rivalry is not an item roll | `FZG-003`, `FZG-005` |
| Meter empty | Suffer further damage | Machine explodes and retires; empty alone is not claimed as immediate retirement | precise failure boundary | `FZG-005` |
| Valid lap three and first place | Cross finish | Classified first-place result and race points appear; Cup is not yet won | local success versus championship | `FZG-002`, `FZG-006` |

## Strategic and experiential structure

- Local decision: choose steering line, shoulder correction, burst, pit
  crossing or attack based on nearby rivals and remaining energy.
- Medium-term planning: protect enough energy for twisted turns and final-lap
  overtaking rather than spending every legal burst immediately.
- Long-term structure: a first-race result contributes to a five-course Cup;
  this packet intentionally stops before the other four courses.
- Common heuristic: preserve a recoverable line and use visible pit sections
  when extra energy outweighs their time cost.
- Failure attribution: lap/energy HUD distinguishes prohibited boost, low
  energy, wrong line, course fall and an insufficient first-place finish.
- Player-trust limit: exact handling, rivals, energy coefficients and finish
  times require a disc/controller trace not available here.
- Claim IDs: `FZG-002`–`FZG-009`.

## Replay and variation

- Grid, rival trajectories, contacts and chosen settings may change between
  attempts, but the packet fixes the first race, machine and Novice profile.
- No item draw or procedural track is admitted. Rival AI variability is not
  quantified by the booklet.
- A conservative pit-supported line, high-risk boost timing and close-range
  attacking are distinct viable tactical approaches to the same finish.
- Retry after retirement begins another attempt and spends a spare machine;
  it does not retroactively complete the failed first attempt.
- Claim IDs: `FZG-003`–`FZG-008`.

## Adjacent systems and history

- *Mario Kart 8 Deluxe* shares direct vehicle control, autonomous racing,
  ordered laps and a live place display, but its items, coins, drift-charge
  boost and whole-Cup terminal are not the shared energy/first-race contract.
- *Need for Speed Underground* likewise shares racing structure yet its
  first Circuit has an independent retained event reward and no shared
  damage/boost energy or first-lap boost prohibition.
- *Burnout Paradise* has chargeable Boost in an open-city event; its
  uncheckpointed route and separate crash model are not imported here.
- Claim IDs: `FZG-002`–`FZG-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-290, ACT-292, ACT-293, ACT-309, ACT-525 | fixed Blue Falcon, centre machine setting, attack direction |
| System Behaviour | SYS-320, SYS-515, SYS-516, SYS-691, SYS-1040 | grip, rivals, energy amount, pit interval |
| Constraint | CON-438, CON-689 | three laps and lap-one gate |
| Information | INF-205, INF-208, INF-390 | place, lap, time, meter and points |
| Objective | OBJ-226 | first race first place, not Cup trophy |
| Time | TIM-003 | live field and race clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `383` (`GAME-0001`–`GAME-0383`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`10 / 21 = 0.476190`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` Need for Speed Underground | Direct vehicle control, opponent-profile and race commitment, live vehicle motion and autonomous rivals, ordered-lap validation, lap constraint, race-place and result displays, and real-time decisions | F-Zero GX adds direct machine attacks and one shared boost/survival energy reserve with a first-lap gate; its first result only carries points into a still-unfinished Cup, whereas Underground finishes a standalone career race with a retained Bank reward | `10 / 21 = 0.476190`; tied near maximum, not an exact event or resource match |

### Preserved research notes

- New genes: `ACT-525`, `SYS-1040`, `CON-689`, `INF-390`, `OBJ-226`.
- Reused genes: `ACT-290`, `ACT-292`, `ACT-293`, `ACT-309`, `SYS-320`,
  `SYS-515`, `SYS-516`, `SYS-691`, `CON-438`, `INF-205`, `INF-208`, `TIM-003`.
- Classification result: new source-bounded energy and staged-Cup genes.

## Taxonomy impact

- Registry changes: five additive Active genes.
- Taxonomy-change record: `TAXONOMY_CHANGE_123`.
- Candidate terms affected: shared boost/damage energy versus independent
  nitrous; first Cup race result versus complete Cup trophy.

## Negative results

- Do not infer a whole-Cup victory from a first-place opening result.
- Do not use `INF-204`: no required gear readout is evidenced here.
- Do not turn exact energy loss, recovery, handling or attack probability
  into a measured claim without direct play.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original booklet specifies three laps per
  race, five races per Cup, a first-lap boost ban, shared energy and
  damage-after-empty retirement (`FZG-002`, `FZG-004`, `FZG-005`).

## New genes

- [Observation | Corroborated | High] `ACT-525`, `SYS-1040`, `CON-689`,
  `INF-390` and `OBJ-226` isolate command, resource, legality, display and
  terminal boundaries of the first race.

## New combinations

- [Observation | Direct | High] No new verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_123` adds five genes
  without changing earlier signatures.

## New questions

- What exact meter debit and collision coefficients apply on the original
  PAL disc, and does a particular attack create a guaranteed energy return?
- Which Blue Falcon line through the twist minimises guardrail damage at the
  centred speed setting? These require direct play, not source extrapolation.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0385 Phoenix Wright: Ace Attorney.
- Optimisation criterion: alternate high-speed continuous spatial control
  with evidence-led courtroom contradiction reasoning.
- Expected information gain: court testimony, evidence selection and
  objection penalties against the current deduction signatures.
- Backlog impact: preserves the selected nine-game order; no next unit
  starts in this commit.

## Why this game

- [Hypothesis | Limited | Medium] Shared survival/boost energy and an
  unfinished Cup's first-race result give a mechanically distinct racing
  boundary, with a direct Nintendo booklet rather than genre inference.
