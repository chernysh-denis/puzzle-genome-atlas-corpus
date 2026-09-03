---
game_id: GAME-0051
slug: mini-motorways
game_title: Mini Motorways
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0051
gene_ids:
  action:
    - ACT-006
    - ACT-025
    - ACT-068
  system:
    - SYS-004
    - SYS-029
    - SYS-030
    - SYS-032
    - SYS-092
  constraint:
    - CON-047
    - CON-049
    - CON-052
    - CON-098
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Mini Motorways

## Analysis scope

- Version / ruleset: current released desktop base game, ordinary Classic mode
  on Los Angeles without a Daily or Weekly modifier.
- Included unit: one complete Classic session from the initial house and
  matching destination through terminal destination overload and the final
  delivered-pin score.
- Included mechanics: tile-based road drawing and delayed reclamation;
  colour-coded houses, attached cars, destinations and pins; automatic
  dispatch, routing, pickup and return; procedural growth; finite road tiles;
  pause, normal and fast time; weekly road award and upgrade choice; ordinary
  Los Angeles bridge use; recoverable overload and scored failure.
- Excluded: Endless, Expert and Creative modes; challenges and modifiers;
  later maps, trains, ferries and map-specific rules; unlocks, leaderboards,
  GIF export, presentation and speedrunning.
