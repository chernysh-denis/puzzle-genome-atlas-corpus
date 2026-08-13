---
game_id: GAME-0049
slug: hexcells-infinite
game_title: Hexcells Infinite
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0049
gene_ids:
  action:
    - ACT-063
  system:
    - SYS-089
  constraint:
    - CON-001
  information:
    - INF-003
    - INF-004
    - INF-026
  objective:
    - OBJ-002
    - OBJ-032
  time:
    - TIM-001
---

# Game: Hexcells Infinite

## Analysis scope

- Version / ruleset: the six fixed authored puzzles of World 1, *The Review
  Exam*, in the September 2014 desktop release, from Puzzle 1-1's initial state
  through completion of Puzzle 1-6 and availability of World 2.
- Included: fixed hex fields; orange unresolved cells; left/right blue/black
  assertions; visible blue-total state; black exact-neighbour clues; the brace-
  marked consecutive qualifier introduced in Puzzle 1-4; correct and mistaken
  adjudication; earned-hex consequence; completion and scoped progression.
- Excluded: Worlds 2–6; two-radius blue clues, whole-line, hyphen-separated and
  question-mark clue grammars not demonstrated in World 1; Infinite random
  generation and seed sharing; user levels, soundtrack, achievements and
  speedrunning.
- Direct-play status: not conducted. Product scope is primary-source evidence;
  World 1 transitions are reconstructed from a reproducible no-mistake
  walkthrough and triangulated with three independent mechanical descriptions.
  One community discussion is used only for the narrow wrong-input boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HEX-001` | Every scoped puzzle is a fixed finite hex field whose orange cells already have concealed blue or black truth values | Confirmed | Corroborated | High | P1, S1, S2, G1 |
| `HEX-002` | The player uses distinct left/right inputs to assert blue or black for one unresolved orange cell | Confirmed | Corroborated | High | S1, S2, S3, G1 |
| `HEX-003` | A correct assertion becomes permanent; a wrong assertion is refused, increments mistakes and does not end the puzzle | Confirmed | Corroborated | High | S1, S3, S4, C1 |
| `HEX-004` | A visible black numbered cell gives the exact number of adjacent blue cells | Confirmed | Corroborated | High | S1, S2, S3, G1 |
| `HEX-005` | From Puzzle 1-4, braces additionally state that the counted adjacent blue cells are consecutive | Confirmed | Corroborated | High | S1, G1 |
| `HEX-006` | The interface exposes the remaining blue-cell total while local clues constrain their identities | Confirmed | Corroborated | High | S2, S3 |
| `HEX-007` | A puzzle completes only after every unresolved cell has been correctly classified | Confirmed | Corroborated | High | S1, S2, G1 |
| `HEX-008` | Mistakes reduce earned score / hexes but do not prevent eventual puzzle completion | Confirmed | Corroborated | High | S1, S3, S4, G1 |
| `HEX-009` | Completing the six World 1 puzzles advances the authored progression to World 2 | Confirmed | Corroborated | Medium | S1, G1 |
| `HEX-010` | The action is neither reveal-only `ACT-003` nor editable assignment `ACT-007`: it asserts one pre-existing class and is immediately truth-adjudicated | Observation | Corroborated | High | HEX-001–HEX-003 |
| `HEX-011` | The scoped game has neither Minesweeper zero-region expansion nor terminal hazard exposure | Observation | Corroborated | High | HEX-002–HEX-004, G1 |
| `HEX-012` | Its local-count deduction substrate recurs with Minesweeper, while its action, response, failure and completion boundaries remain different | Pattern | Corroborated | High | HEX-001–HEX-011, MINE-002–MINE-006 |

## Basic data

- Release / origin: Matthew Brown developed and published Hexcells Infinite for
  Windows, macOS and Linux in September 2014.
- Platform or physical form: single-player desktop logic-puzzle game with 36
  authored puzzles plus an excluded seeded infinite generator.
- Puzzle family: truth-adjudicated binary classification from exact local clues.
- Primary product source:
  - **[P1]** [Official Steam product page](https://store.steampowered.com/app/304410/Hexcells_Infinite/),
    identifying the creator, platforms, authored puzzle set and generator.
- Contemporary and independent mechanical sources:
  - **[S1]** [New Game Network review](https://www.newgamenetwork.com/article/1160/hexcells-infinite-review/),
    documenting orange-cell classes, mouse inputs, count grammar, braces,
    mistakes, points and world progression.
  - **[S2]** [MobyGames screenshots and description](https://www.mobygames.com/game/70368/hexcells-infinite/screenshots/),
    corroborating binary classification, clues, remaining total and completion.
  - **[S3]** [Malvasia Bianca — Hexcells](https://malvasiabianca.org/archives/2019/04/hexcells/),
    documenting refusal of wrong clicks, the error count and permanence of
    correct classifications.
  - **[S4]** [LinuxCommunity review](https://www.linux-community.de/artikel/das-spiel-zum-wochenende-hexcells/),
    corroborating inputs, local counts, non-terminal mistakes and untimed play.
- Reproducible transition documentation:
  - **[G1]** [World 1 no-mistake walkthrough](https://steamcommunity.com/sharedfiles/filedetails/?id=373284523),
    documenting all six *Review Exam* puzzles, 0 / positive local deductions,
    the Puzzle 1-4 brace rule, earned hexes and World 2 unlock.
- Narrow community reference:
  - **[C1]** [Undo discussion](https://steamcommunity.com/app/304410/discussions/0/613936039662554149/),
    used only to corroborate that correct cells cannot be undone and a wrong
    input yields a mistake rather than a persistent wrong assignment.
- Claim IDs: `HEX-001`–`HEX-012`.

## Mechanical decomposition

### Action Genes

- `ACT-063` — assert concealed binary cell class. The player selects one orange
  cell and asserts blue with the left input or black with the right input.
- `ACT-003` is absent: the command includes a proposed class rather than asking
  the system to expose whichever fixed content exists.
- `ACT-007` is absent: a wrong value never persists as an editable tentative
  board assignment.
- Claim IDs: `HEX-001`–`HEX-003`, `HEX-010`.

### System Behaviour Genes

- `SYS-089` — immediate concealed-class truth adjudication. A correct assertion
  is accepted permanently. A wrong button is refused, the mistake count rises
  and the same cell remains logically resolved by the binary feedback rather
  than storing the false value.
- `SYS-005` is absent. A visible zero constrains its neighbourhood but does not
  automatically flood-reveal a connected region.
- Resolution order: receive one class assertion; compare it with fixed truth;
  accept or reject it; update the mistake / earned-hex state; expose any newly
  resolved cell state; test exhaustive completion; accept the next input or
  advance the authored progression.
- Claim IDs: `HEX-003`, `HEX-008`, `HEX-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each authored World 1 puzzle has a
  finite pre-authored set of addressable hexagonal positions.
