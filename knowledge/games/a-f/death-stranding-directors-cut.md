---
game_id: GAME-0310
slug: death-stranding-directors-cut
game_title: "DEATH STRANDING DIRECTOR’S CUT"
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-199
    - ACT-469
    - ACT-470
    - ACT-471
    - ACT-472
  system:
    - SYS-036
    - SYS-896
    - SYS-897
    - SYS-898
    - SYS-899
  constraint: []
  information:
    - INF-075
    - INF-258
    - INF-345
    - INF-346
  objective:
    - OBJ-014
  time:
    - TIM-003
---

# Game: DEATH STRANDING DIRECTOR'S CUT

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Smart Drugs,
Capital Knot City, Sam, Odradek and named interface labels are parameters or
product terms, not gene names.

## Analysis scope

- Version / ruleset: English Windows Steam base product for DEATH STRANDING
  DIRECTOR'S CUT, public-branch build `13300582`, checked 2026-09-19. The build
  number is a secondary distribution observation, not mechanical authority.
  No modification, transferred save, online connection, shared cargo or
  crossover content enters the target.
- Structured analysis target: Windows PC Director's Cut through Steam; see
  `GAME-0310` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup: begin a fresh offline game on Normal difficulty in English. The
  opening package is Order No. 1, Smart Drug Delivery to Capital Knot City.
  Exact package placement, route markers and incidental pickups are parameters.
- Entry: begin at the first controllable outdoor state after the opening cargo
  is dropped and Order No. 1 can be recovered.
- Primary decision loop: scan the nearby terrain and cargo; recover the Smart
  Drugs; distribute carried packages across compatible body positions; read
  weight, balance, stamina, cargo condition and terrain; place linked map
  markers; walk, brace the shifting load and revise the line through slopes,
  rocks and water; commit the required package to Capital Knot City's delivery
  terminal; inspect the accepted delivery result.
- Positive terminal: the Delivery Results surface accepts at least one required
  Smart Drugs consignment for Order No. 1 at Capital Knot City. Exact grade,
  Likes and route statistics are parameters. Persistence after closing and
  reloading was not observed and is not part of this terminal.
- Negative terminal: required cargo is not accepted because it is absent or no
  longer eligible, or the bounded attempt is abandoned before delivery. A
  later retry is a separate trace.
- Included: direct on-foot traversal; prompted cargo pickup and compatible body
  attachment; cargo arrangement; total carried mass and centre of gravity;
  left/right bracing; stamina and balance feedback; uneven terrain, shallow
  water, slopes, falls and package impacts; container/cargo condition; Odradek
  terrain-and-cargo scan; linked map markers; the fixed receiver; accepted
  quantity, condition-aware delivery evaluation, Likes and grade.
- Excluded: later story orders; vehicles; roads, bridges, generators and other
  constructed infrastructure; ladders, climbing anchors and specialised
  equipment; combat, MULEs, BTs and boss encounters; other regions; online
  Social Strand System state, signs, shared structures, lost-player cargo and
  other players' routes; crossover missions; firing range, race track, ranked
  orders, replay, account progression and complete-product mastery.
- Reproducible parameterisation: Windows Steam public build `13300582`, fresh
  English profile, Normal difficulty, offline. Recover the opening Smart Drugs,
  demonstrate manual or automatic cargo arrangement, use an Odradek scan, place
  at least two linked route markers, traverse on foot while demonstrating
  balance correction, and stop at the first accepted Order No. 1 Delivery
  Results surface. Exact route, weather exposure, falls, package placement,
  grade and Likes are parameters.
- Potential scoped modules: direct installed-build verification; save/reload;
  later orders; construction; vehicles; combat; networked Strand state;
  another difficulty or platform; and Director's Cut additions each require a
  separate scope.
