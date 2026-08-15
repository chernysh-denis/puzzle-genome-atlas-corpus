---
game_id: GAME-0065
slug: mastermind
game_title: Mastermind
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0065
gene_ids:
  action:
    - ACT-073
  system:
    - SYS-104
  constraint:
    - CON-020
  information:
    - INF-003
    - INF-031
  objective:
    - OBJ-041
  time:
    - TIM-002
---

# Game: Mastermind

## Analysis scope

- Version / ruleset: Hasbro *Games to Go!* Mastermind standard game, product
  `14151`, copyright 2001, one Decoder attempt against one already fixed code.
- Included: four ordered code positions; six colours; repeated colours in the
  code and guesses; complete four-peg guess rows; persistent prior rows;
  separate exact-colour-and-position and correct-colour-wrong-position counts;
  blank indicators for colours absent after duplicate-aware matching; success
  on four exact indicators; the physical board's ten guess rows; self-paced
  play between guesses.
- Excluded: the Advanced Game's blank code positions; scoring across exchanged
  Codemaker / Decoder roles; deliberate indication errors; competitive bluff
  or social tells; electronic, travel and software editions; configurable code
  lengths, colour counts, timers and no-duplicate variants; algorithmic optimal
  play as a rule requirement.
- Direct-play status: no physical session was conducted. The scoped rule was
  reproduced with the versioned exhaustive control `V1` over all
  `6^4 = 1296` codes. For
  the control secret `A A C D`, guesses `A A B B`, `C D E F`, `A C A D`
  produce `(2 exact, 0 misplaced)`, `(0, 2)` and `(2, 2)` respectively, leaving
  `114`, `42` and then exactly `1` consistent code.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MAS-001` | The standard Codemaker fixes and completely conceals one ordered four-peg code before the Decoder begins | Confirmed | Corroborated | High | P1, P2, A1 |
| `MAS-002` | Each code position uses one of six colours and a colour may occur two or more times | Confirmed | Direct | High | P1 |
| `MAS-003` | Each Decoder hypothesis is one complete ordered row of four colour pegs and earlier rows remain in place | Confirmed | Direct | High | P1 |
| `MAS-004` | Feedback partitions matches into correct colour at the correct position and additional correct colour at an incorrect position | Confirmed | Corroborated | High | P1, A1, A2, V1 |
| `MAS-005` | Duplicate occurrences cannot create more total indicators than matching occurrences available in the fixed code | Confirmed | Corroborated | High | P1, A1, R1, V1 |
| `MAS-006` | Four exact-position indicators terminate the attempt successfully and reveal the concealed code | Confirmed | Direct | High | P1 |
| `MAS-007` | The scoped compact physical board exposes ten guess rows, so exhausting them without four exact matches is a finite failed attempt | Confirmed | Corroborated | High | P1, R1 |
| `MAS-008` | The same concealed code is retained across feedback rounds rather than resampled after each guess | Confirmed | Corroborated | High | P1, A1 |
| `MAS-009` | The feedback is aggregate: it does not identify which guessed positions are responsible for misplaced matches | Confirmed | Corroborated | High | P1, A1, A2 |
| `MAS-010` | A valid strategy repeatedly filters the finite set of codes by compatibility with every retained guess / response pair | Pattern | Corroborated | High | A1, A2, R1, V1 |
| `MAS-011` | Minimising guesses is a stated performance aim, but exact identification is the functional completion objective | Observation | Corroborated | High | P1, A1 |
| `MAS-012` | Mastermind requires new action, resolution, information and objective boundaries without changing the six-type taxonomy | Observation | Corroborated | High | MAS-001–MAS-011 |

## Basic data

- Release / origin: the scoped Hasbro rule sheet is copyright 2001 and states
  that `MASTERMIND` is a registered trademark owned by Invicta Toys and Games
  Ltd. and used under licence. Historical invention and first-release dates are
  not required to establish the bounded mechanics and are not promoted here.
- Platform or physical form: compact two-player peg board with one concealed
  four-hole code row, ten visible four-hole guess rows and a four-hole
  indicator area beside each guess.
- Puzzle family: fixed-secret ordered-code deduction with partitioned aggregate
  feedback.
- Primary and official sources:
  - **[P1] Hasbro rules:** [*Games to Go! MASTERMIND Rules (GB)*](https://www.hasbro.com/common/documents/430e4f3f6bfd10148a8ef35124427085/E0A7EB4950569047F5C0080A51F685F8.pdf),
    product `14151`, 2001. It directly specifies four positions, six colours,
    duplicates, persistent rows, red / white / blank indicators, four-red
    completion and the physical board illustrated with ten guess rows.
  - **[P2] Hasbro product instructions:** [Mastermind product instructions](https://instructions.hasbro.com/en-gb/instruction/mastermind),
    Hasbro Games product `44220`, independently retaining code-breaking as the
    current official product description. This page describes a later product
    and is not used to widen the 2001 ruleset.
- Academic sources:
  - **[A1]** Donald E. Knuth, [“The Computer as Master Mind”](https://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf),
    *Journal of Recreational Mathematics* 9, 1976, pp. 1–6. It formalises the
    classic `4 × 6` code space, response equivalence classes and a finite
    elimination strategy. The paper's five-guess result is strategy evidence,
    not a rule or a required performance claim here.
  - **[A2]** Anders Martinsson and Pascal Su, [“Mastermind with a linear number of queries”](https://doi.org/10.1017/S0963548323000366),
    *Combinatorics, Probability and Computing* 33, 2024, pp. 143–156. It distinguishes
    black-white feedback as the pair of exact and additional colour-match
    counts in generalised Mastermind. Generalised asymptotic bounds do not
    describe the difficulty of this one physical board.
- Reproducible source:
  - **[R1] Simon Tatham's Portable Puzzle Collection:** [Guess rules](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/guess.html),
    an independently implementable account of the default `6` colours, `4`
    pegs, `10` guesses, duplicate-permitted rule and partitioned feedback.
  - **[V1]** [`verify_mastermind_control.py`](../../../scripts/verify_mastermind_control.py),
    an exhaustive `6^4` control that reproduces all three retained candidate
    counts, verifies exact-first duplicate-aware scoring and isolates the one
    compatible secret.
- Claim IDs: `MAS-001`–`MAS-012`.

## Mechanical decomposition

### Action Genes

- `ACT-073` — commit complete ordered-symbol hypothesis. The Decoder fills all
  four positions from the six-colour vocabulary and commits the row for
  adjudication. Equal colours may occupy several positions.
- Peg placement before a complete row is a draft parameter of the same action,
  not four independent concealed-cell assertions: no positional truth is
  reported until the whole hypothesis is evaluated.
- `ACT-032` does not apply. Mastermind's proposal is a fixed-length homogeneous
  sequence, not a multi-field identity / fate dossier with typed semantic
  slots and delayed group confirmation.
- Claim IDs: `MAS-002`, `MAS-003`, `MAS-012`.

### System Behaviour Genes

- `SYS-104` — duplicate-aware positional and residual-match scoring. Exact
  position matches receive priority; among the still-unmatched occurrences,
  each shared colour contributes at most one misplaced indicator. The resulting
  indicator positions do not map back to individual code positions.
- A four-exact result reveals the code and ends the attempt. Other results
  preserve the row and its feedback before the next proposal.
- No autonomous opponent action, random successor or mutable hidden target is
  present. The human Codemaker physically places indicators, but within the
  analysed decision system this is deterministic rule execution rather than a
  strategic second-player response.
- Claim IDs: `MAS-004`–`MAS-006`, `MAS-008`, `MAS-009`.

### Constraint Genes

- `CON-020` — finite action budget with terminal exhaustion. The compact board
  contains ten proposal rows. Each committed complete guess consumes the next
  row; if all are consumed before four exact matches, the code is revealed and
  the Decoder has failed to break it within the board.
- Four positions, six symbol classes and duplicate permission are parameters of
  proposal and scoring, not separate genes. Earlier rows are immutable evidence
  rather than a replenishable resource.
- The broader multi-game scoring rule is excluded, so the Codemaker's points
  per used row do not introduce a score-maximisation objective in this unit.
- Claim IDs: `MAS-002`, `MAS-003`, `MAS-006`, `MAS-007`.

### Information Genes

- `INF-003` — fixed concealed current state. The complete target code already
  exists when the Decoder begins and remains unchanged across all proposals.
- `INF-031` — persistent partitioned hypothesis-match counts. Every completed
  row remains visible beside exact and misplaced aggregate counts, so later
  hypotheses can be checked against the full accumulated evidence set.
- This is not `INF-004`: Mastermind feedback evaluates one submitted global
  ordered hypothesis against the complete secret; it is not a local clue
  attached to a board position that counts one concealed target class in a
  declared neighbourhood.
- Claim IDs: `MAS-001`, `MAS-004`, `MAS-008`–`MAS-010`.

### Objective Genes

- `OBJ-041` — identify fixed concealed ordered sequence. Functional success
  requires one guess matching all four target colours in their exact positions.
- The official instruction to break the code in the fewest guesses expresses
  performance quality. It is not `OBJ-038`, because the rules expose no one
  authored optimal threshold comparable to KAMI's Perfect target.
- The reciprocal Codemaker scoring objective and role rotation belong to the
  excluded match layer.
- Claim IDs: `MAS-006`, `MAS-011`.

### Time Genes

- `TIM-002` — self-paced sequential action. The concealed state does not evolve
  while the Decoder reasons, and no timer forces the next completed row.
- Codemaker and Decoder roles alternate between games, not as adversarial
  `TIM-004` moves within this bounded code-breaking attempt. Indicator placement
  merely resolves the Decoder's committed guess.
- Claim IDs: `MAS-003`, `MAS-008`, `MAS-012`.

## Reproducible transitions

The control secret uses abstract colours `A A C D`. This is one valid standard
code because repetitions are allowed. The feedback algorithm counts exact
matches first and then intersects the remaining colour multisets.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Concealed code `A A C D`; no rows | Commit `A A B B` | Retain row with `2` exact, `0` misplaced; `114 / 1296` codes remain consistent | duplicates and exact-position priority | `MAS-002`–`MAS-005` |
| Same code; first evidence retained | Commit `C D E F` | Retain row with `0` exact, `2` misplaced; `42` codes satisfy both responses | aggregate wrong-position evidence | `MAS-004`, `MAS-008`–`MAS-010` |
| Same code; two rows retained | Commit `A C A D` | Retain row with `2` exact, `2` misplaced; only `A A C D` remains consistent | feedback intersection can identify one code | `MAS-008`–`MAS-010` |
| Same code inferred | Commit `A A C D` | Award four exact indicators, reveal the code and end the attempt | exact ordered completion | `MAS-006`, `MAS-011` |
| Ten non-winning rows already occupied | Attempt another ordinary guess | No proposal row remains; reveal the code and close the attempt | terminal finite budget | `MAS-007` |

The first three transitions are also the state depicted in the Atlas artwork.
Their arithmetic was exhaustively verified across the complete standard code
space; feedback markers are unordered aggregates rather than positional labels.

## Strategic and experiential structure

- Local decision: choose one complete four-colour query that distinguishes as
  many still-consistent codes as useful while respecting the remaining rows.
- Medium-term planning: intersect every response, separate colour multiplicity
  from placement, and avoid proposals that repeat evidence without splitting
  the candidate set.
- Long-term structure: move from broad colour-membership tests toward exact
  positional discrimination until one code remains or a confident final guess
  can be submitted.
- Duplicate colours create the principal bookkeeping hazard. A third red in a
  guess cannot receive a misplaced credit when only two red occurrences exist
  in the secret and both are already matched.
- Failure attribution: a bad guess normally loses one row rather than ending
  play immediately. Contradictory deductions can be checked against persistent
  prior rows; an indication error instead breaks the evidence model and the
  official rules require a replay.
- Player-trust factors: the code must remain fixed, exact matches must be counted
  before residual colour matches, no occurrence may be double-counted, and the
  same scoring function must apply to every row.
- Claim IDs: `MAS-004`, `MAS-005`, `MAS-007`–`MAS-011`.

## Replay and variation

- What changes between attempts: the Codemaker may choose another one of 1296
  standard codes and the Decoder may submit another query sequence.
- What remains stable: four ordered positions, six colours, duplicate
  permission, feedback partition, ten-row capacity and exact-completion rule.
- Randomness or procedural generation: none is required by the physical rules;
  the Codemaker deliberately selects the secret. A software edition may sample
  it, but that setup method is outside this scope.
- Multiple viable strategies: many first guesses and adaptive partitions can
  succeed. Knuth proves one bounded strategy but the rules do not require it.
- Typical replay motive: exchange roles, improve guess count or face a new
  code. The broader match balances roles and scores Codemakers, but is excluded
  from this one-Decoder genome.
- Claim IDs: `MAS-001`, `MAS-002`, `MAS-008`, `MAS-011`.

## Adjacent systems and history

- Minesweeper also has a fixed concealed state, but it permanently reveals
  addressed cells and attaches local neighbour counts to safe positions.
  Mastermind never reveals one selected target position after a failed guess;
  it evaluates a complete global sequence and keeps aggregate counts.
- Balatro shares a finite action allowance and a concealed current order, but
  cards are drawn from and mutate a deck while hands score visible patterns.
  Mastermind's target is immutable and every action is an information query.
- SET also commits a proposal from coloured objects at a self-paced rhythm, but
  its entire field is visible and its accepted triple is unordered. Mastermind
  submits an ordered sequence against inaccessible fixed truth.
- Wordle and Bulls and Cows are close conceptual relatives. Wordle may expose
  per-position colour feedback and lexical constraints; Bulls and Cows often
  forbids repeated digits. Neither boundary is imported into standard scoped
  Mastermind.
- Claim IDs: `MAS-001`–`MAS-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-073` | length `4`, six-colour domain, repeats permitted |
| System Behaviour | `SYS-104` | exact-first duplicate-aware multiset scoring |
| Constraint | `CON-020` | ten complete proposals |
| Information | `INF-003`, `INF-031` | fixed secret plus retained partitioned counts |
| Objective | `OBJ-041` | four exact matches |
| Time | `TIM-002` | no forced clock |

Canonical signature:

`ACT-073; SYS-104; CON-020; INF-003,INF-031; OBJ-041; TIM-002`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`–`GAME-0064`.
- Indexed combinations scanned: every verified record `COMB-0001`–`COMB-0064`.
- Exact genome matches: none.
- Existing combination subsets: none. Every prior verified combination was
  tested as a proper subset of the seven-gene genome and rejected.
