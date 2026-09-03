---
game_id: GAME-0021
slug: cut-the-rope
game_title: Cut the Rope
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0021
gene_ids:
  action:
    - ACT-027
  system:
    - SYS-036
    - SYS-037
  constraint:
    - CON-060
    - CON-061
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-014
  time:
    - TIM-003
---

# Game: Cut the Rope

## Analysis scope

- Version / ruleset: the base rope-and-candy level model of ZeptoLab's
  original 2010 Cut the Rope, represented by levels whose decision-relevant
  components are fixed anchors, cuttable ropes, one candy, up to three stars,
  Om Nom and the level boundary.
- Included: swiping across one or more ropes; irreversible severing; gravity,
  tension, pendulum motion, momentum and ordinary collision; candy contact
  with optional stars; delivery to Om Nom; score / star optimisation; terminal
  candy loss outside the level boundary; restart only as the next attempt.
- Excluded: bubbles, air cushions, bumpers, sliders, rope guns, rockets,
  spikes, spiders, electric sparks, teleporters, gravity switches and every
  other later-box device or hazard; superpowers, coins, hidden prizes,
  advertisements, purchases, box unlock thresholds, achievements,
  leaderboards, remastered variants and sequels.
- Direct-play status: not conducted for this record. Creator and publisher
  descriptions are combined with a peer-reviewed physics-model account and a
  contemporary rules guide.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CTR-001` | The original game is a physics-based single-player puzzle centred on feeding one candy to Om Nom | Confirmed | Direct | High | F1–F3, A1 |
| `CTR-002` | In the scoped level model, the candy begins attached to one or more ropes fixed to anchors | Confirmed | Corroborated | High | A1, S1 |
| `CTR-003` | The player cuts a rope by swiping across it and may intersect several ropes with one continuous gesture | Confirmed | Corroborated | High | F2, F3, S1 |
| `CTR-004` | Cutting removes the intersected support; the player does not directly select the candy's resulting position or velocity | Observation | Corroborated | High | CTR-002, CTR-003, A1 |
| `CTR-005` | Candy motion continues in real time under gravity, remaining rope constraints, momentum and collision between player inputs | Confirmed | Corroborated | High | F1–F3, A1 |
| `CTR-006` | Successful solutions depend on both which rope is cut and the physical state at the moment of the cut | Confirmed | Corroborated | High | F3, A1, S1 |
| `CTR-007` | Contact between the candy and a gold star collects that optional evaluation item without completing the level | Confirmed | Corroborated | High | F1–F3, S1 |
| `CTR-008` | Contact between the candy and Om Nom completes the scoped level | Confirmed | Corroborated | High | F2, F3, A1, S1 |
| `CTR-009` | The scoped attempt fails if the candy leaves the level boundary before delivery | Confirmed | Corroborated | High | A1, S1 |
| `CTR-010` | A severed rope cannot be restored inside the attempt; restart begins a new copy of the initial state | Observation | Corroborated | High | CTR-003, CTR-004, S1 |
| `CTR-011` | The complete current geometry and motion are visible, while the scoped level contains no hidden or random in-play transition | Observation | Corroborated | High | F2, F3, A1 |
| `CTR-012` | Feeding Om Nom is mandatory success, whereas collecting stars and improving score are optional evaluation objectives | Observation | Corroborated | High | F1–F3, S1 |

## Basic data

- Release / origin: ZeptoLab released the original Cut the Rope for iOS in
  2010. This record analyses its foundational rope-cutting model rather than
  the mechanically broader current compilation.
- Platform or physical form: digital touch puzzle; swipe timing and a
  continuously simulated two-dimensional level are mechanically relevant.
- Puzzle family: deterministic real-time physics intervention and payload
  delivery.
- Primary and publisher sources:
  - **[F1]** [ZeptoLab — Cut the Rope](https://www.zeptolab.com/games/cut-the-rope),
    creator identification of the original game, gold stars and physics-based
    play.
  - **[F2]** [developer App Store listing](https://apps.apple.com/us/app/cut-the-rope-physics-puzzle/id1024506959),
    rope cutting, candy guidance, Om Nom delivery, stars and later-device
    boundaries.
  - **[F3]** [Nintendo publisher description](https://www.nintendo.com/en-gb/Games/Nintendo-3DS-download-software/Cut-the-Rope-793490.html),
    touch-screen snipping at a chosen moment, candy delivery, star contact,
    replay and score improvement.
- Formal / reproducible source:
  - **[A1]** Noor Shaker et al.,
    [“Evolving Playable Content for Cut the Rope through a Simulation-Based Approach”](https://cdn.aaai.org/ojs/12690/12690-52-16207-1-2-20201228.pdf),
    AIIDE 2013, describing the original game and a research clone with rope
    constraints, gravity, Newtonian motion, timed actions and boundary-loss
    detection. Clone-only implementation choices are not imported silently.
- Contemporary rule corroboration:
  - **[S1]** [Gamezebo — Cut the Rope walkthrough](https://www.gamezebo.com/walkthroughs/cut-the-rope-walkthrough/),
    2010-era account of multi-rope swipe cutting, candy swing, stars, feeding,
    score, replay and failure / restart.
- Claim IDs: `CTR-001`–`CTR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-027` — swipe-sever selected support link. A gesture intersects one or
  more currently intact ropes and commits their removal at the sampled moment.
- The command target is the rope, not the candy. The player chooses neither a
  destination nor an impulse vector; the resulting trajectory belongs to
  physics resolution.
- Simultaneous multi-rope intersection is an action parameter. It does not turn
  the gesture into several independently scheduled turns.
- Claim IDs: `CTR-002`–`CTR-004`, `CTR-010`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. While simulation
  time advances, gravity accelerates the candy, intact ropes enforce anchor
  distance, tension redirects motion into a swing, and momentum continues
  after support removal.
- `SYS-037` — contact-triggered optional collectible acquisition. When the
  moving candy overlaps a star, that star is credited and removed / marked
  while the same attempt and motion continue.
- Om Nom contact and boundary escape are evaluations of the moving state; they
  are encoded by the success Objective and terminal Constraint rather than
  additional catch-all “win” and “lose” behaviours.
- No random-selection gene is assigned: the scoped level layout and physical
  response are fixed before play.
- Claim IDs: `CTR-005`–`CTR-009`, `CTR-011`.

### Constraint Genes

- `CON-060` — irreversible support-link severing. Every cut rope is absent for
  the remainder of that attempt and cannot be reattached through ordinary
  play.
- `CON-061` — terminal payload boundary escape. If the required candy crosses
  outside the playable canvas before delivery, the attempt fails.
- `CON-013` is absent. A bad cut may make success physically impossible, but
  the scoped failure is normally realised by the explicit boundary-loss state;
  the record does not claim a detected non-terminal deadlock with other useful
  actions still available.
- `CON-001` is absent because continuous coordinates and collision geometry
  are not a fixed collection of addressable occupancy positions.
- Rope count, anchor coordinates, rope lengths, level bounds and star
  positions are parameters.
- Claim IDs: `CTR-002`–`CTR-006`, `CTR-009`, `CTR-010`.

### Information Genes

- `INF-001` — fully visible current state. Candy, anchors, intact ropes, stars,
  Om Nom, boundaries, position and motion direction are visually available.
- The player may need to estimate velocity and future trajectory, but
  uncertainty from continuous prediction is not hidden state or randomness.
- Claim IDs: `CTR-002`, `CTR-005`, `CTR-011`.

### Objective Genes

- `OBJ-014` — deliver indirectly controlled payload to fixed receiver. Success
  requires using timed environmental intervention so the physically simulated
  candy contacts Om Nom.
- `OBJ-002` — maximise accumulated score. Optional star contact and completion
  speed support replay for more stars or a higher score without replacing the
  mandatory delivery condition.
- `OBJ-010` is absent: the candy is not a directly controlled `YOU` object and
  Om Nom is not a mutable rule-defined `WIN` property.
- Claim IDs: `CTR-007`, `CTR-008`, `CTR-012`.

### Time Genes

- `TIM-003` — real-time input during forced progression. The physical state
  continues changing while the player waits, observes and chooses the next
  cut moment.
- This expands evidence for the existing boundary beyond grid and network
  simulations: forced progression may be continuous force integration rather
  than scheduled cell, flow or vehicle steps.
- It is not `TIM-001`, because physics does not finish into a stable decision
  state after each swipe; motion remains live and another cut can be required
  during the same trajectory.
- Claim IDs: `CTR-005`, `CTR-006`, `CTR-011`.

## Reproducible transitions

| Before | Player action | Automatic evolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Candy hangs motionless from one vertical rope | Swipe across that rope | Support disappears and gravity accelerates the candy downward | Cut command and physics response are separate | `CTR-003`–`CTR-005` |
| Candy swings from one intact rope | Wait without input | Position and velocity continue changing along the pendulum arc | A no-input interval changes decision state | `CTR-005`, `CTR-006` |
| Candy is attached to two ropes | Swipe across only the left rope | Right rope remains and redirects the falling body around its anchor | Link selection changes the remaining constraint topology | `CTR-003`–`CTR-006` |
| One swipe intersects two ropes | Complete the gesture | Both intersected links disappear at the gesture time; the candy enters free fall | Multi-link selection is one gesture parameter | `CTR-003`, `CTR-004` |
| Moving candy crosses a gold star | Make no additional command | Star is collected; candy continues moving and the level remains active | Collection is contact-triggered and optional | `CTR-007` |
| Moving candy enters Om Nom's mouth | Make no additional command | Delivery is accepted and the level completes | Fixed receiver contact is mandatory success | `CTR-008`, `CTR-012` |
| Candy misses Om Nom and crosses the level boundary | Make no additional command | Attempt fails and can be restarted from its initial layout | Boundary escape is terminal | `CTR-009`, `CTR-010` |
| A rope was cut too early | Attempt to restore it | No in-attempt action recreates the support | Forward severing is irreversible | `CTR-006`, `CTR-010` |

## Strategic and experiential structure

- Local decision: choose which support link to remove and the exact motion
  phase at which to remove it.
- Medium-term planning: predict how remaining anchors will convert falling
  motion into pendulum arcs and where later release will send the candy.
- Long-term structure: construct a timed sequence of irreversible topology
  changes whose continuous trajectory touches desired stars and ends at Om
  Nom rather than the boundary.
- Common heuristics: wait for the swing apex when direction must reverse; use
  one rope to preserve radius while another creates initial motion; collect a
  star only if its detour leaves a viable receiver trajectory.
- Failure attribution: the scoped model is visible and deterministic, so a
  miss is attributable to cut selection, timing or trajectory estimation rather
  than hidden content or random successor selection.
- Player-trust factors: gesture intersection, rope removal, constraint length,
  collision, star contact, receiver contact and boundary failure must be
  spatially consistent from frame to frame.
- Claim IDs: `CTR-002`–`CTR-012`.

## Replay and variation

- What changes between levels: anchor count and position, rope length, initial
  candy state, star positions, Om Nom position and boundary-relevant geometry.
- What remains stable: swipe cutting, irreversible support loss, deterministic
  continuous physics, contact collection, receiver delivery and boundary loss.
- Randomness or procedural generation: none in the scoped fixed level.
- Multiple viable strategies: some layouts permit different cut order or
  timing windows; star-maximising trajectories may differ from minimum-risk
  delivery.
- Typical replay motive: collect missed stars, improve score or reproduce a
  more reliable timing sequence.
- Claim IDs: `CTR-001`, `CTR-006`–`CTR-012`.

## Adjacent systems and history

- Tetris also accepts real-time intervention while gravity changes state, but
  the player directly repositions one active rigid element on a fixed grid.
  Cut the Rope removes environmental constraints and lets continuous forces
  determine the payload trajectory.
- Pipe Dream also requires actions before a live process reaches failure, but
  its flow traverses player-placed discrete ports. Cut the Rope integrates
  force, velocity and rope constraints in continuous space.
- Baba Is You also completes through object overlap, but its goal is a mutable
  rule property and its controlled object moves directly by grid steps. Om Nom
  is a fixed receiver and candy motion is indirect.
- Later Cut the Rope boxes add player-triggered devices, hazards and alternate
  force fields. Those mechanics require broader scopes and are not treated as
  parameters of this base genome.
- Claim IDs: `CTR-001`–`CTR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-027` | gesture sampling and multi-rope intersection |
| System Behaviour | `SYS-036`, `SYS-037` | physics constants and contact geometry |
| Constraint | `CON-060`, `CON-061` | rope topology and level boundary |
| Information | `INF-001` | motion readability and trajectory aids |
| Objective | `OBJ-002`, `OBJ-014` | score table, stars and receiver geometry |
| Time | `TIM-003` | simulation timestep and pause policy |

Canonical signature:

`ACT-027; SYS-036,SYS-037; CON-060,CON-061; INF-001; OBJ-002,OBJ-014; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `20` (`GAME-0001`–`GAME-0020`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`3 / 21 = 0.142857`); `GAME-0016` — Pipe Mania / Pipe Dream (`3 / 21 = 0.142857`).
- Supported combination subsets: `COMB-0021`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0004` — Tetris | `INF-001`, `OBJ-002`, `TIM-003` | Tetris directly changes a falling rigid piece's grid pose and resolves lock / line clears; Cut the Rope irreversibly removes support links and predicts continuous constrained-body motion toward a receiver | Near, `0.142857` |
| `GAME-0016` — Pipe Mania / Pipe Dream | `INF-001`, `OBJ-002`, `TIM-003` | Pipe Dream places fixed-orientation queue tiles before a directed flow; Cut the Rope has no queue or constructed path and instead times topology removal during force integration | Near, `0.142857` |

### Preserved research notes

- New genes: `ACT-027`, `SYS-036`, `SYS-037`, `CON-060`, `CON-061`,
  `OBJ-014`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: current-state visibility, score optimisation and
  real-time input during forced progression reuse existing boundaries. The
  command target, physical transition, optional contact reward, irreversible
  support state, payload-loss boundary and indirect delivery objective have no
  operational match in the first twenty genomes.

## Combination record

- Registered [`COMB-0021`](../../combinations/COMB-0021.md), a proper
  six-gene subset centred on irreversible support release into live physics
  delivery.
- Optional star collection, general visibility and score remain in the full
  genome but are not required to identify the delivery interaction.

## Taxonomy impact

- Registry changes: six stable genes added; three existing genes reused.
- Taxonomy-change record: none. Continuous force integration fits System
  Behaviour and its scheduling fits existing `TIM-003`; no seventh type is
  needed.
- Candidate terms affected: cut, continuous physics, contact collection,
  irreversible support, payload escape and indirect delivery are promoted to
  bounded records.

## Negative results

- `ACT-014` is absent because the candy is not selected and relocated to a
  destination.
- `SYS-006` is absent because it encodes grid-stepped automatic descent of an
  active falling element, not continuous multi-force dynamics.
- `CON-001` is absent because the level has continuous coordinates rather than
  persistent addressable occupancy cells.
- `OBJ-010` is absent because neither direct control nor mutable goal-property
  syntax applies.
- `TIM-001` is absent because automatic motion remains live between multiple
  possible cut inputs.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.
