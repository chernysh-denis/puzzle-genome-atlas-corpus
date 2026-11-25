---
game_id: GAME-0731
slug: pengo
game_title: "Pengo"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
  system:
    - SYS-045
    - SYS-2033
    - SYS-2034
    - SYS-2035
    - SYS-2036
    - SYS-2037
    - SYS-2038
  constraint: []
  information:
    - INF-179
    - INF-660
  objective:
    - OBJ-007
  time:
    - TIM-003
---

# Game: Pengo — Round 1 on the original SEGA cabinet

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Pengo, Sno-Bees, ordinary ice and the three diamond blocks are
instances of the scoped maze.

## Analysis scope

- Version / ruleset: English North American SEGA commercial arcade cabinet,
  1982, under the ordinary one-player rules documented in original owner's
  manual 420-0811. Use one credited start and the first maze. The recording
  displays `© SEGA 1982`. Exact ROM set, cabinet hardware and operator
  switch positions are unverified.
- Reproducible entry and exit: press the one-player start button and
  begin at the Round 1 maze with the initial flashes. Follow live play
  through the enemy clear and credited time result. Stop at the result
  table before acting in Round 2.
- Primary decision loop: move through the current passages while the
  Sno-Bees pursue, choose a facing interaction with a block or wall,
  use the moving block or a reversible stun against the enemy and
  compare the time cost of clearing early with the optional diamond award.
- Included: facing-based sliding and breaking, hostile interception,
  wall stun, replacement eggs and their brief disclosure, diamond
  alignment, maze clear, and the elapsed-time bonus. Excluded: life-stock
  economy beyond lethal contact, sustained last-enemy escape timing,
  operator option changes, later mazes, interludes and home ports.
- Direct-play status: no personal cabinet or emulator session. The original
  cabinet manual, period trade material and recorded arcade play establish
  the scoped transitions. Only silent background frames were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PE-001 | The 1982 cabinet has four-way control and one facing action input. The initial maze contains ordinary ice, three movable diamond blocks and pursuing Sno-Bees. | Observation | Corroborated | High | P1 p. 4, P2, W1 00:24–00:49, S1 |
| PE-002 | A free adjacent block slides directly away from the player until a solid block or wall stops it. If something solid sits immediately beyond the addressed ordinary block, the same input can disintegrate it in place. Diamond blocks slide when free and resist disintegration. | Observation | Corroborated | High | P1 p. 4, W1 00:51–01:01 and 01:12–01:24, S1 |
| PE-003 | A sliding block sweeps a Sno-Bee to its solid stop and crushes it there. One ordinary crush is worth 400 points, with larger set awards if a single block catches more than one enemy. | Observation | Corroborated | High | P1 pp. 4–5, W1 00:52–00:55 and 01:09–01:12, S2 |
| PE-004 | Addressing an outer wall briefly freezes Sno-Bees touching that same side. Pengo can remove an immobilised enemy by reaching it before recovery. Contact with a normally active Sno-Bee is lethal. | Observation | Corroborated | High | P1 pp. 4–5, S1, S2. W1 corroborates vulnerable contact after the global freeze. |
| PE-005 | A brief flash reveals blocks holding eggs. An unbroken host can release an additional enemy. Crushing a still-occupied egg block removes the reserve and pays the documented 500 points. The precise hatch scheduler was not timed. | Observation | Corroborated | High | P1 pp. 4–5, W1 00:47–00:52 and 00:55–01:06, S2 |
| PE-006 | When all three diamonds touch in a straight interior line, movement pauses for the score tally. After tallying the 10,000 points, play resumes with the surviving enemies stunned for a short interval. The manual also specifies 5,000 for a line along a wall. | Observation | Corroborated | High | P1 pp. 4–5, W1 01:22–01:37, S2 |
| PE-007 | The scoped path removes the remaining active enemies and settles Round 1. The result lists 48 seconds and adds 500 points. Each score bracket is listed through zero credit from 60 seconds on. | Observation | Corroborated | High | P1 p. 5, W1 01:33–01:44 |
| PE-008 | The manual describes the last surviving Sno-Bee accelerating and ultimately disappearing if left alive. The shown successful trace removes its remaining enemies during the stun window. The exact timeout and escape path vary in descriptions and are outside the witnessed sequence. | Observation | Limited | Medium | P1 p. 4, W1 01:32–01:44, S2, S3 |

## Basic data

- Release / origin: SEGA's 1982 commercial arcade game, North American
  owner documentation and sales flyer. The analysed target is
  `PLAT-ARCADE-CABINET`.
