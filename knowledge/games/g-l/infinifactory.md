---
game_id: GAME-0042
slug: infinifactory
game_title: Infinifactory
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0042
gene_ids:
  action:
    - ACT-028
  system:
    - SYS-040
    - SYS-077
  constraint:
    - CON-062
  information:
    - INF-001
    - INF-011
  objective:
    - OBJ-015
    - OBJ-016
  time:
    - TIM-006
---

# Game: Infinifactory

## Analysis scope

- Version / ruleset: the released 2015 base game, scoped to Proving Grounds
  `1-1: Training Routine 1`, the first ordinary factory exercise whose recorded
  solution catalogue uses conveyors as its most advanced factory component.
- Included: fixed input hatch and output area; disclosed input and target voxel
  assemblies; first-person inspection of the workspace; placement, orientation,
  selection, movement and deletion of conveyor / structural blocks; recurring
  input; discrete conveyor transport; start, pause, stop and reset; exact output
  acceptance; ten-output completion; and cycles, footprint and block-count
  evaluation.
- Excluded: welders, rotators, lifters, pushers, blockers, sensors, counters,
  conduits, eviscerators, lasers, teleporters and every later puzzle-specific
  device; campaign progression, narrative, secrets, achievements, sandbox,
  level editor, Workshop, social leaderboards and speedrunning.
- Direct-play status: not conducted. Creator and developer-published material
  establish factory design / execution and optimisation; contemporary reviews
  establish fixed-rate inputs, schemas, conveyors, ten outputs and metrics;
  community level records bound Training Routine 1 to conveyor-only solutions.
  Exact obscure conveyor-priority ties remain parameters rather than claims.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `INFY-001` | Training Routine 1 supplies a fixed input arrangement, target output arrangement and output area inside a persistent 3D workspace | Confirmed | Corroborated | High | P1, S1–S4 |
| `INFY-002` | The player authors the factory by placing, orienting, moving or deleting persistent voxel components before execution | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `INFY-003` | The scoped puzzle can be solved with conveyor and structural blocks; no symbolic controller tape or routed command token is authored | Observation | Corroborated | High | S4, S5 |
| `INFY-004` | During a run, placed conveyors repeatedly move contacting input assemblies in their oriented directions on discrete cycles | Confirmed | Corroborated | High | S1–S3, C1 |
| `INFY-005` | Input hatches emit the declared material repeatedly at a fixed rate and the output accepts only the declared arrangement and orientation | Confirmed | Corroborated | High | S1–S3 |
| `INFY-006` | Completion requires ten accepted target outputs from the same running factory | Confirmed | Direct | High | S3 |
| `INFY-007` | Editing is self-paced and separated from a pausable, stoppable and resettable automatic test run | Confirmed | Corroborated | High | P1, S1, S2, C2 |
| `INFY-008` | A blocked or conflicting conveyor transfer can stall material without acting as the symbolic-program collision halt used by Opus Magnum and SpaceChem | Observation | Limited | Medium | C1, C2 |
| `INFY-009` | A successful solution is evaluated independently by cycles, horizontal footprint and placed factory-block count | Confirmed | Corroborated | High | P1, S3–S5 |
| `INFY-010` | Current components, moving material, target schema and execution state are visible; no scoped random transition changes them | Observation | Corroborated | High | S1–S4 |
| `INFY-011` | First-person jetpack movement changes the editing viewpoint but is not itself a level-completion route or material command | Observation | Corroborated | High | S1, C2 |
| `INFY-012` | The scoped factory shares a spatially configured exact-output core with Opus Magnum but not the symbolic cyclic-program core of `COMB-0032` | Observation | Corroborated | High | INFY-001–INFY-011 |

## Basic data

- Release / origin: Zachtronics developed and published Infinifactory on
  30 June 2015.
- Platform or physical form: digital first-person three-dimensional voxel
  construction editor and deterministic factory simulator.
