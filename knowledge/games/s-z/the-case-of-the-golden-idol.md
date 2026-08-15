---
game_id: GAME-0046
slug: the-case-of-the-golden-idol
game_title: The Case of the Golden Idol
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0046
gene_ids:
  action:
    - ACT-030
    - ACT-059
    - ACT-060
  system:
    - SYS-086
  constraint:
    - CON-064
    - CON-093
  information:
    - INF-001
    - INF-024
  objective:
    - OBJ-017
  time:
    - TIM-002
---

# Game: The Case of the Golden Idol

## Analysis scope

- Version / ruleset: Color Gray Games' original 2022 PC release, scoped to the
  prologue tutorial case *An Abrupt Termination of Contract*.
- Included: the one fixed cliff scene; hotspot highlighting as an optional
  access aid; opening people, possessions, documents and the map; extracting
  highlighted case terms; switching between Exploring and Thinking; the two
  optional identity / location panels; dragging, replacing and removing terms
  in typed slots; section correctness feedback; the mandatory event Scroll;
  accepted Scroll completion and subsequent case unlock.
- Excluded: exact solution wording; the remaining eleven cases, their larger
  identity and custom panels, cross-case character knowledge, intermissions,
  DLC, story interpretation beyond the structured answer, achievements,
  localisation variants, external notes and speedrunning.
