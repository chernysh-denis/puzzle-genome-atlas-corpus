---
game_id: GAME-0031
slug: timelie
game_title: Timelie
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0031
gene_ids:
  action:
    - ACT-044
    - ACT-045
  system:
    - SYS-045
    - SYS-057
  constraint:
    - CON-076
    - CON-077
  information:
    - INF-001
    - INF-018
  objective:
    - OBJ-022
  time:
    - TIM-007
    - TIM-008
---

# Game: Timelie

## Analysis scope

- Version / ruleset: the 2020 base game, scoped to one ordinary single-player
  puzzle after both the girl and cat, timeline scrubbing, vents, meow and door
  interactions are available.
- Included: selecting either character; inserting, replacing or clearing
  timestamped destination / interaction commands; automatic path traversal;
  deterministic robot patrol; sight-triggered pursuit and capture; cat meow
  diversion; character-specific vents / keypads; leftward rewind; rightward
  exact future inspection; editing the past; alternate continuation; fixed exit.
- Excluded: story interpretation, cutscenes, collectibles, achievements,
  late-game special hazards and powers, Hell Loop DLC, mobile path-input
  differences and cosmetic presentation.
- Direct-play status: not conducted. Developer and platform-holder descriptions
  are combined with two contemporary hands-on reviews that document exact
  command insertion, timeline termination and revision transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TML-001` | The player selects the girl or cat and inserts destination or interaction commands at chosen timeline moments rather than steering either actor step by step | Confirmed | Corroborated | High | P1, P2, S2 |
| `TML-002` | Advancing the cursor automatically resolves queued character paths, robot patrols, doors and detection under deterministic rules | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| `TML-003` | The cursor can move right to reveal the exact future produced by the current command plan without requiring real-time commitment | Confirmed | Direct | High | P1–P3, S1 |
| `TML-004` | The cursor can move left to restore an earlier state, where commands can be cleared or changed before a replacement future is generated | Confirmed | Direct | High | P1–P3, S1 |
| `TML-005` | Robot sight triggers pursuit and capture, while an intentionally placed cat meow can divert a robot toward the stimulus | Confirmed | Corroborated | High | P2, S1, S2 |
| `TML-006` | Walls and facing bound visual detection; ordinary proximity without line of sight or an explicit meow does not alert a robot | Confirmed | Direct | High | S1 |
| `TML-007` | The girl and cat have complementary permissions: the cat uses vents and meows, while the girl operates keypads and repairs selected structures | Confirmed | Corroborated | High | S1, S2 |
| `TML-008` | If a required actor is captured, the visible future terminates there until the player rewinds and revises an earlier command | Confirmed | Corroborated | High | S1, S2 |
| `TML-009` | The scoped puzzle succeeds by bringing every required controlled actor to its fixed exit after coordinating their asymmetric routes | Confirmed | Corroborated | High | P1, S1, S2 |
| `TML-010` | Current geometry, actors, patrols, doors and commands are visible; future state is a separate exact simulation disclosure | Confirmed | Corroborated | High | P2, S1, S2 |
| `TML-011` | Timelie's editable random-access timeline is not a locked design/run phase and is not ordinary real-time intervention | Confirmed | Corroborated | High | TML-001–TML-004, TML-008 |

## Basic data

- Release / origin: Urnique Studio developed and published Timelie for PC on
  20 May 2020; the scoped rules were later published on Nintendo Switch.
- Platform or physical form: isometric deterministic stealth puzzle controlled
  through a random-access action timeline.
- Puzzle family: editable two-actor stealth timeline.
- Developer sources:
  - **[P1]** [Timelie official site](https://timelie.urniquestudio.com/),
    describing leftward rewind, rightward future seeking and simultaneous
    planning of both characters on the timeline.
  - **[P2]** [Urnique Studio press kit](https://www.urniquestudio.com/TH/games-press-kit/timelie),
    documenting parallel girl / cat action planning, future disaster preview,
    enemy avoidance and rewind after a mistake.
- Platform-holder source:
  - **[P3]** [Nintendo — Timelie](https://www.nintendo.com/au/games/nintendo-switch/timelie/),
    stating that dragging left undoes the past, dragging right unfolds the
    future and future information can be used to change earlier choices.
- Contemporary corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/timelie-review/),
    documenting command insertion / clearing at arbitrary timeline positions,
    exact patrol observation, capture-bounded future, meow diversion and doors.
  - **[S2]** [Game Informer review](https://gameinformer.com/review/timelie/timelie-review-making-every-second-count),
    describing maze exits, keypads, sight avoidance, vents, meow and coordinated
    two-character playback.
- Claim IDs: `TML-001`–`TML-011`.

## Mechanical decomposition

### Action Genes

- `ACT-045` — edit timestamped agent command. At the current cursor time, the
  player selects one actor and inserts, replaces or clears a destination or
  contextual interaction; the command remains in the plan until revised.
- `ACT-044` — rewind recent simulation history. Dragging the cursor left
  restores actors, robots, doors and command consequences to an earlier moment,
  where a different command can create an alternate continuation.
- `ACT-008` is absent: clicking a destination schedules automatic traversal
  across several positions rather than directly stepping an avatar through
  local movement inputs.
- `ACT-029` is absent: commands belong to situated actors at world times, not
  symbolic cycle slots on a persistent machine mechanism.
- Claim IDs: `TML-001`, `TML-003`, `TML-004`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. When time advances, the
  girl and cat traverse toward their scheduled destinations and robots traverse
  patrol or response paths without commands for individual movement steps.
- `SYS-057` — perception-triggered hostile pursuit or diversion. A robot that
  sees a required actor leaves ordinary patrol to chase and capture it; a cat
  meow can instead retarget an eligible robot toward the decoy stimulus.
- `SYS-020` and `SYS-051` are absent: robots neither resolve declared
  displacement vectors nor autonomously select combat attacks among nearby
  targets; their scoped consequence is route response and capture.
- Resolution order: current timestamp commands establish actor targets;
  characters and patrols advance; explicit interactions update doors or
  stimuli; detection changes hostile route; contact capture terminates the
  currently inspectable future.
- Claim IDs: `TML-002`, `TML-005`, `TML-008`.

### Constraint Genes

- `CON-076` — actor-specific traversal and interaction permissions. The cat can
  cross vents and create a meow stimulus but cannot use the girl's keypads;
  the girl operates required controls and selected repairs but cannot use the
  cat-only passages.
- `CON-077` — directed occlusion-bounded hostile perception. A robot detects an
  actor only inside its current directed sight region with an unobstructed
  line; walls and facing make route timing decision-relevant.
- Scarce strategic resources: safe visibility windows, separation between the
  two actor schedules, diversion duration, reachable interaction order and the
  finite timeline before every required actor exits.
- Claim IDs: `TML-005`–`TML-007`.

### Information Genes

- `INF-001` — fully visible current state. At the selected time the maze,
  characters, robots, doors, traversal permissions and current command state
  are inspectable.
- `INF-018` — exact scrubbed future-state preview. Moving right simulates the
  complete deterministic world generated by the present command schedule,
  including patrol, door, pursuit and capture outcomes, until failure or exit.
- `INF-017` is absent: the interface exposes full progressing world states, not
  only a drawn prospective route through physical routing devices.
- `INF-009` is absent: patrol futures are deterministic consequences the player
  inspects, not separately marked hostile actions committed before a tactical
  turn.
- Claim IDs: `TML-003`, `TML-008`, `TML-010`.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The scoped puzzle completes only after the girl and cat satisfy their exit
  requirements; one captured or stranded required actor cannot be discarded.
- `OBJ-019` is absent: there is no supplied autonomous population, tolerated
  loss or minimum quota below the complete required controlled set.
- Claim IDs: `TML-007`–`TML-009`.

### Time Genes

- `TIM-007` — branchable player-reversible simulation history. The player can
  restore a previously observed state, change a command and replace the future
  in which capture or blockage occurred.
- `TIM-008` — random-access editable deterministic action timeline. Past,
  present and prospective future share one cursor-addressed schedule in which
  actor commands can be inserted or removed before exact resolution is sought.
- `TIM-003` is absent because state need not progress while the player decides,
  and the player may inspect future time without live forced advancement.
- `TIM-006` is absent because command editing is available at arbitrary cursor
  moments; no separate locked automatic run must finish before redesign.
- `TIM-002` is absent because moving the time cursor resolves continuing patrol,
  path and detection processes rather than one self-contained discrete action.
- Claim IDs: `TML-001`–`TML-004`, `TML-008`, `TML-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Cursor rests before a patrol window | Select girl and click a later safe destination | A timestamped destination enters the plan; advancing time pathfinds the girl there while the robot patrols | remote command editing and automatic locomotion are distinct | `TML-001`, `TML-002` |
| Current plan approaches an unseen patrol conflict | Drag cursor right | Full actors, doors and robot states progress until the girl is captured | rightward seek exposes an exact outcome, not a route-only hint | `TML-003`, `TML-008` |
| Future ends at capture | Drag left to before the unsafe command, clear it and insert a wait / alternate destination | Earlier state is restored and the next rightward seek produces a different future | rewind is branchable and commands are cursor-addressed | `TML-004`, `TML-011` |
| Robot blocks the girl's required corridor | Schedule cat meow from a safe visible location | On hearing the stimulus, the eligible robot leaves its prior patrol route toward the cat | hostile route response can be deliberately diverted | `TML-005` |
| Cat stands beside a robot but outside its directed sight | Advance time without meowing | Robot remains on patrol until sight or an explicit stimulus occurs | ordinary proximity is not detection | `TML-006` |
| Girl and cat are separated by a vent / keypad arrangement | Send cat through vent; schedule girl to operate keypad at the coordinated time | Each actor performs only its permitted traversal or interaction and both routes become viable | asymmetric permissions create the coordination puzzle | `TML-007` |
| Girl reaches her exit while cat remains outside | Advance time | Puzzle remains incomplete until the cat reaches its required endpoint | success requires the full controlled set, not a quota | `TML-009` |

