---
game_id: GAME-0010
slug: water-sort
game_title: Water Sort
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0010
gene_ids:
  action:
    - ACT-013
  system:
    - SYS-015
  constraint:
    - CON-001
    - CON-014
    - CON-021
    - CON-022
  information:
    - INF-001
  objective:
    - OBJ-008
  time:
    - TIM-001
---

# Game: Water Sort

## Analysis scope

- Version / ruleset: the formal unit-volume Water Sort puzzle defined by Ito et
  al., with equal-capacity tubes, initially full coloured tubes and additional
  empty tubes.
- Included: visible ordered colour layers; source and destination selection;
  access to the contiguous top colour segment; destination capacity; pouring
  only into an empty tube or onto the same exposed colour; automatic maximal
  transfer, truncated when only part fits; completion when every occupied tube
  is full and monochromatic.
- Excluded: hidden colours, unequal tube capacities, locked completed tubes,
  timers, move limits, undo, restart, hints, shuffling, extra tubes obtained by
  ads or purchases, procedural level selection and metagame rewards.
- Direct-play status: not conducted. The mechanical model is based primarily on
  a peer-reviewed formalisation and corroborated by two public implementations.
  No specific commercial app, level numbering or guarantee of solvability is
  assumed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WAT-001` | Each tube is a fixed-capacity stack of visible coloured unit volumes | Confirmed | Corroborated | High | A1, P1, P2 |
| `WAT-002` | Only the contiguous same-colour segment at the source top is transferable | Confirmed | Corroborated | High | A1, P1 |
| `WAT-003` | A destination accepts a pour only when empty or topped by the same colour and when it has free capacity | Confirmed | Corroborated | High | A1, P1, P2 |
| `WAT-004` | The transferred amount is the largest top same-colour quantity that fits in the destination | Confirmed | Corroborated | High | A1, P1 |
| `WAT-005` | Completion requires every occupied tube to be full and monochromatic, with spare tubes empty | Confirmed | Corroborated | High | A1, P1 |
| `WAT-006` | Empty tubes are temporary strategic workspaces rather than one-element buffers | Observation | Corroborated | High | WAT-001–WAT-005 |
| `WAT-007` | The scoped transition system is deterministic and contains no in-play random event | Observation | Corroborated | High | A1, P1 |
| `WAT-008` | Some formally valid starting instances are unsolvable, so solvability is not guaranteed by the core rules | Confirmed | Direct | High | A1 |
| `WAT-009` | Generalised complexity results do not establish the difficulty of every finite app level | Confirmed | Corroborated | High | A1, A2 |
| `WAT-010` | Source selection and system-determined maximal quantity fit the six-type model without a taxonomy change | Observation | Corroborated | Medium | WAT-001–WAT-009 |

## Basic data

- Release / origin: Water Sort is analysed as a mobile-puzzle family rather
  than attributed to one developer. The academic literature records that Water
  Sort and Ball Sort apps had become popular before their 2022 formal study.
- Platform or physical form: commonly digital, but representable with discrete
  coloured units and stack-like containers.
- Puzzle family: deterministic LIFO colour segregation through bounded vessels.
- Primary academic source:
  - **[A1]** Takehiro Ito et al.,
    [“Sorting Balls and Water: Equivalence and Computational Complexity”](https://arxiv.org/abs/2202.09495),
    later published in *Theoretical Computer Science* 978, 2023. It defines
    capacity, LIFO access, empty-or-matching destinations, partial maximal pours
    and full monochromatic completion.
- Corroborating sources:
  - **[P1]** [Water Sort Puzzle rules](https://play-watersort.com/), documenting
    top-colour transfer, four-unit tubes, same-colour / empty destinations and
    monochromatic completion. Its UI conveniences are excluded.
  - **[P2]** [WaterSort.com](https://watersort.com/), corroborating same-colour
    compatibility and sufficient destination space.
- Complexity corroboration:
  - **[A2]** the peer-reviewed
    [journal record](https://doi.org/10.1016/j.tcs.2023.114158), reporting
    equivalence of Water Sort and Ball Sort solvability and NP-completeness of
    the generalised problem.
- Claim IDs: `WAT-001`–`WAT-010`.

## Mechanical decomposition

### Action Genes

- `ACT-013` — select source and destination containers. The player specifies
  which non-empty tube should pour and which distinct tube should receive.
- The action does not include quantity selection. Once both tubes are chosen,
  the rules determine whether a transfer occurs and exactly how many unit
  volumes move.
- Undo, restart and acquiring another tube are interface or metagame commands
  outside the scoped action set.
- Claim IDs: `WAT-002`–`WAT-004`.

### System Behaviour Genes

- `SYS-015` — maximal compatible top-segment transfer. If the destination is
  legal, the system moves `min(source top-run length, destination free slots)`
  unit volumes as one resolution.
- Same-colour units become one visible contiguous layer after pouring, but
  nothing is created, removed or numerically transformed; `SYS-002` merge is
  therefore absent.
- No gravity, refill, cascade or random outcome occurs after the pour.
- Claim IDs: `WAT-004`, `WAT-007`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The tube set exposes a fixed number of
  unit slots throughout the level.
- `CON-014` — exposed-only stack access. Only the contiguous top colour segment
  is available; a deeper colour requires removal of every segment above it.
- `CON-021` — per-container occupancy capacity. No tube may exceed its fixed
  number of unit slots; free destination margin can truncate a pour.
- `CON-022` — empty-or-matching-top destination compatibility. Capacity alone
  is insufficient when the exposed destination colour differs.
- `CON-015` is absent. An empty Water Sort tube can hold several unit volumes
  and preserve layered order, unlike one single-card FreeCell buffer.
- Tube capacity, number of colours, number of filled tubes and number of empty
  tubes are parameters. The number of empties materially affects solvability
  but does not change the move rule's boundary.
- Claim IDs: `WAT-001`–`WAT-004`, `WAT-006`, `WAT-008`.

### Information Genes

- `INF-001` — fully visible current state. Every tube's ordered layers,
  remaining margin and empty status are inspectable before each selection.
- No colour is hidden below an opaque boundary in the scoped rules. Deeper
  layers are inaccessible but visible, so `INF-003` is absent.
- The result is deterministic once source and destination are chosen; there is
  no future preview or random event.
- Claim IDs: `WAT-001`, `WAT-007`.

### Objective Genes

- `OBJ-008` — segregate types into homogeneous containers. Every occupied tube
  must be full of a single colour and all spare tubes must be empty.
- Tube-to-colour assignment is interchangeable: blue need not finish in a
  particular indexed tube. This is a property-based sorting target rather than
  a separately specified arrangement, so `OBJ-004` is absent.
- The total volume of each colour is conserved; the objective rearranges the
  initial units rather than creating or deleting them.
- Claim IDs: `WAT-005`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One source-destination
  command is followed by the complete maximal pour before another selection is
  accepted.
- The player may pause between resolved pours, but each move contains automatic
  quantity resolution, distinguishing it from `TIM-002`.
- Optional move counting for efficiency is not a terminal move budget in the
  scoped formal rules.
- Claim IDs: `WAT-004`, `WAT-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Source top is two blue units; destination empty with four free slots | Select source then destination | Both blue units move | Maximal top-segment transfer | `WAT-004` |
| Source top is three blue units; destination topped blue with one free slot | Select source then destination | One blue unit moves; two remain | Capacity truncates quantity | `WAT-004` |
| Source top is blue; destination topped red with two free slots | Attempt pour | No state change | Colour compatibility is independent of margin | `WAT-003` |
| Source top is blue; destination full and topped blue | Attempt pour | No state change | Matching colour does not override capacity | `WAT-003` |
| Blue lies below exposed red | Select that source | Only the red top segment can leave | Visible depth remains inaccessible | `WAT-002` |
| Every non-empty tube is full and monochromatic | Complete the last legal pour | Objective is satisfied under any tube-colour permutation | Homogeneous-container target | `WAT-005` |

