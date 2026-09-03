---
game_id: GAME-0112
slug: human-fall-flat
game_title: Human: Fall Flat
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0111
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-114
  system:
    - SYS-036
  constraint:
    - CON-165
  information:
    - INF-001
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Human: Fall Flat

## Analysis scope

- Version / ruleset: single-player base game, bounded to one small physics room
  requiring a crate to be carried beneath a ledge and used while climbing to
  the visible exit.
- Included: walking, jumping, independent arms, contact-held grip, ragdoll
  physics, crate pickup / release, leverage, gravity, collision and exit reach.
- Excluded: multiplayer, vehicles, breakable walls, workshop levels, cosmetics,
  later official maps and platform-specific controls.
- Direct-play status: not conducted. The developer explicitly defines direct
  control, grabbing, climbing, carrying and real physical laws.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HFF-001` | The avatar can walk, jump, grab, climb and carry in a live 3D physics world | Confirmed | Direct | High | P1, P2 |
| `HFF-002` | A grip requires articulated hand contact and remains subject to body leverage | Confirmed | Corroborated | High | P1, P2 |
| `HFF-003` | Open physical solutions permit multiple valid routes to the same exit | Pattern | Corroborated | Medium | P1, P2 |

## Basic data

- Release / origin: No Brakes Games released Human: Fall Flat in 2016.
- Platform or physical form: third-person physics puzzle platformer.
- Puzzle family: physics and object manipulation.
- Primary sources: **[P1]** [No Brakes Games product page](https://nobrakesgames.itch.io/human);
  **[P2]** [developer PlayStation article](https://blog.playstation.com/2017/04/25/master-the-art-of-wobbly-parkour-in-human-fall-flat-out-may-9/).
- Claim IDs: `HFF-001`–`HFF-003`.

## Mechanical decomposition

### Action Genes

- `ACT-008` moves the ragdoll, `ACT-048` carries the crate and `ACT-114`
  independently grips ledges with the two hands.
- Candidate genes: none.
- Claim IDs: `HFF-001`, `HFF-002`.

### System Behaviour Genes

- `SYS-036` continuously resolves gravity, joints, rigid contacts and momentum.
- Resolution order: input forces and grips; joint integration; collision; settle.
- Claim IDs: `HFF-001`, `HFF-002`.

### Constraint Genes

- `CON-165` requires hand contact and sufficient leverage to sustain a grip.
- Scarce strategic resources: reachable geometry and body pose, not inventory.
- Claim IDs: `HFF-002`.

### Information Genes

- `INF-001` visibly exposes avatar, crate, ledge and exit.
- Candidate genes: none.
- Claim IDs: `HFF-001`.

### Objective Genes

- `OBJ-026` requires reaching the visible exit after making the route traversable.
- Success, evaluation and failure: arrival succeeds; falls reset position.
- Claim IDs: `HFF-003`.

### Time Genes

- `TIM-003` keeps physics active while movement and gripping inputs occur.
- Candidate genes: none.
- Claim IDs: `HFF-001`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Hand is below and away from ledge | Hold grip | No grip appears | contact gate | `HFF-002` |
| Raised hand contacts ledge | Hold that hand | Contact becomes a live joint | articulated grip | `HFF-002` |
| Both hands grip while legs swing | Pull and look upward | Body rotates and rises under physics | leverage, not scripted mantle | `HFF-002` |

## Strategic and experiential structure

- Local decision: choose contact point and body pose.
- Medium-term planning: move crate to create reachable leverage.
- Long-term structure: chain improvised physical affordances to the exit.
- Common heuristics: secure one hand before releasing the other.
- Failure attribution: pose and grip errors are visible but physics is nonlinear.
- Player-trust factors: permissive alternatives are part of the design promise.
- Claim IDs: `HFF-002`, `HFF-003`.

## Replay and variation

- What changes between sessions: physical trajectory and chosen route.
- Randomness or procedural generation: none in the scoped room.
- Multiple viable strategies: yes.
- Typical replay motive: improvise or cooperate outside scope.
- Claim IDs: `HFF-003`.

## Adjacent systems and history

- Direct predecessors: physics platformers and manipulation sandboxes.
- Variants: multiplayer is excluded.
- Similar games: Cut the Rope, Portal and Superliminal.
- Important differences: the controllable body itself is an articulated tool.
- Claim IDs: `HFF-002`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-114` | arm channels |
| System Behaviour | `SYS-036` | joint and rigid-body solver |
| Constraint | `CON-165` | reach and grip |
| Information | `INF-001` | camera framing |
| Objective | `OBJ-026` | exit location |
| Time | `TIM-003` | live physics |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `111` (`GAME-0001`–`GAME-0111`).
- Exact genome matches: none.
- Tied near matches: `GAME-0091` — Fez (`5 / 12 = 0.416667`).
- Supported combination subsets: `COMB-0111`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0091`.

## Taxonomy impact

- Registry changes: two Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: ragdoll climbing.

## Negative results

- `none`.
