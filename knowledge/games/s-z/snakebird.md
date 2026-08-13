---
game_id: GAME-0045
slug: snakebird
game_title: Snakebird
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0045
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-037
    - SYS-082
    - SYS-083
    - SYS-084
    - SYS-085
  constraint:
    - CON-001
    - CON-011
    - CON-013
    - CON-061
  information:
    - INF-001
  objective:
    - OBJ-007
    - OBJ-022
  time:
    - TIM-001
---

# Game: Snakebird

## Analysis scope

- Version / ruleset: Noumenon Games' original 2015 Snakebird, scoped to early
  `Level 1`: one snakebird, two fruit, fixed terrain, unsupported boundary
  space and one exit portal.
- Included: one-cell cardinal head input; ordered body following; collision
  with terrain and the snakebird's own body; fruit contact and removal; one
  persistent segment added per fruit; whole-body support; post-input vertical
  falling; abyss death; automatic rollback to the preceding safe state;
  unlimited discrete undo and restart as recovery controls; all-fruit exit
  activation; head-first exit and level completion.
- Excluded: later spikes, multiple snakebirds, movable blocks, inter-snake
  pushing / support, paired portals, advanced zones, world-map progression,
  Snakebird Primer and Snakebird Complete, achievements and speedrunning.
- Direct-play status: not conducted. The developer-published store page and
  development history establish fruit-powered length, snake motion and gravity;
  a peer-reviewed formal domain account establishes action-then-gravity and the
  all-fruit / all-actors goal; platform editorial and contemporary reviews
  corroborate tail collision, segment growth, exit gating, death and undo. An
  early-level guide is used only to bound Level 1 to two fruit and no spikes.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SNB-001` | Level 1 is a fixed side-view grid with one snakebird, two fruit, fixed terrain and one exit | Confirmed | Corroborated | High | P1, A1, S1, R1 |
| `SNB-002` | One cardinal input moves the head one grid cell and every later segment follows its predecessor's prior position | Confirmed | Corroborated | High | P1, A1, S1–S3 |
| `SNB-003` | Terrain and the snakebird's own occupied body cells block head entry | Confirmed | Corroborated | High | S1–S4 |
| `SNB-004` | Head contact removes one fruit and adds one persistent body segment without changing existing segment identities | Confirmed | Corroborated | High | P1, A1, S1–S4 |
| `SNB-005` | After the commanded step, an unsupported snakebird falls vertically in its retained shape until supported or lost | Confirmed | Direct | High | A1, S2, S3 |
| `SNB-006` | Support by any body segment on fixed terrain prevents falling; resting only on the snakebird's own body is not external support | Confirmed | Corroborated | High | A1, S2, R2 |
| `SNB-007` | Falling beyond supported level space kills the required snakebird and restores the preceding safe move | Confirmed | Corroborated | High | A1, S1, S3, R2 |
| `SNB-008` | The exit remains unavailable until all fruit has been eaten | Confirmed | Corroborated | High | A1, S2–S4 |
| `SNB-009` | After activation, moving the head into the fixed exit removes the sole snakebird and completes the scoped level | Confirmed | Corroborated | High | A1, S2–S4 |
| `SNB-010` | A legal growth or body pose can leave actions available while making remaining fruit or exit access unreachable | Observation | Corroborated | High | S1–S4 |
| `SNB-011` | Terrain, fruit, exit state and every ordered body segment are visible before each input | Observation | Corroborated | High | P1, A1, S1–S4 |
| `SNB-012` | Movement, fruit, growth, support, fall, death rollback and exit checks resolve before another input | Observation | Corroborated | High | A1, S2, R2 |
| `SNB-013` | Fruit growth creates body geometry and is not Snowman's bounded unary size-state transition | Observation | Corroborated | High | SNB-004–SNB-006 |

## Basic data

- Release / origin: Noumenon Games developed and published Snakebird on
  4 May 2015.
- Platform or physical form: deterministic single-player side-view grid puzzle
  with one directly commanded articulated body.
- Puzzle family: head-led body-shape planning under discrete gravity.
- Primary and developer sources:
  - **[P1]** [developer-published Steam page](https://store.steampowered.com/app/357300/Snakebird/),
    identifying Noumenon Games, release date, shape-based puzzle actions and the
    dynamic fruit-powered length system.
  - **[P2]** Felix Eliasson,
    [Snakebird development, images and history](https://www.gamedeveloper.com/production/snakebird-development-images-and-history),
    documenting the snake-derived design and implementation of gravity, fruit
    and spikes.
- Formal transition evidence:
  - **[A1]** Sturtevant et al.,
    [The Unexpected Consequence of Incremental Design Changes](https://webdocs.cs.ualberta.ca/~nathanst/papers/sturtevant2020incremental.pdf),
    specifying one-cell action followed by gravity, support, fruit growth,
    hazard death and the all-fruit-before-all-exit objective.
- Platform and specialist corroboration:
  - **[S1]** [Apple editorial overview](https://apps.apple.com/us/iphone/story/id1350884296),
    describing grid input, fruit growth, tail blocking, gravity, falling death
    and exit arrival.
  - **[S2]** [Thinky Games overview](https://thinkygames.com/games/snakebird/),
    documenting all-fruit exit activation, segment support and turn-based play.
  - **[S3]** [Destructoid review](https://www.destructoid.com/reviews/review-snakebird/),
    corroborating one-segment growth, deadlock, death rollback and portal gate.
  - **[S4]** [Pocket Gamer's contemporary account](https://www.pocketgamer.com/snakebird/steam-tip-snakebird-turns-nokia-classic-snake-into-a-deadly-puzzle-of-contortion/),
    documenting grid increments, body-as-obstacle, fruit growth and exit goal.
- Scope and edge references:
  - **[R1]** [Levels 0–10 guide](https://www.levelwinner.com/snakebird-guide-walkthrough-levels-0-10/),
    used only to bound Level 1 to two fruit, cliff support and its portal.
  - **[R2]** [independent solver account](https://blog.jverkamp.com/2021/08/18/solving-snakebird/),
    used to corroborate full-body support, falling, fixed terrain and exit
    ordering rather than as evidence of an official implementation.
- Claim IDs: `SNB-001`–`SNB-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One cardinal input directly advances
  the persistent snakebird head by one cell through legal grid geometry.