## Strategic and experiential structure

- Local decision: choose a legal destination and predict how the forced maximal
  quantity changes both exposed colours and available margins.
- Medium-term planning: expose buried segments, merge compatible top runs and
  avoid occupying empty vessels with colours that cannot soon be consolidated.
- Long-term structure: allocate temporary tube capacity so each colour can be
  gathered without sealing access to another colour.
- Common heuristics: preserve at least one flexible empty tube; prefer pours
  that remove an entire source top run; avoid splitting a consolidated run when
  another compatible destination exists; reason about the next colour exposed
  after each maximal pour.
- Failure attribution: transitions are deterministic and visible, but an early
  legal pour can consume the only usable margin and leave no path to segregation.
- Player-trust factors: deterministic quantity and visible layers make each
  result predictable. Implementations that add hidden layers or locked tubes
  would require separate genes and disclosure.
- Claim IDs: `WAT-006`–`WAT-008`.

## Replay and variation

- What changes between instances: initial layer order, colour count, tube count,
  capacity and number of empty tubes.
- Randomness or procedural generation: none within the scoped instance.
- Multiple viable strategies: several pour sequences may sort the same
  instance; symmetry under tube and colour renaming creates equivalent paths.
- Typical replay motive: recover from an unsortable reached state or minimise
  the number of pours.
