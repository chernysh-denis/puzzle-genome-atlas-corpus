---
game_id: GAME-0053
slug: can-of-wormholes
game_title: Can of Wormholes
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0053
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-082
    - SYS-095
  constraint:
    - CON-001
    - CON-011
    - CON-061
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-001
---

# Game: Can of Wormholes

## Analysis scope

- Version / ruleset: Munted Finger's released base game, scoped to the complete
  first authored zone `1_movement`: `1_overair`, `2_reverse`,
  `3_reversecorner` and `4_turnaround`.
- Included: one-cell cardinal endpoint control; forward head-led body
  propagation; reverse input through the tail's current outward direction;
  straight-line tail extrusion rather than path retracing; fixed platform and
  wall cells; body self-occupancy; partially unsupported poses; whole-body void
  loss; matching the worm's ordered footprint to its fixed worm-shaped hole;
  unlimited discrete undo and restart as recovery controls.
- Excluded: food and segment growth from zone 2 onward; pushing other worms,
  tail devouring, rolling, cutting, thick segments, fences and every later
  interaction; `Gain Insight` mini-stages; interactive overworld and tin-can
  controls; meta-puzzles, secrets, achievements and presentation.
- Direct-play status: not conducted. The creator's rules interview establishes
  four-direction input, endpoint reversal and straight tail behaviour; official
  and specialist sources establish holes, occupancy, void loss, undo and the
  first zone's blockless boundary. The distributed level manifest independently
  fixes the four scoped filenames and their order.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COW-001` | The first zone contains exactly four authored movement stages named `overair`, `reverse`, `reversecorner` and `turnaround` | Confirmed | Direct | High | D1 |
| `COW-002` | A cardinal forward input moves one endpoint one grid cell and propagates the ordered body through predecessor positions | Confirmed | Corroborated | High | P1, R1, R2 |
| `COW-003` | Input opposite the head direction makes the tail become the advancing endpoint along its current outward direction | Confirmed | Direct | High | P1, R1 |
| `COW-004` | Reverse motion straightens from the tail instead of replaying the complete historical path | Confirmed | Corroborated | High | P1, R1 |
| `COW-005` | Fixed platform or wall occupancy and the worm's current body footprint constrain each endpoint step | Confirmed | Corroborated | High | P1, R2, R3 |
| `COW-006` | A worm may bridge unsupported cells, but losing the complete required body to the void dissolves it and resets the attempt | Confirmed | Corroborated | High | R2, R3, D1 |
| `COW-007` | A stage completes only when a worm of matching size and ordered shape fills its declared hole | Confirmed | Corroborated | High | R1–R3 |
| `COW-008` | Every decision-relevant platform cell, body segment and target-hole cell is visible before input | Observation | Corroborated | High | R1–R3 |
| `COW-009` | One endpoint command, propagation or reverse extrusion, loss and completion check resolve before another command | Observation | Corroborated | High | P1, R1–R3 |
| `COW-010` | The first zone contains no growth, container traversal or recursive topology despite the title and overworld tin can | Confirmed | Direct | High | P1, D1, R2 |

## Basic data

- Release / origin: solo developer Ben Taylor, credited as Munted Finger,
  released Can of Wormholes on 24 March 2023.
- Platform or physical form: deterministic single-player three-dimensional
  presentation of compact orthogonal-grid articulated-body puzzles.
- Puzzle family: bidirectionally controlled ordered-body shape fitting.
- Primary and creator sources:
  - **[P1]** Ben Taylor,
    [creator interview on Thinky Games Podcast](https://zencastr.com/z/fop6T-rf),
    explaining the four directional inputs, body-as-obstacle design, forward
    Snake comparison, backward input, tail direction and straightening choice.
  - **[P2]** [Official Steam page](https://store.steampowered.com/app/1295320/Can_of_Wormholes),
    confirming developer, release date, handcrafted stages, unlimited undo /
    restart and the separation between puzzle stages and interactive overworld.
- Distributed-build evidence:
  - **[D1]** [Steam depot file manifest](https://steamdb.info/depot/1295322/),
    listing the complete `1_movement` directory as `1_overair`, `2_reverse`,
    `3_reversecorner` and `4_turnaround`, before the separate `2_food` zone.
- Specialist and platform corroboration:
  - **[R1]** [Nintendo Life review](https://www.nintendolife.com/reviews/switch-eshop/can-of-wormholes),
    documenting cellwise head movement, ordered following, straight-line tail
    reversal, worm-shaped slots and later excluded growth.
  - **[R2]** [Thinky Games overview](https://thinkygames.com/games/can-of-wormholes/),
    documenting worms of fixed lengths, platform / void / wall cells, shape-
    and-size-matched holes and the explicitly blockless first zone.
  - **[R3]** [LadiesGamers review](https://ladiesgamers.com/can-of-wormholes-review/),
    corroborating the hole goal, void dissolution and restart boundary.
- Claim IDs: `COW-001`–`COW-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One cardinal command advances the
  currently leading endpoint into one adjacent legal cell; the active endpoint
  can change when the player reverses through the tail.
