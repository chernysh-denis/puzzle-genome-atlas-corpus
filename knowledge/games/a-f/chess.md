---
game_id: GAME-0011
slug: chess
game_title: Chess
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0011
gene_ids:
  action:
    - ACT-014
    - ACT-015
  system: []
  constraint:
    - CON-001
    - CON-023
    - CON-024
    - CON-025
    - CON-026
    - CON-027
  information:
    - INF-001
    - INF-007
  objective:
    - OBJ-009
  time:
    - TIM-002
    - TIM-004
---

# Game: Chess

## Analysis scope

- Version / ruleset: standard over-the-board chess under the FIDE Laws of
  Chess taking effect 1 January 2023, which remain the current Laws listed in
  the FIDE Handbook at the review date.
- Included: the initial 8 × 8 position; alternating White and Black moves;
  piece-specific movement; blocking; capture; check legality; castling;
  en-passant capture; player-chosen promotion; checkmate; stalemate; dead
  positions; automatic fivefold repetition and 75-move draws.
- Excluded: chess clocks, touch-move procedure, notation duties, arbiters,
  penalties, draw offers, claim-dependent threefold / 50-move draws,
  resignation, tournament scoring, ratings, opening books, engine assistance,
  online premoves and variants such as Chess960.
- Direct-play status: not conducted for this record. The mechanical model is
  derived from FIDE's official rules; commonplace strategic observations are
  bounded separately from rule claims.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CHS-001` | Chess has two opposing sides; White moves first and the sides then alternate | Confirmed | Direct | High | F1 |
| `CHS-002` | Each piece class has declared movement geometry and line pieces cannot cross intervening pieces | Confirmed | Direct | High | F1 |
| `CHS-003` | Moving to a square occupied by an opponent captures and removes that piece as part of the move | Confirmed | Direct | High | F1 |
| `CHS-004` | A legal move may not leave or place the moving side's king in check | Confirmed | Direct | High | F1 |
| `CHS-005` | Castling and en-passant eligibility depend on prior moves, not placement alone | Confirmed | Direct | High | F1 |
| `CHS-006` | A pawn reaching the furthest rank is replaced immediately by a player-chosen queen, rook, bishop or knight | Confirmed | Direct | High | F1 |
| `CHS-007` | Checkmate is an attacked king with no legal escape and ends the game without king capture | Confirmed | Direct | High | F1 |
| `CHS-008` | Stalemate and dead position end the game as draws | Confirmed | Direct | High | F1 |
| `CHS-009` | Fivefold repetition and 75 moves per side without pawn move or capture produce automatic draws, with checkmate precedence on the final move | Confirmed | Direct | High | F1 |
| `CHS-010` | Every in-scope state variable is public, but some rights and draw counters require action history | Observation | Corroborated | High | CHS-001–CHS-009 |
| `CHS-011` | The opponent's move is another player's action rather than an automatic system behaviour | Observation | Corroborated | High | CHS-001 |
| `CHS-012` | The six-type model can encode alternating agency without adding a seventh type | Observation | Corroborated | Medium | CHS-001–CHS-011 |

## Basic data

- Release / origin: the FIDE historical account traces chess through its early
  Indian form and later transformations; this record analyses only the modern
  standard rules, not one commercial release.
- Platform or physical form: physical board game, also widely implemented
  digitally.
- Puzzle family: deterministic, adversarial, perfect-information abstract
  strategy game.
- Primary rules source:
  - **[F1]** [FIDE Laws of Chess](https://handbook.fide.com/chapter/e012023),
    approved in 2022 and effective from 1 January 2023. Articles 1–5 define
    alternating play, movement, check, checkmate, stalemate and dead position;
    Article 9 defines repetition and no-progress draws.
- Historical context:
  - **[F2]** [FIDE's chess history account](https://museum.fide.com/) places
    the game's continuous early history in northern India while acknowledging
    uncertainty around its earliest development.
- Claim IDs: `CHS-001`–`CHS-012`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate a selected controlled board piece. The acting player
  chooses one owned piece and its legal destination. Occupying an opposing
  piece's square specifies its capture; castling is the rules-declared compound
  exception in which the king move also relocates a rook.
- `ACT-015` — choose promotion replacement type. A terminal-rank pawn move
  additionally requires the player to select queen, rook, bishop or knight;
  the choice is not restricted by previously captured material.
- Capture is not a second independent action gene: source and destination
  already determine the captured piece. Check is a relation, not a command.
- Draw offers, claims and resignation are excluded voluntary procedures rather
  than moves in the scoped positional game.
- Claim IDs: `CHS-002`, `CHS-003`, `CHS-006`.

### System Behaviour Genes

- Active genes: none.
- An opponent response is produced by another decision-maker using the same
  Action genes; classifying it as an automatic system transition would erase
  the central source of agency and strategic uncertainty.
- Capture removal, castling rook relocation and promotion replacement are
  components of the chosen move under the physical rules, not an independent
  post-action state process.
- Claim IDs: `CHS-001`, `CHS-003`, `CHS-006`, `CHS-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The standard board retains 64
  individually addressed squares throughout play.