- Direct-play status: not conducted. Official Kojima Productions and
  PlayStation guides directly establish cargo arrangement, mass, centre of
  gravity, bracing, stamina, terrain, scanning, route markers, damage and
  delivery grading. Official product pages establish Windows identity and the
  separable network layer. Static written order records corroborate the exact
  opening order, package and destination. No video or audio was opened, played,
  heard or analysed; no installed build, save or reload trace was available.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DSDC-001` | The target is the Windows Director's Cut base product on the observed Steam public build, with online and later content excluded | Confirmed | Direct | High | P1, P2, P5, S1 |
| `DSDC-002` | The opening bounded order requires one or more Smart Drugs consignments delivered to Capital Knot City | Confirmed | Corroborated | High | S2, S3, S4 |
| `DSDC-003` | Cargo can be attached to compatible body positions and rearranged manually or automatically around a visible centre of gravity | Confirmed | Direct | High | P1, P3 |
| `DSDC-004` | Carried mass and placement affect balance, movement and stamina; left/right grips can brace a shifting load | Confirmed | Direct | High | P1, P3 |
| `DSDC-005` | Rough terrain, water, sharp turns, low stamina and overload raise stumble or fall risk | Confirmed | Direct | High | P1, P3 |
| `DSDC-006` | Falls, drops and Timefall can damage the container or cargo, and cargo condition contributes to delivery evaluation | Confirmed | Direct | High | P1, P3, P4 |
| `DSDC-007` | Odradek scanning reveals nearby terrain risk and cargo while map markers can be linked into a player-authored route | Confirmed | Direct | High | P1, P3 |
| `DSDC-008` | Delivery Results grade the accepted order using visible delivery factors and award Likes | Confirmed | Direct | High | P3, P4 |
| `DSDC-009` | No Windows installation, direct traversal, result acceptance, save or reload was observed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: KOJIMA PRODUCTIONS developed the Windows Director's Cut,
  published by 505 Games on Steam and Epic Games Store on 2022-03-30.
- Platform or physical form: Windows PC digital release; offline single-player
  opening order selected from a product that also has a separable online layer.
- Puzzle family: physics and object manipulation; route planning and delivery;
  real-time system pressure.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [Kojima Productions beginner's guide](https://www.kojimaproductions.jp/en/death-stranding-directors-cut-beginners-guide),
    for cargo placement, weight colours, centre of gravity, auto-arrange,
    stamina, topographic map, linked markers, terrain and cargo damage.
  - **[P2]** [Kojima Productions PC release](https://www.kojimaproductions.jp/en/death-stranding-directors-cut-available-today-for-pc),
    for the 2022-03-30 Windows Director's Cut release and store identities.
  - **[P3]** [Kojima Productions Eastern Region guide](https://kojimaproductions.jp/en/DSTips),
    for Odradek scanning, rough-terrain/load coupling, bracing, stamina, falls,
    Timefall, cargo condition and delivery rating.
  - **[P4]** [PlayStation delivery tips](https://blog.playstation.com/?p=220222),
    for delivery-grade factors including time, cargo weight and condition.
  - **[P5]** [official product page](https://www.kojimaproductions.jp/en/death-stranding-dc),
    for Director's Cut identity and the separable Social Strand System.
- Corroborating static written sources, accessed 2026-09-19:
  - **[S1]** [Steam product record](https://store.steampowered.com/app/1850570/DEATH_STRANDING_DIRECTORS_CUT/),
    for Windows, single-player, publisher and release metadata.
  - **[S2]** [Order No. 1 reference](https://deathstranding.fandom.com/wiki/Order_No._1%3A_Smart_Drug_Delivery),
    for the opening order number, Smart Drugs and Capital Knot City receiver.
  - **[S3]** [static Order No. 1 walkthrough](https://guides4gaming.com/death-stranding-quest-guide-order-1-smart-drug-delivery/),
    for recovery after the opening drop and delivery to the fixed terminal.
  - **[S4]** [static delivery-order list](https://samurai-gamers.com/death-stranding/delivery-order-list/),
    for the first main order's required one-or-more-package acceptance.
- Distribution observation: SteamCMD API reported public-branch build
  `13300582`, timestamp 2024-01-29, when checked 2026-09-19.
- Research record: **[R1]** local preflight found no Windows installation,
  entitlement, save, direct input trace or reload result.
- Claim IDs: `DSDC-001`–`DSDC-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` covers direct on-foot movement and `ACT-199` covers
  recovering a reachable package into a compatible carried/body slot.
- New `ACT-469` redistributes carried packages across body and pack positions,
  directly or through auto-arrange. New `ACT-470` holds the left, right or both
  balance grips to brace a shifting body-carried load. New `ACT-471` emits one
  Odradek pulse to survey nearby terrain and cargo. New `ACT-472` places and
  links topographic map markers into a prospective walking line.
- Parameters: package, slot, placement, arrange mode, braced side, scan origin,
  revealed objects, marker coordinates and route order. Claims:
  `DSDC-002`–`DSDC-007`.

### System Behaviour Genes

- Existing `SYS-036` integrates the avatar and carried stack through gravity,
  momentum, collisions, slopes and water in real time.
- New `SYS-896` composes package mass and body placement into a moving centre
  of gravity. New `SYS-897` couples that load state, terrain, momentum, stamina
  and bracing to movement cost, sway, stumble and fall. New `SYS-898` propagates
  Timefall, drops and impacts through container protection into cargo condition.
  New `SYS-899` accepts the delivered quantity and converts condition and route
  performance into the order's grade and Likes.
- Resolution order: attach and arrange cargo; derive mass and centre of gravity;
  scan or author a route; integrate movement and terrain; spend/recover stamina;
  apply bracing and balance resolution; propagate any impact or Timefall damage;
  submit eligible cargo; settle Delivery Results. Claims:
  `DSDC-003`–`DSDC-008`.

### Constraint Genes

- No new independent constraint is asserted. Compatible attachment belongs to
  `ACT-199`; carrying limits and overload are inputs to the coupled load system
  rather than a hard legality boundary in the evidenced opening packet.
- Scarce strategic resources: carried capacity, stable package placement,
  stamina, footing, time exposed to rain and retained cargo condition.

### Information Genes

- Existing `INF-075` exposes stamina and personal capacity pressure;
  `INF-258` exposes surface geometry, body pose, local hazard and fall risk
  without giving a solved route.
- New `INF-345` exposes the cargo stack's identities, positions, total mass,
  capacity, centre of gravity, container/cargo condition and delivery result.
  New `INF-346` exposes the Odradek scan and linked topographic markers while
  leaving route choice to the player.
- Claims: `DSDC-003`–`DSDC-008`.

### Objective Genes

- Existing `OBJ-014` covers committing the required portable Smart Drugs to
  Capital Knot City's fixed delivery terminal. Grade and Likes evaluate the
  accepted terminal but no minimum grade beyond acceptance is required.

### Time Genes

- Existing `TIM-003` covers live body dynamics, stamina, water, shifting load,
  falls and weather exposure while player input remains available.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening cargo lies near the courier | Recover the Smart Drugs | Required package enters a compatible carried position | portable payload acquisition | `DSDC-002`, `DSDC-003` |
| Multiple packages occupy the body stack | Move one package or invoke auto-arrange | Stack positions and centre of gravity change | placement is mechanically meaningful | `DSDC-003` |
| Stack leans while terrain remains live | Hold the threatened side's grip | Brace input opposes the current shift but restricts the live posture | active balance correction | `DSDC-004` |
| Rough ground and cargo are nearby | Trigger an Odradek scan | Terrain-risk colouring and cargo markers become visible | local survey, not solved route | `DSDC-007` |
| Map is open | Place at least two ordered markers | Markers become a linked prospective walking line | player-authored route scaffold | `DSDC-007` |
| Loaded courier crosses uneven terrain or water | Walk and revise direction/bracing | Mass, placement, footing, momentum and stamina resolve into sway, cost or fall | coupled traversal pressure | `DSDC-004`, `DSDC-005` |
| Package is exposed to rain or impact | Continue exposure or fall/drop it | Container protection and cargo condition can deteriorate | delivery object retains condition | `DSDC-006` |
| Capital Knot City terminal is reached with eligible Smart Drugs | Commit the delivery | Receiver accepts required quantity and opens Delivery Results | fixed-receiver objective | `DSDC-002`, `DSDC-008` |
| Accepted order has route and cargo measurements | Inspect results | Condition and performance become grade and Likes | explicit evaluated terminal | `DSDC-006`, `DSDC-008` |

## Strategic and experiential structure

- Local decision: foot placement, direction, scan timing, route-marker order,
  package arrangement and which side to brace.
- Medium-term planning: trade a shorter hazardous line against stable footing,
  stamina recovery and protection of the required cargo.
- Long-term structure: preserve an acceptable consignment until the fixed
  terminal; higher grade is optional optimisation, not the bounded success.
- Common heuristics: keep the centre of gravity close to the body, scan before
  committing to uncertain slopes or water, brace early, and detour when a
  shorter line would consume stability or cargo condition.
- Failure attribution: overload, poor arrangement, low stamina, unread terrain,
  late bracing, fall, weather exposure and ineligible cargo remain distinct.
- Player trust: pose, sway, stamina, load colours, centre of gravity, scan,
  terrain, cargo condition and Delivery Results expose the causal chain.

## Replay and variation

- What changes: package arrangement, marked route, footing, weather exposure,
  stamina, falls, condition, grade and Likes.
- Randomness or procedural generation: this opening route is not claimed as
  procedurally generated; local traversal outcomes vary with player line and
  physical state.
- Multiple viable strategies: a direct risky crossing and a longer stable line
  can both satisfy the order with different result quality.
- Replay motive: improve condition and grade, test another arrangement or route,
  or enter later excluded systems.

## Adjacent systems and history

- Euro Truck Simulator 2 also transports condition-bearing cargo to a fixed
  receiver and evaluates one delivery. Death Stranding moves that pressure onto
  an articulated body stack whose placement changes balance and stamina rather
  than onto a truck, trailer, deadline and parking bay.
- PEAK shares real-time terrain reading, body feedback, stamina and carried
  weight. Death Stranding adds addressable package placement, active side
  bracing, a scan/map route scaffold and condition-aware delivery settlement.
- Bonfire Peaks shares a portable payload objective but not live body balance,
  cargo degradation or evaluated route performance.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-199`, `ACT-469`, `ACT-470`, `ACT-471`, `ACT-472` | movement, pickup, arrangement, bracing, scan and route markers |
