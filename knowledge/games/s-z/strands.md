---
game_id: GAME-0156
slug: strands
game_title: Strands
analysis_status: reviewed
reviewed: 2026-08-26
combination_ids:
  - COMB-0154
gene_ids:
  action:
    - ACT-255
  system:
    - SYS-427
    - SYS-428
  constraint:
    - CON-001
    - CON-029
    - CON-030
    - CON-376
    - CON-377
  information:
    - INF-003
    - INF-166
  objective:
    - OBJ-085
  time:
    - TIM-002
---

# Game: Strands

## Analysis scope

- Version / ruleset: The New York Times' standard English daily Strands rules,
  as described by the publisher and reviewed on 2026-08-26, restricted to one
  fresh authored 6 × 8 puzzle from its opening clue to full-grid completion.
- Primary decision loop: inspect Today's Theme and the unresolved letter cells,
  trace an eight-neighbour simple path into a word, submit it, then use accepted
  theme paths, non-theme Hint progress and any earned cell or order reveal to
  identify the remaining disjoint paths and the opposite-edge spangram.
- Reproducible entry: open one previously unplayed standard daily puzzle with
  all 48 letters visible, Today's Theme visible, no answer cells claimed and no
  Hint progress accumulated.
- Reproducible exit: every authored theme word and the spangram has been
  accepted as its addressed adjacent-cell path, and their disjoint union claims
  every letter cell exactly once.
- Included: the 6 × 8 letter grid; Today's Theme; horizontal, vertical and
  diagonal path steps; direction changes inside a word; no repeated cell inside
  a path; recognised words of at least four letters; classification as theme,
  spangram, accepted non-theme or rejected; permanent theme-cell claims; three
  non-theme words per Hint; first-stage answer-cell highlight; second-stage
  order reveal; one spangram touching opposite sides; exact full-grid partition.
- Excluded: archive and date selection; the identity or spoiler text of any
  live or past daily answer; streaks, statistics, sharing and account state;
  subscription access; editorial theme or vocabulary selection; tutorial,
  reset and menu gestures; presentation animation; publication cadence as an
  in-attempt timer; treating English vocabulary or a particular theme as genes.
- Direct-play status: the official puzzle UI could not be inspected because the
  available browser environment rejected navigation to the NYT Games route.
  No live answer was consumed. The bounded transitions were instead checked
  against the publisher's unedited launch description mirrored by
  MarketScreener and the formal Strands model in the peer-reviewed FUN 2026
  proceedings; the exact live board remains outside the claims.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `STR-001` | One ordinary daily puzzle presents a fixed 6 × 8 letter grid and one broad theme clue | Confirmed | Corroborated | High | P1, A1, S1 |
| `STR-002` | A word path may step horizontally, vertically or diagonally and may change direction while using no cell twice | Confirmed | Corroborated | High | P1, A1 |
| `STR-003` | Every solution word is theme-related and accepted solution paths are mutually disjoint | Confirmed | Corroborated | High | P1, A1 |
| `STR-004` | The solution paths form an exact partition: every grid letter belongs to one and only one answer | Confirmed | Corroborated | High | P1, A1 |
| `STR-005` | One distinguished spangram names or describes the theme and touches two opposite grid sides | Confirmed | Corroborated | High | P1, A1 |
| `STR-006` | A recognised non-theme word can advance Hint progress without claiming cells in the solution partition | Confirmed | Corroborated | High | P1, A1 |
| `STR-007` | Three accepted non-theme words earn one Hint use | Confirmed | Direct | High | P1, A1 |
| `STR-008` | A first Hint identifies the cells of one unresolved theme word and a following Hint can disclose their exact order | Confirmed | Corroborated | High | A1 |
| `STR-009` | Submitted theme paths remain claimed and reduce the unresolved exact-cover domain | Observation | Corroborated | High | P1, A1 |
| `STR-010` | Daily publication is content cadence, not a forced clock inside the scoped puzzle | Observation | Corroborated | High | P1, S1 |
| `STR-011` | Theme semantics and particular words parameterise an authored instance rather than defining reusable genes | Observation | Corroborated | Medium | `STR-001`–`STR-010` |
| `STR-012` | The hidden answer object is a partition of paths, not one fixed ordered word or a player-authored free routing | Observation | Corroborated | High | `STR-002`–`STR-009` |

## Basic data

