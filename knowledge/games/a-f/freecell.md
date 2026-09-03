---
game_id: GAME-0007
slug: freecell
game_title: FreeCell
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0007
gene_ids:
  action:
    - ACT-010
  system: []
  constraint:
    - CON-014
    - CON-015
    - CON-016
    - CON-017
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-002
---

# Game: FreeCell

## Analysis scope

- Version / ruleset: classic 52-card, eight-cascade, four-free-cell FreeCell
  represented by the widely used Microsoft-style rules.
- Included: all cards dealt face up; four cascades of seven cards and four of
  six; one-card free cells; exposed-card access; alternating-colour descending
  tableau construction; any card into an empty cascade; same-suit foundations
  built ace through king; manual single-card transfers.
- Excluded: automatic foundation moves, hints, undo, scoring, numbered-deal
  selection, animation and unrestricted multi-card dragging. A compound move
  is admitted only as a shortcut for a sequence of legal single-card moves.
- Direct-play status: not conducted. Rules were triangulated from a current
  commercial rules page, a long-running FreeCell rules/history archive and an
  academic planning-domain analysis. No claim is made that every possible deal
  is solvable or equally difficult.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FRC-001` | A standard deal places all 52 cards face up in eight cascades, four with seven cards and four with six | Confirmed | Corroborated | High | P1, P2 |
| `FRC-002` | Only an exposed cascade card or a card in a free cell can be transferred directly | Confirmed | Corroborated | High | P1, P2 |
| `FRC-003` | Each of four free cells holds at most one card | Confirmed | Corroborated | High | P1, P2 |
| `FRC-004` | Tableau cards build downward by alternating colour, while foundations build upward by suit from ace to king | Confirmed | Corroborated | High | P1, P2 |
| `FRC-005` | A multi-card transfer is legal only when available cells and empty cascades can realise the same transfer through primitive card moves | Confirmed | Corroborated | High | P1, P2, A1 |
| `FRC-006` | Success requires transferring the complete deck to the four suit foundations | Confirmed | Corroborated | High | P1, P2 |
| `FRC-007` | The current deal is fully visible and no random event occurs after play begins | Observation | Corroborated | High | FRC-001–FRC-006 |
| `FRC-008` | Free cells and empty cascades are temporary access resources rather than interchangeable generic capacity | Pattern | Corroborated | Medium | FRC-002–FRC-005 |
| `FRC-009` | The original computer version is credited to Paul Alfille on PLATO in the mid-1970s | Confirmed | Corroborated | Medium | H1, H2 |
| `FRC-010` | The six-type model represents FreeCell without a taxonomy change | Observation | Corroborated | Medium | FRC-001–FRC-008 |

## Basic data

- Release / origin: historical accounts credit Paul Alfille with creating the
  original computer FreeCell for the PLATO environment in the mid-1970s. The
  exact year is reported inconsistently, so this analysis does not narrow it
  beyond that range.
- Platform or physical form: computer solitaire derived from a physical-card
  family; the analysed state transitions are platform-independent.
- Puzzle family: fully visible ordered-card transport and reconstruction.
- Primary and rules sources:
  - **[P1] MobilityWare Help Center:**
    [“How do I play FreeCell?”](https://mobilityware.helpshift.com/hc/en/12-freecell/faq/580-how-do-i-play-freecell-1629417414/),
    documenting the eight cascades, four free cells, exposed-card moves,
    alternating descending sequences, suit foundations and simulated sequence
    transfer boundary.
  - **[P2] Freecell.net:**
    [“How to Play Freecell”](https://www.freecell.net/f/c/instructions.html),
    documenting the standard eight-by-four layout and explaining whole-column
    movement through available temporary space.
- Historical sources:
  - **[H1] Freecell.net:**
    [“History and Background”](https://www.freecell.net/f/c/about.html),
    describing Alfille's PLATO implementation and original environment.
  - **[H2] FreeCell Online:**
    [“History of FreeCell”](https://www.freecellonline.com/about-freecell),
    corroborating the PLATO origin and alternating-colour change from Baker's
    Game.
- Academic source:
  - **[A1]** Malte Helmert,
    [“New Complexity Results for Classical Planning Benchmarks”](https://cs.uky.edu/~sgware/reading/papers/helmert2006new.pdf),
    ICAPS 2006, formalising a scalable FreeCell planning domain. Its complexity
    result is not used to rate any fixed deal.
- Claim IDs: `FRC-001`–`FRC-010`.

## Mechanical decomposition

### Action Genes

- `ACT-010` — transfer accessible card between zones. The primitive move
  selects one exposed cascade card or free-cell card and places it into one
  legal cascade, free cell or foundation destination.
- A multi-card drag is not admitted as a second Action Gene. Under the scoped
  convention it is a macro accepted only if the same state can be reached by
  legal single-card transfers through currently available temporary space.
- The initial deal is setup, not a player action. Undo, hints and automatic
  finishing are excluded interface features.
- Claim IDs: `FRC-002`, `FRC-005`.

### System Behaviour Genes

- Existing gene IDs: none.
- Candidate genes: none.
- The scoped rules do not automatically reveal, move, remove or generate a
  card after a legal transfer. Foundation placement is manual.
- The deal determines the initial instance before the decision loop. Treating
  setup shuffling as in-play spawning would falsely align FreeCell with 2048.
- Interface implementations may animate a supermove or auto-send safe cards to
  foundations, but those conveniences are explicitly outside this ruleset.
- Claim IDs: `FRC-001`, `FRC-005`, `FRC-007`.

### Constraint Genes

- `CON-014` — exposed-only stack access. A deeper cascade card cannot move
  until every card below it in the displayed cascade has been displaced.
- `CON-015` — bounded single-element temporary buffer. Four free cells each
  store one card without a rank or suit build rule.
- `CON-016` — alternating-colour descending tableau build. A card placed on a
  non-empty cascade must be exactly one rank lower and of the opposite colour;
  any single card may enter an empty cascade.
- `CON-017` — same-suit ascending foundation build. Each foundation starts with
  an ace and accepts the next rank of that suit through king.
- `CON-001` is absent. Fixed counts of cascades, cells and cards are parameters,
  but cascade depth is dynamic; forcing every finite card slot into generic
  occupancy capacity would erase the access and stack distinctions above.
- Compound transfer length is derived from `CON-014`–`CON-016` and current
  empty-space state. It is not an independent constraint: removing the shortcut
  leaves the reachable state graph unchanged.
- Scarce strategic resources: unoccupied free cells, empty cascades and exposed
  low cards needed to release foundations.
- Claim IDs: `FRC-002`–`FRC-005`, `FRC-008`.

### Information Genes

- `INF-001` — fully visible current state. Every card identity, cascade order,
  occupied free cell and foundation top is inspectable before each move.
- A covered card model is absent. A blocked card is known but inaccessible,
  which is a Constraint rather than hidden Information.
- The initial deal may vary, but no future random card is introduced during the
  scoped decision loop.
- Claim IDs: `FRC-001`, `FRC-007`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. The complete existing deck
  must end in four suit-specific foundations ordered ace through king.
- Unlike Sokoban's interchangeable crates, card identity matters to both the
  destination suit and exact rank position. Unlike Rubik's Cube, the target is
  assembled across completion zones rather than by a permutation-preserving
  turn of one physical object.
- Maintaining legal moves is strategically useful but not itself the success
  condition, so `OBJ-003` is absent.
- Claim IDs: `FRC-004`, `FRC-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. Cards are transferred one at a time
  and the state does not advance while the player pauses.
