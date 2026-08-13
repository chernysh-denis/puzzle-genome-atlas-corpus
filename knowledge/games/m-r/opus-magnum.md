---
game_id: GAME-0022
slug: opus-magnum
game_title: Opus Magnum
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0022
  - COMB-0032
  - COMB-0042
gene_ids:
  action:
    - ACT-028
    - ACT-029
  system:
    - SYS-038
    - SYS-039
    - SYS-040
  constraint:
    - CON-062
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

# Game: Opus Magnum

## Analysis scope

- Version / ruleset: one ordinary production puzzle from the original 2017
  Opus Magnum campaign, using the transmutation-engine editor and the standard
  requirement to demonstrate repeated correct output.
- Included: visible reagent and product schemas; positioning and orienting
  movable ports, arms, tracks and available glyphs; per-mechanism symbolic
  instruction rows; deterministic synchronized cycles; reagent supply, arm
  transport, glyph transformations, exact output acceptance, collision or
  incompatible-motion faults; successful production and the cost, cycles and
  area metrics.
- Excluded: narrative and progression order; Sigmar's Garden; appendix cabinet
  puzzles and conduit-specific restrictions; production-puzzle instruction
  scoring; achievements, Steam Workshop, shared GIFs, friends or global
  leaderboards as social systems; external optimisation categories, exploits,
  mods and the 2026 De Re Metallica expansion.