- The action parameter now records a multi-segment agent whose remaining body
  follows automatically. `ACT-009` is absent: the scoped level has no movable
  block or second snakebird, and the player's own articulated body is not an
  adjacent independently pushed object.
- Undo and restart are recovery interface controls, not a second manipulation
  action or player-navigable continuous history.
- Claim IDs: `SNB-001`–`SNB-003`.

### System Behaviour Genes

- `SYS-037` — contact-triggered collectible acquisition. Head contact removes
  one required fruit and credits it toward the exit gate without immediately
  completing the level.
- `SYS-082` — head-led ordered body propagation. A legal head step makes each
  segment occupy its predecessor's immediately prior cell, preserving order and
  producing a new articulated pose.
- `SYS-083` — consumable-contact persistent segment growth. Eating fruit adds
  one new tail segment while retaining every existing segment and future body
  collision / support consequences.
- `SYS-084` — post-input unsupported rigid-shape fall. After commanded motion
  and growth, the system tests external support and translates the complete
  current body vertically until supported or terminally lost.
- `SYS-085` — exhaustive-collection exit activation. Removal of the final fruit
  changes the fixed exit from unavailable to eligible before the next input.
- `SYS-036` is absent: gravity is a completed cellwise resolution after input,
  with no continuously integrated position, velocity or between-input motion.
- `SYS-080` is absent: fruit consumption adds topology to an unbounded-length
  articulated body; it does not advance one object through a finite state ladder
  with an absorbing maximum.
