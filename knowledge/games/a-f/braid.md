---
game_id: GAME-0034
slug: braid
game_title: Braid, Anniversary Edition
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0034
  - COMB-0041
gene_ids:
  action:
    - ACT-008
    - ACT-044
    - ACT-049
  system:
    - SYS-037
    - SYS-045
    - SYS-062
    - SYS-063
    - SYS-064
    - SYS-065
  constraint: []
  information:
    - INF-001
    - INF-020
  objective:
    - OBJ-018
  time:
    - TIM-003
    - TIM-007
---

# Game: Braid, Anniversary Edition

## Analysis scope

- Version / ruleset: the Anniversary Edition's unchanged original base-game
  rules, scoped to ordinary World 3, “Time and Mystery”, after unrestricted
  rewind and green time immunity have been introduced.
- Included: direct running and jumping; monstar locomotion and directional
  contact; death pause and rewind; ordinary world-state restoration; green
  keys, doors, switches, enemies or platforms continuing in forward time;
  visible green affinity; key carrying and gate opening; lever-controlled
  platforms; required puzzle-piece acquisition.
- Excluded: story interpretation, commentary world, Anniversary-only puzzle
  world, World 4 position-linked time, World 5 shadow replay, World 6 time
  dilation / direction, epilogue, hidden stars, speedrunning and platform-
  specific presentation.
- Direct-play status: not conducted. Creator / publisher descriptions and the
  creator's rewind implementation talk are combined with contemporary reviews
  and a narrow World 3 transition reference. Exact collision-frame tolerances
  remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BRD-001` | Tim is directly controlled through local two-dimensional running and jumping | Confirmed | Corroborated | High | P2, P3, S1, S3 |
| `BRD-002` | Holding rewind restores Tim and ordinary world entities through previously lived states, can continue after death and has no ordinary consumable limit | Confirmed | Direct | High | P2, P4, S1, S2, S3 |
| `BRD-003` | Releasing rewind at an earlier state permits different movement and replaces the previously observed continuation | Confirmed | Corroborated | High | P2, P4, BRD-002 |
| `BRD-004` | Green-glowing entities are exempt from rewind and continue their own forward-time evolution while ordinary entities move backward | Confirmed | Direct | High | P2, S1, S4, R1 |
| `BRD-005` | A green key can remain with Tim while he rewinds out of an otherwise inescapable route, and a green door remains open when ordinary history rewinds before its opening | Confirmed | Corroborated | High | S1, S4, R1 |
| `BRD-006` | Green glow discloses temporal affinity before the player activates rewind | Confirmed | Direct | High | S2, S4, R1 |
| `BRD-007` | Monstars walk automatically; top contact defeats one and rebounds Tim, while unsafe contact pauses at Tim's defeat for rewind | Confirmed | Corroborated | High | P3, S2, S3, R1 |
| `BRD-008` | Contact transfers a key into carried state and contact with its locked gate consumes the key while opening passage | Confirmed | Corroborated | High | S1, S4, R1 |
| `BRD-009` | Reachable levers start or reverse linked moving platforms whose positions evolve with their own temporal affinity | Confirmed | Corroborated | High | S4, R1 |
| `BRD-010` | Required jigsaw pieces are acquired by contact and form the finite progression set across authored stages | Confirmed | Corroborated | High | P3, S1, S2 |
| `BRD-011` | Ordinary movement, enemies and platforms progress in real time, while rewind itself directly drives retained history backward | Confirmed | Corroborated | High | P2, P4, S2 |
| `BRD-012` | Braid has no random-access future cursor or timestamped command plan: only already-lived history is rewound and new local play creates the replacement branch | Confirmed | Corroborated | High | P4, BRD-001–BRD-004 |

## Basic data

- Release / origin: Number None released the original Braid on Xbox 360 in
  2008; Thekla released Braid, Anniversary Edition in 2024 while explicitly
  preserving the original game's fundamentals.
- Platform or physical form: two-dimensional real-time puzzle platformer with
  player-driven reversible simulation history.
- Puzzle family: rewind platforming with entity-specific temporal affinity.
- Creator and official sources:
  - **[P1]** [Braid, Anniversary Edition official site](https://braid-game.com/),
    where Jonathan Blow states that the remaster preserves the original game's
    fundamentals and separates added commentary / puzzle content.
  - **[P2]** [Number None — Braid on Steam](https://store.steampowered.com/app/26800/Braid/),
    describing unrestricted rewind, rewind-immune objects, no conventional
    death / loss and puzzle-piece progression.
  - **[P3]** [PlayStation — Braid, Anniversary Edition](https://www.playstation.com/en-us/games/braid-anniversary-edition/),
    documenting running / jumping, stomping enemies, multiple rewind variants
    and jigsaw-piece assembly.
  - **[P4]** [Jonathan Blow — The Implementation of Rewind in Braid](https://www.youtube.com/watch?v=8dinUbg2h70),
    the creator's GDC technical and design account of retained reversible state.
- Contemporary corroboration:
  - **[S1]** [GameSpot review, 2008](https://www.gamespot.com/reviews/braid-review/1900-6195623/),
    documenting green doors that remain open through rewind, keys and required
    puzzle pieces.
  - **[S2]** [Destructoid review, 2008](https://www.destructoid.com/reviews/destructoid-review-braid/),
    describing death recovery, green time-immune objects and finite jigsaw-
    piece collection.
  - **[S3]** [Wired review, 2008](https://www.wired.com/2008/08/review-braid-in/),
    corroborating platform movement, death pause and rewind recovery.
  - **[S4]** [Den of Geek review, 2008](https://www.denofgeek.com/games/braid-xbox-360-review/),
    documenting green keys, switches, doors and enemies plus the fall / key /
    rewind transition.
- Narrow transition reference:
  - **[R1]** [StrategyWiki — World 3: Time and Mystery](https://strategywiki.org/wiki/Braid/World_3%3A_Time_and_Mystery),
    used only to corroborate ordinary World 3 key transfer, lever, platform,
    monstar and piece-access sequences.
- Claim IDs: `BRD-001`–`BRD-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player directly runs and jumps
  Tim through local platform geometry rather than selecting destinations.