- Direct-play status: not conducted for this record. Creator descriptions are
  combined with contemporary detailed reviews and a current specialist rules
  summary; exact low-level cycle-order edge cases are left as parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OPM-001` | An ordinary puzzle asks the player to design and program an alchemical machine that converts declared reagents into a declared product | Confirmed | Corroborated | High | F1–F3, S1–S3 |
| `OPM-002` | The reagent and product molecular structures and the puzzle's available component catalogue are disclosed before construction | Observation | Corroborated | High | F2, S1, S2 |
| `OPM-003` | The editable layout contains movable or orientable arms, tracks, transformation glyphs and reagent / product ports on a hexagonal workspace | Confirmed | Corroborated | High | F1, F3, S1–S3 |
| `OPM-004` | The player programs each placed mechanism by assigning simple command symbols to positions on its timeline row | Confirmed | Corroborated | High | F2, S1–S3 |
| `OPM-005` | A committed run advances the aligned mechanism rows in shared discrete cycles and automatically repeats their schedule | Observation | Corroborated | High | S1, S2, S4 |
| `OPM-006` | Arms transport atoms or molecules and placed glyphs deterministically bond, separate, change or remove material when their geometry is satisfied | Confirmed | Corroborated | High | F2, S1, S2 |
| `OPM-007` | Reagent ports repeatedly supply their declared assemblies and product ports accept successive assemblies only when they match the target | Observation | Corroborated | High | S1–S3 |
| `OPM-008` | Ordinary campaign completion tests repeated output, reported contemporaneously as six accepted products rather than one accidental pass | Confirmed | Direct | High | S2 |
| `OPM-009` | A physical collision or incompatible simultaneous motion stops the run as a fault and requires design or program revision | Confirmed | Corroborated | High | S1, S2 |
| `OPM-010` | Editing is self-paced and separated from a resettable deterministic test run; the player iterates by stopping or failing and revising | Observation | Corroborated | High | S1, S3 |
| `OPM-011` | Any consistently functioning solution completes the puzzle; one prescribed layout or instruction sequence is not required | Confirmed | Corroborated | High | F1, F3, S1–S3 |
| `OPM-012` | Successful solutions are independently evaluated by cost, completion cycles and occupied area, supporting incompatible optimisation directions | Confirmed | Corroborated | High | F1, S1–S3 |
| `OPM-013` | The scoped execution is fully visible and contains no hidden or random transition after the design is committed | Observation | Corroborated | High | F2, S1–S3 |

## Basic data

- Release / origin: Zachtronics released Opus Magnum in 2017 as an open-ended
  engineering and programming puzzle game.
- Platform or physical form: digital two-dimensional construction editor and
  discrete machine simulator; spatial layout and aligned instruction rows are
  both mechanically relevant.
- Puzzle family: open-ended spatial machine construction and visual
  programming.
- Primary and publisher sources:
  - **[F1]** [Zachtronics — Opus Magnum](https://www.zachtronics.com/opus-magnum/),
    creator description of designing and building machines and optimising for
    simplicity, speed and compactness.
  - **[F2]** [Zachtronics — Zachademics](https://zachtronics.com/zachademics/),
    creator summary of machines constructed from mechanical components and
    programmed with a simple symbol system to manipulate molecular structures.
  - **[F3]** [developer / publisher Steam listing](https://store.steampowered.com/app/558990/Opus_Magnum/),
    release data and open-ended machine design for assembling products.
- Contemporary and specialist corroboration:
  - **[S1]** [Thinky Games — Opus Magnum](https://thinkygames.com/games/opus-magnum/),
    component, glyph, collision, repeated testing, success and metric account.
  - **[S2]** [PC Gamer review, 20 December 2017](https://www.pcgamer.com/opus-magnum-review/),
    sequencer commands, simultaneous physical restrictions, six-product
    completion and cost / area / action evaluation.
  - **[S3]** [Engadget — Building the perfect machine](https://www.engadget.com/2018-07-09-opus-magnum-zachtronics-irl.html),
    hex workspace, parts, timeline programming, outputs and three histograms.
  - **[S4]** [Opus Magnum command reference](https://opus-magnum.fandom.com/wiki/Commands),
    specialist secondary enumeration of mechanism command symbols and repeat
    behaviour; used only to bound the command vocabulary.
- Claim IDs: `OPM-001`–`OPM-013`.

## Mechanical decomposition

### Action Genes

- `ACT-028` — configure spatial machine layout. The player places, removes and
  orients persistent mechanisms and transformation components, deciding which
  positions and trajectories later execution can reach.
- `ACT-029` — edit per-mechanism symbolic instruction tape. Each arm receives
  commands at addressed cycle positions; blanks and macros change the repeated
  schedule without directly moving material during editing.
- Starting, stepping, stopping and resetting a test are phase controls within
  `TIM-006`, not separate problem-solving genes. Their purpose is to inspect
  the authored machine rather than add another transformation command.
- Claim IDs: `OPM-003`, `OPM-004`, `OPM-010`.

### System Behaviour Genes

- `SYS-038` — synchronous cyclic instruction-tape execution. A run reads all
  mechanism rows against one shared cycle coordinate, resolves compatible
  commands together, advances and repeats the schedule without further design
  input.
- `SYS-039` — geometry-triggered molecular transformation. Bonding, unbonding,
  transmutation and disposal occur automatically when the required atoms and
  bonds occupy a glyph's activation geometry.
- `SYS-040` — recurrent reagent-source and exact-product sink processing.
  Cleared sources make another declared reagent available; matching product
  placement consumes and credits output, allowing the same machine to prove a
  production loop.
- Arm movement is the execution of the authored symbols and remains inside
  `SYS-038`; it is not a direct player Action during the run.
- Claim IDs: `OPM-005`–`OPM-008`, `OPM-013`.

### Constraint Genes

- `CON-062` — static machine-footprint placement compatibility. Editor
  placement respects exclusive arm bases, glyph and port footprints plus
  declared overlays such as track under a compatible arm base.
- `CON-063` — kinematic-conflict execution halt. Atom collision, body-to-base
  collision or contradictory simultaneous transport invalidates and stops the
  current run.
- The effectively unbounded ordinary workspace and lack of a mandatory spend
  cap are parameters, not `CON-001` or a finite budget gene. Area and cost
  still matter as post-success measurements.
- Exact product shape is represented by `SYS-040`, `INF-011` and `OBJ-015`:
  disclosure, acceptance transition and pursued output are independently
  bounded rather than duplicated as a generic Constraint.
- Claim IDs: `OPM-002`, `OPM-003`, `OPM-007`–`OPM-009`, `OPM-012`.

### Information Genes

- `INF-001` — fully visible current state. The placed machine, instruction
  rows, current atoms, bonds, mechanism poses and fault location are
  inspectable during editing or testing.
- `INF-011` — exact visible reagent-product specification. The required input
  and output molecular diagrams are known before the machine is authored.
- Difficulty comes from predicting synchronized geometry, not hidden state or
  random successor selection.
- Claim IDs: `OPM-002`, `OPM-004`, `OPM-013`.

### Objective Genes

- `OBJ-015` — repeatedly produce exact target assembly. Functional success
  requires one valid authored machine to submit the exact requested product
  repeatedly during the same run; ordinary campaign corroboration reports six
  accepted copies.
- `OBJ-016` — minimise independent solution resource metrics. After success,
  cost, completion cycles and occupied area remain separate improvement axes
  rather than one accumulated score.
- A cheap but slow machine, a fast component-heavy machine and a compact
  machine may all succeed. The optimisation target is therefore a player-
  selected trade-off, not a hidden single optimum.
- Claim IDs: `OPM-008`, `OPM-011`, `OPM-012`.

### Time Genes

- `TIM-006` — editable design before resettable automatic run. Construction
  and programming are self-paced; once testing starts, the fixed authored
  state advances across multiple cycles until stopped, reset, faulted or
  completed, after which editing can resume.
- It is not `TIM-001`: pressing play does not resolve one ordinary player move
  and return an updated board for the next move; it executes an arbitrarily
  long program.
- It is not `TIM-005`: no hostile side commits intents and the run is a test of
  a persistent program, not the next round inside a tactical mission.
- Claim IDs: `OPM-005`, `OPM-009`, `OPM-010`.

## Reproducible transitions

| Before | Player action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty editable workspace with fixed schemas | Place and orient one arm beside a reagent port | Component remains part of the persistent design but no reagent moves | Layout editing authors future reach rather than executing motion | `OPM-002`, `OPM-003` |
| Placed arm has a blank instruction row | Add grab, rotate and drop symbols at three addressed positions | Symbols persist; the editor state changes but the machine remains stopped | Programming is distinct from mechanism execution | `OPM-004`, `OPM-010` |
| Several arms have aligned instructions | Start or step the test | Each compatible command at the current column resolves in the same cycle | Tapes share a synchronized execution coordinate | `OPM-005` |
| Correct atoms occupy a bonding glyph | Advance the next relevant cycle | The declared bond appears without a separate player command | Transformation is geometry-triggered System Behaviour | `OPM-006` |
| A reagent has been removed from a clear source | Continue the automatic schedule | The source supplies another copy for the repeating machine | Production uses recurrent input rather than finite inventory | `OPM-007` |
| Completed molecule overlaps the product port in the accepted pose | Advance execution | The product is consumed and credited; more copies remain required | Acceptance is exact and repeated | `OPM-007`, `OPM-008` |
| Two atoms' swept paths intersect incompatibly | Advance the conflicting cycle | Execution halts and reports a fault | Dynamic collision is a run-validity constraint | `OPM-009` |
| A run faulted after several cycles | Stop/reset, move a component or command, then rerun | Initial reagent and mechanism state is restored before the revised test | Failure supports deterministic iteration, not irreversible campaign loss | `OPM-009`, `OPM-010` |
| Six correct outputs complete the test | Inspect the result | Cost, cycles and area are reported separately | Functional success and optimisation are distinct layers | `OPM-008`, `OPM-011`, `OPM-012` |

## Strategic and experiential structure

- Local decision: align one arm's reachable poses, one glyph activation area
  and a short instruction subsequence without causing collision.
- Medium-term planning: schedule transfers and temporary storage so multiple
  mechanisms can work in parallel while sharing molecule geometry safely.
- Long-term structure: create a periodic pipeline whose internal state returns
  to a compatible phase while inputs recur and exact outputs leave repeatedly.
- Common heuristics: establish a slow correct loop first; shorten the critical
  path for cycles; remove or share parts for cost; fold trajectories and avoid
  wide swings for area.
- Failure attribution: with visible deterministic execution, a fault or wrong
  product is attributable to layout, program timing or misunderstood glyph
  geometry rather than randomness.
- Player-trust factors: simultaneous command order, swept collision geometry,
  grip ownership, glyph activation, source timing, product equivalence and
  metric measurement must remain reproducible across stepping and full speed.
- Claim IDs: `OPM-003`–`OPM-013`.

## Replay and variation

- What changes between puzzles: reagent and product diagrams, allowed glyphs,
  fixed or movable ports and the transformations or routing burden.
- What remains stable: spatial construction, per-mechanism timelines,
  synchronized deterministic runs, exact repeated output and independent
  optimisation metrics.
- Randomness or procedural generation: none in the scoped fixed production
  puzzle or its committed run.
- Multiple viable strategies: workspace and component choice permit serial,
  parallel, cheap, fast, compact and aesthetic machines with the same product.
- Typical replay motive: improve one metric, explore a different trade-off or
  make a machine simpler and more legible after first success.
- Claim IDs: `OPM-001`, `OPM-011`–`OPM-013`.

## Adjacent systems and history

- Baba Is You exposes executable spatial syntax, but the player mutates rules
  while directly navigating a live board. Opus Magnum authors a separate
  command schedule and then runs it without design edits.
- Into the Breach also separates planning from resolution, but each planning
  phase issues a bounded set of immediate unit commands against previewed
  hostile intent. Opus Magnum repeatedly executes a persistent program from a
  resettable initial state.
- Pipe Dream constructs before and during automatic flow, but does not assign
  independent synchronized instruction rows or validate repeated structured
  products.
- The excluded appendix production cabinets introduce bounded chambers,
  conduits and an instruction metric; those are a distinct scope rather than
  ordinary-figure parameters.
- Claim IDs: `OPM-001`–`OPM-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-028`, `ACT-029` | part catalogue, orientation and command vocabulary |
| System Behaviour | `SYS-038`, `SYS-039`, `SYS-040` | cycle order, glyph mappings and port timing |
| Constraint | `CON-062`, `CON-063` | footprint compatibility and collision sampling |
| Information | `INF-001`, `INF-011` | schema display and execution diagnostics |
| Objective | `OBJ-015`, `OBJ-016` | product count and cost/cycles/area formulas |
| Time | `TIM-006` | step, speed, stop and reset controls |

Canonical signature:

`ACT-028,ACT-029; SYS-038,SYS-039,SYS-040; CON-062,CON-063; INF-001,INF-011; OBJ-015,OBJ-016; TIM-006`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0021`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0021`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0002`: shared `INF-001`; `1 / 18 = 0.055556`.
  - `GAME-0003`: shared none; `0 / 21 = 0.000000`.
  - `GAME-0004`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0005`: shared `INF-001`; `1 / 18 = 0.055556`.
  - `GAME-0006`: shared `INF-001`; `1 / 20 = 0.050000`.
  - `GAME-0007`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0008`: shared `INF-001`; `1 / 18 = 0.055556`.
  - `GAME-0009`: shared `INF-001`; `1 / 27 = 0.037037`.
  - `GAME-0010`: shared `INF-001`; `1 / 20 = 0.050000`.
  - `GAME-0011`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0012`: shared `INF-001`; `1 / 20 = 0.050000`.
  - `GAME-0013`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0014`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0015`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0016`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0017`: shared none; `0 / 25 = 0.000000`.
  - `GAME-0018`: shared `INF-001`; `1 / 30 = 0.033333`.
  - `GAME-0019`: shared `INF-001`; `1 / 21 = 0.047619`.
  - `GAME-0020`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0021`: shared `INF-001`; `1 / 20 = 0.050000`.