- `CON-006` is absent. A mistaken blue/black assertion is non-terminal.
- Scarce strategic resources: unresolved cells, remaining-blue total, clue-
  neighbourhood degrees and the optional no-mistake score. There is no move or
  time budget in the scoped puzzle.
- Claim IDs: `HEX-001`, `HEX-003`, `HEX-006`, `HEX-008`.

### Information Genes

- `INF-003` — fixed concealed current state. Every orange cell's blue/black
  class exists before the assertion that exposes it; the visible total is a
  parameter constraining the remaining hidden composition.
- `INF-004` — exact local aggregate clue. An ordinary black number reports the
  exact count of blue cells in its adjacent hex neighbourhood. The definition
  is generalised representation-neutrally from “hazards” to one concealed
  target class; the decision relation is unchanged.
- `INF-026` — visible local target-contiguity qualifier. Braces around a black
  count from Puzzle 1-4 state that the counted adjacent blue cells occupy one
  consecutive run around that local ring.
- `INF-006` is absent. No scoped clue gives an ordered run-length sequence for
  an entire row or column.
- Claim IDs: `HEX-001`, `HEX-004`–`HEX-006`.

### Objective Genes

- `OBJ-032` — correctly classify every concealed cell. Completion requires all
  initially orange positions to be accepted as their fixed blue/black truth.
- `OBJ-002` — maximise accumulated score. Fewer mistakes preserve more earned
  hexes / points within the authored progression; the player may still finish
  after an error.
- `OBJ-005` is absent because both fixed classes must be explicitly resolved,
  not only a safe complement while hazards remain hidden.
- `OBJ-006` is absent because the player's entries do not construct the answer;
  they are checked against pre-existing hidden contents one by one.
- Claim IDs: `HEX-003`, `HEX-007`–`HEX-010`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each cell assertion is
  adjudicated, scored and reflected in completion state before another input.
- `TIM-002` is absent under the Atlas boundary: thinking is untimed, but every
  completed input has mandatory automatic post-action adjudication.
