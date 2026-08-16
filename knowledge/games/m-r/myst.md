---
game_id: GAME-0111
slug: myst
game_title: Myst
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0110
gene_ids:
  action:
    - ACT-008
    - ACT-085
  system:
    - SYS-112
  constraint:
    - CON-136
  information:
    - INF-001
  objective:
    - OBJ-025
  time:
    - TIM-002
---

# Game: Myst

## Analysis scope

- Version / ruleset: Myst 2021 remake, bounded to the Myst Island tower-rotation
  dependency that exposes one Age access clue and culminates in acquiring the
  corresponding linking-book route.
- Included: first-person navigation, operating the library map / tower control,
  observing the aligned clue, applying the disclosed mechanism settings and
  reaching the revealed linking book.
- Excluded: other Ages, randomised-puzzle option, page collection, endings,
  narrative interpretation, VR controls and complete-island walkthrough.
- Direct-play status: not conducted. Cyan describes Myst as exploration across
  surreal Ages and the scoped sequence is treated as a bounded mechanism packet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MYS-001` | Myst uses exploration and puzzle-solving to open routes between authored Ages | Confirmed | Direct | High | P1 |
| `MYS-002` | The scoped access path is a persistent dependency chain of world mechanisms and disclosed clues | Observation | Corroborated | Medium | P1, S1 |
| `MYS-003` | The packet reuses existing mechanism-dependency boundaries without a new gene | Observation | Corroborated | High | corpus scan |

## Basic data

- Release / origin: Cyan's original Myst appeared in 1993; the scoped remake
  presents the same island as free first-person traversal.
- Platform or physical form: first-person puzzle adventure.
- Puzzle family: knowledge and evidence progression; ordered dependencies.
- Primary sources: **[P1]** [Cyan games catalogue](https://cyan.com/games/).
- Secondary sources: **[S1]** [Library and Archives Canada Myst overview](https://epe.lac-bac.gc.ca/100/201/300/media_free/v32n01/myst.pdf?nodisclaimer=1).
- Claim IDs: `MYS-001`–`MYS-003`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates the island; `ACT-085` turns and commits constrained
  diegetic controls.
- Candidate genes: none.
- Claim IDs: `MYS-001`, `MYS-002`.

### System Behaviour Genes

- `SYS-112` exposes the next authored mechanism state after accepted operation.
- Resolution order: align; reveal clue; configure dependent mechanism; expose route.
- Claim IDs: `MYS-002`.

### Constraint Genes

- `CON-136` requires every earlier state in the access chain.
- Scarce strategic resources: information, not consumable inventory.
- Claim IDs: `MYS-002`.

### Information Genes

- `INF-001` exposes each current local mechanism state.
- Candidate genes: none; clues may be offscreen but are not hidden random state.
- Claim IDs: `MYS-002`.

### Objective Genes

- `OBJ-025` credits the bounded puzzle by reaching its linking-book route.
- Success, evaluation and failure: route exposed; invalid configurations remain reversible.
- Claim IDs: `MYS-001`.

### Time Genes

- `TIM-002` allows self-paced inspection and operation.
- Candidate genes: none.
- Claim IDs: `MYS-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Tower marker is unaligned | Rotate the map control | Tower orientation changes persistently | diegetic state edit | `MYS-002` |
| Correct alignment is active | Enter the tower | Authored clue becomes observable | state-gated evidence | `MYS-002` |
| Dependent mechanism matches the clue | Commit its control | Linking route becomes available | prerequisite chain | `MYS-002` |

## Strategic and experiential structure

- Local decision: inspect and operate one visible mechanism.
- Medium-term planning: carry a clue between separated locations.
- Long-term structure: expand the graph of reachable Ages.
- Common heuristics: write down values and relate landmarks.
- Failure attribution: wrong configurations are reversible and observable.
- Player-trust factors: clue identity must remain stable across travel.
- Claim IDs: `MYS-001`, `MYS-002`.

## Replay and variation

- What changes between sessions: route order and, outside scope, optional randomisation.
- Randomness or procedural generation: excluded.
- Multiple viable strategies: observation order may vary.
- Typical replay motive: rediscover authored dependencies.
- Claim IDs: `MYS-001`.

## Adjacent systems and history