- Mathematically selected near matches: `GAME-0002` — Rubik's Cube,
  `GAME-0005` — Sudoku and `GAME-0008` — Nonogram, tied at
  `1 / 18 = 0.055556`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `INF-001` | Rubik's Cube applies reversible physical permutations toward one static configuration; Opus Magnum authors a spatial program that must repeatedly manufacture outputs | Near match only |
| `GAME-0005` — Sudoku | `INF-001` | Sudoku assigns symbols under static global constraints with no automatic transition; Opus Magnum alternates editor state with synchronized execution and collision faults | Near match only |
| `GAME-0008` — Nonogram | `INF-001` | Nonogram reconstructs a binary assignment from run clues; Opus Magnum exposes exact schemas and searches over executable component geometry and timing | Near match only |

- New genes: `ACT-028`, `ACT-029`, `SYS-038`, `SYS-039`, `SYS-040`,
  `CON-062`, `CON-063`, `INF-011`, `OBJ-015`, `OBJ-016`, `TIM-006`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: only complete current-state visibility reuses an
  existing boundary. Machine authoring, cyclic execution, molecular ports,
  exact repeated production, independent resource minimisation and the
  edit-then-run schedule are absent from the first twenty-one genomes.

## Combination record

- Registered [`COMB-0022`](../../combinations/COMB-0022.md), a proper
  eight-gene subset capturing visible specification, spatial machine authoring
  and deterministic repeated production.
