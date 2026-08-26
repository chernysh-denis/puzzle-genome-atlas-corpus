---
game_id: GAME-0032
slug: spacechem
game_title: SpaceChem
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0032
gene_ids:
  action:
    - ACT-046
  system:
    - SYS-038
    - SYS-040
    - SYS-058
  constraint:
    - CON-001
    - CON-063
  information:
    - INF-001
    - INF-011
  objective:
    - OBJ-015
    - OBJ-016
  time:
    - TIM-006
---

# Game: SpaceChem

## Analysis scope

- Version / ruleset: the original 2011 game, scoped to one ordinary single-
  reactor production puzzle after red and blue waldos, input / output, grab /
  drop, rotate, bond / unbond and sync symbols are available.
- Included: fixed reactor grid; drawing both waldo routes; placing colour-coded
  instructions; recurrent reagent input; automatic simultaneous waldo cycles;
  grab, drop and rotate; explicit bond / unbond activation at bonder geometry;
  synchronization waits; collisions and invalid output; repeated exact-product
  quota; reset / revise; cycles and symbol metrics.
- Excluded: narrative, progression, multi-reactor production maps, sensors,
  fusion, fission, teleporters, defence / boss stages, ResearchNet, challenges,
  achievements, exploits and platform-specific controls.
- Direct-play status: not conducted. Creator documentation and postmortem are
  combined with an academic mechanical account and contemporary reviews; exact
  advanced cycle-order edge cases remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SPC-001` | The puzzle discloses supplied reagent structures, required product structures and the finite reactor grid before programming begins | Confirmed | Corroborated | High | P1, P2, A1, S2 |
| `SPC-002` | The player draws separate red and blue waldo routes and places colour-matched commands directly on addressed reactor cells | Confirmed | Direct | High | P2, A1, S1, S2 |
| `SPC-003` | Starting the reactor makes both waldos advance one shared cycle at a time, execute encountered symbols and loop automatically | Confirmed | Corroborated | High | P2, A1, S1, S2 |
| `SPC-004` | A sync pair holds the first arriving waldo until the other reaches its matching synchronization point | Confirmed | Corroborated | High | S1, S2 |
| `SPC-005` | Input instructions request recurring reagents and output instructions remove and credit only a molecule satisfying the declared product schema | Confirmed | Corroborated | High | P1, P2, A1, S2 |
| `SPC-006` | Bond or unbond resolution requires an explicit waldo instruction while eligible atoms occupy bonder geometry | Confirmed | Corroborated | High | A1, S1, S2 |
| `SPC-007` | Incompatible atom overlap, wall contact or an invalid output halts the current run and requires program revision | Confirmed | Corroborated | High | S2, S3 |
| `SPC-008` | Completion requires the same cyclic program to deliver the correct product repeatedly until the production quota is met | Confirmed | Direct | High | P1, P2, S2, S3 |
| `SPC-009` | Editing is self-paced and separated from a deterministic automatic test that may be stopped or reset before revision | Confirmed | Corroborated | High | P2, A1, S2 |
| `SPC-010` | Successful solutions are compared by independent cycles and symbols measurements; broader production assignments also report reactor count | Confirmed | Corroborated | High | A1, S1, S2 |
| `SPC-011` | Multiple programs can satisfy the same exact input/output requirement without one prescribed route | Confirmed | Corroborated | High | P1, A1, S1 |
| `SPC-012` | SpaceChem and Opus Magnum share a resettable exact-output cyclic execution core but differ in how the player authors motion and transformation | Confirmed | Corroborated | High | SPC-001–SPC-011, OPM-001–OPM-013 |

## Basic data

- Release / origin: Zachtronics released SpaceChem in 2011.
- Platform or physical form: two-dimensional fixed-grid visual-programming
  editor and deterministic parallel reactor simulator.
- Puzzle family: spatial-path molecular production programming.
- Creator sources:
  - **[P1]** [Zachtronics — SpaceChem](https://www.zachtronics.com/spacechem/),
    defining machine construction, raw-material transformation and production
    quotas.
  - **[P2]** [Zach Barth's SpaceChem postmortem](https://www.gamedeveloper.com/design/postmortem-zachtronics-industries-i-spacechem-i-),
    documenting the minimum input / grab / arrows / drop / output program loop
    and the programmable red / blue waldos.
- Academic mechanical account:
  - **[A1]** [Falmouth University — SpaceChem](https://repository.falmouth.ac.uk/3378/1/SpaceChem_accepted.pdf),
    describing grid instruction placement, play-triggered waldo execution,
    input areas, grab / drop, bond and exact output deposition, plus cycles,
    symbols and reactor metrics.
- Contemporary and reference corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/spacechem-review/),
    documenting paired circuits, spin / bond / grab / drop and waldo sync.
  - **[S2]** [MobyGames mechanical summary](https://www.mobygames.com/game/50963/spacechem/),
    describing the 10-by-8 reactor, repeated programs, output targets, waldo
    synchronization and iterative test / redesign.
  - **[S3]** [SpaceChem gameplay reference](https://en.wikipedia.org/wiki/SpaceChem#Gameplay),
    used only to corroborate atom / wall collision halt, wrong-output failure,
    topological product equivalence and quota completion.
- Claim IDs: `SPC-001`–`SPC-012`.

## Mechanical decomposition

### Action Genes

- `ACT-046` — edit spatial controller route and instruction field. The player
  draws a colour-specific path through addressed reactor cells and places,
  changes or removes the red / blue commands executed when its waldo reaches
  those positions.
- `ACT-029` is absent: SpaceChem's instruction address is a world cell reached
  through the authored route, not a cycle column on a separate per-mechanism
  tape. Route geometry and command order are one edited object.
- `ACT-028` is absent: the scoped reactor's ports, bonders and grid are fixed;
  the player authors controller programs rather than placing persistent machine
  components with physical footprints.
- Claim IDs: `SPC-002`, `SPC-009`.

### System Behaviour Genes

- `SYS-038` — synchronous cyclic symbolic-program execution. Both waldos read
  their current spatial program positions in a shared discrete cycle, execute
  compatible commands, advance and repeat without editing during the run; sync
  explicitly aligns them.
- `SYS-040` — recurrent reagent-source and exact-product sink processing.
  Input commands request declared molecules when the input zone is clear;
  output consumes and credits only a product matching the declared schema.
- `SYS-058` — instruction-triggered geometry-validated molecular
  transformation. An encountered bond / unbond command changes eligible bonds
  only when atoms occupy the required bonder positions.
- `SYS-039` is absent: geometry alone does not trigger a passive placed glyph;
  one waldo must execute the explicit transformation instruction.
- Resolution order: both colour programs expose their current commands; sync
  waits are resolved; compatible motion / grab / drop / rotate and reactor
  commands apply in the deterministic cycle order; collision and output
  validity are checked; control advances to the next routed cells.
- Claim IDs: `SPC-003`–`SPC-008`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The reactor exposes a persistent
  10-by-8 set of addressed cells on which colour routes and instruction symbols
  are authored and through which carried molecules must fit.
- `CON-063` — kinematic-conflict execution halt. A molecule intersecting
  another molecule or reactor wall invalidates and stops the automatic test;
  conflicting carried motion must be redesigned.
- `CON-062` is absent: route symbols are allowed program state on fixed cells,
  not separately anchored machine components subject to pairwise footprint
  compatibility.
- Scarce strategic resources: grid cells, unoccupied molecular trajectories,
  available bonders, safe shared-cycle timing and instruction count for an
  efficient solution.
- Claim IDs: `SPC-001`, `SPC-002`, `SPC-007`, `SPC-010`.

### Information Genes

- `INF-001` — fully visible current state. Routes, symbols, waldo positions,
  atoms, bonds, input / output areas and the faulting state are inspectable.
- `INF-011` — exact visible reagent-product specification. Input diagrams and
  required atom / bond schemas are disclosed before editing; SpaceChem product
  acceptance uses graph equivalence rather than requiring one screen
  orientation.
- The scoped reactor is deterministic and has no hidden successor input.
- Claim IDs: `SPC-001`, `SPC-005`, `SPC-009`.

### Objective Genes

- `OBJ-015` — repeatedly produce exact target assembly. One uninterrupted
  valid cyclic program must submit the specified molecule until the declared
  shipment quota is complete.
- `OBJ-016` — minimise independent solution resource metrics. After functional
  success, cycles and placed symbols provide distinct optimisation directions;
  reactor count is an additional metric outside the single-reactor scope.
- Claim IDs: `SPC-008`, `SPC-010`, `SPC-011`.

### Time Genes

- `TIM-006` — editable design before resettable automatic run. Path and command
  editing are untimed; pressing play commits the program to deterministic
  multi-cycle execution until quota completion, stop, reset or fault, after
  which the design can be revised.
- This is not `TIM-008`: the player cannot seek to an arbitrary prospective
  cycle and edit commands inside the active history.
- Claim IDs: `SPC-003`, `SPC-007`–`SPC-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty reactor program with fixed ports and bonders | Draw a red loop and place input, grab, arrows, drop and output symbols on its cells | Persistent program state changes; no molecule moves before play | spatial-path program editing differs from component placement and execution | `SPC-002`, `SPC-009` |
| Red and blue routes contain commands | Press play or step | Both waldos execute their current positions under one shared cycle and advance | programs resolve synchronously and cyclically | `SPC-003` |
| Red reaches its sync before blue | Advance cycles | Red waits until blue reaches its paired sync, then both continue | synchronization is an authored concurrency control | `SPC-004` |
| An input zone is clear when its colour executes Input | Advance that cycle | The declared reagent appears for pickup and later requests can supply further copies | source processing is recurrent, not finite inventory | `SPC-005` |
| Eligible atoms occupy bonder pads while a waldo reaches Bond | Advance that cycle | The permitted bond changes only because the instruction executes | transformation is command-triggered, unlike an Opus glyph | `SPC-006` |
| Carried molecule enters an occupied atom cell or wall | Advance the conflicting cycle | Reactor execution halts and the program remains available for revision | dynamic collision is a run-validity constraint | `SPC-007` |
| Correct product is dropped in the output zone and Output executes | Advance the cycle | Matching molecule is removed and credited; the loop continues for more copies | exact sink processing and repeated-production objective are separate | `SPC-005`, `SPC-008` |
| Quota is reached by an uninterrupted loop | Inspect completion result | Puzzle succeeds and cycles / symbols are reported independently | functional success does not impose one optimisation trade-off | `SPC-008`, `SPC-010`, `SPC-011` |