- Claim IDs: `HEX-002`, `HEX-003`, `HEX-007`.

## Reproducible transitions

These transitions use only the fixed World 1 grammar. `?` is an orange cell,
`B` a confirmed blue cell and black numbers are written as plain digits.

| Before | Action or inference | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Puzzle 1-1 visible `0` beside unresolved neighbours | Assert each neighbour black | Correct assertions persist | Exact zero local target count | `HEX-004` |
| Puzzle 1-1 visible `6` with six unresolved neighbours | Assert each neighbour blue | Correct assertions persist and remaining-blue total falls | Exact full local target count | `HEX-004`, `HEX-006` |
| Ordinary clue `3` with exactly three unresolved neighbours still needed blue | Assert all three blue | Each is separately adjudicated | Overlapping exact-count deduction | `HEX-002`–`HEX-004` |
| Puzzle 1-4 brace clue `{2}` with candidate neighbours around its ring | Retain only placements whose two blue cells touch in ring order | Non-consecutive pairs are ruled out before input | Local contiguity qualifier | `HEX-005` |
| Fixed blue cell, still orange | Assert black | Input is refused and mistake state increases; play continues | Truth adjudication, not tentative assignment or terminal hazard | `HEX-003` |
| One unresolved orange cell remains and clues force its class | Assert the forced class | Cell is accepted; exhaustive classification completes the puzzle | Completion objective | `HEX-007` |
| Puzzle 1-6 completed | Accept completion transition | Authored progression makes World 2 available | Scoped progression boundary | `HEX-009` |

## Strategic and experiential structure

- Local decision: translate a clue into an equality over adjacent unresolved
  cells, then choose one cell only when its blue/black truth is forced.
- Medium-term planning: subtract overlapping neighbourhoods, combine a local
  count with the remaining-blue total and use brace contiguity to eliminate
  otherwise count-compatible placements.
- Long-term structure: propagate certain classifications until every cell is
  resolved; avoid speculative inputs because binary feedback would solve the
  cell at the cost of earned score.
- Common heuristics: exhaust `0` and full-neighbour clues first, compare shared
  neighbours between clues and treat braces as a topology restriction rather
  than as an additional blue count.
- Failure attribution: immediate adjudication makes the clicked assertion
  locally attributable. A mistake does not invalidate the puzzle state, but it
  weakens no-mistake mastery and progression score.
- Player-trust factors: exact clues and fixed truths must remain stable after
  disclosure; changing a concealed class after its neighbours were shown would
  break the deduction contract.
- Claim IDs: `HEX-003`–`HEX-008`.

## Replay and variation

- Within scope, authored layouts and solutions do not change between attempts.
- Multiple viable strategies: independent forced regions can be resolved in
  different orders, but accepted cell truths and final classification are fixed.
- Typical replay motive: recover a perfect earned-hex result after mistakes or
  practise faster deduction; time pressure itself is excluded.
- Outside scope, Infinite mode generates seed-addressable puzzles and expands
  the clue grammar. It is not evidence for the World 1 genome.
- Claim IDs: `HEX-001`, `HEX-003`, `HEX-008`.

## Adjacent systems and history

- Hexcells Infinite follows Hexcells and Hexcells Plus, but lineage claims are
  not required to classify the scoped transitions.
- Minesweeper shares fixed concealed state, exact local counts and discrete
  resolution. It differs by reveal-only input, optional hypothesis flags,
  automatic zero expansion, terminal hazard exposure and safe-only completion.
- Sudoku and Nonogram construct editable assignments rather than asserting a
  pre-existing concealed truth one cell at a time. Nonogram clues describe
  ordered whole-line runs, not one cyclic local-neighbour run.
- The Witness commits a complete traced answer object for later validation;
  Hexcells validates each asserted binary class immediately.
- Later Hexcells grammars may justify separate information records, but they
  cannot be inferred from the six-puzzle World 1 unit.
- Claim IDs: `HEX-010`–`HEX-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-063` | mouse mapping, accessibility input |
| System Behaviour | `SYS-089` | feedback detail, score penalty |
| Constraint | `CON-001` | hex-field size and topology |
| Information | `INF-003`, `INF-004`, `INF-026` | target class, neighbourhood order, remaining total |
| Objective | `OBJ-002`, `OBJ-032` | earned-hex schedule, world threshold |
| Time | `TIM-001` | animation and input lock |

Canonical signature:

