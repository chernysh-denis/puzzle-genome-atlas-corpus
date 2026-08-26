---
game_id: GAME-0062
slug: hexologic
game_title: Hexologic
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0062
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-109
  information:
    - INF-001
    - INF-029
    - INF-030
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Hexologic

## Analysis scope

- Version / ruleset: MythicOwl's released Hexologic, restricted to ordinary
  story levels 1–15 on Normal difficulty, the complete first authored family
  before level 16 introduces immutable grey values.
- Included: one fixed finite arrangement of editable hexagonal cells; values
  one, two or three represented by pips; repeated tapping to change one cell's
  value; visible arrow clues for fixed straight lines in any of the three hex-
  grid axes; cells shared by intersecting lines; exact line-sum satisfaction;
  live green satisfied-line borders; completion when every cell is assigned and
  every displayed sum holds; deterministic revision in the player's own time.
- Excluded: levels 16 onward; immutable grey cells, same-colour linked cells and
  all later world mechanics; hidden special levels; Hard difficulty; Infinite
  Mode; level editor and Workshop; unlock progression, achievements, sound,
  presentation, accessibility annotations and speedrunning.
- Direct-play status: not conducted. The developer and official storefronts
  establish the three-direction exact-sum rule and authored level supply. A
  complete 1–15 walkthrough and a versioned achievement guide make the first
  family reproducible and place the first new element at level 16. Five
  independent hands-on descriptions corroborate the 1–3 domain, tap cycle,
  intersections, live sum feedback, complete assignment and self-paced play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HEX-001` | Ordinary levels 1–15 form the complete first basic family and level 16 introduces immutable grey cells | Confirmed | Corroborated | High | S1, S2, S7 |
| `HEX-002` | Every scoped puzzle exposes one fixed arrangement of editable hexagonal cells and all relevant clues | Confirmed | Corroborated | High | P1, P2, S1-S6 |
| `HEX-003` | Tapping one editable cell assigns or changes only that cell among one, two and three pips | Confirmed | Corroborated | High | S2-S4, S6 |
| `HEX-004` | An arrow clue identifies a fixed straight line and gives the exact sum required across that line | Confirmed | Corroborated | High | P1, P2, S3-S6 |
| `HEX-005` | Clued lines may run along all three hex-grid axes and intersect through shared cells | Confirmed | Corroborated | High | P1, P2, S1, S3-S5 |
| `HEX-006` | A shared cell contributes its one current value to every clued line containing it | Confirmed | Corroborated | High | S1, S3-S6 |
| `HEX-007` | A clued line receives a green border as soon as its current values equal its target sum | Confirmed | Corroborated | High | S3-S5 |
| `HEX-008` | One green line can later require rearrangement because an intersecting line is not satisfied | Confirmed | Corroborated | High | S3, S5 |
| `HEX-009` | Completion requires a value in every cell and simultaneous satisfaction of every displayed line sum | Confirmed | Corroborated | High | P1, S2-S6 |
| `HEX-010` | Scoped play has no random successor, forced clock or terminal move allowance | Observation | Corroborated | High | S3-S6 |
| `HEX-011` | Levels 16+, special puzzles and later updates introduce rules outside the selected arithmetic core | Confirmed | Corroborated | High | P1, S2, S3, S7 |

## Basic data

- Release / origin: developed and published by MythicOwl; released on Steam on
  29 May 2018 and on Nintendo Switch on 12 June 2018.
- Platform or physical form: deterministic single-player digital number-
  assignment puzzle for mouse, controller and touch input.
- Puzzle family: overlapping exact-sum equations on hex-grid lines.
- Primary creator and official storefront sources:
  - **[P1]** [Hexologic on Steam](https://store.steampowered.com/app/785890/Hexologic/),
    for developer, release, single-player product, authored worlds and the
    official rule that pips in three directions must sum to edge clues.
  - **[P2]** [Hexologic on Nintendo](https://www.nintendo.com/es-mx/store/products/hexologic-switch/),
    for the same developer-supplied three-direction rule, 90-plus level supply,
    one-player boundary and Switch release date.
- Reproducible boundary and solution evidence:
  - **[S1]** [wolftooth — levels 1–15 gameplay walkthrough](https://www.youtube.com/watch?v=PlsKv4Cn6ZE),
    a continuous no-commentary record of the complete scoped family.
  - **[S2]** [XboxAchievements guide](https://www.xboxachievements.com/game/hexologic/guide/),
    for the 15-level family cadence, levels 1–15 as the basic set, level 16's
    immutable grey cells, 1–3 assignments and later linked-cell exclusion.
- Contemporary and specialised corroboration:
  - **[S3]** [oprainfall review](https://operationrainfall.com/2018/07/13/review_hexologic/),
    for the three line directions, intersections, green exact-total feedback,
    incomplete local correctness and later linked / locked-cell separation.
  - **[S4]** [Droid Gamers review](https://www.droidgamers.com/reviews/hexologic-review/),
    for tap assignment, the 1–3 solution domain, invalid zero state and
    cross-line arithmetic deduction.
  - **[S5]** [GamingBoulevard analysis](https://gamingboulevard.com/2018/06/indie-corner-hexologic/),
    for arrow direction, exact sums, one-value cells and green line feedback.
  - **[S6]** [MythicOwl's Kongregate release](https://www.kongregate.com/en/games/mythicowl/hexologic),
    for mouse placement, one-to-three dots and exact arrow-line totals.
  - **[S7]** [TrueAchievements walkthrough](https://www.trueachievements.com/game/Hexologic/walkthrough),
    for the level-15 boundary and the transition to later level families.
- Claim IDs: `HEX-001`–`HEX-011`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign a symbol to an open position. One tap addresses one
  editable hex and records one value from the domain `{1, 2, 3}`; later taps
  replace that proposed value. Cycling is an input-medium parameter of direct
  assignment, not a new mechanical action.
- Empty zero is an initial incomplete state rather than an accepted solution
  symbol. Candidate annotations and reset controls are excluded interface
  layers.
- Claim IDs: `HEX-003`, `HEX-009`.

### System Behaviour Genes

- None. Current sums and completion are evaluated continuously, but no distinct
  object transformation, random successor or autonomous step follows an
  assignment in the scoped family.
- The green border is classified under information because it reports a
  predicate without changing the arithmetic state or future action set.
- Claim IDs: `HEX-007`, `HEX-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each authored puzzle preserves one
  finite arrangement of individually addressable hexagonal cells.