## Strategic and experiential structure

- Local decision: choose one route cell and colour instruction whose spatial
  position both orders the program and determines the waldo's physical access.
- Medium-term planning: coordinate two loops around shared bonders and molecule
  geometry, adding sync only where relative phase must be fixed.
- Long-term structure: return every cycle of production to a safe periodic
  state that accepts new reagents and emits quota products indefinitely.
- Common heuristics: make one slow valid loop, isolate red / blue duties, trace
  both cycles together, reserve clearance around rotations, then shorten paths
  or remove symbols.
- Failure attribution: visible deterministic stepping ties a crash, deadlock or
  wrong output to a route, symbol, phase relation or molecular shape.
- Player-trust factors: simultaneous ordering, sync release, carried-molecule
  rotation, bonder selection, output equivalence and collision sampling must be
  consistent between step and full-speed execution.
- Claim IDs: `SPC-001`–`SPC-012`.

## Replay and variation

- What changes between puzzles: reagent / product schemas, enabled commands,
  fixed reactor features and any advanced operators excluded from this scope.
- Randomness or procedural generation: none in the scoped reactor or run.
- Multiple viable strategies: red / blue division of labour, loop topology,
  sync positions, temporary storage and metric trade-offs can differ.
- Typical replay motive: reduce cycles or symbols, remove fragile
  synchronization or redesign for clarity after first quota completion.
