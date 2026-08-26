---
game_id: GAME-0037
slug: cosmic-express
game_title: Cosmic Express
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0037
gene_ids:
  action:
    - ACT-016
  system:
    - SYS-031
  constraint:
    - CON-001
    - CON-029
    - CON-050
    - CON-051
  information:
    - INF-001
  objective:
    - OBJ-024
  time:
    - TIM-009
---

# Game: Cosmic Express

## Analysis scope

- Version / ruleset: the 2017 base game, scoped to one ordinary early authored
  colony puzzle with one fixed entrance and exit, one train with one passenger
  seat, several ordinary colour-coded aliens and matching homes.
- Included: fixed finite grid; tracing one route from entrance to exit;
  adjacent-cell continuity, no branching, revisiting or self-crossing;
  explicit run start; locked deterministic train traversal; automatic adjacent
  boarding and alighting; one-seat capacity; colour-compatible homes; delivery
  of every alien before the train exits; reset and route revision.
- Excluded: later slime / contamination passengers, extra carriages, portals,
  crossovers, multiple exits, constellation progression, hints, achievements,
  narrative interpretation, platform gestures and the 2025 Spooky Express.
- Direct-play status: not conducted. The official press kit and storefront
  establish route planning, passenger homes and one-seat capacity; four
  contemporary reviews corroborate grid tracing, non-crossing, automatic
  ordered pickup / drop-off, explicit run and exit completion. Exact tie-breaks
  for simultaneous equidistant passengers remain a parameter.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CEX-001` | Each scoped puzzle has a fixed finite gridded dome with a train entrance, an exit, waiting aliens and destination homes | Confirmed | Corroborated | High | P1, P2, S1–S3 |
| `CEX-002` | The player traces one continuous track from the entrance toward the exit before starting the train | Confirmed | Corroborated | High | P1, S1–S4 |
| `CEX-003` | The ordinary route is unbranched and cannot revisit or cross itself | Confirmed | Corroborated | High | S1–S4 |
| `CEX-004` | Starting execution locks route editing while the train follows the authored track automatically until success, failure or reset | Confirmed | Corroborated | High | S2–S4 |
| `CEX-005` | A waiting alien boards automatically when the passing carriage can serve it and has a free seat | Confirmed | Corroborated | High | P2, S1–S4 |
| `CEX-006` | The scoped carriage holds at most one alien, so pickup and delivery order determines who can board later | Confirmed | Direct | High | P2, S2–S4 |
| `CEX-007` | A carried alien leaves automatically at a compatible same-colour home encountered along the route | Confirmed | Corroborated | High | S1–S4 |
| `CEX-008` | Success requires every required alien to be delivered before the train reaches the selected exit | Confirmed | Corroborated | High | S1–S4 |
| `CEX-009` | Route design is self-paced, and a failed deterministic run returns to revision rather than permitting live track edits | Confirmed | Corroborated | High | S1–S4 |
| `CEX-010` | The passenger set, homes, grid, capacity and current route are visible; no scoped in-play random event changes them | Observation | Corroborated | High | CEX-001–CEX-009 |
| `CEX-011` | Cosmic Express route authoring shares Flow Free's compound path trace but not paired endpoint identity or full-board coverage | Observation | Corroborated | High | CEX-002, CEX-003 |
| `CEX-012` | Its one-shot locked service run differs from Mini Metro's live editable recurring network and from SpaceChem's cyclic production machine | Observation | Corroborated | High | CEX-004–CEX-009 |

## Basic data

- Release / origin: Cosmic Engineers released Cosmic Express on 16 March
  2017; the official credits identify Alan Hazelden and Benjamin Davis as
  designers / programmers and Tyu as artist.
- Platform or physical form: deterministic, self-paced route-design puzzle
  with an automatic one-shot train execution phase.
- Puzzle family: capacity-ordered passenger-route planning.
- Primary and official sources:
  - **[P1]** [Official press kit](https://cosmicexpressgame.com/press/),
    describing route planning, aliens needing homes, authorship and release.
  - **[P2]** [Official Steam listing](https://store.steampowered.com/app/583270/Cosmic_Express/),
    stating that the player lays track through small stations, each alien has a
    home and the ordinary passenger car has room for one alien.
- Contemporary corroboration:
  - **[S1]** [Pocket Gamer review](https://www.pocketgamer.com/cosmic-express/review/),
    documenting a dragged grid route, non-crossing track, automatic pickup /
    delivery, colour destinations and the train exit.
  - **[S2]** [Stuff review](https://www.stuff.tv/review/app-of-the-week-cosmic-express-review/),
    documenting entrance / exit stubs, one-seat carriage, pickup ordering and
    the absence of junctions.
  - **[S3]** [Big Boss Battle review](https://bigbossbattle.com/review-cosmic-express/),
    documenting entrance, one-at-a-time delivery, non-crossing and final exit.
  - **[S4]** [eShopperReviews Switch review](https://eshopperreviews.com/2023/08/16/cosmic-express-for-nintendo-switch-review/),
    corroborating explicit track drawing, start command, automatic adjacency
    boarding / alighting, colour matching, capacity and self-crossing ban.
- Claim IDs: `CEX-001`–`CEX-012`.

## Mechanical decomposition

### Action Genes

- `ACT-016` — trace path from fixed endpoint. The player starts at the fixed
  entrance stub and drags one variable-length ordered route through adjacent
  grid cells to the selected exit as a compound gesture.
- `ACT-023` is absent: the route is not a persistent named service line edited
  while recurrent transport runs. Reset or pre-run redrawing replaces a
  one-shot plan.
- `ACT-046` is absent: the route carries no addressed instruction symbols or
  separately controlled program token.
- The run button commits the temporal phase described by `TIM-009`; it is not a
  separate reusable manipulation of a world object.
- Claim IDs: `CEX-002`–`CEX-004`, `CEX-011`, `CEX-012`.

### System Behaviour Genes

- `SYS-031` — automatic route-based passenger transport. Once started, the
  train traverses the traced route and automatically loads, carries and unloads
  eligible aliens according to adjacency, capacity and destination type.
- `SYS-029` / `SYS-030` are absent: stations and demand do not arrive over
  simulation time. `SYS-038` / `SYS-040` are absent because no cyclic controller
  schedule or machine-geometry failure is evaluated.
- Resolution order at a route position: advance train to the next track cell;
  process eligible alighting; if capacity is then free, process eligible
  boarding; preserve current occupant otherwise; continue toward the exit;
  evaluate all-delivered success or incomplete exit failure.
- Claim IDs: `CEX-004`–`CEX-009`, `CEX-012`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The complete scoped dome is one finite
  unchanging set of grid cells with fixed entrance, exit, passenger and home
  locations.
- `CON-029` — orthogonally contiguous simple path. In logical grid topology,
  the track is one unbranched adjacent-cell sequence with no revisits; turns
  rendered diagonally by the isometric view do not add diagonal grid edges.
- `CON-050` — capacity-bounded passenger pickup. The ordinary carriage has one
  seat, so a waiting alien cannot board until the current occupant leaves.
- `CON-051` — type-coded destination completion. A passenger alights only at a
  home compatible with its displayed colour/type.
- `CON-028` is absent: entrance and exit are route terminals, not one member of
  several immutable labelled terminal pairs. `CON-030` is absent because the
  scope has one simple path; its self-revisit ban belongs to `CON-029`, not
  competition between distinct paths for a cell.
- Scarce strategic resources: route cells, the single seat, opportunity order
  along the simple path and access to the exit after all deliveries.
- Claim IDs: `CEX-001`–`CEX-003`, `CEX-005`–`CEX-008`, `CEX-011`.

### Information Genes

- `INF-001` — fully visible current state. Grid, entrance, exit, aliens, colour
  homes, train capacity and the complete current route are inspectable before
  execution; the run is deterministic.
- Pickup sequence is not a separate future preview: it is derivable from the
  visible ordered route and automatic transition rules.
- Claim IDs: `CEX-001`, `CEX-010`.

### Objective Genes

- `OBJ-024` — complete finite passenger-service route. Every required waiting
  passenger must be transported to a compatible destination and the service
  vehicle must then reach the declared route exit in the same run.
- `OBJ-019` is absent: aliens are ordered passengers delivered to typed homes,
  not an autonomous population reaching a shared extraction quota.
- `OBJ-023` is absent: the train carries agents to distributed homes rather
  than transporting designated world objects to one operational base.
- Claim IDs: `CEX-005`–`CEX-008`.

### Time Genes

- `TIM-009` — self-paced route design before locked one-shot traversal. The
  player may revise the complete route without time pressure, then starts one
  deterministic traversal during which edits are unavailable until success,
  failure or reset.
- `TIM-006` is absent: Cosmic Express has no cyclic machine program, repeated
  production or multi-cycle steady-state test. `TIM-003` is absent because the
  player does not edit while train progression runs. `TIM-002` is absent at
  whole-puzzle scope because one run resolves many transport events after the
  design phase rather than each edit becoming final sequential world state.
- Claim IDs: `CEX-004`, `CEX-009`, `CEX-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty fixed dome has entrance and exit stubs | Drag from entrance through adjacent cells to exit | One ordered unbranched route is recorded | fixed-endpoint compound tracing | `CEX-001`, `CEX-002` |
| Active trace would enter an earlier route cell | Continue toward that cell | Self-crossing / revisit is rejected or cannot persist | route is simple and non-crossing | `CEX-003` |
| Complete route is visible | Press start | Train begins automatic traversal and route editing locks | design and execution are separate phases | `CEX-004`, `CEX-009` |
| Empty carriage passes one waiting alien | Let train advance | Alien boards automatically and consumes the sole seat | adjacency and capacity determine pickup | `CEX-005`, `CEX-006` |
| Occupied carriage passes another waiting alien | Let train advance | Second alien remains waiting | route order matters beyond connectivity | `CEX-006` |
| Carried purple alien passes a purple home | Let train advance | Alien leaves, home is satisfied and seat becomes free | typed destination completion | `CEX-007` |
| Carried purple alien passes a differently typed home | Let train advance | Passenger remains aboard | proximity without compatibility is insufficient | `CEX-007` |
| Train reaches exit with one alien still waiting | Let traversal finish | Run fails / does not complete and route can be revised | exit alone is not success | `CEX-008`, `CEX-009` |
| Every alien has reached a compatible home before exit | Let train reach exit | Puzzle completes | finite service route is conjunctive | `CEX-008` |

