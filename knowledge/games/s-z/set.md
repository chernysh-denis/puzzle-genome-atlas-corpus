---
game_id: GAME-0064
slug: set
game_title: SET
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0064
gene_ids:
  action:
    - ACT-021
  system: []
  constraint:
    - CON-110
  information:
    - INF-001
  objective:
    - OBJ-040
  time:
    - TIM-002
---

# Game: SET

## Analysis scope

- Version / ruleset: the official Basic SET solitaire procedure, restricted to
  one reproducible visible 12-card field encoded from the standard 81-card deck.
- Included: four independent card attributes—number, colour, shape and
  shading—with three values each; one unique card for every attribute tuple;
  twelve simultaneously visible cards; selecting exactly three distinct field
  cards; accepting the selection only when every attribute is independently
  either equal on all three cards or different on all three; retaining one
  found SET; self-paced inspection and immediate rule checking. The fixed
  control field below contains exactly one SET, at positions `3`, `6` and `11`.
- Excluded: competitive races and the call / pickup deadline; other players,
  penalties and scoring comparisons; continued replacement draws; the
  no-SET three-card expansion; deck exhaustion; Easy Start; Daily Puzzle,
  SET Junior, CO-OP SET and every other variant; visual-search speed,
  colour-vision accessibility and presentation.
