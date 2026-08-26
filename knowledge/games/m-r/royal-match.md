---
game_id: GAME-0009
slug: royal-match
game_title: Royal Match
analysis_status: reviewed
reviewed: 2026-08-11
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

# Game: Royal Match

## Analysis scope

- Version / ruleset: the current Royal Match core board loop, narrowed to a
  standard rectangular level whose targets are quantities of ordinary coloured
  items.
- Included: orthogonally adjacent swaps that form a match; automatic clearing
  of three or more same-coloured items; vertical collapse; unpreviewed refill;
  repeated cascades; finite moves; match-created Rocket, Propeller, TNT and
  Light Ball power-ups; direct activation and power-up combinations.
- Excluded: pre-level and in-level purchased Boosters, obstacle-specific rules,
  non-rectangular flow paths, coins, extra-move purchases, lives, stars,
  renovation, teams, collections, events, tournaments, difficulty labels and
  all other meta-progression.
- Direct-play status: not conducted. Royal-specific targets, move limits and
  power-ups were taken from the current official help centre. The ordinary
  clear-collapse-refill loop was corroborated by match-3 research and gameplay
  documentation. The exact refill distribution is unpublished and no fairness
  or solvability claim is made.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RYL-001` | A level is won by completing every displayed target | Confirmed | Direct | High | P1, P2 |
| `RYL-002` | Ordinary targets can be advanced by matching three or more same-coloured items | Confirmed | Direct | High | P1, P2 |
| `RYL-003` | Each level supplies a finite move allowance and fails if it is exhausted before the targets are complete | Confirmed | Direct | High | P1, P2 |
| `RYL-004` | The core swap-match loop exchanges adjacent items, clears qualifying matches, drops retained items, refills vacancies and repeats newly formed matches before the next move | Pattern | Corroborated | Medium | S1, A1, A2 |
| `RYL-005` | Matches of four or more in declared geometries create Rocket, Propeller, TNT or Light Ball power-ups | Confirmed | Direct | High | P3 |
| `RYL-006` | A power-up can be tapped or swapped to activate a rule-defined multi-item effect | Confirmed | Direct | High | P3 |
| `RYL-007` | Swapping two power-ups produces a larger combined clearing effect | Confirmed | Direct | High | P2, P4 |
| `RYL-008` | Current board, targets and remaining moves are visible, while future refill item identities are not previewed | Observation | Corroborated | Medium | P1, S1, A1 |
| `RYL-009` | Refill and Propeller targeting introduce random outcomes during the decision loop | Pattern | Corroborated | Medium | P3, P4, A1 |
| `RYL-010` | The six-type model separates commanded swaps from automatic cascade resolution without a taxonomy change | Observation | Corroborated | Medium | RYL-001–RYL-009 |

## Basic data

- Release / origin: Dream Games identifies Royal Match as one of its titles;
  release catalogues place its iOS launch in 2020 and wider 2021 release. The
  analysed rules are the current service rules, not one historical build.
- Platform: mobile digital puzzle game.
- Puzzle family: move-limited swap-match with automatic cascades.
- Official sources:
  - **[P1] Dream Games Help Center:**
    [“How do I play Royal Match?”](https://dreamgames.helpshift.com/hc/en/3-royal-match/faq/3-how-do-i-play-royal-match/),
    documenting targets, matches of three or more, move allowance and failure.
  - **[P2] Dream Games Help Center:**
    [“How can I play the levels?”](https://dreamgames.helpshift.com/hc/en/3-royal-match/faq/4-how-can-i-play-the-levels/),
    corroborating target clearing, move limits and power-up combinations.
  - **[P3] Dream Games Help Center:**
    [“Creating and Using the Power-Ups”](https://dreamgames.helpshift.com/hc/en/3-royal-match/faq/6-creating-and-using-the-power-ups/),
    defining creation patterns, activation and the four power-up classes.
  - **[P4] Dream Games Help Center:**
    [“Power-up Combinations”](https://dreamgames.helpshift.com/hc/en/3-royal-match/faq/7-power-up-combinations/),
    documenting combined footprints and random Propeller targets.
- Corroborating and academic sources:
  - **[S1]** [Royal Match gameplay guide](https://playroyalmatch.com/how-to-play),
    describing adjacent swaps, removal and incoming pieces. It is secondary and
    is not used for monetisation or fairness claims.
  - **[A1]** Daniel Eckmann, Kai Schiesser and Sebastian von Mammen,
    [“The Royal Crush: Analysis of Match-3 Mechanics”](https://downloads.hci.informatik.uni-wuerzburg.de/2024-CoG-RoyalCrush.pdf),
    IEEE CoG 2024, describing move, detection, removal, random refill and
    pattern-conditioned special-item creation in modern match-3 systems.
  - **[A2]** Luciano Gualà, Stefano Leucci and Emanuele Natale,
    [“Bejeweled, Candy Crush and other Match-Three Games are (NP-)Hard”](https://arxiv.org/abs/1403.5830),
    formalising adjacent swap, simultaneous pop, fall, refill and repeated
    cascades for the canonical swap-match family.
- Claim IDs: `RYL-001`–`RYL-010`.

## Mechanical decomposition

### Action Genes

- `ACT-011` — swap orthogonally adjacent board elements. The player selects two
  neighbouring ordinary items whose exchange is intended to form a match.
- `ACT-012` — activate or combine board power-up. A persistent Rocket, TNT,
  Propeller or Light Ball can be tapped or swapped; two power-ups can be swapped
  together for a combined effect.
- These actions differ because an ordinary swap must satisfy a match-validity
  condition, while power-up activation directly commands a stored effect.
- Pre-level Booster selection and purchases are outside the level genome.
- Claim IDs: `RYL-002`, `RYL-005`–`RYL-007`.

### System Behaviour Genes

- `SYS-003` — element spawn after valid action. After collapse, new ordinary
  items enter from above to restore playable board occupancy.
- `SYS-004` — random outcome selection. Incoming item types and Propeller
  targets are system-selected; the exact probability policy is not published.
- `SYS-010` — automatic qualifying-match removal. The system detects and clears
  horizontal or vertical groups of at least three same-coloured ordinary items.
- `SYS-011` — vacancy-driven vertical board collapse. Retained items above
  cleared cells fall into reachable vacancies.
- `SYS-012` — repeat automatic resolution until stable. Matches created by
  falling or refill resolve as cascades without spending another move.
- `SYS-013` — pattern-conditioned special-element creation. Four-item line or
  square and five-item line, L or T patterns create the documented power-up
  class instead of only disappearing.
- `SYS-014` — activated multi-target clearing effect. The system computes and
  applies the row, column, radius, random-target, colour-wide or combined
  footprint after the player activates a power-up.
- `SYS-001` is absent: gravity direction is not selected by the player and the
  post-clear movement is vacancy-driven rather than maximal board compression
  following a global direction command.
- `SYS-006` is absent: items do not descend on a real-time schedule while the
  player is deciding; collapse belongs to discrete post-action resolution.
- Claim IDs: `RYL-004`–`RYL-009`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The scoped level uses a fixed set of
  addressed rectangular board cells even though their occupants change.
- `CON-019` — match-valid adjacent swap. An ordinary orthogonal exchange is a
  useful state-changing move only when it creates a qualifying same-colour
  line; power-up activation is the explicit exception.
- `CON-020` — finite action budget with terminal exhaustion. Chargeable moves
  reduce the displayed allowance; zero remaining before target completion ends
  the attempt.
- Board dimensions, colour count, target quantities and initial move allowance
  are parameters. Obstacles and irregular paths are excluded because their
  distinct access and damage rules require separate evidence.
- Claim IDs: `RYL-002`–`RYL-004`.

### Information Genes

- `INF-001` — fully visible current state. Current ordinary items, power-ups,
  targets and remaining moves are displayed before a decision.
- `INF-002` — unpreviewed random future event. The identities of ordinary items
  that will enter after future clears are not exposed in a preview queue.
- The future refill distribution is not inferred from visible current state.
  Randomness claims are limited to varying unpreviewed outcomes and the
  explicitly random Propeller target; no weighting policy is claimed.
- Claim IDs: `RYL-008`, `RYL-009`.

### Objective Genes

- `OBJ-007` — clear declared board-element targets. The scoped level requires
  collection of every displayed quantity of specified ordinary colour items.
- Completing one target is insufficient when several are shown. The goal must
  be reached before `CON-020` exhausts the attempt.
- Stars, coins and renovation are post-level rewards or meta-progression and do
  not enter the core objective signature.
- `OBJ-002` is absent: points may be displayed by implementations, but the
  official level rule defines victory through targets rather than maximum score.
- Claim IDs: `RYL-001`–`RYL-003`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One charged swap or
  activation is followed by all power-up effects, matches, collapse, refill and
  cascade steps before the board returns to a stable decision state.
- Animation duration is not a real-time decision window in the scoped model.
  The player can pause indefinitely once resolution is stable.
- Claim IDs: `RYL-003`, `RYL-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two adjacent ordinary items can form a same-colour line of three | Swap them | Match is detected and its ordinary items clear | Direct swap versus automatic removal | `RYL-002` |
| Clear leaves vacancies below retained items | Wait for resolution | Retained items fall and new items enter from above | Collapse and refill are separate behaviours | `RYL-004` |
| Collapse or refill forms another qualifying line | No new input | New line clears and resolution repeats | Cascade costs no second move | `RYL-004` |
| Four same-coloured items form a line | Complete the forming swap | Match resolves into a Rocket at the creation position | Pattern-conditioned special creation | `RYL-005` |
| Rocket is present | Tap or swap it | System clears its directed row or column | Action / effect separation | `RYL-006` |
| Rocket and TNT are adjacent | Swap them together | System clears three rows and three columns | Combination as parameterised effect | `RYL-007` |
| Final required target item clears with one move left | Resolve the move | Level completes before budget failure | Objective check precedes exhaustion loss | `RYL-001`, `RYL-003` |
| Last move resolves without completing every target | Finish resolution | Attempt fails at zero remaining moves | Terminal action budget | `RYL-003` |

