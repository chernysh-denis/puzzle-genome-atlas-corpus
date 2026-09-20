---
game_id: GAME-0330
slug: silent-hill-2-2024
game_title: Silent Hill 2 (2024 remake)
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-089
    - ACT-090
    - ACT-131
    - ACT-161
    - ACT-341
    - ACT-356
  system:
    - SYS-045
    - SYS-063
    - SYS-215
    - SYS-578
    - SYS-755
  constraint:
    - CON-210
    - CON-282
    - CON-296
    - CON-442
    - CON-579
  information:
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-359
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Silent Hill 2 (2024 remake)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). James Sunderland,
South Vale, Neely's Bar, Wood Side Apartments, named inventory items and the
juke-box configuration are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: North American English PlayStation 5 Standard Edition,
  product `UP0101-PPSA08710_00-MAINGAME00000000`, released 2024-10-08, fresh
  New Game with Combat Challenge and Puzzle Challenge both set to Standard.
  The installed patch and exact console firmware were not observed. This is
  the 2024 remake, not the 2001 PlayStation 2 original, PC edition, Deluxe
  Edition, New Game Plus or a modification.
- Structured analysis target: licensed PlayStation 5 Standard Edition; see
  `GAME-0330` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: navigate James through fog-limited Eastern South
  Vale; inspect the partial map and local interactables; use sight, spatial
  sound and the carried radio's static to judge nearby monsters; evade or
  strike when passage is threatened; collect the two broken record halves,
  vinyl glue, juke-box button and one coin; combine the record, restore and
  operate the juke box, receive the bar key, then follow the resulting key
  chain until the Wood Side Apartments entrance becomes traversable.
- Entry: first ordinary control at the observation-deck restroom after the
  opening mirror scene, before leaving toward the cemetery.
- Positive terminal: James uses the Wood Side Apartments Key at the main
  entrance, crosses the threshold and ordinary control resumes inside the
  lobby. No apartment room, puzzle, enemy or save fixture is admitted.
- Negative state: depleted health ends the current attempt. Exact checkpoint,
  Continue and save-state replacement semantics were not verified and do not
  enter the signature.
- Included: direct third-person walking and running; contextual examination,
  pushing and fixture operation; addressed item pickup; the wooden plank;
  carefully timed directional dodges; first-route melee; autonomous nearby
  monsters; one continuous health pool and finite healing items; local sight
  and spatial sound; radio static as a nondirectional nearby-threat signal;
  partial map and marked route state; item identities and compatibility;
  breaking the required Groovy Music window; combining the two broken records
  with vinyl glue into one repaired record; inserting and operating juke-box
  components; the coin result; Neely's Bar Key; the chained back-alley route;
  the Wood Side Apartments Key; typed key consumption and final arrival.
- Excluded: the first save square as a persistence claim; exact damage,
  invulnerability or enemy-health numbers; firearm combat; every interior
  room, puzzle and monster in Wood Side Apartments; Pyramid Head; Maria;
  endings; collectibles not causally required by this route; New Game Plus;
  Deluxe content; achievements as goals; accessibility options as mechanics;
  PC-specific controls and performance; later patches, mods, trainers,
  glitches, speedrun routes, screenshots, video and audio evidence.
- Reproducible parameterisation: start New Game on Standard/Standard and take
  the ordinary Eastern South Vale route. Acquire the map, radio and wooden
  plank; pass or defeat route-blocking monsters. At Neely's Bar inspect the
  disabled juke box and take the first broken record. Take the second record
  and glue from Groovy Music, the coin from the Texan Cafe register and the
  juke-box button through the Saul Street Apartments route. Combine the record
  pieces with the glue, configure the juke box, insert the record, button and
  coin, then select the declared track to receive Neely's Bar Key. Use it on
  the bar's locked continuation, move the trolley, climb through, inspect the
  clothes in the back alley for the Wood Side Apartments Key, then use that
  key and cross the apartment entrance. Exact combat contacts, healing spends,
  inspected optional notes and elapsed time are parameters.