- Claim IDs: `WAT-007`–`WAT-009`.

## Adjacent systems and history

- Ito et al. prove Water Sort and Ball Sort equivalent with respect to
  solvability, even though a Water Sort move transfers a maximal same-colour
  top segment while Ball Sort moves one ball at a time.
- That equivalence does not make their action granularity identical for this
  atlas; Ball Sort needs its own decomposition if input and move counting are
  compared.
- Classical water-jug puzzles transfer undifferentiated volumes to measure
  quantities. They do not share Water Sort's coloured LIFO layers or
  same-colour destination rule.
- Complexity caveat: NP-completeness applies to scalable formal instances and
  does not establish the difficulty of every finite mobile level.
- Claim IDs: `WAT-008`, `WAT-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-013` | source and destination selection |
| System Behaviour | `SYS-015` | maximal quantity and unit granularity |
| Constraint | `CON-001`, `CON-014`, `CON-021`, `CON-022` | tube capacity and empty-tube count |
| Information | `INF-001` | all layers visible |
| Objective | `OBJ-008` | tube-colour permutation equivalence |
| Time | `TIM-001` | one command then resolved pour |

Canonical signature:

`ACT-013; SYS-015; CON-001,CON-014,CON-021,CON-022; INF-001; OBJ-008; TIM-001`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0009`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0009`.
- Exact genome matches: none.
- Shared with `GAME-0001`: `CON-001`, `INF-001`, `TIM-001`; intersection `3`,
  union `20`, `3 / 20 = 0.150000`.
- Shared with `GAME-0002`: `CON-001`, `INF-001`; intersection `2`, union `14`,
  `2 / 14 = 0.142857`.
- Shared with `GAME-0003`: `CON-001`, `TIM-001`; intersection `2`, union `16`,
  `2 / 16 = 0.125000`.
- Shared with `GAME-0004`: `CON-001`, `INF-001`; intersection `2`, union `22`,
  `2 / 22 = 0.090909`.
- Shared with `GAME-0005`: `CON-001`, `INF-001`; intersection `2`, union `14`,
  `2 / 14 = 0.142857`.
- Shared with `GAME-0006`: `CON-001`, `INF-001`; intersection `2`, union `16`,
  `2 / 16 = 0.125000`.
- Shared with `GAME-0007`: `CON-014`, `INF-001`; intersection `2`, union `15`,
  `2 / 15 = 0.133333`.
- Shared with `GAME-0008`: `CON-001`, `INF-001`; intersection `2`, union `14`,
  `2 / 14 = 0.142857`.
- Shared with `GAME-0009`: `CON-001`, `INF-001`, `TIM-001`; intersection `3`,
  union `22`, `3 / 22 = 0.136364`.
- Near match: `GAME-0001`, the unique positive maximum among non-exact indexed
  games.
- Supported existing combination subsets: none. Every indexed combination
  requires at least one absent action, behaviour, constraint or objective.
- New combination: `COMB-0010`, whose seven genes are a proper subset of this
  nine-gene genome.
