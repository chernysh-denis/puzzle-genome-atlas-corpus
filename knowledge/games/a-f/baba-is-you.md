---
game_id: GAME-0013
slug: baba-is-you
game_title: Baba Is You
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0013
gene_ids:
  action:
    - ACT-009
    - ACT-017
    - ACT-018
  system:
    - SYS-017
    - SYS-018
  constraint:
    - CON-001
    - CON-031
    - CON-032
    - CON-033
  information:
    - INF-001
    - INF-008
  objective:
    - OBJ-010
  time:
    - TIM-001
---

# Game: Baba Is You

## Analysis scope

- Version / ruleset: the introductory deterministic fragment of the current
  commercial Baba Is You rules, limited to noun, `IS`, `YOU`, `PUSH`, `STOP`
  and `WIN` word blocks on a bounded orthogonal level grid.
- Included: directional input; zero, one or multiple `YOU` objects; ordinary
  single-object and chain pushing; intrinsically movable word blocks; horizontal
  and vertical rule formation; automatic rule parsing; dynamic reassignment of
  `YOU`, `PUSH`, `STOP` and `WIN`; winning through `YOU` / `WIN` overlap.
- Excluded: undo, restart and wait as interface commands; noun-to-noun object
  transformation; `MOVE`, `SHIFT`, `SINK`, `DEFEAT`, `OPEN`, `SHUT`, `HAS`,
  `MAKE`, `NOT`, `AND`, conditions and other extended vocabulary; randomness;
  overworld manipulation, late-game meta systems, editor and custom levels.