- Direct-play status: not conducted. The official publisher storefront and a
  designer interview establish the free investigation, fixed death scenes,
  limited phrase vocabulary, fill-in-the-blank Scroll and validation design.
  A contemporary review corroborates the exact explore / collect / think loop;
  one walkthrough is used only for the tutorial's bounded panels, completion
  condition and reproducible transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GID-001` | The prologue contains one fixed depicted moment with two people, their possessions, nearby containers, documents and a map available for inspection | Confirmed | Corroborated | High | P1, D1, S1, R1 |
| `GID-002` | Clicking an eligible person, object or document opens its fixed evidence detail without changing the represented event | Confirmed | Corroborated | High | D1, S1, R1 |
| `GID-003` | Clicking highlighted words inside evidence adds reusable case-local terms to a persistent bank | Confirmed | Corroborated | High | D1, S1, R1 |
| `GID-004` | The player can switch freely from evidence exploration to a Thinking screen containing structured blank panels | Confirmed | Corroborated | High | D1, S1, R1 |
| `GID-005` | Collected terms can be dragged into, replaced in and removed from semantically constrained answer slots | Confirmed | Corroborated | High | D1, S1, R1 |
| `GID-006` | Filling a complete section causes whole-section correctness evaluation rather than per-slot truth disclosure | Confirmed | Direct | High | D1, R1 |
| `GID-007` | The tutorial exposes optional identity and location panels, but only the event Scroll must be correct to complete the case | Confirmed | Corroborated | High | S1, R1 |
| `GID-008` | Correct Scroll completion accepts the reconstructed event and unlocks the remaining base-game cases | Confirmed | Corroborated | High | S1, R1 |
| `GID-009` | All case evidence, extracted terms and answer entries remain stable and revisable without a deadline | Observation | Corroborated | High | D1, S1, R1 |
| `GID-010` | The scoped case has no corpse-triggered memory entry, audio lead-in, complete identity roster or thresholded batch of subject records | Observation | Corroborated | High | GID-001–GID-009 |
| `GID-011` | Its required answer is one structured causal event account rather than an identity-and-fate ledger covering every person | Observation | Corroborated | High | D1, S1, R1 |
| `GID-012` | Return of the Obra Dinn shares immutable self-paced evidence inspection but not the scoped term-extraction, phrase-slot or validation loop | Observation | Corroborated | High | GID-001–GID-011 |

## Basic data

- Release / origin: Color Gray Games developed and Playstack published The
  Case of the Golden Idol on 13 October 2022.
- Platform or physical form: a mouse-driven two-dimensional frozen evidence
  scene paired with a structured word-bank deduction interface.
- Puzzle family: causal event reconstruction from selectively extracted fixed
  evidence.
- Primary and creator sources:
  - **[P1]** [developer-published Steam page](https://store.steampowered.com/app/1677770/The_Case_of_the_Golden_Idol/),
    identifying developer, publisher, release and the twelve fixed murder
    scenes whose suspects, motives and methods the player reconstructs.
  - **[D1]** [Game Developer interview with designer Andrejs Klavins](https://www.gamedeveloper.com/design/case-of-the-golden-idol),
    documenting free scene examination, gathered names / terms, limited phrase
    vocabulary, grammatical Scroll context, complete-puzzle validation and the
    reason per-slot correctness is withheld.
- Contemporary corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/the-case-of-the-golden-idol-review/),
    documenting the opening cliff case, fixed-scene clicking, word collection,
    Exploring / Thinking switch, drag-and-drop blanks, optional portraits and
    the correctly completed murder Scroll as the progression condition.
  - **[S2]** [The Guardian review](https://www.theguardian.com/games/2022/nov/12/the-case-of-the-golden-idol-review-delicious-sherlockian-mystery-color-gray-playstack),
    independently corroborating the scene-by-scene observational deduction
    structure and comparison with Return of the Obra Dinn.
- Reproducible scope reference:
  - **[R1]** [GameFAQs prologue walkthrough](https://gamefaqs.gamespot.com/pc/327944-the-case-of-the-golden-idol/faqs/79560/an-abrupt-termination-of-contract),
    used only to bound the hotspot tutorial, inspected containers and map,
    eleven-term bank, two auxiliary panels, whole-section checking and the
    Scroll-only completion condition.
- Claim IDs: `GID-001`–`GID-012`.

## Mechanical decomposition

### Action Genes

- `ACT-030` — navigate and focus within static evidence scene. The player
  moves pointer focus across the bounded depicted event and selects people,
  possessions, documents or map details for closer inspection. The access
  parameter is two-dimensional pointer-and-overlay navigation rather than Obra
  Dinn's free three-dimensional camera.
- `ACT-059` — extract highlighted term from evidence detail. Selecting one
  eligible word adds that exact reusable phrase token to the case bank; merely
  reading unhighlighted prose does not create a token.
- `ACT-060` — assign phrase token to structured answer slot. In Thinking mode,
  the player drags one collected term into a compatible blank, and can replace
  or remove it while refining the event account.
- `ACT-031` is absent: the prologue scene is already open and contains no
  corpse-selected transition into another memory. `ACT-032` is absent because
  the mandatory answer is not a subject dossier combining roster identity and
  fate; even the optional name panel is separate from the event Scroll.
- Claim IDs: `GID-001`–`GID-005`, `GID-010`, `GID-011`.

### System Behaviour Genes

- `SYS-086` — complete-section phrase-assignment validation. After every blank
  in one Thinking section is occupied, the system compares the whole phrase
  assignment with its accepted account and reports section correctness without
  exposing the correct value of each wrong slot.
- An optional close-answer indicator can state that no more than two slots are
  wrong; this is a feedback-granularity parameter of the same whole-section
  evaluation, not independent per-slot validation.
- Correct evaluation of the mandatory Scroll accepts the case and makes later
  cases available. Unlocking is a progression consequence of `OBJ-028`, not a
  second reusable transition in this one-case scope.
- `SYS-041` is absent because no death-memory audio or reconstructed scene is
  instantiated after a corpse action. `SYS-042` is absent because one complete
  section is checked immediately; the system does not wait for three correct
  subject records or permanently lock a hidden subset.
- Claim IDs: `GID-006`–`GID-008`, `GID-010`.

### Constraint Genes

- `CON-064` — immutable non-interactive evidence tableau. People, possessions,
  documents and the represented death moment can be inspected through overlays
  but not moved, altered or advanced.
- `CON-093` — case-local phrase vocabulary and typed answer slots. The player
  can fill blanks only with terms extracted in the current case, and each slot
  accepts the phrase class permitted by its grammatical or semantic position.
  This restricts expressible hypotheses while preventing free-text syntax
  ambiguity.
- The finite phrase set also enables brute-force attempts, but search cost is a
  strategic consequence rather than a separate action budget or failure rule.
- Claim IDs: `GID-001`–`GID-006`, `GID-009`.

### Information Genes

- `INF-001` — fully visible current state. Every decision-relevant scene detail
  is available for sequential inspection; current extracted terms and placed
  answers are visible, and no random or permanently concealed case state
  changes between actions. Optional hotspot markers change search convenience,
  not evidence content.
- `INF-024` — persistent extracted phrase bank with answer scaffold. Eligible
  words collected from distributed evidence remain visible as reusable tokens,
  while the partially written Scroll supplies grammatical and semantic context
  for their possible roles.
- `INF-012` is absent in the one-case scope: there is no finite index of named
  memories discovered and revisited across separate evidence scenes.
- `INF-013` is absent: only names actually encountered in this case enter the
  bank; no complete candidate roster with disclosed occupations or nationalities
  is supplied before mapping labels to faces.
- Claim IDs: `GID-001`–`GID-005`, `GID-009`, `GID-010`.

### Objective Genes

- `OBJ-017` — complete exact structured evidence account. The case is solved by
  filling every mandatory Scroll slot so the accepted phrases identify the
  relevant actors, action and location in one exact causal account.
- Event-statement rather than roster topology is a schema parameter. The
  tutorial does not require every person's identity and fate, but it does
  require every mandatory field of its declared structured evidence account.
- `OBJ-006` is absent: the Scroll does not assign values to every position in a
  puzzle instance under interacting declared constraints; it reconstructs one
  accepted event proposition from evidence.
- Claim IDs: `GID-005`–`GID-008`, `GID-011`.

### Time Genes

- `TIM-002` — self-paced sequential action. Evidence inspection, term
  extraction, mode switching and answer revision do not advance the depicted
  moment, trigger an automatic clock or impose a deadline.
- Whole-section validation occurs when a section becomes complete, but it does
  not create a decision-relevant automatic resolution chain between ordinary
  inputs; the player remains free to revise afterward.
- Claim IDs: `GID-002`–`GID-009`.

## Reproducible transitions

| Before | Player action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fixed cliff tableau is open | Select one person or nearby container | Its fixed possessions appear in an inspection overlay; scene objects do not move | pointer focus is evidence access inside an immutable event | `GID-001`, `GID-002` |
| A document contains an eligible highlighted name | Click the highlighted word | That exact term is added to the persistent case bank | evidence extraction differs from merely reading prose | `GID-003` |
| The map overlay is open | Select each eligible place word | Location terms enter the same bank while map content remains unchanged | phrase vocabulary is accumulated from distributed details | `GID-003` |
| Exploration has yielded some terms | Switch to Thinking mode | Structured identity, location and event panels plus collected terms appear | evidence access and hypothesis construction are separate views | `GID-004` |
| One compatible answer blank is empty | Drag a collected term into it | The term occupies that slot and remains replaceable | assignment records a provisional structured hypothesis | `GID-005` |
| At least one section blank remains empty | Change another completed slot | No complete-section verdict is produced for the unfinished section | validation waits for section completeness, not a batch of dossiers | `GID-006` |
| Every blank in a section is occupied but at least one term is wrong | Complete the final blank | The section is rejected without revealing each correct replacement | feedback evaluates the assignment as a whole | `GID-006` |
| Optional identity panel is correct but Scroll is incomplete | Finish the optional panel | Helpful correctness feedback appears, but the case does not complete | identity mapping is auxiliary in this tutorial | `GID-007` |
| Every mandatory Scroll slot contains the accepted term | Complete or revise the final slot | The Scroll is accepted and the prologue completes | exact event account is the scoped objective | `GID-007`, `GID-008` |

## Strategic and experiential structure

- Local decision: choose the next hotspot, possession, text fragment or map
  detail to inspect, then decide which extracted term best fits one typed blank.
- Medium-term planning: map the two people to their belongings, distinguish
  candidate locations through visible geography and use the auxiliary panels
  to stabilise facts before committing the event Scroll.
- Long-term structure: convert dispersed scene evidence into a compact causal
  statement whose actor, action and place agree simultaneously.
- Common heuristics: gather all highlighted terms before brute force; separate
  observed possessions from inferred ownership; use grammatical context to
  reduce candidates; treat optional panel confirmation as evidence, not as the
  final objective.
- Failure attribution: there is no terminal failed attempt. An incorrect
  complete section gives coarse feedback and remains editable; ambiguity is
  resolved by revisiting stable evidence.
- Player-trust factors: hotspot eligibility, extracted vocabulary, slot typing,
  accepted phrase equivalence and whole-section feedback must remain stable.
- Claim IDs: `GID-001`–`GID-011`.

## Replay and variation

- What changes between cases: scene composition, people, evidence details,
  extracted terms, Scroll grammar and optional custom panels.
- What remains stable in the scoped case: every depicted fact, eligible term,
  correct identity / location relation and accepted event account.
- Randomness or procedural generation: none.
- Multiple viable strategies: evidence may be inspected in any order and the
  optional panels may be solved before, during or after Scroll construction;
  the accepted account is fixed.
- Typical replay motive: revisit the deduction path, test which clue supports a
  term or complete auxiliary panels omitted on the first pass.
- Claim IDs: `GID-001`–`GID-009`.

## Adjacent systems and history

- Return of the Obra Dinn shares self-paced inspection of an immutable death
  tableau. It distributes evidence across corpse-triggered memories, supplies a
  complete crew roster and validates identity-fate dossiers in batches; Golden
  Idol's tutorial instead extracts a local phrase bank and immediately checks
  one completed event section.
- Nonogram and Sudoku expose their entire clue systems up front and require
  complete cell assignments. Golden Idol exposes selectable evidence details
  and asks for one causal proposition rather than board-wide constraint
  satisfaction.
- The Witness also validates a complete submitted answer and may localise some
  violated clues. Its answer is a traced path constrained by panel topology;
  Golden Idol's answer consists of typed phrase tokens supported by external
  evidence and receives section-level rather than clue-location feedback.
- Minesweeper reveal exposes fixed concealed cell content. Clicking a Golden
  Idol word does not expose a hidden truth value; it copies an already readable
  evidence term into the hypothesis vocabulary.
- Claim IDs: `GID-001`–`GID-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-030`, `ACT-059`, `ACT-060` | pointer focus, term extraction and phrase-slot revision |
| System Behaviour | `SYS-086` | section-complete trigger and coarse close-answer signal |
| Constraint | `CON-064`, `CON-093` | immutable event plus finite typed phrase vocabulary |
| Information | `INF-001`, `INF-024` | inspectable evidence, persistent word bank and scaffold |
| Objective | `OBJ-017` | exact actor-action-location event account |
| Time | `TIM-002` | untimed exploration and revision |

Canonical signature:

`ACT-030,ACT-059,ACT-060; SYS-086; CON-064,CON-093; INF-001,INF-024;
OBJ-017; TIM-002`

## Corpus comparison

- Indexed games scanned: all 45 prior records, `GAME-0001`–`GAME-0045`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0045`.
- Exact genome matches: none.
- Existing combination subsets: none before registering `COMB-0046`.
- Mathematical near match: `GAME-0023` — Return of the Obra Dinn at
  `4 / 16 = 0.250000`. The pair shares `ACT-030`, `CON-064`, `OBJ-017` and
  `TIM-002`; phrase extraction, answer grammar and validation remain distinct.