- Claim IDs: `SPC-001`, `SPC-004`, `SPC-010`, `SPC-011`.

## Adjacent systems and history

- Opus Magnum shares synchronized cyclic programs, recurrent exact ports,
  collision faults, visible schemas, repeated output, metric optimisation and
  edit-before-run time. It spatially places mechanisms and writes separate
  time-row commands; SpaceChem writes route and commands into the same finite
  grid and explicitly invokes bond transformations.
- Pipe Dream also authors a route for automatic material flow, but the supplied
  queue is committed one piece at a time during live progression and no paired
  symbolic controllers manufacture an exact repeated assembly.
- Timelie edits commands for moving actors on a random-access timeline; it
  permits revision inside simulated history rather than resetting a fixed
  cyclic production program.
- Claim IDs: `SPC-001`–`SPC-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-046` | spatial route and colour-command editing |
| System Behaviour | `SYS-038`, `SYS-040`, `SYS-058` | cyclic execution, ports and instructed bonding |
| Constraint | `CON-001`, `CON-063` | finite reactor grid and collision halt |
| Information | `INF-001`, `INF-011` | current state and exact schemas |
| Objective | `OBJ-015`, `OBJ-016` | repeated quota and cycles / symbols metrics |
| Time | `TIM-006` | self-paced edit, committed run and reset |

