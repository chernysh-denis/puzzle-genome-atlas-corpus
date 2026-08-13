---
game_id: GAME-0025
slug: lemmings
game_title: Lemmings
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0025
gene_ids:
  action:
    - ACT-036
    - ACT-037
  system:
    - SYS-045
    - SYS-046
    - SYS-047
    - SYS-048
  constraint:
    - CON-067
    - CON-068
  information:
    - INF-001
  objective:
    - OBJ-019
  time:
    - TIM-003
---

# Game: Lemmings

## Analysis scope

- Version / ruleset: one original 1991 single-player level under the classic
  eight-skill ruleset documented by Psygnosis for the Amiga, Atari ST and PC.
- Included: timed trapdoor release; autonomous walking, turning and falling;
  selection and assignment of Climber, Floater, Bomber, Blocker, Builder,
  Basher, Miner and Digger; persistent and immediate skill effects; terrain
  construction and destruction; lethal hazards; finite skill counts; release-
  rate adjustment; exit rescue; required rescue percentage; time limit; pause.
- Excluded: two-player competition, passwords, presentation, later-series
  skills, engine glitches, materially different port rules and level editors.
- Direct-play status: not conducted for this record. The original manual was
  extracted and visually inspected; creator history, a preserved artefact,
  secondary catalogue data and a formal rules paper provide corroboration.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LEM-001` | The player influences individual lemmings by assigning one of eight skills rather than issuing walking commands | Confirmed | Direct | High | F1, P1, M1, A1 |
| `LEM-002` | Released lemmings walk autonomously, turn at blocking terrain and otherwise continue into falls or hazards | Confirmed | Direct | High | F1, M1, S1 |
| `LEM-003` | Lemmings enter automatically through a trapdoor at a player-adjustable release rate | Confirmed | Direct | High | F1, M1 |
| `LEM-004` | Each level supplies a finite displayed count for each available skill | Confirmed | Direct | High | F1, M1, S1 |
| `LEM-005` | Assigned roles execute without continuous steering and can persist, build terrain, remove terrain, redirect peers or alter survival | Confirmed | Direct | High | F1, M1, A1 |
| `LEM-006` | Hazard or fatal-fall contact removes a lemming, while reaching the exit removes and credits it as rescued | Confirmed | Corroborated | High | F1, M1, S1 |
| `LEM-007` | A level requires a declared rescue percentage before its time expires | Confirmed | Direct | High | F1, M1, S1 |
| `LEM-008` | The interface discloses the current level, agents, skill stocks, rescued percentage and remaining time, with a whole-level micro-map | Confirmed | Direct | High | F1, M1 |
| `LEM-009` | The running population advances in real time while skill and release-rate inputs remain available; pause supplies planning time | Confirmed | Direct | High | F1, M1 |
| `LEM-010` | Within the scoped authored level, rules and starting resources are fixed rather than randomly generated | Observation | Corroborated | High | LEM-001–LEM-009, A1 |

## Basic data

- Release / origin: DMA Design developed Lemmings and Psygnosis published the
  original Amiga release in 1991; programmer Mike Dailly records a 14 February
  1991 launch.
- Platform or physical form: a real-time two-dimensional digital puzzle in
  which a cursor assigns roles to members of an autonomous population.
- Puzzle family: indirect multi-agent rescue and terrain transformation.
- Original rules:
  - **[F1]** [Psygnosis, *Lemmings* manual](https://www.dosdays.co.uk/media/games/lemmings/Lemmings%20-%20Manual.pdf),
    copyright 1991, documenting the game objective, controls, eight skills,
    finite counts, flow adjustment, micro-map, rescue display and time limit.
- Preserved physical artefact:
  - **[P1]** [The Strong National Museum of Play — *The Complete Lemmings Manual*](https://artsandculture.google.com/asset/video-game-instruction-book-lemmings-the-complete-lemmings-manual/gQEj5UWG3CUrLQ?hl=en),
    identifying the 1991 Psygnosis publication and skill-assignment premise.
- Creator history:
  - **[M1]** Mike Dailly,
    [“And then there was Lemmings (1991)”](https://lemmings.info/lemmings-1991/),
    a first-person DMA Design development history and release account.
- Secondary and formal corroboration:
  - **[S1]** [MobyGames — Lemmings](https://www.mobygames.com/game/683/lemmings/),
    catalogue description of skill assignment, saved count, rescue percentage
    and remaining time.
  - **[A1]** Giovanni Viglietta,
    [“Lemmings is PSPACE-complete”](https://arxiv.org/abs/1202.6581), a formal
    model of guiding agents through hazards by assigning behaviour-changing
    skills.
- Claim IDs: `LEM-001`–`LEM-010`.

## Mechanical decomposition

### Action Genes

- `ACT-036` — assign selected role to autonomous agent. The cursor commits the
  currently selected finite skill to one eligible lemming; it does not specify
  a destination or continuously steer the resulting behaviour.
- `ACT-037` — adjust automatic population-release rate. The minus and plus
  controls persistently change the cadence at which the trapdoor supplies
  agents without changing their locomotion speed.
- `ACT-019` is absent. Into the Breach targets an area with an ability owned by
  a directly controlled unit; Lemmings selects a population member as the
  recipient of a role whose execution is autonomous.
- Claim IDs: `LEM-001`, `LEM-003`–`LEM-005`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. A released Walker moves
  on the live simulation clock, turns when blocked, falls without support and
  enters hazards without awaiting another player command.
- `SYS-046` — assigned-role autonomous execution. A committed skill changes
  the agent state and then resolves its declared behaviour: persistent
  climbing or floating, blocking, a countdown and explosion, twelve-step
  bridge construction, or horizontal, diagonal or vertical excavation.
- `SYS-047` — time-scheduled population release. The trapdoor automatically
  introduces successive lemmings according to the current release rate.
- `SYS-048` — terminal-zone population accounting. A lemming that reaches the
  fixed exit is removed from the active level and increments the rescued
  population; lethal contact instead removes it without rescue credit.
- Role predicates and magnitudes such as suitable diggable material, twelve
  Builder bricks and persistent Athlete traits are parameters of `SYS-046`.
  Metal's resistance is level terrain data, not another player action.
- Claim IDs: `LEM-002`–`LEM-006`.

### Constraint Genes

- `CON-067` — finite typed role-assignment inventory. Each skill has its own
  displayed stock; an accepted assignment consumes the relevant type and zero
  stock prevents further use without itself ending the level.
- `CON-068` — fixed attempt deadline with terminal expiry. Remaining time
  decreases during the running level, and expiry ends the attempt if the
  required rescue state has not been reached.
- `CON-020` is absent. Exhausting one or every skill stock need not terminate
  the attempt; the level can continue until rescue, time expiry or population
  loss resolves it.
- Claim IDs: `LEM-004`, `LEM-007`, `LEM-009`.

### Information Genes

- `INF-001` — fully visible current state. The screen and whole-level micro-map
  expose current terrain and population location; the panel displays per-skill
  stock, current population, rescued percentage and remaining time.
- Future success depends on deterministic consequences of player timing and
  authored geometry, not an undisclosed random event.
- Claim IDs: `LEM-008`, `LEM-010`.

### Objective Genes

- `OBJ-019` — rescue minimum population quota through fixed exit. The pursued
  completion state is a level-specific percentage of the supplied population
  safely accounted for at the exit before time expires.
- `OBJ-014` is absent. Cut the Rope delivers one physical payload by changing
  its supports; Lemmings repeatedly rescues members of a role-assignable
  population and permits losses below the quota margin.
- Claim IDs: `LEM-006`, `LEM-007`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Walking, falling,
  role execution, hazards and scheduled release continue while the player
  selects agents and changes the release rate.
- Pause supplies planning time but does not turn the running level into a
  discrete-turn system.
- Claim IDs: `LEM-003`, `LEM-005`, `LEM-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Walker approaches open danger | No input | It continues walking and may fall or enter the hazard | locomotion is autonomous rather than command-per-step | `LEM-002` |
| Suitable lemming and skill stock are available | Select the skill and click that lemming | Stock decreases once and the selected role executes without steering | assignment and execution are distinct types | `LEM-001`, `LEM-004`, `LEM-005` |
| Builder places its twelfth brick | Do not reassign Builder | It returns to Walker; a second assignment can extend the bridge only if stock remains | role duration and stock are independent parameters | `LEM-004`, `LEM-005` |
| Trapdoor is releasing the remaining population | Increase release rate | Later lemmings enter at a shorter interval while current agents keep their speed | release cadence is not simulation acceleration | `LEM-003` |
| One lemming enters the exit and another hits a hazard | No second command | Both leave active play, but only the first increases the rescued percentage | terminal-zone accounting distinguishes rescue from loss | `LEM-006` |
| Quota has not been reached | Allow remaining time to reach zero | The attempt ends unsuccessfully even if agents or skills remain | deadline is distinct from inventory exhaustion | `LEM-007` |