| System Behaviour | `SYS-036`, `SYS-896`, `SYS-897`, `SYS-898`, `SYS-899` | body dynamics, centre of gravity, traversal pressure, condition and result |
| Constraint | — | no independent hard legality boundary asserted |
| Information | `INF-075`, `INF-258`, `INF-345`, `INF-346` | stamina, terrain, cargo stack, scan and results |
| Objective | `OBJ-014` | deliver required Smart Drugs to fixed terminal |
| Time | `TIM-003` | continuous traversal and exposure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `309` (`GAME-0001`–`GAME-0309`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`3 / 22 = 0.136364`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0112` — Human: Fall Flat | `ACT-008`, `SYS-036`, `TIM-003` | Both expose direct movement through continuously resolved body physics. DEATH STRANDING adds addressable body cargo, spatial centre of gravity, active bracing, terrain survey, route planning, condition degradation and evaluated delivery; Human: Fall Flat instead uses two free-gripping arms, a crate, climbing and a visible avatar-exit objective. | Near, `0.136364` |

## Taxonomy impact

- Registry changes: add ten Active genes and DEATH STRANDING support to seven
  compatible existing boundaries; no prior signature or lifecycle changes.
- Taxonomy-change record: none; no existing definition is broadened.
- Candidate terms affected: Smart Drugs, Capital Knot City, Sam, Odradek,
  Timefall, Likes, Normal and Order No. 1 remain product terms or parameters.

## Negative results

- No installed Windows build, direct input trace, accepted result, save or
  reload exists; exact defaults, key bindings, grade values and persistence are
  not asserted.
- Build `13300582` is a distribution observation, not evidence for mechanics.
- Exact opening route and order details rely on corroborating static sources;
  broader mechanics rely on official guides.
- Later construction, vehicles, combat and networked assistance are excluded
  even where official sources document them.

## Delta summary

## New facts

- [Confirmed | Direct | High] Official guides establish cargo placement,
  centre of gravity, bracing, scan, terrain, stamina, condition and delivery
  grading (`DSDC-003`–`DSDC-008`).
- [Confirmed | Corroborated | High] Static order records establish the exact
  opening payload and fixed receiver (`DSDC-002`).

## New genes

- [Confirmed | Direct | High] `ACT-469`–`ACT-472`, `SYS-896`–`SYS-899`,
  `INF-345` and `INF-346` isolate reusable cargo-arrangement, balance,
  terrain-survey, route, condition and evaluated-delivery boundaries.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is asserted;
  the deterministic subset scan is recorded after index generation.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier game signature or lifecycle changes;
  seven compatible existing records gain only a support citation.

## New questions

- Which exact grade thresholds and Like coefficients apply to Order No. 1 in
  the observed Windows public build?
- Does its accepted result reproduce identically after a verified close and
  reload on a fresh offline profile?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0311` — Super Mario Bros. Wonder,
  Nintendo Switch base product.
- Optimisation criterion: contrast continuous condition-bearing delivery with
  a bounded authored platforming course and its state transformations.
- Backlog impact: `GAME-0311` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | Medium] DEATH STRANDING tests whether an iconic
  traversal game decomposes into portable balance, scan, route and evaluated
  delivery rules rather than being reduced to theme, walking or generic cargo.
