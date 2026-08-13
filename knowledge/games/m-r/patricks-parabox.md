---
game_id: GAME-0036
slug: patricks-parabox
game_title: "Patrick’s Parabox"
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0036
  - COMB-0044
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-018
  system:
    - SYS-069
    - SYS-070
  constraint:
    - CON-011
    - CON-013
    - CON-082
  information:
    - INF-001
    - INF-022
  objective:
    - OBJ-004
  time:
    - TIM-002
---

# Game: Patrick's Parabox

## Analysis scope

- Version / ruleset: Patrick Traynor's 2022 base game, scoped to the ordinary
  authored recursive box-pushing grammar after enterable boxes, exiting,
  multi-box pushing and self-containing boxes have been introduced.
- Included: cardinal player movement; ordinary and contiguous-chain pushes;
  static wall occupancy; box entry and exit through aligned open boundaries;
  pushing boxes into and out of other boxes; identity-preserving nested and
  cyclic containment; visible parent context; separate box and player goals;
  self-paced resolution and objective deadlocks.
- Excluded: later named variants such as Eat, Wall, Open, clone / transfer
  mechanics and alternate rulesets; overworld progression; optional challenge
  taxonomy; custom levels; secrets; achievements; narrative interpretation;
  undo and reset as recovery interface commands.
- Direct-play status: not conducted. The official press kit and store copy,
  Patrick Traynor's post-release rules interview and GDC slides establish the
  system; contemporary reviews corroborate goals, no-pull pushing, entry,
  recursion and recovery controls. Exact animation timing is not classified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PPB-001` | The player moves one cell orthogonally and pushes adjacent boxes rather than pulling them | Confirmed | Corroborated | High | P2, P3, S1, S2 |
| `PPB-002` | A legal directional push can advance a contiguous aligned row of multiple boxes | Confirmed | Direct | High | P2, P3 |
| `PPB-003` | Enterable boxes are both movable parent-grid objects and containers with their own fixed internal cell grids | Confirmed | Direct | High | P1–P3 |
| `PPB-004` | An actor or pushed box crosses between parent and child spaces through a corresponding open boundary, with current rules using the centre position of that side | Confirmed | Direct | High | P2, P3 |
| `PPB-005` | Pushing a box into or out of another changes containment membership while preserving the moved box and its contents | Confirmed | Direct | High | P1–P3 |
| `PPB-006` | A box may recursively contain itself, and moving that box into another box changes the resulting world structure | Confirmed | Direct | High | P1–P3 |
| `PPB-007` | The camera exposes the active interior while retaining surrounding parent context needed to judge whether exit is blocked | Confirmed | Direct | High | P2, P3 |
| `PPB-008` | A scoped puzzle is complete only when ordinary boxes occupy their box goals and the player occupies the designated player goal | Confirmed | Corroborated | High | S1, S2 |
| `PPB-009` | Legal pushes can make the goal configuration unreachable while other movement remains possible; undo or reset permits interface recovery | Confirmed | Corroborated | High | S1–S3 |
| `PPB-010` | Moves resolve deterministically and sequentially without a running simulation clock | Observation | Corroborated | High | P2, S1–S3 |
| `PPB-011` | Recursive containment is authoritative world topology, not a camera-only zoom, visual overlay or fixed paired portal | Observation | Corroborated | High | PPB-003–PPB-007 |
| `PPB-012` | The finite authored object set can form an unbounded recursive view without creating new gameplay objects at every visible depth | Observation | Corroborated | Medium | P1–P3 |

## Basic data

- Release / origin: Patrick Traynor released the Windows, macOS and Linux
  versions on 29 March 2022; Draknek & Friends published console versions on
  26 July 2023.
- Platform or physical form: deterministic two-dimensional cardinal-grid
  block-pushing puzzle whose boxes can also be traversable nested spaces.
- Puzzle family: recursive-containment Sokoban.
- Primary and creator sources:
  - **[P1]** [Official press kit](https://www.patricksparabox.com/press/),
    describing boxes pushed into and out of one another, self-containment,
    infinity and more than 350 authored puzzles.
  - **[P2]** [Game Developer interview with Patrick Traynor](https://www.gamedeveloper.com/design/patrick-s-parabox-),
    defining the game as recursive block pushing, explaining nested areas,
    entry / emergence, self-containment, row pushing and centre-only entry.
  - **[P3]** Patrick Traynor,
    [“System-Centric Puzzle Design”](https://media.gdcvault.com/gdc2024/Slides/GDC%2Bslide%2Bpresentations/Traynor_Patrick_SystemCentricPuzzle.pdf),
    GDC 2024 slides illustrating the recursive system and its rule-led puzzle
    exploration.
- Official storefront corroboration:
  - **[P4]** [Steam product page](https://store.steampowered.com/app/1260520/Patricks_Parabox/),
    confirming developer, release date, recursive world manipulation and the
    authored puzzle collection.
- Contemporary corroboration:
  - **[S1]** [Slant Magazine review](https://www.slantmagazine.com/games/patricks-parabox-review/),
    documenting cardinal no-pull pushing, box and player goals, enterable boxes
    and self-referential structures.
  - **[S2]** [Nintendo Life review](https://www.nintendolife.com/reviews/switch-eshop/patricks-parabox),
    documenting recursive navigation, box placement, self-containing boxes and
    immediate undo / reset recovery.
  - **[S3]** [PlayStation Universe review](https://www.psu.com/reviews/patricks-parabox-review-ps5/),
    corroborating inside / outside traversal and unlimited undo / reset.
- Claim IDs: `PPB-001`–`PPB-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One cardinal input moves Patrick
  into an adjacent free local cell, including an eligible cross-boundary move
  whose topology is resolved by `SYS-069`.