- Mathematically selected unique near match: `GAME-0017` Balatro shares
  `CON-020`, `INF-003` at
  `2 / 18 = 0.111111`. SET follows at `1 / 11 = 0.090909`; Rubik's Cube,
  Sudoku, Nonogram and Rush Hour tie at `1 / 13 = 0.076923` through `TIM-002`.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `0 / 21 = 0.000000`; `GAME-0002`: `1 / 13 = 0.076923`;
    `GAME-0003`: `1 / 15 = 0.066667`; `GAME-0004`: `0 / 22 = 0.000000`;
    `GAME-0005`: `1 / 13 = 0.076923`; `GAME-0006`: `1 / 15 = 0.066667`;
    `GAME-0007`: `1 / 14 = 0.071429`; `GAME-0008`: `1 / 13 = 0.076923`;
    `GAME-0009`: `1 / 22 = 0.045455`; `GAME-0010`: `0 / 16 = 0.000000`;
    `GAME-0011`: `1 / 19 = 0.052632`; `GAME-0012`: `1 / 15 = 0.066667`;
    `GAME-0013`: `0 / 20 = 0.000000`; `GAME-0014`: `0 / 22 = 0.000000`;
    `GAME-0015`: `0 / 21 = 0.000000`; `GAME-0016`: `0 / 22 = 0.000000`;
    `GAME-0017`: `2 / 18 = 0.111111`; `GAME-0018`: `0 / 26 = 0.000000`;
    `GAME-0019`: `0 / 17 = 0.000000`; `GAME-0020`: `0 / 21 = 0.000000`;
    `GAME-0021`: `0 / 16 = 0.000000`; `GAME-0022`: `0 / 19 = 0.000000`;
    `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `1 / 18 = 0.055556`;
    `GAME-0025`: `0 / 18 = 0.000000`; `GAME-0026`: `0 / 19 = 0.000000`;
    `GAME-0027`: `0 / 19 = 0.000000`; `GAME-0028`: `0 / 24 = 0.000000`;
    `GAME-0029`: `0 / 19 = 0.000000`; `GAME-0030`: `0 / 21 = 0.000000`;
    `GAME-0031`: `0 / 18 = 0.000000`; `GAME-0032`: `0 / 18 = 0.000000`;
    `GAME-0033`: `0 / 20 = 0.000000`; `GAME-0034`: `0 / 21 = 0.000000`;
    `GAME-0035`: `0 / 25 = 0.000000`; `GAME-0036`: `1 / 18 = 0.055556`;
    `GAME-0037`: `0 / 16 = 0.000000`; `GAME-0038`: `0 / 23 = 0.000000`;
    `GAME-0039`: `1 / 15 = 0.066667`; `GAME-0040`: `1 / 14 = 0.071429`;
    `GAME-0041`: `0 / 18 = 0.000000`; `GAME-0042`: `0 / 16 = 0.000000`;
    `GAME-0043`: `0 / 21 = 0.000000`; `GAME-0044`: `0 / 17 = 0.000000`;
    `GAME-0045`: `0 / 21 = 0.000000`; `GAME-0046`: `1 / 16 = 0.062500`;
    `GAME-0047`: `1 / 20 = 0.050000`; `GAME-0048`: `0 / 21 = 0.000000`;
    `GAME-0049`: `1 / 15 = 0.066667`; `GAME-0050`: `0 / 22 = 0.000000`;
    `GAME-0051`: `0 / 23 = 0.000000`; `GAME-0052`: `0 / 17 = 0.000000`;
    `GAME-0053`: `0 / 16 = 0.000000`; `GAME-0054`: `0 / 18 = 0.000000`;
    `GAME-0055`: `0 / 17 = 0.000000`; `GAME-0056`: `0 / 15 = 0.000000`;
    `GAME-0057`: `0 / 15 = 0.000000`; `GAME-0058`: `0 / 16 = 0.000000`;
    `GAME-0059`: `0 / 14 = 0.000000`; `GAME-0060`: `0 / 14 = 0.000000`;
    `GAME-0061`: `1 / 16 = 0.062500`; `GAME-0062`: `1 / 14 = 0.071429`;
    `GAME-0063`: `1 / 13 = 0.076923`; `GAME-0064`: `1 / 11 = 0.090909`.
- Scan date: 2026-08-14.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0017` — Balatro | `CON-020`, `INF-003` | Balatro spends hands against a score threshold while concealed deck order changes through draws; Mastermind repeatedly queries one immutable ordered target | Unique nearest, `0.111111` |
| `GAME-0064` — SET | `TIM-002` | SET selects one unordered relation from a fully visible field; Mastermind commits ordered hypotheses against concealed truth and consumes a finite row | Second, `0.090909` |
| `GAME-0003` — Minesweeper | `INF-003` | Minesweeper reveals individual cells and local class counts with a terminal hazard; Mastermind retains only global query-response aggregates | Information-boundary control, `0.066667` |