## Strategic and experiential structure

- Local decision: identify the correct moving agent and commit a scarce role at
  the position and moment where its deterministic execution is useful.
- Medium-term planning: contain the crowd, create or remove traversable terrain
  and schedule specialists so later walkers inherit a safe route.
- Long-term structure: preserve enough population and typed skill stock to meet
  the rescue quota before the fixed deadline.
- Common heuristics: slow the initial release while constructing a route;
  isolate a worker with a Blocker; increase flow only after a safe path exists;
  treat irreversible excavation and Bomber use as route-shaping commitments.
- Failure attribution: outcomes normally trace to assignment choice, agent
  selection, timing, resource allocation or route geometry rather than chance.
- Player-trust factors: visible counts, deterministic skills and pause make
  crowded real-time failure inspectable, although selecting one overlapping
  moving agent can remain execution-sensitive.
- Claim IDs: `LEM-001`–`LEM-010`.

## Replay and variation

- What changes between sessions: the selected authored level, its population,
  release setting, skill allotment, terrain, quota and deadline.
- Randomness or procedural generation: none in the scoped level grammar.
- Multiple viable strategies: some levels admit different worker choices,
  release-rate schedules, routes or acceptable sacrifice counts, while tighter
  levels constrain them sharply.
- Typical replay motive: improve survival percentage or execution, recover
  from a failed assignment, or solve a harder authored level.
