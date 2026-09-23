---
game_id: GAME-0374
slug: burnout-paradise
game_title: Burnout Paradise
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-293
    - ACT-309
  system:
    - SYS-320
    - SYS-519
    - SYS-691
    - SYS-765
    - SYS-1020
  constraint: []
  information:
    - INF-206
    - INF-381
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Burnout Paradise

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Car model, chosen
junction, start, finish, rival count and boost amount are parameters, not
additional genes.

## Analysis scope

- Version / ruleset: original 2008 English Xbox 360 Burnout Paradise offline
  car-event rules, as documented by the contemporary Electronic Arts manual.
  No disc, installed version or patch was inspected. Later PC Ultimate Box and
  Remastered rules are not silently imported.
- Structured analysis target: original Xbox 360 base-game offline ordinary
  `Race` event; `GAME-0374` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: locate a discovered Race junction; commit the event
  from a stationary car; read the map, destination compass, remaining distance
  and suggested turns; steer, accelerate, brake and use the available car's
  bounded Boost while choosing a path through the open city; negotiate road
  contact and other moving vehicles; cross the named red finish banner before
  the competing drivers, then retain the event-win contribution to the licence.
- Entry and exit: use an offline original-game save with a drivable car and a
  discovered junction labelled `Race`. Record the car's boost class, junction,
  destination and prior win state. Stop at that junction, start the event by
  holding brake and accelerator, and accept first race driving control. The
  positive terminal is a first-place crossing under its red finish banner,
  followed by the settled event win and one licence point if this was the
  event's first win in the current licence tier. A mere finish after rivals,
  stopping, entering Showtime or quitting early is not positive completion.
  The manual does not specify an exact ordinary Race crash-retry transition;
  none is invented.
- Included: one offline car Race only; mapped junction discovery and event
  launch; direct vehicle control, road contact and collision; point-to-point
  city routing without fixed intermediate checkpoints; live destination cues;
  autonomous competitors and finish ordering; one Stunt- or Aggression-boost
  car's eligible manoeuvre charging and spend; result settlement and the
  first-win licence contribution. This packet fixes a Stunt-class Boost car;
  Aggression- and Speed-class charging rules are outside its boundary.
- Excluded: Road Rage, Marked Man, Stunt Run, Burning Route, Road Rules,
  Showtime and its crash score, online races, bikes, Big Surf Island, DLC,
  career-wide licence upgrades, car unlocks, billboards, collectible Smashes,
  Super Jumps as a separate target, power parking, garage selection and
  repairs as an optimisation loop. A permissible shortcut is route geometry,
  not a second event goal.
- Potential scoped modules: a Speed-boost Race, Road Rage takedown target,
  Marked Man damage-survival route, Stunt Run score chain, Burning Route timed
  car gate or licence-tier campaign each needs its own entry, rules and
  terminal evidence.
- Direct-play status: none. The original EA manual is the source for the
  bounded rules; no Xbox 360 disc, save, executable hash, controller trace,
  screenshot, video or audio was inspected. No precise handling coefficient,
  crash reset or rival path algorithm is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BOP-001` | The original Xbox 360 manual exposes a city map, junction event markers, a dedicated event-start input and direct driving controls. | Confirmed | Direct | High | EA Xbox 360 manual pp. 1–2, 4, 6 |
| `BOP-002` | A standard Race is point-to-point with no fixed route; the compass and distance guide a choice of streets, and a red overhead banner marks the finish. | Confirmed | Direct | High | EA Xbox 360 manual p. 4 |
| `BOP-003` | Event wins advance a licence; a given event contributes only once before the licence tier resets its win status. | Confirmed | Direct | High | EA Xbox 360 manual p. 4 |
| `BOP-004` | A Stunt-class car may spend and replenish Boost while driving; eligible manoeuvres charge its reserve. | Confirmed | Direct | High | EA Xbox 360 manual p. 5 |
| `BOP-005` | Road contact and crashes matter to car travel, but the contemporary manual does not fix the precise failure or restart rule for an ordinary Race. | Observation | Limited | Medium | EA Xbox 360 manual pp. 3–5; bounded absence review |
| `BOP-006` | The offline Race packet excludes the separate Road Rage, Marked Man, Stunt Run, Burning Route, Showtime and Road Rule predicates. | Confirmed | Direct | High | EA Xbox 360 manual pp. 3–5 |

## Basic data

- Release / origin: Criterion Games / Electronic Arts, original Burnout
  Paradise, 2008.
- Platform or physical form: English Xbox 360 base game, offline car Race;
  the listed platform is an analysis target, not an audit of every release.
- Puzzle family: `FAM-010` real-time system pressure, because route choices,
  Boost and car contact resolve while other race traffic continues moving;
  `FAM-007` physics and object manipulation, because the driven car's momentum
  and collision-bound turn or shortcut shape its reachable route. The city
  graph is selected through, not edited, so `FAM-014` does not fit.
- Primary sources: [EA's original Xbox 360 instruction manual, preserved as
  PDF](https://www.gamesdatabase.org/Media/SYSTEM/Microsoft_Xbox_360/Manual/formated/Burnout_Paradise_-_2008_-_Electronic_Arts.pdf),
  pp. 1–6; [text-accessible rendering of that same EA
  booklet](https://manualzz.com/doc/25609167/games-microsoft-xbox-burnout-paradise-owner-s-manual).
- Secondary sources: none used to admit mechanic claims. EA's later
  [Remastered Xbox One manual](https://eaassets-a.akamaihd.net/eahelp/manuals/bpr-manuals_xboxone_en.pdf)
  confirms shared terminology but does not define this original edition.
- Claim IDs: `BOP-001`–`BOP-006`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-290` direct car steering, throttle, brake and
  handbrake; `ACT-293` commit one mapped driving event; `ACT-309` spend the
  current bounded Boost reserve.