- Puzzle family: spatial automation and repeated exact-output production.
- Primary and creator sources:
  - **[P1]** [developer-published Steam listing](https://store.steampowered.com/app/300570/Infinifactory/),
    identifying Zachtronics, the release, first-person 3D factory design / run,
    product assembly and optimisation histograms.
  - **[P2]** [Zachtronics — Infinifactory](https://www.zachtronics.com/infinifactory/),
    the creator's canonical product page.
- Contemporary and mechanical corroboration:
  - **[S1]** [PC Gamer review, 3 July 2015](https://www.pcgamer.com/infinifactory-review/),
    documenting block placement, fixed-rate inputs, target schematics,
    first-person jetpack inspection and consistent simplified physics.
  - **[S2]** [PCGamesN impressions, 21 January 2015](https://www.pcgamesn.com/infinifactory/here-are-my-impressions-of-infinifactory-please-trust-them),
    documenting placed conveyors, automated assembly lines, reliable output and
    multiple valid layouts.
  - **[S3]** [Gold-Plated Games review](https://goldplatedgames.com/2017/08/03/review-infinifactory/),
    documenting recurring hatches, exact output platforms, conveyors, ten
    required products and solution evaluation by speed and space.
  - **[S4]** [Training Routine 1 specialist record](https://infinifactory.fandom.com/wiki/Training_Routine_1),
    identifying the scoped level and its cycles, footprint and blocks metrics.
  - **[S5]** [archived solution-score catalogue](https://gist.github.com/madewokherd/119b19529293ce2a4f0c26195b5f751e),
    a community reproducibility artefact listing conveyor-only Training Routine
    1 solutions and all three metric values.
- Bounded community rule checks:
  - **[C1]** [conveyor-force discussion](https://steamcommunity.com/app/300570/discussions/0/523890681403417436/),
    used only for the opposed-conveyor stall boundary.
  - **[C2]** [general mechanics summary](https://en.wikipedia.org/wiki/Infinifactory),
    used only to corroborate unlimited setup time, free viewpoint movement,
    start / pause inspection and resettable fault checking.
- Claim IDs: `INFY-001`–`INFY-012`.

## Mechanical decomposition

### Action Genes

- `ACT-028` — configure spatial machine layout. The player places, orients,
  relocates and deletes persistent conveyor / support voxels whose geometry
  determines later material motion.
- `ACT-029` is absent: the scoped factory has no per-mechanism addressed
  instruction row. `ACT-046` is absent: conveyor positions are machine
  components, not a routed program cursor carrying command symbols.
- Jetpack travel and viewpoint rotation are editor navigation parameters. They
  expose placement positions but do not pursue a world destination, so
  `ACT-008` is absent.
- Claim IDs: `INFY-002`, `INFY-003`, `INFY-011`.

### System Behaviour Genes

- `SYS-040` — recurrent input-source and exact-product sink processing. The
  hatch repeatedly emits its declared assembly and the output region consumes
  and credits only the accepted target geometry / orientation.
- `SYS-077` — discrete contact-driven conveyor transport. During each running
  cycle, powered conveyor faces contribute translation to contacting material;
  a compatible assembly advances while a blocked or opposed transfer stalls.
- `SYS-038` is absent because no programmed controller reads or repeats a
  temporal or spatial symbol sequence. Repeated physical component behaviour
  is not by itself a symbolic cyclic program.
- `SYS-039` is absent because Training Routine 1 performs transport only; the
  later weld / cut / rotate catalogue is outside scope.
- Resolution order at the claimed boundary: make a recurring input available;
  evaluate conveyor contact and compatible translation for the current cycle;
  preserve blocked material; test an assembly occupying the output zone
  against the disclosed schema; consume and credit a match; repeat until the
  quota is met or the player stops / resets.
- Claim IDs: `INFY-004`–`INFY-008`.

### Constraint Genes

- `CON-062` — static machine-footprint placement compatibility. A persistent
  factory voxel cannot be committed inside an incompatible existing component,
  immutable hatch, output device or fixed environment footprint.
- `CON-063` is absent. The scoped conveyor run need not halt as an invalid
  symbolic program when material is blocked; stalled bodies expose a layout
  problem while the simulation can remain active.
- `CON-001` is absent: ordinary factory construction is not a fixed finite set
  of persistent board cells, and sources explicitly describe plentiful space
  and no component-count cap. Voxel addressability alone is insufficient.
- Scarce strategic resources are not hard budgets: path clearance and spacing
  affect function, while footprint and block count evaluate an already valid
  solution.
- Claim IDs: `INFY-001`, `INFY-002`, `INFY-008`, `INFY-009`.

### Information Genes

- `INF-001` — fully visible current state. The authored components, input,
  moving assemblies, target diagram, output count and run state are inspectable.
- `INF-011` — exact visible input-output assembly schema. Before construction,
  the puzzle discloses acceptance-relevant voxel identities, relative geometry
  and orientation of the supplied and requested assemblies.
- The target schematic is not hidden-state deduction and the deterministic run
  does not add an uncertainty gene.
- Claim IDs: `INFY-001`, `INFY-005`, `INFY-010`.

### Objective Genes

- `OBJ-015` — repeatedly produce exact target assembly. One persistent factory
  must deliver ten accepted copies during a valid run.
- `OBJ-016` — minimise independent solution resource metrics. After functional
  success, cycles, horizontal footprint and placed factory-block count are
  separate improvement axes rather than one mandatory aggregate score.
- One correctly placed output is insufficient for completion; a low-metric
  solution is not required for functional success.
- Claim IDs: `INFY-006`, `INFY-009`.

### Time Genes

- `TIM-006` — editable design before resettable automatic run. Layout editing
  is self-paced; starting the test locks component editing while the factory
  advances through multiple discrete cycles until completion, stop or reset.
- `TIM-002` is absent at whole-puzzle scope because a placement does not resolve
  one complete world step and return control; it authors a later run.
- `TIM-003` is absent because factory construction is unavailable while the
  automatic process advances; pause is inspection, not live layout editing.
- Claim IDs: `INFY-004`, `INFY-007`.

## Reproducible transitions

| Before | Action or event | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty editable space lies between hatch and output | Place and orient a conveyor voxel | Component persists, but no material moves while editing | layout authors future transport | `INFY-002` |
| Conveyor is oriented away from the required route | Rotate or replace it before running | Persistent direction changes with no immediate material transition | component orientation is part of `ACT-028` | `INFY-002`, `INFY-003` |
| A complete layout is visible | Start the factory | Editing locks and recurring discrete execution begins | design and automatic run are distinct | `INFY-007` |
| Input assembly contacts an unobstructed aligned conveyor | Advance one cycle | Assembly translates in the conveyor direction | transport comes from placed component geometry | `INFY-004` |
| Material is blocked or receives opposed conveyor movement | Advance execution | It does not complete the incompatible transfer; the factory may remain running | stall differs from `CON-063` program invalidation | `INFY-008` |
| Correct assembly enters the output in the accepted pose | Advance execution | Output is consumed and credited; another copy remains required | exact recurrent sink and quota | `INFY-005`, `INFY-006` |
| Wrong geometry or orientation reaches the output area | Advance execution | It is not credited as the target output | visible schema has operational acceptance force | `INFY-005` |
| Layout stalls before quota | Stop or reset, change conveyors, rerun | Initial execution state is restored and the revised layout is tested | deterministic iterative design loop | `INFY-007`, `INFY-008` |
| Tenth correct output is accepted | Inspect completion report | Puzzle succeeds and cycles, footprint and blocks are shown separately | success and optimisation are distinct | `INFY-006`, `INFY-009` |

## Strategic and experiential structure

- Local decision: orient one conveyor so the current rigid assembly advances
  without becoming blocked or diverted.
- Medium-term planning: embed a continuous 3D route between immutable input and
  output geometry while preserving clearance around every moving voxel.
- Long-term structure: make the same passive field accept a recurring stream
  indefinitely enough to reach the ten-product quota.
- Common heuristics: prove one product path first; inspect the run cycle by
  cycle; revise the first stalled location; then reduce redundant conveyors or
  fold vertical layers to improve metrics.
- Failure attribution: visible deterministic motion ties a missed output to
  direction, support, clearance, spacing or target orientation rather than
  random input.
- Player-trust factors: conveyor contact, opposed-force priority, rigid assembly
  occupancy, input cadence, output equivalence, pause / reset restoration and
  all three measurements must remain stable.
- Claim IDs: `INFY-001`–`INFY-010`.

## Replay and variation

- What changes between puzzles: input / target geometry, hatch and output
  placement, immutable scenery, available factory-block catalogue and later
  excluded transformation burden.
- Randomness or procedural generation: none in the scoped authored level or
  committed run.
- Multiple viable strategies: Training Routine 1 records materially different
  conveyor layouts trading cycles, footprint and block count.
- Typical replay motive: repair a failed path or optimise one measurement
  without accepting a single compulsory compromise score.
- Claim IDs: `INFY-001`, `INFY-007`, `INFY-009`, `INFY-010`.

## Adjacent systems and history

- Opus Magnum is the mathematical near match. Both disclose exact assemblies,
  let the player configure persistent spatial machinery, run a resettable
  recurrent source / sink process and evaluate multiple resource metrics.
  Opus additionally programs symbolic per-arm tapes, invokes molecular glyphs
  and halts on kinematic program conflicts.
- SpaceChem shares recurring exact ports, schemas, quota, metrics and the edit-
  then-run boundary. Its machine is a finite reactor with routed red / blue
  symbolic programs and explicit bond instructions; Infinifactory's conveyor
  field has no controller program counter.
- Pipe Mania places route pieces while a real-time flow continues, consumes a
  forced random queue and pursues distance / score rather than repeated exact
  structured output.
- Cosmic Express traces one simple route and commits a one-shot passenger run.
  It neither places reusable machine components nor cycles a source / product
  process.
- Claim IDs: `INFY-001`–`INFY-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-028` | conveyor / support catalogue, orientation and area-select editing |
| System Behaviour | `SYS-040`, `SYS-077` | input cadence, output equivalence and conveyor force priority |
| Constraint | `CON-062` | component / fixed-fixture footprint compatibility |
| Information | `INF-001`, `INF-011` | visible state and voxel input-output schema |
| Objective | `OBJ-015`, `OBJ-016` | ten outputs; cycles / footprint / blocks |
| Time | `TIM-006` | self-paced edit, committed run, pause / stop / reset |

Canonical signature:

`ACT-028; SYS-040,SYS-077; CON-062; INF-001,INF-011; OBJ-015,OBJ-016; TIM-006`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `41` (`GAME-0001`–`GAME-0041`).
- Exact genome matches: none.
- Tied near matches: `GAME-0022` — Opus Magnum (`8 / 13 = 0.615385`).
- Supported combination subsets: `COMB-0042`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0022` — Opus Magnum | `ACT-028`, `SYS-040`, `CON-062`, `INF-001`, `INF-011`, `OBJ-015`, `OBJ-016`, `TIM-006` | Infinifactory's passive 3D conveyor field has no separate symbolic tapes, molecular transformation glyphs or kinematic program-fault halt; it adds discrete contact-driven assembly transport | Near, `0.615385` |

### Preserved research notes

- New genes: `SYS-077`.
- Classification result: `New gene` and a new recurring combination of known
  genes.
- Evidence and reasoning: eight prior boundaries recur without erasing the
  central distinction between physical component fields and symbolic cyclic
  controllers. Conveyor transport is separately decision-relevant and lacks an
  existing System boundary.

## Combination record

- Registered recurring [`COMB-0042`](../../combinations/COMB-0042.md), the
  six-gene spatially configured exact-output factory core supported by Opus
  Magnum and Infinifactory.
- `COMB-0032` remains unchanged. It still requires symbolic cyclic execution
  and kinematic-conflict invalidation, neither of which is evidenced here.

## Taxonomy impact

- Registry changes: added `SYS-077`; reused eight existing genes.
- `INF-011`, `SYS-040` and `TIM-006` receive representation-neutral wording
  that explicitly includes voxel assemblies and layout-only machines. Their
  disclosed exact-schema, recurring port and separate resettable-run boundaries
  do not change, and no earlier signature is rewritten.
- `ACT-028`, `CON-062`, `OBJ-015` and `OBJ-016` gain a second or third analysed
  example without a definition change.
- Taxonomy-change record: none; no merge, split, lifecycle change or prior
  classification correction is required.
- Candidate terms affected: discrete contact-driven conveyor transport is
  promoted as `SYS-077`.

## Negative results

- `ACT-029`, `ACT-046` and `SYS-038` are rejected because repeated conveyor
  operation has no authored symbols, instruction addresses or program cursor.
- `CON-063` is rejected because obstruction can stall material without
  invalidating and halting an authored program.
- `CON-001` is rejected because voxel addressability and spacious construction
  do not create a fixed finite occupancy board.
- `SYS-039` is rejected in the conveyor-only scope; later welders and other
  transformers require their own broader analysis.
- `TIM-002` and `TIM-003` are rejected because editing is neither one resolved
  world move nor concurrent with the running factory.
- `COMB-0032` does not recur; a narrower causal shared core is recorded as
  `COMB-0042` rather than weakening the symbolic-program combination.