- Static placement compatibility, general current-state visibility, broad
  glyph transformation and optional metric optimisation remain in the full
  genome but are not all required to identify the program-production loop.
- Later cross-game analysis registered
  [`COMB-0032`](../../combinations/COMB-0032.md), the six-gene resettable exact-
  output cyclic-production core shared with SpaceChem. It does not replace the
  more specific spatial-machine and instruction-tape boundary of `COMB-0022`.

## Taxonomy impact

- Registry changes: eleven stable genes added; `INF-001` reused.
- Taxonomy-change record: none. The editor commands, automatic state changes,
  legality / failure predicates, disclosed schemas, pursued outcomes and phase
  schedule remain separable inside the existing six types.
- Candidate terms affected: spatial machine configuration, instruction-tape
  editing and execution, glyph transformation, source/sink production,
  footprint and collision validity, exact schemas, repeated production,
  multi-metric minimisation and design/run scheduling are promoted.

## Negative results

- `ACT-014` is absent because arms move material from an authored program, not
  from direct piece-destination choices during execution.
- `SYS-024` and `INF-005` are absent because a repeating instruction tape is
  player-authored program state, not a supplied successor queue.
- `CON-001` is absent because the ordinary workspace is not a fixed finite
  occupancy capacity.
- `OBJ-004` is absent because success is repeated automatic output, not one
  manually reconstructed static configuration.
