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

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `110` (`GAME-0001`–`GAME-0110`).
- Exact genome matches: none.
- Tied near matches: `GAME-0086` — Machinarium (`5 / 15 = 0.333333`).
- Supported combination subsets: `COMB-0110`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0086`.

## Taxonomy impact

- Registry changes: none.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- `none`.