- Direct-play status: not conducted. The current publisher page and archived
  official instructions establish the deck, predicate and solo availability.
  The Mathematical Association of America and two mathematical treatments
  independently corroborate the `3^4` deck and coordinate-wise predicate. A
  local exhaustive check tested all `C(12,3) = 220` triples in the recorded
  field and found exactly one accepted triple.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SET-001` | The standard deck contains 81 unique cards, one for each tuple of four three-valued attributes | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `SET-002` | A Basic SET field begins with 12 face-up cards | Confirmed | Corroborated | High | P2, S1–S3 |
| `SET-003` | A candidate contains exactly three distinct visible cards | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `SET-004` | For each attribute independently, a candidate is valid only when all three values are equal or all three are different | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `SET-005` | Two equal and one different value in any single attribute rejects the whole candidate | Confirmed | Direct | High | P2, S1 |
| `SET-006` | The official rules explicitly support one-player solitaire | Confirmed | Direct | High | P1, P2 |
| `SET-007` | If solitaire search finds no SET, three cards are added and a penalty must later be removed from the last 12 | Confirmed | Direct | High | P2 |
| `SET-008` | The bounded control field has 12 unique cards, balanced attribute frequencies and exactly one valid triple, positions `3`, `6`, `11` | Confirmed | Direct | High | R1 |
| `SET-009` | Every decision-relevant attribute of all 12 current cards is simultaneously visible | Observation | Corroborated | High | P2, S1–S3 |
| `SET-010` | Given any two standard-deck cards, exactly one third deck card completes their SET | Confirmed | Corroborated | High | S1–S3 |

## Basic data

- Release / origin: Marsha Falco devised SET from a genetics data-coding system
  in 1974; it was commercially published in 1990. The scoped product is the
  current PlayMonster standard 81-card edition, item 1000.
- Platform or physical form: single- or multiplayer physical card game. This
  record isolates one solitaire visual-classification decision.
- Puzzle family: coordinate-wise relational subset recognition.
- Primary and official sources:
  - **[P1]** [PlayMonster product page](https://playmonster.com/product/set/),
    for the 81-card contents, solo support and the four-feature all-same / all-
    different rule.
  - **[P2]** [official English instructions](https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf),
    for the 12-card field, exactly-three selection, independent feature test,
    invalid two-plus-one boundary and solitaire expansion / penalty. The legacy
    host presented an expired TLS certificate on 2026-08-13; the document was
    retrieved only for source review and its claims were independently checked.
- Independent and mathematical corroboration:
  - **[S1]** Gordon and McMahon,
    [“On Your Mark, Get SET, Geometry!”](https://maa.org/math-values/on-your-mark-get-set-geometry/),
    Mathematical Association of America, for the attributes, 12-card procedure,
    coordinate-wise predicate and unique completion of any pair.
  - **[S2]** Sangchampa, Saiphet and Uiyyasathian,
    [“SET Game and Affine Geometry”](https://ejournals.swu.ac.th/index.php/sej/article/view/9451),
    for 81 unique cards and the `AG(4,3)` model.
  - **[S3]** McCullagh,
    [“SET and Affine Caps”](https://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/McCullagh.pdf),
    for the 12-card layout, four three-valued dimensions and formal SET rule.
- Reproducible computational evidence:
  - **[R1]** Encode a card as `(number, colour, shape, shading)` in
    `{0,1,2}^4`. The control field is
    `[(2,1,0,2),(0,1,2,0),(1,2,0,2),(1,2,1,2),`
    `(0,0,0,0),(2,0,1,0),(1,2,1,1),(2,1,1,1),`
    `(2,0,2,0),(0,2,0,2),(0,1,2,1),(1,0,2,1)]`.
    Exhaustively accept a triple when each coordinate sums to `0 mod 3`.
    Exactly positions `(3,6,11)` pass. Each coordinate value occurs four times.
- Claim IDs: `SET-001`–`SET-010`.

## Mechanical decomposition

### Action Genes

- `ACT-021` — commit selected visible-card subset. The player chooses exactly
  three distinct cards from the current face-up field and commits that subset
  for rule evaluation.
- The selected zone is a parameter. SET demonstrates that the gene is not
  limited to cards held privately in a hand; no new action ID is required.
- Claim IDs: `SET-002`, `SET-003`.

### System Behaviour Genes

- None in the bounded physical-solitaire decision. The player applies the
  printed predicate and retains a valid triple; no automatic digital
  classifier, replacement draw or score resolver is assumed.
- Continued-deck replacement and no-SET expansion are deliberately outside the
  one-field boundary rather than silently classified as system behaviour.
- Claim IDs: `SET-004`–`SET-007`.

### Constraint Genes

- `CON-110` — coordinate-wise ternary same-or-all-different subset predicate.
  Exactly three distinct cards are legal only when, for each of the four
  attributes independently, their values are all equal or all different.
- Number, colour, shape, shading, their concrete labels and the fixed arity
  `4 × 3` are parameters of one predicate, not separate genes.
- Claim IDs: `SET-001`, `SET-003`–`SET-005`, `SET-010`.

### Information Genes

- `INF-001` — fully visible current state. All twelve card identities and every
  decision-relevant feature are inspectable before a triple is selected.
- The order of excluded replacement cards is irrelevant to this fixed-field
  decision, so neither concealed-current-state nor future-randomness genes are
  asserted.
- Claim IDs: `SET-002`, `SET-009`.

### Objective Genes

- `OBJ-040` — identify one valid relational subset. Completion of this bounded
  solitaire unit requires finding and retaining one exactly-three subset that
  satisfies the declared coordinate-wise relation.
- Maximising sets across an exhausted deck and competing for highest score are
  broader-session objectives excluded here.
- Claim IDs: `SET-003`, `SET-004`, `SET-008`.

### Time Genes

- `TIM-002` — self-paced sequential action. The solo player may inspect the
  visible field without a deadline and commit one candidate when ready.
- The multiplayer call race and pickup interval are excluded, so no real-time
  gene enters this genome.
- Claim IDs: `SET-006`, `SET-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Control-field positions `3`, `6`, `11` are `2 purple open diamonds`, `3 red solid ovals`, `1 green striped squiggle` | Select all three | Count, colour, shape and shading are each all different; candidate is accepted | Four coordinates are tested independently | `SET-004`, `SET-008` |
| Positions `1`, `3`, `5` are selected | Compare every attribute | Count and colour are all different, shape is all equal, but shading is `outline, outline, solid`; whole candidate is rejected | One two-plus-one attribute rejects an otherwise valid-looking triple | `SET-005`, `SET-008` |
| Two visible cards agree in one attribute | Determine the only possible completion | Third card must share that value in the coordinate | Equal pair forces the same third coordinate | `SET-010` |
| Two visible cards differ in one attribute | Determine the only possible completion | Third card must use the missing coordinate value | Unequal pair forces the third distinct value | `SET-010` |
| All 220 triples in the control field are enumerated | Apply the predicate to each | Only `(3,6,11)` passes | The depicted field has exactly one solution, not a decorative coincidence | `SET-008` |