- Resolution order: validate the next head cell and ordered body move; propagate
  all existing segments; acquire contacted fruit and append the new tail cell;
  activate the exit if no fruit remains; test external support; fall the entire
  shape until supported or lost; roll back terminal death; otherwise accept the
  next input or complete on eligible head-first exit.
- Claim IDs: `SNB-002`, `SNB-004`–`SNB-009`, `SNB-012`, `SNB-013`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Level 1 has one finite authored set of
  terrain and air cells; fruit and exit state change without expanding it.
- `CON-011` — exclusive occupancy with static barriers. Each cell contains at
  most one snakebird segment, fruit or incompatible terrain occupant; the head
  cannot enter fixed terrain or the current body footprint.
- `CON-013` — irrecoverable objective deadlock. A legal turn or growth can fold
  the body into a non-terminal pose from which a remaining fruit or exit is
  unreachable despite other moves.
- `CON-061` — terminal required-object boundary escape. If the sole required
  snakebird falls beyond supported level space before exit, the attempt branch
  fails and recovery restores the previous safe state.
- Scarce strategic resources: free head cells, tail clearance, externally
  supported segments, reachable fruit order and enough final body shape to
  approach the exit head-first.
- Claim IDs: `SNB-001`, `SNB-003`, `SNB-005`–`SNB-007`, `SNB-010`.

### Information Genes

- `INF-001` — fully visible current state. Fixed terrain, remaining fruit,
  exit state and the position / order of every body segment are inspectable.
- Gravity and successor pose are deterministic; no hidden or random state is
  introduced in the scoped transition.
- Claim IDs: `SNB-011`, `SNB-012`.

### Objective Genes

- `OBJ-007` — clear declared board-element targets. Every fruit in the scoped
  board must be removed by head contact before the exit becomes usable. The
  definition is generalised from displayed quantities to a finite conjunction
  of visible target instances without changing Royal Match's signature.
- `OBJ-022` — evacuate every required controlled actor through fixed exits. The
  sole snakebird must enter the activated portal head-first; no actor loss is
  permitted.
- `OBJ-018` is absent: the required fruit set is a within-level gate, not a
  sequence of campaign stages whose token collection is itself final progress.
- Success is conjunctive: all fruit cleared and the required actor exited.
- Claim IDs: `SNB-004`, `SNB-008`, `SNB-009`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One directional input
  is followed by complete body propagation, growth, gate update, falling,
  death rollback or exit checks.
- `TIM-002` is absent under the exclusive boundary because automatic gravity
  and gate state changes are decision-relevant post-input system steps.
- `TIM-007` is absent: unlimited move undo restores discrete states; it does
  not scrub through continuously lived simulation history or expose an editable
  time axis.
