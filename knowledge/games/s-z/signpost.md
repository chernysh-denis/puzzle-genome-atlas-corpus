---
game_id: GAME-0082
slug: signpost
game_title: Signpost
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0082
gene_ids:
  action:
    - ACT-082
  system: []
  constraint:
    - CON-001
    - CON-010
    - CON-029
    - CON-135
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Signpost

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `4 × 4`, with forced opposite-corner endpoints, exact game ID
  `4x4c:1dececcehbfghahc16a`.
- Included: dragging from one cell to a successor anywhere on its eight-way
  arrow ray; the reciprocal predecessor gesture; one ordered path through all
  16 cells; immutable `1` at `A1` and `16` at `D4`; propagated numeric or
  temporary chain labels; complete visibility, revision and self-paced solving.
- Excluded: free-end and larger presets; legal-target highlighting, dots,
  dimmed arrows, temporary colours, unlink-one and unlink-chain gestures,
  Solve, Undo, Redo and Restart as interface support.
- Direct-play status: the current official manual, JavaScript version and source
  were inspected. The control was generated from source revision
  `3c3632259d298ab62aafa8a5858823569ab1af46` with seed `202608140082`.
  An independent Hamiltonian-path enumerator proved exactly one 16-cell
  permutation satisfying both immutable numbers and all 15 arrow-ray
  successor relations.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SIG-001` | The current desktop default is a `4 × 4` field with start and end in opposite corners | Confirmed | Direct | High | S1, S2, S3 |
| `SIG-002` | Every non-final cell points in one of eight directions and may link to any cell at positive distance on that ray | Confirmed | Direct | High | S1, S2 |
| `SIG-003` | Linked cells are consecutive in one numeric sequence from `1` through `N` | Confirmed | Direct | High | S1, S2 |
| `SIG-004` | Every field cell occurs exactly once in the completed sequence | Confirmed | Direct | High | S1, S2 |
| `SIG-005` | The player explicitly chooses successor links; numbers and chain labels are derived presentation | Confirmed | Direct | High | S1, S2, S3 |
| `SIG-006` | The exact control has only fixed `1` and `16` and one unique 16-cell solution | Observation | Direct | High | S2, local exhaustive control |
| `SIG-007` | Directional reachability, global ordering and complete cell coverage constrain one shared path | Observation | Corroborated | High | `SIG-002`–`SIG-006` |

## Basic data

- Release / origin: the manual credits Janko's *Pfeilpfad* and James Harvey's
  contribution to the collection.
- Platform or physical form: open-source desktop and official JavaScript
  single-player path-deduction puzzle.
- Puzzle family: arrow-ray-constrained Hamiltonian successor ordering.
- Primary sources:
  - **[S1] Simon Tatham:** [official Signpost manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/signpost.html),
    specifying the sequence, ray reach and controls.
  - **[S2] Simon Tatham:** [current `signpost.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=signpost.c;hb=HEAD),
    defining defaults, codec, generator, legal links and completion checks.
  - **[S3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/signpost.html),
    confirming current presentation and drag semantics.
