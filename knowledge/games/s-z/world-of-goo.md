---
game_id: GAME-0026
slug: world-of-goo
game_title: World of Goo
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0026
gene_ids:
  action:
    - ACT-038
  system:
    - SYS-036
    - SYS-048
    - SYS-049
    - SYS-050
  constraint:
    - CON-047
    - CON-069
    - CON-070
  information:
    - INF-001
    - INF-015
  objective:
    - OBJ-019
  time:
    - TIM-003
---

# Game: World of Goo

## Analysis scope

- Version / ruleset: the original 2008 single-player construction grammar,
  represented by the `Fisty's Bog` level and corroborated against the original
  game's early black, green and Balloon Goo rules.
- Included: selecting a loose or detachable Goo Ball; dragging it into eligible
  attachment range; prospective strand display; automatic elastic-link
  formation; live gravity, load and buoyancy; autonomous loose-ball traversal;
  spikes and pipe extraction; finite dual-use Goo population; black Goo
  commitment; reusable green / Balloon Goo; required extraction count.
- Excluded: narrative interpretation, cosmetics, soundtrack, optional Time Bug
  undo, OCD challenges, World of Goo Corporation sandbox and leaderboards,
  co-op, later chapters' one-off transformations, remaster-only presentation,
  World of Goo 2, editors, mods and physics exploits.
- Direct-play status: not conducted for this record. The official developer
  description and creator retrospective are combined with a visually inspected
  academic level study, contemporary hands-on accounts and reviews.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WOG-001` | The player directly grabs a loose or detachable Goo Ball and releases it near an existing structure rather than commanding the whole structure's motion | Confirmed | Corroborated | High | P1, S1–S3 |
| `WOG-002` | A valid release automatically creates a type-bounded set of elastic strands to nearby structural nodes | Confirmed | Corroborated | High | P1, S1–S3 |
| `WOG-003` | The connected structure continuously responds to gravity, weight, elasticity and level-specific forces such as buoyancy and can sag, oscillate or collapse | Confirmed | Direct | High | F1, P1, A1, S1–S3 |
| `WOG-004` | Loose Goo Balls roam along the connected construction and, once it reaches the suction pipe, traverse into the pipe and are counted | Confirmed | Corroborated | High | S1–S3 |
| `WOG-005` | A standard level supplies a finite Goo population and requires a declared minimum number to enter its pipe | Confirmed | Direct | High | A1, S1–S3 |
| `WOG-006` | A countable Goo Ball committed as structure is unavailable for extraction, coupling structural cost to the remaining completion quota | Confirmed | Corroborated | High | S1–S3 |
| `WOG-007` | Structural removability is type-conditioned: black Goo is committed, while green and Balloon Goo can be detached and reused | Confirmed | Corroborated | High | S1, S2, S4 |
| `WOG-008` | In Fisty's Bog, lower spikes kill Goo Balls and upper spikes pop Balloons, so force balance and hazard clearance jointly constrain the bridge | Confirmed | Direct | High | A1, S3 |
| `WOG-009` | The current level and provisional strands are visible before release, but the interface does not disclose the resulting physical deformation | Confirmed | Corroborated | High | S1 |
| `WOG-010` | Physical state continues changing in real time while the player may grab and place another eligible ball | Confirmed | Corroborated | High | P1, A1, S1–S3 |
| `WOG-011` | The scoped authored level has fixed geometry, resources and force rules rather than random generation | Observation | Corroborated | High | WOG-001–WOG-010 |

## Basic data

- Release / origin: 2D Boy, the studio founded by Kyle Gabler and Ron Carmel,
  developed and published World of Goo in 2008 after Gabler's `Tower of Goo`
  prototype established the spring-linked construction model.
- Platform or physical form: pointer-controlled two-dimensional physics puzzle;
  continuous coordinates, elastic links and simulation time are mechanical.
- Puzzle family: live force-bearing network construction and population
  extraction.
- Official developer source:
  - **[F1]** [2D Boy — World of Goo](https://2dboy.com/), identifying the game
    as a physics-based puzzle / construction game.
- Creator primary account:
  - **[P1]** [Game Developer — “Making World of Goo, an all-time indie darling”](https://www.gamedeveloper.com/design/making-world-of-goo-an-all-time-indie-darling),
    Kyle Gabler's account of the spring prototype, pointer placement,
    automatic links, weight and elastic collapse.
- Formal and visually inspected source:
  - **[A1]** Valerie J. Shute and Yoon Jeon Kim,
    [“Does Playing the World of Goo Facilitate Learning?”](https://myweb.fsu.edu/vshute/pdf/Goo%20paper.pdf),
    documenting `Fisty's Bog`, gravity / buoyancy equilibrium, Goo and Balloon
    bridge construction, spikes, suction pipe and the exact six-ball quota.