- `CON-023` — side-owned piece control. White can move only white pieces and
  Black only black pieces on their respective turns.
- `CON-024` — piece-class movement and line obstruction. Each class has its own
  vectors; bishop, rook and queen paths cannot cross occupancy, while the
  knight's destination rule ignores intervening squares.
- `CON-025` — own-king attack prohibition. A candidate move is illegal if its
  result leaves or places the acting side's king in check. Castling also tests
  the king's start, transit and destination squares.
- `CON-026` — history-sensitive position rights and counters. Identical piece
  placement can carry different castling rights, en-passant availability,
  repetition identity or no-progress count.
- `CON-027` — non-winning terminal draw predicate. Stalemate, dead position,
  fivefold repetition and the 75-move threshold end the scoped game without a
  winner.
- `CON-005` is absent. Captures, pawn movement, castling-right loss and history
  changes mean primitive chess moves do not all have legal state-restoring
  inverses.
- Claim IDs: `CHS-002`–`CHS-005`, `CHS-008`, `CHS-009`.

### Information Genes

- `INF-001` — fully visible current state. All pieces, ownership, squares and
  attacks are publicly inspectable; the scoped rules contain no hidden unit or
  random future event.
- `INF-007` — public action-history state. Castling and en-passant rights,
  position occurrences and the pawn-move / capture counter remain public and
  decision-relevant even when placement alone cannot reconstruct them.
- Strategic uncertainty about the opponent's future choice is not hidden
  information: the choice has not yet been made by that independent agent.
- Claim IDs: `CHS-005`, `CHS-009`–`CHS-011`.

### Objective Genes

- `OBJ-009` — checkmate the opposing royal piece. The target is an attacked
  opposing king for which no legal reply removes the attack.
- Material gain, space, development and promotion are instrumental evaluations,
  not terminal objectives in the formal rules.
- Capturing the king is illegal; the game terminates at checkmate before such a
  capture. Automatic draw predicates prevent either side from completing the
  objective in some terminal states.