- `ACT-044` — rewind recent simulation history. Holding rewind traverses
  retained lived states backward; stopping earlier and moving differently
  creates a replacement continuation.
- `ACT-049` — toggle reachable world switch. Tim activates a nearby lever to
  start, stop or reverse a linked platform's authored motion.
- `ACT-045` is absent: the player never inserts commands at selected timeline
  timestamps. Rewind changes the current state, after which ordinary local
  input resumes.
- Claim IDs: `BRD-001`–`BRD-003`, `BRD-009`, `BRD-012`.

### System Behaviour Genes

- `SYS-037` — contact-triggered collectible acquisition. Tim touching a
  required jigsaw piece marks it acquired for the finite progression set.
- `SYS-045` — continuous autonomous agent locomotion. Monstars walk under
  authored ground and collision rules without a command for each step.
- `SYS-062` — rewind-exempt forward-time evolution. A green entity retains its
  state or continues forward while Tim and ordinary entities restore backward.
- `SYS-063` — carried-key barrier consumption. Contact gives Tim a key; contact
  with its gate consumes the carried key and opens the barrier, subject to each
  entity's rewind affinity.
- `SYS-064` — direction-sensitive avatar-enemy contact resolution. A top stomp
  removes the monstar and rebounds Tim; unsafe contact defeats Tim and waits for
  rewind.
- `SYS-065` — switch-directed platform traversal. Lever state directs a moving
  platform along a fixed path while its applicable time direction advances.
- Resolution order: local avatar and autonomous motion advance; collisions
  resolve support, stomp / defeat, key transfer, gate opening or piece contact;
  switch state directs linked platform travel. During rewind, ordinary entities
  load earlier states while `SYS-062` entities continue their own direction.
- Claim IDs: `BRD-004`, `BRD-005`, `BRD-007`–`BRD-011`.

### Constraint Genes

- No stable constraint gene is assigned. Platform geometry, ladders, spikes,
  gate locations and jump reach define authored instance geometry; key-gated
  opening is encoded as an automatic carried-state interaction in `SYS-063`.
- Green immunity is not merely an action limit: immune entities actually
  evolve while rewind resolves, so it is `SYS-062` rather than a Constraint.
- Scarce strategic resources: reachable history, relative phase between
  ordinary and green entities, one carried key, platform position and safe
  collision timing.
- Claim IDs: `BRD-004`–`BRD-009`.

### Information Genes

- `INF-001` — fully visible current state. Current platforms, monstars, Tim,
  keys, gates, switches, hazards and pieces are visible within the authored
  side-scrolling scene; camera extent is an inspection parameter.
- `INF-020` — visible rewind-affinity marking. Green glow declares which
  entities will remain outside ordinary history restoration before rewind.
- `INF-018` is absent: the player cannot seek forward beyond already lived
  history to reveal an exact prospective world state.
- Claim IDs: `BRD-004`–`BRD-006`, `BRD-012`.

### Objective Genes

