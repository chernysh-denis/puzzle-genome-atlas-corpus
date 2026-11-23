---
game_id: GAME-0529
slug: tetris-effect
game_title: Tetris Effect
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids:
  - COMB-0004
gene_ids:
  action:
    - ACT-005
    - ACT-006
    - ACT-722
    - ACT-723
    - ACT-724
  system:
    - SYS-004
    - SYS-006
    - SYS-007
    - SYS-008
    - SYS-009
    - SYS-1520
    - SYS-1521
    - SYS-1522
  constraint:
    - CON-001
    - CON-007
    - CON-008
    - CON-440
  information:
    - INF-001
    - INF-005
    - INF-514
  objective:
    - OBJ-002
    - OBJ-003
    - OBJ-007
  time:
    - TIM-003
---

# Game: Tetris Effect

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Well dimensions, queue depth, gauge marks and score amounts parameterise the
rules.

## Analysis scope

- Version / ruleset: North American English PlayStation 4 release rules,
  Enhance, 2018, before the Connected update. Journey Mode, Normal, standard
  display with the default Hold, next queue and landing outline enabled.
  An exact installed patch and executable identity were not checked.
- Structured analysis target: PLAT-PLAYSTATION-4, full 2018 release with
  a standard controller and display. PlayStation VR is optional in this
  edition and outside this analysis.
- Primary decision loop: read the well, landing outline, reserve and
  upcoming pieces. Choose a legal fit and lock it, taking ordinary rows
  toward the stage goal. Decide whether to spend the charged Zone to
  interrupt gravity and collect rows for later removal and added score.
- Entry: start a new Normal Journey in Area 1, at the empty well of
  The Deep. Exit: complete the 36 credited rows and observe the transition
  to Pharaoh's Code. An early terminal top-out ends an unsuccessful
  attempt. No moves in Pharaoh's Code are included.
- Included: translation, rotation with fitted offsets, two drop inputs,
  ordinary automatic descent and contact locking, the ready queue,
  one-piece Hold, row completion, score, stage count, speed changes and
  one or more optional Zone uses.
- Excluded: other difficulty settings, exact rotation offset tables and
  timing constants, individual scoring coefficients, complete Journey
  runs, Effect Modes, online events, the Connected update, multiplayer,
  external music rules, ports and altered control-assist options.
- Direct-play status: no console or emulator ran. The scope is reconstructed
  from Enhance's original release materials, contemporary firsthand PS4
  accounts and a technical comparison. The later official-hosted community
  guide is corroboration for common controls and documented mechanics.
  Exact historical frames and executable identity are unverified. No
  video or audio was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TE-001 | The November 2018 PS4 release includes Journey with three difficulties. The first Normal stage is The Deep, with a 36-row target, followed by Pharaoh's Code. | Confirmed | Corroborated | High | P1, P2, S2, T1 |
| TE-002 | One tetromino translates and rotates under ordinary gravity. Collisions bound the legal pose. Ground contact permits a finite adjustment window. Soft drop accelerates descent and hard drop commits the landing. | Observation | Corroborated | High | P2, S1, S3, T1 |
| TE-003 | A visible queue previews future shapes. Hold stores one shape and replaces the active one from the queue or the previous reserve. The landing outline shows a candidate lock pose on the current stack. | Observation | Corroborated | High | P2, S1, S3 |
| TE-004 | The documented Guideline piece stream permutes the seven shapes per bag. Rotation tries ordered candidate offsets when the rotated piece would otherwise overlap. Exact release code, frame timings and offset tables are not established. | Observation | Corroborated | Medium | P3, S3, T1, T2 |
| TE-005 | A normal full row is removed on lock and the retained rows above shift down. It credits the stage and can charge Zone. The Deep increases ordinary fall speed as stage lines accumulate. | Observation | Corroborated | High | P1, P2, S2, S3, T1 |
| TE-006 | Sufficient normal line credit enables voluntary Zone. While active, natural descent is suspended but manually moving and dropping pieces remains possible. More gauge charge provides a longer interval. | Observation | Corroborated | High | P1, P2, P3, S1, T1 |
| TE-007 | Completed rows in Zone move to the bottom and stay occupied. They support later placements. At Zone exit the collected rows disappear and their settlement yields score without credit toward the stage quota. | Observation | Corroborated | High | P2, S1, S2, S3 |
| TE-008 | Zone exit can follow timer exhaustion or pressure at the playable ceiling. The latter first settles stored rows, which can provide space to resume. An unrelieved ordinary entry obstruction ends the attempt. | Observation | Corroborated | High | P2, S1, T1 |

