---
game_id: GAME-0378
slug: super-monkey-ball-2
game_title: Super Monkey Ball 2
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-519
  system:
    - SYS-037
    - SYS-1028
    - SYS-1029
  constraint:
    - CON-068
    - CON-685
  information:
    - INF-385
  objective:
    - OBJ-220
  time:
    - TIM-003
---

# Game: Super Monkey Ball 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Stage geometry,
banana count, ball speed and the displayed time allowance are parameters,
not separate genes.

## Analysis scope

- Version / ruleset: original English-language GameCube edition, one-player
  Story Mode, the first Jungle Island stage *Simple* (World 1-1) from a new
  save. The preserved English instruction booklet is the normative mechanical
  source; the publisher-supplied [Nintendo GameCube product
  page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Super-Monkey-Ball-2-268929.html)
  corroborates tilt, inertia, platform edges, goal and unlimited Story retries.
  The *Simple* stage name and number are independently reported by a
  contemporary stage guide, not asserted by the booklet itself.
- Structured analysis target: original English-language Nintendo GameCube
  disc's one-player Story Mode, not *Super Monkey Ball Deluxe*, *Banana Mania*
  or later physics reimplementations.
- Primary decision loop: push the Control Stick to tilt the playfield rather
  than teleporting or directly commanding the sphere; gravity, retained
  motion and platform collision roll the monkey-containing ball over the
  authored surface. Steer toward the goal while optionally collecting
  reachable bananas and watching remaining time and speed. Entering the
  goal before expiry clears the stage; leaving the platform or running out of
  time ends that attempt.
- Entry and exit: start a blank Story Mode save, select Jungle Island's first
  stage, and begin one attempt with the ball on its starting platform. The
  positive terminal is goal entry while time remains; the negative terminal
  is falling from the course or timer expiry. Story Mode permits a new try
  afterward, but that subsequent attempt is not concatenated into this
  genome. A reproduction must preserve the actual disc, stage, controller
  calibration, input sequence, ball position/speed and timer.
- Included: continuous playfield tilt, gravitational/inertial ball motion,
  support-edge failure, visible stage and clock/speed/score feedback,
  optional contact bananas and their credit, time-sensitive clear score,
  goal entry and the live deadline. No banana pickup is required for the goal.
- Excluded: the other nine Jungle Island stages, later worlds and moving
  obstacle arrangements, Challenge Mode's finite lives and 100-banana extra
  monkey, Practice Mode, 12 party games, character differences, unlockable
  Play Points, stage selection as a strategy layer, remake-specific controls
  and physical controller calibration as an in-game action.
- Potential scoped modules: World progression, Challenge Mode's life economy,
  and each party game need separate reviewed packets if later analysed.
- Direct-play status: none. The original manual and publisher copy were read;
  no GameCube disc, emulator, controller trace, video or audio was inspected.
  The exact *Simple* geometry, banana placement and timer must be checked by
  direct play before claiming a measured route or optimal movement.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SMB2-001 | The GameCube Control Stick tilts the playfield, causing the ball to roll; reaching the goal is the stage task. | Confirmed | Direct | High | P1 pp. 5, 9; P2 |
| SMB2-002 | Leaving the field ends the current try, while the live timer must stay above zero for a clear. | Confirmed | Direct | High | P1 p. 9; P2 |
| SMB2-003 | Bananas are optional contact pickups that add score; quicker goal completion also increases score. | Confirmed | Direct | High | P1 p. 9; S1 for presence in *Simple* |
| SMB2-004 | Story Mode offers unlimited retries, whereas Challenge Mode has finite monkeys; only the former is in scope. | Confirmed | Direct | High | P1 pp. 13–14; P2 |
| SMB2-005 | *Simple* is the first Jungle Island Story Mode stage, with a traversable route, bananas and goal. | Observation | Limited | Medium | S1, S2; no disc check |
| SMB2-006 | On a sloping or narrowing platform, tilt can accelerate the sphere while inertia makes braking and edge avoidance decision-relevant. | Confirmed | Corroborated | High | P1 p. 9; P2 |

## Basic data

- Release / origin: Amusement Vision / SEGA's original GameCube *Super Monkey
  Ball 2*; the Nintendo UK product page identifies the regional release as
  2003. This packet does not transfer its mechanics to remakes.
- Platform or physical form: original GameCube disc, one-player Story Mode;
  `PLAT-NINTENDO-GAMECUBE`.
- Puzzle family: indirect physics navigation under a live deadline, with
  optional pickups rather than a required collection quota.