`ACT-063; SYS-089; CON-001; INF-003,INF-004,INF-026; OBJ-002,OBJ-032; TIM-001`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`–`GAME-0048`.
- Indexed combinations scanned: every prior record `COMB-0001`–`COMB-0048`,
  with `COMB-0003`, `COMB-0005`, `COMB-0008`, `COMB-0039` and all proper
  subsets explicitly rechecked as required by selection 008.
- Exact genome matches: none.
- Unique near match: `GAME-0003` — Minesweeper, sharing `CON-001`, `INF-003`,
  `INF-004`, `TIM-001`; intersection `4`, union `14`, `4 / 14 = 0.285714`.
- Next similarity tier: 2048 and Threes each share `OBJ-002`, `CON-001`,
  `TIM-001`; `3 / 20 = 0.150000`.
- Existing combination subsets: none. In particular, `COMB-0003` fails because
  `ACT-003`, `SYS-005`, `CON-006` and `OBJ-005` are absent; `COMB-0005`,
  `COMB-0008` and `COMB-0039` fail their assignment / clue / submission genes.
- New recurring combination: `COMB-0049`, the four-gene shared proper subset
  `CON-001`, `INF-003`, `INF-004`, `TIM-001`, supported exactly by Minesweeper
  and Hexcells Infinite in the 49-game corpus.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `3 / 20 = 0.150000`.
  - `GAME-0002`: `1 / 15 = 0.066667`.
  - `GAME-0003`: `4 / 14 = 0.285714`.
  - `GAME-0004`: `2 / 22 = 0.090909`.
  - `GAME-0005`: `1 / 15 = 0.066667`.
  - `GAME-0006`: `1 / 17 = 0.058824`.
  - `GAME-0007`: `0 / 17 = 0.000000`.
  - `GAME-0008`: `1 / 15 = 0.066667`.
  - `GAME-0009`: `2 / 23 = 0.086957`.
  - `GAME-0010`: `2 / 16 = 0.125000`.
  - `GAME-0011`: `1 / 21 = 0.047619`.
  - `GAME-0012`: `1 / 17 = 0.058824`.
  - `GAME-0013`: `2 / 20 = 0.100000`.
  - `GAME-0014`: `1 / 23 = 0.043478`.
  - `GAME-0015`: `3 / 20 = 0.150000`.
  - `GAME-0016`: `2 / 22 = 0.090909`.
  - `GAME-0017`: `2 / 20 = 0.100000`.
  - `GAME-0018`: `1 / 27 = 0.037037`.
  - `GAME-0019`: `2 / 17 = 0.117647`.
  - `GAME-0020`: `2 / 21 = 0.095238`.
  - `GAME-0021`: `1 / 17 = 0.058824`.
  - `GAME-0022`: `0 / 21 = 0.000000`.
  - `GAME-0023`: `0 / 19 = 0.000000`.
  - `GAME-0024`: `1 / 20 = 0.050000`.
  - `GAME-0025`: `0 / 20 = 0.000000`.
  - `GAME-0026`: `0 / 21 = 0.000000`.
  - `GAME-0027`: `1 / 20 = 0.050000`.
  - `GAME-0028`: `1 / 25 = 0.040000`.
  - `GAME-0029`: `1 / 20 = 0.050000`.
  - `GAME-0030`: `0 / 23 = 0.000000`.
  - `GAME-0031`: `0 / 20 = 0.000000`.
  - `GAME-0032`: `1 / 19 = 0.052632`.
  - `GAME-0033`: `0 / 22 = 0.000000`.
  - `GAME-0034`: `0 / 23 = 0.000000`.
  - `GAME-0035`: `0 / 27 = 0.000000`.
  - `GAME-0036`: `0 / 21 = 0.000000`.
  - `GAME-0037`: `1 / 17 = 0.058824`.
  - `GAME-0038`: `0 / 25 = 0.000000`.
  - `GAME-0039`: `1 / 17 = 0.058824`.
  - `GAME-0040`: `0 / 17 = 0.000000`.
  - `GAME-0041`: `0 / 20 = 0.000000`.
  - `GAME-0042`: `0 / 18 = 0.000000`.
  - `GAME-0043`: `2 / 21 = 0.095238`.
  - `GAME-0044`: `2 / 17 = 0.117647`.
  - `GAME-0045`: `2 / 21 = 0.095238`.
  - `GAME-0046`: `0 / 19 = 0.000000`.
  - `GAME-0047`: `2 / 21 = 0.095238`.
  - `GAME-0048`: `1 / 22 = 0.045455`.

- Scan date: 2026-08-12.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0003` — Minesweeper | `CON-001`, `INF-003`, `INF-004`, `TIM-001` | reveal plus optional flag; zero expansion; terminal hazard; safe-only objective versus asserted binary truth, non-terminal rejection and all-cell classification | Unique near, `0.285714` |
| `GAME-0005` — Sudoku | `CON-001` | editable constructed digits under row/column/block constraints versus fixed hidden binary truth checked per input | Boundary control, `0.066667` |
| `GAME-0008` — Nonogram | `CON-001` | editable filled/empty assignment and whole-line run descriptions versus local cyclic contiguity and immediate truth feedback | Boundary control, `0.066667` |
| `GAME-0039` — The Witness | `CON-001` | complete path submission and post-commit clue feedback versus per-cell class assertion | Boundary control, `0.058824` |

