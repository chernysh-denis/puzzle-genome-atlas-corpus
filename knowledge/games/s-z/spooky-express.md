---
game_id: GAME-0586
slug: spooky-express
game_title: Spooky Express
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-016
  system:
    - SYS-1728
    - SYS-1729
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
    - TIM-002
---

# Game: Spooky Express

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Draw the track and watch its service order as it grows. A single
carriage must serve two different passengers before leaving.

## Analysis scope

- Version / ruleset: English iPhone commercial iOS edition, App Store
  6738424828, full base release dated 21 October 2025 by the developer.
  Scope uses the release-window 1.0-series rules, Ghoulish Graveyard 7.
  The launch-day mobile recording links the iPhone listing.
  Its exact installed patch is not recoverable from the frames.
  App Store history explicitly records a later edit to Graveyard 2,
  which is a different board.
- Structured analysis target: PLAT-IOS.
  See [platform coverage](../../platforms/games.json).
- Entry: choose the seventh numbered puzzle in Ghoulish Graveyard after
  its ordinary unlock. Begin on the original board with no player-laid
  track, one empty carriage at the entry, one waiting zombie and one
  waiting vampire. Visible destinations are one grave and one coffin.
- Primary decision loop: drag the train from the fixed entrance or the
  current track end along adjacent floor cells. Each addition lays
  track and advances the train, so neighbouring passenger and
  destination interactions take effect as the route is extended.
  Keep the single carriage available in the required order and
  preserve unused floor for the rest of the track. Retract a chosen
  suffix or reset when the current route cannot complete the service.
- Positive exit: deliver the vampire to the coffin and the zombie to
  the grave, then reach the fixed exit. The solved board shows Continue.
  Stop at this clear boundary without opening another puzzle.
- Negative exit: a track that reaches the exit too early, or strands the
  train by exhausting the reachable unused cells, fails to complete.
  It remains revisable. No timed fail screen or best-length ranking
  enters this scope.
- Included: fixed grid and endpoints, direct route tracing, simple
  path legality, immediate capacity-gated boarding and typed
  alighting, reversible route effects, and a self-paced clear.
- Excluded: prerelease/demo builds, paid-entitlement verification,
  optional hint and achievement systems, other boards, PC or
  Android as targets, human and imp rules, multiple carriages,
  route-selection map interactions and exact animation timing.
- Potential scoped module: a later board with humans and monsters,
  where passenger interaction changes more than typed service.
- Direct-play status: not conducted. The iPhone-linked launch-day
  mobile guide and static frames corroborate the numbered board,
  incremental service and solved terminal. The independent written
  reports describe their own play of the same released rules with
  carrier and patch differences left open. No executable, video
  playback or audio was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SE-001 | The full commercial iOS game shipped in October 2025. The scoped numbered puzzle visibly has a fixed cell board, two distinct passengers, their two destinations and two track endpoints. | Confirmed | Direct | High | P1, P2, W1 |
| SE-002 | The player extends a simple track incrementally. After a legal extension the train advances and its current service status updates while later cells remain free to choose. | Observation | Corroborated | High | P2, W1, R1, R2 |
| SE-003 | The one-seat carriage cannot take another passenger when occupied. A grave serves the zombie and a coffin serves the vampire. The train serves eligible riders and stops automatically as it advances. | Observation | Corroborated | High | P1, P2, W1, R1 |
| SE-004 | Dragging back retracts track, allowing the player to revise a failed continuation. Changed load and service on erased segments are rolled back with the route, rather than permanently banked. Reset returns to the initial puzzle. | Observation | Corroborated | Medium | W1, R1, R2 |
| SE-005 | A confirmed Graveyard 7 route takes the vampire to the coffin first, then the zombie to the grave, and leaves by the exit only after both deliveries. Completion enters a Continue state. | Observation | Corroborated | High | W1, P2, R1 |

## Basic data

- Draknek & Friends. FAM-005 for a noncrossing route that must leave
  space for later pickups and delivery, and FAM-017 for the ordered
  service dependencies imposed by the single carriage.
