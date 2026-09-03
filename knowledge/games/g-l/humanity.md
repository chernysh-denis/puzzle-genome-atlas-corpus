---
game_id: GAME-0029
slug: humanity
game_title: HUMANITY
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0029
gene_ids:
  action:
    - ACT-006
    - ACT-008
    - ACT-042
  system:
    - SYS-045
    - SYS-047
    - SYS-048
    - SYS-055
  constraint:
    - CON-001
    - CON-075
  information:
    - INF-001
  objective:
    - OBJ-019
  time:
    - TIM-003
---

# Game: HUMANITY

## Analysis scope

- Version / ruleset: the 2023 Story Mode, scoped to one ordinary early
  single-player trial after Turn and Jump are available and before finite-
  command, Start Switch, Others, weapon or Follow variants.
- Included: direct Shiba Inu traversal; placing, changing and removing
  persistent commands on the stage grid; a recurring stream from a gate;
  autonomous forward walking; contact-triggered turn / jump execution; terrain,
  pits and pushable-block interaction; goal filling by a sufficient flow;
  non-punitive human loss / recurrence; pause, free-camera stop, fast-forward
  and retry with kept or cleared commands.
- Excluded: Goldy collection, meta rewards, narrative, action / boss stages,
  Others and combat, Start Switch preplanning variants, finite command
  inventories, Follow mode, Stage Creator, user stages, VR presentation and
  cosmetic statistics.
- Direct-play status: not conducted. Official developer / publisher gameplay
  material and tips are combined with platform-holder explanation and
  contemporary reviews.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HUM-001` | The player directly traverses the three-dimensional trial as a Shiba Inu in order to reach command-placement positions | Confirmed | Corroborated | High | P1, S1, S2 |
| `HUM-002` | A command is placed persistently on a grid position rather than assigned to one selected human | Confirmed | Direct | High | P2, P4 |
| `HUM-003` | Every eligible human crossing the marker executes its direction or movement behaviour, so one command can affect a continuing stream | Confirmed | Direct | High | P2, P3 |
| `HUM-004` | Humans emerge successively from a gate and walk forward autonomously until terrain or a command changes their behaviour | Confirmed | Direct | High | P3, P4 |
| `HUM-005` | Early stages can supply a continuing population whose falls are not terminal failure; lost spirits recur and loss count is not held against completion | Confirmed | Direct | High | P2, P3 |
| `HUM-006` | The ordinary early-stage goal completes only after enough humans have entered the pillar of light | Confirmed | Direct | High | P2 |
| `HUM-007` | Placed commands remain world state across later walkers and can move with a pushable block on which they are attached | Confirmed | Direct | High | P2 |
| `HUM-008` | The player can stop or pause time to inspect and edit, accelerate execution, and retry while preserving or clearing the command field | Confirmed | Corroborated | High | P2, S1 |
| `HUM-009` | The current stage geometry, stream, commands, goal fill and available command types are visible before further intervention | Confirmed | Corroborated | High | P2, P4, S1 |
| `HUM-010` | The scoped stage has no finite per-command stock; later limited-command trials are a distinct variant and do not instantiate `CON-067` here | Confirmed | Corroborated | High | P2, S2, S3 |
| `HUM-011` | HUMANITY shares Lemmings' autonomous release / locomotion / terminal accounting / rescue objective motif but not its individual skill-assignment interaction | Confirmed | Corroborated | High | HUM-002–HUM-006 |

## Basic data

- Release / origin: tha ltd. developed HUMANITY and Enhance published it on
  16 May 2023.
- Platform or physical form: real-time, pauseable three-dimensional action-
  puzzle; the player navigates one dog while directing a large autonomous crowd
  through persistent spatial instructions.
- Puzzle family: world-instruction crowd routing and threshold rescue.
- Official sources:
  - **[P1]** [HUMANITY official site](https://humanity.game/), describing the
    dog issuing commands that make marching crowds turn, jump, float and climb
    toward pillars of light.
  - **[P2]** [Official HUMANITY tips collection](https://humanity.game/community_news/community-humanity-tips-digest),
    documenting grid command placement, contact execution, goal-fill threshold,
    recurring spirits, command-bearing pushable blocks, time stop and retry
    with retained / cleared commands.
  - **[P3]** [Xbox Wire publisher overview](https://news.xbox.com/en-us/2024/04/30/humanity-with-xbox-game-pass-may-30/),
    stating that a never-ending stream emerges from the gate, walks forward and
    follows ground commands toward the goal.
  - **[P4]** [Official Steam gameplay overview](https://store.steampowered.com/news/posts/?enddate=1682962033&feed=steam_community_announcements),
    describing ground commands followed by the marching horde.
- Contemporary corroboration:
  - **[S1]** [GameSpot review](https://www.gamespot.com/reviews/humanity-review-what-is-a-man/1900-6418071/),
    describing direct dog movement, persistent directional spaces, crowd
    physics, goal routing and fast-forward.
  - **[S2]** [Push Square review](https://www.pushsquare.com/reviews/ps5/humanity),
    distinguishing ordinary continuous-stream trials from finite-population,
    command-limited and preplanned variants.
  - **[S3]** [PC Gamer review](https://www.pcgamer.com/humanity-takes-the-idea-lemmings-but-with-people-and-turns-it-into-something-profound/),
    corroborating limited-command Start Switch stages as a later variant, not
    the scoped early grammar.
- Claim IDs: `HUM-001`–`HUM-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Local run and jump inputs directly
  move the Shiba Inu through the stage so it can reach command positions; the
  people are not navigated by the same action.