Canonical signature:

`ACT-046; SYS-038,SYS-040,SYS-058; CON-001,CON-063; INF-001,INF-011; OBJ-015,OBJ-016; TIM-006`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `31` (`GAME-0001`–`GAME-0031`).
- Exact genome matches: none.
- Tied near matches: `GAME-0022` — Opus Magnum (`8 / 15 = 0.533333`).
- Supported combination subsets: `COMB-0032`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0022` — Opus Magnum | `SYS-038`, `SYS-040`, `CON-063`, `INF-001`, `INF-011`, `OBJ-015`, `OBJ-016`, `TIM-006` | spatial route-program and explicit bond commands on a finite grid versus placed mechanisms, separate temporal tapes and passive transformation glyphs | Near, `0.533333` |

### Preserved research notes

- New genes: `ACT-046`, `SYS-058`.
- Classification result: `New gene` and the first cross-game verified
  combination.
- Evidence and reasoning: nine boundaries recur cleanly. Spatial route-command
  authoring and instruction-triggered bonding remain decision-relevant
  differences rather than parameters of Opus component layout or passive glyphs.

## Combination record

- Registered [`COMB-0032`](../../combinations/COMB-0032.md), the six-gene
  resettable exact-output cyclic-production core supported by both SpaceChem
  and Opus Magnum.
- This does not weaken or replace `COMB-0022`: that combination continues to
  require Opus Magnum's spatial component configuration and separate mechanism
  tapes, which SpaceChem does not instantiate.
- `COMB-0032` is the corpus's first verified combination with two complete game
  supporters.

## Taxonomy impact

- Registry changes: two stable genes added; nine existing genes reused.
- `SYS-038` is renamed from tape-specific to symbolic-program execution and
  its wording generalised to cover temporal rows or spatial routed programs;
  its shared-cycle and cyclic-execution boundary is unchanged.
- `INF-011`, `SYS-040` and `OBJ-015` gain product-schema parameters for
  topological equivalence without changing their exact-output boundaries.
- Taxonomy-change record: none; no prior classification or lifecycle changes.

## Negative results

- `ACT-028` and `CON-062` are absent because fixed reactor features are not
  placed machine components.
- `ACT-029` is absent because grid position and controller route determine
  command order instead of a separate addressed time row.
- `SYS-039` is absent because bonder geometry requires an explicit waldo
  instruction rather than passively transforming any eligible occupant.
- `COMB-0022` does not recur in full. A new shared execution subset is recorded
  separately instead of weakening the older authored-machine combination.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] SpaceChem authors red / blue cyclic programs as
  routes and commands on one fixed grid, then repeatedly manufactures an exact
  output quota (`SPC-001`–`SPC-008`).
- [Confirmed | Corroborated | High] It shares a six-gene execution core with
  Opus Magnum while preserving distinct authoring and transformation mechanics
  (`SPC-006`, `SPC-009`–`SPC-012`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-046` and `SYS-058`; reused
  nine existing genes.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0032` is the first combination
  verified across two analysed games: SpaceChem and Opus Magnum.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; `SYS-038` wording
  is representation-neutral while its synchronized cyclic boundary is retained.

## Нові питання

- Does the new cross-game combination justify a focused audit of older
  combinations for stable shared cores before another long expansion sequence?
- Can Portal reuse physical transfer genes without inheriting autonomous
  population or continuous force-network structure?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `CHECKPOINT_032`.
- Optimisation criterion: audit the first six post-horizon games and the first
  cross-game combination before selecting `GAME-0033`.
- Expected information gain: measure singleton change, verify combination
  abstraction policy and decide whether normalisation or Portal should follow.
- Backlog impact: pause game selection for one bounded checkpoint; retain
  Braid, Portal and Pikmin 4.

## Чому саме вона

- [Hypothesis | Corroborated | High] Six games and two selection / normalisation
  decisions have materially changed reuse evidence since checkpoint 026; an
  audit now prevents the new shared-core precedent from silently weakening
  future combinations.