- `CON-109` — overlapping exact line-sum satisfaction. Every clued line's
  assigned values must add to its visible target, and one cell at an
  intersection contributes the same value to every line that contains it.
- The domain `{1, 2, 3}`, line membership, axis and target are parameters. They
  do not create all-different coverage: repeated values in one line are legal.
- Claim IDs: `HEX-002`, `HEX-004`–`HEX-006`, `HEX-009`.

### Information Genes

- `INF-001` — fully visible current state. The complete fixed board, all arrow
  clues, every current pip assignment and every satisfied-line border are
  visible before the next choice.
- `INF-029` — visible exact directional line-sum clue. Each arrow discloses one
  fixed member line and its exact required numeric total without specifying
  the individual cell values.
- `INF-030` — live exact-subconstraint satisfaction indication. A green border
  reports that a particular line currently equals its target, while correctly
  avoiding the stronger claim that its internal values are globally final.
- Claim IDs: `HEX-002`, `HEX-004`, `HEX-007`, `HEX-008`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Every hex must hold
  one valid value and all declared line equations must hold simultaneously.
- Completing an individual green line is not a separate objective; it is one
  currently satisfied conjunct of the full assignment.
- Claim IDs: `HEX-008`, `HEX-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. The player may pause or revise any
  editable value between taps without a time-driven state change.
- Border animation duration and speedrun timing are presentation or external
  evaluation, not part of the scoped decision clock.
- Claim IDs: `HEX-003`, `HEX-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One blank editable cell lies on a clued line | Tap that cell once | It displays one pip while every other cell remains unchanged | Addressed bounded-value assignment | `HEX-003` |
| The same cell currently shows one pip | Tap it twice more, one tap at a time | Its proposal advances through two and three pips | Replaceable 1–3 assignment domain | `HEX-003` |
| A two-cell line has target 4 and currently holds one and two pips | Change the second cell to three | The line total becomes four and its clue border turns green | Exact-sum rule and live equality feedback | `HEX-004`, `HEX-007` |
| Two clued lines cross at one two-pip cell | Change the shared cell to three | Both current line totals increase by one | One shared assignment participates in overlapping equations | `HEX-005`, `HEX-006` |
| One target line is green but a crossing target cannot be met with its other cells | Rearrange values within the green line while preserving or later restoring its sum | The first line's local total is not proof that its cells are globally final | Local versus global satisfaction boundary | `HEX-008` |
| Every clued line is satisfied but one unclued-member cell is still blank | Leave the cell at zero | The puzzle remains incomplete | Complete assignment is required in addition to clue equality | `HEX-009` |
| Every cell has 1–3 pips and every displayed line equals its target | Make the final required assignment | The authored level completes | Conjunctive functional objective | `HEX-009` |