- Scan date: 2026-08-11.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` — 2048 | `CON-001`, `INF-001`, `TIM-001` | Both resolve a discrete command on a fixed visible board; 2048 moves every tile, merges and spawns randomly, while Water Sort deterministically transfers one maximal compatible top segment | Near, `0.150000` |
| `GAME-0002` — Rubik's Cube | `CON-001`, `INF-001` | Cube turns are reversible permutations without containers; Water Sort has LIFO access and capacity-bounded compatibility | Non-near, `0.142857` |
| `GAME-0003` — Minesweeper | `CON-001`, `TIM-001` | Minesweeper reveals concealed hazards; Water Sort shows all layers and rearranges conserved units | Non-near, `0.125000` |
| `GAME-0004` — Tetris | `CON-001`, `INF-001` | Tetris advances in real time with random successors; Water Sort waits and resolves deterministic commanded pours | Non-near, `0.090909` |
| `GAME-0005` — Sudoku | `CON-001`, `INF-001` | Sudoku assigns new symbolic values under global uniqueness; Water Sort transports existing typed units through vessels | Non-near, `0.142857` |
| `GAME-0006` — Sokoban | `CON-001`, `INF-001` | Sokoban requires agent access behind one object; Water Sort requires top-segment access and destination compatibility | Non-near, `0.125000` |
| `GAME-0007` — FreeCell | `CON-014`, `INF-001` | Both expose only stack ends and depend on workspace; FreeCell moves one card into ordered zones, while Water Sort automatically moves the maximal compatible segment into multi-unit vessels | Non-near, `0.133333` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001` | Nonogram assigns binary states from clues; Water Sort rearranges conserved visible layers | Non-near, `0.142857` |
| `GAME-0009` — Royal Match | `CON-001`, `INF-001`, `TIM-001` | Royal Match removes, randomly refills and cascades under a move budget; Water Sort conserves every unit and has one deterministic resolution | Non-near, `0.136364` |

- New genes: `ACT-013`, `SYS-015`, `CON-021`, `CON-022`, `OBJ-008`.
- Classification result: `New gene`.
- Reused genes: `CON-001`, `CON-014`, `INF-001`, `TIM-001`.
- Evidence and reasoning: selecting containers and resolving quantity are
  independently defined Action and System roles. Top access generalises across
  FreeCell and Water Sort, while multi-unit capacity and colour acceptance are
  distinct from a one-card free cell.

## Taxonomy impact

- Registry changes: five bounded genes added and four reused.
- Taxonomy-change record: none. The post-checkpoint Action / System test cleanly
  separates destination choice from forced maximal transfer quantity.
- Candidate terms affected: pour, layered capacity, empty buffers, access order,
  compatibility and homogeneous sorting now have bounded mappings.
- Empty-tube count remains a parameter despite its strategic importance because
  it changes state-space freedom without changing transition legality.
- Claim IDs: `WAT-010`.

## Negative results

Water Sort does not reuse FreeCell's `CON-015`: a tube is a multi-unit ordered
container, not a one-element unordered buffer. Same-colour contact does not
instantiate `SYS-002` because no units combine into a transformed output.
Optional move counting is not `CON-020` unless exhaustion terminates the level.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Transfer quantity is forced by the source
  top run and destination margin (`WAT-002`–`WAT-004`).
- [Observation | Corroborated | High] Empty tubes provide layered workspace,
  not FreeCell-style single-element storage (`WAT-006`).
- [Confirmed | Direct | High] The formal rule family admits unsolvable starting
  instances (`WAT-008`).

## Нові гени

- [Observation | Corroborated | High] `ACT-013`, `SYS-015`, `CON-021`,
  `CON-022` and `OBJ-008`.
- [Observation | Corroborated | High] `CON-001`, `CON-014`, `INF-001` and
  `TIM-001` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0010` — top-access homogeneous
  sorting through bounded vessels.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Container choice
  and automatic maximal quantity follow the checkpoint boundary tests.

## Нові питання

- TODO: compare Ball Sort to test whether action granularity changes the genome
  despite solvability equivalence.
- TODO: test `CON-021` with unequal-capacity vessels and classical measuring
  objectives.
- TODO: find a second non-card family for `CON-014` with direct single-element
  rather than segment transfer.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0011` — Chess.
- Optimisation criterion: introduce an adversarial second decision-maker after
  ten single-agent systems.
- Expected information gain: test alternating turns, opponent-controlled state
  changes, capture, check-constrained legality, checkmate and draw boundaries.
- Backlog impact: Chess moves from the coverage pool to the immediate task;
  Water Sort leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Chess is mechanically distant from the entire
  current corpus and directly tests whether opponent actions belong in Action,
  System Behaviour or a missing agency dimension without assuming a seventh
  gene type in advance.
