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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-113; SYS-146; CON-164; INF-001; OBJ-002,OBJ-007; TIM-003`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0110` — Angry Birds Classic at `6 / 9 = 0.666667`.
- Supported combination subsets: `COMB-0113`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `2 / 19 = 0.105263`; `GAME-0002`: `1 / 13 = 0.076923`; `GAME-0003`: `0 / 16 = 0.000000`; `GAME-0004`: `3 / 19 = 0.157895`.
- `GAME-0005`: `1 / 13 = 0.076923`; `GAME-0006`: `1 / 15 = 0.066667`; `GAME-0007`: `1 / 14 = 0.071429`; `GAME-0008`: `1 / 13 = 0.076923`.
- `GAME-0009`: `2 / 21 = 0.095238`; `GAME-0010`: `1 / 15 = 0.066667`; `GAME-0011`: `1 / 19 = 0.052632`; `GAME-0012`: `1 / 15 = 0.066667`.
- `GAME-0013`: `1 / 19 = 0.052632`; `GAME-0014`: `1 / 21 = 0.047619`; `GAME-0015`: `2 / 19 = 0.105263`; `GAME-0016`: `3 / 19 = 0.157895`.
- `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `3 / 23 = 0.130435`; `GAME-0019`: `1 / 16 = 0.062500`; `GAME-0020`: `2 / 19 = 0.105263`.
- `GAME-0021`: `3 / 13 = 0.230769`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `0 / 17 = 0.000000`; `GAME-0024`: `1 / 18 = 0.055556`.
- `GAME-0025`: `2 / 16 = 0.125000`; `GAME-0026`: `2 / 17 = 0.117647`; `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`.
- `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `2 / 19 = 0.105263`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `1 / 17 = 0.058824`.
- `GAME-0033`: `2 / 18 = 0.111111`; `GAME-0034`: `2 / 19 = 0.105263`; `GAME-0035`: `2 / 23 = 0.086957`; `GAME-0036`: `1 / 18 = 0.055556`.
- `GAME-0037`: `1 / 15 = 0.066667`; `GAME-0038`: `2 / 21 = 0.095238`; `GAME-0039`: `1 / 15 = 0.066667`; `GAME-0040`: `1 / 14 = 0.071429`.
- `GAME-0041`: `2 / 16 = 0.125000`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `1 / 20 = 0.050000`; `GAME-0044`: `1 / 16 = 0.062500`.
- `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `1 / 16 = 0.062500`; `GAME-0047`: `1 / 20 = 0.050000`; `GAME-0048`: `1 / 20 = 0.050000`.
- `GAME-0049`: `1 / 15 = 0.066667`; `GAME-0050`: `1 / 21 = 0.047619`; `GAME-0051`: `3 / 20 = 0.150000`; `GAME-0052`: `2 / 15 = 0.133333`.
- `GAME-0053`: `1 / 15 = 0.066667`; `GAME-0054`: `1 / 17 = 0.058824`; `GAME-0055`: `1 / 16 = 0.062500`; `GAME-0056`: `1 / 14 = 0.071429`.
- `GAME-0057`: `1 / 14 = 0.071429`; `GAME-0058`: `1 / 15 = 0.066667`; `GAME-0059`: `1 / 13 = 0.076923`; `GAME-0060`: `2 / 12 = 0.166667`.
- `GAME-0061`: `1 / 16 = 0.062500`; `GAME-0062`: `1 / 14 = 0.071429`; `GAME-0063`: `1 / 13 = 0.076923`; `GAME-0064`: `1 / 11 = 0.090909`.
- `GAME-0065`: `0 / 14 = 0.000000`; `GAME-0066`: `0 / 17 = 0.000000`; `GAME-0067`: `1 / 14 = 0.071429`; `GAME-0068`: `0 / 15 = 0.000000`.
- `GAME-0069`: `1 / 14 = 0.071429`; `GAME-0070`: `2 / 13 = 0.153846`; `GAME-0071`: `1 / 13 = 0.076923`; `GAME-0072`: `1 / 14 = 0.071429`.
- `GAME-0073`: `1 / 13 = 0.076923`; `GAME-0074`: `1 / 15 = 0.066667`; `GAME-0075`: `1 / 15 = 0.066667`; `GAME-0076`: `1 / 13 = 0.076923`.
- `GAME-0077`: `1 / 13 = 0.076923`; `GAME-0078`: `1 / 13 = 0.076923`; `GAME-0079`: `1 / 13 = 0.076923`; `GAME-0080`: `1 / 13 = 0.076923`.
- `GAME-0081`: `1 / 14 = 0.071429`; `GAME-0082`: `1 / 14 = 0.071429`; `GAME-0083`: `1 / 14 = 0.071429`; `GAME-0084`: `1 / 16 = 0.062500`.
- `GAME-0085`: `0 / 18 = 0.000000`; `GAME-0086`: `1 / 19 = 0.052632`; `GAME-0087`: `2 / 15 = 0.133333`; `GAME-0088`: `1 / 15 = 0.066667`.
- `GAME-0089`: `1 / 15 = 0.066667`; `GAME-0090`: `1 / 21 = 0.047619`; `GAME-0091`: `2 / 14 = 0.142857`; `GAME-0092`: `2 / 15 = 0.133333`.
- `GAME-0093`: `1 / 15 = 0.066667`; `GAME-0094`: `2 / 15 = 0.133333`; `GAME-0095`: `2 / 17 = 0.117647`; `GAME-0096`: `2 / 15 = 0.133333`.
- `GAME-0097`: `2 / 13 = 0.153846`; `GAME-0098`: `2 / 12 = 0.166667`; `GAME-0099`: `2 / 13 = 0.153846`; `GAME-0100`: `1 / 17 = 0.058824`.
- `GAME-0101`: `0 / 17 = 0.000000`; `GAME-0102`: `0 / 14 = 0.000000`; `GAME-0103`: `1 / 15 = 0.066667`; `GAME-0104`: `1 / 15 = 0.066667`.
- `GAME-0105`: `1 / 16 = 0.062500`; `GAME-0106`: `0 / 14 = 0.000000`; `GAME-0107`: `1 / 14 = 0.071429`; `GAME-0108`: `1 / 16 = 0.062500`.
- `GAME-0109`: `2 / 21 = 0.095238`; `GAME-0110`: `6 / 9 = 0.666667`; `GAME-0111`: `1 / 13 = 0.076923`; `GAME-0112`: `2 / 13 = 0.153846`.
- `GAME-0113`: `2 / 19 = 0.105263`.

## Taxonomy impact

- Registry changes: `ACT-113`, `SYS-146`, `CON-164` gain a second carrier.
- Taxonomy-change record: none.
- Candidate terms affected: fixed-launch ballistics.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Pattern | Corroborated | High] Fixed-launch ballistics and finite projectile
  stock transfer across destructive and non-destructive puzzle families.

## Нові гени

- [Observation | Corroborated | High] Нових генів немає.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0113`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does bucket motion need its own reusable timing gene after another carrier?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Unpacking.
- Optimisation criterion: switch from trajectories to semantic spatial placement.
- Expected information gain: many valid placements under room affordances.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It tests placement validity without one exact target layout.