## Strategic and experiential structure

- Local decision: assign or revise one cell while comparing the remaining sum
  on each incident clue line with the feasible `1..3` range of its blanks.
- Medium-term planning: solve tight lines first, propagate a shared value into
  intersecting equations and preserve alternative decompositions of a total
  until crossings distinguish them.
- Long-term structure: find one complete bounded integer assignment satisfying
  the visible sparse system of overlapping line equations.
- Common heuristics: subtract already assigned pips; use minimum and maximum
  remaining totals; prioritise short or extreme-total lines; treat a green line
  as an equation met, not immutable cell truth; revisit ambiguous permutations
  at intersections.
- Failure attribution: no random event changes the board. A contradiction is
  attributable to an earlier value hypothesis or to mistaking one locally
  correct total for a globally compatible arrangement.
- Claim IDs: `HEX-002`–`HEX-010`.

## Replay and variation

- What changes between scoped instances: cell topology, line length, arrow
  direction, target sums, intersection pattern and number of unclued lines.
- Randomness or procedural generation: none during the selected authored
  levels. Later Infinite Mode is excluded from both state and supply claims.
- Multiple viable strategies: deduction order and temporary values can differ;
  the evidence does not justify claiming every puzzle has one unique sequence
  of taps or even one unique assignment unless separately proven.
- Typical replay motive: revise an inconsistent hypothesis, solve the next
  authored layout or compare a different deduction order.
- Claim IDs: `HEX-001`, `HEX-008`–`HEX-011`.

## Adjacent systems and history

- Sudoku is a close control because it also assigns visible bounded symbols to
  overlapping units, but Sudoku's units are all-different domain coverage with
  immutable givens, not arithmetic sums.
- Nonogram also couples cells through intersecting line descriptions, but its
  domain is binary and each clue is an ordered run grammar rather than one
  numeric total.
- Minesweeper exposes exact local counts over concealed hazard classes and
  resolves through reveal. Hexologic exposes all current proposals, assigns
  positive values directly and sums fixed whole lines.
- Hexcells Infinite shares hex presentation and numeric clues but classifies
  concealed binary cells under neighbourhood and contiguity qualifiers;
  neither the hexagons nor the use of digits establish mechanical identity.