- Claim IDs: `CHS-007`–`CHS-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. With clocks excluded, a player may
  deliberate between discrete moves and no state changes merely because time
  passes.
- `TIM-004` — alternating adversarial turns. White takes the first exclusive
  turn; each completed non-terminal move hands the next decision to Black, then
  control continues alternating.
- Alternation is not `TIM-001`: no system-owned resolution phase chooses or
  performs the opponent's reply.
- Claim IDs: `CHS-001`, `CHS-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| White to move in the initial position | Move pawn `e2` to `e4` | White pawn occupies `e4`; control passes to Black | Ownership, geometry and alternation | `CHS-001`, `CHS-002` |
| White bishop has a clear diagonal to a black piece | Move bishop onto that occupied square | Black piece is removed and bishop occupies the square | Destination-specified capture | `CHS-003` |
| A pinned piece could move geometrically but expose its king | Attempt that relocation | Move is illegal | Geometry alone does not determine legality | `CHS-004` |
| Same placement, but king or rook previously moved and returned | Attempt castling | Castling is illegal in the position with lost rights | History changes legal options | `CHS-005` |
| Opposing pawn has just advanced two squares beside a pawn | Capture en passant on the immediate reply | Opposing pawn is removed from its passed square | Transient public-history right | `CHS-005` |
| White pawn reaches the eighth rank | Choose a knight | Pawn is replaced by a white knight with immediate effect | Player-selected state transformation | `CHS-006` |
| Side to move is attacked and has no legal reply | Complete the mating move | Game ends with the mover winning | Checkmate, not king capture | `CHS-007` |
| Side to move is not attacked but has no legal move | Complete the preceding legal move | Game ends drawn | Stalemate differs from checkmate | `CHS-008` |
| Same position occurs for the fifth time | Complete the move creating it | Game ends drawn automatically | History-sensitive terminal threshold | `CHS-009` |

## Strategic and experiential structure

- Local decision: compare legal candidate moves, immediate threats, captures,
  checks and the opponent's best replies.
- Medium-term planning: develop pieces, coordinate attacks and defence, manage
  king safety, pawn structure, space and tactical sequences.
- Long-term structure: convert persistent positional advantages or material
  into a mating attack while preventing the opponent from doing the same.
- Common heuristics: consider forcing checks, captures and threats; avoid
  undefended losses; improve piece activity; evaluate the opponent's strongest
  response rather than treating the board as passive.
- Failure attribution: no random or hidden event intervenes, but the other
  player deliberately selects an adverse continuation. A legal move can lose
  because its forecast of that reply was incomplete.
- Player-trust factors: identical public rules and complete current information
  apply to both sides. History-dependent rights must remain mutually known.
- Claim IDs: `CHS-001`–`CHS-011`.

## Replay and variation

- What changes between sessions: the move sequence and resulting positions;
  the standard initial arrangement remains fixed.
- Randomness or procedural generation: none in the scoped game.
- Multiple viable strategies: opening choices branch rapidly into distinct
  tactical and positional plans, with the opponent selecting against them.
- Typical replay motive: face a different opponent or continuation, improve
  calculation and strategy, or examine alternative choices from a known
  position.
- Claim IDs: `CHS-001`, `CHS-010`, `CHS-011`.

## Adjacent systems and history

- Earlier chess forms and related games such as shatranj differ in piece powers
  and winning rules; they require independent decomposition rather than
  inheriting this genome.
- Chess960 changes the initial back-rank arrangement and castling mapping but
  preserves much of standard chess's action and agency structure.
- Checkers also alternates adversarial moves and captures, but uses different
  movement, forced-capture and promotion rules and has no check-constrained
  royal piece.
- Chess problems normally fix a composed position and task, sometimes with a
  specified move count; that is a different objective and information scope
  from playing a complete adversarial game.
- Claim IDs: `CHS-001`–`CHS-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-015` | castling as compound exception; promotion set |
| System Behaviour | none | opponent response explicitly excluded |
| Constraint | `CON-001`, `CON-023`, `CON-024`, `CON-025`, `CON-026`, `CON-027` | board geometry, piece classes and automatic draw thresholds |
| Information | `INF-001`, `INF-007` | formal record versus mutual memory |
| Objective | `OBJ-009` | checkmate relation |
| Time | `TIM-002`, `TIM-004` | White starts; clocks excluded |

Canonical signature:

`ACT-014,ACT-015; ; CON-001,CON-023,CON-024,CON-025,CON-026,CON-027; INF-001,INF-007; OBJ-009; TIM-002,TIM-004`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `10` (`GAME-0001`–`GAME-0010`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`3 / 17 = 0.176471`); `GAME-0005` — Sudoku (`3 / 17 = 0.176471`); `GAME-0008` — Nonogram (`3 / 17 = 0.176471`).
- Supported combination subsets: `COMB-0011`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `CON-001`, `INF-001`, `TIM-002` | Both are visible deterministic self-paced systems; Cube turns preserve material and are primitively reversible, while Chess alternates hostile ownership, captures and king-safety legality | Near, `0.176471` |
| `GAME-0005` — Sudoku | `CON-001`, `INF-001`, `TIM-002` | Sudoku assigns symbols against static all-different constraints; Chess relocates conserved and capturable pieces against an adapting opponent | Near, `0.176471` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001`, `TIM-002` | Nonogram resolves visible clues into one binary assignment; Chess's public history and opponent choices continually change the legal and useful move set | Near, `0.176471` |

### Preserved research notes

- New combination: `COMB-0011`, whose six genes are a proper subset of this
  thirteen-gene genome.
- New genes: `ACT-014`, `ACT-015`, `CON-023`, `CON-024`, `CON-025`,
  `CON-026`, `CON-027`, `INF-007`, `OBJ-009`, `TIM-004`.
- Classification result: `New gene`.
- Reused genes: `CON-001`, `INF-001`, `TIM-002`.
- Evidence and reasoning: alternating agency changes who selects the next move
  but not what an Action is. Public history is separated from visible placement
  because it changes both legal rights and terminal evaluation.

## Taxonomy impact

- Registry changes: ten bounded genes added and three reused.
- Taxonomy-change record: none. Opponent agency is represented by ownership
  constraints and turn scheduling; it does not behave like a system transition.
- Candidate terms affected: move pieces, capture, opponent response, access by
  ownership, movement geometry, check, public history, draw, promotion and
  alternating turns now have bounded mappings.
- Material value, mobility, centre control and tempo remain strategic
  evaluations or parameters rather than formal objectives.
- Claim IDs: `CHS-012`.

## Negative results

Chess has no active System Behaviour gene in this scope: the opponent is not
the system. `CON-005` is absent because capture, pawn movement and move-history
rights prevent universal primitive reversibility. Check is neither damage nor
king capture; it is part of move legality and the checkmate objective.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] The sides alternate independent choices, and the
  opponent's move is not an automatic response (`CHS-001`, `CHS-011`).
- [Confirmed | Direct | High] Identical placement can differ in castling,
  en-passant and draw state because public history is part of the position
  (`CHS-005`, `CHS-009`, `CHS-010`).
- [Confirmed | Direct | High] Checkmate ends the game before king capture;
  stalemate and dead position instead end it drawn (`CHS-007`, `CHS-008`).

## Нові гени

- [Observation | Direct | High] `ACT-014`, `ACT-015`, `CON-023`, `CON-024`,
  `CON-025`, `CON-026`, `CON-027`, `INF-007`, `OBJ-009` and `TIM-004`.
- [Observation | Corroborated | High] `CON-001`, `INF-001` and `TIM-002` are
  reused.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0011` — alternating threat-constrained
  movement toward checkmate.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Alternating
  agency fits Action, Constraint and Time without a new type.

## Нові питання

- TODO: compare Checkers to test reuse of ownership and alternating agency
  without own-king safety.
- TODO: compare a hidden-information adversarial game to separate public
  opponent choice from concealed opponent state.
- TODO: test whether claim-dependent draw procedures deserve Action genes in a
  competition-specific Chess genome.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0012` — Flow Free.
- Optimisation criterion: cover a connection / routing puzzle after the first
  adversarial system and satisfy the roadmap's outstanding flow-family target.
- Expected information gain: test endpoint-to-endpoint path construction,
  non-overlap, full-board coverage and whether continuous drag is one compound
  action or a sequence of cell assignments.
- Backlog impact: Flow Free moves from the coverage pool to the immediate task;
  Chess leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Flow Free is agency-distant from Chess and
  fills a known family gap while directly comparing connection constraints
  against Sudoku and Nonogram's static assignment structures.
