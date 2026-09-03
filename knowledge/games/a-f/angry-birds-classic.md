---
game_id: GAME-0110
slug: angry-birds-classic
game_title: Angry Birds Classic
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0109
gene_ids:
  action:
    - ACT-113
  system:
    - SYS-146
    - SYS-147
  constraint:
    - CON-164
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-029
  time:
    - TIM-003
---

# Game: Angry Birds Classic

## Analysis scope

- Version / ruleset: Rovio Classics reconstruction of the original slingshot
  loop, bounded to one early level using only red birds, pigs and glass / wood
  / stone structures.
- Included: aim strength and direction, release, gravity, collision, material
  damage, support loss, cascading collapse, finite ordered birds, pig clearance
  and score.
- Excluded: mid-flight bird abilities, power-ups, Mighty Eagle, boss stages,
  three-star thresholds, advertisements and meta-progression.
- Direct-play status: not conducted. Rovio defines slingshot, tower destruction
  and pig popping; the bounded transition is corroborated by formal AI research.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ABC-001` | The player pulls and releases birds from a slingshot into destructible pig structures | Confirmed | Direct | High | P1 |
| `ABC-002` | Live collision can remove support and cascade further damage | Confirmed | Corroborated | High | P1, S1 |
| `ABC-003` | The level succeeds when all pigs are removed before the bird queue is exhausted | Confirmed | Corroborated | High | P1, S1 |

## Basic data

- Release / origin: Rovio released the original Angry Birds in 2009; the
  scoped modern reconstruction preserves classic gameplay.
- Platform or physical form: touch / pointer physics puzzle.
- Puzzle family: physics and object manipulation.
- Primary sources: **[P1]** [Rovio Classics: Angry Birds](https://www.angrybirds.com/games/rovio-classics-angry-birds/).
- Secondary sources: **[S1]** [Computational Complexity of Angry Birds](https://arxiv.org/abs/1812.07793).
- Claim IDs: `ABC-001`–`ABC-003`.

## Mechanical decomposition

### Action Genes

- `ACT-113` aims and releases the current bird from a fixed slingshot.
- Candidate genes: none. Parameters are angle and pull distance.
- Claim IDs: `ABC-001`.

### System Behaviour Genes

- `SYS-146` resolves ballistic collisions; `SYS-147` propagates material damage
  into support loss and collapse.
- Resolution order: release; flight; impact; damage; structural fall; settle.
- Claim IDs: `ABC-002`.

### Constraint Genes

- `CON-164` limits the attempt to the displayed ordered bird queue.
- Scarce strategic resources: remaining launches.
- Claim IDs: `ABC-003`.

### Information Genes

- `INF-001` exposes birds, pigs, materials and current structure.
- Candidate genes: none.
- Claim IDs: `ABC-001`, `ABC-002`.

### Objective Genes

- `OBJ-029` removes every pig; `OBJ-002` records destruction efficiency.
- Success, evaluation and failure: all pigs cleared, or queue exhausted first.
- Claim IDs: `ABC-003`.

### Time Genes

- `TIM-003` permits no discrete interruption of live flight and collapse.
- Candidate genes: none.
- Claim IDs: `ABC-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Bird waits in slingshot | Pull down-left and release | Bird flies up-right under gravity | fixed-launch aim | `ABC-001` |
| Bird hits a weak glass support | Allow physics to settle | Glass breaks and supported block falls | damage cascade | `ABC-002` |
| Last pig remains and no birds remain | Wait for settle | Attempt fails after live bodies settle | finite stock | `ABC-003` |

## Strategic and experiential structure

- Local decision: select an impact point and launch energy.
- Medium-term planning: exploit weak supports rather than direct hits.
- Long-term structure: reserve enough birds to clear every pig.
- Common heuristics: strike load-bearing glass or wood.
- Failure attribution: aim is visible, but nonlinear collision chains can surprise.
- Player-trust factors: material differences must remain legible.
- Claim IDs: `ABC-001`–`ABC-003`.

## Replay and variation

- What changes between sessions: chosen trajectory and resulting collision chain.
- Randomness or procedural generation: none claimed in the scoped level.
- Multiple viable strategies: often yes.
- Typical replay motive: clear with fewer birds or improve score.
- Claim IDs: `ABC-003`.

## Adjacent systems and history

- Direct predecessors: artillery and castle-destruction games.
- Variants: later bird powers and power-ups are excluded.
- Similar games: Cut the Rope and Peggle share live physics.
- Important differences: the player launches a finite destructive body into a
  damage-bearing support structure.
- Claim IDs: `ABC-002`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-113` | angle; strength |
| System Behaviour | `SYS-146`, `SYS-147` | materials; damage |
| Constraint | `CON-164` | queue size and order |
| Information | `INF-001` | material readability |
| Objective | `OBJ-002`, `OBJ-029` | score; pig set |
| Time | `TIM-003` | physics rate |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `109` (`GAME-0001`–`GAME-0109`).
- Exact genome matches: none.
- Tied near matches: `GAME-0021` — Cut the Rope (`3 / 14 = 0.214286`).
- Supported combination subsets: `COMB-0109`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0021`.

## Taxonomy impact

- Registry changes: four Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: fixed-launch ballistics.

## Negative results

- `none`.