- Claim IDs: `HEX-002`–`HEX-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | tap cycling and erasure controls |
| System Behaviour | none | completion animation |
| Constraint | `CON-001`, `CON-109` | topology, line membership, value domain and targets |
| Information | `INF-001`, `INF-029`, `INF-030` | arrow notation, colours and border animation |
| Objective | `OBJ-006` | accepted completion timing and uniqueness guarantee |
| Time | `TIM-002` | pause duration and touch sampling |

Canonical signature:

`ACT-007; none; CON-001,CON-109; INF-001,INF-029,INF-030; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `61` (`GAME-0001`–`GAME-0061`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`5 / 10 = 0.500000`); `GAME-0008` — Nonogram (`5 / 10 = 0.500000`).
- Supported combination subsets: `COMB-0062`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku preserves immutable givens and all-different coverage; Hexologic permits repeated values and satisfies exact arithmetic lines with live local feedback | Near, `0.500000` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram assigns binary cell classes from ordered orthogonal run clues; Hexologic assigns 1–3 and couples three-axis lines by exact totals | Near, `0.500000` |

### Preserved research notes

- New genes: `CON-109`, `INF-029`, `INF-030`.
- Generalised genes: `ACT-007`, `CON-001`, `INF-001`, `OBJ-006` and
  `TIM-002` gain a corroborating Hexologic support case without widening their
  operational boundaries.
- Classification result: one new constraint gene, two new information genes
  and one new verified combination.
- Evidence and reasoning: exact numeric equality, directional line membership
  and live predicate feedback change deductions independently of finite board
  geometry, direct assignment and completion.

## Taxonomy impact

- Registry changes: add `CON-109`, `INF-029` and `INF-030`; extend evidence for
  five recurring genes while preserving every prior signature.
- Taxonomy-change record: none. Neighbour-count clues, ordered run clues and
  all-different units remain distinct operational constraints.
- Candidate terms affected: exact line sums, intersecting equations and live
  local predicate feedback.
- Claim IDs: `HEX-003`–`HEX-009`.

## Negative results

- `CON-010` rejected: repeated values in one line are legal, and no line must
  contain every domain symbol exactly once.
- `INF-004` rejected: clues sum visible assigned magnitudes over whole lines;
  they do not count concealed members of one target class in a local
  neighbourhood.
- `INF-006` rejected: one total contains no ordered run-length grammar.
- `INF-023` rejected: green feedback is live before any complete answer
  submission and reports satisfaction rather than locating a rejected clue.
- Hexagonal rendering is a topology parameter, not a new gene or evidence of
  kinship with Hexcells Infinite.
- Hard, Infinite and later modules are excluded and therefore add no random,
  immutable-value, linked-assignment or optimisation genes.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Levels 1–15 are one complete authored basic
  family of direct 1–3 assignments under overlapping exact line sums; level 16
  begins the next mechanic family (`HEX-001`–`HEX-011`).

## Нові гени

- [Observation | Corroborated | High] `CON-109` — overlapping exact line-sum
  satisfaction.
- [Observation | Corroborated | High] `INF-029` — visible exact directional
  line-sum clue.
- [Observation | Corroborated | High] `INF-030` — live exact-subconstraint
  satisfaction indication.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0062` — overlapping exact-sum lines
  over bounded cell values.

## Зміни таксономії

- None. Existing assignment, visibility, complete-answer and self-paced genes
  gain one new support case without a definition change.

## Нові питання

- Do later operator tiles (`=`, `<`, `>`) constitute a distinct relation-clue
  grammar or only another parameterised equation family?
- Does Infinite Mode preserve deductive solvability, and is its generation
  state relevant only between puzzles or also during an attempt?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Rush Hour.
- Optimisation criterion: move from static arithmetic assignment to constrained
  sliding-object reachability while retaining a fully visible deterministic
  authored instance as the control.
- Expected information gain: test whether existing sliding, obstruction and
  delivery genes cover length-two and length-three vehicles whose motion is
  permanently axis-locked.
- Backlog impact: retain levels 16+, Hard and Infinite Hexologic as optional
  modular expansions instead of blending them into the arithmetic baseline.

## Чому саме вона

- [Hypothesis | Corroborated | High] Rush Hour is mechanically distant from
  Hexologic's equation solving, has primary published rules and fixed challenge
  cards, and can expose a clean recurrence-versus-new-axis-lock boundary for
  the eighth unit of this Goal.