## Strategic and experiential structure

- Local decision: choose an adjacent swap that advances a target, creates a
  power-up or improves the board after collapse.
- Medium-term planning: conserve moves, position power-ups for combinations and
  anticipate which columns will collapse after a clear.
- Long-term structure: allocate the finite move budget among multiple target
  quantities while exploiting free cascade progress.
- Common heuristics: prefer moves with direct target credit; value larger
  pattern matches; combine power-ups when their expanded footprint intersects
  targets; avoid spending moves in irrelevant board regions.
- Failure attribution: a swap has visible immediate consequences but random
  refill can amplify or reduce its downstream value, so outcomes are not fully
  attributable to planning.
- Player-trust factors: targets and move budget are explicit; unpublished
  refill distributions prevent exact forward prediction and should not be
  described as uniformly random or intentionally biased without evidence.
- Claim IDs: `RYL-003`–`RYL-009`.

## Replay and variation

- What changes between attempts: initial item arrangement and unpreviewed
  refill outcomes may vary; target quantities and move allowance belong to the
  selected level definition.
- Randomness: in-play refill and some target selection effects.
- Multiple viable strategies: different swaps, power-up creation patterns and
  cascade outcomes may reach the same target counts.
- Typical replay motive: retry after budget exhaustion or find a sequence that
  uses fewer charged moves.