- Claim IDs: `LEM-004`, `LEM-007`, `LEM-010`.

## Adjacent systems and history

- Direct predecessors: no mechanical predecessor is asserted here; the creator
  history traces the project to DMA Design's experiments with tiny walking
  sprites before the rescue game was formed.
- Variants: later ports, sequels and two-player modes alter controls, skill sets
  or objectives and remain outside this signature.
- Similar games: Cut the Rope also uses real-time indirect intervention and a
  fixed receiver; Mini Metro also manages many automatically progressing units.
- Important differences: Lemmings assigns finite behavioural roles to
  individual autonomous walkers and alters traversable terrain to rescue a
  quota. Cut the Rope changes supports around one physics payload; Mini Metro
  edits reusable transport infrastructure around recurring demand.
- Claim IDs: `LEM-001`–`LEM-010`, M1.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-036`, `ACT-037` | role assignment and release-rate control |
| System Behaviour | `SYS-045`, `SYS-046`, `SYS-047`, `SYS-048` | walking, role execution, release and terminal accounting |
| Constraint | `CON-067`, `CON-068` | typed skill stock and deadline |
| Information | `INF-001` | visible terrain, population, stocks, quota and time |
| Objective | `OBJ-019` | minimum population rescue through exit |
| Time | `TIM-003` | live population progression with pause |

Canonical signature:

`ACT-036,ACT-037; SYS-045,SYS-046,SYS-047,SYS-048; CON-067,CON-068; INF-001; OBJ-019; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0024`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0024`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0002`: shared `INF-001`; `1 / 17 = 0.058824`.
  - `GAME-0003`: shared none; `0 / 20 = 0.000000`.
  - `GAME-0004`: shared `INF-001`, `TIM-003`; `2 / 24 = 0.083333`.
  - `GAME-0005`: shared `INF-001`; `1 / 17 = 0.058824`.
  - `GAME-0006`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0007`: shared `INF-001`; `1 / 18 = 0.055556`.
  - `GAME-0008`: shared `INF-001`; `1 / 17 = 0.058824`.
  - `GAME-0009`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0010`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0011`: shared `INF-001`; `1 / 23 = 0.043478`.
  - `GAME-0012`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0013`: shared `INF-001`; `1 / 23 = 0.043478`.
  - `GAME-0014`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0015`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0016`: shared `INF-001`, `TIM-003`; `2 / 24 = 0.083333`.
  - `GAME-0017`: shared none; `0 / 24 = 0.000000`.
  - `GAME-0018`: shared `INF-001`, `TIM-003`; `2 / 28 = 0.071429`.
  - `GAME-0019`: shared `INF-001`; `1 / 20 = 0.050000`.
  - `GAME-0020`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0021`: shared `INF-001`, `TIM-003`; `2 / 18 = 0.111111`.
  - `GAME-0022`: shared `INF-001`; `1 / 22 = 0.045455`.
  - `GAME-0023`: shared none; `0 / 21 = 0.000000`.
  - `GAME-0024`: shared `TIM-003`; `1 / 22 = 0.045455`.
