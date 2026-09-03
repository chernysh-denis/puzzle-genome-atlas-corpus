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

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `114` (`GAME-0001`–`GAME-0114`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`3 / 10 = 0.300000`); `GAME-0008` — Nonogram (`3 / 10 = 0.300000`); `GAME-0071` — Slant (`3 / 10 = 0.300000`); `GAME-0073` — Dominosa (`3 / 10 = 0.300000`); `GAME-0076` — Loopy (`3 / 10 = 0.300000`); `GAME-0077` — Map (`3 / 10 = 0.300000`); `GAME-0078` — Galaxies (`3 / 10 = 0.300000`); `GAME-0079` — Filling (`3 / 10 = 0.300000`); `GAME-0080` — Keen (`3 / 10 = 0.300000`).
- Supported combination subsets: `COMB-0114`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0005`, `GAME-0008`, `GAME-0071`, `GAME-0073`, `GAME-0076`, `GAME-0077`, `GAME-0078`, `GAME-0079`, `GAME-0080`.

## Taxonomy impact

- Registry changes: `SYS-148`, `CON-167`.
- Taxonomy-change record: none.
- Candidate terms affected: semantic packing.

## Negative results

- `none`.