- New genes: `ACT-073`, `SYS-104`, `INF-031`, `OBJ-041`.
- Reused genes: `CON-020`, `INF-003`, `TIM-002`.
- Classification result: four new operational boundaries plus one new verified
  combination around a repeated finite-query loop.
- Evidence and reasoning: none of the existing hypothesis actions submits one
  homogeneous ordered sequence; no system gene performs exact-first residual
  multiset scoring; no information gene retains the resulting two anonymous
  counts; and no objective identifies one fixed concealed ordered sequence.

## Combination record

- Registered [`COMB-0065`](../../combinations/COMB-0065.md), the complete-query
  / partitioned-feedback / fixed-secret elimination interaction.
- The combination omits the ten-row budget and self-paced scheduling because
  neither is required to define how one proposal partitions the consistent
  target set.

## Taxonomy impact

- Registry changes: add `ACT-073`, `SYS-104`, `INF-031` and `OBJ-041`; add
  Mastermind as evidence for `INF-003`, `CON-020` and `TIM-002`.
- Taxonomy-change record: none. Existing boundaries remain correct; Mastermind
  supplies a new cross-type interaction rather than reclassifying prior games.
- Candidate terms affected: complete sequence hypothesis, duplicate-aware
  exact / residual scoring, persistent partitioned feedback and concealed
  ordered-sequence identification.