- `OBJ-018` — complete finite staged token collection. Tim must acquire the
  declared finite jigsaw-piece set distributed across authored puzzle stages;
  each scoped World 3 piece is one required member.
- A room exit permits traversal and backtracking but does not replace missing
  required pieces, so `OBJ-022` is absent.
- Claim IDs: `BRD-010`.

### Time Genes

- `TIM-003` — real-time input during forced progression. During forward play,
  Tim, enemies and platforms continue changing on the simulation clock while
  the player supplies movement, jump or switch inputs.
- `TIM-007` — branchable player-reversible simulation history. Rewind restores
  already lived states, subject to declared green exceptions, and lets a new
  local action replace the old continuation.
- `TIM-008` is absent: there is no cursor-addressed prospective future or
  command schedule. `TIM-002` is absent because autonomous motion continues
  between player inputs.
- Claim IDs: `BRD-002`–`BRD-004`, `BRD-011`, `BRD-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Tim has just crossed safe ground while ordinary enemy walks | Hold rewind | Tim and enemy traverse retained positions backward | rewind restores active world state rather than restarting the stage | `BRD-002` |
| Tim has rewound before a failed jump | Release rewind and jump at a different time | New local motion produces a continuation different from the discarded attempt | restored history is branchable | `BRD-003` |
| Tim falls into a pit and takes a green key | Rewind to before the fall | Tim returns to safe geometry while the immune key remains carried | temporal affinity can intentionally separate coupled histories | `BRD-004`, `BRD-005` |
| A green door has been opened | Rewind to before its opening event in ordinary history | Door remains open while ordinary state restores | immunity can preserve mechanism state, not only position | `BRD-004`, `BRD-005` |
| Ordinary and green entities are visible | Inspect their rendering before rewinding | Green aura identifies the exceptional entity set | immunity is disclosed information, not trial-only hidden state | `BRD-006` |
| Tim lands on a monstar carrying a key | Continue downward contact | Monstar is removed, Tim rebounds and the key becomes carried | collision orientation and key transfer are separate automatic rules | `BRD-007`, `BRD-008` |
| Tim carries a compatible key at a locked gate | Contact gate | Key is consumed and gate opens under its own rewind affinity | access is an inventory-state transition | `BRD-008` |
| Linked platform is travelling away | Activate reachable lever | Platform reverses / changes its fixed traversal and continues automatically | switch command differs from platform motion | `BRD-009` |
| Tim reaches a required jigsaw piece | Contact piece | Piece is credited to the finite set while the broader game remains active | acquisition system and staged collection objective are distinct | `BRD-010` |

## Strategic and experiential structure

- Local decision: choose Tim's jump, switch timing or rewind depth relative to
  an enemy, platform, key or gate.
- Medium-term planning: use a green entity's uninterrupted forward progress to
  create a state combination that no single shared timeline could reach.
- Long-term structure: collect each authored puzzle piece by discovering which
  state must persist outside the ordinary rewind branch.
- Common heuristics: identify green affinity first, reason in two clocks, use
  death as a reversible probe, rewind only until Tim is safely repositioned and
  preserve irreversible green progress needed for the solution.
- Failure attribution: ordinary errors can be replayed backward visibly; when
  rewind makes a green arrangement worse, the aura identifies the exception
  that caused the branch mismatch.
- Player-trust factors: stored position / velocity, collision outcomes, carried
  keys, gate state, platform riders and green exceptions must resolve
  consistently at every rewind speed.
- Claim IDs: `BRD-001`–`BRD-012`.

## Replay and variation

- What changes between stages: geometry, piece position, enemy paths, keys,
  gates, switches, platform trajectories and which entities are green.
- Randomness or procedural generation: none in the scoped authored World 3
  puzzle rules.
- Multiple viable strategies: execution timing may vary, but minimal World 3
  puzzles often enforce one temporal dependency while permitting safe-route
  or rewind-depth variations.
- Typical replay motive: acquire missed pieces, understand a temporal boundary
  more cleanly or reproduce a solution with less exploratory rewind.
- Claim IDs: `BRD-002`–`BRD-010`.

## Adjacent systems and history

- Tin Hearts shares live autonomous motion, visible state and branchable world-
  history rewind. It changes the branch by repositioning physical routing
  devices around a population; Braid directly replays one avatar and exempts
  marked entities from restoration.
- Timelie also rewinds branchable history, but exposes exact prospective states
  and edits timestamped commands on a random-access timeline. Braid has neither
  future seeking nor scheduled actor commands.
- Portal shares direct embodied navigation and real-time spatial timing, but
  rewires position / velocity through apertures rather than restoring history.
- Gorogoa supplies the finite staged token-collection objective, but its panel
  transformations are self-paced and do not maintain reversible simulation.
- Claim IDs: `BRD-001`–`BRD-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-044`, `ACT-049` | local platforming, rewind and switch activation |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-062`, `SYS-063`, `SYS-064`, `SYS-065` | collection, enemies, immunity, keys, collision and platforms |
| Constraint | none | authored platform geometry and jump reach |
| Information | `INF-001`, `INF-020` | visible state and temporal affinity |
| Objective | `OBJ-018` | finite staged puzzle-piece collection |
| Time | `TIM-003`, `TIM-007` | live forward play and branchable rewind |

