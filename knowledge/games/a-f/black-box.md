---
game_id: GAME-0066
slug: black-box
game_title: Black Box
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0066
gene_ids:
  action:
    - ACT-007
    - ACT-074
    - ACT-075
  system:
    - SYS-105
    - SYS-106
  constraint:
    - CON-111
  information:
    - INF-003
    - INF-032
  objective:
    - OBJ-042
  time:
    - TIM-002
---

# Game: Black Box

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current manual
  version `20260720.3c36322`, default Black Box parameters `8 × 8` with exactly
  five hidden balls, one generated arena from initial state through an accepted
  solution.
- Included: 32 perimeter laser entries; deterministic straight travel, hits,
  ninety-degree deflections away from a forward-diagonal ball, pre-entry and
  returned reflections, and paired different-edge exits; persistent `H`, `R`
  and numbered-pair observations; marking, removing and optionally locking five
  ball hypotheses; Check; an existing contradictory observation or one newly
  exposed distinguishing ray after a wrong check; acceptance of any layout
  with the same complete laser behaviour; self-paced undo and restart.
- Excluded: custom dimensions and ball counts; Solve / reveal as an ordinary
  strategy; generator internals; the original competitive scoring system;
  multiplayer questioning; variants, cosmetic themes and speed play.
- Direct-play status: no complete direct solve was conducted. The scoped
  transition system was independently reproduced from the documented rules
  and open implementation. For the control balls `(3,1)`, `(1,4)`,
  `(4,6)`, `(5,6)`, `(7,8)`, all 32 entries terminate: 18 are hits, six are
  reflections and eight form four paired exits. Representative outcomes are
  `T1=H`, `T2=R`, `T6↔R5`, `R3↔L2` and `B3↔L7`.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BLB-001` | The default puzzle fixes five concealed balls in an `8 × 8` arena before probing begins | Confirmed | Direct | High | P1, R1 |
| `BLB-002` | A player fires one unused laser from a perimeter entry and cannot observe its internal route | Confirmed | Direct | High | P1, R1 |
| `BLB-003` | A ball directly ahead absorbs the ray as a hit before diagonal deflection is considered | Confirmed | Corroborated | High | P1, R1, F1 |
| `BLB-004` | A ball on one forward diagonal turns the ray ninety degrees away; boundary adjacency or return to the entry produces a reflection | Confirmed | Corroborated | High | P1, R1, F1 |
| `BLB-005` | A ray leaving through another boundary position creates one persistent paired entry / exit observation | Confirmed | Direct | High | P1, R1 |
| `BLB-006` | The player may toggle cell hypotheses and Check is enabled only after the declared number of balls is marked | Confirmed | Direct | High | P1, R1 |
| `BLB-007` | A wrong complete hypothesis is answered with an existing contradictory ray or one newly fired distinguishing ray, not the whole solution | Confirmed | Direct | High | P1, R1 |
| `BLB-008` | The checker accepts any five-ball layout whose outcomes match the hidden layout for every laser, because distinct layouts can be observationally indistinguishable | Confirmed | Corroborated | High | P1, P2, R1 |
| `BLB-009` | Persistent observations support constraint intersection over a fixed concealed state rather than independent cell reveal | Pattern | Corroborated | High | P1, A1, R1 |
| `BLB-010` | Black Box requires new probe, ray-resolution, counterexample, indirect-information and equivalence-objective boundaries without changing the six-type taxonomy | Observation | Corroborated | High | `BLB-001`–`BLB-009` |

## Basic data

- Release / origin: Eric Solomon designed the physical *Black Box*, published
  by Waddingtons in 1977. This historical fact identifies the predecessor but
  does not import its competitive score into the scoped solo implementation.
- Platform or physical form: open-source single-player desktop and web puzzle;
  a concealed rectangular field surrounded by selectable laser ports.
- Puzzle family: fixed-hidden-layout deduction by indirect boundary probes.
- Primary and official sources:
  - **[P1] Simon Tatham manual:** [Black Box](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/blackbox.html),
    version `20260720.3c36322`. It directly specifies ball concealment, every
    ray interaction, result notation, hypothesis controls, Check and acceptance
    of observationally equivalent layouts.
  - **[P2] Simon Tatham developer note:** [Writing a puzzle](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/devel/writing.html).
    Its Black Box example explicitly explains why exact hidden coordinates are
    not a valid checker requirement when two layouts produce identical probes.
- Reproducible sources:
  - **[R1] Open implementation:** [blackbox.c](https://github.com/ghewgill/puzzles/blob/master/blackbox.c)
    in the open-source puzzle collection. `laser_exit` establishes precedence
    and travel; `check_guesses` compares every possible laser result and emits
    one counterexample when needed.
  - **[R2] Official playable build:** [Black Box in JavaScript](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/blackbox.html).
- Formal and academic corroboration:
  - **[F1] British Informatics Olympiad 1999:** [Black Box](https://olympiad.org.uk/papers/1999/bio/bio99r1q2.html),
    an independent formal statement of forward hits, away-from-atom deflection
    and reflection. Its `10 × 10` task is not imported into the default scope.
  - **[A1]** [“Information stored in memory affects abductive reasoning”](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476388/),
    *Scientific Reports* 11, 2021. It uses Black Box as a hidden-cause inference
    task; its experimental layouts only corroborate the abductive structure.
- Historical source:
  - **[H1] David Parlett:** [Eric Solomon and originality](https://www.parlettgames.uk/solomon/originality.html),
    documenting Solomon's authorship and Waddingtons' 1977 publication.
- Claim IDs: `BLB-001`–`BLB-010`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. A left click toggles the selected
  arena cell between unmarked and proposed-ball occupancy; a right click may
  lock the current mark against accidental changes. The proposed value remains
  editable until successful adjudication.
- `ACT-074` — fire probe from perimeter entry. Selecting an unused boundary
  port commits a query whose interior path cannot be steered or seen.
- `ACT-075` — submit fixed-cardinality spatial hypothesis. Check commits the
  complete set of five marked cells for global evaluation.
- `ACT-003` and `ACT-004` do not apply. No cell is revealed by addressing it,
  and a ball mark neither protects a cell from reveal nor changes laser travel;
  it is only part of the submitted answer.
- Claim IDs: `BLB-002`, `BLB-006`, `BLB-010`.

### System Behaviour Genes

- `SYS-105` — hidden orthogonal ray interaction resolution. Forward contact is
  tested before forward diagonals. A ball ahead yields `H`; one on the ray's
  forward-left turns it right, and one on forward-right turns it left. The ray
  continues until absorbed or outside the arena. Returning to the entry, or
  being turned away before entry, yields `R`; a different exit is paired with
  the entry.
- `SYS-106` — observational-equivalence adjudication with counterexample. Check
  computes every boundary laser outcome for the proposal and the hidden field.
  Equal complete mappings succeed even when the coordinates differ. Otherwise
  the system identifies an already fired contradiction or exposes one omitted
  probe whose predicted outcomes differ.
- These behaviours are separate: the ray resolver defines one experiment;
  global adjudication quantifies over the complete experiment domain.
- Claim IDs: `BLB-003`–`BLB-005`, `BLB-007`, `BLB-008`.

### Constraint Genes

- `CON-111` — exact cardinality of spatial hypothesis. Default Check requires
  five distinct proposed cells, matching the declared hidden-ball count.
- The 64 cells and 32 ports are bounded parameters. Lasers are not a finite
  loss budget: a player may use every port, and information gathering itself
  does not create a failure condition.
- Logical locks are an input safeguard, not an additional puzzle-state
  restriction; they do not alter ray outcomes or acceptance.
- Claim IDs: `BLB-001`, `BLB-006`.

### Information Genes

- `INF-003` — fixed concealed current state. The five generated ball positions
  already exist, remain unchanged, and govern every query.
- `INF-032` — persistent indirect probe outcome. `H`, `R`, or a matching number
  remains at the responsible port or pair of ports, while the internal route
  and ball coordinates remain concealed.
- This is not `INF-004`: a result is not an exact local count around an interior
  cell. It can depend on a long deflected path through several hidden regions.
- Claim IDs: `BLB-001`–`BLB-005`, `BLB-009`.

### Objective Genes

- `OBJ-042` — reconstruct observationally equivalent concealed layout. Success
  requires five proposed ball cells whose complete 32-probe mapping equals the
  fixed hidden mapping.
- Exact coordinate recovery is sufficient but not always necessary. The
  manual warns that puzzles above four balls can have indistinguishable
  alternatives, so literal truth equality would reject a valid deduction.
- `OBJ-041` does not apply: cells form an unordered spatial occupancy field,
  not a symbol sequence with independently meaningful ordered slots.
- Claim IDs: `BLB-006`–`BLB-008`, `BLB-010`.

### Time Genes

- `TIM-002` — self-paced sequential action. Neither the balls nor unrequested
  observations change while the player reasons. Probe, edit, undo, restart and
  Check wait for explicit input.
- Automatic ray resolution is immediate consequence processing, not a timed
  turn or autonomous opponent.
- Claim IDs: `BLB-001`, `BLB-002`, `BLB-009`.

## Reproducible transitions

Coordinates are one-indexed from the top-left of an `8 × 8` field. The control
layout contains balls at `(3,1)`, `(1,4)`, `(4,6)`, `(5,6)`, `(7,8)`. Ports are
named by side (`T`, `R`, `B`, `L`) and coordinate from left or top.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Control field fixed; no observations | Fire `T1` | Ball `(1,4)` is directly ahead before any deflection; retain `H` at `T1` | internal absorption | `BLB-002`, `BLB-003`, `BLB-005` |
| Same field | Fire `T2` | Edge-adjacent ball `(3,1)` lies on the forward-left diagonal, turns the ray back before entry; retain `R` | pre-entry reflection | `BLB-004`, `BLB-005` |
| Same field | Fire `T6` | The ray is deflected and leaves at `R5`; retain one matching pair on `T6` and `R5` | hidden bent path and paired exit | `BLB-004`, `BLB-005` |
| Same field | Fire `R3` | The ray leaves at `L2`; retain a second matching pair | paired outcomes are not straight-line claims | `BLB-004`, `BLB-005` |
| Four rather than five cells marked | Press Check | Submission remains unavailable until one more distinct cell is marked | exact proposal cardinality | `BLB-006` |
| Five marked cells predict all visible rays but differ on an untested entry | Press Check | Reject and expose one entry whose proposed and hidden outcomes differ | counterexample-guided correction | `BLB-007` |
| Five marked cells reproduce all 32 outcomes | Press Check | Accept, even if an indistinguishable coordinate layout differs from the generated one | observational equivalence is the terminal predicate | `BLB-008` |

The local model exhaustively traced every control entry and asserted reciprocal
pairing: `T6↔R5`, `T8↔R7`, `R3↔L2`, `B3↔L7`. It produced 18 hits, six
reflections and eight paired endpoints with no non-terminating ray.

## Strategic and experiential structure

- Local decision: choose an unused port likely to separate remaining layouts,
  or edit one ball hypothesis so it satisfies the strongest retained rays.
- Medium-term planning: translate hits into direct-line occupancy constraints,
  reflections into near-edge or return-path alternatives, and paired exits
  into coupled path constraints; test hypotheses against all of them.
- Long-term structure: reduce the set of five-cell layouts until one complete
  observational class remains, then submit any member of that class.
- Common heuristics: start with probes that cross many cells; exploit boundary
  reflections to localise edge-adjacent balls; use intersecting hits and paired
  exits to distinguish absorption from deflection; avoid reading the drawn
  hypothesis balls as revealed truth.
- Failure attribution: an incorrect Check supplies a falsifying experiment,
  making the mismatch attributable without revealing the answer. The player
  can revise marks and preserve all accumulated evidence.
- Player-trust factors: hit precedence, left / right deflection, result pairing
  and global equivalence must be deterministic; one hidden layout cannot change
  between queries.
- Claim IDs: `BLB-003`–`BLB-009`.

## Replay and variation

- What changes between sessions: the generator selects another legal fixed
  five-ball layout and therefore another complete 32-probe outcome mapping.
- Randomness or procedural generation: generation occurs before the decision
  sequence. After setup, all ray outcomes and checker responses are fully
  deterministic.
- Multiple viable strategies: players may fire different subsets and mark
  different intermediate layouts. Some final coordinate layouts are distinct
  but belong to the same accepted observational class.
- Typical replay motive: solve a new concealed field with fewer unnecessary
  probes or a cleaner deduction chain. Original competitive scoring is not
  part of this solo genome.
- Claim IDs: `BLB-001`, `BLB-007`–`BLB-009`.

## Adjacent systems and history

- Mastermind also holds one fixed secret and persistent query feedback, but a
  query there is a complete ordered answer candidate and returns duplicate-safe
  aggregate match counts. Black Box queries one boundary experiment, resolves
  hidden spatial propagation and accepts a whole equivalence class.
- Minesweeper marks hypotheses on a fixed hidden field, but direct cell reveal
  changes information and safe cells expose local neighbour counts. Black Box
  marks do not affect probing and no interior cell is revealed during play.
- Hexcells Infinite and Nonogram edit cell assertions, but their visible clues
  define local counts or ordered line runs. Black Box derives constraints only
  through system-resolved indirect experiments.
- The physical predecessor by Eric Solomon uses the same ray logic. Tatham's
  checker formalises an important digital boundary: observable behaviour, not
  unknowable generator coordinates, defines correctness.
- Claim IDs: `BLB-001`–`BLB-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007`, `ACT-074`, `ACT-075` | cell toggles, 32 entries, Check |
| System Behaviour | `SYS-105`, `SYS-106` | hit priority, ninety-degree deflection, total-probe comparison |
| Constraint | `CON-111` | exactly five distinct cells |
| Information | `INF-003`, `INF-032` | fixed field; persistent `H` / `R` / paired exit |
| Objective | `OBJ-042` | complete observational equivalence |
| Time | `TIM-002` | self-paced |

Canonical signature:

`ACT-007,ACT-074,ACT-075; SYS-105,SYS-106; CON-111; INF-003,INF-032; OBJ-042; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `65` (`GAME-0001`–`GAME-0065`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`2 / 15 = 0.133333`); `GAME-0008` — Nonogram (`2 / 15 = 0.133333`); `GAME-0065` — Mastermind (`2 / 15 = 0.133333`).
- Supported combination subsets: `COMB-0066`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `TIM-002` | fully visible givens and all-different assignment versus hidden propagation probes and behavioural equivalence | Near, `0.133333` |
| `GAME-0008` — Nonogram | `ACT-007`, `TIM-002` | visible ordered run clues and complete cell classification versus indirect ray outcomes | Near, `0.133333` |
| `GAME-0065` — Mastermind | `INF-003`, `TIM-002` | complete sequence queries and partitioned match counts versus perimeter experiments and spatial equivalence | Near, `0.133333` |