- Secondary maximum group: Rubik's Cube, Sudoku, Nonogram and Carto each score
  `2 / 15 = 0.133333`; their overlap is generic self-paced information or fixed
  structure, not investigation logic.
- Full Jaccard scan (intersection / union = score):
  `GAME-0001` `1 / 23 = 0.043478`; `GAME-0002` `2 / 15 = 0.133333`;
  `GAME-0003` `0 / 19 = 0.000000`; `GAME-0004` `1 / 24 = 0.041667`;
  `GAME-0005` `2 / 15 = 0.133333`; `GAME-0006` `2 / 17 = 0.117647`;
  `GAME-0007` `2 / 16 = 0.125000`; `GAME-0008` `2 / 15 = 0.133333`;
  `GAME-0009` `1 / 25 = 0.040000`; `GAME-0010` `1 / 18 = 0.055556`;
  `GAME-0011` `2 / 21 = 0.095238`; `GAME-0012` `2 / 17 = 0.117647`;
  `GAME-0013` `1 / 22 = 0.045455`; `GAME-0014` `1 / 24 = 0.041667`;
  `GAME-0015` `1 / 23 = 0.043478`; `GAME-0016` `1 / 24 = 0.041667`;
  `GAME-0017` `0 / 23 = 0.000000`; `GAME-0018` `1 / 28 = 0.035714`;
  `GAME-0019` `1 / 19 = 0.052632`; `GAME-0020` `1 / 23 = 0.043478`;
  `GAME-0021` `1 / 18 = 0.055556`; `GAME-0022` `1 / 21 = 0.047619`;
  `GAME-0023` `4 / 16 = 0.250000`; `GAME-0024` `1 / 21 = 0.047619`;
  `GAME-0025` `1 / 20 = 0.050000`; `GAME-0026` `1 / 21 = 0.047619`;
  `GAME-0027` `1 / 21 = 0.047619`; `GAME-0028` `1 / 26 = 0.038462`;
  `GAME-0029` `1 / 21 = 0.047619`; `GAME-0030` `1 / 23 = 0.043478`;
  `GAME-0031` `1 / 20 = 0.050000`; `GAME-0032` `1 / 20 = 0.050000`;
  `GAME-0033` `1 / 22 = 0.045455`; `GAME-0034` `1 / 23 = 0.043478`;
  `GAME-0035` `1 / 27 = 0.037037`; `GAME-0036` `2 / 20 = 0.100000`;
  `GAME-0037` `1 / 18 = 0.055556`; `GAME-0038` `1 / 25 = 0.040000`;
  `GAME-0039` `2 / 17 = 0.117647`; `GAME-0040` `2 / 16 = 0.125000`;
  `GAME-0041` `1 / 20 = 0.050000`; `GAME-0042` `1 / 18 = 0.055556`;
  `GAME-0043` `1 / 23 = 0.043478`; `GAME-0044` `1 / 19 = 0.052632`;
  `GAME-0045` `1 / 23 = 0.043478`.