## Strategic and experiential structure

- Local decision: choose the next route cell so the train approaches the next
  useful passenger or home without consuming a needed later corridor.
- Medium-term planning: alternate pickup and compatible drop-off to free the
  single seat, while preserving one simple route to the exit.
- Long-term structure: embed the complete passenger-service order into a
  non-self-crossing geometric path before committing the run.
- Common heuristics: reason backward from the exit; express the required event
  order first, then test whether it has a simple spatial embedding; avoid
  passing a passenger before capacity can serve it.
- Failure attribution: the visible run shows the first missed boarding,
  incompatible home or premature exit, tying failure to route order rather
  than randomness.
- Player-trust factors: adjacency radius, simultaneous alight / board order,
  colour compatibility, route validation and reset restoration must be stable.
- Claim IDs: `CEX-001`–`CEX-012`.

## Replay and variation

- What changes between puzzles: grid shape, obstacles, entrance / exit,
  passenger and home placement, and later excluded rule modules.
- Randomness or procedural generation: none in the scoped authored puzzle.
- Multiple viable strategies: some instances may admit different geometric
  paths expressing the same service order; compact layouts often force the
  key pickup / delivery sequence.
- Typical replay motive: revise a failed route, reduce exploratory runs or
  solve optional branches of the constellation map.
