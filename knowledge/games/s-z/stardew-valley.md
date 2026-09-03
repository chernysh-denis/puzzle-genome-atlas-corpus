---
game_id: GAME-0089
slug: stardew-valley
game_title: Stardew Valley
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0089
gene_ids:
  action:
    - ACT-093
  system:
    - SYS-116
    - SYS-117
  constraint:
    - CON-136
    - CON-140
  information:
    - INF-001
    - INF-039
  objective:
    - OBJ-047
  time:
    - TIM-013
---

# Game: Stardew Valley

## Analysis scope

- Version / ruleset: unmodded Stardew Valley `1.6.15`, standard rather than
  remixed Community Center bundles, restricted to the Boiler Room after its
  scroll and all required inventory stacks are already available. The packet
  begins before any Boiler Room contribution and ends when the repaired
  minecarts become available on the following day.
- Included: the Blacksmith's Bundle's copper, iron and gold bars; the
  Geologist's Bundle's quartz, Earth Crystal, Frozen Tear and Fire Quartz; two
  distinct choices from the Adventurer's Bundle's 99 Slime, 10 Bat Wings,
  Solar Essence and Void Essence; inventory consumption; persistent filled
  slots and bundle completion; aggregate Boiler Room completion; the overnight
  Junimo repair; next-day four-stop minecart availability.
- Excluded: acquiring the supplied items; unlocking readable Junimo text and
  the Boiler Room; individual reward collection; every other Community Center
  room; remixed bundles; the Joja purchase route; farming, mining, combat,
  relationships, economy, story, multiplayer and platform-specific controls.