- Mechanical families: `FAM-007` for lane-dependent block motion and
  collision, and `FAM-010` for an arena whose pursuers and reserve
  arrivals advance while the player repositions.
- Primary evidence checked 2026-11-25:
  - **P1:** [SEGA Electronics owner’s manual 420-0811](https://arcarc.xmission.com/PDF_Arcade_Manuals_and_Schematics/Pengo_Owners_Manual_%28420-0811%29.pdf).
    Printed pp. 4–5 cover control, ice classes, the wall, eggs and
    the separate score tables. The operator tables describe variants.
  - **P2:** [SEGA’s 1982 US arcade sales flyer](https://flyers.arcade-museum.com/arcades/show/1846).
    American commercial cabinet evidence.
- Recorded and period evidence:
  - **W1:** [GEURO’s arcade Round 1 capture](https://www.youtube.com/watch?v=3MaLvOKxA4E&t=46s).
    Moves from a one-player credit through the first maze, interior
    diamond bonus, vulnerable contacts and time table. No PCB or ROM
    identity is assigned based on the capture.
  - **S1:** [Video Games, March 1983](https://www.digitpress.com/library/magazines/video_games/video_games_mar83.pdf),
    printed p. 42, contemporary arcade play report. It distinguishes
    block disintegration, free travel and wall freezing.
  - **S2:** [Joystik, April 1983](https://arcarc.xmission.com/Magazines%20and%20Books/Joystik%20Magazines%20%2810%20Issues%29/Joystik_Vol1-5_83-Apr.pdf).
    Period play account with the egg, diamond and wall strategies.
  - **S3:** [Arcade History’s cabinet and revision entry](https://www.arcade-history.com/game/1944/pengo).
    Later documentation of the final enemy and cabinet variants.
    The original manual and Round 1 frames own the accepted boundary.
- Claim IDs: PE-001–PE-008. The first round can be repeated with
  each starting maze recorded separately. Read the awarded time
  directly from the displayed table and distinguish it from the
  optional alignment award.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: steer Pengo through the current open passages
  (PE-001, PE-002).
- Reuse `ACT-341`: commit the local interaction with the addressed
  ice block or perimeter side (PE-002, PE-004).

### System Behaviour Genes

- Reuse `SYS-045`: Sno-Bees traverse the changing maze without awaiting
  each player command (PE-001, PE-003).
- New `SYS-2033`: branch between sliding to a stop and breaking when
  blocked, with a separate durable block class (PE-002).
- New `SYS-2034`: a sliding block sweeps enemies and resolves the
  captured set at the solid stop (PE-003).
- New `SYS-2035`: the addressed side temporarily reverses the
  ordinary contact outcome for hostiles touching that side (PE-004).
- New `SYS-2036`: reserves hatch from particular destructible hosts,
  and early removal of a host denies its reinforcement (PE-005).
- New `SYS-2037`: special-object alignment adds a position-dependent
  award and releases a temporary global stun (PE-006).
- New `SYS-2038`: clearing the round pays the applicable elapsed-time
  score bracket (PE-007).

### Constraint Genes

No separate constraint is admitted. Direction validity, immediate
obstruction, durable blocks and aligned-object criteria are parts
of the corresponding state transitions.

### Information Genes

- Reuse `INF-179`: the bounded field shows Pengo, the maze, live enemies
  and distinguishable diamond blocks (PE-001).
- New `INF-660`: a temporary flash identifies egg-bearing ordinary
  blocks before their reserves emerge (PE-005).

### Objective Genes

- Reuse `OBJ-007`: remove the enemy targets from the current maze to
  settle the observed clear, including enemies that hatch or reserves
  broken inside ice. Optional alignment contributes score and leverage
  during the clear (PE-003, PE-005–PE-007).

### Time Genes

- Reuse `TIM-003`: choose timing and direction while the enemies travel.
  The discrete diamond tally temporarily halts active movement (PE-003, PE-006).

## Formal state and transitions

Track Pengo's cell and facing, boundary sides, the two block classes,
their cells and any sliding body, the active enemy set, its stunned
subset and the egg-bearing host set. A sliding body may carry a captured
enemy until a solid stopping position is reached. Addressing a wall
creates a side-specific vulnerability window. A credited diamond line
pauses movement and leaves all surviving active enemies temporarily
vulnerable when control comes back. Track the accumulated score and
time result separately.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Facing a block with open space behind it | Press the action button | The block slides until it meets solid geometry | PE-002 |
| Facing an ordinary block with an immediate solid stop beyond it | Use the same action | The ordinary block disintegrates and its cell opens. A diamond under the same condition survives | PE-002 |
| An active enemy is in a sliding block's lane | Let the block reach its end | The enemy is swept to the stopping surface and crushed, with point credit | PE-003 |
| A Sno-Bee touches the addressed outer wall | Pulse that wall, then reach the enemy during the stun | The temporarily vulnerable enemy is removed by contact | PE-004 |
| An egg is still in a destructible host | Break the eligible block before it hatches | The reserve disappears before entering the maze | PE-005 |
| Third diamond becomes adjacent in a straight interior line | Let the award settle | The interior award transfers to score and surviving Sno-Bees are temporarily stunned | PE-006 |
| The scoped clear ends at the 48-second result | Let the time table settle | 500 additional points are credited in the 40–49 second bracket | PE-007 |

## Strategic and experiential structure

Work backward from a solid stopping line so a push will sweep a
hostile rather than merely change the corridors. The wall method can
turn a chase into a brief opportunity. Early recognition of egg
locations can prevent a replacement enemy. Taking time to align
diamonds trades some speed for a larger bonus and a useful stun.

## Replay and variation

Ordinary maze contents and positions should be observed on each
retry. The manual describes a faster last enemy that can disappear.
The GEURO run credits direct removal and a 48-second time result.
The wall-line award is documented independently of the interior
line witnessed in the trace.

## Adjacent systems and history

The owner's manual distinguishes one- and two-player operation and
operator options. Later rounds change enemy quantities and layouts.
The analysis ends at the ordinary first round and leaves later
interludes and port differences outside its scope.

## Normalised genome

- Action: ACT-008, ACT-341.
- System Behaviour: SYS-045, SYS-2033, SYS-2034, SYS-2035, SYS-2036,
  SYS-2037, SYS-2038.
- Constraint: none.
- Information: INF-179, INF-660.
- Objective: OBJ-007.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `730` (`GAME-0001`–`GAME-0730`).
- Exact genome matches: none.
- Tied near matches: `GAME-0387` — Super Bomberman (`5 / 22 = 0.227273`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Bomberman (GAME-0387)](../s-z/super-bomberman.md) | ACT-008, INF-179, OBJ-007, SYS-045, TIM-003 | Both move through an exposed maze with roaming enemies and clear enemy targets in real time. Super Bomberman commits a timed bomb and escapes the cross-shaped blast before exposing its exit. Pengo slides ice into enemies, can stun them from a wall and awards points for optional diamond alignment. | Near, `0.227273`. |

## Taxonomy impact

Separate forward block resolution, moving-body hostile capture and
contact vulnerability. Keep the temporary egg cue independent of
the spawn rule, and score settlement independent of the enemy clear.

## Negative results

- The interior diamond alignment leaves the round active after its
  bonus tally.
- A blocked diamond stays intact. The corresponding ordinary block
  can be broken with the same directional action.
- The result table assigns zero bonus to a clear at 60 seconds or more.

## Delta summary

Record the original arcade opening with its collision-dependent
maze editing, enemy reserves, optional positional award and separate
elapsed-time scoring.

## New facts

- A move that pushes a free block can break the blocked ordinary
  block when used from a different position.
- The optional special-object line creates a vulnerability window.
- The same maze records combat, alignment and time credit separately.

## Principles and design implications

Let one contextual action alter paths and threaten enemies along the
same axis. Telegraph temporary opportunities through distinct outcomes.
Give the player visible reasons to choose between fast clearance and
a higher-investment bonus.

## Puzzle or game generation potential

Build one reusable ice lane with a fixed stopping face, a destructible
egg host and three durable specials. Check both outcomes of the
contextual input and separate the clear from the optional score awards.

## New genes

- SYS-2033
- SYS-2034
- SYS-2035
- SYS-2036
- SYS-2037
- SYS-2038
- INF-660

## New combinations

None. The full predecessor and combination scan found no admitted combination.

## Taxonomy changes

[Taxonomy Change 477](../../../research/taxonomy-changes/TAXONOMY_CHANGE_477.md).

## Next recommended game

TOEM on PlayStation 5 is the next Selection 064 unit.

## Why this game

First-round ice placement changes both movement and combat. The optional
alignment then reuses the same movement rule to earn score and time to
act against the remaining enemies.

## Review status

Reviewed 2026-11-25 for the ordinary North American SEGA cabinet
rules. The demonstration ends with the first round's scored result.