- Claim IDs: `CEX-001`, `CEX-009`, `CEX-010`.

## Adjacent systems and history

- Flow Free shares direct compound path tracing, fixed cells, visible state and
  a simple adjacent route. Cosmic Express draws one entrance-to-exit track,
  does not pair colours at endpoints and does not cover every cell.
- Mini Metro shares automatic capacity-bounded typed passenger transport.
  Cosmic Express fixes all demand and geometry, commits one simple route before
  execution and ends after a successful finite run rather than editing a live
  recurring network for score.
- SpaceChem and Opus Magnum share design-before-run separation, but their runs
  execute cyclic instruction schedules and repeated production. Cosmic Express
  executes one spatial service traversal without program symbols.
- Pipe Mania also commits spatial routing under a running process, but its
  flow begins on a forced clock while pieces remain editable; Cosmic Express
  starts only after the route is complete and locks edits during traversal.
- Claim IDs: `CEX-001`–`CEX-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-016` | one entrance-to-exit compound route trace |
| System Behaviour | `SYS-031` | automatic one-shot passenger service |
| Constraint | `CON-001`, `CON-029`, `CON-050`, `CON-051` | simple path, one seat and typed homes |
| Information | `INF-001` | visible deterministic route state |
| Objective | `OBJ-024` | all deliveries followed by train exit |
| Time | `TIM-009` | self-paced design, locked one-shot run |