- Direct-play status: not conducted. ConcernedApe's official site establishes
  Community Center restoration as a core world-infrastructure arc. The official
  wiki's current standard-bundle table, bundle-data format and Minecart record
  agree on all types, quantities, quotas, group structure, end-of-day repair and
  next-day availability. The local verifier formalises only that bounded packet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SDV-001` | Stardew Valley is an open-ended country-life RPG released for PC on 26 February 2016, and restoring the old Community Center is a core route for repairing valley infrastructure | Confirmed | Direct | High | F1 |
| `SDV-002` | The current PC ruleset is 1.6.15 and standard versus remixed Community Center bundles are selected as different rulesets | Confirmed | Corroborated | High | S1, S4 |
| `SDV-003` | The standard Boiler Room contains Blacksmith's, Geologist's and Adventurer's Bundles, and completing all three repairs the minecarts | Confirmed | Direct | High | S1, S3 |
| `SDV-004` | Blacksmith's requires one Copper Bar, Iron Bar and Gold Bar; Geologist's requires one Quartz, Earth Crystal, Frozen Tear and Fire Quartz | Confirmed | Direct | High | S1, S2 |
| `SDV-005` | Adventurer's exposes four typed options with quantities and completes after any two distinct slots | Confirmed | Direct | High | S1, S2 |
| `SDV-006` | Bundle progress remains inspectable; accepted contributions fill persistent slots and each bundle completes independently | Confirmed | Corroborated | High | S1, S2, S5 |
| `SDV-007` | Room rewards resolve at the end of the day, and repaired minecarts become available the next day between Bus Stop, Mines, Quarry and Town | Confirmed | Direct | High | S1, S3 |
| `SDV-008` | The executable control proves nine accepted typed contributions, three persistent bundle completions, one 2-of-4 alternative, one next-day repair and six rejected invalid transitions | Observation | Direct | High | V1, SDV-003–SDV-007 |
| `SDV-009` | The room-level packet is not Day of the Tentacle's exact recipient set: it is a hierarchy of inanimate collection slots, and one group explicitly accepts alternatives | Observation | Corroborated | High | S1, S2 |

## Basic data

- Release / origin: developed by ConcernedApe and released for Windows on
  26 February 2016; the analysed PC ruleset is `1.6.15`.
- Platform or physical form: open-ended single-player country-life RPG with a
  persistent inventory, calendar, locations and world-progression state.
- Puzzle family: hierarchical typed donation bundles into delayed world repair.
- Primary source:
  - **[F1]** [Stardew Valley — official About page](https://www.stardewvalley.net/about/),
    for the release, genre and Community Center infrastructure-restoration arc.
- Reproducible corroboration:
  - **[S1]** [Stardew Valley Wiki — Bundles / Boiler Room](https://wiki.stardewvalley.net/Boiler_Room),
    for contribution rules, the three standard bundles, exact item quantities,
    individual and room rewards, end-of-day resolution and minecart repair.
  - **[S2]** [Stardew Valley Wiki — bundle data format](https://wiki.stardewvalley.net/Modding%3ABundles),
    for canonical item IDs, counts, minimum quality, slot quotas and Boiler Room
    bundle records `20`–`22`.
  - **[S3]** [Stardew Valley Wiki — Minecart](https://wiki.stardewvalley.net/Mine_Cart),
    for next-day availability and the four travel destinations.
  - **[S4]** [Stardew Valley Wiki — Version History](https://wiki.stardewvalley.net/Version_History),
    for current PC version `1.6.15`.
  - **[S5]** [Stardew Valley Wiki — Junimos](https://wiki.stardewvalley.net/Junimos),
    for item offerings, per-bundle collection and the room-wide valley
    improvement after all subordinate bundles.
  - **[V1]**
    [`verify_stardew_valley_control.py`](../../../scripts/verify_stardew_valley_control.py),
    an executable model of typed slots, group quotas, persistent completion and
    next-day minecart repair.

## Mechanical decomposition

### Player actions

- `ACT-093` — contribute inventory quantity to displayed collection slot. The
  player selects one compatible item stack and commits the exact displayed
  quantity to the addressed Boiler Room bundle requirement.

### System behaviours

- `SYS-116` — persistent typed-slot contribution completes collection group.
  Accepted quantities disappear from inventory, their filled slots persist,
  and the system independently completes the three-, four- or two-slot bundle.
- `SYS-117` — aggregate collection completion schedules world-service
  restoration. Once all three bundle-complete states coexist, the Boiler Room
  is marked complete and the minecart repair is scheduled for the day boundary.

### Constraints

- `CON-136` — persistent prerequisite-gated mechanism dependency. Filled slots
  precede bundle completion, all three bundle completions precede the room
  reward, and the overnight repair precedes minecart availability.
- `CON-140` — typed collection slots with fixed and alternative quotas. The
  Blacksmith's and Geologist's Bundles demand every displayed type; the
  Adventurer's Bundle accepts any two distinct displayed options at their
  respective quantities.

### Information

- `INF-001` — fully visible current state. Inventory quantities, displayed
  requirements, filled slots and bundle-complete markers are inspectable at
  every contribution decision.
- `INF-039` — visible typed collection schema and retained slot progress. Each
  scroll exposes item identity, count, any quality threshold, group quota and
  prior filled state without disclosing how to acquire the items.

### Objective

- `OBJ-047` — restore persistent world service through collection groups. The
  bounded packet completes by satisfying all Boiler Room bundles so the
  minecart travel network becomes permanently available.

### Time

- `TIM-013` — completed progression schedules next-day world update. The last
  contribution marks the room complete immediately, but Junimos repair the
  network overnight and minecart use begins the following day.

## Reproducible transitions

The executable control starts with every selected contribution already in
inventory and performs this accepted trace:

1. Contribute Copper Bar, Iron Bar and Gold Bar to complete Blacksmith's.
2. Contribute Quartz, Earth Crystal, Frozen Tear and Fire Quartz to complete
   Geologist's.
3. Contribute 99 Slime and 10 Bat Wings as two of Adventurer's four options.
4. Complete Adventurer's and thereby all three Boiler Room groups.
5. End the current day, scheduling the Junimo repair.
6. Begin the next day with the minecart service available.

Six controls reject a nonexistent room group, an unsupported type, an
insufficient stack, duplicate filling of one slot, end-of-day repair before all
three groups and next-day activation without a scheduled repair. A one-of-two
Adventurer partial state is separately asserted not to complete the room.

## Strategic and experiential structure

- Contribution order is flexible within and across bundles, so the long-term
  planning problem lies in sourcing item types while persistent slots externalise
  progress and reduce the remaining requirement set.
- Fixed and alternative schemas coexist. The first two bundles are all-of
  checklists, while Adventurer's lets the player substitute between four routes
  by completing any two distinct offered slots.
- Individual bundle rewards are immediate local incentives, but the bounded
  structural objective sits one hierarchy above them: every group must be
  complete before the world service changes.
- The overnight boundary separates proof of completion from capability. The
  player cannot use the minecarts on the same day as the final contribution.

## Replay and variation

- Standard bundle identities and quantities are fixed, but the order and chosen
  Adventurer pair vary with the player's inventory and acquisition history.
- Remixed bundles materially change the collection schemas and are a separate
  ruleset excluded from this record.
- The Joja route buys minecart repair with currency and therefore does not
  instantiate the same typed-slot combination.

## Adjacent systems and history

- Day of the Tentacle is the nearest corpus control because both preserve
  partial typed inventory transfers behind a dependency chain. Red is an
  addressed character who accepts one exact three-item set and constructs an
  object; Stardew's scrolls are persistent collection schemas, include a 2-of-4
  substitution, nest three groups and restore a service after a day boundary.
- Inbento exposes a complete typed recipe, but placements overwrite a small
  spatial product during one puzzle and do not persist as a campaign collection.
- Dorfromantik and Loop Hero grant infrastructure-like rewards, but their
  triggers do not consist of visible typed donation slots grouped under one
  aggregate completion predicate.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-093` | irreversible typed quantity contribution |