- `ACT-042` — place persistent traversal command. At the dog's current eligible
  grid position, the player selects a command and orientation, leaving a marker
  that can later be changed or cleared and that affects every eligible walker
  crossing it.
- `ACT-006` — accelerate automatic progression. Fast-forward raises the crowd
  simulation rate without changing commands, walking rules or goal threshold.
- `ACT-036` is absent: the player does not select one human and spend a role on
  it; the recipient relationship is deferred until any walker contacts the
  persistent marker.
- Claim IDs: `HUM-001`–`HUM-003`, `HUM-008`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. Released people march
  forward and interact with local geometry without step commands.
- `SYS-047` — time-scheduled population release. The gate supplies successive
  people at a recurring cadence; unlike Lemmings, the scoped stream is not a
  finite waiting population.
- `SYS-055` — contact-triggered persistent command execution. A walker entering
  the marked cell reads the command and automatically turns, jumps or performs
  its declared traversal behaviour; the marker remains for later walkers.
- `SYS-048` — terminal-zone population accounting. Entering the light goal
  removes and credits a human toward fill; a fall removes the current body but
  does not credit the goal and its spirit can recur from the stream.
- `SYS-046` is absent: command execution is caused by world-marker contact, not
  a role previously committed to the selected individual.
- Claim IDs: `HUM-003`–`HUM-007`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The authored trial exposes persistent
  addressed grid positions for terrain, goals, obstacles and commands.
- `CON-075` — avatar-local world-command placement. A command can be placed or
  edited only where the directly controlled dog can physically reach the
  eligible stage grid, making avatar access part of routing authority.
- The scoped early trial has no `CON-067`: commands are persistent reusable
  world instructions rather than a finite typed stock consumed per recipient.
- Scarce strategic resources: reachable command positions, unblocked flow
  lanes, goal throughput and time before a moving crowd reaches an unfinished
  section; population losses themselves are replenishable.
- Claim IDs: `HUM-001`, `HUM-002`, `HUM-007`, `HUM-010`.

### Information Genes

- `INF-001` — fully visible current state. Trial geometry, people, gate, goal
  fill, placed commands, pushable blocks and available command types are
  inspectable; free camera can stop motion for review.