### Preserved research notes

- New genes: `ACT-074`, `ACT-075`, `SYS-105`, `SYS-106`, `CON-111`,
  `INF-032`, `OBJ-042`.
- Classification result: `New genes` and a new verified combination.
- Evidence and reasoning: reusing `ACT-007`, `INF-003` and `TIM-002` preserves
  established assignment, fixed-secret and pacing meanings. No prior action
  commits one external spatial experiment; no system resolver propagates an
  unseen ray or compares complete probe maps; and no prior objective accepts a
  concealed layout by observational rather than literal equivalence.

## Taxonomy impact

- Registry changes: add seven active bounded genes and their Ukrainian layer;
  no merge, deprecation or six-type taxonomy change.
- Taxonomy-change record: none.
- Candidate terms affected: perimeter probe, hidden orthogonal propagation,
  complete probe-map equivalence, exact spatial hypothesis cardinality and
  persistent indirect probe result are promoted to stable IDs.

## Negative results

- `ACT-004` rejected: a ball mark does not protect a cell or change probe input.
- `INF-004` rejected: no interior position reveals a local neighbour count.
- `OBJ-041` rejected: the accepted answer is an unordered spatial occupancy
  class, not an exact ordered sequence.
- `CON-020` rejected: probes are not a terminal finite allowance.