- Candidate genes: none.
- Parameters: car, junction, chosen street, handbrake, Boost class and
  activation interval.
- Claim IDs: `BOP-001`, `BOP-002`, `BOP-004`.

### System Behaviour Genes

- Existing gene IDs: `SYS-320` continuous vehicle motion and collision;
  `SYS-519` persistent event-win settlement; `SYS-691` spend Boost as
  acceleration; `SYS-765` credit eligible Stunt driving to the bounded Boost
  reserve.
- Candidate gene: `SYS-1020` for an uncheckpointed city race with autonomous
  rivals, one named finish banner and classified arrival order. `SYS-515`
  presumes a shared fixed course and `SYS-516` validates ordered checkpoints
  or laps, so neither is silently reused for the original ordinary Race.
- Resolution order: a mapped junction commits the event; the city remains
  traversable by alternative streets; live steering, acceleration and contact
  change car state; eligible manoeuvres replenish Boost and activation spends
  it; the first valid finish crossing is classified against rivals; a win
  settles into the current licence tier.
- Parameters: car class, road graph, rivals, contact, Boost cap, manoeuvre,
  destination, route choice, finish place and prior win flag.
- Claim IDs: `BOP-001`–`BOP-005`.

### Constraint Genes

- Existing gene IDs: none. The selected event permits multiple streets rather
  than imposing a fixed checkpoint or vehicle-class eligibility gate.
- Candidate genes: none.
- Scarce strategic resources: Boost charge and time against moving rivals;
  quantities are parameters of action and system rules, not new constraints.
- Claim IDs: `BOP-002`, `BOP-004`.

### Information Genes

- Existing gene ID: `INF-206` for the discovered map's event type, location
  and start/finish disclosure.
- Candidate gene: `INF-381` for the live compass destination vector, current
  heading, remaining distance and suggested junction turn. `INF-204` joins
  speed and gear to route guidance, which the original Xbox 360 booklet does
  not establish as this packet's displayed information.
- Claim IDs: `BOP-001`, `BOP-002`.

### Objective Genes

- Existing gene ID: `OBJ-134` for winning one rival race and retaining its
  first-win licence contribution.
- Candidate genes: none.
- Success, evaluation and failure: first place at the named banner is the
  positive race result; an already-won event may be replayed but gives no
  second licence point until the licence tier resets event status. Ordinary
  Race crash/retry behaviour is not specified by the booklet.
- Claim IDs: `BOP-002`, `BOP-003`, `BOP-005`.

### Time Genes

- Existing gene ID: `TIM-003` for steering and Boost input while rivals and
  vehicle motion continue in real time.