## Negative results

- `ACT-032` rejected: a four-colour row has one homogeneous positional grammar,
  not typed identity / fate fields or delayed multi-record confirmation.
- `INF-004` rejected: the feedback is a global response to the submitted
  sequence, not a fixed local clue position counting concealed neighbours.
- `INF-023` rejected: the rules do not point to a violated clue or responsible
  proposal position.
- `SYS-089` rejected: no independently addressed concealed position is judged
  true or false and permanently resolved after each action.
- `OBJ-006` rejected: the Decoder is not constructing a visible assignment
  constrained by public givens; the target already exists and stays concealed.
- `OBJ-038` rejected: “fewest guesses” is a performance aim without one
  authored Perfect threshold in the scoped rules.
- `TIM-004` rejected: Codemaker indicator placement is deterministic resolution
  within the attempt, not a strategic adversarial turn.
- No novelty or ownership claim follows from the new Atlas boundaries.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Standard scoped Mastermind uses four ordered
  positions, six colours and permits repeated colours (`MAS-001`–`MAS-003`).
- [Confirmed | Corroborated | High] Feedback must count exact occurrences first
  and additional shared-colour occurrences without double counting
  (`MAS-004`, `MAS-005`).
- [Confirmed | Direct | High] The physical compact board bounds the attempt to
  ten complete guesses and succeeds on four exact indicators (`MAS-006`,
  `MAS-007`).