- **[P1]** [Original SEGA GameCube instruction booklet,
  mirrored](https://manualzz.com/doc/54732408/sega-super-monkey-ball-2-user-manual),
  pp. 5, 9 and 13–14, checked 2026-09-23. This is the publisher-authored
  primary artifact on a third-party host, not an Atlas-owned manual.
- **[P2]** [Nintendo UK's GameCube product
  page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Super-Monkey-Ball-2-268929.html),
  with publisher-supplied description, checked 2026-09-23.
- **[S1]** [Contemporary stage guide by
  Sixstring983](https://gamefaqs.gamespot.com/gamecube/561200-super-monkey-ball-2/faqs/43324),
  first-world stage listing and optional bananas, checked 2026-09-23.
- **[S2]** [Contemporary stage guide by
  Notae](https://gamefaqs.gamespot.com/gamecube/561200-super-monkey-ball-2/faqs/38305),
  *Simple* route, bananas and goal, checked 2026-09-23. The secondary guides
  choose the packet, not the rules asserted by the primary artifact.

## Mechanical decomposition

### Action Genes

- `ACT-519`: tilt the whole playfield continuously with the Control Stick to
  affect the ball's rolling direction and braking. This is not direct avatar
  locomotion or choosing a gravity-down surface in discrete steps.
- Parameters: stick angle and duration, camera view and controller neutral
  position.
- Claim IDs: SMB2-001, SMB2-006.

### System Behaviour Genes

- `SYS-1028`: resolve the ball's gravity-driven motion, retained momentum,
  friction and course contact under the changing field angle.
- `SYS-037`: touching an optional banana removes it and credits score without
  ending the stage.
- `SYS-1029`: a successful goal settlement credits remaining-time speed in
  addition to banana score; exact formula remains unclaimed without a run.
- Resolution order: applied tilt changes field orientation; the ball rolls
  and collides; any contacted banana is credited; goal entry or off-field
  departure can end the attempt. Timer expiry is an independent negative gate.
- Parameters: ball speed, slope, surface, banana value, remaining time and
  score formula.
- Claim IDs: SMB2-001, SMB2-002, SMB2-003, SMB2-006.

### Constraint Genes

- `CON-685`: crossing off an unsupported platform edge ends this attempt;
  a safe platform contact does not.
- `CON-068`: a fixed stage clock ends an uncleared attempt at zero.
- Scarce strategic resources: remaining seconds and safe traversable floor;
  bananas are optional score opportunities, not consumable control resources.
- Claim IDs: SMB2-002, SMB2-006.

### Information Genes

- `INF-385`: the main-game screen exposes current stage, timer, speed, score,
  banana tally, ball and visible local course/goal; it does not reveal a
  solved route or guarantee safety beyond the camera.
- Claim IDs: SMB2-001, SMB2-003.

### Objective Genes

- `OBJ-220`: roll the avatar-containing ball into the fixed stage goal before
  the current attempt expires. Bananas and a high score are optional.
- Success, evaluation and failure: entering the goal within time clears and
  scores the attempt; leaving the field or timer expiry fails it. Story Mode
  permits retry but does not retroactively clear the failed attempt.
- Claim IDs: SMB2-001–SMB2-004.

### Time Genes

- `TIM-003`: tilt, motion, collision and countdown update in live time; the
  player does not receive a turn-by-turn planning pause.
- Claim IDs: SMB2-001, SMB2-002.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ball rests on supported floor, time remains | Tilt the playfield toward the route | Gravity accelerates the ball along the inclined surface; returning the stick toward neutral does not instantaneously erase its speed | Control changes the field; motion has inertia | SMB2-001, SMB2-006 |
| Ball passes over an optional banana on a supported surface | Maintain a legal tilt through contact | Banana disappears and score/banana tally increases while the attempt continues | Pickup is not the goal gate | SMB2-003 |
| Ball is near a platform edge, time remains | Continue a tilt that carries it beyond support | Ball leaves the field and the current attempt fails; later Story retry begins another attempt | Off-field failure is terminal locally, not a loss of Story lives | SMB2-002, SMB2-004 |
| Ball is supported, remaining time reaches zero | Do not enter the goal before expiry | Current attempt fails despite survival on the surface | Deadline and edge failure are distinct | SMB2-002 |
| Ball is supported and time remains | Tilt along the traversable route into the goal | Stage clears; goal speed contributes to the resulting score, whether or not every banana was collected | Goal contact is sufficient and optional score is separate | SMB2-001, SMB2-003 |

These are rule transitions inferred from the publisher material, **not**
measurements of *Simple*'s coordinates, accelerations or remaining-time
values. A failed navigation attempt could be repeated in Story Mode, but that
is the next packet instance, not a continuing life stock here.

## Strategic and experiential structure

- Local decision: trade acceleration against braking room as the field tilts
  under a rolling body rather than issuing a destination command.
- Medium-term planning: inspect the visible course, choose a safe line across
  narrow surface, and decide whether a banana detour is worth time and edge
  risk.
- Long-term structure: one successful first-stage clear contributes to later
  world progression; the world unlock is outside this bounded attempt.
- Common heuristics: begin with a shallow tilt on a narrow route, counter-tilt
  before an edge, and ignore optional pickups when they threaten the clear.
- Failure attribution: falling and countdown expiry are visible; without an
  input trace, exact loss of traction or stage-specific geometry cannot be
  assigned confidently to one frame.
- Player-trust factors: Story Mode permits retries without Challenge Mode's
  finite-life depletion, but the local failure remains explicit.
- Claim IDs: SMB2-001–SMB2-006.

## Replay and variation

- What changes between sessions: steering path, timer at entry, optional
  pickups and achieved score; the selected stage layout is authored rather
  than procedurally regenerated.
- Randomness or procedural generation: none is claimed within this packet.
- Multiple viable strategies: a safe direct goal line or a slower banana
  detour can both clear if the ball remains supported and time remains.
- Typical replay motive: improve control, survival, bananas or completion
  time. The numeric score formula is not inferred from memory.
- Claim IDs: SMB2-001–SMB2-006.

## Adjacent systems and history

- Direct predecessors: the original *Super Monkey Ball*'s field-tilt main
  game, outside this corpus comparison because it lacks a reviewed record.
- Variants: *Super Monkey Ball Deluxe* and *Banana Mania* are later products;
  their physics, stage inventories and controls are not evidence for this
  GameCube packet.
- Similar games: Golf Peaks and Katamari Damacy REROLL share physical-ball
  language but differ in input commitment, attachment and objective. The
  canonical tied-near results below come from all lower-ID signatures.
- Important differences: the avatar is enclosed in the ball, the player
  tilts a stage continuously, and a single gate ends a live attempt; this is
  not a discrete card stroke or accumulating body size.
- Claim IDs: SMB2-001–SMB2-006.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-519` | Continuous field angle and duration |
| System Behaviour | `SYS-037`, `SYS-1028`, `SYS-1029` | Optional pickups, rolling physics, time score |
| Constraint | `CON-068`, `CON-685` | Deadline and off-field failure |
| Information | `INF-385` | Stage, time, speed, score, bananas and local view |
| Objective | `OBJ-220` | One fixed goal gate |
| Time | `TIM-003` | Live clock and continuous response |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `377` (`GAME-0001`–`GAME-0377`).
- Exact genome matches: none.
- Tied near matches: `GAME-0376` — Katamari Damacy REROLL (`2 / 15 = 0.133333`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0376` Katamari Damacy REROLL | `CON-068`, `TIM-003` | Both attempts run live against a terminal deadline. Katamari directly rolls a growing object and must meet a size threshold at settlement; Super Monkey Ball 2 tilts the stage under a fixed-size avatar ball and must enter a fixed goal without leaving the support surface. Their shared clock does not imply the same control, pickup or completion rule. | Tied near, `0.133333` |

- New genes: `ACT-519`, `SYS-1028`, `SYS-1029`, `CON-685`, `INF-385`,
  `OBJ-220`.
- Classification result: `New gene`.
- Evidence and reasoning: the exact GameCube main-game manual directly
  distinguishes field tilt, a physically rolling body, off-course attempt
  failure, a live goal deadline and time-sensitive score. Existing
  locomotion, shot-ball and platform-life genes have different boundaries.

### Preserved research notes

- New genes: `ACT-519`, `SYS-1028`, `SYS-1029`, `CON-685`, `INF-385`,
  `OBJ-220`.
- Classification result: `New gene`.
- Evidence and reasoning: the exact GameCube main-game manual directly
  distinguishes field tilt, a physically rolling body, off-course attempt
  failure, a live goal deadline and time-sensitive score. Existing
  locomotion, shot-ball and platform-life genes have different boundaries.

## Taxonomy impact

- Registry changes: six additive Active IDs; no old lifecycle or signature
  changed.
- Taxonomy-change record: `TAXONOMY_CHANGE_117`.
- Candidate terms affected: continuous stage tilt, inertia, unsupported
  edge failure, time score and avatar-in-ball goal entry.

## Negative results

- `none`; no earlier accepted mechanic or combination is disproved. A
  later-edition physics claim is excluded, not rejected as false.

## Delta summary

## New facts

- [Confirmed | Direct | High] `SMB2-001`–`SMB2-004` establish the
  tilt-driven, timed one-stage Story attempt and its separate optional score.

## New genes

- [Observation | Direct | High] Six bounded IDs for stage tilt, rolling
  response, time-sensitive score, edge failure, stage HUD and goal entry.

## New combinations

- [Observation | Direct | High] No new combination; one scoped game is not a
  second independent carrier for a reusable interaction.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_117` records the six
  additions; old signatures remain unchanged.

## New questions

- What are the measured ball acceleration and friction on the original
  GameCube disc with neutral controller calibration? Which exact *Simple*
  banana arrangement and timer are shown in each regional disc revision?

## Next recommended game

- [Hypothesis | Limited | Medium] No game is selected beyond the completed
  nine-subject horizon. The maintainer should review genre and evidence
  diversity before reserving another ID.
- Optimisation criterion: broaden independently observed physics-control
  families without chaining adjacent similar artwork or input loops.
- Expected information gain: a later original-disc comparison could test
  whether continuous field tilt deserves wider reuse.
- Backlog impact: preserve all unselected candidates in the research plan.

## Why this game

- [Hypothesis | Limited | Medium] The 2002 GameCube packet adds a familiar
  stage-tilt navigation loop between physical object puzzles and live
  traversal games while ending the selected horizon with a different visual
  and mechanical family from CATAN.