- `ACT-009` — push adjacent movable object. A directional input advances one
  adjacent box into a valid free local or cross-boundary destination and moves
  Patrick into the vacated position.
- `ACT-018` — push contiguous movable chain. When several aligned boxes
  can all resolve one step from the far end, one input advances the entire row.
- `ACT-034` is absent: the player navigates one persistent world actor rather
  than selecting a view node in a scene graph. `ACT-047` is absent because no
  remote portal endpoints are aimed or placed.
- Undo and reset restore discrete input history for recovery but do not expose
  a simulation timeline, so neither is `ACT-044`.
- Claim IDs: `PPB-001`, `PPB-002`, `PPB-004`.

### System Behaviour Genes

- `SYS-069` — aligned container-boundary transfer. A legal inward or outward
  directional move maps an actor or pushed box between the centre-aligned edge
  cells of a container's parent and child grids while preserving identity.
- `SYS-070` — recursive containment-graph reparenting. When one box is pushed
  into or out of another, the moved box and its complete interior acquire the
  destination containment relation; cyclic self-containment remains a valid
  authoritative topology.
- `SYS-043` is absent: entry does not substitute a picture inside one fixed
  panel slot. `SYS-044` is absent: separate images are not temporarily treated
  as one authored seam. `SYS-059` is absent: there is no fixed complementary
  aperture pair.
- Resolution order: test the aligned chain from its distal member; test local
  occupancy and boundary eligibility; resolve required parent / child transfer;
  update any moved container's parent relation with its interior intact; move
  nearer boxes and Patrick; then test the goal configuration.
- Claim IDs: `PPB-003`–`PPB-006`, `PPB-011`, `PPB-012`.

### Constraint Genes

- `CON-011` — exclusive occupancy with static barriers. Every local cell holds
  at most one occupying entity and wall cells block movement and pushing.
- `CON-013` — irrecoverable objective deadlock. Within world state, a legal
  push may strand a required box or Patrick so the goals cannot all be filled,
  even though interface undo can restore an earlier discrete state.
- `CON-082` — centre-aligned nested-boundary access. Entry or exit requires the
  appropriate side's centre cell and corresponding source / destination route
  to be open; another open cell elsewhere on that edge is insufficient.