- [Confirmed | Corroborated | High] The reproducible three-response control
  narrows all `1296` codes to exactly `1` (`MAS-008`–`MAS-010`).

## Нові гени

- [Observation | Corroborated | High] `ACT-073` — commit complete ordered-symbol
  hypothesis.
- [Observation | Corroborated | High] `SYS-104` — duplicate-aware positional
  and residual-match scoring.
- [Observation | Corroborated | High] `INF-031` — persistent partitioned
  hypothesis-match counts.
- [Observation | Corroborated | High] `OBJ-041` — identify fixed concealed
  ordered sequence.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0065` — fixed-secret elimination by
  complete ordered queries and partitioned aggregate feedback.

## Зміни таксономії

- None. Four new genes fit the current Action / System Behaviour / Information
  / Objective split; `CON-020`, `INF-003` and `TIM-002` are reused unchanged.

## Нові питання

- Does a later Wordle analysis reuse `ACT-073` while requiring a distinct
  position-addressed feedback information gene?
- Should optimisation across exchanged Codemaker / Decoder roles form a
  separate adversarial combination once the complete match is in scope?
- Does the ten-row physical limit recur in other query games without their
  scoring and hidden-state structures recurring?

## Наступна рекомендована гра

- No `GAME-0066` is selected in this unit. The next recorded task is the
  deferred 65-game corpus audit required before adaptive selection resumes.
- Audit criterion: measure singleton share and cross-type reuse after
  `ACT-073`, `SYS-104`, `INF-031`, `OBJ-041`; inspect combinations for exact
  subset recurrence; then select `GAME-0066` by expected information gain.
- Run context: after the audit, the active local-only Goal continues until
  exactly 99 reviewed games, with one validated commit per game.

## Чому саме вона

- The audit was explicitly deferred during `GAME-0056`–`GAME-0065`. Mastermind
  closes that ten-game evidence tranche and introduces four new singletons, so
  choosing another subject before measuring the expanded registry would ignore
  the Atlas selection rule.
