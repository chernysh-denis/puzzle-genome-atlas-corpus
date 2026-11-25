---
game_id: GAME-0712
slug: jellycar-worlds
game_title: "JellyCar Worlds"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-308
  system:
    - SYS-036
    - SYS-1997
    - SYS-1998
  constraint: []
  information:
    - INF-208
    - INF-317
  objective:
    - OBJ-026
    - OBJ-372
  time:
    - TIM-003
---

# Game: JellyCar Worlds

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Drive a deformable car through moving course geometry and reach the
normal stop sign. Optionally repeat the same course against a distinct
time target.

## Analysis scope

- Version / ruleset: American English commercial Nintendo Switch
  eShop base game. Nintendo dates the release to December 8, 2022.
  The main recording is attributed to Nintendo Switch in April 2023.
  A second commercial eShop recording corroborates the normal route
  in January 2025. Exact installed build, console model and patch
  parity are unverified.
- Structured analysis target: PLAT-NINTENDO-SWITCH in
  [platform coverage](../../platforms/games.json).
- Entry: Level 1-1 of solo Worlds Adventure, at its initial
  car-drop entrance and uncommitted ordinary time challenge.
- Primary decision loop: apply forward or reverse wheel drive
  and tilt to keep the car aligned as it rolls, deforms and rebounds.
  Follow the descending route through the moving blocks and roller
  bend. Reach the red stop sign to clear the ordinary course.
  For the optional replay, select Beat the Clock, adjust the line
  after restarting and meet its independently declared time target.
- Positive terminal: Level 1-1 Complete at an observed 0:38.991.
  The comparative replay ends with Challenge Complete at 0:30.416,
  under the 0:35 target for Beat the Clock.
- Included: wheel drive, local airborne or low-speed tilt,
  continuous collision, deformation and recovery, local input
  hints, finish, fresh restart and the separately selected time
  challenge on Level 1-1.
- Excluded: alternative exits, later Grow, Balloon or other
  powers, personal-best persistence after relaunch, developer
  time challenge execution, custom cars, editor, physical
  motion controls and exact simulation constants.
- Potential scoped module: quantify eligibility and release of the
  temporary Grow state on one later commercial course.
- Direct-play status: no personal Switch session, installed build
  inspection or recorded controller telemetry. The eShop edition,
  Walaber's guide and technical account, and two Switch-attributed
  recordings delimit the rule evidence. Frame inspection was in
  the background with no audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| JCW-001 | Nintendo lists the complete Nintendo Switch eShop game, publisher Walaber Entertainment, American English and December 8, 2022 release. Some Walaber materials dated December 2022 advertise December 9. The regional eShop listing governs this scope. | Confirmed | Direct | High | P1, P2, P3 |
| JCW-002 | The dedicated car can drive forward and reverse and tilt its body to recover wheel contact or adjust a landing. The course supplies spatial hints for acceleration, reverse and flipping. | Observation | Corroborated | High | P3 0:03–0:17; W1 0:43–1:15; W2 0:48–1:20 |
| JCW-003 | The body and tyres deform under contact. The car can flatten under a moving block and recover its shape when compression eases. It also changes orientation to travel around the roller bend. The developer describes elasticity and shape matching for the body, pressure for tyres and joints between the assemblies. | Observation | Corroborated | High | P4; W1 1:03–1:12, 1:51–1:56, 3:00–3:05; W2 1:12–1:18 |
| JCW-004 | Contact with the red stop sign transitions out of the active course and displays Level 1-1 Complete with the finished elapsed time, 0:38.991 in W1. The ordinary result gives a separate entry point to Challenges. W2 shows the same exit and completion at a different elapsed time. | Observation | Corroborated | High | P3 0:07–0:09, 1:05–1:12; W1 1:20–1:28; W2 1:24–1:29 |
| JCW-005 | In the selected Beat the Clock replay, pausing and choosing Restart restores the starting geometry, the initial vehicle drop and a fresh elapsed clock while keeping the challenge selected. The screen also offers Quick Reset with a gesture hint. | Observation | Direct | High | W1 1:56–2:03; W2 0:45–0:55 for the quick reset hint |
| JCW-006 | Beat the Clock names the same red sign and an inclusive 0:35 elapsed limit before replay. The ordinary 0:38.991 run already clears the level. The tagged replay at 0:30.416 shows a separate Challenge Complete banner and reward cue. | Observation | Direct | High | W1 1:27–1:36, 3:13–3:18; P3 1:05–1:16 |

## Basic data

- Release / origin: Walaber Entertainment LLC, US Nintendo Switch
  eShop edition, December 2022. JellyCar Worlds revisits the series
  in a new commercial base game with separately themed worlds.