- `TIM-001`, `TIM-003` and `TIM-005` are absent for the phase-boundary reasons
  above.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Opus Magnum separates self-paced spatial
  construction and symbolic programming from a deterministic cyclic machine
  run (`OPM-003`–`OPM-010`).
- [Confirmed | Corroborated | High] Functional production and independent
  cost, cycles and area optimisation are distinct objective layers
  (`OPM-008`, `OPM-011`, `OPM-012`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-028`, `ACT-029`, `SYS-038`,
  `SYS-039`, `SYS-040`, `CON-062`, `CON-063`, `INF-011`, `OBJ-015`,
  `OBJ-016` and `TIM-006`; reused `INF-001`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0022` captures an authored spatial
  program that repeatedly transforms declared inputs into exact outputs.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; a new Time gene
  resolves the editor / automatic-run boundary without changing the six types.

## Нові питання

- Does a non-spatial programming puzzle reuse `ACT-029`, `SYS-038` and
  `TIM-006` while replacing machine geometry?
- Can `OBJ-016` gain cross-game support from a puzzle with several independent
  optimisation metrics but no programmable machine?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0023` — Return of the Obra Dinn.
- Optimisation criterion: maximise distance from both physics and program
  construction while testing evidence accumulation and delayed validation.
- Expected information gain: separate revisitable evidence scenes, explicit
  identity/fate assignment and batched confirmation from Minesweeper's local
  concealed hazards.
- Backlog impact: remove Return of the Obra Dinn from the retained pool;
  preserve Lemmings, Gorogoa and World of Goo.

## Чому саме вона

- [Hypothesis | Limited | High] It targets the corpus's uncovered
  investigative-deduction structure and should stress Information genes more
  directly than another spatial construction game.