- `CON-001` is absent at whole-puzzle scale because moving a container changes
  which addressed grid is parent, child or self-referential. Each individual
  box grid is finite and authored, but the playable containment topology is not
  one fixed finite position set.
- `CON-012` is absent because legal actions may push two or more contiguous
  boxes. Pulling remains unavailable as a parameter of the action set.
- Scarce strategic resources: access to pushing sides, centre-boundary
  clearance, containment depth / parent relation and goal-compatible staging
  cells.
- Claim IDs: `PPB-001`–`PPB-006`, `PPB-009`.

### Information Genes

- `INF-001` — fully visible current state. The current local grid exposes its
  walls, occupants and goals, and deterministic nesting can be inspected before
  committing the next move; there is no hidden or random puzzle variable.
- `INF-022` — nested-space view with parent-boundary context. When focus moves
  into an enterable box, the interior expands while the surrounding parent
  geometry remains visible enough to expose the corresponding exit blockage
  and containment relation.
- `INF-014` is absent: useful positions are authoritative nested grids, not
  hidden illustrated view nodes selected for composition.
- Claim IDs: `PPB-007`, `PPB-010`–`PPB-012`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. Required boxes must occupy
  box goal cells and Patrick must occupy the distinct player goal; container
  depth and exact identities matter only where the authored target marking
  distinguishes them.
- This generalises the target-equivalence parameter from Sokoban's
  interchangeable crate set to multiple marked occupant classes without
  changing the arrangement objective.
- Claim IDs: `PPB-008`, `PPB-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. Each cardinal input completely
  resolves movement, chain propagation, boundary transfer and containment
  updates before another input is accepted; waiting changes nothing.
- Unlimited undo is discrete recovery history, not `TIM-007`: no previously
  lived continuous simulation is scrubbed or resumed under live progression.
- Claim IDs: `PPB-009`, `PPB-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty cardinal neighbour in current grid | Move toward it | Patrick occupies the neighbour | ordinary navigation survives recursion | `PPB-001` |
| One box has a free destination behind it | Move toward the box | Box advances and Patrick occupies its old cell | single Sokoban push remains present | `PPB-001` |
| Two aligned boxes have a resolvable distal destination | Push the nearer box | Both advance one step from distal to proximal | chain pushing violates `CON-012` | `PPB-002` |
| Enterable box has open aligned centre access | Move Patrick into its side | Patrick transfers to the interior edge and the view expands | box is traversable child space | `PPB-003`, `PPB-004` |
| Centre interior entry cell is blocked but another edge cell is open | Move toward the box | Entry is rejected | access is centre-aligned, not any-edge search | `PPB-004` |
| Patrick reaches an open interior boundary with clear parent destination | Move outward | Patrick transfers to the parent's corresponding side | exit is inverse topological transfer, not visual zoom alone | `PPB-004` |
| A movable box is aligned with an enterable box | Push it through the boundary | Moved box becomes a child while retaining its contents | pushing rewrites containment membership | `PPB-005` |
| A self-containing box is moved into a different box | Complete the legal push | Its cyclic identity persists under a new outer parent relation | recursion is authoritative topology | `PPB-006` |
| Required box or Patrick is stranded from a goal | Continue legal walking | Movement can remain legal although completion is unreachable | non-terminal objective deadlock | `PPB-009` |
| All marked box goals and the player goal are occupied correctly | Complete final move | Puzzle completion is credited | target configuration spans occupant classes | `PPB-008` |

## Strategic and experiential structure

- Local decision: choose a walk, one-box push, chain push or boundary crossing
  and check the destination in the correct containment frame.
- Medium-term planning: preserve access to both sides of an enterable box,
  stage boxes at centre apertures and decide whether a container should be
  moved as an object before entering its interior.
- Long-term structure: reason over the mutable containment graph, including
  which space is parent, child or cyclic, while reconstructing the marked goal
  configuration.
- Common heuristics: name the active containment level; trace a prospective
  push from the distal chain member; distinguish moving a container from moving
  inside it; reserve a return path through each centre aperture.