- Claim IDs: `SNB-005`–`SNB-009`, `SNB-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Head destination is free and body remains supported | Move one cardinal cell | Head enters destination and every segment follows predecessor's old cell | ordered head-led propagation | `SNB-002` |
| Head destination contains an existing body segment or terrain | Move toward it | Input is rejected; body pose is unchanged | self and static occupancy block entry | `SNB-003` |
| Head enters a fruit cell | Complete the step | Fruit disappears and one persistent tail segment is added | contact acquisition plus geometric growth | `SNB-004` |
| At least one segment has fixed terrain directly below | Complete the step | Whole body remains at its new pose | support belongs to the complete articulated body | `SNB-006` |
| No segment has external support | Complete the step | Complete retained body shape falls vertically cell by cell | gravity is discrete post-input resolution | `SNB-005`, `SNB-006` |
| Falling body leaves supported level space | Resolve gravity | Snakebird dies and preceding safe state is restored | boundary loss is terminal but recoverable by rollback | `SNB-007` |
| Fruit remains and head reaches the exit cell | Attempt entry | Exit does not accept the snakebird | exhaustive collection gates exit | `SNB-008` |
| Final fruit is eaten | Complete the step | Exit becomes active before the next input | gate transition follows the last acquisition | `SNB-008` |
| No fruit remains and head enters exit | Complete the step | Sole snakebird exits and level completes | all targets plus all actors satisfy success | `SNB-009` |

## Strategic and experiential structure

- Local decision: choose a head cell that leaves the complete resulting body
  supported after propagation and any growth.
- Medium-term planning: order the two fruit so each extra segment improves
  reach without sealing the return path or creating self-collision.
- Long-term structure: transform body topology into a supported route that
  clears the fruit gate and still approaches the portal head-first.
- Common heuristics: reason from the tail as well as the head; treat each fruit
  as both progress and permanent geometry; maintain one externally supported
  segment; preview gravity after, not before, the body-follow transition.
- Failure attribution: lethal falling is immediate and automatically rolled
  back, while a softlock can originate several legal poses earlier when growth
  changed available turning clearance.
- Player-trust factors: segment-follow order, append location, support test,
  fall distance, exit-gate timing and undo restoration must be invariant.
- Claim IDs: `SNB-002`–`SNB-012`.

## Replay and variation

- What changes between puzzles: terrain, starting body pose / length, fruit,
  spikes, exits and later excluded snakebirds, blocks and paired portals.
- Randomness or procedural generation: none in scoped authored Level 1.
- Multiple viable strategies: local detours may vary, but fruit order and the
  supported approach to the exit strongly constrain useful poses.
- Typical replay motive: undo an unsupported or deadlocking pose, reverse fruit
  order or search for a shorter deterministic solution.
- Claim IDs: `SNB-001`, `SNB-007`, `SNB-010`–`SNB-012`.

## Adjacent systems and history

- A Good Snowman consumes snow and changes one ball through three bounded size
  states. Snakebird consumes fruit and adds a persistent collision / support
  cell, so `SYS-080` and `SYS-083` remain distinct.
- Sokoban shares fixed cells, exclusive occupancy, visible state and deadlock,
  but controls a one-cell keeper that pushes independent crates. Snakebird's
  commanded head repositions its own ordered body before gravity.
- Cut the Rope shares contact acquisition and required-object boundary loss,
  yet candy motion is continuous force integration. Snakebird resolves a
  complete discrete body pose and then applies cellwise falling.
- Portal shares direct navigation and an all-required-actors fixed-exit
  objective, but its portals transport continuously dynamic bodies and are
  placed in pairs. The scoped Snakebird exit is fixed and merely gated by fruit.
- Peg Solitaire shares deterministic turn resolution and soft deadlock, but
  monotonically removes pieces rather than growing navigable body geometry.
- Claim IDs: `SNB-002`–`SNB-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | head cell; cardinal grid step |
| System Behaviour | `SYS-037`, `SYS-082`, `SYS-083`, `SYS-084`, `SYS-085` | ordered follow; one-segment growth; rigid-shape fall; final-fruit gate |
| Constraint | `CON-001`, `CON-011`, `CON-013`, `CON-061` | finite cells; self-occupancy; softlock; abyss loss |
| Information | `INF-001` | visible segment order and gate state |
| Objective | `OBJ-007`, `OBJ-022` | clear all fruit, then exit sole actor |
| Time | `TIM-001` | input followed by complete deterministic resolution |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008; SYS-037,SYS-082,SYS-083,SYS-084,SYS-085;
  CON-001,CON-011,CON-013,CON-061; INF-001; OBJ-007,OBJ-022; TIM-001`.
- Indexed games scanned: all 44 prior records, `GAME-0001`–`GAME-0044`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0044`.
- Exact genome matches: none.
- Near matches and similarity scores: Stephen's Sausage Roll is the unique
  maximum at `7 / 21 = 0.333333`; Sokoban follows at
  `5 / 18 = 0.277778`; A Good Snowman is `5 / 19 = 0.263158`; Peg Solitaire
  is `4 / 20 = 0.200000`; Cut the Rope is `3 / 20 = 0.150000`; Portal is
  `3 / 24 = 0.125000`.
