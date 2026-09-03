---
game_id: GAME-0017
slug: balatro
game_title: Balatro
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0017
gene_ids:
  action:
    - ACT-021
    - ACT-022
  system:
    - SYS-026
    - SYS-027
    - SYS-028
  constraint:
    - CON-020
    - CON-043
    - CON-044
    - CON-045
    - CON-046
  information:
    - INF-003
  objective:
    - OBJ-013
  time:
    - TIM-001
---

# Game: Balatro

## Analysis scope

- Version / ruleset: one ordinary Small Blind in the standard Balatro rules
  current at the review date, entered with the draw deck and owned Joker row
  already fixed.
- Included: visible held cards; concealed draw-pile order; selecting one to
  five cards to Play or Discard; automatic refill; finite Hands and Discards;
  standard poker-hand predicates and precedence; a fixed exemplar Joker row
  limited to passive `+Chips`, `+Mult` and `XMult` scoring modifiers; player
  reordering of those Jokers; target score, success and failure.
- Excluded: blind skipping, Big and Boss Blind modifiers, shop purchases,
  money, interest, Ante traversal, Tarot / Planet / Spectral consumables,
  Vouchers, deck editing during the Blind, Joker acquisition or sale, Jokers
  that change draw, hand definitions, action allowances or economy, challenge
  and seeded runs, unlocks and profile metaprogression.