## Strategic and experiential structure

- Local decision: choose which actor receives a destination or interaction at
  one precise cursor time without entering a robot's directed sight.
- Medium-term planning: align cat diversions, vents, girl-only controls and door
  states so both scheduled routes remain safe as deterministic patrols advance.
- Long-term structure: construct and verify one complete joint timeline ending
  with every required actor evacuated.
- Common heuristics: scrub forward before committing to a corridor, work
  backward from fixed patrol windows, use meow only after the girl is positioned
  to exploit diversion, and revise the earliest command that causes failure.
- Failure attribution: exact future playback ties capture to a timestamped
  command, sight line or mistimed interaction rather than hidden randomness.
- Player-trust factors: free rewind removes repeated manual execution, while
  full future state makes deterministic patrol logic auditable; long-range
  early mistakes can still require substantial plan revision.
- Claim IDs: `TML-001`–`TML-011`.

## Replay and variation

- What changes between sessions: authored maze, patrol paths, door / vent
  layout, actor start / exit positions and available contextual interactions.
- Randomness or procedural generation: none in the scoped puzzle grammar.
- Multiple viable strategies: safe paths, diversion timing, actor order and the
  exact command schedule can differ where patrol windows overlap.
- Typical replay motive: optimise a plan, avoid unnecessary waits, inspect the
  final uninterrupted playback or solve excluded harder variants.