Canonical signature:

`ACT-016; SYS-031; CON-001,CON-029,CON-050,CON-051; INF-001; OBJ-024; TIM-009`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `36` (`GAME-0001`–`GAME-0036`).
- Exact genome matches: none.
- Tied near matches: `GAME-0012` — Flow Free (`4 / 14 = 0.285714`).
- Supported combination subsets: `COMB-0037`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0012`.

## Combination record

- Registered recurring `COMB-0037` — visible capacity-bounded typed passenger
  transport, supported by Mini Metro and Cosmic Express.
- The four-gene core excludes live demand generation, network editing,
  one-shot route tracing, run timing and each game's different objective.

## Taxonomy impact

- Registry changes for Cosmic Express: two stable genes added and seven
  existing genes reused.
- `ACT-016`, `SYS-031` and `CON-051` receive representation-neutral wording
  generalisations for terminal type and one-shot versus repeated service.
- Separate pre-classification audit accepted
  [`TAXONOMY_CHANGE_003`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_003.md),
  merging duplicate `ACT-053` into `ACT-018`; this does not affect the Cosmic
  Express signature.

## Negative results

- `ACT-023` and `TIM-003` are rejected because track is not edited during live
  recurring service.
- `ACT-046` and `TIM-006` are rejected because the route has no instruction
  symbols, controller or repeated machine-production cycle.
- `CON-028` and `CON-030` are rejected because there are no labelled endpoint
  pairs or multiple competing paths; simple self-noncrossing is `CON-029`.
- `OBJ-019` and `OBJ-023` are rejected because typed passengers are delivered
  to distributed homes before the vehicle exits.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] One self-paced route encodes the complete
  pickup / drop-off order before a locked deterministic train run (`CEX-002`–
  `CEX-009`).
- [Confirmed | Direct | High] One-seat capacity turns visible geometric order
  into a passenger-service constraint (`CEX-005`–`CEX-008`).

## Нові гени

- [Observation | Corroborated | High] Added `OBJ-024` and `TIM-009`; reused
  seven existing genes.

## Нові комбінації

- [Observation | Corroborated | High] Registered recurring `COMB-0037` with
  Mini Metro for visible capacity-bounded typed passenger transport.

## Зміни таксономії

- [Observation | Corroborated | High] Accepted `TAXONOMY_CHANGE_003`, merging
  duplicate Patrick's Parabox `ACT-053` into shared `ACT-018`; Cosmic Express
  itself requires no correction to an earlier signature.

## Нові питання

- Does The Swapper generalise `ACT-052` control transfer or require a separate
  consciousness / body locus action?
- Can The Witness create a second route-tracing recurrence without conflating
  endpoint, region and full-board constraints?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `GAME-0038` — The Swapper.
- Optimisation criterion: follow route / logistics reuse with the strongest
  mechanically independent retained Action-singleton falsifier.
- Expected information gain: test clone instantiation, synchronized body
  response, control-locus transfer, light-field permissions and fixed exit.
- Backlog impact: retain The Witness, Viewfinder and Carto.

## Sources consulted

- Official Cosmic Express press kit and Steam listing.
- Contemporary Pocket Gamer, Stuff, Big Boss Battle and eShopperReviews
  mechanical accounts.