- Direct-play status: not conducted for this record. Official product sources
  establish the Blind / Joker structure; detailed action, hand and scoring
  rules are corroborated by specialist reference records.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BAL-001` | A Blind requires the player to earn at least a displayed Chips target by playing poker hands | Confirmed | Direct | High | F1, F2 |
| `BAL-002` | The player selects a non-empty subset of up to five visible held cards and commits it either to Play or Discard | Confirmed | Corroborated | High | F3, F4 |
| `BAL-003` | Played or discarded cards leave the hand and the system draws replacements from the current deck | Confirmed | Corroborated | High | F3, F4 |
| `BAL-004` | The remaining deck's card multiset can be inspected, while its current draw order remains concealed until cards are dealt | Confirmed | Corroborated | Medium | F3, F4 |
| `BAL-005` | A committed Play is classified by the highest-precedence satisfied poker-hand predicate | Confirmed | Corroborated | High | F3 |
| `BAL-006` | Only cards belonging to the classified hand ordinarily score, although additional played cards are still consumed | Confirmed | Corroborated | High | F3 |
| `BAL-007` | Scoring starts from the hand's Chips and Mult and applies eligible played-card, held-card and Joker effects in a defined sequence | Confirmed | Corroborated | High | F3, F5, F6 |
| `BAL-008` | Additive and multiplicative modifier order can change the final score, so the player may strategically reorder Jokers | Confirmed | Corroborated | High | F5, F6 |
| `BAL-009` | Playing consumes one finite Hand; reaching the target succeeds, while exhausting Hands below target fails | Confirmed | Corroborated | High | F1, F4 |
| `BAL-010` | Discarding consumes a separate finite Discard allowance whose exhaustion removes redraw but does not itself end the Blind | Confirmed | Corroborated | High | F4 |
| `BAL-011` | Joker text supplies fixed passive effects in this scope rather than player-manipulated executable syntax | Observation | Corroborated | High | F1, F2, F5 |
| `BAL-012` | Pre-shuffled concealed deck order is Information state, not an in-play random selection after every command | Observation | Corroborated | Medium | BAL-003, BAL-004 |

## Basic data

- Release: 20 February 2024.
- Developer: LocalThunk. Publisher: Playstack.
- Puzzle family: stochastic hand-management and ordered score-combination
  puzzle within a roguelike deckbuilder.
- Sources:
  - **[F1]** [Official Balatro FAQ](https://www.playbalatro.com/faq), defining
    poker-hand scoring, Blind progression and unique Joker mechanisms.
  - **[F2]** [Official Steam page](https://store.steampowered.com/app/2379780/Balatro/),
    release metadata and the official poker-hand / Joker / Blind description.
  - **[F3]** [Balatro Wiki — Poker Hands](https://balatrogame.fandom.com/wiki/Poker_Hands),
    hand sizes, predicate precedence, base Chips / Mult and scoring-card
    boundaries.
  - **[F4]** [HandWiki — Balatro](https://handwiki.org/wiki/Software%3ABalatro),
    held-card selection, finite Hands and Discards, replacement draws and Blind
    failure.
  - **[F5]** [Balatro Wiki — Activation Type](https://balatrogame.fandom.com/wiki/Activation_Type),
    effect categories and activation-sequence reference.
  - **[F6]** [Balatro score reference implementation](https://mathiaslj.github.io/balatro/reference/balatro.html),
    independent executable documentation of base, played-card, held-card and
    Joker ordering. It is corroboration, not an official implementation.
- Claim IDs: `BAL-001`–`BAL-012`.

## Mechanical decomposition

### Action Genes

- `ACT-021` — commit selected visible-card subset. The relevant zone is
  Balatro's hand: the player selects one to five visible held cards and chooses
  either Play for scoring or Discard for replacement without score.
- `ACT-022` — reorder persistent effect sequence. The player may rearrange the
  fixed Joker row before committing a Play so order-sensitive additive and
  multiplicative effects resolve in the intended sequence.
- Draw identities, poker-hand classification and score calculation are system
  outcomes rather than additional commands.
- Claim IDs: `BAL-002`, `BAL-008`.

### System Behaviour Genes

- `SYS-026` — draw-to-hand replacement. Committed cards leave the hand and the
  system reveals the current top cards until the allowed hand size is restored
  or the deck is exhausted.
- `SYS-027` — highest-precedence pattern classification. A Play is assigned the
  most specific satisfied poker hand under the fixed hierarchy.
- `SYS-028` — ordered additive-and-multiplicative score resolution. The system
  begins from the classified hand's Chips and Mult, resolves scoped eligible
  card effects and then the fixed Joker modifiers in their active order before
  adding the product to the Blind total.
- `SYS-004` is absent. The scoped draw order is selected before player
  decisions begin and then persists as concealed current state; drawing reveals
  that order rather than sampling a fresh outcome after each command.
- Claim IDs: `BAL-003`–`BAL-008`, `BAL-012`.

### Constraint Genes

- `CON-020` — finite action budget with terminal exhaustion. Each Play spends
  one Hand, and exhausting the last Hand below the target ends the Blind.
- `CON-043` — bounded visible hand and commit size. The hand has a fixed current
  capacity and no Play or Discard may contain more than five held cards.
- `CON-044` — finite non-terminal redraw allowance. Each Discard spends one
  separate allowance; zero Discards disables that mode but leaves Plays legal.
- `CON-045` — ranked card-pattern predicates. Rank and suit relations define
  High Card through Straight Flush and determine which cards ordinarily score.
- `CON-046` — fixed-capacity ordered modifier tableau. The scoped passive
  Jokers occupy bounded ordered slots, and changing their order may change
  arithmetic resolution.
- Joker identities and numerical modifiers are parameters in this bounded
  scope; rule-changing Joker families require later decomposition.
- Claim IDs: `BAL-002`, `BAL-005`–`BAL-010`.

### Information Genes

- `INF-003` — fixed concealed current state. Held cards and remaining deck
  composition are visible, but the persistent order of the draw pile is not
  disclosed until `SYS-026` reveals its top cards.
- `INF-001` is absent because exact future draw order is decision-relevant
  current state and is concealed. This is not a wholly visible game merely
  because the hand and Joker text are public.
- `INF-002` is absent under the scoped interpretation: the next cards are not
  newly sampled after Play or Discard; they are concealed entries of the
  already ordered deck.
- Claim IDs: `BAL-004`, `BAL-012`.

### Objective Genes

- `OBJ-013` — reach target score within action budget. Accumulated hand scores
  must meet or exceed the Blind requirement before Hands reach zero.
- `OBJ-002` is absent. Excess score beyond the threshold is not a separately
  maximised formal objective within one scoped Blind; the broader run rewards
  efficiency through economy, which is excluded here.
- Claim IDs: `BAL-001`, `BAL-009`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. A Play triggers complete
  classification, ordered scoring and refill; a Discard triggers removal and
  refill. The next command waits until that resolution finishes.
- There is no real-time deadline or independent opponent in the scoped Blind.
- Claim IDs: `BAL-002`, `BAL-003`, `BAL-007`.

## Reproducible transitions

| Before | Player command | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Visible hand contains a pair plus unrelated cards | Select the pair and Play | System classifies Pair, calculates score, spends one Hand and draws replacements | Selection, classification and resolution are separate | `BAL-002`, `BAL-003`, `BAL-005` |
| Five selected cards satisfy both Flush and Straight Flush | Play them | Higher-precedence Straight Flush is assigned | Overlapping predicates resolve by hierarchy | `BAL-005` |
| Five cards are played but only two make the classified Pair | Play all five | Pair cards ordinarily score; every played card leaves the hand | Committed subset and scoring subset differ | `BAL-006` |
| Visible hand lacks the desired rank | Select up to five cards and Discard | Discard allowance decreases; replacements are revealed; no score is added | Redraw budget differs from scoring Hands | `BAL-003`, `BAL-010` |
| `+Mult` Joker is left of `XMult` Joker | Play a triggering hand | Additive Mult is applied before later multiplication | Modifier order changes result | `BAL-007`, `BAL-008` |
| Same two Jokers are reversed | Play an otherwise identical triggering hand | Multiplication precedes later addition and produces a different total | Reordering is decision-relevant Action | `BAL-008` |
| Final Hand resolves below target | Complete scoring | Blind fails after budget reaches zero | Hand allowance is terminal | `BAL-009` |
| A hand raises cumulative Chips to the target | Complete scoring | Blind succeeds immediately with unused Hands remaining | Threshold objective | `BAL-001`, `BAL-009` |

## Strategic and experiential structure

- Local decision: compare the expected score of a visible playable subset with
  the expected value of spending one Discard to improve the hand.
- Medium-term planning: preserve complementary ranks or suits across draws,
  track the remaining deck composition and allocate finite Hands between safe
  points and higher-variance combinations.
- Modifier planning: arrange additive effects before multiplicative effects
  when their predicates and activation phases allow it.
- Long-term within the Blind: reach the target with enough allowance margin to
  absorb an unhelpful concealed draw sequence.
- Failure attribution: exact current hand, remaining counts, target and effect
  text are visible, but hidden deck order makes future draws uncertain without
  introducing an adversarial decision-maker.
- Claim IDs: `BAL-001`–`BAL-012`.

## Replay and variation

- What changes: the pre-shuffled deck order, held-card sequence, fixed Joker
  tableau entering the Blind and resulting pattern opportunities.
- What remains stable in scope: play/discard commands, poker-hand hierarchy,
  draw refill, score phases and target / budget relation.
- Randomness: Blind entry establishes a concealed deck order. In-play commands
  reveal and consume that state rather than rerolling each draw independently.
- Typical replay motive: adapt to different deck and Joker builds in the full
  run. Shop-driven build evolution is acknowledged but excluded here.
- Claim IDs: `BAL-003`, `BAL-004`, `BAL-011`, `BAL-012`.

## Adjacent systems and history

- FreeCell also uses a known deck but exposes every card and moves individual
  accessible cards among zones. Balatro exposes a bounded hand while retaining
  concealed draw order and commits subsets for automatic evaluation.
- Minesweeper shares fixed concealed current state: uncertainty is resolved by
  revealing pre-existing content rather than generating a new result at each
  action. Its information is spatial clues, not a known multiset draw pile.
- Royal Match shares a terminal action budget but spends every accepted move on
  board transformation. Balatro separates terminal Hands from non-terminal
  Discards.
- Baba Is You lets the player spatially rewrite executable rule syntax. Scoped
  Balatro Jokers are fixed persistent modifiers whose order is controllable,
  not text rules the player composes or activates through grammar.
- Claim IDs: `BAL-004`, `BAL-008`–`BAL-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-021`, `ACT-022` | card count, Play / Discard mode and reorder timing |
| System Behaviour | `SYS-026`, `SYS-027`, `SYS-028` | draw count, scoring phases and retriggers |
| Constraint | `CON-020`, `CON-043`, `CON-044`, `CON-045`, `CON-046` | hand size, allowances, hand list and Joker slots |
| Information | `INF-003` | visible remaining multiset versus hidden order |
| Objective | `OBJ-013` | Blind target and early-success rule |
| Time | `TIM-001` | animation does not accept unresolved commands |

Canonical signature:

`ACT-021,ACT-022; SYS-026,SYS-027,SYS-028; CON-020,CON-043,CON-044,CON-045,CON-046; INF-003; OBJ-013; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `16` (`GAME-0001`–`GAME-0016`).
- Exact genome matches: none.
- Tied near matches: `GAME-0003` — Minesweeper (`2 / 20 = 0.100000`).
- Supported combination subsets: `COMB-0017`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0003`.

### Preserved research notes

- Result: no exact signature or existing combination match. The low near score
  confirms mechanical distance and is not a novelty claim.

## Combination record

- Registered [`COMB-0017`](../../combinations/COMB-0017.md), a proper
  twelve-gene subset centred on hidden-order hand management and ordered
  modifier scoring under a terminal action budget.
- Bounded hand capacity remains in the full genome but is omitted from the
  combination because the core interaction is already bounded by subset,
  redraw and scoring-action rules.

## Taxonomy impact

- Three existing genes are reused and ten bounded genes are added; the
  six-type taxonomy remains sufficient for the scoped Blind loop.
- Rule-changing Jokers, Boss Blinds and shop construction remain explicitly
  outside this record rather than being collapsed into broad genes.

## Negative results

- `SYS-004` and `INF-002` are rejected for the in-Blind loop: shuffled order is
  fixed at entry and later revealed, so `INF-003` is the relevant boundary.
- `INF-001` is rejected despite a visible hand because exact deck order is
  concealed decision-relevant current state.
- `ACT-010` and `CON-014` are rejected: Balatro commits a held subset and the
  system draws, rather than the player transferring one exposed stack card.
- `SYS-017`, `SYS-018` and `INF-008` are rejected. Fixed Joker effect text does
  not become executable through player-arranged grammar; only effect order is
  changed in scope.
- Rule-changing Jokers, Boss Blinds and shop build construction remain a
  deliberate future scope. Treating all 150 Joker mechanisms as parameters of
  `SYS-028` would overgeneralise this bounded record.
- No taxonomy change is required.

## Research notes

- Strongest finding: Balatro separates two finite resources with different
  terminal semantics—Hands produce score and can end the Blind, while Discards
  alter information access without directly scoring or terminating at zero.
- Registry consequence: `CON-020`, `INF-003` and `TIM-001` are reused; ten
  bounded genes are admitted for hand commitment, draw, pattern evaluation,
  ordered scoring and modifier structure.
- Next selection should test spatial placement or real-time network demand,
  avoiding a second consecutive deck / hand system.