- Claim IDs: `RYL-003`, `RYL-008`, `RYL-009`.

## Adjacent systems and history

- Dream Games describes Royal Match as one of its mobile titles. This analysis
  does not treat decoration or live-service progression as puzzle mechanics of
  the selected level.
- Bejeweled-family research corroborates the clear-collapse-refill cascade but
  does not prove Royal Match's unpublished random distribution or level
  solvability.
- Match-3 variants based on selecting clusters, tracing chains or firing pieces
  do not share `ACT-011` or `CON-019` merely because they clear three items.
- Obstacle-heavy Royal Match levels can add hit counters, adjacency effects,
  transport paths and access restrictions. Those are excluded, not silently
  compressed into `OBJ-007`.
- Complexity caveat: scalable match-3 hardness results do not establish the
  human difficulty of a fixed Royal Match level.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-011`, `ACT-012` | activation gesture and power-up composition |
| System Behaviour | `SYS-003`, `SYS-004`, `SYS-010`, `SYS-011`, `SYS-012`, `SYS-013`, `SYS-014` | refill distribution and effect footprints |
| Constraint | `CON-001`, `CON-019`, `CON-020` | board size, colour count and move allowance |
| Information | `INF-001`, `INF-002` | no future refill preview |
| Objective | `OBJ-007` | target classes and quantities |
| Time | `TIM-001` | one input followed by stable resolution |

Canonical signature:

`ACT-011,ACT-012; SYS-003,SYS-004,SYS-010,SYS-011,SYS-012,SYS-013,SYS-014; CON-001,CON-019,CON-020; INF-001,INF-002; OBJ-007; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `8` (`GAME-0001`–`GAME-0008`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`6 / 24 = 0.250000`).
- Supported combination subsets: `COMB-0009`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` — 2048 | `SYS-003`, `SYS-004`, `CON-001`, `INF-001`, `INF-002`, `TIM-001` | Both resolve random insertion after discrete inputs; 2048 globally slides and merges values, while Royal Match validates local swaps then iterates clear-collapse-refill cascades under a move budget | Near, `0.250000` |

### Preserved research notes

- New combination: `COMB-0009`, whose nine genes are a proper subset of this
  sixteen-gene genome.
- New genes: `ACT-011`, `ACT-012`, `SYS-010`, `SYS-011`, `SYS-012`, `SYS-013`,
  `SYS-014`, `CON-019`, `CON-020`, `OBJ-007`.
- Classification result: `New gene`.
- Reused genes: `SYS-003`, `SYS-004`, `CON-001`, `INF-001`, `INF-002`,
  `TIM-001`.
- Evidence and reasoning: the decomposition preserves the checkpoint's
  Action/System boundary and distinguishes the cascade's removal, movement,
  insertion and repeat rules. Power-up identity and effect footprints are
  parameters inside creation and activation behaviours rather than one gene per
  named power-up.

## Taxonomy impact

- Registry changes: ten bounded genes added and six reused.
- Taxonomy-change record: none. Direct commands, automatic state transitions,
  move legality, visible / future information, targets and scheduling all fit
  the existing six types.
- Checkpoint result confirmed: System Behaviour reuse increased from one gene
  to three (`SYS-003`, `SYS-004` now join the previously reused set), while the
  cascade required five new bounded behaviours.
- Candidate terms affected: swap, match clear, gravity, refill, cascade,
  pattern-conditioned power-up, move limit and target clearing now have bounded
  mappings.
- Claim IDs: `RYL-010`.

## Negative results

Royal Match gravity does not reuse `SYS-001` or `SYS-006`: it is neither a
direction selected by the player nor continuous time-driven descent. Power-up
names were not admitted as separate genes because their creation patterns and
effect footprints fit parameters of `SYS-013` and `SYS-014`. Meta-progression
and Boosters were excluded rather than mixed into the core level genome.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Targets and finite moves define success and
  failure independently of score (`RYL-001`–`RYL-003`).
- [Pattern | Corroborated | Medium] One charged swap can trigger an unbounded-
  length but finite clear-collapse-refill cascade (`RYL-004`).
- [Confirmed | Direct | High] Larger match geometry creates persistent
  power-ups whose activated effects clear rule-selected footprints
  (`RYL-005`–`RYL-007`).

## Нові гени

- [Observation | Corroborated | High] `ACT-011`, `ACT-012`, `SYS-010`–`SYS-014`,
  `CON-019`, `CON-020` and `OBJ-007`.
- [Observation | Corroborated | High] `SYS-003`, `SYS-004`, `CON-001`,
  `INF-001`, `INF-002` and `TIM-001` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0009` — move-limited swap-and-cascade
  target clearing.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. The checkpoint
  boundary tests correctly separate direct swap / activation from automatic
  cascade and effect resolution.

## Нові питання

- TODO: analyse an obstacle-bearing Royal Match level separately before
  generalising obstacle hit and transport rules.
- TODO: test `SYS-011` in another vacancy-collapse puzzle with a different
  gravity topology.
- TODO: compare a deterministic-refill match-3 puzzle to isolate `SYS-004` and
  `INF-002` from the core cascade.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0010` — Water Sort.
- Optimisation criterion: return to a deterministic system while testing
  multi-layer container capacity, top-layer access and bounded empty vessels
  against FreeCell's single-card buffers.
- Expected information gain: determine whether pouring a maximal compatible
  top segment is a direct action or automatic post-selection resolution, and
  whether tube capacity is a parameter or a distinct layered constraint.
- Backlog impact: Water Sort moves from the coverage pool to the immediate task;
  Royal Match leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Water Sort directly challenges the broadest
  remaining buffer and capacity boundaries without repeating Royal Match's
  automatic random cascade family.
