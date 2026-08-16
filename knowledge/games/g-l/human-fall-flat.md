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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008,ACT-048,ACT-114; SYS-036; CON-165; INF-001; OBJ-026; TIM-003`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0091` — Fez at `5 / 12 = 0.416667`.
- Supported combination subsets: `COMB-0111`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 21 = 0.047619`; `GAME-0002`: `1 / 14 = 0.071429`; `GAME-0003`: `0 / 17 = 0.000000`; `GAME-0004`: `2 / 21 = 0.095238`.
- `GAME-0005`: `1 / 14 = 0.071429`; `GAME-0006`: `2 / 15 = 0.133333`; `GAME-0007`: `1 / 15 = 0.066667`; `GAME-0008`: `1 / 14 = 0.071429`.
- `GAME-0009`: `1 / 23 = 0.043478`; `GAME-0010`: `1 / 16 = 0.062500`; `GAME-0011`: `1 / 20 = 0.050000`; `GAME-0012`: `1 / 16 = 0.062500`.
- `GAME-0013`: `1 / 20 = 0.050000`; `GAME-0014`: `1 / 22 = 0.045455`; `GAME-0015`: `1 / 21 = 0.047619`; `GAME-0016`: `2 / 21 = 0.095238`.
- `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `2 / 25 = 0.080000`; `GAME-0019`: `1 / 17 = 0.058824`; `GAME-0020`: `1 / 21 = 0.047619`.
- `GAME-0021`: `3 / 14 = 0.214286`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `0 / 18 = 0.000000`; `GAME-0024`: `1 / 19 = 0.052632`.
- `GAME-0025`: `2 / 17 = 0.117647`; `GAME-0026`: `3 / 17 = 0.176471`; `GAME-0027`: `2 / 18 = 0.111111`; `GAME-0028`: `2 / 23 = 0.086957`.
- `GAME-0029`: `3 / 17 = 0.176471`; `GAME-0030`: `3 / 19 = 0.157895`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `1 / 18 = 0.055556`.
- `GAME-0033`: `5 / 16 = 0.312500`; `GAME-0034`: `3 / 19 = 0.157895`; `GAME-0035`: `3 / 23 = 0.130435`; `GAME-0036`: `2 / 18 = 0.111111`.
- `GAME-0037`: `1 / 16 = 0.062500`; `GAME-0038`: `4 / 20 = 0.200000`; `GAME-0039`: `1 / 16 = 0.062500`; `GAME-0040`: `3 / 13 = 0.230769`.
- `GAME-0041`: `4 / 15 = 0.266667`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `2 / 16 = 0.125000`.
- `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `1 / 17 = 0.058824`; `GAME-0047`: `1 / 21 = 0.047619`; `GAME-0048`: `1 / 21 = 0.047619`.
- `GAME-0049`: `0 / 17 = 0.000000`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `2 / 22 = 0.090909`; `GAME-0052`: `1 / 17 = 0.058824`.
- `GAME-0053`: `2 / 15 = 0.133333`; `GAME-0054`: `3 / 16 = 0.187500`; `GAME-0055`: `3 / 15 = 0.200000`; `GAME-0056`: `1 / 15 = 0.066667`.
- `GAME-0057`: `1 / 15 = 0.066667`; `GAME-0058`: `1 / 16 = 0.062500`; `GAME-0059`: `1 / 14 = 0.071429`; `GAME-0060`: `1 / 14 = 0.071429`.
- `GAME-0061`: `1 / 17 = 0.058824`; `GAME-0062`: `1 / 15 = 0.066667`; `GAME-0063`: `1 / 14 = 0.071429`; `GAME-0064`: `1 / 12 = 0.083333`.
- `GAME-0065`: `0 / 15 = 0.000000`; `GAME-0066`: `0 / 18 = 0.000000`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `0 / 16 = 0.000000`.
- `GAME-0069`: `1 / 15 = 0.066667`; `GAME-0070`: `1 / 15 = 0.066667`; `GAME-0071`: `1 / 14 = 0.071429`; `GAME-0072`: `1 / 15 = 0.066667`.
- `GAME-0073`: `1 / 14 = 0.071429`; `GAME-0074`: `1 / 16 = 0.062500`; `GAME-0075`: `1 / 16 = 0.062500`; `GAME-0076`: `1 / 14 = 0.071429`.
- `GAME-0077`: `1 / 14 = 0.071429`; `GAME-0078`: `1 / 14 = 0.071429`; `GAME-0079`: `1 / 14 = 0.071429`; `GAME-0080`: `1 / 14 = 0.071429`.
- `GAME-0081`: `1 / 15 = 0.066667`; `GAME-0082`: `1 / 15 = 0.066667`; `GAME-0083`: `1 / 15 = 0.066667`; `GAME-0084`: `1 / 17 = 0.058824`.
- `GAME-0085`: `0 / 19 = 0.000000`; `GAME-0086`: `1 / 20 = 0.050000`; `GAME-0087`: `2 / 16 = 0.125000`; `GAME-0088`: `1 / 16 = 0.062500`.
- `GAME-0089`: `1 / 16 = 0.062500`; `GAME-0090`: `2 / 21 = 0.095238`; `GAME-0091`: `5 / 12 = 0.416667`; `GAME-0092`: `2 / 16 = 0.125000`.
- `GAME-0093`: `2 / 15 = 0.133333`; `GAME-0094`: `5 / 13 = 0.384615`; `GAME-0095`: `5 / 15 = 0.333333`; `GAME-0096`: `5 / 13 = 0.384615`.
- `GAME-0097`: `4 / 12 = 0.333333`; `GAME-0098`: `4 / 11 = 0.363636`; `GAME-0099`: `2 / 14 = 0.142857`; `GAME-0100`: `1 / 18 = 0.055556`.
- `GAME-0101`: `1 / 17 = 0.058824`; `GAME-0102`: `0 / 15 = 0.000000`; `GAME-0103`: `1 / 16 = 0.062500`; `GAME-0104`: `3 / 14 = 0.214286`.
- `GAME-0105`: `3 / 15 = 0.200000`; `GAME-0106`: `0 / 15 = 0.000000`; `GAME-0107`: `3 / 13 = 0.230769`; `GAME-0108`: `4 / 14 = 0.285714`.
- `GAME-0109`: `1 / 23 = 0.043478`; `GAME-0110`: `2 / 14 = 0.142857`; `GAME-0111`: `2 / 13 = 0.153846`.

## Taxonomy impact

- Registry changes: two Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: ragdoll climbing.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] The avatar's articulated grip is itself a
  manipulable physical constraint (`HFF-002`).

## Нові гени

- [Observation | Corroborated | High] `ACT-114`, `CON-165`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0111`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does two-player grip coordination justify a separate future combination?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Portal 2 cooperative campaign.
- Optimisation criterion: retain physics while adding explicit two-agent topology.
- Expected information gain: four owned portal channels.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It separates embodied cooperation from one ragdoll.