- Candidate genes: none.
- Claim IDs: `BOP-001`, `BOP-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A discovered junction displays `Race` and the car is stopped there | Hold brake and accelerator | The bounded point-to-point event starts | A map marker alone is not an active race | `BOP-001` |
| The finish lies northeast, and two city streets depart the next junction | Turn onto either legal street | Both remain route candidates; the bearing and remaining distance update | The race has no required intermediate checkpoint order | `BOP-002` |
| The Stunt-class car performs a qualifying manoeuvre | Keep driving | The live action credits bounded Boost | Driving risk and reserve acquisition are distinct from spending | `BOP-004` |
| Boost charge is available while a straight is clear | Activate Boost | Charge is spent and acceleration changes the car's trajectory | Reserve spend creates a local speed-versus-contact decision | `BOP-004` |
| The player reaches the named red banner before competitors | Drive beneath it | The first-place result is classified and the win settles | Mere proximity to the destination is not the terminal | `BOP-002`, `BOP-003` |
| The same junction event has already been won in this licence tier | Win it again | The event remains replayable but grants no second tier point | The first-win flag matters to retained progression | `BOP-003` |
| Showtime becomes available during the race | Enter it | The current event is quit, not won | A crash-scoring mode cannot satisfy this Race packet | `BOP-006` |

The table records rule categories, not measured lap times, Boost coefficients,
specific rival routes, traffic spawns or crash-restart frames. A direct-play
replication would record car and boost class, junction, destination, prior win
state, chosen streets, Boost actions, collisions, finish order and licence
change.

## Strategic and experiential structure

- Local decision: choose street and cornering/braking line while deciding when
  to spend Boost without losing control.
- Medium-term planning: read the destination vector and map, trade a possibly
  shorter shortcut against its turn and collision exposure.
- Long-term structure: a first event win adds one licence point; repeated wins
  in that tier do not farm points.
- Common heuristics: compare the next-turn recommendation with the broader
  road graph and use Boost on a controllable segment. These are possible
  plans, not claims of optimal driving.
- Failure attribution: the map, compass, remaining distance, road contact and
  visible finish distinguish wrong-route and contact errors; exact rival AI
  and ordinary Race crash resets remain uninspected.
- Player-trust factors: the game marks event type at its junction, displays
  destination cues and uses an overhead finish banner.
- Claim IDs: `BOP-001`–`BOP-006`.

## Replay and variation

- What changes between sessions: selected Race junction, start/finish pair,
  car/boost class, route choice and prior win state.
- Randomness or procedural generation: the packet does not assert a traffic
  or rival-route seed; the source establishes an authored city and event
  locations, not a quantified distribution.
- Multiple viable strategies: several street routes can approach the same
  banner; their relative optimality depends on live control and contact.
- Typical replay motive: improve route and driving result or gain the licence
  point after a tier reset.
- Claim IDs: `BOP-002`–`BOP-004`.

## Adjacent systems and history

- Direct predecessors: no series-lineage claim is needed for this packet.
- Variants: the manual documents distinct Road Rage, Marked Man, Stunt Run,
  Burning Route and Showtime loops excluded here.
- Similar games: complete-corpus signature comparison is owned below.
- Important differences: unlike Trackmania and circuit racers, an ordinary
  Burnout Paradise Race does not validate an ordered waypoint or lap sequence.
- Claim IDs: `BOP-002`, `BOP-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-293`, `ACT-309` | Car, event and Boost class |
| System Behaviour | `SYS-320`, `SYS-519`, `SYS-691`, `SYS-765`, `SYS-1020` | Road graph, contact, reserve and rivals |
| Constraint | None | No fixed checkpoint order |
| Information | `INF-206`, `INF-381` | Junction, compass, distance and map |
| Objective | `OBJ-134` | First win and licence point |
| Time | `TIM-003` | Live steering and competitors |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `373` (`GAME-0001`–`GAME-0373`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`7 / 19 = 0.368421`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` Need for Speed Underground | `ACT-290`, `ACT-293`, `SYS-320`, `SYS-519`, `INF-206`, `OBJ-134`, `TIM-003` | Both commit a mapped car race, drive in real time and retain a first-place result. Underground's circuit requires a fixed course, ordered laps and its own HUD; Paradise permits alternative city streets, uses destination cues and a Stunt-Boost loop. | Tied near, score 0.368421 |

### Preserved research notes

- New genes: `SYS-1020`, `INF-381`.
- Classification result: New gene.
- Evidence and reasoning: the original EA manual's no-fixed-route and
  destination-compass rules do not fit ordered-course validation or speed/
  gear-only HUD boundaries. This is not a new game-family claim.

## Taxonomy impact

- Registry changes: add `SYS-1020` and `INF-381`; no existing signature
  changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_113`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_113.md).
- Candidate terms affected: open-city point-to-point race and destination
  compass are accepted as operational boundaries, not genres.

## Negative results

- No verified combination subset is claimed before the complete scan; other
  event families do not transfer to this Race packet.

## Delta summary

The headings below list only new corpus changes. Reviewed Ukrainian research
views are generated from the separate locale layer.

## New facts

- [Confirmed | Direct | High] One ordinary offline Race can use alternative
  city streets to its named banner; its first win contributes once to the
  licence tier (`BOP-002`, `BOP-003`).

## New genes

- [Observation | Direct | High] `SYS-1020` and `INF-381` separate open-city
  finish settlement and live destination guidance from checkpointed races.

## New combinations

- [Observation | Direct | High] No combination is added for this game.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_113` adds two bounded
  definitions without changing earlier signatures.

## New questions

- A direct Xbox 360 trace could fix ordinary Race crash/recovery and rival
  path details; neither is inferred from manual silence.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0375` Viva Piñata, the next selected
  genre-contrast unit.
- Optimisation criterion: alternate vehicle routing with garden residency.
- Expected information gain: test species attraction and retained garden
  conditions against existing ecology genes.
- Backlog impact: no predecessor signature is revised.

## Why this game

- [Hypothesis | Limited | Medium] Burnout Paradise tests whether open-road
  route freedom is distinguishable from a fixed checkpoint course without
  conflating racing, crashes and stunt-scoring modes.