| System | `SYS-116`, `SYS-117` | persistent group completion; aggregate next-day service restoration |
| Constraint | `CON-136`, `CON-140` | dependency hierarchy; two fixed schemas and one 2-of-4 schema |
| Information | `INF-001`, `INF-039` | visible inventory/state; displayed schemas and filled slots |
| Objective | `OBJ-047` | permanently restore minecart travel |
| Time | `TIM-013` | end-of-day scheduling; next-day activation |

Compact signature:

`ACT-093; SYS-116,SYS-117; CON-136,CON-140; INF-001,INF-039; OBJ-047; TIM-013`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `88` (`GAME-0001`–`GAME-0088`).
- Exact genome matches: none.
- Tied near matches: `GAME-0088` — Day of the Tentacle (`2 / 16 = 0.125000`).
- Supported combination subsets: `COMB-0089`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0088`.

## Coverage decision

- Keep the seven new boundaries provisional but active: each is operationally
  required to distinguish persistent collection, alternative slot membership,
  aggregate room completion and calendar-delayed service from `GAME-0088`.
- Do not apply `ACT-091`, `SYS-115`, `CON-139`, `INF-038` or `OBJ-046`: the
  scroll is not an addressed character, one bundle accepts substitutes, and no
  completed inputs become a held constructed device.
- Next falsification target: a visible multi-group collection that retains
  progress and grants a persistent world capability immediately rather than at
  a calendar boundary, preferably without consuming inventory quantities.

## Confidence and open questions

### Assumptions

- The standard PC `1.6.15` data is analysed; remixed bundle selection is a
  materially different ruleset.
- The control selects Slime and Bat Wings for Adventurer's, but any two distinct
  listed options satisfy the same quota boundary.

### Unknowns

- Platform-specific input gestures and multiplayer contribution races were not
  directly inspected.
- The exact visual persistence of a partially filled slot across every platform
  was not direct-play verified; persistent bundle progress and current data
  structure are corroborated.

### Confidence

- High for types, quantities, bundle quotas, aggregate reward and next-day
  minecart availability.
- Medium-high for interaction-level presentation because direct play was not
  conducted.

## Combination candidate

- Candidate ID: `COMB-0089`.
- Gene set: `ACT-093`, `SYS-116`, `SYS-117`, `CON-140`, `INF-039`, `OBJ-047`,
  `TIM-013`.
- Supporting game: `GAME-0089`.
- Proper-subset rationale: `CON-136` and `INF-001` support the general
  prerequisite chain and inspectable state but do not define the nested typed
  collection, alternative quota or deferred service restoration.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `CON-136`, `INF-001`.
- Added genes: `ACT-093`, `SYS-116`, `SYS-117`, `CON-140`, `INF-039`,
  `OBJ-047`, `TIM-013`.
- Added combination: `COMB-0089`.
- Evidence gate: passed with the official product description, current standard
  bundle table, raw bundle schema, Junimo and Minecart records, plus one
  executable verifier.
- Nearest prior genome: Day of the Tentacle; see `Corpus comparison` for the
  current result.
- Next falsification target: a persistent visible multi-group collection whose
  final world capability resolves immediately rather than at a day boundary.

## Taxonomy impact

- Persistent typed contribution is now separated from addressed character
  hand-in: the destination can be an inanimate schema with quantity-bearing
  slots and no dialogue recipient.
- Exact all-of membership and distinct k-of-n substitution are parameters of
  one collection-slot constraint, while Day of the Tentacle's exact character
  commission remains narrower and is not reused.
- Group reward, aggregate area reward and activation time are separate axes:
  an immediate item reward does not explain a next-day world-service repair.

## Negative results

- Item acquisition, calendar strategy and mining routes do not support the
  bounded contribution genes because the verifier begins with supplied stacks.
- The Adventurer's Bundle disproves one exact nine-item room set: only two of
  four displayed monster-drop identities are required.
- Junimo animation is not a player construction action, and repaired minecarts
  are not an inventory object.
- Individual Furnace, Omni Geode and Small Magnet Ring rewards are adjacent
  outputs, not the aggregate objective.
- The verifier proves bundle membership, hierarchy and schedule, not remixed
  data, multiplayer races or platform-specific drag controls.