- Direct-play status: not conducted for this record. The fragment is grounded
  in the developer's product description and peer-reviewed mechanical accounts.
  It is not claimed to encode every level or current editor word.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BABA-001` | Rules exist as word objects inside the bounded level and can be pushed to change mechanics | Confirmed | Corroborated | High | D1, A1, A2 |
| `BABA-002` | Text is parsed left-to-right or top-to-bottom into syntactically valid active rules | Confirmed | Corroborated | High | A1, A2 |
| `BABA-003` | `NOUN IS PROPERTY` applies that property to all objects of the noun class while the rule remains active | Confirmed | Corroborated | High | A1, A2 |
| `BABA-004` | Objects assigned `YOU` receive player input, and there may be zero or multiple controlled objects | Confirmed | Direct | High | A1 |
| `BABA-005` | `PUSH` permits displacement when another moving object enters, while `STOP` prevents entry | Confirmed | Direct | High | A1 |
| `BABA-006` | A contiguous chain of pushable objects can be shifted when space and downstream interactions allow it | Confirmed | Corroborated | High | A1, S1 |
| `BABA-007` | Moving one word out of a sentence removes the corresponding property assignment after rules are recalculated | Confirmed | Corroborated | High | A2, S1 |
| `BABA-008` | The player wins when a `YOU` object shares a cell with a `WIN` object | Confirmed | Direct | High | A1 |
| `BABA-009` | Breaking every `YOU` rule can leave no object responsive to directional input without itself creating a formal loss state | Observation | Corroborated | Medium | A1, A2 |
| `BABA-010` | All scoped objects, word syntax and active mechanical consequences are public and deterministic | Observation | Corroborated | High | BABA-001–BABA-009 |
| `BABA-011` | Parsing and property enactment are separate automatic roles even when they occur in one resolution phase | Observation | Corroborated | Medium | BABA-002, BABA-003, BABA-007 |
| `BABA-012` | Rules-as-objects fit the six-type model as an interaction across Action, System, Constraint, Information and Objective | Observation | Corroborated | Medium | BABA-001–BABA-011 |

## Basic data

- Release / origin: created by Arvi Teikari / Hempuli Oy, originating as the
  winning Nordic Game Jam 2017 entry and commercially released in 2019.
- Platform or physical form: digital grid puzzle for desktop, console and
  mobile platforms.
- Puzzle family: rule-manipulation block-pushing puzzle.
- Developer source:
  - **[D1]** [official Steam product page](https://store.steampowered.com/app/736260/Baba_Is_You/),
    identifying rules as interactive level blocks whose manipulation changes
    mechanics, transforms objects and can change the goal.
- Primary mechanical source:
  - **[A1]** Abel and Hendrickson,
    [“Baba Is Universal”](https://doi.org/10.4230/LIPIcs.FUN.2024.1),
    a peer-reviewed account defining player control, pushing, left-to-right and
    top-to-bottom rules, `YOU`, `WIN`, `STOP` and `PUSH` semantics.
- Corroborating research:
  - **[A2]** Cloos et al.,
    [“Baba Is AI: Break the Rules to Beat the Benchmark”](https://arxiv.org/abs/2407.13729),
    demonstrating active aligned rules, breaking and constructing sentences,
    dynamic walls, control reassignment and rule-defined winning objects.
- Input / timing corroboration:
  - **[S1]** [community manual](https://steamcommunity.com/sharedfiles/filedetails/?id=2725290821),
    used only for chain-push and end-of-turn recalculation edge cases.
- Claim IDs: `BABA-001`–`BABA-012`.

## Mechanical decomposition

### Action Genes

- `ACT-009` — push one adjacent movable object. A directional input into one
  word or `PUSH` object displaces it one cell when the destination accepts it.
- `ACT-017` — directionally step all rule-controlled objects. One orthogonal
  input is applied to every current instance whose class bears `YOU`; the set
  may change after any rule edit.
- `ACT-018` — push a contiguous movable chain. The same directional command can
  propagate through multiple adjacent word or `PUSH` objects and shift the
  whole chain by one cell.
- Rule editing is not a separate direct command: the player edits syntax by
  moving or pushing the word objects with these spatial Actions.
- Undo and restart are excluded interface actions.
- Claim IDs: `BABA-001`, `BABA-004`–`BABA-007`.

### System Behaviour Genes

- `SYS-017` — spatial text-rule parsing. After movement, aligned words are read
  horizontally or vertically; valid sentences enter the active rule set and
  broken sentences leave it.
- `SYS-018` — active-rule property rebinding. The system automatically applies
  or withdraws `YOU`, `PUSH`, `STOP` and `WIN` from every matching noun object
  under the newly parsed rules.
- Parsing answers which sentences are active. Rebinding answers what those
  active sentences do to object roles; keeping them separate prevents grammar
  from becoming one giant behaviour gene.
- Noun-to-noun transformation and automatic `MOVE` are excluded, so no generic
  transformation or autonomous-movement gene is admitted here.
- Claim IDs: `BABA-002`, `BABA-003`, `BABA-007`, `BABA-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The scoped level retains a finite set
  of individually addressed grid cells.
- `CON-031` — rule-assigned simultaneous controllability. Only current `YOU`
  classes receive player direction, and every current instance is eligible.
- `CON-032` — property-conditioned movement blocking. A `STOP` object blocks
  entry while its rule is active; without the property, objects may share its
  cell under the remaining interaction rules.
- `CON-033` — contiguous push-chain free-end requirement. A chain of text or
  `PUSH` objects moves only when every member can shift and the far destination
  accepts the last member.
- `CON-011` and `CON-012` are absent. Baba Is You lacks universal exclusive
  occupancy and static barriers, while its chain pushes exceed Sokoban's
  one-object, fixed-rule access boundary.
- Object count, board size, word vocabulary and number of simultaneous `YOU`
  instances are parameters.
- Claim IDs: `BABA-004`–`BABA-007`.

### Information Genes

- `INF-001` — fully visible current state. All scoped objects, text positions,
  overlaps and active sentence layouts are inspectable before the next input.
- `INF-008` — visible executable rule syntax. Word positions are both board
  state and an explicit disclosure of the rules currently being parsed.