- Secondary source: [Janko Pfeilpfad collection](https://www.janko.at/Raetsel/Pfeilpfad/).
- Reproducible artefact: `scripts/verify_signpost_control.py` independently
  decodes the 16 direction tokens and immutable numbers, constructs every
  positive-distance target on each arrow ray and enumerates complete paths to
  a second-solution limit.
- Claim IDs: `SIG-001`–`SIG-007`.

## Mechanical decomposition

### Action Genes

- `ACT-082` — link directed-ray successor. The player selects one source cell
  and one still-eligible target at any positive distance on the source's fixed
  arrow ray, declaring them consecutive.
- Right-drag expresses the same relation from successor to predecessor. It is
  not a second mechanical action.
- Claim IDs: `SIG-002`, `SIG-003`, `SIG-005`.

### System Behaviour Genes

- None promoted. Numeric propagation and algebraic chain labels expose the
  consequences of an explicit link but do not autonomously choose a successor.
- Claim IDs: `SIG-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control preserves 16 individually
  addressed cells and their immutable arrow directions.
- `CON-010` — all-different unit coverage. Treating the entire field as one
  unit, the final labels cover `1` through `16` exactly once.
- `CON-029` — topology-contiguous simple path. One unbranched sequence visits
  16 distinct cells under the instance's directed ray topology.
- `CON-135` — arrow-ray consecutive-successor relation. If one cell receives
  number `n < 16`, the cell numbered `n+1` must lie at positive distance on
  exactly the row, column or diagonal ray indicated by its arrow.
- The fixed `1` and `16` anchor the sequence; their positions are instance
  givens rather than a separate reusable constraint.
- Claim IDs: `SIG-001`–`SIG-007`.

### Information Genes

- `INF-001` — fully visible current state. Every arrow, immutable number,
  current link and derived chain label is visible before the next edit.
- Claim IDs: `SIG-001`–`SIG-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  one complete permutation and path satisfying all arrows and fixed numbers.
- Claim IDs: `SIG-003`, `SIG-004`, `SIG-006`, `SIG-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. Nothing advances between link
  edits, and any unfinished chain may remain while the player reasons.
- Claim IDs: `SIG-005`, `SIG-006`.

## Reproducible transitions

Coordinates use rows `A`–`D` and columns `1`–`4`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fixed `1` at `A1`, southeast arrow | link `A1` to `C3` | `C3` becomes `2`; the intermediate `B2` is not selected | positive-distance arrow-ray successor | `SIG-002`, `SIG-003` |
| `C3=2`, west arrow | link `C3` to `C2` | `C2` becomes `3` | consecutive directed relation | `SIG-002`, `SIG-003` |
| Unnumbered `B2`, east arrow | link `B2` to `B3` before anchoring either end | both cells receive consecutive temporary chain labels | labels derive from explicit topology | `SIG-005` |
| `A1` | attempt to link to `B3` | target is rejected because it is not on the southeast ray | direction and collinearity are mandatory | `SIG-002` |
| Two existing chains | link a tail to an eligible head | chains merge only if their numeric spans and fixed anchors remain compatible | one unbranched global ordering | `SIG-003`, `SIG-007` |
| Exact control | select all verifier transitions | path `A1,C3,C2,D1,B1,B4,A3,A4,C4,A2,D2,C1,B2,B3,D3,D4` covers every cell | complete accepted permutation | `SIG-003`, `SIG-004`, `SIG-006` |
| Fixed control after first solution | continue exhaustive search | every other branch conflicts with a given, repeats a cell or reaches no eligible ray target | unique recorded solution | `SIG-006` |

The verifier asserts the exact official solution description
`S1d10e7c8e5c13c14e6h12b3f2g9h4a11h15c16a`, two fixed endpoints, all
16 unique cells, 15 valid ray transitions and exhaustion after the first
solution.

## Strategic and experiential structure

- Long-ray ambiguity: an arrow identifies a direction but not a distance, so
  several visible cells may be plausible successors.
- Bidirectional deduction: a cell's predecessor can be restricted by all
  arrows aimed toward it even before its own successor is known.
- Chain interval fitting: immutable or already propagated numbers bound how
  many unnumbered cells can fit between two partial chains.
- Coverage pressure: a locally legal shortcut may strand a cell that no
  remaining predecessor ray can reach.
- Claim IDs: `SIG-002`–`SIG-007`.

## Replay and variation

- Generated arrows and additional immutable numbers change the deduction
  order while preserving the scoped gene set.
- Width, height and forced-corner endpoints are setup parameters. Free-end
  presets move the visible `1` and `N` but retain both anchors and the same
  completion predicate.
- Target highlighting, dots and chain colours are inference aids, not required
  answer state.
- Claim IDs: `SIG-001`, `SIG-005`, `SIG-006`.

## Adjacent systems and history

- Flow Free and The Witness share a complete simple path vocabulary, but their
  steps follow local grid edges and their endpoints are not a 1-to-N
  permutation governed by per-cell directed rays.
- Sudoku and Keen share complete all-different numeric coverage, but numbers
  are directly assigned under row and column units rather than propagated by
  successor links.
- Inertia uses a chosen direction for forced traversal across several cells,
  while Signpost chooses a destination on a cell's immutable ray and records a
  persistent ordering relation without moving an actor.
- Claim IDs: `SIG-002`–`SIG-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-082` | source cell; target distance on fixed ray |
| System Behaviour | none | derived labels are presentation |
| Constraint | `CON-001`, `CON-010`, `CON-029`, `CON-135` | 16 cells; anchors 1 and 16 |
| Information | `INF-001` | arrows, links and labels visible |
| Objective | `OBJ-006` | one valid complete permutation |
| Time | `TIM-002` | self-paced link editing |

Canonical signature:

`ACT-082; CON-001,CON-010,CON-029,CON-135; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `81` (`GAME-0001`–`GAME-0081`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`5 / 10 = 0.500000`); `GAME-0080` — Keen (`5 / 10 = 0.500000`).
- Supported combination subsets: `COMB-0082`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `CON-001`, `CON-010`, `INF-001`, `OBJ-006`, `TIM-002` | direct digit assignment under overlapping row, column and block units; no path or arrows | Near, `0.500000` |
| `GAME-0080` — Keen | `CON-001`, `CON-010`, `INF-001`, `OBJ-006`, `TIM-002` | arithmetic cages and Latin units replace directed successor topology | Near, `0.500000` |

## Combination candidate

- Candidate ID: `COMB-0082`.
- Gene set: `ACT-082`, `CON-010`, `CON-029`, `CON-135`, `OBJ-006`, `TIM-002`.
- Decision structure: explicitly link ray-compatible successors into one
  complete simple path whose propagated labels form the entire ordinal domain
  exactly once.
- Supporting games: `GAME-0082` only.
- Distinctness: no prior combination includes directed-ray successor choice;
  generic path completion omits the permutation and arrow relation, while
  generic all-different filling omits the path.

## Outcome

- Reused genes: `CON-001`, `CON-010`, `CON-029`, `INF-001`, `OBJ-006`,
  `TIM-002`.
- Added genes: `ACT-082`, `CON-135`.
- Rejected candidates: automatic numeric propagation as a System Behaviour;
  immutable endpoints as a standalone constraint; separate predecessor-link
  action; fixed path length as a gene.
- Registered combination: `COMB-0082`.
- Taxonomy change: none outside the two new operational boundaries.
- Next falsification target: Net, to test whether rotating local connection
  tiles into one spanning network reuses path topology or requires a separate
  network-completion boundary.

## Taxonomy impact

- Added `ACT-082`, `CON-135` and `COMB-0082`.
- Extended `CON-001`, `CON-010`, `CON-029`, `INF-001`, `OBJ-006` and
  `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Numeric propagation and temporary algebraic labels expose link consequences
  and do not constitute autonomous state resolution.
- Right-dragging from successor to predecessor creates the same directed link
  as left-dragging forward, not a second action gene.
- An arrow ray admits any positive distance, so nearest-target linkage
  `ACT-080` does not apply.
- The fixed corner endpoints are instance parameters; the general rules still
  show both endpoints when the free-end preset is used.

## Delta summary

- Added one reviewed game, two active genes and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 82 reviewed games, 413 active genes and 82 combinations.

## Нові факти

- Зафіксовано точний стандартний контроль `4 × 4` лише з незмінними `1` та
  `16` у протилежних кутах.
- Незалежний перебір довів один повний 16-клітинний шлях із 15 валідними
  переходами вздовж стрілочних променів.

## Нові гени

- `ACT-082` — зв'язати наступника на фіксованому напрямленому промені.
- `CON-135` — наступне порядкове значення лежить на стрілочному промені
  попередньої клітини.

## Нові комбінації

- `COMB-0082` — повний порядковий шлях за напрямленими променями наступників.

## Зміни таксономії

- Повторно використано простий шлях і all-different покриття, але окремо
  активовано вибір віддаленого наступника та перевірку його стрілочного
  напряму.

## Український підсумок

Signpost у межах поточного стандартного контролю — задача на полі `4 × 4`, де
кожна клітина, крім останньої, має стрілку. Гравець з'єднує клітину з наступною
на будь-якій додатній відстані вздовж її стрілочного променя. Усі 16 клітин
мають утворити один простий порядок від незмінної `1` у `A1` до `16` у `D4`,
а кожне число трапляється рівно один раз. Незалежний перебір декодував точний
game ID, підтвердив усі 15 переходів і довів єдиність повного шляху.