- Potential scoped modules: one Wood Side apartment route, one firearm packet,
  one boss encounter, one ending and New Game Plus require separate terminals
  and evidence.
- Direct-play status: not conducted. No PS5, entitlement, installed build,
  controller trace, save, screenshot, video or audio was used. Konami and
  PlayStation establish product identity, release, camera, expanded map,
  combat and timed dodge; three independent written routes establish the
  bounded item-and-fixture chain. This is a source-bounded reconstruction, not
  a claimed playthrough or patch test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SH2R-001` | The packet is the 2024 PS5 Standard Edition product `PPSA08710`, separate from the 2001 original, PC and Deluxe products | Confirmed | Direct | High | P1, P2, P3 |
| `SH2R-002` | The remake uses an over-the-shoulder view, expanded explorable spaces and updated combat with carefully timed dodges | Confirmed | Direct | High | P1, P2, P3 |
| `SH2R-003` | Dense fog limits visibility, local sound exposes nearby action and radio static warns that a monster is nearby without disclosing its exact position | Confirmed | Corroborated | High | P3, P4 |
| `SH2R-004` | The Eastern South Vale route supplies the map, radio, wooden plank and first live monsters before the juke-box chain | Observation | Corroborated | High | S1, S2 |
| `SH2R-005` | The route collects two broken records, glue, a button and a coin, repairs the record, reconfigures the juke box and receives Neely's Bar Key | Observation | Corroborated | High | S1, S2, S3 |
| `SH2R-006` | Neely's Bar Key opens a continuation through a moved trolley and climb, whose back alley contains the Wood Side Apartments Key | Observation | Corroborated | High | S1, S2 |
| `SH2R-007` | Using the apartment key and crossing the entrance settles the bounded South Vale route at ordinary lobby control | Observation | Corroborated | High | S1, S2 |
| `SH2R-008` | Standard combat admits direct melee, carefully timed dodge, health loss and finite healing while nearby monsters act continuously | Strong Pattern | Corroborated | Medium | P3, S1, S2 |

## Basic data

- Release / origin: Bloober Team and Konami Digital Entertainment; PS5 and
  Windows release 2024-10-08.
- Platform or physical form: North American PlayStation 5 Standard Edition,
  one-player offline product `UP0101-PPSA08710_00-MAINGAME00000000`.
- Puzzle family: inventory and fixture dependencies; ordered dependency
  sequencing; local-threat exploration; real-time system pressure.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [Konami launch announcement](https://www.konami.com/games/us/en/topics/2440/),
    for the 2024-10-08 release, PS5/Steam products, expanded exploration,
    over-the-shoulder view and revamped combat.
  - **[P2]** [Konami product page](https://www.konami.com/games/eu/en/products/silenthill2r/),
    for publisher, remake identity, platforms and release date.
  - **[P3]** [PlayStation Store Standard Edition record](https://store.playstation.com/en-us/product/UP0101-PPSA08710_00-MAINGAME00000000),
    for exact product identity, one-player offline PS5 support, Standard versus
    Deluxe contents, expanded map, fog, over-the-shoulder camera and carefully
    timed dodge.
  - **[P4]** [PlayStation Blog gameplay overview](https://blog.playstation.com/2024/05/30/silent-hill-2-launches-october-8-new-gameplay-revealed/),
    for visibility-limiting fog, radio cues for nearby monsters, updated
    combat and altered remake puzzles.
- Corroborating textual sources, accessed 2026-09-21:
  - **[S1]** [Silent Hill Memories Eastern South Vale walkthrough](https://www.silenthillmemories.net/sh2_remake/walkthrough_01_eastern_south_vale_en.htm),
    for the complete map/radio, Groovy Music, Texan Cafe, Saul Street, juke-box,
    bar-key, trolley, alley-key and apartment-entry order.
  - **[S2]** [PowerPyx South Vale East route](https://www.powerpyx.com/silent-hill-2-remake-south-vale-east-collectible-locations/),
    for an independently ordered route, point-of-no-return boundary and Wood
    Side arrival.
  - **[S3]** [Gameranx juke-box puzzle guide](https://gameranx.com/features/id/511838/article/silent-hill-2-remake-jukebox-puzzle-guide/),
    for the exact component set, internal mechanism, insertion order and key
    result. Embedded media was not opened.
- Claim IDs: `SH2R-001`–`SH2R-008`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer James through streets, interiors and the final
  apartment entrance.
- Existing `ACT-087`: insert the repaired record, button, coin and acquired
  keys into compatible persistent fixtures.
- Existing `ACT-089`: collect each addressed route item into the persistent
  inventory.
- Existing `ACT-090`: replace compatible held constituents by the repaired
  record; the two record halves are combined first and the glue is the
  consumable joining parameter of that operation.
- Existing `ACT-131`: consume a carried healing item only after damage.
- Existing `ACT-161`: commit a reachable wooden-plank melee strike.
- Existing `ACT-341`: examine, push, climb through and operate addressed world
  fixtures, including the articulated juke-box mechanism and trolley.
- Existing `ACT-356`: commit a carefully timed directional dodge during live
  monster combat.
- Item names, route, dodge direction, exact strikes and control mapping are
  parameters. Claims: `SH2R-002`, `SH2R-004`–`SH2R-008`.

### System Behaviour Genes

- Existing `SYS-045`: nearby monsters patrol, emerge and pursue without a
  separate player command for each step.
- Existing `SYS-063`: applying each typed route key opens its compatible
  barrier and consumes or retires the key's route use.
- Existing `SYS-215`: movement, monster attacks, melee strikes and dodges
  resolve under a live combat clock.
- Existing `SYS-578`: damage and healing change one continuous health pool;
  depletion is failure.
- Existing `SYS-755`: the required Groovy Music window accepts impact and
  changes from blocking geometry to a traversable opening.
- Resolution order: validate the current action and required item; resolve
  live movement or impact; update health, inventory or fixture state; expose
  the next authored dependency; accept the final keyed threshold. Claims:
  `SH2R-004`–`SH2R-008`.

### Constraint Genes

- Existing `CON-210`: item pickup and combination require compatible inventory
  capacity.
- Existing `CON-282`: the records, glue, button, coin, juke-box result, bar
  continuation and apartment key form an authored predecessor chain.
- Existing `CON-296`: each locked route barrier requires its matching key.
- Existing `CON-442`: melee, dodge, pickup, combine, push, climb and fixture
  operation require compatible current range, pose, inventory and fixture
  state.
- Existing `CON-579`: a finite healing item is legal only below full health.
- Claims: `SH2R-005`–`SH2R-008`.

### Information Genes

- Existing `INF-075`: current health condition and damage feedback expose the
  immediate recovery decision.
- Existing `INF-115`: fog-limited local sight and spatial sound reveal only
  nearby monsters and actions.
- Existing `INF-125`: the acquired town map and current markings expose the
  discovered route and authored destinations without revealing interiors.
- Existing `INF-128`: prompts and inventory expose item identity, current
  possession and compatible combination or fixture use.
- New `INF-359`: while carried, the radio emits an anonymous static warning
  when a monster is nearby, without giving exact bearing, identity, distance
  band or route.
- Claims: `SH2R-003`–`SH2R-008`.

### Objective Genes

- Existing `OBJ-026`: make Wood Side Apartments traversably connected through
  the complete item-and-key chain, then navigate James across its designated
  entrance into ordinary lobby control.
- Claims: `SH2R-005`–`SH2R-007`.

### Time Genes

- Existing `TIM-003`: monsters, movement, strikes and dodges continue in real
  time while commands are accepted; map and inventory inspection interrupt
  that cadence where the interface permits.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A nearby monster is hidden by fog or occlusion | carry the acquired radio while moving | static begins without supplying an exact coordinate | a dedicated sensor differs from ordinary spatial sound | `SH2R-003` |
| A route monster threatens striking range | time a directional dodge or commit a plank strike | live movement and contact resolve; a mistimed choice can lower health | combat remains a local route decision, not a turn | `SH2R-002`, `SH2R-008` |
| Groovy Music is blocked by an eligible window | strike the pane | the barrier breaks and the interior becomes traversable | typed world destruction opens required access | `SH2R-005` |
| Both record pieces and glue are held | combine them | constituents are replaced by one repaired record | held identities become a route-compatible composite | `SH2R-005` |
| Juke-box components are ready | align the internal mechanism and insert record, button and coin | the declared selection becomes operable and yields Neely's Bar Key | articulated fixture state and typed inserts close one dependency | `SH2R-005` |
| Neely's Bar Key is held | unlock the bar continuation, push the trolley and climb through | the back-alley route becomes reachable | key use and contextual traversal remain distinct operations | `SH2R-006` |
| Wood Side Apartments Key is held at the entrance | apply the key and cross the threshold | the barrier opens and ordinary lobby control resumes | the bounded route settles at a retained designated location | `SH2R-007` |

## Edge-case audit

- Radio static is not `INF-172`: no authored distance bands or chase music are
  claimed. It is not `INF-203`: no direction, distance measurement or hidden
  collectible manifestation is supplied. It is not `INF-349`: it neither
  classifies allegiance nor plots relative bearing.
- Ordinary footsteps and visible silhouettes remain `INF-115`; the radio's
  system-generated anonymous warning is separately decision-relevant.
- `ACT-090` owns the inventory replacement, while `ACT-087` owns inserting the
  repaired result into a world fixture. The juke-box's internal manipulation
  stays `ACT-341`; no game-specific juke-box gene is created.
- Carefully timed dodge is admitted only as the official combat action. Exact
  protection frames, recovery and enemy tracking are not inferred.
- Health and healing are conditional route states, not mandatory damage. No
  specific hit or restorative spend is required for the positive terminal.
- The Wood Side lobby is the terminal location. Its rooms, map, save fixture
  and threats do not leak into this signature.

## Strategic and experiential structure

- Local decision: decide whether a radio warning warrants stopping, evading,
  striking or passing through fog before spending health.
- Medium-term planning: keep inventory capacity for every juke-box component,
  remember which street fixture accepts it and avoid confusing a useful key
  with optional written evidence.
- Long-term structure: turn dispersed partial objects into one repaired record,
  turn the restored fixture into a key and chain that key into the apartment
  threshold.
- Failure attribution: missed dodge, live hit, missing component, unconfigured
  fixture and wrong barrier remain distinguishable through local feedback and
  inventory state.
- Player trust: the same radio proximity state must provide the same class of
  warning, and a completed dependency must not silently lose its key result.

## Replay and variation

- Street geometry, component locations, fixture dependencies and the terminal
  are authored. No procedural layout or random item identity is claimed.
- Exact monster contact, route inspection, healing and optional pickups may
  vary while the reproducible dependency chain stays fixed.
- Replay within this packet compares combat avoidance and route efficiency,
  not endings, collectibles or whole-game completion.

## Adjacent systems and history

- *Resident Evil 2 (2019 remake)* shares traversal, melee/ranged threat
  handling, health, healing, inventory, keys, map information, ordered gates
  and a designated-location terminal. Its opening is a firearm-and-ammunition
  escape retained by a manual save; this packet is a fog-limited melee route
  whose radio warning and multipart juke-box chain lead to an apartment.
- *The Room* shares addressed item pickup, inventory combination, articulated
  fixture manipulation and applying a completed object. Its closed-box puzzle
  exposes a static inspection surface; this packet embeds those dependencies
  in live hostile streets with health and keyed traversal.
- *Alien: Isolation* shares obscured local threat reading and continuous
  survival pressure. Its motion tracker reports directional movement; the
  radio here deliberately provides only anonymous nearby static.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-089`, `ACT-090`, `ACT-131`, `ACT-161`, `ACT-341`, `ACT-356` | path, components, fixture, strike and dodge timing |