- Supported combination subsets: new `COMB-0045` only.
- Scan date: 2026-08-12.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0043` — Stephen's Sausage Roll | `ACT-008`, `CON-001`, `CON-011`, `CON-013`, `CON-061`, `INF-001`, `TIM-001` | one-cell fork agent and elongated cooking object versus one growing articulated controlled body under gravity | Unique near match, `0.333333` |
| `GAME-0006` — Sokoban | `ACT-008`, `CON-001`, `CON-011`, `CON-013`, `INF-001` | independent crate push and fixed goals versus self-body propagation, growth, gravity and fruit gate | Second, `0.277778` |
| `GAME-0044` — A Good Snowman Is Hard to Build | `ACT-008`, `CON-001`, `CON-013`, `INF-001`, `TIM-001` | bounded ball-size transform / stack assembly versus segment addition / exit gate | Controlled growth comparison, `0.263158` |
| `GAME-0019` — Peg Solitaire | `CON-001`, `CON-013`, `INF-001`, `TIM-001` | monotonic removal and exact final occupancy versus articulated growth and evacuation | Deterministic deadlock control, `0.200000` |
| `GAME-0021` — Cut the Rope | `SYS-037`, `CON-061`, `INF-001` | continuous candy dynamics and optional stars versus discrete body gravity and mandatory fruit | Physics / collection control, `0.150000` |
| `GAME-0033` — Portal | `ACT-008`, `INF-001`, `OBJ-022` | live portal placement and force-preserving traversal versus fixed collection-gated exit | Exit control, `0.125000` |

The complete numeric scan is: `GAME-0001` `3 / 25 = 0.120000`;
`GAME-0002` `2 / 19 = 0.105263`; `GAME-0003` `2 / 21 = 0.095238`;
`GAME-0004` `2 / 27 = 0.074074`; `GAME-0005` `2 / 19 = 0.105263`;
`GAME-0006` `5 / 18 = 0.277778`; `GAME-0007` `1 / 21 = 0.047619`;
`GAME-0008` `2 / 19 = 0.105263`; `GAME-0009` `4 / 26 = 0.153846`;
`GAME-0010` `3 / 20 = 0.150000`; `GAME-0011` `2 / 25 = 0.080000`;
`GAME-0012` `2 / 21 = 0.095238`; `GAME-0013` `3 / 24 = 0.125000`;
`GAME-0014` `3 / 26 = 0.115385`; `GAME-0015` `3 / 25 = 0.120000`;
`GAME-0016` `2 / 27 = 0.074074`; `GAME-0017` `1 / 26 = 0.038462`;
`GAME-0018` `1 / 32 = 0.031250`; `GAME-0019` `4 / 20 = 0.200000`;
`GAME-0020` `2 / 26 = 0.076923`; `GAME-0021` `3 / 20 = 0.150000`;
`GAME-0022` `1 / 25 = 0.040000`; `GAME-0023` `0 / 24 = 0.000000`;
`GAME-0024` `1 / 25 = 0.040000`; `GAME-0025` `1 / 24 = 0.041667`;
`GAME-0026` `1 / 25 = 0.040000`; `GAME-0027` `2 / 24 = 0.083333`;
`GAME-0028` `2 / 29 = 0.068966`; `GAME-0029` `3 / 23 = 0.130435`;
`GAME-0030` `1 / 27 = 0.037037`; `GAME-0031` `2 / 23 = 0.086957`;
`GAME-0032` `2 / 23 = 0.086957`; `GAME-0033` `3 / 24 = 0.125000`;
`GAME-0034` `3 / 25 = 0.120000`; `GAME-0035` `2 / 30 = 0.066667`;
`GAME-0036` `4 / 22 = 0.181818`; `GAME-0037` `2 / 21 = 0.095238`;
`GAME-0038` `3 / 27 = 0.111111`; `GAME-0039` `2 / 21 = 0.095238`;
`GAME-0040` `2 / 20 = 0.100000`; `GAME-0041` `3 / 22 = 0.136364`;
`GAME-0042` `1 / 22 = 0.045455`; `GAME-0043` `7 / 21 = 0.333333`;
`GAME-0044` `5 / 19 = 0.263158`.

- New genes: `SYS-082`, `SYS-083`, `SYS-084`, `SYS-085`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: the formal action-then-gravity transition separates
  articulated follow, geometry-adding growth, discrete fall and exhaustive-
  collection gate from every earlier continuous physics, bounded growth and
  final-arrangement rule.

## Combination record

- Registered `COMB-0045` — head-led growth, gravity and gated evacuation.
- No earlier analysed game contains its articulated propagation, persistent
  segment growth, post-input fall and exhaustive exit activation set.

## Taxonomy impact

- Registry changes: added `SYS-082`–`SYS-085`; added Snakebird evidence to
  `ACT-008`, `SYS-037`, `CON-001`, `CON-011`, `CON-013`, `CON-061`, `INF-001`,
  `OBJ-007`, `OBJ-022` and `TIM-001`.
- `OBJ-007` wording is generalised to visible target instances as well as
  displayed quantities; its removal / hit boundary and Royal Match signature
  remain unchanged.
- Taxonomy-change record: none; no earlier classification changes.
- Candidate terms affected: promoted head-led body propagation, consumable-
  contact segment growth, post-input rigid-shape fall and exhaustive-
  collection exit activation.

## Negative results

- `ACT-009`, `SYS-036`, `SYS-080`, `OBJ-018`, `TIM-002` and `TIM-007` are
  rejected by scoped transition counterexamples.
- No existing combination is a proper subset of the new genome; `COMB-0044`
  fails because the scoped level has no adjacent-object push action.
- No separate negative-result record is needed because no accepted distinction
  or concrete earlier hypothesis is overturned.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] One head step is followed by ordered body
  propagation and a separate support-triggered fall (`SNB-002`, `SNB-005`).
- [Confirmed | Corroborated | High] Each fruit adds one persistent segment and
  the final fruit activates the fixed exit (`SNB-004`, `SNB-008`).

## Нові гени

- [Observation | Corroborated | High] Added `SYS-082`, `SYS-083`, `SYS-084`
  and `SYS-085`; reused ten existing genes.

## Нові комбінації

- [Observation | Corroborated | High] Registered `COMB-0045`; no prior genome
  supports the full articulated-growth and gated-evacuation subset.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; `OBJ-007` gains
  a representation-neutral visible-instance example.

## Нові питання

- Should Hexcells Infinite be admitted directly as the retained deduction
  candidate, or should the now-exhausted two-game pool be refreshed first?
- Which later independent game can test `SYS-083` without also inheriting
  Snakebird's head-led body topology?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `TARGETED_REUSE_SELECTION_006`.
- Optimisation criterion: refresh a sourced candidate pool after Snakebird
  exhausts the physical-system candidate and leave exactly enough Goal units
  for one selected game and final audit.
- Expected information gain: compare Hexcells Infinite against at least four
  independent candidates targeting weak System, Constraint and Objective
  singletons before assigning `GAME-0046`.
- Backlog impact: retain Hexcells Infinite as the deduction benchmark.

## Чому саме вона

- [Hypothesis | Corroborated | High] The active Goal has three units after this
  one. A bounded selection now can choose one final high-information game and
  preserve unit 30 for the required final corpus validation.

## Sources consulted

- Noumenon Games' Steam page and Felix Eliasson's development history.
- Sturtevant et al.'s peer-reviewed formal Snakebird domain account.
- Apple, Thinky Games, Destructoid and Pocket Gamer mechanical descriptions.
- One early-level guide and one independent solver account for scope and edge
  corroboration only.
