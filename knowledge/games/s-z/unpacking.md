---
game_id: GAME-0115
slug: unpacking
game_title: Unpacking
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0114
gene_ids:
  action:
    - ACT-048
  system:
    - SYS-148
  constraint:
    - CON-167
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Unpacking

## Analysis scope

- Version / ruleset: one ordinary early bedroom stage, bounded to removing every
  object from boxes, freely repositioning it among visible room supports and
  completing only when every object occupies an accepted context.
- Included: box-order reveal, drag / release, shelves, drawers, wardrobe,
  surfaces, collision footprints, invalid-placement markers and completion.
- Excluded: story interpretation, later multi-room moves, stickers, photo mode,
  accessibility mode that disables placement puzzles and achievements.
- Direct-play status: not conducted. Witch Beam defines the unpack-and-place
  loop; developer commentary establishes objects as authored life evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `UNP-001` | The player removes possessions from boxes and places them into a room | Confirmed | Direct | High | P1, P2 |
| `UNP-002` | Completion accepts classes of contextually suitable placements rather than one exact arrangement | Confirmed | Corroborated | High | P1, P2 |
| `UNP-003` | Object meaning is communicated through placement constraints without explicit textual orders | Pattern | Corroborated | Medium | P2 |

## Basic data

- Release / origin: Witch Beam released Unpacking in 2021.
- Platform or physical form: pointer / touch spatial organisation puzzle.
- Puzzle family: spatial assembly and constraint satisfaction.
- Primary sources: **[P1]** [official Unpacking site](https://www.unpackinggame.com/);
  **[P2]** [developer PlayStation article](https://blog.playstation.com/?p=364454).
- Claim IDs: `UNP-001`–`UNP-003`.

## Mechanical decomposition

### Action Genes

- `ACT-048` directly picks up, moves and releases one household object.
- Candidate genes: none; pointer drag and rotation availability are parameters.
- Claim IDs: `UNP-001`.

### System Behaviour Genes

- `SYS-148` validates every placed object once boxes are empty and marks invalids.
- Resolution order: reveal object; place; empty all boxes; validate; complete.
- Claim IDs: `UNP-002`.

### Constraint Genes

- `CON-167` requires non-overlap and an accepted room / support affordance.
- Scarce strategic resources: shelf, drawer and surface space.
- Claim IDs: `UNP-002`, `UNP-003`.

### Information Genes

- `INF-001` shows all revealed objects, supports and current invalid markers.
- Candidate genes: none; unrevealed box order is setup sequencing, not hidden deduction.
- Claim IDs: `UNP-001`.

### Objective Genes

- `OBJ-006` requires a complete constraint-satisfying placement assignment.
- Success, evaluation and failure: every item placed legally; no irreversible failure.
- Claim IDs: `UNP-002`.

### Time Genes

- `TIM-002` permits self-paced reorganisation.
- Candidate genes: none.
- Claim IDs: `UNP-001`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Box still contains an item | Select top item | Item becomes movable and leaves the box | ordered reveal | `UNP-001` |
| Shirt is released into wardrobe | Place without overlap | Placement remains accepted | affordance class | `UNP-002` |
| Shirt is released on an invalid support | Empty remaining boxes | Shirt is marked invalid and completion is withheld | semantic constraint | `UNP-002` |

## Strategic and experiential structure

- Local decision: fit one object into an appropriate visible support.
- Medium-term planning: reserve constrained storage for specialised objects.
- Long-term structure: make every possession contextually valid.
- Common heuristics: group by use and exploit drawers / vertical shelves.
- Failure attribution: invalid objects are identified after placement.
- Player-trust factors: validation must allow plausible alternatives.
- Claim IDs: `UNP-002`, `UNP-003`.

## Replay and variation

- What changes between sessions: chosen valid arrangement.
- Randomness or procedural generation: none.
- Multiple viable strategies: yes, by design.
- Typical replay motive: create a different personal arrangement.
- Claim IDs: `UNP-002`.

## Adjacent systems and history

- Direct predecessors: dollhouse organisation and inventory packing.
- Variants: later stages add rooms and shared spaces.
- Similar games: Sudoku at the abstract assignment layer; spatial packing games.
- Important differences: compatibility is semantic and many final layouts are valid.
- Claim IDs: `UNP-003`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-048` | drag; optional rotation |
| System Behaviour | `SYS-148` | validation timing |
| Constraint | `CON-167` | room / support affordances |
| Information | `INF-001` | invalid marker |
| Objective | `OBJ-006` | complete assignment |
| Time | `TIM-002` | self-paced |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-048; SYS-148; CON-167; INF-001; OBJ-006; TIM-002`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0005` — Sudoku at `3 / 10 = 0.300000`; `GAME-0008` — Nonogram at `3 / 10 = 0.300000`; `GAME-0071` — Slant at `3 / 10 = 0.300000`; `GAME-0073` — Dominosa at `3 / 10 = 0.300000`; `GAME-0076` — Loopy at `3 / 10 = 0.300000`; `GAME-0077` — Map at `3 / 10 = 0.300000`; `GAME-0078` — Galaxies at `3 / 10 = 0.300000`; `GAME-0079` — Filling at `3 / 10 = 0.300000`; `GAME-0080` — Keen at `3 / 10 = 0.300000`.
- Supported combination subsets: `COMB-0114`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 19 = 0.052632`; `GAME-0002`: `2 / 11 = 0.181818`; `GAME-0003`: `0 / 15 = 0.000000`; `GAME-0004`: `1 / 20 = 0.050000`.
- `GAME-0005`: `3 / 10 = 0.300000`; `GAME-0006`: `2 / 13 = 0.153846`; `GAME-0007`: `2 / 12 = 0.166667`; `GAME-0008`: `3 / 10 = 0.300000`.
- `GAME-0009`: `1 / 21 = 0.047619`; `GAME-0010`: `1 / 14 = 0.071429`; `GAME-0011`: `2 / 17 = 0.117647`; `GAME-0012`: `3 / 12 = 0.250000`.
- `GAME-0013`: `1 / 18 = 0.055556`; `GAME-0014`: `1 / 20 = 0.050000`; `GAME-0015`: `1 / 19 = 0.052632`; `GAME-0016`: `1 / 20 = 0.050000`.
- `GAME-0017`: `0 / 19 = 0.000000`; `GAME-0018`: `1 / 24 = 0.041667`; `GAME-0019`: `1 / 15 = 0.066667`; `GAME-0020`: `1 / 19 = 0.052632`.
- `GAME-0021`: `1 / 14 = 0.071429`; `GAME-0022`: `1 / 17 = 0.058824`; `GAME-0023`: `1 / 15 = 0.066667`; `GAME-0024`: `1 / 17 = 0.058824`.
- `GAME-0025`: `1 / 16 = 0.062500`; `GAME-0026`: `1 / 17 = 0.058824`; `GAME-0027`: `1 / 17 = 0.058824`; `GAME-0028`: `1 / 22 = 0.045455`.
- `GAME-0029`: `1 / 17 = 0.058824`; `GAME-0030`: `1 / 19 = 0.052632`; `GAME-0031`: `1 / 16 = 0.062500`; `GAME-0032`: `1 / 16 = 0.062500`.
- `GAME-0033`: `2 / 17 = 0.117647`; `GAME-0034`: `1 / 19 = 0.052632`; `GAME-0035`: `1 / 23 = 0.043478`; `GAME-0036`: `2 / 16 = 0.125000`.
- `GAME-0037`: `1 / 14 = 0.071429`; `GAME-0038`: `1 / 21 = 0.047619`; `GAME-0039`: `3 / 12 = 0.250000`; `GAME-0040`: `2 / 12 = 0.166667`.
- `GAME-0041`: `1 / 16 = 0.062500`; `GAME-0042`: `1 / 14 = 0.071429`; `GAME-0043`: `1 / 19 = 0.052632`; `GAME-0044`: `1 / 15 = 0.066667`.
- `GAME-0045`: `1 / 19 = 0.052632`; `GAME-0046`: `2 / 14 = 0.142857`; `GAME-0047`: `1 / 19 = 0.052632`; `GAME-0048`: `1 / 19 = 0.052632`.
- `GAME-0049`: `0 / 15 = 0.000000`; `GAME-0050`: `1 / 20 = 0.050000`; `GAME-0051`: `1 / 21 = 0.047619`; `GAME-0052`: `1 / 15 = 0.066667`.
- `GAME-0053`: `1 / 14 = 0.071429`; `GAME-0054`: `1 / 16 = 0.062500`; `GAME-0055`: `2 / 14 = 0.142857`; `GAME-0056`: `1 / 13 = 0.076923`.
- `GAME-0057`: `1 / 13 = 0.076923`; `GAME-0058`: `1 / 14 = 0.071429`; `GAME-0059`: `1 / 12 = 0.083333`; `GAME-0060`: `1 / 12 = 0.083333`.
- `GAME-0061`: `3 / 13 = 0.230769`; `GAME-0062`: `3 / 11 = 0.272727`; `GAME-0063`: `2 / 11 = 0.181818`; `GAME-0064`: `2 / 9 = 0.222222`.
- `GAME-0065`: `1 / 12 = 0.083333`; `GAME-0066`: `1 / 15 = 0.066667`; `GAME-0067`: `0 / 14 = 0.000000`; `GAME-0068`: `1 / 13 = 0.076923`.
- `GAME-0069`: `2 / 12 = 0.166667`; `GAME-0070`: `1 / 13 = 0.076923`; `GAME-0071`: `3 / 10 = 0.300000`; `GAME-0072`: `3 / 11 = 0.272727`.
- `GAME-0073`: `3 / 10 = 0.300000`; `GAME-0074`: `3 / 12 = 0.250000`; `GAME-0075`: `3 / 12 = 0.250000`; `GAME-0076`: `3 / 10 = 0.300000`.
- `GAME-0077`: `3 / 10 = 0.300000`; `GAME-0078`: `3 / 10 = 0.300000`; `GAME-0079`: `3 / 10 = 0.300000`; `GAME-0080`: `3 / 10 = 0.300000`.
- `GAME-0081`: `3 / 11 = 0.272727`; `GAME-0082`: `3 / 11 = 0.272727`; `GAME-0083`: `3 / 11 = 0.272727`; `GAME-0084`: `3 / 13 = 0.230769`.
- `GAME-0085`: `1 / 16 = 0.062500`; `GAME-0086`: `2 / 17 = 0.117647`; `GAME-0087`: `1 / 15 = 0.066667`; `GAME-0088`: `2 / 13 = 0.153846`.
- `GAME-0089`: `1 / 14 = 0.071429`; `GAME-0090`: `2 / 19 = 0.105263`; `GAME-0091`: `1 / 14 = 0.071429`; `GAME-0092`: `1 / 15 = 0.066667`.
- `GAME-0093`: `2 / 13 = 0.153846`; `GAME-0094`: `2 / 14 = 0.142857`; `GAME-0095`: `2 / 16 = 0.125000`; `GAME-0096`: `2 / 14 = 0.142857`.
- `GAME-0097`: `1 / 13 = 0.076923`; `GAME-0098`: `1 / 12 = 0.083333`; `GAME-0099`: `1 / 13 = 0.076923`; `GAME-0100`: `0 / 17 = 0.000000`.
- `GAME-0101`: `1 / 15 = 0.066667`; `GAME-0102`: `2 / 11 = 0.181818`; `GAME-0103`: `1 / 14 = 0.071429`; `GAME-0104`: `1 / 14 = 0.071429`.
- `GAME-0105`: `0 / 16 = 0.000000`; `GAME-0106`: `1 / 12 = 0.083333`; `GAME-0107`: `2 / 12 = 0.166667`; `GAME-0108`: `3 / 13 = 0.230769`.
- `GAME-0109`: `1 / 21 = 0.047619`; `GAME-0110`: `1 / 13 = 0.076923`; `GAME-0111`: `2 / 11 = 0.181818`; `GAME-0112`: `2 / 12 = 0.166667`.
- `GAME-0113`: `2 / 18 = 0.111111`; `GAME-0114`: `1 / 12 = 0.083333`.

## Taxonomy impact

- Registry changes: `SYS-148`, `CON-167`.
- Taxonomy-change record: none.
- Candidate terms affected: semantic packing.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Unpacking validates placement classes, not
  one canonical room layout (`UNP-002`).

## Нові гени

- [Observation | Corroborated | High] `SYS-148`, `CON-167`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0114`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which later shared-room exceptions broaden the compatibility boundary?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] The Stanley Parable: Ultra Deluxe.
- Optimisation criterion: test route choice as narrative state.
- Expected information gain: authored branch response and ending objective.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It moves from spatial correctness to authored choice interpretation.
