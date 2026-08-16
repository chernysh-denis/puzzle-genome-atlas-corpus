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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-011,ACT-012; SYS-003,SYS-004,SYS-010,SYS-011,SYS-012,SYS-013,SYS-014; CON-001,CON-019,CON-020; INF-001,INF-002; OBJ-007; TIM-001`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: `GAME-0009`.
- Near matches and similarity scores: `GAME-0009` — Royal Match at `16 / 16 = 1.000000`.
- Supported combination subsets: `COMB-0009`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `6 / 24 = 0.250000`; `GAME-0002`: `2 / 21 = 0.095238`; `GAME-0003`: `2 / 23 = 0.086957`; `GAME-0004`: `3 / 28 = 0.107143`.
- `GAME-0005`: `2 / 21 = 0.095238`; `GAME-0006`: `2 / 23 = 0.086957`; `GAME-0007`: `1 / 23 = 0.043478`; `GAME-0008`: `2 / 21 = 0.095238`.
- `GAME-0009`: `16 / 16 = 1.000000`; `GAME-0010`: `3 / 22 = 0.136364`; `GAME-0011`: `2 / 27 = 0.074074`; `GAME-0012`: `2 / 23 = 0.086957`.
- `GAME-0013`: `3 / 26 = 0.115385`; `GAME-0014`: `2 / 29 = 0.068966`; `GAME-0015`: `5 / 25 = 0.200000`; `GAME-0016`: `3 / 28 = 0.107143`.
- `GAME-0017`: `2 / 27 = 0.074074`; `GAME-0018`: `3 / 32 = 0.093750`; `GAME-0019`: `3 / 23 = 0.130435`; `GAME-0020`: `3 / 27 = 0.111111`.
- `GAME-0021`: `1 / 24 = 0.041667`; `GAME-0022`: `1 / 27 = 0.037037`; `GAME-0023`: `0 / 26 = 0.000000`; `GAME-0024`: `1 / 27 = 0.037037`.
- `GAME-0025`: `1 / 26 = 0.038462`; `GAME-0026`: `1 / 27 = 0.037037`; `GAME-0027`: `2 / 26 = 0.076923`; `GAME-0028`: `4 / 29 = 0.137931`.
- `GAME-0029`: `2 / 26 = 0.076923`; `GAME-0030`: `1 / 29 = 0.034483`; `GAME-0031`: `1 / 26 = 0.038462`; `GAME-0032`: `2 / 25 = 0.080000`.
- `GAME-0033`: `1 / 28 = 0.035714`; `GAME-0034`: `1 / 29 = 0.034483`; `GAME-0035`: `1 / 33 = 0.030303`; `GAME-0036`: `1 / 27 = 0.037037`.
- `GAME-0037`: `2 / 23 = 0.086957`; `GAME-0038`: `1 / 31 = 0.032258`; `GAME-0039`: `2 / 23 = 0.086957`; `GAME-0040`: `1 / 23 = 0.043478`.
- `GAME-0041`: `1 / 26 = 0.038462`; `GAME-0042`: `1 / 24 = 0.041667`; `GAME-0043`: `3 / 27 = 0.111111`; `GAME-0044`: `3 / 23 = 0.130435`.
- `GAME-0045`: `4 / 26 = 0.153846`; `GAME-0046`: `1 / 25 = 0.040000`; `GAME-0047`: `2 / 28 = 0.071429`; `GAME-0048`: `2 / 28 = 0.071429`.
- `GAME-0049`: `2 / 23 = 0.086957`; `GAME-0050`: `3 / 28 = 0.107143`; `GAME-0051`: `3 / 29 = 0.103448`; `GAME-0052`: `1 / 25 = 0.040000`.
- `GAME-0053`: `3 / 22 = 0.136364`; `GAME-0054`: `3 / 24 = 0.125000`; `GAME-0055`: `3 / 23 = 0.130435`; `GAME-0056`: `2 / 22 = 0.090909`.
- `GAME-0057`: `3 / 21 = 0.142857`; `GAME-0058`: `3 / 22 = 0.136364`; `GAME-0059`: `3 / 20 = 0.150000`; `GAME-0060`: `3 / 20 = 0.150000`.
- `GAME-0061`: `2 / 24 = 0.083333`; `GAME-0062`: `2 / 22 = 0.090909`; `GAME-0063`: `2 / 21 = 0.095238`; `GAME-0064`: `1 / 20 = 0.050000`.
- `GAME-0065`: `1 / 22 = 0.045455`; `GAME-0066`: `0 / 26 = 0.000000`; `GAME-0067`: `2 / 22 = 0.090909`; `GAME-0068`: `1 / 23 = 0.043478`.
- `GAME-0069`: `2 / 22 = 0.090909`; `GAME-0070`: `4 / 20 = 0.200000`; `GAME-0071`: `2 / 21 = 0.095238`; `GAME-0072`: `2 / 22 = 0.090909`.
- `GAME-0073`: `2 / 21 = 0.095238`; `GAME-0074`: `2 / 23 = 0.086957`; `GAME-0075`: `2 / 23 = 0.086957`; `GAME-0076`: `2 / 21 = 0.095238`.
- `GAME-0077`: `2 / 21 = 0.095238`; `GAME-0078`: `2 / 21 = 0.095238`; `GAME-0079`: `2 / 21 = 0.095238`; `GAME-0080`: `2 / 21 = 0.095238`.
- `GAME-0081`: `2 / 22 = 0.090909`; `GAME-0082`: `2 / 22 = 0.090909`; `GAME-0083`: `2 / 22 = 0.090909`; `GAME-0084`: `2 / 24 = 0.083333`.
- `GAME-0085`: `0 / 27 = 0.000000`; `GAME-0086`: `1 / 28 = 0.035714`; `GAME-0087`: `1 / 25 = 0.040000`; `GAME-0088`: `1 / 24 = 0.041667`.
- `GAME-0089`: `1 / 24 = 0.041667`; `GAME-0090`: `2 / 29 = 0.068966`; `GAME-0091`: `1 / 24 = 0.041667`; `GAME-0092`: `1 / 25 = 0.040000`.
- `GAME-0093`: `1 / 24 = 0.041667`; `GAME-0094`: `1 / 25 = 0.040000`; `GAME-0095`: `1 / 27 = 0.037037`; `GAME-0096`: `1 / 25 = 0.040000`.
- `GAME-0097`: `1 / 23 = 0.043478`; `GAME-0098`: `1 / 22 = 0.045455`; `GAME-0099`: `2 / 22 = 0.090909`; `GAME-0100`: `0 / 27 = 0.000000`.
- `GAME-0101`: `0 / 26 = 0.000000`; `GAME-0102`: `0 / 23 = 0.000000`; `GAME-0103`: `1 / 24 = 0.041667`; `GAME-0104`: `1 / 24 = 0.041667`.
- `GAME-0105`: `0 / 26 = 0.000000`; `GAME-0106`: `0 / 23 = 0.000000`; `GAME-0107`: `1 / 23 = 0.043478`; `GAME-0108`: `1 / 25 = 0.040000`.

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