- Contemporary corroboration:
  - **[S1]** [Nintendo World Report review](https://www.nintendoworldreport.com/review/17003/world-of-goo-wii),
    grab / link input, prospective strands, live physical effect, black and
    green valence / removability, autonomous traversal and extraction.
  - **[S2]** [GamesRadar review](https://www.gamesradar.com/world-of-goo-11/),
    limited population, structural engineering, fixed pipe, rescue count,
    gravity, hazards and committed versus repositionable types.
  - **[S3]** [GameSpot hands-on](https://www.gamespot.com/articles/world-of-goo-hands-on/1100-6189203/),
    pointer placement, automatic interlocking, swaying / collapse, finite
    material, bridge hazards and Balloon support.
  - **[S4]** [GameFAQs original-game guide](https://gamefaqs.gamespot.com/wii/945832-world-of-goo/faqs/54454),
    community corroboration for detachable green Goo and Balloon reuse; not
    used alone for a canonical rule.
- Claim IDs: `WOG-001`–`WOG-011`.

## Mechanical decomposition

### Action Genes

- `ACT-038` — attach selected live node to force-bearing structure. The player
  grabs one loose or currently detachable Goo Ball, drags it into range and
  releases it at a chosen continuous-space position. If the type is reusable,
  the same action can first reclaim it from the structure and place it again.
- This is not `ACT-028`: Opus Magnum configures static machine footprints in a
  paused editor before a separate run, whereas World of Goo changes a live
  deforming structure during the simulation.
- Claim IDs: `WOG-001`, `WOG-007`, `WOG-010`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. Every Goo node and
  strand participates in live gravity, elastic constraint, collision, load and
  any Balloon buoyancy; the multi-body structure can deform or collapse
  between inputs.
- `SYS-049` — placement-triggered elastic-link formation. Releasing an eligible
  Goo node makes the system instantiate the previewed nearby strands according
  to type, range and remaining valence.
- `SYS-050` — autonomous traversal over live structure. Uncommitted Goo Balls
  roam over connected strands and converge toward a reachable active pipe
  without the player routing each step.
- `SYS-048` — terminal-zone population accounting. Pipe suction removes and
  credits eligible free Goo, while lower spikes or other lethal zones remove
  countable Goo without extraction credit. Balloon contact with upper spikes
  is a hazard-response parameter of the live force system.
- Claim IDs: `WOG-002`–`WOG-005`, `WOG-008`, `WOG-010`.

### Constraint Genes

- `CON-070` — type-and-range-bounded structural attachment. A release can form
  strands only within eligible distance and up to the selected Goo type's
  connection valence; black Goo supports at most two links and green Goo at
  most three in the corroborated original rules.
- `CON-069` — finite construction-or-extraction population. Each countable Goo
  Ball can either remain free for pipe extraction or be committed as a load-
  bearing node, so structural expenditure reduces the maximum remaining quota.
- `CON-047` — finite reassignable network inventory applies to reusable
  structural types: an attached green or Balloon Goo cannot support a second
  location until it is detached and reassigned.
- Black Goo's irreversible commitment is a type parameter of `ACT-038` and
  `CON-069`; it is not `CON-060`, which requires the player to destroy an
  existing support link through a dedicated sever command.
- Claim IDs: `WOG-002`, `WOG-005`–`WOG-008`.

### Information Genes

- `INF-001` — fully visible current state. Terrain, hazards, pipe, loose Goo,
  current connected structure and the extracted / required count are visible.
- `INF-015` — prospective structural-link preview. While a ball is held near
  eligible nodes, guidelines show which strands will exist if it is released.
  They do not reveal the subsequent physical deformation or stability.
- Claim IDs: `WOG-009`, `WOG-011`.

### Objective Genes

- `OBJ-019` — rescue minimum population quota through fixed exit. The standard
  level completes when at least the displayed number of eligible loose Goo
  Balls traverse the player-built structure into the fixed suction pipe.
- The instance reuses the Lemmings objective boundary even though the route is
  constructed from members of the same population rather than produced by
  assigning them roles.
- Claim IDs: `WOG-004`–`WOG-006`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Elastic motion,
  gravity, buoyancy, loose-ball traversal and hazard interaction continue while
  the player observes or performs another placement.
- The absence of a countdown does not make the puzzle self-paced: waiting can
  materially change load, oscillation and failure state.
- Claim IDs: `WOG-003`, `WOG-008`, `WOG-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Loose black Goo is held within range of two structural nodes | Release it at the previewed position | Two strands form and the ball becomes a committed load-bearing node | placement, automatic linking and irreversible resource use are distinct | `WOG-001`, `WOG-002`, `WOG-006`, `WOG-007` |
| Held ball is outside eligible range or valence | Release it | No valid structural attachment matching that preview is committed | attachment legality is a constraint, not arbitrary free placement | `WOG-002`, `WOG-009` |
| A bridge has insufficient lift | Attach a Balloon to one side | A buoyant force enters the live constraint network and the whole structure rebalances over time | physics affects the complete construction after input | `WOG-003`, `WOG-010` |
| A reusable Balloon is attached | Grab and relocate it | Its former support disappears and new support forms at the destination | reusable deployed inventory differs from committed black Goo | `WOG-007` |
| Structure reaches the pipe with loose countable Goo remaining | No routing command | Loose Goo traverses the strands, enters the pipe and increments extraction count | autonomous traversal and terminal accounting follow construction | `WOG-004`, `WOG-005` |
| Too many countable Goo Balls remain structural | Reach the pipe | Fewer free balls can be extracted than the declared quota | construction material and completion population are one finite resource | `WOG-005`, `WOG-006` |
| Fisty's Bog bridge contacts lower or upper spikes | No corrective placement in time | Lower spikes kill Goo; upper spikes pop Balloons and may destabilise the bridge | hazards interact with both population and force balance | `WOG-008`, `WOG-010` |

## Strategic and experiential structure

- Local decision: choose one loose or detachable ball and a position whose
  previewed strands extend the structure without creating immediate overload.
- Medium-term planning: distribute triangles and buoyant supports so the live
  network clears hazards and settles near a viable path to the pipe.
- Long-term structure: reach the extraction zone while spending few enough
  countable Goo Balls as structure to preserve the required free surplus.
- Common heuristics: widen the base, triangulate long spans, counter sag with
  distributed Balloons, move reusable support progressively and wait briefly to
  observe equilibrium before committing scarce black nodes.
- Failure attribution: collapse, hazard contact or quota shortage normally
  traces to geometry, material allocation and timing rather than randomness.
- Player-trust factors: exact prospective strands and visible force response
  support experimentation, while deliberately undisclosed future deformation
  keeps stability a learned prediction rather than a solved preview.
- Claim IDs: `WOG-001`–`WOG-011`.

## Replay and variation

- What changes between sessions: the selected authored level, fixed terrain,
  Goo types, starting structures, hazards, forces, pipe and required count.
- Randomness or procedural generation: none in the scoped level grammar.
- Multiple viable strategies: continuous placement coordinates, structural
  topology, support relocation and acceptable material expenditure can yield
  several stable solutions.
- Typical replay motive: rescue more surplus Goo, use fewer moves, finish
  faster or recover from structural collapse; OCD thresholds are excluded from
  the canonical objective but motivate optimisation in the wider game.
- Claim IDs: `WOG-003`, `WOG-005`–`WOG-011`.

## Adjacent systems and history

- Direct predecessor: Gabler's `Tower of Goo` prototype already used pointer-
  placed nodes, automatic spring links and live weight-driven collapse; World
  of Goo added authored traversal, extraction and varied material types.
- Lemmings also rescues a quota of autonomous agents, but spends a separate
  typed skill inventory to alter behaviour and terrain. World of Goo directly
  converts potential rescue units into the force-bearing route itself.
- Cut the Rope also uses continuous constrained physics, but removes supports
  around one payload. World of Goo adds nodes and elastic links to a many-body
  structure that becomes the transport path.
- Mini Metro also edits a live network from finite reusable inventory, but its
  topology drives scheduled vehicles and demand rather than force equilibrium.
- Claim IDs: `WOG-001`–`WOG-011`, P1.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-038` | loose versus detachable source and continuous placement position |
| System Behaviour | `SYS-036`, `SYS-048`, `SYS-049`, `SYS-050` | elasticity, gravity, buoyancy, traversal and extraction |
| Constraint | `CON-047`, `CON-069`, `CON-070` | reassignable types, dual-use population, range and valence |
| Information | `INF-001`, `INF-015` | complete current state and prospective strands |
| Objective | `OBJ-019` | minimum pipe-extraction count |
| Time | `TIM-003` | live physical evolution during placement |

Canonical signature:

`ACT-038; SYS-036,SYS-048,SYS-049,SYS-050; CON-047,CON-069,CON-070; INF-001,INF-015; OBJ-019; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `25` (`GAME-0001`–`GAME-0025`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`4 / 19 = 0.210526`).
- Supported combination subsets: `COMB-0026`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0025` — Lemmings | `SYS-048`, `INF-001`, `OBJ-019`, `TIM-003` | Lemmings spends a separate typed skill stock to assign roles to continuously walking agents and mutate terrain; World of Goo directly places members of the potential rescue population as elastic load-bearing nodes, and loose members traverse the resulting structure | Near, `0.210526` |

### Preserved research notes

- New genes: `ACT-038`, `SYS-049`, `SYS-050`, `CON-069`, `CON-070` and
  `INF-015`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: force dynamics, terminal-zone population accounting,
  reassignable network inventory, full current visibility, quota rescue and
  live scheduling all survive their existing boundaries. Direct live-node
  placement, automatic spring linking, autonomous structure traversal, dual-
  use population, attachment valence and prospective topology preview do not.

## Combination record

- Registered [`COMB-0026`](../../combinations/COMB-0026.md), a nine-gene
  proper subset centred on building a live force-bearing route out of the same
  finite population that must later traverse it to extraction.
- Reassignable-type inventory and both information genes remain in the full
  genome but are not required to identify the central dual-use construction.

## Taxonomy impact

- Registry changes: six stable genes added; `SYS-036`, `SYS-048`, `CON-047`,
  `INF-001`, `OBJ-019` and `TIM-003` reused.
- Taxonomy-change record: none. Placement, automatic linking / physics,
  eligibility / scarcity, preview, extraction target and live scheduling remain
  cleanly represented by the current six types.
- Candidate terms affected: live structural-node attachment, elastic-link
  formation, autonomous structure traversal, dual-use structural population,
  bounded attachment geometry and prospective strand preview are promoted.

## Negative results

- `ACT-028` is absent because there is no paused machine editor followed by a
  separate execution phase; the structure is live during every placement.
- `ACT-036` and `CON-067` are absent because Goo Balls are placed as material,
  not assigned behavioural roles from a separate finite skill stock.
- `CON-060` is absent because ordinary construction does not provide a command
  to irreversibly sever a selected support link.
- `OBJ-014` is absent because success counts multiple autonomous Goo Balls at a
  pipe rather than one indirectly controlled physical payload at a receiver.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.