- Families: FAM-007 for driving through changing geometry with a
  deformable body, and FAM-010 for real-time body reactions and the
  scoped optional elapsed challenge.
- P1: [Nintendo US product page](https://www.nintendo.com/us/store/products/jellycar-worlds-switch/).
- P2: [Walaber's press kit](https://www.walaber.com/jellycar-worlds-press-kit).
- P3: [Walaber's controls and features video](https://www.youtube.com/watch?v=w5mDcQ4LO2g).
  The edited presentation is evidence of supported controls, the
  stop-sign convention and the existence of distinct challenges.
  Its shots need not all be Nintendo Switch footage.
- P4: [Tim FitzRandolph's technical account of the car simulation](https://www.gamedeveloper.com/programming/deep-dive-the-soft-body-physics-of-jelly-car-explained).
  The developer describes moving shape points, elastic constraints,
  tyre pressure and connected wheel assemblies. The analysis
  relies on observable deformation, not version-specific constants.
- W1: [Nindie Spotlight, Nintendo Switch Level 1-1 and challenge replay](https://www.youtube.com/watch?v=_cstHTrD1ro&t=42s).
  Main implementation and observed transition witness, published
  April 2023.
- W2: [NintenDaan, Nintendo Switch eShop opening route](https://www.youtube.com/watch?v=mhf03SEcqJ8&t=45s).
  Published January 2025. Corroborates the route and ordinary exit.
- Claim IDs: JCW-001–JCW-006.

### Reproducible fixture evidence

1. Enter solo Level 1-1. W1 0:42–0:55 shows the car settle on the
   left ledge, accelerate right and drop beyond the first ramp
   and suspended strips. A local prompt then names Reverse.
2. At W1 0:55–1:07, reverse on the lower surface toward the
   moving blocks and press through the middle passage when it
   can be crossed. The next attempt at 1:51–1:56 visibly
   compresses the same car under a block and keeps driving after
   it recovers. The record cannot isolate a single force magnitude.
3. W1 1:07–1:13 shows the wheels approach the large rollers and
   the car curve around the end roller through the narrow teal
   passage into the lower corridor. W2 1:12–1:18 corroborates the
   geometry and downward handoff. Use tilt to regain wheel
   contact at the stepped end.
4. At W1 1:20–1:24, reach the red sign. The elapsed time stops
   at 0:38.991 and the ordinary completion menu appears. Open
   Challenges to read the 0:35 Beat the Clock threshold. The
   separate Beat the Dev choice remains outside the run.
5. During the selected replay, W1 1:57–2:00 shows Restart in the
   pause menu and the fresh attempt from the same starting
   ledge. The replay banner persists across the reset.
6. Follow the successful retry from about W1 2:42 to 3:14.
   It approaches the block chamber and rollers again, then
   reaches the stop sign at 0:30.416 elapsed. The Challenge
   Complete banner appears at about 3:16. The 0:35 condition was
   met without converting it into an ordinary completion limit.

## Mechanical decomposition

### Action Genes

- ACT-290: directly drive the dedicated car. The traced route
  uses both forward and reverse wheel drive.
- ACT-308: tilt or flip the dedicated car relative to its wheels
  or airborne orientation to recover a useful pose.

### System Behaviour Genes

- SYS-036: position, speed and orientation continue to resolve
  under gravity, wheel motion, normal contact and momentum.
- SYS-1997: contact changes the distributed shape of the body
  and tyres. The linked body and wheels can compress, travel
  through restricted geometry and regain shape on unloading.
- SYS-1998: restarting a live authored attempt restores local
  course state and elapsed clock while retaining the currently
  selected rule, such as a time challenge.

### Constraint Genes

- No separate constraint gene. The relevant geometry and contact
  are represented by the live body and deformation rules. The
  optional time threshold is scoped to its objective.

### Information Genes

- INF-208: the settled driving result exposes the final elapsed
  time and distinct progression and replay choices.
- INF-317: route-local tutorial prompts identify the relevant
  control at a change of required movement.

### Objective Genes

- OBJ-026: drive the controlled body to the normal red stop sign
  through the authored course.
- OBJ-372: deliberately repeat the completed route under the
  separate optional elapsed-time ceiling and reach the same sign.

### Time Genes

- TIM-003: moving blocks, rotation, elapsed clock and body state
  continue while acceleration, reversal and tilt can be adjusted.

### Parameters

Initial pose, drive direction, airborne orientation, wheel
contact, deformable body shape, moving block position, roller
clearance, sign overlap, challenge identity and elapsed limit.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Car at the starting ledge | Drive down the right approach | Car drops into a lower lane with a reverse prompt | JCW-002 |
| Lower corridor before a moving block | Follow the opening and adjust drive | Body and tyres compress with contact and recover under reduced load | JCW-002–JCW-003 |
| Approach to the end roller | Keep the wheels aligned through the curved clearance | Car follows the roller bend and drops to the lower corridor | JCW-003 |
| Ordinary attempt near the exit | Touch the red sign | Elapsed result stops at 0:38.991 and Level 1-1 Complete appears | JCW-004 |
| Ordinary completion | Select Beat the Clock | Replay uses the same finish and exposes the separate 0:35 ceiling | JCW-004–JCW-006 |
| Paused replay already away from the entrance | Choose Restart | Fresh car drop and elapsed time with challenge retained | JCW-005 |
| Beat the Clock replay below 0:35 | Touch the same sign at 0:30.416 | Separate Challenge Complete and reward cue | JCW-006 |

## Strategic and experiential structure

The player controls wheel drive and body pitch while course
geometry and soft-body contact keep changing. Reversal can make
the lower route reachable. Moving obstacles need room to pass,
and elastic recovery preserves the car after contact. A clean
ordinary finish can be replayed for speed on the same geometry.

## Replay and variation

The ordinary and challenge recordings traverse the same 1-1 route.
Only the selected replay is judged by the measured 0:35 condition.
The documented Restart returns to the beginning mid-attempt. A
local pause-menu selection, quick reset gesture hint and the
post-clear Play Again choice are distinct affordances.

## Adjacent systems and history

Walaber's direction and control explanations mention later special
abilities and optional alternate exits. The ordinary 1-1 fixture
establishes baseline deformation and the separate challenge, with
no temporary enlargement needed or observed.

## Normalised genome

- Action: ACT-290, ACT-308.
- System Behaviour: SYS-036, SYS-1997, SYS-1998.
- Constraint: none.
- Information: INF-208, INF-317.
- Objective: OBJ-026, OBJ-372.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `711` (`GAME-0001`–`GAME-0711`).
- Exact genome matches: none.
- Tied near matches: `GAME-0677` — Stunt Car Racer (`4 / 17 = 0.235294`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Stunt Car Racer (GAME-0677)](../s-z/stunt-car-racer.md) | ACT-290, INF-208, SYS-036, TIM-003 | JellyCar Worlds drives a soft car alone to one stop sign and offers an optional same-course time challenge. Stunt Car Racer scores an elevated circuit against a rival and records win and best-lap credits in a division. | Near, `0.235294`. |

## Taxonomy impact

Reuse dedicated drive, vehicle tilt, continuous dynamics, driving
result, local authored hints, designated arrival and real-time
adjustment. Admit one boundary for recoverable deformation of the
vehicle assemblies, one for a selected-rule restart during the
live attempt and one for the separate timed retry objective.

## Negative results

- Crush and release in the observed chamber do not establish a
  damage model or an interchangeable suspension part.
- The recorded ordinary finish succeeds above the replay's time
  ceiling. That ceiling applies only after selecting its challenge.
- Restart returns to the entrance, not to an intermediate
  location or a variable rewind point.
- The timed settlement does not establish retained rewards or best
  time after relaunch.

## Delta summary

Wheel drive, tilt and real-time elastic contact determine path
through the close geometry. Touching the stop sign clears the
ordinary route. The selected same-route replay keeps its condition
when restarting and has separate timed settlement.

## New facts

- The same car can recover from visible flattening in passage.
- The ordinary finish makes an optional timed replay available.
- A paused replay can restart the course with the selected rule
  retained.

## Principles and design implications

Treat deformation as a navigational state when contact changes
clearance. Keep the standard completion and stricter replay
objective legible as separate outcomes on one geometry.

## Puzzle or game generation potential

Build a short 2D route with a reversal, one moving clearance, a
roller bend and a single normal outcome marker. Add a separately
chosen elapsed target on the same course. Compare a normal finish
above the target, a mid-run restart and a successful timed finish.

## New genes

- OBJ-372
- SYS-1997
- SYS-1998

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 458](../../../research/taxonomy-changes/TAXONOMY_CHANGE_458.md).

## New questions

- What is the exact toggle and refill behaviour of Grow in the
  Nintendo Switch version?
- Which additional states persist through each available restart
  control when the course contains optional pickups?

## Next recommended game

Continue Selection 062 with Firestriker, the North American Super
Nintendo commercial cartridge. Follow a single-player arena from
Trialight contact through its target criterion and exit.

## Why this game

One short route distinguishes wheel control from continuous
deformation and shows ordinary and stricter replay outcomes at the
same goal.