- Direct-play status: not conducted. Developer product, support and design
  sources establish the live city, road, spawn, pin and mode boundaries. Four
  hands-on reviews independently reproduce dispatch, weekly awards, redraw and
  overload transitions. No particular generated layout is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MMW-001` | Classic play uses a persistent editable branching road graph built from finite road tiles | Confirmed | Corroborated | High | P1, D1, R1 |
| `MMW-002` | Houses and destinations appear over simulation time under weighted procedural placement rules | Confirmed | Direct | High | P1, D1 |
| `MMW-003` | Visible destination pins generate demand for an available connected car from a same-colour house | Confirmed | Corroborated | High | P2, R2, R3 |
| `MMW-004` | A dispatched house car follows the road graph to clear one pin and returns to its own house | Confirmed | Corroborated | High | P2, R2 |
| `MMW-005` | Each week grants road tiles and presents a bounded infrastructure choice | Confirmed | Corroborated | High | R1, R3, R4 |
| `MMW-006` | A bridge consumes finite infrastructure and road tiles while crossing Los Angeles water | Confirmed | Corroborated | High | R1, C1 |
| `MMW-007` | Excess pins start a visible recoverable overload warning; persistence ends Classic play | Confirmed | Corroborated | High | R1, R2, R4 |
| `MMW-008` | Completed trips raise the final session score | Confirmed | Corroborated | High | R2, R3 |
| `MMW-009` | `SYS-031`, `CON-050` and `CON-051` fail because cars neither board passengers nor carry bounded destination units | Observation | Corroborated | High | MMW-003–MMW-004 |
| `MMW-010` | The common Mini Metro relation is the smaller live-growth / finite-network / overload core recorded as `COMB-0051` | Observation | Corroborated | High | MMW-001–MMW-009 |

## Basic data

- Release / origin: Dinosaur Polo Club released Mini Motorways on Apple Arcade
  in 2019 and on Steam in 2021; the scoped current desktop base game retains
  ordinary Classic mode.
- Platform or physical form: single-player digital real-time network strategy
  game.
- Puzzle family: live finite-road-network demand management.
- Primary / creator sources:
  - **[P1]** [Official Steam page](https://store.steampowered.com/app/1127500/),
    for dynamic city growth, road drawing, redesign, upgrades and Classic
    survival framing.
  - **[P2]** [Dinosaur Polo Club support page](https://dinopoloclub.com/support/mini-motorways/),
    for destination-pin collection, mode boundaries and official support.
  - **[D1]** [Developer design interview](https://www.gamedeveloper.com/audio/-i-mini-motorways-i-and-the-delicate-art-of-marrying-complexity-and-minimalism),
    for finite road length, physical traffic capacity, weighted procedural
    house / destination regions and tile-based branching roads.
- Hands-on sources:
  - **[R1]** [Game Informer review](https://gameinformer.com/review/mini-motorways/contemplative-commute),
    for finite roads, pause, redraw, weekly awards and overload failure.
  - **[R2]** [NookGaming review](https://www.nookgaming.com/mini-motorways-review/),
    for same-colour house-car dispatch, pin pickup, round trip and deletion.
  - **[R3]** [Nintendo Insider review](https://www.nintendo-insider.com/mini-motorways-review/),
    for colour compatibility, trip score and weekly random upgrade choice.
  - **[R4]** [Pixelkin review](https://pixelkin.org/2022/05/23/mini-motorways-review/),
    for limited roads, bridge need, pin accumulation and Game Over.
- Narrow community control:
  - **[C1]** [Mini Motorways upgrade reference](https://mini-motorways.fandom.com/wiki/Upgrades),
    used only to corroborate ordinary bridge / road-tile inventory semantics.
- Claim IDs: `MMW-001`–`MMW-010`.

## Mechanical decomposition

### Action Genes

- `ACT-068` — edit persistent branching road network. The player draws,
  extends, redraws and marks road tiles for removal; intersections may branch
  and serve multiple house-destination routes.
- `ACT-025` — choose periodic network upgrade. At the weekly boundary the
  player selects one offered bundle such as a bridge, motorway, roundabout or
  traffic light plus roads.
- `ACT-006` — accelerate automatic progression. Pause and fast time change the
  live simulation rate; pause is a `TIM-003` parameter.
- `ACT-023` is absent because there is no named ordered station line.
- `ACT-024` is absent because cars remain attached to houses rather than being
  assigned among routes.
- Claim IDs: `MMW-001`, `MMW-005`.

### System Behaviour Genes

- `SYS-004` — the system selects placements, colours, demand timing and weekly
  offers through probability-governed processes.
- `SYS-029` — houses and destinations appear as simulation time advances.
- `SYS-030` — visible pins accumulate at destinations over time.
- `SYS-032` — each weekly boundary adds road capacity and presents a bounded
  infrastructure offer.
- `SYS-092` — a pin dispatches an available compatible house car, which drives
  to the destination, clears demand and returns home.
- `SYS-031` is absent: no passenger boards, transfers or exits a route vehicle.
- Resolution order: time creates nodes and pins; a connected destination
  requests an eligible car; the car reserves and follows its current path,
  removes one pin on arrival, returns home and becomes available again; node
  overload, weekly rewards and terminal checks update around this service.
- Claim IDs: `MMW-002`–`MMW-005`.

### Constraint Genes

- `CON-047` — road tiles, bridges and other upgrades are finite reusable
  inventory; marked road tiles return only after current traffic releases them.
- `CON-049` — an ordinary road crossing Los Angeles water consumes an
  available bridge and its road-tile length while deployed.
- `CON-052` — sustained destination overload terminates the session after a
  visible grace interval; sufficient service can reverse the warning.
- `CON-098` — only an available car from a same-colour connected house may
  answer a destination pin.
- `CON-048` is absent because one road network may branch at intersections.
- `CON-050` is absent because each car carries no bounded passenger set; road
  throughput and attached-car availability are different constraints.
- `CON-051` is absent because the demand remains at the destination and calls a
  compatible origin, the reverse of passenger destination completion.
- Claim IDs: `MMW-001`, `MMW-003`, `MMW-006`, `MMW-007`, `MMW-009`.

### Information Genes

- `INF-001` — current houses, destinations, pins, cars, roads, inventory,
  warning state, time and score are visible.
- `INF-002` — the identity, position and timing of the next generated house,
  destination or pin are not previewed.
- Claim IDs: `MMW-002`, `MMW-003`, `MMW-007`.

### Objective Genes

- `OBJ-002` — maximise the number of completed trips before terminal overload.
- Overload is the failure constraint `CON-052`, not a separate objective.
- Claim IDs: `MMW-007`, `MMW-008`.

### Time Genes

- `TIM-003` — nodes, demand and traffic advance by real time while the player
  may edit the network; pause permits planning without changing that running
  schedule classification.
- Claim IDs: `MMW-002`–`MMW-007`.

## Reproducible transitions

| Before | Player action or elapsed event | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One house and same-colour destination are disconnected | Draw a continuous road between their entrances | The graph becomes traversable without assigning a car | Road editing is separate from dispatch | `MMW-001` |
| A connected destination has one pin and a matching house car is parked | Let simulation time advance | The car leaves home, follows the graph, clears one pin and returns | Origin-bound automatic round trip | `MMW-003`, `MMW-004` |
| A blue house shares roads with a red destination | A red pin appears | The blue car remains ineligible despite connectivity | Compatibility is origin/destination colour | `MMW-003` |
| Cars occupy a road section | Mark that section for deletion | Existing traffic completes its use before tiles return to inventory | Reclamation is delayed and finite | `MMW-001` |
| A proposed road crosses water with no free bridge | Attempt the crossing | The crossing cannot be retained until a bridge is available | Geography gates finite infrastructure | `MMW-006` |
| The weekly boundary arrives | No road command | Road tiles are granted and an upgrade choice interrupts ordinary play | Periodic award and selection are distinct | `MMW-005` |
| Pins exceed a destination's service tolerance | Allow time to pass | A visible overload warning grows toward failure | Overload has a grace interval | `MMW-007` |
| Matching cars arrive before the warning fills | Continue service | Pins and warning pressure fall; play continues | Overload is recoverable | `MMW-007` |
| Any overload warning completes | Let time advance | Classic play ends and completed-trip score is final | Local failure terminates global score run | `MMW-007`, `MMW-008` |

## Strategic and experiential structure

- Local decision: spend scarce road length on the nearest compatible link or
  preserve tiles for a likely crossing and future growth.
- Medium-term planning: separate colour flows, reduce intersections, control
  trip length and redeploy reclaimed roads or weekly upgrades.
- Long-term structure: keep the branching graph adaptable as weighted but
  unpreviewed houses, destinations and demand expand the city.
- Common colour segregation and spawn-blocking techniques are strategies, not
  additional rules or genes.

## Replay and variation

- Weighted procedural placement, destination schedule, demand and weekly offers
  vary while the Los Angeles geography and Classic rules stay within scope.
- Identical connectivity can produce different throughput because trip length,
  intersections and simultaneous cars occupy physical road space.
- Expert permanence, challenge modifiers and map-specific systems would change
  the genome boundary and remain excluded.

## Adjacent systems and history

- Mini Metro shares live growth, finite infrastructure, score and overload,
  but uses named unbranched lines, route-assigned trains and passengers.
- Freeways separates construction from simulation and remains the strongest
  timing control for a subsequent bounded analysis.
- Pipe Mania accepts live edits during forced progression but consumes queued
  tiles into one advancing flow rather than servicing generated demand.
- Claim IDs: `MMW-009`, `MMW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-025`, `ACT-068` | pause input, edit gesture |
| System Behaviour | `SYS-004`, `SYS-029`, `SYS-030`, `SYS-032`, `SYS-092` | spawn weights, dispatch priority |
| Constraint | `CON-047`, `CON-049`, `CON-052`, `CON-098` | road count, bridge count, grace duration |
| Information | `INF-001`, `INF-002` | warning rendering, colour-blind encoding |
| Objective | `OBJ-002` | score display |
| Time | `TIM-003` | pause and fast-forward rates |

Canonical signature:

`ACT-006,ACT-025,ACT-068; SYS-004,SYS-029,SYS-030,SYS-032,SYS-092; CON-047,CON-049,CON-052,CON-098; INF-001,INF-002; OBJ-002; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `50` (`GAME-0001`–`GAME-0050`).
- Exact genome matches: none.
- Tied near matches: `GAME-0018` — Mini Metro (`13 / 22 = 0.590909`).
- Supported combination subsets: `COMB-0051`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0018`.

### Preserved research notes

- New recurring combination: `COMB-0051`, the shared finite live-network,
  generated-demand, score and sustained-overload interaction.
- New genes: `ACT-068`, `SYS-092`, `CON-098`.
- Reused genes: `ACT-006`, `ACT-025`, `SYS-004`, `SYS-029`, `SYS-030`,
  `SYS-032`, `CON-047`, `CON-049`, `CON-052`, `INF-001`, `INF-002`, `OBJ-002`,
  `TIM-003`.
- Classification result: `New gene` with a deliberately smaller recurring
  combination; no novelty claim.

## Combination record

- `COMB-0051` recurs across Mini Metro and Mini Motorways while excluding their
  incompatible route, vehicle, passenger and graph representations.
- Exhaustive supporter scan: exactly `GAME-0018` and `GAME-0051` contain the
  complete proper subset.

## Taxonomy impact

- Generalised the labels and examples of `SYS-029`, `SYS-030` and `CON-052`
  from station-only wording to representation-neutral service nodes. Their
  causal boundaries and every prior signature remain unchanged.
- Added three separately observable road-graph, house-car and origin-class
  records. No merge, split, lifecycle change or type move is required.

## Negative results

- `COMB-0018` is not reused wholesale despite the direct product lineage.
- `COMB-0037` remains passenger-specific and does not match pins requesting
  empty house-bound cars.
- Freeways remains an external timing control rather than evidence for this
  live Classic signature.
