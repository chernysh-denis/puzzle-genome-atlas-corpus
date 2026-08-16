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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008; SYS-149; CON-168; INF-001; OBJ-052; TIM-003`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0098` — Hyperbolica at `3 / 10 = 0.300000`.
- Supported combination subsets: `COMB-0115`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 19 = 0.052632`; `GAME-0002`: `1 / 12 = 0.083333`; `GAME-0003`: `0 / 15 = 0.000000`; `GAME-0004`: `2 / 19 = 0.105263`.
- `GAME-0005`: `1 / 12 = 0.083333`; `GAME-0006`: `2 / 13 = 0.153846`; `GAME-0007`: `1 / 13 = 0.076923`; `GAME-0008`: `1 / 12 = 0.083333`.
- `GAME-0009`: `1 / 21 = 0.047619`; `GAME-0010`: `1 / 14 = 0.071429`; `GAME-0011`: `1 / 18 = 0.055556`; `GAME-0012`: `1 / 14 = 0.071429`.
- `GAME-0013`: `1 / 18 = 0.055556`; `GAME-0014`: `1 / 20 = 0.050000`; `GAME-0015`: `1 / 19 = 0.052632`; `GAME-0016`: `2 / 19 = 0.105263`.
- `GAME-0017`: `0 / 19 = 0.000000`; `GAME-0018`: `2 / 23 = 0.086957`; `GAME-0019`: `1 / 15 = 0.066667`; `GAME-0020`: `1 / 19 = 0.052632`.
- `GAME-0021`: `2 / 13 = 0.153846`; `GAME-0022`: `1 / 17 = 0.058824`; `GAME-0023`: `0 / 16 = 0.000000`; `GAME-0024`: `1 / 17 = 0.058824`.
- `GAME-0025`: `2 / 15 = 0.133333`; `GAME-0026`: `2 / 16 = 0.125000`; `GAME-0027`: `2 / 16 = 0.125000`; `GAME-0028`: `2 / 21 = 0.095238`.
- `GAME-0029`: `3 / 15 = 0.200000`; `GAME-0030`: `2 / 18 = 0.111111`; `GAME-0031`: `1 / 16 = 0.062500`; `GAME-0032`: `1 / 16 = 0.062500`.
- `GAME-0033`: `3 / 16 = 0.187500`; `GAME-0034`: `3 / 17 = 0.176471`; `GAME-0035`: `3 / 21 = 0.142857`; `GAME-0036`: `2 / 16 = 0.125000`.
- `GAME-0037`: `1 / 14 = 0.071429`; `GAME-0038`: `3 / 19 = 0.157895`; `GAME-0039`: `1 / 14 = 0.071429`; `GAME-0040`: `2 / 12 = 0.166667`.
- `GAME-0041`: `3 / 14 = 0.214286`; `GAME-0042`: `1 / 14 = 0.071429`; `GAME-0043`: `2 / 18 = 0.111111`; `GAME-0044`: `2 / 14 = 0.142857`.
- `GAME-0045`: `2 / 18 = 0.111111`; `GAME-0046`: `1 / 15 = 0.066667`; `GAME-0047`: `1 / 19 = 0.052632`; `GAME-0048`: `1 / 19 = 0.052632`.
- `GAME-0049`: `0 / 15 = 0.000000`; `GAME-0050`: `2 / 19 = 0.105263`; `GAME-0051`: `2 / 20 = 0.100000`; `GAME-0052`: `1 / 15 = 0.066667`.
- `GAME-0053`: `2 / 13 = 0.153846`; `GAME-0054`: `2 / 15 = 0.133333`; `GAME-0055`: `2 / 14 = 0.142857`; `GAME-0056`: `1 / 13 = 0.076923`.
- `GAME-0057`: `1 / 13 = 0.076923`; `GAME-0058`: `1 / 14 = 0.071429`; `GAME-0059`: `1 / 12 = 0.083333`; `GAME-0060`: `1 / 12 = 0.083333`.
- `GAME-0061`: `1 / 15 = 0.066667`; `GAME-0062`: `1 / 13 = 0.076923`; `GAME-0063`: `1 / 12 = 0.083333`; `GAME-0064`: `1 / 10 = 0.100000`.
- `GAME-0065`: `0 / 13 = 0.000000`; `GAME-0066`: `0 / 16 = 0.000000`; `GAME-0067`: `0 / 14 = 0.000000`; `GAME-0068`: `0 / 14 = 0.000000`.
- `GAME-0069`: `1 / 13 = 0.076923`; `GAME-0070`: `1 / 13 = 0.076923`; `GAME-0071`: `1 / 12 = 0.083333`; `GAME-0072`: `1 / 13 = 0.076923`.
- `GAME-0073`: `1 / 12 = 0.083333`; `GAME-0074`: `1 / 14 = 0.071429`; `GAME-0075`: `1 / 14 = 0.071429`; `GAME-0076`: `1 / 12 = 0.083333`.
- `GAME-0077`: `1 / 12 = 0.083333`; `GAME-0078`: `1 / 12 = 0.083333`; `GAME-0079`: `1 / 12 = 0.083333`; `GAME-0080`: `1 / 12 = 0.083333`.
- `GAME-0081`: `1 / 13 = 0.076923`; `GAME-0082`: `1 / 13 = 0.076923`; `GAME-0083`: `1 / 13 = 0.076923`; `GAME-0084`: `1 / 15 = 0.066667`.
- `GAME-0085`: `0 / 17 = 0.000000`; `GAME-0086`: `1 / 18 = 0.055556`; `GAME-0087`: `2 / 14 = 0.142857`; `GAME-0088`: `1 / 14 = 0.071429`.
- `GAME-0089`: `1 / 14 = 0.071429`; `GAME-0090`: `2 / 19 = 0.105263`; `GAME-0091`: `3 / 12 = 0.250000`; `GAME-0092`: `2 / 14 = 0.142857`.
- `GAME-0093`: `1 / 14 = 0.071429`; `GAME-0094`: `3 / 13 = 0.230769`; `GAME-0095`: `3 / 15 = 0.200000`; `GAME-0096`: `3 / 13 = 0.230769`.
- `GAME-0097`: `3 / 11 = 0.272727`; `GAME-0098`: `3 / 10 = 0.300000`; `GAME-0099`: `2 / 12 = 0.166667`; `GAME-0100`: `1 / 16 = 0.062500`.
- `GAME-0101`: `0 / 16 = 0.000000`; `GAME-0102`: `0 / 13 = 0.000000`; `GAME-0103`: `1 / 14 = 0.071429`; `GAME-0104`: `2 / 13 = 0.153846`.
- `GAME-0105`: `2 / 14 = 0.142857`; `GAME-0106`: `0 / 13 = 0.000000`; `GAME-0107`: `2 / 12 = 0.166667`; `GAME-0108`: `2 / 14 = 0.142857`.
- `GAME-0109`: `1 / 21 = 0.047619`; `GAME-0110`: `2 / 12 = 0.166667`; `GAME-0111`: `2 / 11 = 0.181818`; `GAME-0112`: `3 / 11 = 0.272727`.
- `GAME-0113`: `3 / 17 = 0.176471`; `GAME-0114`: `2 / 11 = 0.181818`; `GAME-0115`: `1 / 11 = 0.090909`.

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