- Direct predecessors: graphical adventure and mechanical puzzle spaces.
- Variants: original node navigation versus remake free movement.
- Similar games: The Room and Tunic.
- Important differences: clues are spatially distributed across an explorable Age.
- Claim IDs: `MYS-003`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-085` | navigation model |
| System Behaviour | `SYS-112` | revealed mechanism state |
| Constraint | `CON-136` | dependency graph |
| Information | `INF-001` | clue location |
| Objective | `OBJ-025` | route token |
| Time | `TIM-002` | self-paced |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008,ACT-085; SYS-112; CON-136; INF-001; OBJ-025; TIM-002`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0086` — Machinarium at `5 / 15 = 0.333333`.
- Supported combination subsets: `COMB-0110`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 20 = 0.050000`; `GAME-0002`: `2 / 12 = 0.166667`; `GAME-0003`: `0 / 16 = 0.000000`; `GAME-0004`: `1 / 21 = 0.047619`.
- `GAME-0005`: `2 / 12 = 0.166667`; `GAME-0006`: `3 / 13 = 0.230769`; `GAME-0007`: `2 / 13 = 0.153846`; `GAME-0008`: `2 / 12 = 0.166667`.
- `GAME-0009`: `1 / 22 = 0.045455`; `GAME-0010`: `1 / 15 = 0.066667`; `GAME-0011`: `2 / 18 = 0.111111`; `GAME-0012`: `2 / 14 = 0.142857`.
- `GAME-0013`: `1 / 19 = 0.052632`; `GAME-0014`: `1 / 21 = 0.047619`; `GAME-0015`: `1 / 20 = 0.050000`; `GAME-0016`: `1 / 21 = 0.047619`.
- `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `1 / 25 = 0.040000`; `GAME-0019`: `1 / 16 = 0.062500`; `GAME-0020`: `1 / 20 = 0.050000`.
- `GAME-0021`: `1 / 15 = 0.066667`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `1 / 18 = 0.055556`.
- `GAME-0025`: `1 / 17 = 0.058824`; `GAME-0026`: `1 / 18 = 0.055556`; `GAME-0027`: `1 / 18 = 0.055556`; `GAME-0028`: `1 / 23 = 0.043478`.
- `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `1 / 20 = 0.050000`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `1 / 17 = 0.058824`.
- `GAME-0033`: `2 / 18 = 0.111111`; `GAME-0034`: `2 / 19 = 0.105263`; `GAME-0035`: `2 / 23 = 0.086957`; `GAME-0036`: `3 / 16 = 0.187500`.
- `GAME-0037`: `1 / 15 = 0.066667`; `GAME-0038`: `3 / 20 = 0.150000`; `GAME-0039`: `2 / 14 = 0.142857`; `GAME-0040`: `3 / 12 = 0.250000`.
- `GAME-0041`: `2 / 16 = 0.125000`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `2 / 19 = 0.105263`; `GAME-0044`: `2 / 15 = 0.133333`.
- `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `2 / 15 = 0.133333`; `GAME-0047`: `1 / 20 = 0.050000`; `GAME-0048`: `1 / 20 = 0.050000`.
- `GAME-0049`: `0 / 16 = 0.000000`; `GAME-0050`: `2 / 20 = 0.100000`; `GAME-0051`: `1 / 22 = 0.045455`; `GAME-0052`: `1 / 16 = 0.062500`.
- `GAME-0053`: `2 / 14 = 0.142857`; `GAME-0054`: `2 / 16 = 0.125000`; `GAME-0055`: `2 / 15 = 0.133333`; `GAME-0056`: `1 / 14 = 0.071429`.
- `GAME-0057`: `1 / 14 = 0.071429`; `GAME-0058`: `1 / 15 = 0.066667`; `GAME-0059`: `1 / 13 = 0.076923`; `GAME-0060`: `1 / 13 = 0.076923`.
- `GAME-0061`: `2 / 15 = 0.133333`; `GAME-0062`: `2 / 13 = 0.153846`; `GAME-0063`: `2 / 12 = 0.166667`; `GAME-0064`: `2 / 10 = 0.200000`.
- `GAME-0065`: `1 / 13 = 0.076923`; `GAME-0066`: `1 / 16 = 0.062500`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `1 / 14 = 0.071429`.
- `GAME-0069`: `2 / 13 = 0.153846`; `GAME-0070`: `1 / 14 = 0.071429`; `GAME-0071`: `2 / 12 = 0.166667`; `GAME-0072`: `2 / 13 = 0.153846`.
- `GAME-0073`: `2 / 12 = 0.166667`; `GAME-0074`: `2 / 14 = 0.142857`; `GAME-0075`: `2 / 14 = 0.142857`; `GAME-0076`: `2 / 12 = 0.166667`.
- `GAME-0077`: `2 / 12 = 0.166667`; `GAME-0078`: `2 / 12 = 0.166667`; `GAME-0079`: `2 / 12 = 0.166667`; `GAME-0080`: `2 / 12 = 0.166667`.
- `GAME-0081`: `2 / 13 = 0.153846`; `GAME-0082`: `2 / 13 = 0.153846`; `GAME-0083`: `2 / 13 = 0.153846`; `GAME-0084`: `2 / 15 = 0.133333`.
- `GAME-0085`: `4 / 14 = 0.285714`; `GAME-0086`: `5 / 15 = 0.333333`; `GAME-0087`: `2 / 15 = 0.133333`; `GAME-0088`: `3 / 13 = 0.230769`.
- `GAME-0089`: `2 / 14 = 0.142857`; `GAME-0090`: `5 / 17 = 0.294118`; `GAME-0091`: `2 / 14 = 0.142857`; `GAME-0092`: `1 / 16 = 0.062500`.
- `GAME-0093`: `3 / 13 = 0.230769`; `GAME-0094`: `2 / 15 = 0.133333`; `GAME-0095`: `2 / 17 = 0.117647`; `GAME-0096`: `2 / 15 = 0.133333`.
- `GAME-0097`: `2 / 13 = 0.153846`; `GAME-0098`: `2 / 12 = 0.166667`; `GAME-0099`: `2 / 13 = 0.153846`; `GAME-0100`: `0 / 18 = 0.000000`.
- `GAME-0101`: `1 / 16 = 0.062500`; `GAME-0102`: `1 / 13 = 0.076923`; `GAME-0103`: `1 / 15 = 0.066667`; `GAME-0104`: `2 / 14 = 0.142857`.
- `GAME-0105`: `1 / 16 = 0.062500`; `GAME-0106`: `1 / 13 = 0.076923`; `GAME-0107`: `3 / 12 = 0.250000`; `GAME-0108`: `3 / 14 = 0.214286`.
- `GAME-0109`: `1 / 22 = 0.045455`; `GAME-0110`: `1 / 14 = 0.071429`.

## Taxonomy impact

- Registry changes: none.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Observation | Corroborated | Medium] Myst distributes one dependency chain
  across navigable locations (`MYS-002`).

## Нові гени

- [Observation | Corroborated | High] Нових генів немає.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0110`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which full-Age information channels merit a later broader scope?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Human: Fall Flat.
- Optimisation criterion: test continuous embodied manipulation.
- Expected information gain: articulated grips and leverage.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It separates authored mechanism use from open physics.