## Strategic and experiential structure

- Local decision: compare three cards one attribute at a time and immediately
  reject any two-plus-one coordinate.
- Medium-term planning: choose two cards, derive the unique required third
  tuple, then search the visible field for that exact card.
- Long-term structure: excluded in this one-field boundary; no replacement
  sequence or deck-exhaustion plan is claimed.
- Common heuristics: use the two-plus-one rejection shortcut; encode each
  attribute as `0/1/2`; search pair completions rather than all triples.
- Failure attribution: every relevant value is visible and the predicate is
  exact, so a rejected candidate follows from a named attribute mismatch.
- Player-trust factors: acceptance has no hidden tie-break, visual proximity or
  semantic category; all four printed attributes have equal logical status.
- Claim IDs: `SET-003`–`SET-005`, `SET-008`–`SET-010`.

## Replay and variation

- What changes between sessions: an ordinary shuffled deal changes the visible
  12-card subset and number / location of SETs.
- Randomness or procedural generation: setup shuffle supplies a field, but the
  scoped control field is fixed before the decision and no random event occurs
  between inspection and commitment.
- Multiple viable strategies: scan complete triples, derive the third card from
  pairs or group visually by one attribute; all use the same predicate.
- Typical replay motive: recognise valid relations faster across new fields.
- Claim IDs: `SET-001`, `SET-002`, `SET-006`, `SET-010`.

## Adjacent systems and history

- Balatro also commits a visible card subset, but accepts several ranked poker
  predicates, consumes action resources, draws from concealed order and scores
  through modifiers. SET has one unranked four-coordinate legality relation.
- Sudoku and Nonogram also expose a complete finite puzzle state for self-paced
  constraint reasoning, but require full position assignments rather than
  selecting one already-present relational subset.
- Spot It! searches a shared symbol between two cards; SET instead requires a
  three-card relation to hold independently in every attribute.
- The attribute vocabulary came from Falco's genetics record-keeping, but
  origin does not make genetics a mechanic.
- Claim IDs: `SET-001`–`SET-006`, `SET-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-021` | visible field zone, exact commit size `3` |
| System Behaviour | none | none within fixed-field physical solitaire |
| Constraint | `CON-110` | four coordinates, three values each |
| Information | `INF-001` | simultaneous face-up field |
| Objective | `OBJ-040` | one accepted triple |
| Time | `TIM-002` | no solo deadline |

Canonical signature:

