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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-113; SYS-146,SYS-147; CON-164; INF-001; OBJ-002,OBJ-029; TIM-003`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0021` — Cut the Rope at `3 / 14 = 0.214286`.
- Supported combination subsets: `COMB-0109`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `2 / 20 = 0.100000`; `GAME-0002`: `1 / 14 = 0.071429`; `GAME-0003`: `0 / 17 = 0.000000`; `GAME-0004`: `3 / 20 = 0.150000`.
- `GAME-0005`: `1 / 14 = 0.071429`; `GAME-0006`: `1 / 16 = 0.062500`; `GAME-0007`: `1 / 15 = 0.066667`; `GAME-0008`: `1 / 14 = 0.071429`.
- `GAME-0009`: `1 / 23 = 0.043478`; `GAME-0010`: `1 / 16 = 0.062500`; `GAME-0011`: `1 / 20 = 0.050000`; `GAME-0012`: `1 / 16 = 0.062500`.
- `GAME-0013`: `1 / 20 = 0.050000`; `GAME-0014`: `1 / 22 = 0.045455`; `GAME-0015`: `2 / 20 = 0.100000`; `GAME-0016`: `3 / 20 = 0.150000`.
- `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `3 / 24 = 0.125000`; `GAME-0019`: `1 / 17 = 0.058824`; `GAME-0020`: `2 / 20 = 0.100000`.
- `GAME-0021`: `3 / 14 = 0.214286`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `0 / 18 = 0.000000`; `GAME-0024`: `1 / 19 = 0.052632`.
- `GAME-0025`: `2 / 17 = 0.117647`; `GAME-0026`: `2 / 18 = 0.111111`; `GAME-0027`: `2 / 18 = 0.111111`; `GAME-0028`: `2 / 23 = 0.086957`.
- `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `2 / 20 = 0.100000`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `1 / 18 = 0.055556`.
- `GAME-0033`: `2 / 19 = 0.105263`; `GAME-0034`: `2 / 20 = 0.100000`; `GAME-0035`: `2 / 24 = 0.083333`; `GAME-0036`: `1 / 19 = 0.052632`.
- `GAME-0037`: `1 / 16 = 0.062500`; `GAME-0038`: `2 / 22 = 0.090909`; `GAME-0039`: `1 / 16 = 0.062500`; `GAME-0040`: `1 / 15 = 0.066667`.
- `GAME-0041`: `2 / 17 = 0.117647`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `1 / 21 = 0.047619`; `GAME-0044`: `1 / 17 = 0.058824`.
- `GAME-0045`: `1 / 21 = 0.047619`; `GAME-0046`: `1 / 17 = 0.058824`; `GAME-0047`: `2 / 20 = 0.100000`; `GAME-0048`: `2 / 20 = 0.100000`.
- `GAME-0049`: `1 / 16 = 0.062500`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `3 / 21 = 0.142857`; `GAME-0052`: `2 / 16 = 0.125000`.
- `GAME-0053`: `1 / 16 = 0.062500`; `GAME-0054`: `1 / 18 = 0.055556`; `GAME-0055`: `1 / 17 = 0.058824`; `GAME-0056`: `1 / 15 = 0.066667`.
- `GAME-0057`: `1 / 15 = 0.066667`; `GAME-0058`: `1 / 16 = 0.062500`; `GAME-0059`: `1 / 14 = 0.071429`; `GAME-0060`: `1 / 14 = 0.071429`.
- `GAME-0061`: `1 / 17 = 0.058824`; `GAME-0062`: `1 / 15 = 0.066667`; `GAME-0063`: `1 / 14 = 0.071429`; `GAME-0064`: `1 / 12 = 0.083333`.
- `GAME-0065`: `0 / 15 = 0.000000`; `GAME-0066`: `0 / 18 = 0.000000`; `GAME-0067`: `1 / 15 = 0.066667`; `GAME-0068`: `0 / 16 = 0.000000`.
- `GAME-0069`: `1 / 15 = 0.066667`; `GAME-0070`: `1 / 15 = 0.066667`; `GAME-0071`: `1 / 14 = 0.071429`; `GAME-0072`: `1 / 15 = 0.066667`.
- `GAME-0073`: `1 / 14 = 0.071429`; `GAME-0074`: `1 / 16 = 0.062500`; `GAME-0075`: `1 / 16 = 0.062500`; `GAME-0076`: `1 / 14 = 0.071429`.
- `GAME-0077`: `1 / 14 = 0.071429`; `GAME-0078`: `1 / 14 = 0.071429`; `GAME-0079`: `1 / 14 = 0.071429`; `GAME-0080`: `1 / 14 = 0.071429`.
- `GAME-0081`: `1 / 15 = 0.066667`; `GAME-0082`: `1 / 15 = 0.066667`; `GAME-0083`: `1 / 15 = 0.066667`; `GAME-0084`: `1 / 17 = 0.058824`.
- `GAME-0085`: `0 / 19 = 0.000000`; `GAME-0086`: `1 / 20 = 0.050000`; `GAME-0087`: `2 / 16 = 0.125000`; `GAME-0088`: `1 / 16 = 0.062500`.
- `GAME-0089`: `1 / 16 = 0.062500`; `GAME-0090`: `1 / 22 = 0.045455`; `GAME-0091`: `2 / 15 = 0.133333`; `GAME-0092`: `2 / 16 = 0.125000`.
- `GAME-0093`: `1 / 16 = 0.062500`; `GAME-0094`: `2 / 16 = 0.125000`; `GAME-0095`: `2 / 18 = 0.111111`; `GAME-0096`: `2 / 16 = 0.125000`.
- `GAME-0097`: `2 / 14 = 0.142857`; `GAME-0098`: `2 / 13 = 0.153846`; `GAME-0099`: `2 / 14 = 0.142857`; `GAME-0100`: `1 / 18 = 0.055556`.
- `GAME-0101`: `0 / 18 = 0.000000`; `GAME-0102`: `0 / 15 = 0.000000`; `GAME-0103`: `1 / 16 = 0.062500`; `GAME-0104`: `1 / 16 = 0.062500`.
- `GAME-0105`: `1 / 17 = 0.058824`; `GAME-0106`: `0 / 15 = 0.000000`; `GAME-0107`: `1 / 15 = 0.066667`; `GAME-0108`: `1 / 17 = 0.058824`.
- `GAME-0109`: `1 / 23 = 0.043478`.

## Taxonomy impact

- Registry changes: four Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: fixed-launch ballistics.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Support damage can multiply one launch into
  a cascading clearance event (`ABC-002`).

## Нові гени

- [Observation | Corroborated | High] `ACT-113`, `SYS-146`, `SYS-147`, `CON-164`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0109`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does post-release ability activation need a separate action boundary?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Myst.
- Optimisation criterion: move from live physics to authored knowledge routing.
- Expected information gain: mechanism dependency without inventory consumption.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] Myst tests a maximally different self-paced family.
