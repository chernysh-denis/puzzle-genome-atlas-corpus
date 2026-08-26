---
game_id: GAME-0109
slug: candy-crush-saga
game_title: Candy Crush Saga
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0009
gene_ids:
  action:
    - ACT-011
    - ACT-012
  system:
    - SYS-003
    - SYS-004
    - SYS-010
    - SYS-011
    - SYS-012
    - SYS-013
    - SYS-014
  constraint:
    - CON-001
    - CON-019
    - CON-020
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-007
  time:
    - TIM-001
---

# Game: Candy Crush Saga

## Analysis scope

- Version / ruleset: current ordinary move-limited order level, restricted to
  adjacent swapping, colour matches, striped / wrapped / colour-bomb creation,
  clearing, collapse, refill and cascades.
- Included: visible rectangular board, legal match-producing swaps, direct
  special activation, finite moves and a declared colour-order target.
- Excluded: blockers, timed levels, boosters, lives, purchases, events, map
  progression and obstacle-specific exceptions.
- Direct-play status: not conducted. King's current help centre defines swapping,
  matching and move efficiency; the order guide establishes target completion.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CCS-001` | Swapping adjacent candies to form rows or columns of at least three is the core input | Confirmed | Direct | High | P1 |
| `CCS-002` | A bounded order level combines automatic clearing and refill with a finite move budget | Confirmed | Corroborated | High | P1, P2 |
| `CCS-003` | Under the scoped resolution, Candy Crush and Royal Match have the same complete current genome signature | Observation | Corroborated | High | P1, P2, corpus scan |

## Basic data

- Release / origin: King released Candy Crush Saga in 2012.
- Platform or physical form: touch / pointer match-three puzzle.
- Puzzle family: move-limited matching and combination.
- Primary sources: **[P1]** [King controls guide](https://candycrush.zendesk.com/hc/en-us/articles/360000750278-Controls-how-to-switch-and-match-candies);
  **[P2]** [King order guide](https://community.king.com/en/candy-crush-saga/discussion/246651/collecting-orders-in-candy-crush-saga).
- Claim IDs: `CCS-001`–`CCS-003`.

## Mechanical decomposition

### Action Genes

- `ACT-011` swaps one orthogonally adjacent pair; `ACT-012` activates or
  combines available special candies.
- Candidate genes: none. Parameters are candy palette and special shapes.
- Claim IDs: `CCS-001`.

### System Behaviour Genes

- `SYS-003`, `SYS-004`, `SYS-010`–`SYS-014` resolve matching, special creation,
  clearing, collapse, refill and repeated cascades.
- Resolution order: commit swap; clear; create / trigger specials; collapse;
  refill; repeat until stable.
- Claim IDs: `CCS-002`.

### Constraint Genes

- `CON-001` fixes the board, `CON-019` restricts swaps to match-producing
  neighbours and `CON-020` supplies the finite move budget.
- Scarce strategic resources: remaining moves and board-local specials.
- Claim IDs: `CCS-002`.

### Information Genes

- `INF-001` exposes current board state; `INF-002` withholds refill identities.
- Candidate genes: none.
- Claim IDs: `CCS-002`.

### Objective Genes

- `OBJ-007` requires clearing the displayed target quantities.
- Success, evaluation and failure: all targets before moves reach zero.
- Claim IDs: `CCS-002`.

### Time Genes

- `TIM-001` completes every cascade before the next decision.
- Candidate genes: none.
- Claim IDs: `CCS-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two adjacent candies would not create a match | Swap them | Swap is rejected or restored | match-producing legality | `CCS-001` |
| Three equal candies align | Commit the swap | Match clears, columns fall and new candies refill | staged resolution | `CCS-002` |
| One move remains and target is incomplete | Make a non-finishing move | Cascades finish, moves reach zero and attempt fails | finite horizon | `CCS-002` |

## Strategic and experiential structure

- Local decision: choose a legal swap and predict its first clear.
- Medium-term planning: preserve moves and construct useful specials.
- Long-term structure: complete the order before exhaustion.
- Common heuristics: prefer moves that advance targets or create combinations.
- Failure attribution: visible moves are attributable; refill remains uncertain.
- Player-trust factors: the record makes no claim about generation fairness.
- Claim IDs: `CCS-002`, `CCS-003`.

## Replay and variation

- What changes between sessions: refill sequence and level layout.
- Randomness or procedural generation: refill is not previewed.
- Multiple viable strategies: usually yes.
- Typical replay motive: solve after move exhaustion or improve efficiency.
- Claim IDs: `CCS-002`.

## Adjacent systems and history

- Direct predecessors: Bejeweled-style match-three systems.
- Variants: blockers, ingredients and timed levels are outside scope.
- Similar games: Royal Match.
- Important differences: theme and content parameters do not split the current
  gene boundaries.
- Claim IDs: `CCS-003`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-011`, `ACT-012` | palette; special set |
| System Behaviour | `SYS-003`, `SYS-004`, `SYS-010`–`SYS-014` | refill distribution |
| Constraint | `CON-001`, `CON-019`, `CON-020` | board and move count |
| Information | `INF-001`, `INF-002` | preview policy |
| Objective | `OBJ-007` | order quantities |
| Time | `TIM-001` | cascade duration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `108` (`GAME-0001`–`GAME-0108`).
- Exact genome matches: `GAME-0009` — Royal Match.
- Tied near matches: `GAME-0001` — 2048 (`6 / 24 = 0.250000`).
- Supported combination subsets: `COMB-0009`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0009`, `GAME-0001`.

## Taxonomy impact

- Registry changes: none.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Observation | Corroborated | High] Candy Crush provides a mass-market exact
  match for the existing move-limited match-three genome (`CCS-003`).

## Нові гени

- [Observation | Corroborated | High] Нових генів немає.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0009` gains an independent carrier.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Do blocker-heavy Candy Crush levels require a later bounded scope split?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Angry Birds Classic.
- Optimisation criterion: move from discrete match resolution to live ballistics.
- Expected information gain: launcher, damage and support-collapse boundaries.
- Backlog impact: preserve the remaining popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It maximises mechanical distance from this exact match.