- Release / origin: developed and published by The New York Times Games;
  released in beta in March 2024 and added to the NYT Games app on 26 June
  2024 after its beta period.
- Platform or physical form: browser and mobile-app daily word-path puzzle.
- Puzzle family: hidden themed exact-cover word search.
- Primary publisher source:
  - **[P1]** [The New York Times Company — Solvers can now play Strands in the New York Times Games app](https://www.marketscreener.com/quote/stock/THE-NEW-YORK-TIMES-COMPAN-13865/news/New-York-Times-Solvers-can-now-play-Strands-in-the-New-York-Times-Games-app-47248594/),
    an unedited publisher release mirrored by MarketScreener. It states the
    theme-word and spangram objective, opposite-side spangram condition,
    eight-neighbour direction-changing input, no reused letters, perfect grid
    fit and three-non-theme-word Hint rule.
- Formal source:
  - **[A1]** Berggren et al.,
    [“The Complexity of Strands”](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/LIPIcs.FUN.2026.2/LIPIcs.FUN.2026.2.pdf),
    *LIPIcs FUN 2026*. It formalises the grid as disjoint valid word paths that
    cover it exactly, permits all eight neighbouring cells, forbids repeated
    cells within a word and documents the spangram plus two-stage Hint reveal.
- Contemporary product corroboration:
  - **[S1]** [Forbes — NYT Strands hints, spangram and answers](https://www.forbes.com/sites/paultassi/2024/06/13/nyt-strands-hints-spangram-and-answers-for-friday-june-14-take-a-load-off/),
    for the 6 × 8 daily format and varied semantic forms a theme clue can take.
    Its specific daily answers are not copied or used as canonical evidence.
- Claim IDs: `STR-001`–`STR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-255` — trace and submit an adjacent letter-cell word. One compound
  proposal begins on any eligible cell and records an ordered, direction-
  changing route through adjacent letters before submission.
- `ACT-016` is rejected because its route must begin at a fixed endpoint and
  aim toward a declared terminal. Strands begins a candidate at any eligible
  unresolved cell, and only the hidden answer set determines whether it is a
  theme path.
- Typing and ordinary UI taps are presentation controls, not separate scoped
  actions.
- Claim IDs: `STR-002`, `STR-006`, `STR-012`.

### System Behaviour Genes

- `SYS-427` — classify a submitted word path against the authored answer set.
  A matching theme path is retained, the designated spangram is marked
  distinctly, and an accepted non-theme word instead advances assistance.
- `SYS-428` — convert non-answer words into staged answer-path hints. Every
  three credited non-theme words grant a Hint; the first use on an unresolved
  answer identifies its cells and the next applicable use exposes their order.
- Wordle's `SYS-104` is absent: Strands does not compare a guess position by
  position with one target word or issue duplicate-limited ternary similarity.
- Claim IDs: `STR-003`, `STR-005`–`STR-009`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The authored 6 × 8 matrix supplies 48
  persistent addressed cells, each carrying one visible letter.
- `CON-029` — topology-contiguous simple path. Consecutive letters must be
  horizontal, vertical or diagonal neighbours; a path may turn but cannot
  branch, disconnect or revisit a cell.
- `CON-030` — exclusive path-cell occupancy. Accepted answer paths cannot share
  a letter cell in the final solution partition.
- `CON-376` — variable-length lexicon membership gate. At least four traced
  letters must form a recognised word before answer classification or Hint
  credit; unlike Wordle, no single exact word length defines every proposal.
- `CON-377` — spanning answer connects opposite grid boundaries. Exactly one
  designated spangram path must reach top-to-bottom or left-to-right and
  describe the commonality among the other answers.
- Exact answer count, path lengths, cell coordinates, letters and semantic
  theme are instance parameters rather than additional genes.
- Claim IDs: `STR-001`–`STR-007`, `STR-011`.

### Information Genes

- `INF-003` — fixed concealed current state. The complete authored partition
  and which eligible words belong to it already exist but are not exposed at
  entry; submissions and Hints reveal that same fixed object.
- `INF-166` — progressive themed-path discovery and earned route disclosure.
  Today's Theme and all letters begin visible; accepted answer paths persist,
  the Hint meter reports progress, and earned assistance can reveal one path's
  cells and later its traversal order.
- `INF-001` is rejected because the answer membership and partition are
  decision-relevant but concealed even though every surface letter is visible.
- Claim IDs: `STR-001`, `STR-003`–`STR-009`, `STR-012`.

### Objective Genes

- `OBJ-085` — reveal the complete hidden word-path partition. Completion
  requires every authored answer, including the spangram, to be identified as
  its exact path so the disjoint accepted paths cover all 48 cells.
- `OBJ-006` is rejected because it concerns constructing a constraint-
  satisfying assignment and explicitly excludes revealing pre-existing hidden
  contents. Strands recovers the publisher-authored answer partition.
- Finding many valid words or the spangram alone is insufficient while any
  theme path and its cells remain unresolved.
- Claim IDs: `STR-003`–`STR-005`, `STR-009`, `STR-012`.

### Time Genes

- `TIM-002` — self-paced sequential action. The player may pause between path
  proposals and Hint decisions; no in-puzzle clock changes the letter grid.
- A new puzzle's daily publication is supply cadence and remains outside the
  bounded attempt.
- Claim IDs: `STR-010`.

## Reproducible transitions

These rule fixtures use invented letters and paths and do not reproduce a live
or archived NYT answer board.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Four visible cells form a recognised word through diagonal and orthogonal neighbours | Trace those four distinct cells and submit | The proposal reaches authored-answer classification | eight-neighbour, direction-changing compound input | `STR-002` |
| A proposed route jumps over a cell or revisits its first cell | Submit the traced letters | The route is ineligible regardless of its readable spelling | simple-path topology precedes semantics | `STR-002` |
| An eligible path exactly matches one unresolved authored theme answer | Submit it | Its cells and word remain claimed as a solved theme path | fixed answer classification and persistent disclosure | `STR-003`, `STR-009` |
| An eligible path spells a recognised word outside the answer set | Submit it | No solution cells are claimed; non-theme Hint progress increases | lexical validity differs from theme membership | `STR-006` |
| Hint progress stands at two credited non-theme words | Submit a third distinct eligible non-theme word | One Hint use becomes available | thresholded assistance conversion | `STR-007` |
| One Hint is available and no route hint is active | Use Hint | The cell set of one unresolved answer is highlighted without yet supplying order | first-stage spatial disclosure | `STR-008` |
| The same highlighted answer remains unresolved and another Hint is available | Use Hint again | The traversal order through those highlighted letters is disclosed | second-stage ordered disclosure | `STR-008` |
| A found ordinary theme word touches two adjacent sides | Submit it | It may be accepted as a theme word but does not satisfy the spangram condition | opposite rather than merely multiple boundaries | `STR-005` |
| One accepted answer path would reuse a cell already claimed by another | Compare with the authored partition | Both cannot coexist as distinct solution paths | exclusive answer-path occupancy | `STR-003`, `STR-004` |
| Every answer except one is found and its remaining cells form the final legal path | Submit that path | Every cell becomes claimed exactly once and the puzzle completes | exact-cover objective | `STR-004`, `STR-009` |

## Strategic and experiential structure

- Local decision: choose the next adjacent letter while preserving a readable
  word, avoiding a cell revisit and keeping plausible continuation geometry.
- Medium-term planning: combine Today's Theme, found answer meanings, edge
  pressure and remaining cell clusters to decide whether a candidate is a
  theme path, the spangram or a useful non-theme Hint contribution.
- Long-term structure: recover a disjoint exact cover of the grid. Each accepted
  answer removes cells and sharpens both the semantic category and the spatial
  possibilities for every unresolved word.
- Common heuristics: seek a long category-describing path that can reach an
  opposite edge pair; inspect awkward residual pockets; use uncommon letter
  clusters to anchor long words; avoid treating a valid dictionary word as a
  required answer merely because it exists; spend Hints when a residual cell
  set has several plausible traversals.
- Failure attribution: invalid geometry and unrecognised strings fail before
  answer classification; recognised non-theme words are productive but do not
  alter the fixed solution; an impossible residual region signals that the
  player's semantic hypothesis is wrong rather than that accepted paths can
  overlap.
- Player-trust factors: the same submitted path must always receive the same
  class, claimed solution cells must remain disjoint, three credited non-theme
  words must produce one Hint, hint stages must refer to an actually unresolved
  answer and completion must coincide with exact full-grid coverage.
- Claim IDs: `STR-001`–`STR-012`.

## Replay and variation

- What changes between instances: letter placement, theme clue, solution-word
  identities, path geometry, answer count and spangram route.
- Randomness or procedural generation: none is asserted during one scoped
  authored puzzle. Editorial selection and daily publication are outside the
  transition system available to the player.
- Multiple viable strategies: answer discovery order, non-theme words and Hint
  use can differ while the authored solution paths stay fixed.
- Typical replay motive: solve a later daily partition or retry without Hints;
  archive access, streaks and share results remain excluded metagame layers.
- Claim IDs: `STR-001`, `STR-006`–`STR-010`.

## Adjacent systems and history

- Wordle is the closest publisher sibling but queries one fixed five-position
  word under a six-row budget and receives letter-similarity evidence. Strands
  instead submits variable-length spatial paths and recovers every path in one
  hidden exact cover without a failure row limit.
- Flow Free shares simple, disjoint, full-grid paths, but its coloured endpoints
  and all route targets are public and the player constructs any valid covering
  assignment. Strands hides the authored answer membership and path partition,
  begins paths without fixed endpoints and validates their ordered letters.
- A conventional word search exposes a list or category of target words and
  often constrains each word to one straight line. Strands permits turns,
  discloses only a broad theme and makes every cell part of the solution.
- The formal complexity result applies to generalised Strands instances. It
  does not establish the difficulty or uniqueness of every editorial daily.
- Claim IDs: `STR-002`–`STR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-255` | touch or mouse sampling and submission gesture |
| System Behaviour | `SYS-427`, `SYS-428` | answer set, Hint threshold and target selection |
| Constraint | `CON-001`, `CON-029`, `CON-030`, `CON-376`, `CON-377` | 6 × 8 size, eight-neighbour topology and spangram side pair |
| Information | `INF-003`, `INF-166` | theme wording, retained colours and hint presentation |
| Objective | `OBJ-085` | answer count and exact 48-cell coverage |
| Time | `TIM-002` | self-paced within the daily attempt |

Canonical signature:

`ACT-255; SYS-427,SYS-428; CON-001,CON-029,CON-030,CON-376,CON-377; INF-003,INF-166; OBJ-085; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `155` (`GAME-0001`–`GAME-0155`).
- Exact genome matches: none.
- Tied near matches: `GAME-0012` — Flow Free (`4 / 17 = 0.235294`).
- Supported combination subsets: `COMB-0154`.
- Scan date: 2026-08-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0012` — Flow Free | `CON-001`, `CON-029`, `CON-030`, `TIM-002` | Both partition a fixed grid into disjoint self-paced paths; Flow Free constructs public endpoint-paired routes, while Strands reveals hidden lexically classified paths, a spanning answer and earned hints | Near, `0.235294` |

### Preserved research notes

- New combination: `COMB-0154`, whose ten-gene themed hidden-path core is a
  proper subset of this twelve-gene genome.
- New genes: `ACT-255`, `SYS-427`, `SYS-428`, `CON-376`, `CON-377`, `INF-166`
  and `OBJ-085`.
- Reused genes: `CON-001`, `CON-029`, `CON-030`, `INF-003` and `TIM-002`.
- Classification result: `New gene`.
- Evidence and reasoning: the spatial word proposal has no fixed endpoint;
  answer-set classification and earned staged assistance are automatic
  transitions; variable length differs from Wordle's exact-length query gate;
  the opposite-edge spangram is a completion-relevant route constraint; and
  revealing a pre-existing exact cover is excluded by `OBJ-006`.

## Taxonomy impact

- Added seven active genes and reused five existing boundaries without changing
  the six-type taxonomy.
- Generalised `CON-029` and `CON-030` evidence to include hidden answer paths;
  their topology and exclusive-position boundaries remain unchanged.
- Generalised `INF-003` evidence from concealed words and card order to a fixed
  concealed partition whose surface letters are visible.
- Registered `COMB-0154` as the strict interaction subset connecting spatial
  word submission, authored classification, earned hints, hidden state,
  disjoint path topology, lexical eligibility, the spangram and full reveal.

## Negative results

- No evidence supports treating the vocabulary, today's semantic theme or a
  particular answer word as a gene; each is authored instance content.
- `ACT-016` is too narrow because it requires a fixed start and declared
  terminal; broadening it would erase a stable decision boundary.
- `CON-112` is rejected because Strands accepts variable lengths above a
  minimum rather than one declared exact length.
- `SYS-104`, `INF-034` and `OBJ-041` are rejected because there is no one-word
  positional similarity query or exact-sequence terminal predicate.
- `OBJ-006` is rejected because its definition excludes revealing pre-existing
  hidden contents; Strands does not permit any satisfying free path cover.
- Hint selection, colour animation and theme-word semantics do not justify new
  top-level gene types.

## Confidence and open questions

- Overall confidence: High for the standard rules, path topology, exact cover,
  spangram condition and three-word Hint conversion; Medium for minor product
  details that may change independently of the rule contract.
- Open question: the official web UI was not directly inspectable in this
  environment, so the precise current visual encoding and duplicate non-theme
  word feedback remain implementation parameters rather than claims.
- Open question: publisher documentation states the first Hint stage; the
  ordered second stage relies on the formal paper's contemporary model and
  should be rechecked if the standard interface changes.

## Selection rationale

- Search-demand basis: Google global Games rank `#3` in the recorded
  2026-08-17 snapshot, with a direct daily-puzzle discovery fit.
- Gap filled: introduces a hidden, lexically validated exact-cover path puzzle
  combining word discovery with full-grid spatial partitioning.
- Contrast value: separates Wordle-style fixed-sequence deduction from Flow
  Free-style visible route construction while retaining measurable overlap
  with both.
- Source readiness: publisher rules and a formal peer-reviewed model support
  all causally necessary transitions without recording a live daily answer.

## Next research question

- How does Split Fiction's Friend Pass co-op campaign combine asymmetric
  character abilities, shared checkpoint recovery and genre-changing authored
  set pieces without flattening presentation changes into genes?

## Next-candidate queue

- [Hypothesis | Limited | High] `GAME-0157` — Split Fiction.
- [Hypothesis | Limited | High] `GAME-0158` — The Sims 4.
- [Hypothesis | Limited | High] `GAME-0159` — Path of Exile 2.
- [Hypothesis | Limited | High] `GAME-0160` — Marvel Mystic Mayhem.
- [Hypothesis | Limited | High] `GAME-0161` — Five Nights at Freddy's: Secret of the Mimic.
- [Hypothesis | Limited | High] `GAME-0162` — Pokémon Legends: Z-A.

## Next-subject decision

- Selected next: `GAME-0157` — Split Fiction.
- Decision rule: preserve the authorised search-demand order after completing
  the exact Strands unit.
- Backlog impact: advances the batch without changing any later subject.
- Scope debt carried: precise current visual encoding and duplicate-word
  feedback remain parameters pending future direct UI access.

## Forward research leads

- [Hypothesis | Limited | High] Split Fiction should expose whether one bounded
  co-op campaign scope can preserve repeated partner-recovery rules while
  treating each authored genre shift as parameterised content.
- [Hypothesis | Limited | Medium] Future word-path games may recur with
  `ACT-255`, `CON-029` and `CON-376` but omit the hidden exact-cover objective,
  testing whether `COMB-0154` should remain Strands-specific.
- [Hypothesis | Limited | Medium] A future official interface review may refine
  Hint presentation parameters without changing the canonical signature.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Strands hides one exact cover of a 6 × 8
  grid by disjoint themed word paths, including an opposite-edge spangram, and
  converts every three accepted non-theme words into staged assistance
  (`STR-001`–`STR-010`).

## Нові гени

- [Observation | Corroborated | High] `ACT-255`, `SYS-427`, `SYS-428`,
  `CON-376`, `CON-377`, `INF-166` and `OBJ-085`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0154` isolates the themed hidden-path
  classification, assistance and exact-cover interaction.

## Зміни таксономії

- [Observation | Corroborated | High] Змін типів або раніших signatures немає;
  `CON-029`, `CON-030` та `INF-003` лише отримали нове evidence.

## Нові питання

- Як Split Fiction поєднує асиметричні здібності двох персонажів, спільне
  відновлення на checkpoint і жанрово мінливі authored set pieces?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0157` — Split Fiction.
- Optimisation criterion: continue the authorised Goal in the recorded
  search-demand order after one compact deterministic daily puzzle.
- Expected information gain: test bounded cooperative recovery and asymmetric
  action ownership across a campaign whose presentation changes frequently.
- Backlog impact: advances the recorded order without displacing `GAME-0158`
  The Sims 4 or later authorised subjects.

## Чому саме вона

- [Hypothesis | Limited | High] Split Fiction maximises contrast with Strands:
  shared real-time co-op progression follows a solitary hidden exact cover.