- `ACT-009` is absent: the first movement zone is explicitly blockless and does
  not push another worm or independent object.
- Undo and restart restore discrete states but do not expose a time axis, so
  neither is `ACT-044`.
- Claim IDs: `COW-002`–`COW-005`, `COW-010`.

### System Behaviour Genes

- `SYS-082` — endpoint-led ordered body propagation. Forward movement makes
  every later segment occupy its predecessor's prior cell. Its representation-
  neutral boundary now admits a currently leading endpoint rather than assuming
  that one anatomical head must remain the sole control locus.
- `SYS-095` — tail-directed straight reverse propagation. An opposite input
  promotes the tail to the advancing endpoint and extrudes it along its current
  outward direction; the rest of the ordered body follows from that end rather
  than retracing historical head turns.
- `SYS-083` is absent: zone 1 precedes food and conserves body length. `SYS-069`
  and `SYS-070` are absent: neither the worm nor the can crosses a nested
  boundary or rewrites containment topology in the scoped puzzle stages.
- Resolution order: determine forward or reverse endpoint; validate the next
  cell against barriers and body occupancy; propagate the ordered segments from
  that endpoint; resolve void loss; test exact hole occupancy; accept the next
  input or complete the stage.
- Claim IDs: `COW-002`–`COW-004`, `COW-006`, `COW-007`, `COW-009`, `COW-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each scoped stage has one finite
  authored platform, wall, void and hole topology.
- `CON-011` — exclusive occupancy with static barriers. Segments occupy
  distinct cells; fixed barriers and the current body footprint reject an
  endpoint entry.
- `CON-061` — terminal required-object boundary escape. Letting the complete
  required worm lose platform support dissolves it and resets the attempt.
- `CON-012` is absent because no independent adjacent object is pushed in the
  blockless first zone.
- Scarce strategic resources: clearance at both endpoints, a usable tail
  outward direction, enough supported body to span gaps and the orientation
  needed to enter the exact hole footprint.
- Claim IDs: `COW-005`–`COW-007`.

### Information Genes

- `INF-001` — fully visible current state. Platform, walls, void, target hole,
  every segment and both endpoint orientations are inspectable before input.
- No hidden successor, random state or unpreviewed system event exists in the
  scoped four authored stages.
- Claim IDs: `COW-008`, `COW-009`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. The existing ordered worm
  must occupy every cell of its fixed worm-shaped hole with matching length and
  shape. The objective boundary is generalised from arranging several
  components to matching one articulated component's complete footprint.
- `OBJ-022` is absent: the hole is an exact retained target footprint, not an
  exit through which the controlled body evacuates the board.
- Claim IDs: `COW-007`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each endpoint command
  is followed by complete ordered propagation, void and hole checks before the
  next input.
- `TIM-002` is absent under the exclusive taxonomy boundary because the
  decision-relevant body update is a system resolution after endpoint input.
- Unlimited undo is recovery history rather than `TIM-007`; no running
  simulation clock or editable temporal axis exists.
- Claim IDs: `COW-002`–`COW-004`, `COW-006`, `COW-007`, `COW-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Forward neighbour is free | Move one cardinal cell through the head | Head advances and each segment occupies its predecessor's old cell | ordinary endpoint-led propagation | `COW-002` |
| Input is opposite the head-facing direction | Press that direction | Tail becomes the advancing endpoint along its own outward direction | reversal changes the control locus | `COW-003` |
| Tail follows a recently bent historical path | Continue reverse input | Tail extrudes straight from its present orientation; later segments follow it | reverse is not historical path replay | `COW-004` |
| Endpoint destination is a wall or occupied body cell | Move toward it | Input is rejected and the ordered pose remains unchanged | static and self-occupancy constrain motion | `COW-005` |
| Some middle segments span void while other segments remain supported | Complete the move | Worm retains one connected ordered pose | partial overhang is legal | `COW-006` |
| Complete required body loses the platform | Complete the move | Worm dissolves and the attempt returns to a recoverable state | whole-body void loss is terminal | `COW-006` |
| Length matches but one bend differs from the hole | Enter the partial target | Stage remains incomplete | occupancy requires exact ordered shape | `COW-007` |
| Every worm segment matches the target hole | Complete the final endpoint move | Stage completion is credited | full footprint reconstruction is the goal | `COW-007` |