- Claim IDs: `TML-001`–`TML-004`, `TML-007`, `TML-009`.

## Adjacent systems and history

- Tin Hearts shares world-state rewind, automatic locomotion and branch
  replacement. It manipulates live physical routing objects around a population;
  Timelie edits commands for two controlled actors on one exact timeline.
- Opus Magnum shares editable command scheduling and deterministic execution,
  but locks edits during a separate machine run and resets after failure;
  Timelie allows random access and revision inside the simulated history.
- Into the Breach shares deterministic hostile consequences, but exposes one
  already committed action per enemy before a bounded turn instead of letting
  the player scrub full patrol futures.
- Braid remains an unanalysed adjacent control for rewind without a timestamped
  multi-actor command plan.
- Claim IDs: `TML-001`–`TML-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-044`, `ACT-045` | rewind and timestamped command editing |
| System Behaviour | `SYS-045`, `SYS-057` | automatic locomotion and perception response |
| Constraint | `CON-076`, `CON-077` | asymmetric permissions and directed sight |
| Information | `INF-001`, `INF-018` | current state and exact future simulation |
| Objective | `OBJ-022` | evacuate all required controlled actors |
| Time | `TIM-007`, `TIM-008` | branchable history and editable random-access timeline |

Canonical signature:

`ACT-044,ACT-045; SYS-045,SYS-057; CON-076,CON-077; INF-001,INF-018; OBJ-022; TIM-007,TIM-008`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `30` (`GAME-0001`–`GAME-0030`).
- Exact genome matches: none.
- Tied near matches: `GAME-0030` — Tin Hearts (`4 / 21 = 0.190476`).
- Supported combination subsets: `COMB-0031`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0030` — Tin Hearts | `ACT-044`, `SYS-045`, `INF-001`, `TIM-007` | physical devices redirect a released rescue troop in live time versus timestamped commands coordinating two capability-asymmetric actors through exact future inspection | Near, `0.190476` |

### Preserved research notes

- New genes: `ACT-045`, `SYS-057`, `CON-076`, `CON-077`, `INF-018`,
  `OBJ-022`, `TIM-008`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: rewind, automatic multi-step locomotion, current-state
  visibility and branch replacement reuse cleanly. Timestamped command editing,
  stimulus-responsive pursuit, asymmetric actor permissions, directed sight,
  exact future scrub, full-set evacuation and random-access plan time do not.

## Combination record

- Registered [`COMB-0031`](../../combinations/COMB-0031.md), a ten-gene proper
  subset for coordinating asymmetric actors against deterministic patrols on
  one editable reversible timeline.
- Generic current-state visibility remains in the complete genome but is not
  required to distinguish the interaction.
- No previous complete combination gains a second supporting game.

## Taxonomy impact

- Registry changes: seven stable genes added; four existing genes reused.
- Taxonomy-change record: none. `ACT-044` remains the rewind input and
  `TIM-007` the branch affordance; `TIM-008` adds random-access command editing
  rather than renaming either boundary.
- Candidate terms affected: timestamped actor-command editing, perception-
  triggered pursuit, actor-specific permissions, directed sight, exact future
  inspection, required-actor evacuation and editable plan time are promoted.

## Negative results

- `ACT-008` is rejected because actors automatically pathfind to remote
  destinations instead of receiving local traversal inputs.
- `ACT-006` and `TIM-003` are rejected because rightward seeking is random
  access to a simulated future, not merely faster forced live progression.
- `ACT-029` and `TIM-006` are rejected because there is no per-mechanism tape or
  locked execution phase; commands may be changed at arbitrary cursor times.
- `SYS-020`, `SYS-051` and `INF-009` are rejected because robots pursue and
  capture through perception rather than resolving a committed attack intent.
- `INF-017` is rejected because Timelie displays exact evolving world states,
  not only a prospective route line.
- The selection hypothesis that future seeking might be only informational is
  rejected: source transitions show one editable schedule whose exact resolved
  future changes after a past command is revised.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Timelie lets the player insert or clear commands
  at arbitrary timeline moments, scrub their exact deterministic outcome and
  revise the past after a captured future (`TML-001`–`TML-004`, `TML-008`).
- [Confirmed | Corroborated | High] Girl / cat permission asymmetry and robot
  sight / meow responses make coordination structural rather than cosmetic
  (`TML-005`–`TML-009`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-045`, `SYS-057`, `CON-076`,
  `CON-077`, `INF-018`, `OBJ-022` and `TIM-008`; reused four existing genes.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0031` captures editable reversible-
  timeline coordination of capability-asymmetric actors under hostile patrol.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; random-access plan
  editing is added beside, not substituted for, branchable rewind.

## Нові питання

- Does Braid reuse `TIM-007` without `TIM-008`, confirming that branchable
  rewind and timestamped plan editing remain separable?
- Can an existing machine-programming game support a proper subset of
  `COMB-0022` without inheriting Opus Magnum's spatial glyph grammar?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `GAME-0032` — SpaceChem.
- Optimisation criterion: test cross-game combination reuse after two
  consecutive reversible-time analyses.
- Expected information gain: challenge Opus Magnum's command-tape,
  deterministic execution, collision and exact-output boundaries in a related
  but independently scoped reactor grammar.
- Backlog impact: promote retained SpaceChem; keep Braid, Portal and Pikmin 4.

## Чому саме вона

- [Hypothesis | Corroborated | High] SpaceChem was the strongest retained
  non-time candidate and prevents the corpus from overfitting immediately to a
  third rewind game while directly addressing zero full combination recurrence.