- P1: [Official App Store product](https://apps.apple.com/us/app/spooky-express/id6738424828).
  Its version history records 1.0, release-window 1.0.2 and 1.0.3,
  and a November 1.0.4 change naming Graveyard 2. The base commercial
  unlock is a one-time purchase within the app; no purchase is
  asserted here.
- P2: [Draknek & Friends' dated press kit](https://spooky.express/press/).
  Gives 21 October 2025 and the single place, self-crossing restriction,
  train task, grave and coffin compatibilities.
- W1: [AppUnwrapper's release-day route and numbered solution stills](https://www.appunwrapper.com/2025/10/21/spooky-express-walkthrough-guide/).
  The companion [mobile recording](https://www.youtube.com/watch?v=rBezvm2Dd9I&t=180s)
  links the iOS store. Sampled frames at 3:00–3:15 show the starting
  board, partial track near the vampire, the empty vampire platform
  and service extending around it. At 3:15–3:25 the path reaches the
  grave and enters Continue. The Level 7 solution still shows the
  complete train line from its start and independently permits tile
  transcription. Still sampling does not identify sub-frame interactions.
- R1: [GamesRadar's October 24 direct-play account](https://www.gamesradar.com/games/puzzle/spooky-express-is-an-adorable-puzzle-game-that-has-me-mapping-out-tracks-in-trainsylvania-to-help-undead-passengers-and-its-perfect-for-halloween/).
  Describes moving forward to lay track, moving backward to undo,
  one-car service and reset.
- R2: [Electron Dance's written play account](https://www.electrondance.com/puzzleworks-11-spooky-express/).
  Independently describes the train moving as track is drawn rather
  than waiting for a separate launch action. Later asymmetric
  boards may impose different endpoint goals. Here the rider
  and destination counts are equal and both must be served.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-016 draws the next edge-connected segment from the entrance or
  route tip. Retracting the tracing gesture revises an earlier suffix
  (SE-002, SE-004).

### System Behaviour Genes

- SYS-1728 advances the train and handles local service during route
  extension, before the exit (SE-002, SE-003).
- SYS-1729 retracts service state with the route, so a changed branch
  repeats the relevant decision instead of inheriting its old riders
  or deliveries (SE-004).

### Constraint Genes

- CON-001 keeps the authored floor cells and fixture positions fixed.
  CON-029 requires a single edge-connected track with no reused cell,
  junction or crossing (SE-001, SE-002).
- CON-050 limits current occupancy to one. CON-051 pairs the vampire
  with the coffin and the zombie with the grave (SE-003).

### Information Genes

- INF-001 exposes the board, current track, train, riders and their
  local destinations. This makes currently blocked pickup and lost
  route space legible (SE-001–SE-003).

### Objective Genes

- OBJ-024 requires the two deliveries and then the exit. Passing a
  destination with no compatible rider does not fulfill it (SE-005).

### Time Genes

- TIM-002 permits untimed decisions between extensions. Train motion
  follows the player's extensions rather than an independent timetable
  that spends the decision time (SE-002, SE-004).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Empty carriage at the entry | Add legal track toward the vampire platform | The train moves during construction and takes an eligible rider while the remaining route is still open to editing. | SE-002, SE-003 |
| Vampire occupies the one carriage | Approach a grave or the other waiting rider first | Neither the incompatible stop nor the waiting rider can free or reuse the occupied place. | SE-003 |
| Occupied carriage at the coffin | Extend the path past the matching delivery side | The vampire leaves and frees the carriage before the later zombie pickup. | SE-003, SE-005 |
| Current suffix visited a platform | Retract past the boarding segment and take a different corridor | The earlier load and waiting state return with the retained path. The erased continuation confers no permanent delivery. | SE-004 |
| Both riders have left at their matched destinations | Extend the last stem into the exit | The board settles as complete and gives Continue. A route stranded before the exit remains incomplete. | SE-005 |

Normalize the visible floor as seven rows by seven columns, with the
entrance at the north edge next to (1,2) and the exit at the south
edge next to (7,6). The vampire platform is at (4,5), the coffin
beside the west edge at row 4, the zombie beside the north edge at
column 4 and the grave beside the south edge at column 4. The
documented route follows these grid waypoints, visiting all
intervening cells in order:

```text
Entry → (1,2) → (3,2) → (3,4) → (4,4) → (4,1) → (5,1)
      → (5,6) → (3,6) → (3,5) → (2,5) → (2,4) → (1,4)
      → (1,7) → (6,7) → (6,4) → (7,4) → (7,6) → Exit
```

This transcription specifies the path rather than an exact locomotive
or carriage contact frame. The first inward dogleg leaves the centre
platform on one side and the outside coffin on the other. The east
corridor keeps a later continuous route between the top zombie and
bottom grave. It enters no platform tile and never revisits a tile.

## Strategic and experiential structure

One place makes a locally available pickup costly if its proper drop-off
has been routed away. The path occupies scarce floor as it is built.
Service is legible immediately, making a bad branch reversible without
submitting a complete candidate. The challenge is to preserve the
space needed for the later leg of the route while serving the current
rider.

## Replay and variation

The recorded route is one clear, with no claim of uniqueness or shortest
length. Decorative post-clear motion may reuse the completed route;
it is separate from the acceptance decision. Later levels can change
types, interaction rules and endpoint demand.

## Adjacent systems and history

This is the released successor to Cosmic Express. The two games share
capacity and typed delivery constraints. The separate locked test run
of Cosmic Express is not required in the traced Spooky Express board.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-016 | edge-connected touch trace |
| System Behaviour | SYS-1728, SYS-1729 | incremental service and retractable suffix |
| Constraint | CON-001, CON-029, CON-050, CON-051 | fixed cells, simple route, one place, zombie/grave and vampire/coffin |
| Information | INF-001 | visible route, riders and endpoints |
| Objective | OBJ-024 | both deliveries and exit |
| Time | TIM-002 | untimed path extension |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `585` (`GAME-0001`–`GAME-0585`).
- Exact genome matches: none.
- Tied near matches: `GAME-0037` — Cosmic Express (`7 / 12 = 0.583333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Cosmic Express (`GAME-0037`) | ACT-016, CON-001, CON-029, CON-050, CON-051, INF-001, OBJ-024 | Both plan a single visible track with one place and typed deliveries. Cosmic Express launches a separate locked run. In this route each accepted extension executes new service, and erasing it rewinds those effects immediately. | `7 / 12 = 0.583333` |

### Preserved research notes

- New genes: SYS-1728 and SYS-1729.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_332](../../../research/taxonomy-changes/TAXONOMY_CHANGE_332.md)
  isolates service coupled to route extension and service-state rollback.

## Negative results

- SYS-031 does not describe the active solve. The player advances the
  vehicle during trace editing rather than launching it on a completed line.
- TIM-009 requires a separate locked traversal, and TIM-007 permits
  restoration of an independent running simulation. Neither describes
  this step-coupled route and its suffix.
- Board dimensions, passenger names, route coordinates and decorative
  motion remain parameters. No independent transfer priority is
  inferred for simultaneous contacts.

## Delta summary

## New facts

- [Observation | Corroborated | High] In this numbered puzzle one
  route construction advances the train and resolves typed pickups
  and drop-offs as the remaining track is still being authored.

## New genes

- [Observation | Corroborated | Medium] Two additions in TAXONOMY_CHANGE_332.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are listed in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- A native repeat could measure exact same-transition stop order
  when a pickup and a compatible delivery are both adjacent.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0587, Panzer Dragoon II Zwei.
  Reconstruct a complete released Saturn flight segment with route and
  lock-on decisions.
- Optimisation criterion: contrast a trace-controlled rail with the
  decisions within an authored on-rails shooter's movement.

## Why this game

- [Hypothesis | Limited | Medium] The launch-era seven-by-seven
  board isolates the service state changed by an in-progress design.