## Strategic and experiential structure

- Local decision: choose which endpoint should lead and whether its next step
  preserves the tail orientation needed for a later reverse.
- Medium-term planning: use legal overhangs and bends to reposition the body
  without blocking both endpoints or destroying access to the hole mouth.
- Long-term structure: reconstruct the target footprint while reasoning about
  two asymmetric propagation rules over the same conserved segment order.
- Common heuristics: mark the current outward direction at each end; simulate
  a reverse as straight extrusion; enter the hole from the end whose remaining
  body naturally follows its bends.
- Failure attribution: the complete visible transition makes a failed pose
  traceable to endpoint choice, self-blocking, support loss or shape mismatch.
- Player-trust factors: endpoint selection, segment update order, self-contact,
  support and target acceptance must remain deterministic.
- Claim IDs: `COW-002`–`COW-009`.

## Replay and variation

- All four stage topologies, body lengths and target holes are authored; no
  random or procedural state changes between attempts.
- Equivalent walking detours may exist, but reverse direction and final hole
  entry strongly constrain the decisive sequence.
- Replay is driven by undoing a locked pose, learning the reverse rule or
  solving an optional separate `Gain Insight` stage, which remains excluded.
- Claim IDs: `COW-001`, `COW-003`, `COW-004`, `COW-007`.

## Adjacent systems and history

- Snakebird shares ordered following, fixed cells, self-occupancy, visible
  deadlock and automatic resolution. It grows, falls as a complete body and
  clears fruit before evacuating; zone 1 of Can of Wormholes instead conserves
  length, reverses through either endpoint and reconstructs a hole footprint.
- Sokoban shares fixed visible deadlock planning and a configuration objective,
  but a one-cell keeper pushes independent crates rather than propagating its
  own ordered body.
- Stephen's Sausage Roll shares a multi-cell occupancy puzzle and automatic
  post-input response, but a separate rigid sausage slides or rolls under a
  fork; it has neither an ordered follower chain nor endpoint reversal.
- Patrick's Parabox shares visible grid occupancy and configuration recovery,
  but mutates containment between nested spaces. The scoped Can of Wormholes
  stages contain no container traversal or recursive topology.
- Claim IDs: `COW-002`–`COW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | cardinal endpoint step |
| System Behaviour | `SYS-082`, `SYS-095` | forward follow and tail-directed reverse |
| Constraint | `CON-001`, `CON-011`, `CON-061` | fixed cells, self-blocking and void loss |
| Information | `INF-001` | visible endpoint orientations and target footprint |
| Objective | `OBJ-004` | exact shape-and-length hole occupancy |
| Time | `TIM-001` | input followed by complete propagation and checks |

Canonical signature:

`ACT-008; SYS-082,SYS-095; CON-001,CON-011,CON-061; INF-001; OBJ-004; TIM-001`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`–`GAME-0052`.
- Exact genome matches: none.
- Existing combination subsets: none. `COMB-0045` requires growth, gravity,
  exhaustive collection and evacuation; `COMB-0044` requires adjacent-object
  pushing; every other verified proper subset was tested and rejected.