## Combination record

- Registered recurring `COMB-0046` — self-paced immutable evidence
  inspection, supported exhaustively by Return of the Obra Dinn and The Case of
  the Golden Idol.
- `COMB-0023` remains supported only by Return of the Obra Dinn. Golden Idol
  lacks all eight required genes except `TIM-002`, so thematic similarity does
  not weaken its batched dossier boundary.

## Taxonomy impact

- Registry changes originally added `ACT-059`, `ACT-060`, `SYS-086`, `CON-093`,
  `INF-024` and `OBJ-028`; normalisation 004 later merged `OBJ-028` into
  generalised `OBJ-017`. Added Golden Idol evidence to `ACT-030`, `CON-064`,
  `INF-001` and `TIM-002`.
- `ACT-030` and `CON-064` gain representation-neutral wording for pointer-
  accessed two-dimensional tableaux as well as navigable three-dimensional
  reconstructions. Their immutable inspection boundary does not change.
- Taxonomy-change record: none; no prior signature changes.
- Candidate terms affected: promoted evidence-term extraction, phrase-slot
  assignment, complete-section validation, typed case vocabulary, persistent
  phrase bank and exact event-account completion.

## Negative results

- Rejected `ACT-031`, `ACT-032`, `SYS-041`, `SYS-042`, `INF-012`, `INF-013`
  and `OBJ-006` through explicit transition and completion counterexamples.
  Normalisation 004 superseded the earlier narrow `OBJ-017` rejection.
