---
game_id: GAME-0068
slug: wordle
game_title: Wordle
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0068
gene_ids:
  action:
    - ACT-073
  system:
    - SYS-104
  constraint:
    - CON-020
    - CON-112
  information:
    - INF-003
    - INF-034
  objective:
    - OBJ-041
  time:
    - TIM-002
---

# Game: Wordle

## Analysis scope

- Version / ruleset: The New York Times' current daily Wordle, one ordinary
  English puzzle from an empty board until the answer is found or six accepted
  guesses are spent.
- Included: one fixed five-letter answer; complete five-letter word guesses;
  rejection of incomplete or unrecognised entries without spending a row;
  exact-position, present-wrong-position and absent / exhausted feedback;
  exact-first duplicate accounting; persistent guess history; six accepted
  rows; success on the exact word and failure after the sixth non-answer.
- Excluded: Wordle Archive browsing, Hard Mode, WordleBot, hints, streaks,
  statistics, sharing and emoji result grids; editor selection policy; themed
  or multilingual variants; accessibility quality; keyboard colouring as an
  independent evidence channel; the identity of the live daily answer.
- Direct-play status: no live daily answer was consumed or recorded. The
  bounded transition system was reproduced locally from the official current
  product statement and formal published rules. With fixed answer `APPLE`,
  guesses `ALLEY`, `PAPAL`, `AMPLE`, `APPLE` yield `GYBYB`, `YYGBY`, `GBGGG`,
  `GGGGG`; the doubled `L` and `A` prove that excess occurrences are grey only
  after exact and residual target occurrences have been consumed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WRD-001` | One daily puzzle fixes one concealed five-letter answer and allows at most six accepted guesses | Confirmed | Direct | High | P1, A1, A2 |
| `WRD-002` | A submitted row must be one recognised five-letter word; incomplete or unrecognised strings do not become scored attempts | Confirmed | Corroborated | High | A1, A2, S1 |
| `WRD-003` | Every accepted guess receives one retained categorical result per letter position: exact, present elsewhere or absent | Confirmed | Corroborated | High | A1, A2, S1 |
| `WRD-004` | Exact matches consume answer occurrences before residual matches, so repeated guess letters cannot claim one answer occurrence twice | Confirmed | Corroborated | High | A1, A2, local control |
| `WRD-005` | The exact answer ends the attempt successfully; six accepted non-answers exhaust it | Confirmed | Corroborated | High | P1, A1, A2 |
| `WRD-006` | Ordinary mode does not make previous colour hints a legality condition for the next recognised word | Observation | Corroborated | High | A1, scoped exclusion of Hard Mode |
| `WRD-007` | Daily availability and social presentation are cadence / metagame layers, not decision rules inside the bounded attempt | Observation | Corroborated | High | P1, S1 |
| `WRD-008` | Wordle reuses Mastermind's complete-query and duplicate-safe comparison but exposes position-addressed evidence under a lexicon gate | Observation | Corroborated | High | `WRD-001`–`WRD-007` |

## Basic data

- Release / origin: Josh Wardle released Wordle publicly in 2021; The New York
  Times acquired it in 2022 and is the publisher of the scoped current game.
- Platform or physical form: browser-based daily word puzzle with a six-row,
  five-column board and keyboard input.
- Puzzle family: lexically constrained fixed-word deduction.
- Primary and official source:
  - **[P1] The New York Times:** [Wordle](https://www.nytimes.com/games/wordle/index.html).
    Its current canonical product metadata states that the player guesses the
    hidden word in six tries and that a new puzzle is available each day.
- Formal and academic sources:
  - **[A1] Joel David Hamkins:** [“Infinite Wordle and the mastermind numbers”](https://doi.org/10.1002/malq.202200049),
    *Mathematical Logic Quarterly* 69(3), 2023. It formalises Wordle guesses,
    green-first adjudication and occurrence-limited yellow feedback, including
    repeated letters, and explicitly relates the information structure to
    Mastermind.
  - **[A2] Alex Selby:** [“An Exact Solution to Wordle”](https://doi.org/10.1287/opre.2022.0434),
    *Operations Research*. It formalises legal five-letter word guesses, six
    rows and the repeated-character rule used by exact solving.
- Creator and contemporary corroboration:
  - **[S1] TechCrunch:** [A conversation with Josh Wardle, creator of viral hit Wordle](https://techcrunch.com/2022/01/12/josh-wardle-interview-wordle/).
    The interview documents the original creator, five-letter / six-try form,
    daily release and result sharing; sharing remains outside this genome.
- Claim IDs: `WRD-001`–`WRD-008`.

## Mechanical decomposition

### Action Genes

- `ACT-073` — commit complete ordered-symbol hypothesis. The player composes
  all five letter positions and submits the word as one query against the
  fixed answer. A partial row can be edited but is not adjudicated.
- Unlike Mastermind's bounded colour alphabet, `CON-112` additionally requires
  the completed sequence to belong to the accepted word lexicon.
- Claim IDs: `WRD-001`, `WRD-002`, `WRD-008`.

### System Behaviour Genes

- `SYS-104` — duplicate-aware positional and residual-match scoring. The
  system first marks every same-letter / same-position pair. It then consumes
  remaining answer occurrences while assigning present-elsewhere feedback to
  unmatched guess positions; further duplicates remain absent / exhausted.
- Mastermind aggregates the exact and residual partitions. Wordle assigns the
  same duplicate-safe matching result back to individual guess positions; the
  output-granularity difference belongs to Information, not to a second
  scoring algorithm.
- Claim IDs: `WRD-003`, `WRD-004`, `WRD-008`.

### Constraint Genes

- `CON-020` — finite action budget with terminal exhaustion. Only accepted,
  scored words spend one of six rows; the sixth non-answer ends the attempt.
- `CON-112` — fixed-length lexicon membership gate. A row can become a query
  only if it has five positions and the completed sequence is recognised as an
  eligible word. The current answer itself belongs to the narrower answer
  selection, but that editorial pool is not exposed as the complete guess
  vocabulary.
- Earlier colour evidence is not encoded as a normal-mode legality constraint;
  importing it would silently turn the scope into Hard Mode.
- Claim IDs: `WRD-001`, `WRD-002`, `WRD-005`, `WRD-006`.

### Information Genes

- `INF-003` — fixed hidden state. The answer is fixed for the whole attempt;
  guesses disclose evidence about it rather than changing it.
- `INF-034` — persistent position-addressed ternary hypothesis feedback. Every
  accepted word remains visible, with each of its five positions labelled as
  exact, present elsewhere, or absent / exhausted.
- `INF-031` does not apply. Mastermind retains two aggregate counts and hides
  which positions earned misplaced credit; Wordle deliberately identifies the
  status attached to each guessed position.
- Claim IDs: `WRD-001`, `WRD-003`, `WRD-004`, `WRD-008`.

### Objective Genes

- `OBJ-041` — identify fixed concealed ordered sequence. Success requires all
  five submitted letters to equal the answer at their corresponding positions.
  Vocabulary knowledge narrows legal queries but does not replace exact
  sequence equality as the completion predicate.
- Claim IDs: `WRD-001`, `WRD-005`.

### Time Genes

- `TIM-002` — self-paced sequential action. Inside the scoped daily attempt,
  no per-row timer advances the puzzle while the player considers a word.
  Once-per-day publication is content cadence, not a live-time mechanism.
- Claim IDs: `WRD-007`.

## Reproducible transitions

The local control uses answer `APPLE`; it does not reveal or depend on the live
New York Times answer. `G` means exact position, `Y` means present elsewhere
after occurrence accounting, and `B` means absent or an exhausted duplicate.

| Before | Submission | Retained feedback | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty board | `ABLE` or `ZZZZZ` | Rejected; zero rows spent | length and lexicon gate precede scoring | `WRD-002` |
| Answer `APPLE`, row 1 | `ALLEY` | `G Y B Y B` | only one of two guessed `L`s can consume the answer's one residual `L` | `WRD-003`, `WRD-004` |
| Row 2 | `PAPAL` | `Y Y G B Y` | exact `P` is reserved first; only one of two guessed `A`s receives remaining credit | `WRD-004` |
| Row 3 | `AMPLE` | `G B G G G` | four exact positions and one absent letter persist as position evidence | `WRD-003` |
| Row 4 | `APPLE` | `G G G G G`; success | all-position equality identifies the concealed word | `WRD-005` |
| Separate unsolved attempt | six accepted non-answer words | sixth row exhausts attempt; seventh submission is blocked | accepted-row budget and failure boundary | `WRD-005` |

The verifier checks these transitions and exhaustively evaluates all 59,049
answer / guess pairs over a three-letter, five-position domain. For every pair,
green occurs exactly at equal positions and each letter receives exactly
`min(answer count, guess count)` total green-plus-yellow credits.

## Strategic and experiential structure

- Local decision: choose one recognised five-letter word whose letters and
  positions discriminate among answers still consistent with retained rows.
- Medium-term planning: trade direct solution probability against information
  gain, cover uncertain positions and avoid spending duplicate letters unless
  their multiplicity is itself the question.
- Long-term structure: shrink a fixed candidate set before the sixth accepted
  query and commit the exact answer while at least one row remains.
- Failure attribution: grey on an extra duplicate does not prove the letter is
  globally absent; it proves that all answer occurrences were already consumed
  by exact or earlier residual matches in that guess.
- Player-trust factors: identical answer / guess pairs must score identically,
  exact matches must have priority, no answer occurrence may be credited twice,
  rejected input must not consume a row, and all prior feedback must persist.
- Claim IDs: `WRD-002`–`WRD-005`.

## Replay and variation

- What changes between daily sessions: the fixed answer changes on the
  publisher's cadence; the five-position vocabulary gate, six-row budget and
  feedback semantics remain stable.
- Randomness or procedural generation: none is asserted inside the attempt.
  Editorial answer selection and publication order are outside the transition
  system available to the player.
- Multiple viable strategies: high-frequency openers, vowel / consonant
  coverage, candidate-count minimisation and direct likely-word guesses all
  query the same fixed state.
- Typical replay motive: another daily answer creates another deduction tree;
  streak and share displays are optional metagame motivation, not genome genes.
- Claim IDs: `WRD-001`, `WRD-007`.

## Adjacent systems and history

- Mastermind is the mechanical parent: both submit complete ordered hypotheses
  to a fixed duplicate-permitting target and use exact-first residual matching.
  Mastermind accepts arbitrary colour sequences and returns unordered totals;
  Wordle gates guesses through a lexicon and returns a category at each guessed
  position.
- The Case of the Golden Idol also uses words, but its terms are visible,
  extracted evidence tokens placed into typed causal slots. It validates a
  structured event account rather than querying an unknown word with partial
  identity feedback.
- Black Box also accumulates query evidence about one fixed hidden state, but
  its actions are spatial boundary probes and its outcomes describe hidden ray
  behaviour rather than symbol identity.
- Claim IDs: `WRD-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-073` | five letter positions, complete word submission |
| System Behaviour | `SYS-104` | exact-first occurrence-limited scoring |
| Constraint | `CON-020`, `CON-112` | six accepted rows; five-letter recognised word |
| Information | `INF-003`, `INF-034` | fixed answer; retained per-position ternary feedback |
| Objective | `OBJ-041` | exact five-position answer |
| Time | `TIM-002` | self-paced within an attempt |

Canonical signature:

`ACT-073; SYS-104; CON-020,CON-112; INF-003,INF-034; OBJ-041; TIM-002`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0067`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0067`.
- Exact genome matches: none.
- Unique near match: `GAME-0065` Mastermind at `6 / 9 = 0.666667`, sharing
  complete ordered submission, duplicate-safe matching, terminal row budget,
  fixed secret, exact ordered-sequence objective and self-paced turns.
- Next matches: `GAME-0066` Black Box at `2 / 16 = 0.125000`, then
  `GAME-0017` Balatro at `2 / 19 = 0.105263`.
- Supported prior combination subsets: none. `COMB-0065` additionally requires
  aggregate `INF-031`, which Wordle replaces with position-addressed `INF-034`.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `0 / 22 = 0.000000`; `GAME-0002`: `1 / 14 = 0.071429`; `GAME-0003`: `1 / 16 = 0.062500`; `GAME-0004`: `0 / 23 = 0.000000`.
  - `GAME-0005`: `1 / 14 = 0.071429`; `GAME-0006`: `1 / 16 = 0.062500`; `GAME-0007`: `1 / 15 = 0.066667`; `GAME-0008`: `1 / 14 = 0.071429`.
  - `GAME-0009`: `1 / 23 = 0.043478`; `GAME-0010`: `0 / 17 = 0.000000`; `GAME-0011`: `1 / 20 = 0.050000`; `GAME-0012`: `1 / 16 = 0.062500`.
  - `GAME-0013`: `0 / 21 = 0.000000`; `GAME-0014`: `0 / 23 = 0.000000`; `GAME-0015`: `0 / 22 = 0.000000`; `GAME-0016`: `0 / 23 = 0.000000`.
  - `GAME-0017`: `2 / 19 = 0.105263`; `GAME-0018`: `0 / 27 = 0.000000`; `GAME-0019`: `0 / 18 = 0.000000`; `GAME-0020`: `0 / 22 = 0.000000`.
  - `GAME-0021`: `0 / 17 = 0.000000`; `GAME-0022`: `0 / 20 = 0.000000`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `1 / 19 = 0.052632`.
  - `GAME-0025`: `0 / 19 = 0.000000`; `GAME-0026`: `0 / 20 = 0.000000`; `GAME-0027`: `0 / 20 = 0.000000`; `GAME-0028`: `0 / 25 = 0.000000`.
  - `GAME-0029`: `0 / 20 = 0.000000`; `GAME-0030`: `0 / 22 = 0.000000`; `GAME-0031`: `0 / 19 = 0.000000`; `GAME-0032`: `0 / 19 = 0.000000`.
  - `GAME-0033`: `0 / 21 = 0.000000`; `GAME-0034`: `0 / 22 = 0.000000`; `GAME-0035`: `0 / 26 = 0.000000`; `GAME-0036`: `1 / 19 = 0.052632`.
  - `GAME-0037`: `0 / 17 = 0.000000`; `GAME-0038`: `0 / 24 = 0.000000`; `GAME-0039`: `1 / 16 = 0.062500`; `GAME-0040`: `1 / 15 = 0.066667`.
  - `GAME-0041`: `0 / 19 = 0.000000`; `GAME-0042`: `0 / 17 = 0.000000`; `GAME-0043`: `0 / 22 = 0.000000`; `GAME-0044`: `0 / 18 = 0.000000`.
  - `GAME-0045`: `0 / 22 = 0.000000`; `GAME-0046`: `1 / 17 = 0.058824`; `GAME-0047`: `1 / 21 = 0.047619`; `GAME-0048`: `0 / 22 = 0.000000`.
  - `GAME-0049`: `1 / 16 = 0.062500`; `GAME-0050`: `0 / 23 = 0.000000`; `GAME-0051`: `0 / 24 = 0.000000`; `GAME-0052`: `0 / 18 = 0.000000`.
  - `GAME-0053`: `0 / 17 = 0.000000`; `GAME-0054`: `0 / 19 = 0.000000`; `GAME-0055`: `0 / 18 = 0.000000`; `GAME-0056`: `0 / 16 = 0.000000`.
  - `GAME-0057`: `0 / 16 = 0.000000`; `GAME-0058`: `0 / 17 = 0.000000`; `GAME-0059`: `0 / 15 = 0.000000`; `GAME-0060`: `0 / 15 = 0.000000`.
  - `GAME-0061`: `1 / 17 = 0.058824`; `GAME-0062`: `1 / 15 = 0.066667`; `GAME-0063`: `1 / 14 = 0.071429`; `GAME-0064`: `1 / 12 = 0.083333`.
  - `GAME-0065`: `6 / 9 = 0.666667`; `GAME-0066`: `2 / 16 = 0.125000`; `GAME-0067`: `0 / 16 = 0.000000`.
- Interpretation: this is the first deliberately close falsifier of a recent
  genome. It confirms that the scoring system recurs while separating legal
  query vocabulary and evidence granularity from the shared hidden-sequence
  deduction core.

## Taxonomy impact

- Added two active genes: `CON-112` and `INF-034`.
- Reused `ACT-073`, `SYS-104`, `CON-020`, `INF-003`, `OBJ-041` and `TIM-002`.
- Refined `SYS-104` so its stable boundary is duplicate-safe exact-first
  matching, whether its result is aggregated or assigned to guess positions;
  the disclosure distinction remains entirely in Information.
- Registered `COMB-0068` as the proper interaction subset connecting the
  complete word query, duplicate-safe scoring, lexicon gate, fixed answer,
  position-addressed feedback and exact-word objective.

## Negative results

- No evidence supports treating rejected strings as spent rows or scored
  hypotheses.
- No evidence supports double-counting a repeated guess letter when the answer
  contains fewer occurrences.
- No evidence supports importing Hard Mode's clue-reuse restriction into the
  ordinary mode genome.
- The daily cadence does not add a time-pressure gene, and share colours do not
  add an information gene inside play.
- The live answer, answer schedule and complete publisher lexicons are neither
  copied nor exposed by this record.

## Delta summary

- New game: `GAME-0068` Wordle.
- New genes: `CON-112`, `INF-034`.
- Reused genes: `ACT-073`, `SYS-104`, `CON-020`, `INF-003`, `OBJ-041`,
  `TIM-002`.
- New combination: `COMB-0068`.
- New reproducible artefact: `scripts/verify_wordle_control.py`.
- Nearest prior genome: Mastermind at `6 / 9 = 0.666667`; no exact match and no
  earlier supported combination subset.

## Нові факти

- Wordle приймає повне п'ятибуквене слово як один запит і витрачає лише
  прийняті запити із запасу шести рядків.
- Зелені збіги резервуються першими; жовті споживають лише решту входжень
  літери, тому зайві дублікати стають сірими.
- На відміну від Mastermind, результат зберігається біля кожної позиції слова,
  а не як дві непозиційні суми.

## Нові гени

- `CON-112` — допуск повної послідовності за фіксованою довжиною та словником.
- `INF-034` — збережений позиційний тристоронній відгук на гіпотезу.

## Нові комбінації

- `COMB-0068` — лексично обмежена дедукція слова з позиційним відгуком.

## Зміни таксономії

- `SYS-104` узагальнено на спільне exact-first зіставлення входжень у
  Mastermind і Wordle; агрегована або позиційна форма результату визначається
  відповідним Information Gene.