- Unique near match: `GAME-0045` — Snakebird at intersection `7`, union `16`,
  `7 / 16 = 0.437500`. Sokoban follows at `5 / 13 = 0.384615`; A Good Snowman
  at `5 / 14 = 0.357143`; Stephen's Sausage Roll at
  `6 / 17 = 0.352941`; Peg Solitaire at `4 / 15 = 0.266667`; Shogun Showdown
  at `5 / 19 = 0.263158`.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `3 / 20 = 0.150000`.
  - `GAME-0002`: `3 / 13 = 0.230769`.
  - `GAME-0003`: `2 / 17 = 0.117647`.
  - `GAME-0004`: `2 / 22 = 0.090909`.
  - `GAME-0005`: `2 / 14 = 0.142857`.
  - `GAME-0006`: `5 / 13 = 0.384615`.
  - `GAME-0007`: `2 / 15 = 0.133333`.
  - `GAME-0008`: `2 / 14 = 0.142857`.
  - `GAME-0009`: `3 / 22 = 0.136364`.
  - `GAME-0010`: `3 / 15 = 0.200000`.
  - `GAME-0011`: `2 / 20 = 0.100000`.
  - `GAME-0012`: `2 / 16 = 0.125000`.
  - `GAME-0013`: `3 / 19 = 0.157895`.
  - `GAME-0014`: `3 / 21 = 0.142857`.
  - `GAME-0015`: `3 / 20 = 0.150000`.
  - `GAME-0016`: `2 / 22 = 0.090909`.
  - `GAME-0017`: `1 / 21 = 0.047619`.
  - `GAME-0018`: `1 / 27 = 0.037037`.
  - `GAME-0019`: `4 / 15 = 0.266667`.
  - `GAME-0020`: `2 / 21 = 0.095238`.
  - `GAME-0021`: `2 / 16 = 0.125000`.
  - `GAME-0022`: `1 / 20 = 0.050000`.
  - `GAME-0023`: `0 / 19 = 0.000000`.
  - `GAME-0024`: `1 / 20 = 0.050000`.
  - `GAME-0025`: `1 / 19 = 0.052632`.
  - `GAME-0026`: `1 / 20 = 0.050000`.
  - `GAME-0027`: `2 / 19 = 0.105263`.
  - `GAME-0028`: `2 / 24 = 0.083333`.
  - `GAME-0029`: `3 / 18 = 0.166667`.
  - `GAME-0030`: `1 / 22 = 0.045455`.
  - `GAME-0031`: `1 / 19 = 0.052632`.
  - `GAME-0032`: `2 / 18 = 0.111111`.
  - `GAME-0033`: `2 / 20 = 0.100000`.
  - `GAME-0034`: `2 / 21 = 0.095238`.
  - `GAME-0035`: `2 / 25 = 0.080000`.
  - `GAME-0036`: `4 / 17 = 0.235294`.
  - `GAME-0037`: `2 / 17 = 0.117647`.
  - `GAME-0038`: `2 / 23 = 0.086957`.
  - `GAME-0039`: `2 / 17 = 0.117647`.
  - `GAME-0040`: `2 / 15 = 0.133333`.
  - `GAME-0041`: `2 / 18 = 0.111111`.
  - `GAME-0042`: `1 / 17 = 0.058824`.
  - `GAME-0043`: `6 / 17 = 0.352941`.
  - `GAME-0044`: `5 / 14 = 0.357143`.
  - `GAME-0045`: `7 / 16 = 0.437500`.
  - `GAME-0046`: `1 / 18 = 0.055556`.
  - `GAME-0047`: `3 / 20 = 0.150000`.
  - `GAME-0048`: `3 / 20 = 0.150000`.
  - `GAME-0049`: `2 / 16 = 0.125000`.
  - `GAME-0050`: `5 / 19 = 0.263158`.
  - `GAME-0051`: `1 / 24 = 0.041667`.
  - `GAME-0052`: `1 / 18 = 0.055556`.
- Scan date: 2026-08-13.
- New genes: `SYS-095`.
- Reused genes: `ACT-008`, `SYS-082`, `CON-001`, `CON-011`, `CON-061`,
  `INF-001`, `OBJ-004`, `TIM-001`.
- Classification result: `New gene` and a new verified combination; no novelty
  claim.

## Combination record

- `COMB-0053` captures endpoint-led ordered propagation, the distinct straight
  reverse rule and exact target-footprint reconstruction.
- Exhaustive supporter scan: only `GAME-0053` contains the complete proper
  subset.

## Taxonomy impact

- Generalised `SYS-082` from a permanently head-led body to an endpoint-led
  ordered body while retaining Snakebird's fixed-head control as a parameter.
- Generalised `OBJ-004` to cover one articulated object's complete target
  footprint as well as arrangements of several components. No earlier
  signature changes.
- Added `SYS-095`; added Can of Wormholes evidence to the nine reused genes.
  No merge, split, lifecycle or type change.

## Negative results

- The planned can-entry / recursive-space boundary is rejected. The tin can is
  an overworld launcher, while the complete first zone contains only four
  movement stages and predates food, pushing and later transformations.
- `ACT-009`, `SYS-070`, `SYS-083`, `SYS-084`, `OBJ-022` and `TIM-002` fail the
  bounded first-zone transitions. No standalone negative-result record is
  needed because the correction affects only the provisional unit scope.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Reverse input advances from the tail's current
  outward direction instead of retracing the head's historical path.
- [Confirmed | Direct | High] The complete first zone is four blockless
  movement stages and contains no growth or recursive container traversal.

## Нові гени

- `SYS-095` — tail-directed straight reverse propagation.

## Нові комбінації

- `COMB-0053` — bidirectional ordered-body shape reconstruction.

## Зміни таксономії

- [Observation | Corroborated | High] `SYS-082` now admits either controlled
  endpoint; `OBJ-004` admits exact articulated-footprint targets. Existing
  signatures remain unchanged.

## Нові питання

- Which independent articulated-body puzzle repeats endpoint-swapping reverse
  propagation without inheriting Can of Wormholes' rule directly?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0054` — A Monster's Expedition.

## Чому саме вона

- It leaves direct body control and tests log-rolling state, traversal-created
  connectivity and open-world dependency structure before the 55-game audit.