- Failure attribution: a visible but mentally mis-scoped parent relation often
  causes mistakes; unlimited discrete undo makes the responsible push locally
  recoverable without erasing its world-state deadlock property.
- Player-trust factors: centre alignment, preserved box identity, distal-first
  chain resolution, scale animation and parent-context visibility must remain
  consistent through self-reference.
- Claim IDs: `PPB-001`–`PPB-012`.

## Replay and variation

- What changes between puzzles: local grids, containment graph, goal classes,
  available box types and which recursive relation must be exploited.
- Randomness or procedural generation: none in the scoped authored puzzles.
- Multiple viable strategies: exploratory walking and some staging orders may
  differ, but small deterministic levels often constrain the decisive
  containment transitions tightly.
- Typical replay motive: recover through undo / reset, understand a recursive
  consequence, solve an optional challenge or reduce exploratory moves.
- Claim IDs: `PPB-008`–`PPB-010`.

## Adjacent systems and history

- Sokoban supplies direct navigation, single-box pushing, occupancy, deadlock,
  target reconstruction and self-paced play. Patrick's Parabox removes the
  global fixed-board and single-object-only restrictions, adding chain motion
  and mutable recursive containment.
- Gorogoa's nested views are information nodes inside four fixed panel slots;
  their overlay creates authored represented continuity. Parabox moves actual
  occupants and containers between authoritative parent / child grids.
- Portal maps bodies through a replaceable paired aperture and reorients
  velocity in one continuous space. Parabox has no placed endpoint pair,
  momentum transform or real-time physics.
- The creator cites Sokoban as the core lineage and notes earlier box-within-
  box exploration such as Sokosoko; this record makes no novelty claim.
- Claim IDs: `PPB-001`–`PPB-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009`, `ACT-018` | cardinal movement, one-box and chain push |
| System Behaviour | `SYS-069`, `SYS-070` | boundary transfer and containment reparenting |
| Constraint | `CON-011`, `CON-013`, `CON-082` | occupancy, deadlock and centre access |
| Information | `INF-001`, `INF-022` | visible state and parent-context nesting |
| Objective | `OBJ-004` | marked box and player goal configuration |
| Time | `TIM-002` | deterministic self-paced inputs |

Canonical signature:

`ACT-008,ACT-009,ACT-018; SYS-069,SYS-070; CON-011,CON-013,CON-082; INF-001,INF-022; OBJ-004; TIM-002`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0035`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0035`.
- Exact genome matches: none.
- Existing combination subsets: none before registering `COMB-0036`.
- Full Jaccard scan (intersection / union = score):
  `GAME-0001` `1 / 25 = 0.040000`; `GAME-0002` `3 / 16 = 0.187500`;
  `GAME-0003` `0 / 21 = 0.000000`; `GAME-0004` `1 / 26 = 0.038462`;
  `GAME-0005` `2 / 17 = 0.117647`; `GAME-0006` `7 / 14 = 0.500000`;
  `GAME-0007` `3 / 17 = 0.176471`; `GAME-0008` `2 / 17 = 0.117647`;
  `GAME-0009` `1 / 27 = 0.037037`; `GAME-0010` `1 / 20 = 0.050000`;
  `GAME-0011` `2 / 23 = 0.086957`; `GAME-0012` `2 / 19 = 0.105263`;
  `GAME-0013` `3 / 22 = 0.136364`; `GAME-0014` `2 / 25 = 0.080000`;
  `GAME-0015` `1 / 25 = 0.040000`; `GAME-0016` `1 / 26 = 0.038462`;
  `GAME-0017` `0 / 25 = 0.000000`; `GAME-0018` `1 / 30 = 0.033333`;
  `GAME-0019` `3 / 19 = 0.157895`; `GAME-0020` `1 / 25 = 0.040000`;
  `GAME-0021` `1 / 20 = 0.050000`; `GAME-0022` `1 / 23 = 0.043478`;
  `GAME-0023` `1 / 21 = 0.047619`; `GAME-0024` `1 / 23 = 0.043478`;
  `GAME-0025` `1 / 22 = 0.045455`; `GAME-0026` `1 / 23 = 0.043478`;
  `GAME-0027` `1 / 23 = 0.043478`; `GAME-0028` `1 / 28 = 0.035714`;
  `GAME-0029` `2 / 22 = 0.090909`; `GAME-0030` `1 / 25 = 0.040000`;
  `GAME-0031` `1 / 22 = 0.045455`; `GAME-0032` `1 / 22 = 0.045455`;
  `GAME-0033` `2 / 23 = 0.086957`; `GAME-0034` `2 / 24 = 0.083333`;
  `GAME-0035` `2 / 28 = 0.071429`.