- The player must interpret consequences, but no scoped property is hidden and
  no future random selection occurs.
- An absent rule is meaningful information: `WALL` objects are not blocking
  merely because their appearance resembles a wall.
- Claim IDs: `BABA-001`–`BABA-003`, `BABA-010`.

### Objective Genes

- `OBJ-010` — overlap controlled and rule-defined goal objects. The level ends
  successfully when an object currently bearing `YOU` occupies a cell with an
  object currently bearing `WIN`.
- The object class serving as goal can change when word alignment changes;
  reaching a visually flag-like object is insufficient without an active
  `FLAG IS WIN` rule.
- Creating a `WIN` rule alone is not completion; the required overlap still has
  to occur. An object may bear both properties and satisfy the condition in its
  own cell.
- Claim IDs: `BABA-003`, `BABA-008`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One direction produces
  the movement / push attempt, after which text is reparsed, properties are
  rebound and victory is evaluated before the next decision.
- With automatic `MOVE` excluded, no state changes merely because real time
  passes. The game remains self-paced between fully resolved inputs, but the
  explicit automatic rule phase makes `TIM-001` the operative scheduling gene.
- Claim IDs: `BABA-002`, `BABA-003`, `BABA-007`, `BABA-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| `BABA IS YOU` is active and one Baba exists | Press right | Baba attempts one rightward step | Rule-assigned control | `BABA-004` |
| Two Baba objects exist under `BABA IS YOU` | Press up | Both attempt the same up step | One input can control multiple objects | `BABA-004` |
| `WALL IS STOP` is active | Attempt to enter a wall cell | Movement is blocked | Blocking comes from active property | `BABA-005` |
| Push `STOP` out of `WALL IS STOP` | Move the word one cell out of line | Parser removes the rule and walls lose `STOP` | Parsing and property withdrawal | `BABA-007` |
| Two aligned text blocks stand before an open cell | Push the chain toward the open cell | Both text blocks shift one cell | Chain push differs from Sokoban boundary | `BABA-006` |
| Replace `BABA IS YOU` with `ROCK IS YOU` | Complete the new alignment | Rocks receive later directional input; Baba no longer does | Controllability is mutable | `BABA-003`, `BABA-004` |
| `FLAG IS WIN` and `BABA IS YOU` are active | Move Baba onto a flag | Level completes | Rule-defined contact objective | `BABA-008` |
| Push `YOU` out of the only control sentence | Complete that move | No object receives later directions; no separate loss event fires | Soft loss of agency, not terminal hazard | `BABA-009` |

## Strategic and experiential structure

- Local decision: predict one step, any push chain and the complete rule set
  that will exist after word movement.
- Medium-term planning: preserve controllability while opening space to break
  obstructive rules or assemble useful `YOU`, `PUSH`, `STOP` and `WIN`
  assignments.
- Long-term structure: transform the reachable interaction model itself so a
  controlled class can overlap a current winning class.
- Common heuristics: read every horizontal and vertical sentence after each
  edit; distinguish word blocks from the objects they name; avoid pushing a
  needed word against an unrecoverable edge; look for alternative noun subjects
  when the apparent avatar or goal is inaccessible.
- Failure attribution: a spatially legal push may delete control, make a
  blocker active or strand a required word. The outcome is deterministic but
  depends on both physical and syntactic state.
- Player-trust factors: rules must be visibly and consistently parsed. The
  central promise is that word arrangement, not object appearance, governs the
  scoped properties.
- Claim IDs: `BABA-001`–`BABA-011`.

## Replay and variation

- What changes between levels: object classes, grid geometry, word inventory,
  initial active sentences and which rules can be physically edited.
- Randomness or procedural generation: none in the scoped fragment.
- Multiple viable strategies: a level may support different rule constructions
  or controlled classes leading to the same `YOU` / `WIN` overlap.
- Typical replay motive: recover from a loss of agency, find another rule edit
  order or discover an alternative interpretation of the same word inventory.
- Claim IDs: `BABA-001`, `BABA-009`, `BABA-010`.

## Adjacent systems and history

- Baba Is You began as a Nordic Game Jam 2017 project and became a commercial
  release in 2019; this record does not claim the introductory fragment covers
  the hundreds of later levels or editor vocabulary.
- Sokoban shares body-mediated pushing and spatial deadlock pressure, but its
  walls, avatar, crates and goals do not change roles when text moves.
- Rule-programming puzzle games may expose commands or automation without
  making their grammar movable board occupancy; those require a separate
  comparison to `INF-008` and `SYS-017`.
- The formal universality and undecidability literature depends on extended or
  generalised mechanics. Those complexity results demonstrate expressive power
  but do not establish the difficulty of each finite introductory level.
- Claim IDs: `BABA-001`–`BABA-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-009`, `ACT-017`, `ACT-018` | direction set, controlled count and push-chain length |
| System Behaviour | `SYS-017`, `SYS-018` | grammar and property vocabulary |
| Constraint | `CON-001`, `CON-031`, `CON-032`, `CON-033` | grid size, word placement and simultaneous movement |
| Information | `INF-001`, `INF-008` | visible active-rule presentation |
| Objective | `OBJ-010` | current `YOU` and `WIN` subject classes |
| Time | `TIM-001` | movement then rule recalculation |

Canonical signature:

`ACT-009,ACT-017,ACT-018; SYS-017,SYS-018; CON-001,CON-031,CON-032,CON-033; INF-001,INF-008; OBJ-010; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `12` (`GAME-0001`–`GAME-0012`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`3 / 19 = 0.157895`); `GAME-0010` — Water Sort (`3 / 19 = 0.157895`).
- Supported combination subsets: `COMB-0013`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0006` — Sokoban | `ACT-009`, `CON-001`, `INF-001` | Both use visible body-mediated pushing on a fixed grid; Sokoban has one persistent agent and static walls / goals, while Baba dynamically reassigns control, collision and victory through text | Near, `0.157895` |
| `GAME-0010` — Water Sort | `CON-001`, `INF-001`, `TIM-001` | Both resolve deterministic commands on visible fixed capacity; Water Sort has stable pour rules, while Baba reparses player-moved syntax and changes the mechanics themselves | Near, `0.157895` |

### Preserved research notes

- New combination: `COMB-0013`, whose eight genes are a proper subset of this
  thirteen-gene genome.
- New genes: `ACT-017`, `ACT-018`, `SYS-017`, `SYS-018`, `CON-031`,
  `CON-032`, `CON-033`, `INF-008`, `OBJ-010`.
- Classification result: `New gene`.
- Reused genes: `ACT-009`, `CON-001`, `INF-001`, `TIM-001`.
- Evidence and reasoning: rules-as-objects is not one indivisible gene. It is a
  verified interaction among spatial Actions, automatic parsing and enactment,
  property-dependent Constraints, visible syntax and a mutable goal relation.

## Taxonomy impact

- Registry changes: nine bounded genes added and four reused.
- Taxonomy-change record: none. Each observed role has a clean home in the six
  existing types; the unusual structure lies in their interaction.
- Candidate terms affected: move rules, rule parsing, property rebinding,
  dynamic controllability, conditional blocking, chain pushing, executable
  syntax and rule-defined goals now have bounded mappings.
- Word vocabulary, simultaneous controlled count, sentence count and exact
  grammar remain parameters of the admitted genes.
- Claim IDs: `BABA-011`, `BABA-012`.

## Negative results

The scoped game does not reuse `ACT-008` because control can move between noun
classes and apply to multiple objects. It does not reuse Sokoban's `CON-011` or
`CON-012` because overlap and blocking are property-dependent and chains can be
pushed. A visually flag-like object is not an `OBJ-004` fixed target: `WIN` can
be reassigned during play.