## Basic data

- Release / origin: Enhance and development partners Monstars and Resonair,
  North American PS4 launch, 9 November 2018.
- Families: spatial assembly and packing, and real-time system pressure.
- Sources accessed 2026-11-17:
  - **P1** — [Enhance launch announcement](https://www.tetriseffect.game/2018/11/09/tetris-effect-now-available-on-playstation4-worldwide/).
    The heading, North American product identifier and Journey section
    establish the platform, release identity and settings. The [original
    announcement](https://blog.playstation.com/?p=201748) introduces Zone
    in the contemporary PS4 product.
  - **P2** — [PlayStation's launch-day play account](https://blog.playstation.com/?p=205477),
    sections “Line ’em Up”, “Know What’s Next” and “Zone Out”. The
    [earlier first-hand demonstration account](https://blog.playstation.com/?p=202354)
    identifies voluntary meter use and cessation of gravity, with its
    prerelease control button assignment treated as provisional.
  - **P3** — [Enhance-hosted beginner's community guide](https://www.tetriseffect.game/beginners-community-guide/).
    The shared control glossary and Journey Zone sections support the
    reconstruction. Connected-only cases do not enter the scope.
  - **S1** — [Ars Technica's 2018 original PS4 review](https://arstechnica.com/gaming/2018/11/tetris-effect-uses-vr-to-drop-puzzle-pieces-directly-into-your-brain/),
    Journey controls, deferred removal, expiry and ceiling relief.
  - **S2** — [Chalgyr's contemporary Normal PS4 play account](https://www.chalgyr.com/2018/11/Review-PS4-TetrisEffect.html),
    36-row Normal quota, faster sections and Zone row order.
  - **S3** — [Meristation's original PS4 play account](https://as.com/meristation/2018/11/12/analisis/1542057533_712319.html),
    retained occupancy between stages, reserve, post-contact movement and
    accumulation before Zone expiry.
  - **T1** — [TetrisWiki's Tetris Effect entry](https://www.tetris.wiki/Tetris_Effect)
    and the [Hard Drop speed table](https://harddrop.com/wiki/Tetris_Effect).
    Used for first-stage order, cadence and Zone distinctions. Both
    include later modes, which are outside this record.
  - **T2** — [Guideline differences by game](https://tetris.wiki/Guideline_compliant_game_differences).
    The Tetris Effect column supports the common seven-bag and rotation
    behaviour without certifying exact original implementation.
- Claim IDs: TE-001–TE-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-005`: choose a new legal orientation or transverse
  coordinate for the active tetromino.
- Reuse `ACT-006`: accelerate descent with soft drop during the live loop.
- New `ACT-722`: send the active tetromino to the lowest collision-valid
  position on its present straight descent path and commit it immediately.
- New `ACT-723`: store the current shape in the single Hold reserve,
  taking the queue head if the reserve was empty or the previous reserved
  shape otherwise. A second Hold before placement is ineligible.
- New `ACT-724`: request Zone after enough ordinary rows have charged the
  gauge. The player chooses when to activate the available interval.
- Claim IDs: TE-002, TE-003, TE-006.

### System Behaviour Genes

- Reuse `SYS-004`: the bag sets the bounded variety of the pseudorandom
  piece sequence. The reported seven-shape permutation is a selection
  parameter. A bag boundary permits consecutive copies of a shape.
- Reuse `SYS-006`, `SYS-007`, `SYS-009`: the ordinary clock pushes the
  active shape down. Continued blocked descent fixes it after finite lock
  delay. The next scheduled shape enters after settlement.
- Reuse `SYS-008`: remove and collapse completed rows as part of ordinary
  lock settlement. The ordinary loop remains present even when the timed
  replacement rule is available.
- New `SYS-1520`: trade accumulated ordinary line clears for a temporary
  suspension of automatic fall while keeping manual placement live.
  Charge supplies a duration and is consumed by that use. Expiry or
  ceiling pressure ends the special interval.
- New `SYS-1521`: move complete rows to a contiguous occupied band at the
  bottom during Zone. Those rows still support the stack. End the mode by
  removing the band and adding its scoring benefit without advancing the
  ordinary objective count.
- New `SYS-1522`: a rotation can use the first passing candidate of an
  ordered offset search. If none fits, the old pose persists.
- Claim IDs: TE-002, TE-004–TE-008.

### Constraint Genes

- Reuse `CON-001`, `CON-007`: the visible well has 10 columns and 20
  rows. Each attempted post-rotation, drop or movement pose must respect
  available board space and occupied tiles.
- Reuse `CON-008`: ordinary obstruction that prevents the new active
  piece from entering terminates the attempt. Ceiling pressure during
  Zone instead first invokes the temporary mode's settlement.
- Reuse `CON-440`: access to the authored next stage requires accumulated
  qualifying rows within the current stage. Zone rows are ineligible.
- Claim IDs: TE-001, TE-002, TE-005, TE-007, TE-008.

### Information Genes

- Reuse `INF-001`, `INF-005`: show the settled well, active shape and
  current resources, and disclose an ordered exact future piece queue.
  Its visible depth is an option, not a gene. Hold is a reserved piece
  and may change which queued piece gets played first.
- New `INF-514`: the ghost outline projects the current shape's nearest
  valid downward stopping pose along its straight path. It moves when
  the active pose changes and has no occupancy.
- Claim IDs: TE-002, TE-003, TE-006, TE-007.

### Objective Genes

- Reuse `OBJ-007`: clear the required count of qualifying board rows
  to finish this Normal stage. The target is a count of events, so it
  does not require ending with an empty well.
- Reuse `OBJ-002` and `OBJ-003`: build score and preserve entry room
  until the finite goal settles. A Zone placement can advance score or
  recover space without advancing the quota.
- Claim IDs: TE-001, TE-005, TE-007, TE-008.

### Time Genes

- Reuse `TIM-003`: normal input competes with automatic descent and lock
  timing. Zone removes ordinary airborne descent for its interval while
  the interval itself still drains. It is not a menu pause, nor a return
  to an earlier state.
- Claim IDs: TE-002, TE-005, TE-006, TE-008.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Active piece has an open drop path | Move one column and hard drop | The projected stopping pose updates, then the piece fixes at the last legal pose in that column | Landing information previews a distinct placement action | TE-002, TE-003 |
| Reserve empty and Hold available | Press Hold twice without settling the new piece | First press stores the active shape and introduces the queue head. The second press does not cycle the reserve again. | Hold reallocates one shape before placement | TE-003, TE-004 |
| Rotated footprint collides but an ordered offset fits | Request rotation | First eligible offset becomes the orientation's position. With no eligible offset the old pose persists. | A blocked first candidate does not imply that rotation always fails | TE-002, TE-004 |
| One ordinary row is incomplete under the charge threshold | Lock the missing cells into place | Completed row disappears, higher occupancy shifts down and the ordinary count increments. The gauge gains qualifying credit. | Normal placement restores capacity immediately | TE-005, TE-006 |
| Zone is ready and the ordinary bar is short of its goal | Activate Zone and finish a row from a legal gap | Without automatic descent, manual placement completes the row and moves it into the bottom band. The stage count stays fixed. | Deferral preserves occupied capacity until exit | TE-006, TE-007 |
| Zone has completed rows at the foot of the well | Let the finite interval finish or reach its ceiling exit | The bottom band is removed and the well settles. Zone adds score and the stage count has no credit from the band. | The end of Zone can restore headroom without paying the stage gate | TE-007, TE-008 |
| Normal stage at 35 credited rows | Clear a row outside Zone | The stage quota is met and the presentation hands off to Pharaoh's Code. | Ordinary progress releases the authored successor | TE-001, TE-005 |

## Strategic and experiential structure

Choose between clean immediate clearance, shaping a narrow well for a later
piece, and spending Zone to rescue a risky stack or accumulate score. The
ordinary speed change makes it costly to postpone work. Zone temporarily
reduces that input pressure but raises the effective floor each time a row
joins the retained band. A player seeking simple progress can omit Zone.
For a score attempt, the withheld quota credit permits more placements in
the stage. Releasing Zone can reopen space before the next piece settles.

## Replay and variation

- The randomized bag order, placements, reserve commitments and use of Zone
  change the board and score between attempts. The Normal target and first
  stage order remain fixed.
- Compare a normal clear with the same fill inside a charged Zone. Move
  a ghost-marked piece horizontally before hard drop to compare the two
  legal landing poses.
- Claim IDs: TE-001, TE-002, TE-004–TE-008.

## Adjacent systems and history

- The original PS4 game applies a limited gravity and row-settlement
  intervention to the already established falling-block loop. The visual
  soundtrack response accompanies placement. There is no requirement for
  play on a beat in this scope.
- The later Connected modes use different shared fields, opponents or
  charge schedules. Their rules do not transfer to this packet.
- Claim IDs: TE-001, TE-005–TE-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-005`, `ACT-006`, `ACT-722`, `ACT-723`, `ACT-724` | movement, rotation, soft and hard drop, Hold, Zone request |
| System Behaviour | `SYS-004`, `SYS-006`, `SYS-007`, `SYS-008`, `SYS-009`, `SYS-1520`, `SYS-1521`, `SYS-1522` | bag, ordinary fall and lock, row collapse, successor, Zone spend and settlement, rotation offsets |
| Constraint | `CON-001`, `CON-007`, `CON-008`, `CON-440` | well size, collision, entry obstruction, 36-row gate |
| Information | `INF-001`, `INF-005`, `INF-514` | seen board and gauges, next queue, landing outline |
| Objective | `OBJ-002`, `OBJ-003`, `OBJ-007` | score, headroom, ordinary rows |
| Time | `TIM-003` | fall speeds, contact window, Zone interval |

Canonical signature:

`ACT-005,ACT-006,ACT-722,ACT-723,ACT-724; SYS-004,SYS-006,SYS-007,SYS-008,SYS-009,SYS-1520,SYS-1521,SYS-1522; CON-001,CON-007,CON-008,CON-440; INF-001,INF-005,INF-514; OBJ-002,OBJ-003,OBJ-007; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `528` (`GAME-0001`–`GAME-0528`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`15 / 24 = 0.625000`).
- Supported combination subsets: `COMB-0004`.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0004` — Tetris | `ACT-005`, `ACT-006`, `CON-001`, `CON-007`, `CON-008`, `INF-001`, `INF-005`, `OBJ-002`, `OBJ-003`, `SYS-004`, `SYS-006`, `SYS-007`, `SYS-008`, `SYS-009`, `TIM-003` | Both place one temporary piece into a collision-bound falling well. NES A-Type credits and removes a completed row in ordinary play and ends at top-out. Tetris Effect adds a finite Normal quota, reserve and landing controls, and an optional charged Zone that moves completed rows to the floor and settles them for score separately from the quota. | Tied near (`0.625000`) |

### Preserved research notes

- New genes: `ACT-722`–`ACT-724`, `SYS-1520`–`SYS-1522`, `INF-514`.
- Classification result: `New gene`.
- Evidence and reasoning: the ordinary lock, collapse and entry sequence
  already supports `COMB-0004`. The timed replacement has a separate boundary:
  the same fill predicate goes to a different temporary occupied state
  and a different credit path inside Zone.

## Taxonomy impact

- Registry changes: seven Active additions and seventeen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_276](../../../research/taxonomy-changes/TAXONOMY_CHANGE_276.md).

## Negative results

- The ordinary game loop already matches the verified timed falling-block
  combination. One scoped witness does not establish wider support for
  a separate Zone combination.
- Available sources do not establish the exact frame on which Zone exits
  relative to the last lock in the original executable.

## Delta summary

## New facts

- [Observation | Corroborated | High] Ordinary and Zone rows have the same
  full-row predicate. Zone changes where they reside, when they are
  removed and which counter receives credit.

## New genes

- [Observation | Corroborated | High] Hard drop, reserve swap, Zone
  activation, gravity suspension, deferred row settlement and projected
  landing are isolated. The ordered rotation correction is Corroborated /
  Medium for the original release.

## New combinations

- [Observation | Corroborated | High] Reuses `COMB-0004` during ordinary
  play. No new proposed combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_276`.

## New questions

- Does the original executable settle an exhausted Zone immediately or
  wait for the next piece lock in every relevant state?

## Next recommended game

- [Hypothesis | Limited | Medium] Original North American Xbox 360
  *Lost Odyssey*.
- Optimisation criterion: compare real-time input inside a turn-based
  command flow with timing pressure from automatic descent in Tetris Effect.
- Backlog impact: advance Selection 041 to its eighth candidate.

## Why this game

- [Hypothesis | Limited | Medium] Moving row settlement into a limited
  manually triggered interval changes both survival and score decisions
  while preserving the ordinary placement cycle as a direct comparison.
