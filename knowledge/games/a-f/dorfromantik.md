---
game_id: GAME-0020
slug: dorfromantik
game_title: Dorfromantik
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0020
gene_ids:
  action:
    - ACT-026
  system:
    - SYS-004
    - SYS-024
    - SYS-034
    - SYS-035
  constraint:
    - CON-039
    - CON-056
    - CON-058
    - CON-059
  information:
    - INF-001
    - INF-005
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-001
---

# Game: Dorfromantik

## Analysis scope

- Version / ruleset: one standard scored Classic-mode session in the full PC
  release, using ordinary procedurally supplied hex tiles.
- Included: the finite tile stack; current and visible successor tiles;
  rotation and adjacent placement; typed edge matching; connected landscape
  groups; ordinary number and closure quests; perfect placements; score and
  tile-stack rewards; termination when the stack is empty.
- Excluded: Creative, Quick, Hard, Custom and Monthly modes; unlock
  progression, challenges, achievements, leaderboards, explicit seed sharing,
  undo and presentation-only biome variation.
- Direct-play status: not conducted for this record. The creator's product
  description establishes the core loop; current rule details are
  corroborated by the maintained community rules reference.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DOR-001` | Classic play begins with a finite stack of procedurally supplied hex tiles and consumes its current tile one placement at a time | Confirmed | Direct | High | F1, F3 |
| `DOR-002` | The current tile may be rotated and placed in an available empty hex beside the existing landscape, while later tiles cannot be selected first | Confirmed | Corroborated | High | F3, S1 |
| `DOR-003` | The current state and a short exact successor horizon are visible before placement | Observation | Corroborated | High | S1 |
| `DOR-004` | Touching edge types are evaluated after placement and compatible edges join landscape groups | Confirmed | Corroborated | High | F3, S1, S2 |
| `DOR-005` | Placement quality, affected landscape groups and completed quests produce score automatically | Confirmed | Corroborated | High | F2, F3, S1, S4 |
| `DOR-006` | A placement whose six completed adjacencies all match is a perfect placement and rewards an additional tile | Confirmed | Corroborated | High | S1, S2, S4 |
| `DOR-007` | Completing an ordinary quest adds several tiles to the same stack that placements consume | Confirmed | Corroborated | High | F3, S1, S3 |
| `DOR-008` | The session ends when the tile stack is exhausted | Confirmed | Direct | High | F3 |
| `DOR-009` | Because tile rewards can offset consumption, the remaining stack is a replenishable action supply rather than a strictly decreasing move counter | Observation | Corroborated | High | DOR-001, DOR-006–DOR-008 |
| `DOR-010` | The landscape's addressable frontier grows with placement instead of consuming a predeclared fixed board | Observation | Corroborated | High | F1–F3 |
| `DOR-011` | The scoped objective is to maximise session score while preserving enough tile supply to continue placing | Observation | Corroborated | High | F2, F3, DOR-005–DOR-009 |
| `DOR-012` | Rotation and position are player choices; edge/group evaluation, scoring, rewards and queue advance resolve automatically before the next tile decision | Observation | Corroborated | High | DOR-002–DOR-007 |

## Basic data

- Release / origin: Toukana Interactive released Dorfromantik in Early Access
  on 2021-03-25 and as a full PC release on 2022-04-28.
- Platform or physical form: digital single-player tile-placement puzzle on PC
  and Nintendo Switch; this record concerns the PC videogame, not the later
  cooperative board-game adaptation.
- Puzzle family: stochastic expanding hex-landscape placement and score
  optimisation.
- Primary sources:
  - **[F1]** [Toukana Interactive — Dorfromantik](https://www.toukana.com/dorfromantik),
    creator overview of the ever-growing tile-built landscape and quests.
  - **[F2]** [Toukana Interactive press kit](https://www.toukana.com/dorfromantik/presskit),
    creator description, release facts, high-score objective and mode boundary.
  - **[F3]** [official Steam product description](https://store.steampowered.com/app/1455840/Dorfromantik/),
    developer/publisher account of procedural tile supply, rotation,
    placement, groups, quest rewards and stack-exhaustion termination.
- Rule-detail corroboration:
  - **[S1]** [Dorfromantik Wiki — How to play](https://dorfromantik.fandom.com/wiki/How_to_play_guide_for_Dorfromantik),
    current tile and preview display, edge feedback, perfect placements and
    tile rewards.
  - **[S2]** [Dorfromantik Wiki — Tiles](https://dorfromantik.fandom.com/wiki/Tiles),
    typed edge sections, connected groups, placement compatibility and perfect
    closure.
  - **[S3]** [Dorfromantik Wiki — Quests](https://dorfromantik.fandom.com/wiki/Quests),
    minimum, exact and closure quest predicates and stack rewards.
  - **[S4]** [Dorfromantik Wiki — Score](https://dorfromantik.fandom.com/wiki/Score),
    edge, perfect-placement and quest scoring.
- Claim IDs: `DOR-001`–`DOR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-026` — orient and place mandatory supply-head tile. The player chooses
  one of the current hex tile's rotations and an eligible frontier hex, then
  commits that exact tile.
- This is not `ACT-020`: Pipe Dream's supplied queue head is fixed in its
  displayed orientation, whereas Dorfromantik makes orientation part of the
  placement decision.
- The player does not directly command a landscape-group merge, score event or
  tile reward.
- Claim IDs: `DOR-001`, `DOR-002`, `DOR-012`.

### System Behaviour Genes

- `SYS-004` — random outcome selection. Procedural generation selects tile and
  quest characteristics across sessions; the exact disclosed horizon remains
  visible once generated.
- `SYS-024` — visible supplied-sequence advance. Committing the current tile
  promotes the next previewed tile and reveals a new successor while supply
  remains.
- `SYS-034` — placement-triggered edge and group evaluation. After commitment,
  the system classifies new shared edges, merges compatible landscape groups,
  checks affected quests and perfect closures, and assigns score.
- `SYS-035` — earned action-supply replenishment. A completed quest or perfect
  placement inserts reward tiles into the finite stack without an additional
  player command.
- Resolution order is placement, edge/group update, quest and perfect checks,
  score and supply rewards, then queue advance to the next current tile.
- Claim IDs: `DOR-001`, `DOR-003`–`DOR-007`, `DOR-012`.

### Constraint Genes

- `CON-056` — adjacent-frontier expanding placement. A committed tile occupies
  an empty hex adjoining the connected landscape, and the new perimeter adds
  possible future positions. `CON-001` is absent because Classic mode does not
  begin with a fixed set of addressable board cells.
- `CON-039` — mandatory supplied-head commitment. The current tile may rotate
  through `ACT-026`, but it cannot be exchanged for a visible successor,
  stored or discarded within the scoped rules.
- `CON-058` — typed shared-edge compatibility. Matching terrain edges connect
  groups and support perfect placement; rail and river exits impose stricter
  continuation limits than ordinary score-losing mismatches.
- `CON-059` — replenishable finite supply with exhaustion termination. Every
  placement spends a tile, qualifying placements can earn tiles back, and an
  empty stack ends the session.
- `CON-020` is absent. Royal Match and Balatro consume a bounded attempt
  allowance that ordinary successful actions do not replenish inside that
  attempt; Dorfromantik's central feedback loop explicitly expands its own
  remaining action supply.
- Claim IDs: `DOR-001`, `DOR-002`, `DOR-004`, `DOR-006`–`DOR-010`.

### Information Genes

- `INF-001` — fully visible current state. Placed tiles, open frontier,
  connected groups, quest markers, score and remaining stack count are visible.
- `INF-005` — exact ordered successor preview. The current tile and the next
  two supplied tiles are shown in order; later procedural outcomes remain
  outside the disclosed horizon.
- Preview does not permit selection. `INF-005` describes knowledge while
  `CON-039` preserves forced consumption order.
- Claim IDs: `DOR-003`, `DOR-012`.

### Objective Genes

- `OBJ-002` — maximise accumulated score through compatible edges, perfect
  closures and quest completion.
- `OBJ-003` — preserve move availability by maintaining the tile stack. There
  is no fixed winning score in the scoped Classic session; extending supply
  enables further scoring decisions before inevitable or avoidable exhaustion.
- Individual quests are reward conditions inside this optimisation loop, not
  the final session objective.
- Claim IDs: `DOR-005`–`DOR-011`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. The player may
  deliberate indefinitely over rotation and position; after commitment, all
  evaluation, scoring, rewards and queue changes complete before the next
  tile is placed.
- No simulation clock independently changes the landscape in Classic mode.
- Claim IDs: `DOR-002`, `DOR-012`.

## Reproducible transitions

| Before | Player action | Automatic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current tile has several rotations and one successor is previewed | Rotate and place the current tile on an adjacent empty hex | Shared edges and groups are evaluated; the successor becomes current | Orientation and position are one command; queue progression is automatic | `DOR-002`, `DOR-003`, `DOR-012` |
| A legal placement touches one matching and one ordinary mismatching edge | Commit the tile | The matching edge joins its group and scores; the mismatch remains a non-perfect boundary | Compatibility affects value without making every mismatch illegal | `DOR-004`, `DOR-005` |
| An empty hex is enclosed by six compatible neighbours | Rotate the current tile so all six sides match and place it | The system recognises a perfect placement, scores it and adds a reward tile | Spatial closure can replenish the consumed supply | `DOR-006`, `DOR-009` |
| A quest group is below its required amount | Place a tile that connects enough matching landscape elements | The group reaches the predicate; score and several stack tiles are awarded | Group completion is evaluated after placement | `DOR-005`, `DOR-007` |
| A visible successor would fit better than the current tile | Attempt to select it first | It remains unavailable until the current tile is committed | Preview does not grant queue reordering | `DOR-002`, `DOR-003` |
| Exactly one tile remains and its placement earns no reward | Commit it | Resolution completes, the stack becomes empty and the session ends | Finite-supply exhaustion is terminal | `DOR-008`, `DOR-009` |
| Exactly one tile remains and its placement completes a quest | Commit it | Reward tiles enter the stack, so another placement becomes available | The action budget is replenishable, not monotonic | `DOR-007`, `DOR-009` |

## Strategic and experiential structure

- Local decision: maximise compatible shared edges without giving the current
  tile an orientation that blocks rail, river or quest continuations.
- Medium-term planning: shape groups toward their quest thresholds while
  reserving frontier geometries that the known successor tiles can fill.
- Long-term structure: convert placements into enough perfect closures and
  quest rewards that the stack survives while score compounds over an
  expanding, increasingly constrained boundary.
- Common heuristics: build compactly to create six-neighbour holes; keep exact
  quests separable from oversized groups; leave flexible ordinary terrain on
  exposed edges; avoid isolated rail or river exits.
- Failure attribution: random future supply constrains options, but the visible
  horizon, persistent edge commitments and explicit reward feedback expose why
  a placement either preserved or consumed future runway.
- Player-trust factors: preview order, highlighted edge compatibility, group
  membership, quest progress, score credit and stack rewards must agree.
- Claim IDs: `DOR-002`–`DOR-012`.

## Replay and variation

- What changes: procedural tile and quest order, resulting landscape topology,
  available perfect-placement pockets and the player's placement history.
- What remains stable: mandatory current-tile order, rotation freedom,
  adjacency, edge/group evaluation, reward loop and stack-exhaustion boundary.
- Randomness or procedural generation: a new session supplies a different
  sequence, while the short disclosed successor horizon supports contingent
  planning.
- Multiple viable strategies: compact perfect-placement play, quest-focused
  group growth and hybrid approaches can all extend a run and raise score.
- Typical replay motive: beat a personal high score, improve perfect-placement
  efficiency or recover better from an awkward tile sequence.
- Claim IDs: `DOR-001`, `DOR-003`, `DOR-005`–`DOR-011`.

## Adjacent systems and history

- Pipe Dream also exposes a mandatory previewed tile queue, but its pieces
  cannot rotate and must prepare a path before a real-time flow reaches it.
  Dorfromantik resolves adjacency immediately and remains self-paced.
- Flow Free also values spatial connectivity, but it traces fixed-endpoint
  paths across a finite full-cover board. Dorfromantik places discrete typed
  tiles on a growing frontier and does not require global coverage.
- 2048 and Threes share stochastic successor pressure, score maximisation and
  move preservation. Their fixed 4 × 4 boards generate capacity through
  movement and merging; Dorfromantik generates space outward but can run out
  of supply.
- Creative and Custom modes can remove or alter the supply and world limits;
  they are different rulesets rather than parameters silently folded into this
  Classic genome.
- Claim IDs: `DOR-001`–`DOR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-026` | rotation count and input method |
| System Behaviour | `SYS-004`, `SYS-024`, `SYS-034`, `SYS-035` | generator, score table and reward quantities |
| Constraint | `CON-039`, `CON-056`, `CON-058`, `CON-059` | supply order, hex topology, edge vocabulary and initial stack |
| Information | `INF-001`, `INF-005` | exact preview depth |
| Objective | `OBJ-002`, `OBJ-003` | score and survival trade-off |
| Time | `TIM-001` | one completed placement cycle |

Canonical signature:

`ACT-026; SYS-004,SYS-024,SYS-034,SYS-035; CON-039,CON-056,CON-058,CON-059; INF-001,INF-005; OBJ-002,OBJ-003; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `19` (`GAME-0001`–`GAME-0019`).
- Exact genome matches: none.
- Tied near matches: `GAME-0016` — Pipe Mania / Pipe Dream (`6 / 23 = 0.260870`).
- Supported combination subsets: `COMB-0020`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0016` — Pipe Mania / Pipe Dream | `SYS-004`, `SYS-024`, `CON-039`, `INF-001`, `INF-005`, `OBJ-002` | Both consume an exact visible supplied sequence in order; Pipe Dream fixes orientation and builds ahead of live flow, while Dorfromantik permits rotation and grows a scored frontier whose quality can replenish supply | Near, `0.260870` |

### Preserved research notes

- New genes at original analysis time: `ACT-026`, `SYS-034`, `SYS-035`, `CON-056`, `CON-057`,
  `CON-058`, `CON-059`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: existing randomness, visible queue advance, current
  visibility, exact preview, score, move preservation and discrete resolution
  boundaries fit. Placement with rotation, expanding frontier geometry,
  typed-edge group evaluation and supply earned back by good play require
  narrower new boundaries.

## Combination record

- Registered [`COMB-0020`](../../combinations/COMB-0020.md), a proper
  eleven-gene subset centred on mandatory rotatable placement whose spatial
  quality can replenish the finite supply it consumes.
- Procedural randomness, general current-state visibility and the low-level
  typed-edge predicate remain in the complete genome but are not all required
  to identify that feedback loop.

## Taxonomy impact

- Registry changes at original analysis time: seven stable genes added and
  seven existing genes reused. Normalisation later merged `CON-057` into
  shared `CON-039` through `TAXONOMY_CHANGE_002`.
- Candidate terms affected: rotatable supply-head placement, expanding
  frontier, typed shared-edge compatibility and replenishable action supply
  are promoted from generic vocabulary.

## Negative results

- `CON-001` is absent because the ordinary landscape expands into newly
  addressable frontier positions rather than filling a fixed board.
- `CON-020` is absent because qualifying in-session play replenishes the same
  action supply whose exhaustion ends the session.
- `ACT-020` is absent because current tiles may rotate. `CON-039` is present:
  it now represents mandatory supplied-head commitment independently of
  transform permission.
- `CON-040` and `SYS-025` are absent because edge matching updates static
  landscape groups; no live directed flow traverses the network.
- `OBJ-006` is absent because Classic mode does not require a globally complete
  assignment or full-board cover.
- No structured negative-result record is required because no prior concrete
  novelty or taxonomy claim was rejected.