`ACT-021; none; CON-110; INF-001; OBJ-040; TIM-002`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`–`GAME-0063`.
- Indexed combinations scanned: every verified record `COMB-0001`–`COMB-0063`.
- Exact genome matches: none.
- Existing combination subsets: none. Every prior combination gene set was
  tested as a proper subset of the five-gene signature and rejected.
- Near match tie: `GAME-0002` Rubik's Cube, `GAME-0005` Sudoku, `GAME-0008`
  Nonogram and `GAME-0063` Rush Hour each share `INF-001`, `TIM-002` at
  `2 / 10 = 0.200000`. Hexologic, Carto and FreeCell
  follow at `2 / 11 = 0.181818`. Balatro shares only generalised `ACT-021` at
  `1 / 17 = 0.058824` and is retained as the action-boundary control.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 18 = 0.055556`; `GAME-0002`: `2 / 10 = 0.200000`;
    `GAME-0003`: `0 / 14 = 0.000000`; `GAME-0004`: `1 / 19 = 0.052632`;
    `GAME-0005`: `2 / 10 = 0.200000`; `GAME-0006`: `2 / 12 = 0.166667`;
    `GAME-0007`: `2 / 11 = 0.181818`; `GAME-0008`: `2 / 10 = 0.200000`;
    `GAME-0009`: `1 / 20 = 0.050000`; `GAME-0010`: `1 / 13 = 0.076923`;
    `GAME-0011`: `2 / 16 = 0.125000`; `GAME-0012`: `2 / 12 = 0.166667`;
    `GAME-0013`: `1 / 17 = 0.058824`; `GAME-0014`: `1 / 19 = 0.052632`;
    `GAME-0015`: `1 / 18 = 0.055556`; `GAME-0016`: `1 / 19 = 0.052632`;
    `GAME-0017`: `1 / 17 = 0.058824`; `GAME-0018`: `1 / 23 = 0.043478`;
    `GAME-0019`: `1 / 14 = 0.071429`; `GAME-0020`: `1 / 18 = 0.055556`;
    `GAME-0021`: `1 / 13 = 0.076923`; `GAME-0022`: `1 / 16 = 0.062500`;
    `GAME-0023`: `1 / 14 = 0.071429`; `GAME-0024`: `1 / 16 = 0.062500`;
    `GAME-0025`: `1 / 15 = 0.066667`; `GAME-0026`: `1 / 16 = 0.062500`;
    `GAME-0027`: `1 / 16 = 0.062500`; `GAME-0028`: `1 / 21 = 0.047619`;
    `GAME-0029`: `1 / 16 = 0.062500`; `GAME-0030`: `1 / 18 = 0.055556`;
    `GAME-0031`: `1 / 15 = 0.066667`; `GAME-0032`: `1 / 15 = 0.066667`;
    `GAME-0033`: `1 / 17 = 0.058824`; `GAME-0034`: `1 / 18 = 0.055556`;
    `GAME-0035`: `1 / 22 = 0.045455`; `GAME-0036`: `2 / 15 = 0.133333`;
    `GAME-0037`: `1 / 13 = 0.076923`; `GAME-0038`: `1 / 20 = 0.050000`;
    `GAME-0039`: `2 / 12 = 0.166667`; `GAME-0040`: `2 / 11 = 0.181818`;
    `GAME-0041`: `1 / 15 = 0.066667`; `GAME-0042`: `1 / 13 = 0.076923`;
    `GAME-0043`: `1 / 18 = 0.055556`; `GAME-0044`: `1 / 14 = 0.071429`;
    `GAME-0045`: `1 / 18 = 0.055556`; `GAME-0046`: `2 / 13 = 0.153846`;
    `GAME-0047`: `1 / 18 = 0.055556`; `GAME-0048`: `1 / 18 = 0.055556`;
    `GAME-0049`: `0 / 14 = 0.000000`; `GAME-0050`: `1 / 19 = 0.052632`;
    `GAME-0051`: `1 / 20 = 0.050000`; `GAME-0052`: `1 / 14 = 0.071429`;
    `GAME-0053`: `1 / 13 = 0.076923`; `GAME-0054`: `1 / 15 = 0.066667`;
    `GAME-0055`: `1 / 14 = 0.071429`; `GAME-0056`: `1 / 12 = 0.083333`;
    `GAME-0057`: `1 / 12 = 0.083333`; `GAME-0058`: `1 / 13 = 0.076923`;
    `GAME-0059`: `1 / 11 = 0.090909`; `GAME-0060`: `1 / 11 = 0.090909`;
    `GAME-0061`: `2 / 13 = 0.153846`; `GAME-0062`: `2 / 11 = 0.181818`;
    `GAME-0063`: `2 / 10 = 0.200000`.