- Mathematical near match: `GAME-0006` — Sokoban at `7 / 14 = 0.500000`.
  Both share navigation, ordinary pushing, occupancy, non-terminal deadlock,
  visible state, arrangement reconstruction and self-paced play. Patrick's
  Parabox replaces Sokoban's fixed global board and one-box-only access rule
  with chain pushing and recursive containment.

## Combination record

- Registered recurring `COMB-0036` — visible self-paced push-only target
  reconstruction, supported by Sokoban and Patrick's Parabox.
- The shared seven-gene core excludes Sokoban's fixed board and single-box
  access restriction as well as every Parabox-specific recursive transition.

## Taxonomy impact

- Registry changes at admission: five stable genes added and seven existing
  genes reused. `TAXONOMY_CHANGE_003` subsequently merged duplicate `ACT-053`
  into pre-existing `ACT-018` without changing genome size.
- `OBJ-004` examples now explicitly admit multiple marked occupant classes as
  a target-equivalence parameter.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_003`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_003.md).

## Negative results

- `CON-001` and `CON-012` are rejected because whole-puzzle topology can be
  reparented recursively and one input may push a multi-box chain.
- `ACT-034`, `SYS-043`, `SYS-044` and `INF-014` are rejected because entry
  changes actor containment in authoritative space rather than selecting or
  composing illustrated views.
- `ACT-047`, `SYS-059` and `SYS-060` are rejected because nested boundaries
  are neither placed portal pairs nor continuous momentum transforms.
- `ACT-044` / `TIM-007` are rejected: discrete undo is a recovery interface,
  not branchable continuous simulation history.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Boxes are simultaneously movable objects and
  fixed internal grids; centre-aligned crossing transfers occupants between
  containment levels (`PPB-003`–`PPB-005`).
- [Confirmed | Direct | High] Box movement can rewrite a cyclic containment
  graph while preserving object identity and contents (`PPB-005`, `PPB-006`).

## Нові гени

- [Observation | Corroborated | High] Added `SYS-069`, `SYS-070`, `CON-082`
  and `INF-022`; the initially added duplicate `ACT-053` was merged into
  reused `ACT-018` by taxonomy change 003.

## Нові комбінації

- [Observation | Corroborated | High] Registered recurring `COMB-0036` for the
  seven-gene shared Sokoban / Patrick's Parabox push-reconstruction core.

## Зміни таксономії

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_003` merged duplicate
  chain-push Action IDs while retaining recursive-space boundaries.

## Нові питання

- Does the 36-game checkpoint justify merging any remaining fixed-space or
  navigation singletons after recursive containment exposed their boundaries?
- Is The Swapper still the best next falsifier after the checkpoint, or should
  Carto test another form of authoritative topology editing first?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `CHECKPOINT_036` before another game.
- Optimisation criterion: honour the six-game audit cadence and measure whether
  recent targeted reuse reduced singleton density without collapsing recursive
  topology distinctions.
- Expected information gain: recheck all six types, combination supporters,
  lifecycle aliases and the next candidate ordering at a 36-game boundary.
- Backlog impact: retain The Swapper, Viewfinder and Carto until the checkpoint.

## Sources consulted

- Official Patrick's Parabox press kit, Steam page and GDC 2024 slides.
- Patrick Traynor's post-release Game Developer interview.
- Contemporary Slant Magazine, Nintendo Life and PlayStation Universe reviews.
