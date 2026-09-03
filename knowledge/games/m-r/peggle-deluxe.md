---
game_id: GAME-0114
slug: peggle-deluxe
game_title: Peggle Deluxe
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0113
gene_ids:
  action:
    - ACT-113
  system:
    - SYS-146
  constraint:
    - CON-164
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-007
  time:
    - TIM-003
---

# Game: Peggle Deluxe

## Analysis scope

- Version / ruleset: Peggle Deluxe Adventure mode, bounded to an ordinary level
  with blue and orange pegs, a finite ball stock, fixed top launcher, walls and
  moving bottom bucket; character powers and green / purple pegs are excluded.
- Included: aim, launch, gravity, ricochet, peg hits, end-of-shot removal,
  orange-target clearance, free-ball bucket catch and score.
- Excluded: Peggle Masters, powers, challenge modes, multiplayer, achievements
  and platform-specific aim controls.
- Direct-play status: not conducted. EA defines aimed peg clearing and orange
  target completion; the preserved PopCap manual corroborates the bounded loop.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PEG-001` | A fixed launcher fires one aimed ball through a field of pegs | Confirmed | Direct | High | P1 |
| `PEG-002` | The ball follows live gravity and collision while contacted pegs become cleared targets | Confirmed | Corroborated | High | P1, P2 |
| `PEG-003` | All orange pegs must be cleared before the recoverable finite ball stock ends | Confirmed | Corroborated | High | P1, P2 |

## Basic data

- Release / origin: PopCap released Peggle in 2007.
- Platform or physical form: pointer-controlled pachinko-like puzzle.
- Puzzle family: physics and object manipulation; target clearance.
- Primary sources: **[P1]** [EA Peggle catalogue](https://www.ea.com/en-ca/games/peggle);
  **[P2]** [PopCap manual PDF](https://static-www.ec.popcap.com/support.popcap.com/sites/support.popcap.com/files/0107_PEGDS_Manual_011609.pdf).
- Claim IDs: `PEG-001`–`PEG-003`.

## Mechanical decomposition

### Action Genes

- `ACT-113` aims and releases one ball from the fixed top launcher.
- Candidate genes: none.
- Claim IDs: `PEG-001`.

### System Behaviour Genes

- `SYS-146` resolves gravity, wall / peg impacts and the moving bucket.
- Resolution order: launch; collisions and scoring; fall / catch; clear hit pegs.
- Claim IDs: `PEG-002`.

### Constraint Genes

- `CON-164` consumes one ball per shot, with bucket catch restoring one.
- Scarce strategic resources: remaining balls.
- Claim IDs: `PEG-003`.

### Information Genes

- `INF-001` shows peg positions, colours, bucket and ball count.
- Candidate genes: none.
- Claim IDs: `PEG-001`.

### Objective Genes

- `OBJ-007` clears every orange peg; `OBJ-002` rewards additional contacts.
- Success, evaluation and failure: orange set empty, or balls exhausted first.
- Claim IDs: `PEG-003`.

### Time Genes

- `TIM-003` advances the ball and bucket continuously during a shot.
- Candidate genes: none.
- Claim IDs: `PEG-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Aim line crosses one orange peg | Release | Ball contacts peg and continues under collision | shared ballistic gene | `PEG-001`, `PEG-002` |
| Ball falls into moving bucket | Wait | Shot ends and one ball is returned | recoverable finite stock | `PEG-003` |
| Last orange peg is hit | Let shot complete | Level succeeds after live resolution | target-clear objective | `PEG-003` |

## Strategic and experiential structure

- Local decision: choose angle to intersect several targets.
- Medium-term planning: preserve balls through bucket catches.
- Long-term structure: remove every orange peg.
- Common heuristics: bank shots through dense target clusters.
- Failure attribution: aim is visible; multi-impact bounces are hard to predict.
- Player-trust factors: peg state and ball stock are explicit.
- Claim IDs: `PEG-002`, `PEG-003`.

## Replay and variation

- What changes between sessions: shot trajectory and collision path.
- Randomness or procedural generation: none claimed in the fixed level.
- Multiple viable strategies: yes.
- Typical replay motive: clear efficiently or improve score.
- Claim IDs: `PEG-003`.

## Adjacent systems and history

- Direct predecessors: pachinko and bagatelle.
- Variants: character powers are excluded.
- Similar games: Angry Birds Classic and Golf Peaks.
- Important differences: hit pegs are targets, not load-bearing destructible bodies.
- Claim IDs: `PEG-002`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-113` | launch angle |
| System Behaviour | `SYS-146` | peg and bucket collision |
| Constraint | `CON-164` | ball count; catch recovery |
| Information | `INF-001` | aim guide |
| Objective | `OBJ-002`, `OBJ-007` | orange roster; score |
| Time | `TIM-003` | bucket and ball rate |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `113` (`GAME-0001`–`GAME-0113`).
- Exact genome matches: none.
- Tied near matches: `GAME-0110` — Angry Birds Classic (`6 / 9 = 0.666667`).
- Supported combination subsets: `COMB-0113`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0110`.

## Taxonomy impact

- Registry changes: `ACT-113`, `SYS-146`, `CON-164` gain a second carrier.
- Taxonomy-change record: none.
- Candidate terms affected: fixed-launch ballistics.

## Negative results

- `none`.