- A timer or move counter may evaluate performance but is not part of the
  completion rule. Animation does not create simultaneous unresolved action.
- Claim IDs: `FRC-002`, `FRC-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Exposed red five; black six exposed elsewhere | Transfer five onto six | Five becomes the new exposed end of that cascade | Alternating descending build | `FRC-004` |
| Exposed red five; red six exposed elsewhere | Attempt the same transfer | Move is rejected | Colour alternation is active | `FRC-004` |
| One free cell is empty | Transfer any accessible card to it | Cell holds that single card | Unordered temporary storage | `FRC-003` |
| All four free cells are occupied | Attempt to store another card in them | No free-cell destination accepts it | Buffer capacity is state-dependent | `FRC-003` |
| Ace of hearts is accessible; heart foundation empty | Transfer ace to foundation | Heart foundation begins at ace | Foundation start rule | `FRC-004` |
| Three hearts is accessible; heart foundation top is ace | Attempt foundation transfer | Move is rejected until two hearts is placed | Exact same-suit rank order | `FRC-004` |
| Ordered run has a legal primitive transfer sequence through open space | Request compound transfer | Implementation may execute the equivalent sequence | Macro adds convenience, not reachability | `FRC-005` |

## Strategic and experiential structure

- Local decision: expose a needed card without consuming the destination or
  free cell required for the next transfer.
- Medium-term planning: build reversible alternating runs, open cascades and
  decide when a card can safely leave tableau circulation for its foundation.
- Long-term structure: release low ranks in suit order while preserving enough
  temporary capacity to dismantle blockers and transport longer ordered runs.
- Common heuristics: keep free cells open when possible; value an empty cascade
  more than one free cell because it can stage a stack; avoid sending a card to
  a foundation when its absence blocks a needed tableau build; inspect buried
  aces and twos before committing high cards.
- Failure attribution: every card is visible, but a locally legal transfer can
  consume the only staging space needed to reach a buried prerequisite.
- Player-trust factors: deterministic transitions and open information make
  consequences inspectable, while implementation-specific auto-moves can
  obscure which transfers were actually chosen; those are excluded here.
- Claim IDs: `FRC-005`, `FRC-008`.

## Replay and variation

- What changes between sessions: the initial permutation of the 52 cards.
- Randomness or procedural generation: the deal may be selected or shuffled at
  setup; there is no random in-play successor event.
- Multiple viable strategies: many deals allow different exposure orders,
  foundation timings and temporary-storage sequences that converge on the same
  target foundations.
- Typical replay motive: solve a failed deal, reduce moves or test another deal.
- Claim IDs: `FRC-001`, `FRC-007`, `FRC-008`.

## Adjacent systems and history

- Historical accounts link Alfille's PLATO FreeCell to Baker's Game and
  identify alternating-colour tableau building as the decisive rule change.
- Related solitaire variants change buffer count, empty-cascade acceptance,
  build suit or concealed-card access. Those differences can change multiple
  genes and require their own decompositions.
- Klondike should not inherit this genome from theme alone: stock draws,
  concealed cards and automatic reveal introduce different action,
  information and system structures.
- Complexity caveat: Helmert analyses a scalable formal planning family. The
  result does not prove that every fixed 52-card deal is difficult or solvable.
- Claim IDs: `FRC-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-010` | source and destination zone |
| System Behaviour | none | setup deal and excluded auto-moves |
| Constraint | `CON-014`, `CON-015`, `CON-016`, `CON-017` | four cells, eight cascades, empty-cascade rule |
| Information | `INF-001` | complete deal visible |
| Objective | `OBJ-004` | four ace-to-king suit foundations |
| Time | `TIM-002` | optional move/time evaluation |

Canonical signature:

`ACT-010; ; CON-014,CON-015,CON-016,CON-017; INF-001; OBJ-004; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `6` (`GAME-0001`–`GAME-0006`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`3 / 12 = 0.250000`).
- Supported combination subsets: `COMB-0007`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `INF-001`, `OBJ-004`, `TIM-002` | Both self-pacedly reconstruct visible components; Cube turns are primitive reversible permutations, while FreeCell access depends on ordered stacks and temporary storage | Near, `0.250000` |