- Mathematically selected near match: `GAME-0021` — Cut the Rope at
  `2 / 18 = 0.111111`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0021` — Cut the Rope | `INF-001`, `TIM-003` | Cut the Rope irreversibly severs supports around one continuously simulated payload and completes on one receiver contact; Lemmings repeatedly assigns finite typed roles to autonomous walkers, changes terrain and must rescue a population quota | Near match only |

- New genes: `ACT-036`, `ACT-037`, `SYS-045`, `SYS-046`, `SYS-047`,
  `SYS-048`, `CON-067`, `CON-068` and `OBJ-019`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: `INF-001` and `TIM-003` fit unchanged. Existing unit-
  ability targeting, general speed acceleration, single-payload delivery and
  terminal move-budget boundaries each fail a decision-relevant test.

## Combination record

- Registered [`COMB-0025`](../../combinations/COMB-0025.md), an eight-gene
  proper subset centred on finite role assignment to a live autonomous rescue
  population.
- Release-rate control, current-state visibility and the fixed deadline remain
  in the complete genome but are not required to identify this core grammar.

## Taxonomy impact

- Registry changes: nine stable genes added; `INF-001` and `TIM-003` reused.
- Taxonomy-change record: none. Commands, automatic transitions, limiting
  predicates, disclosed state, pursued quota and scheduling remain separable
  under the current six types.
- Candidate terms affected: autonomous-role assignment, release-rate control,
  autonomous locomotion, role execution, scheduled population release,
  terminal-zone population accounting, typed skill stock, attempt deadline and
  population rescue quota are promoted.

## Negative results

- `ACT-006` is absent because the release-rate controls persistently alter only
  future population-entry cadence and can decrease it; they do not temporarily
  accelerate the whole simulation.
- `ACT-019` is absent because the selected lemming receives a role and remains
  autonomous rather than acting as a directly controlled targeting unit.
- `CON-020` is absent because skill exhaustion does not itself end the level.
- `OBJ-014` is absent because the objective counts repeated population rescue,
  not one unchanged payload contacting a receiver.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Original Lemmings separates a player-issued role
  assignment from the selected agent's continuing autonomous execution
  (`LEM-001`–`LEM-005`).
- [Confirmed | Direct | High] Success couples finite typed skill stocks with a
  population rescue percentage and fixed level deadline (`LEM-004`, `LEM-007`).

## Нові гени

- [Observation | Direct | High] Added `ACT-036`, `ACT-037`, `SYS-045`,
  `SYS-046`, `SYS-047`, `SYS-048`, `CON-067`, `CON-068` and `OBJ-019`; reused
  `INF-001` and `TIM-003`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0025` captures finite role
  assignment to a concurrently progressing autonomous rescue population.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; the current six
  types represent assignment, execution, scarcity, quota and live scheduling
  without overlap.

## Нові питання

- Will another multi-agent puzzle reuse `ACT-036` while agents execute on
  discrete turns rather than `TIM-003`?
- Does a construction game reuse `CON-067` when finite typed stock is placed as
  persistent structure rather than assigned as an agent role?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0026` — World of Goo.
- Optimisation criterion: complete the 26-game horizon with load-bearing live-
  physics construction from finite structural inventory, then run the mandated
  full-corpus checkpoint.
- Expected information gain: distinguish direct structural placement from
  Lemmings role assignment and Cut the Rope support removal while testing
  continuous physics, recoverable inventory and delivery-quota boundaries.
- Backlog impact: promote World of Goo from the retained coverage pool; after
  its decomposition the next unit must be `CHECKPOINT_026`, not another game.

## Чому саме вона

- [Hypothesis | Limited | High] World of Goo is the remaining sourced distant
  candidate and tests constructive continuous physics at the exact checkpoint
  boundary without adding a close relative of Lemmings.