- Scan date: 2026-08-13.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `INF-001`, `TIM-002` | Sudoku creates a complete 81-position assignment under all-different units; SET selects one existing three-card relation | Tied nearest, `0.200000` |
| `GAME-0008` — Nonogram | `INF-001`, `TIM-002` | Nonogram assigns every cell from ordered run clues; SET changes no attribute values and needs one accepted subset | Tied nearest, `0.200000` |
| `GAME-0002` — Rubik's Cube | `INF-001`, `TIM-002` | Rubik's Cube transforms a permutation through reversible layer rotations; SET only classifies a visible triple | Tied nearest, `0.200000` |
| `GAME-0063` — Rush Hour | `INF-001`, `TIM-002` | Rush Hour rearranges persistent rigid blocks to extract one; SET leaves the field unchanged and identifies a relation | Tied nearest, `0.200000` |
| `GAME-0017` — Balatro | `ACT-021` | Balatro commits up to five held cards into ranked scoring / discard systems under concealed draws and budgets; SET commits exactly three face-up cards to one unranked legality predicate | Action-boundary control, `0.058824` |

- New genes: `CON-110`, `OBJ-040`.
- Generalised genes: `ACT-021` now covers committing a selected subset from a
  visible hand or face-up field; its card zone is a parameter.
- Classification result: two new genes and one new combination around a reused
  subset-commit action.
- Evidence and reasoning: SET's relation is neither poker-hand precedence nor
  generic equality. It conjunctively evaluates every coordinate and rejects a
  two-plus-one split in any one coordinate. Finding one already-present valid
  subset is also distinct from completing a global assignment.

## Taxonomy impact

- Registry changes: generalise `ACT-021`; add `CON-110` and `OBJ-040`; add SET
  as evidence for `INF-001` and `TIM-002`.
- Taxonomy-change record: none. Balatro remains within the broader action
  boundary, while its hand-only description is corrected without changing its
  signature.
- Candidate terms affected: visible-card subset commitment, coordinate-wise
  ternary relation and relational-subset discovery.

## Negative results

- `CON-045` rejected: SET has one unranked predicate; it does not choose the
  highest-precedence member of overlapping poker-hand classes.
- `SYS-027` rejected: the bounded physical solitaire procedure does not supply
  an automatic classifier, and there is no pattern hierarchy.
- `OBJ-006` rejected: the player neither fills positions nor completes a total
  assignment; card attributes pre-exist and remain unchanged.
- `INF-003` and `INF-002` rejected: the fixed control field is fully visible,
  and excluded replacement order cannot affect the current decision.
- `OBJ-002` rejected: one-field completion is finding one SET, not maximising a
  session score.
- No claim of mechanic ownership follows from trademarked visual vocabulary;
  Atlas artwork uses original symbols while preserving the abstract relation.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] A SET is an exactly-three relation over four
  independent three-valued coordinates; one two-plus-one coordinate rejects
  the whole candidate (`SET-003`–`SET-005`).
- [Confirmed | Direct | High] The 12-card control field has exactly one valid
  triple among 220 candidates, positions `3`, `6`, `11` (`SET-008`).

## Нові гени

- [Observation | Corroborated | High] `CON-110` — coordinate-wise ternary
  same-or-all-different subset predicate.
- [Observation | Corroborated | High] `OBJ-040` — identify one valid relational
  subset.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0064` — visible exactly-three
  coordinate-relation discovery.

## Зміни таксономії

- [Observation | Corroborated | High] `ACT-021` now treats hand versus face-up
  field as a card-zone parameter; Balatro's existing signature is unchanged.

## Нові питання

- Does a full solitaire deck session need a distinct no-match tableau-expansion
  interaction once replacement order and penalty are admitted into scope?
- Should accessibility transformations of colour preserve one-to-one attribute
  identity as presentation, or can they become mechanically relevant aids?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Mastermind, bounded to one standard
  four-peg code with six colours and duplicate colours permitted.
- Optimisation criterion: retain exact finite relational reasoning while moving
  from complete visibility to repeated hypotheses against partitioned feedback.
- Expected information gain: test concealed target information, structured
  proposal submission and exact-position / wrong-position feedback without
  conflating feedback pegs with direct clue constraints.
- Backlog impact: retain full-deck SET solitaire as a later expansion audit.

## Чому саме вона

- [Hypothesis | Corroborated | High] Mastermind is mechanically distant from
  the recent spatial run yet provides a sharp falsification boundary for SET's
  visible relation and the Atlas's existing concealed-state deduction genes.