### Preserved research notes

- New combination: `COMB-0007`, whose seven genes are a proper subset of this
  eight-gene genome.
- New genes: `ACT-010`, `CON-014`, `CON-015`, `CON-016`, `CON-017`.
- Classification result: `New gene`.
- Evidence and reasoning: direct card transfer, stack-end access, single-card
  buffers and the two incompatible build orders have distinct operational
  boundaries. Deal number, zone counts and empty-cascade convention remain
  parameters. Supermove length is derived rather than admitted separately.

## Taxonomy impact

- Registry changes: five bounded genes added; `INF-001`, `OBJ-004` and
  `TIM-002` reused.
- Taxonomy-change record: none. Ordered access and resource limits fit the
  Constraint type, while direct zone transfer fits Action.
- Candidate terms affected: move / stack, empty buffers, access order and
  sequence now have bounded FreeCell mappings.
- `INF-003` remains absent because buried cards are visible and fixed; their
  issue is accessibility, not concealment.
- No System Behaviour is inferred from the setup deal or optional interface
  automation.
- Claim IDs: `FRC-010`.

## Negative results

The multi-card supermove candidate was rejected as an independent gene. Under
the scoped rule it is exactly a macro over legal primitive transfers, so it
changes input efficiency but neither reachability nor the underlying decision
constraints. Automatic foundation movement was also rejected from the genome
because it is implementation-specific and excluded by scope.