Canonical signature:

`ACT-008,ACT-044,ACT-049; SYS-037,SYS-045,SYS-062,SYS-063,SYS-064,SYS-065; ; INF-001,INF-020; OBJ-018; TIM-003,TIM-007`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `33` (`GAME-0001`–`GAME-0033`).
- Exact genome matches: none.
- Tied near matches: `GAME-0030` — Tin Hearts (`5 / 23 = 0.217391`).
- Supported combination subsets: `COMB-0034`, `COMB-0041`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0030` — Tin Hearts | `ACT-044`, `SYS-045`, `INF-001`, `TIM-003`, `TIM-007` | directly navigated platform avatar, green forward-time exceptions and token collection versus finite population routing by moved physical devices with path projection | Near, `0.217391` |

### Preserved research notes

- New genes: `ACT-049`, `SYS-062`, `SYS-063`, `SYS-064`, `SYS-065`,
  `INF-020`.
- Reused genes: `ACT-008`, `ACT-044`, `SYS-037`, `SYS-045`, `INF-001`,
  `OBJ-018`, `TIM-003`, `TIM-007`.
- Classification result: `New gene` and a recurring combination.
- Evidence and reasoning: rewind, autonomous motion, visible state and live
  time recur cleanly. Green forward evolution, local platforming, key / door
  state and collision semantics remain distinct from Tin Hearts routing.

## Combination record

- `COMB-0034` — live autonomous motion with branchable rewind.
- The five-gene subset is shared with Tin Hearts and deliberately omits how
  each game changes the replacement branch.

## Taxonomy impact

- Registry changes: six stable genes added; eight existing genes reused.
- `SYS-037` is generalised from optional rating collectibles to optional or
  required contact-acquired progression tokens. The contact-acquisition
  boundary is unchanged; objective status remains encoded separately.
- Taxonomy-change record: none; no prior signature or lifecycle changes.

## Negative results

- `ACT-045`, `INF-018` and `TIM-008` are absent: Braid does not address an
  unplayed future or edit commands at arbitrary timestamps.
- Green immunity is not folded into `TIM-007`: it resolves a distinct
  concurrent forward-time transition while ordinary history restores.
- Death is not a terminal attempt boundary in scope; it pauses for rewind, so
  no failure constraint or restart gene is admitted.
- World-specific time / position linkage, shadow replay and dilation are not
  inferred from World 3.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Braid restores already lived ordinary states but
  visibly green entities continue forward, enabling cross-history key, door,
  enemy and platform arrangements (`BRD-002`–`BRD-006`).
- [Confirmed | Corroborated | High] Replacement branches are created through
  ordinary live avatar input, not a prospective command timeline
  (`BRD-001`, `BRD-003`, `BRD-011`, `BRD-012`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-049`, `SYS-062`–`SYS-065`
  and `INF-020`; reused eight existing genes.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0034` records the five-gene live
  autonomous-motion / branchable-rewind core shared by Braid and Tin Hearts.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; `SYS-037` now
  separates contact acquisition from whether the token is optional or required.

## Нові питання

- Does another rewind puzzle reuse visible temporal affinity without the live
  platforming core?
- Should the next unit test the retained population-command candidate or first
  audit the second recurring combination and post-Portal singleton growth?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `TARGETED_REUSE_SELECTION_003`.
- Optimisation criterion: compare Pikmin 4 against at least three mechanically
  independent candidates before committing `GAME-0035`.
- Expected information gain: avoid extending either the time or population
  cluster without a fresh reuse / singleton estimate.
- Backlog impact: retain Pikmin 4 and rebuild the candidate pool.

## Sources consulted

- Official Braid site, Number None Steam description and PlayStation overview.
- Jonathan Blow's GDC rewind implementation talk.
- Contemporary GameSpot, Destructoid, Wired and Den of Geek reviews.
- StrategyWiki used only for narrow World 3 transition corroboration.