- New genes: `ACT-063`, `SYS-089`, `INF-026`, `OBJ-032`.
- Reused genes: `CON-001`, `INF-003`, `INF-004`, `OBJ-002`, `TIM-001`.
- Classification result: `New gene` plus recurring combination. New records are
  required for the assertion/adjudication pair, local contiguity disclosure and
  fixed-truth exhaustive completion; `INF-004` is generalised without changing
  type or prior signature.

## Combination record

- `COMB-0049` isolates the fixed concealed local-count deduction substrate
  shared with Minesweeper. It deliberately excludes action and objective genes:
  these are exactly where reveal-risk and truth-assertion designs diverge.
- Exhaustive supporter scan: `GAME-0003`, `GAME-0049`; no other current genome
  contains all four genes.
- The set is a proper subset of each supporting genome and has no novelty claim.

## Taxonomy impact

- Registry changes: four active records added and five existing records reused.
- `INF-004` wording is generalised from hazard-specific presentation to a fixed
  concealed target class. Mines remain an included target-class instance, so
  the change preserves the original boundary and Minesweeper signature.
- No merge, split, lifecycle change, type move or taxonomy-change record is
  justified. The six existing types represent the complete scoped loop.
- `ACT-063` / `SYS-089` preserve the crucial boundary between a player command
  that asserts truth and the automatic system response that adjudicates it.
- Candidate terms now map binary truth assertion, immediate adjudication,
  local contiguity and exhaustive hidden classification to bounded records.
- Claim IDs: `HEX-010`–`HEX-012`.

## Negative results

No separate negative-result record is required. The analysis rejects several
nearby classifications (`ACT-003`, `ACT-007`, `SYS-005`, `CON-006`, `INF-006`,
`OBJ-005`, `OBJ-006`, `TIM-002`) but does not invalidate a canonical record,
combination or novelty claim.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] World 1 is a fixed binary truth-
  classification sequence using exact local blue counts and, from Puzzle 1-4,
  a visible consecutive-neighbour qualifier.
- [Confirmed | Corroborated | High] Wrong class inputs are immediate,
  informative and score-reducing but non-terminal; false values do not persist.
- [Pattern | Corroborated | High] Minesweeper and Hexcells Infinite share the
  fixed concealed local-count substrate but not their intervention or objective.

## Нові гени

- `ACT-063` — assert concealed binary cell class.
- `SYS-089` — immediate concealed-class truth adjudication.
- `INF-026` — visible local target-contiguity qualifier.
- `OBJ-032` — correctly classify every concealed cell.

## Нові комбінації

- `COMB-0049` — fixed concealed local-count deduction under discrete
  resolution; recurring in `GAME-0003` and `GAME-0049`.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy change. `INF-004` receives a
  representation-neutral wording generalisation with no signature rewrite.

## Нові питання

- Does a later Hexcells authored world require a separate line-wide count or
  separation qualifier, or can those grammars remain parameters of existing
  information relations?
- Does another game preserve the same truth-assertion/adjudication pair while
  changing topology, feedback cost or class cardinality?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `TARGETED_REUSE_SELECTION_009`.
- Optimisation criterion: rescore Shogun Showdown, Mini Motorways and Can of
  Wormholes against the 49-game / expanded-gene corpus before `GAME-0050`.
- Expected information gain: high for deciding whether the final two units of
  this Goal should test action-alternating exact intent, sibling live-network
  boundaries or recent articulated-body boundaries.

## Чому саме вона

- [Hypothesis | Corroborated | High] Selection 008 ranked the retained games
  before four Hexcells boundary genes and one recurring combination existed.
  The project's adaptive rule requires reassessment after every completed game.
