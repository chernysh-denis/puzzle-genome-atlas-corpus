---
game_id: GAME-0116
slug: the-stanley-parable-ultra-deluxe
game_title: The Stanley Parable: Ultra Deluxe
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0115
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-149
  constraint:
    - CON-168
  information:
    - INF-001
  objective:
    - OBJ-052
  time:
    - TIM-003
---

# Game: The Stanley Parable: Ultra Deluxe

## Analysis scope

- Version / ruleset: Ultra Deluxe, bounded to one fresh run from office 427
  through the first two-door choice and one resulting terminal ending route.
- Included: first-person navigation, narrator's announced left route, choosing
  either open door by traversal, branch-specific response, authored downstream
  geometry, terminal ending and run reset.
- Excluded: New Content, bucket routes, prior-run unlocks, every other ending,
  achievements, settings jokes and thematic interpretation beyond mechanics.
- Direct-play status: not conducted. The developer describes choices and
  powerlessness; the product page labels choices and multiple endings.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TSP-001` | Ultra Deluxe is an expanded re-imagining built around choices and their removal | Confirmed | Direct | High | P1 |
| `TSP-002` | Traversing an authored route commits a narrator-recognised branch | Confirmed | Corroborated | High | P1, S1 |
| `TSP-003` | A terminal branch ending returns the player to a replay boundary | Observation | Corroborated | High | P1, S1 |

## Basic data

- Release / origin: Crows Crows Crows released Ultra Deluxe in 2022.
- Platform or physical form: first-person branching narrative exploration.
- Puzzle family: rule and interface manipulation; temporal replay.
- Primary sources: **[P1]** [official Steam page](https://store.steampowered.com/app/1703340/The_Stanley_Parable_Ultra_Deluxe/).
- Secondary sources: **[S1]** [official development showcase](https://www.stanleyparable.com/hds/3/).
- Claim IDs: `TSP-001`–`TSP-003`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates Stanley through one of the open routes.
- Candidate genes: none; the choice is embodied traversal, not a menu action.
- Claim IDs: `TSP-002`.

### System Behaviour Genes

- `SYS-149` selects narrator response and downstream authored state from the
  crossed route threshold and history.
- Resolution order: narration; traversal threshold; branch response; ending.
- Claim IDs: `TSP-002`, `TSP-003`.

### Constraint Genes

- `CON-168` limits agency to currently authored open branches and commits a path.
- Scarce strategic resources: unexplored branches within the current run.
- Claim IDs: `TSP-001`, `TSP-002`.

### Information Genes

- `INF-001` exposes open doors and current world state; narration discloses one
  proposed path.
- Candidate genes: none.
- Claim IDs: `TSP-002`.

### Objective Genes

- `OBJ-052` reaches one authored ending rather than a conventional win state.
- Success, evaluation and failure: terminal presentation closes the branch.
- Claim IDs: `TSP-003`.

### Time Genes

- `TIM-003` allows narration and trigger states to progress while walking.
- Candidate genes: none.
- Claim IDs: `TSP-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Narrator says Stanley took the left door; both doors are open | Walk through left | Following branch response begins | compliance is stateful | `TSP-002` |
| Same fork | Walk through right | Contradiction-specific response and route begin | embodied choice | `TSP-002` |
| Terminal trigger is reached | Continue | Ending is presented and replay becomes available | branch objective | `TSP-003` |

## Strategic and experiential structure

- Local decision: follow or contradict the described route.
- Medium-term planning: explore consequences of a committed branch.
- Long-term structure: learn the authored branch graph across repeated runs.
- Common heuristics: test the narrator's stated assumptions.
- Failure attribution: there is no universal failure; closure is branch-specific.
- Player-trust factors: responsiveness depends on acknowledging visible choices.
- Claim IDs: `TSP-001`–`TSP-003`.

## Replay and variation

- What changes between sessions: route choices and later retained unlocks outside scope.
- Randomness or procedural generation: none in the bounded branch.
- Multiple viable strategies: multiple authored routes, not freeform outcomes.
- Typical replay motive: discover another ending and narrator response.
- Claim IDs: `TSP-003`.

## Adjacent systems and history

- Direct predecessors: branching interactive fiction and walking simulators.
- Variants: 2013 edition; expanded Ultra Deluxe content outside scope.
- Similar games: Antichamber and Outer Wilds at reset / knowledge boundaries.
- Important differences: narration explicitly anticipates and reinterprets traversal.
- Claim IDs: `TSP-002`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | route choice |
| System Behaviour | `SYS-149` | narrator branch table |
| Constraint | `CON-168` | authored routes |
| Information | `INF-001` | door and narration cues |
| Objective | `OBJ-052` | ending route |
| Time | `TIM-003` | trigger timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `115` (`GAME-0001`–`GAME-0115`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 10 = 0.300000`).
- Supported combination subsets: `COMB-0115`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0098`.

## Taxonomy impact

- Registry changes: `SYS-149`, `CON-168`, `OBJ-052`.
- Taxonomy-change record: none.
- Candidate terms affected: narrated branch.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Traversal itself is the branch-selection
  interface and narration is its stateful response (`TSP-002`).

## Нові гени

- [Observation | Corroborated | High] `SYS-149`, `CON-168`, `OBJ-052`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0115`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which retained Ultra Deluxe unlocks deserve a loop-retention scope?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] OneShot.
- Optimisation criterion: move from narrated fourth-wall response to external interface action.
- Expected information gain: host artefact as required clue channel.
- Backlog impact: finish the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It tests whether meta-interface interaction is a real mechanical boundary.