- `COMB-0023` is not a subset and receives no new supporter. The smaller shared
  inspection interaction is recorded separately as `COMB-0046`.
- No separate negative-result record is needed because the result narrows a
  selection hypothesis without overturning an accepted earlier distinction.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] The tutorial separates fixed-scene exploration,
  case-term extraction and typed phrase assignment (`GID-002`–`GID-006`).
- [Confirmed | Corroborated | High] Only the complete event Scroll is required
  for case completion; identities and location are auxiliary panels
  (`GID-007`, `GID-008`).

## Нові гени

- [Observation | Corroborated | High] Originally added `ACT-059`, `ACT-060`,
  `SYS-086`, `CON-093`, `INF-024` and `OBJ-028`; normalisation 004 later
  replaced `OBJ-028` with reused `OBJ-017`.

## Нові комбінації

- [Strong Pattern | Corroborated | High] Registered recurring `COMB-0046` with
  Return of the Obra Dinn for self-paced immutable evidence inspection.

## Зміни таксономії

- [Observation | Corroborated | High] Первинний аналіз не змінював таксономію;
  normalisation 004 пізніше об'єднала `OBJ-028` із `OBJ-017`.

## Нові питання

- Does another evidence-construction game reuse the phrase-bank loop without
  a death-scene setting?
- Should the final audit retain `SYS-086` as phrase-specific validation or
  propose a future cross-domain normalisation with other submit-time validators?

## Наступна рекомендована гра

- No game is scheduled inside the active 30-unit Goal.
- Mandatory next unit: `FINAL_GOAL_AUDIT_030`, covering the full run,
  registries, indexes, comparison invariants, source coverage and final
  repository validation before Goal mode is completed.

## Sources consulted

- Official developer-published Steam page.
- Game Developer interview with Color Gray Games designer Andrejs Klavins.
- Contemporary PC Gamer and Guardian reviews.
- GameFAQs prologue transition and completion reference.