- There is no hidden-state or future-randomness gene in the scoped deterministic
  trial.
- Claim IDs: `HUM-008`, `HUM-009`.

### Objective Genes

- `OBJ-019` — rescue minimum population quota through fixed exit. The goal
  fills only when a sufficient flow of autonomous people reaches its fixed
  light column; falls are tolerated because the recurring stream can still
  satisfy the threshold.
- Optional Goldy objectives are excluded rather than folded into the minimum
  ordinary human flow.
- Claim IDs: `HUM-005`, `HUM-006`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Population release,
  walking, command contact and falls continue while the player navigates and
  edits; pause / free camera stop and fast-forward alter the available planning
  rate without changing the running grammar.
- `TIM-006` is absent in the scoped live stage. Start Switch stages genuinely
  use a separate planning / execution structure, but are excluded variants.
- Claim IDs: `HUM-003`–`HUM-005`, `HUM-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Dog stands on an eligible empty grid position | Place an oriented Turn command | A persistent marker appears while the current crowd continues moving | command placement changes world state, not one selected agent | `HUM-001`, `HUM-002` |
| Several humans approach the same Turn marker at different times | Give no additional command | Every eligible crosser turns in the stored direction and continues walking | one world instruction is reusable across the stream | `HUM-003`, `HUM-007` |
| A Turn command is placed on a pushable block | Crowd pushes the block | The command moves with the block and remains executable at its new position | command identity is attached to world state rather than absolute UI overlay | `HUM-007` |
| Gate remains active | Wait | Successive humans enter and walk forward automatically | release cadence and locomotion are separate system behaviours | `HUM-004` |
| One human falls while later humans remain in the stream | Give no reset input | The body is lost without goal credit, but recurrence preserves future rescue capacity | scoped losses differ from a finite Lemmings population | `HUM-005` |
| Sufficient humans enter the light column | Give no further input | Goal fill reaches its threshold and the trial completes | reuses population-quota rescue despite an unbounded supply parameter | `HUM-006` |
| Command layout is nearly correct after a failed run | Choose Retry Keep Commands | Population state resets while the command field remains for further editing | persistent design can survive retry without becoming pre-run-only programming | `HUM-008` |
| Crowd route is stable | Activate fast-forward | All scheduled crowd processes advance faster under unchanged logic | speed control is not release-rate adjustment | `HUM-008` |

## Strategic and experiential structure

- Local decision: reach a cell as the dog and encode the direction or movement
  transformation needed by every later person arriving there.
- Medium-term planning: compose a persistent command path whose markers are
  encountered in the correct order, while keeping the dog ahead of the stream
  and accounting for movable obstacles.
- Long-term structure: establish enough stable throughput from the recurring
  gate to fill the goal despite tolerated falls and route experiments.
- Common heuristics: stop time to inspect downstream geometry, build backward
  from the goal, test one route segment, preserve working markers on retry and
  fast-forward only after the flow is stable.
- Failure attribution: failures normally trace to marker position / orientation,
  dog access, command order or obstacle state rather than selecting the wrong
  individual in a crowd.
- Player-trust factors: visible persistent commands and non-punitive recurring
  bodies support experimentation; crowd pressure can still create emergent
  deviations around blocks and edges.
- Claim IDs: `HUM-001`–`HUM-011`.

## Replay and variation

- What changes between sessions: selected authored trial, geometry, enabled
  command vocabulary, gates, goals, blocks and any variant rules.
- Randomness or procedural generation: none in the scoped trial grammar.
- Multiple viable strategies: some stages support different command routes,
  dog traversal paths, acceptable losses and timing of edits.
- Typical replay motive: refine a partial route, preserve more people, collect
  excluded Goldy or solve later variants with stricter toolsets.
- Claim IDs: `HUM-005`, `HUM-008`–`HUM-010`.

## Adjacent systems and history

- Lemmings is the strongest neighbour: both schedule autonomous population
  release, locomotion, terminal accounting and quota rescue in real time.
  Lemmings spends a finite skill on one selected agent; HUMANITY writes a
  reusable command into the world for every later crosser.
- Loop Hero also places persistent world conditions around autonomous motion,
  but its cards create future encounters for one fixed-route hero. HUMANITY
  places executable traversal instructions for a recurring rescue stream.
- World of Goo also rescues a quota, but the potential rescue population is
  directly consumed as elastic construction and then traverses that live
  structure. HUMANITY builds no force-bearing route.
- Claim IDs: `HUM-001`–`HUM-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-008`, `ACT-042` | fast-forward, dog navigation and persistent command placement |
| System Behaviour | `SYS-045`, `SYS-047`, `SYS-048`, `SYS-055` | walking, recurring release, goal / loss accounting and command execution |
| Constraint | `CON-001`, `CON-075` | fixed stage grid and avatar-local command authority |
| Information | `INF-001` | visible geometry, crowd, commands and goal fill |
| Objective | `OBJ-019` | sufficient crowd flow through fixed goal |
| Time | `TIM-003` | live editing with pause and acceleration |

Canonical signature:

`ACT-006,ACT-008,ACT-042; SYS-045,SYS-047,SYS-048,SYS-055; CON-001,CON-075; INF-001; OBJ-019; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `28` (`GAME-0001`–`GAME-0028`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`6 / 17 = 0.352941`).
- Supported combination subsets: `COMB-0029`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0025` — Lemmings | `SYS-045`, `SYS-047`, `SYS-048`, `INF-001`, `OBJ-019`, `TIM-003` | finite skill assignment to selected agents versus avatar-local persistent world commands and a recurring population | Near, `0.352941` |

### Preserved research notes

- New genes: `ACT-042`, `SYS-055`, `CON-075`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: acceleration, direct avatar navigation, autonomous
  locomotion, scheduled release, terminal accounting, fixed cells, visible
  state, quota rescue and live scheduling survive their prior boundaries.
  Persistent spatial command placement, contact execution and avatar-local
  authority do not.

## Combination record

- Registered [`COMB-0029`](../../combinations/COMB-0029.md), a nine-gene proper
  subset for avatar-authored persistent crowd instructions and rescue flow.
- Generic fixed capacity, current visibility and fast-forward remain in the full
  genome but are not required to identify the interaction.
- `COMB-0025` does not gain a second supporting game because its action,
  execution and finite-stock genes are deliberately Lemmings-specific; the six-
  gene shared rescue motif is now evidenced across two complete genomes.

## Taxonomy impact

- Registry changes: three stable genes added; nine existing genes reused.
- `SYS-047` is generalised from a finite waiting population to a finite or
  recurring supplied stream, with population extent retained as a parameter.
- `OBJ-019` is correspondingly generalised so tolerated non-credit exits need
  not reduce a finite maximum; the completion boundary remains a minimum quota
  through a fixed exit.
- Taxonomy-change record: none. The changes broaden evidenced parameters without
  merging, splitting or reclassifying an ID.
- Candidate terms affected: persistent traversal-command placement, contact-
  triggered persistent command execution and avatar-local world-command
  placement are promoted.

## Negative results

- `ACT-036`, `SYS-046` and `CON-067` are absent: no individual is selected as a
  skill recipient and no per-recipient finite skill unit is consumed.
- `SYS-050` is absent because the crowd follows authored terrain and persistent
  commands, not a live force-bearing structure toward extraction.
- `SYS-053` is absent because a command marker changes behaviour on contact; it
  does not generate encounter actors.
- `TIM-006` is absent from the scoped live trial; Start Switch stages are an
  excluded variant that would require their own signature.
- This disproves the working hypothesis that HUMANITY might support the whole
  `COMB-0025`; it supports only the six-gene release / rescue motif.