| System Behaviour | `SYS-045`, `SYS-063`, `SYS-215`, `SYS-578`, `SYS-755` | monster, barrier, health and breakable window |
| Constraint | `CON-210`, `CON-282`, `CON-296`, `CON-442`, `CON-579` | capacity, dependency, key and legality predicates |
| Information | `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-359` | health, map, inventory and radio warning |
| Objective | `OBJ-026` | Wood Side Apartments threshold |
| Time | `TIM-003` | live exploration and combat clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `329` (`GAME-0001`–`GAME-0329`).
- Exact genome matches: none.
- Tied near matches: `GAME-0280` — Resident Evil 2 (2019 remake) (`16 / 36 = 0.444444`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0280` — Resident Evil 2 (2019 remake) | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-578`, `CON-210`, `CON-282`, `CON-296`, `CON-579`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `OBJ-026`, `TIM-003` | Both carry a health-and-inventory route through live hostiles, ordered keys and a mapped designated-location terminal. Resident Evil 2 centres a magazine handgun, body-region shots and save retention; Silent Hill 2 adds held-item combination, articulated fixture restoration, a timed dodge, a breakable route window and nondirectional radio warning. | Near, `16 / 36 = 0.444444` |

### Preserved research notes

- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: established action, combat, inventory, gate, health,
  map and objective boundaries fit. Earlier proximity surfaces either encode
  distance bands, direction or classified contacts; none owns an anonymous
  nearby-threat signal that deliberately withholds those details.

## Taxonomy impact

- Registry changes: add one Active information boundary and Silent Hill 2
  support to twenty-four established boundaries.
- Taxonomy-change record: none; no existing boundary or lifecycle changes.
- Candidate terms affected: James, South Vale, Wood Side Apartments, record,
  glue, coin, button, juke box and named keys remain carrier parameters.

## Negative results

- No PS5, entitlement, installed patch, direct play, save, screenshot, video
  or audio evidence exists for this unit.
- No radio direction, distance band, identity class or exact detection radius
  is asserted.
- No dodge invulnerability duration, weapon damage, enemy health, checkpoint
  replacement or save persistence is inferred.
- Later apartments, firearms, bosses, endings and New Game Plus remain excluded
  rather than imported from whole-game guides.

## Delta summary

## New facts

- [Confirmed | Direct | High] Official publisher and platform pages establish
  the exact PS5 product, expanded exploration, over-the-shoulder view, fog,
  updated combat and carefully timed dodge (`SH2R-001`–`SH2R-003`).
- [Observation | Corroborated | High] Three written routes establish the
  complete juke-box-to-apartment dependency chain (`SH2R-004`–`SH2R-007`).

## New genes

- [Confirmed | Corroborated | High] `INF-359` isolates the radio's anonymous
  nearby-threat static from ordinary spatial sound and directional trackers.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] No earlier boundary, signature or lifecycle
  state changes; twenty-four existing genes are reused as written.

## New questions

- Does every current PS5 patch use identical radio onset and falloff thresholds
  for every early monster type?
- Which exact transient states survive every checkpoint return before the Wood
  Side threshold?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0331` *Starfield* is the next reserved
  audience-recognition unit.
- Optimisation criterion: replace a fixed urban horror dependency route with a
  bounded first spaceflight and artefact handoff.
- Backlog impact: completes 6/9 of the current fixed horizon.

## Why this game

- [Hypothesis | Limited | High] The remake is a recognisable horror anchor whose
  nondirectional radio warning and hostile inventory-fixture route differ from
  a generic survival-horror label.

## Completion checklist

- [x] exact PS5 product, settings, entry, terminal and exclusions declared
- [x] official identity and mechanics separated from written route evidence
- [x] radio warning separated from ordinary sound and directional trackers
- [x] exact/near scan and selected-neighbour interpretation recorded
- [x] Ukrainian, platform, presentation, artwork and validation tracked in the unit
