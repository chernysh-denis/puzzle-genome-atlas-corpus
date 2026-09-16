---
game_id: GAME-0289
slug: american-truck-simulator
game_title: American Truck Simulator
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids:
  - COMB-0167
gene_ids:
  action:
    - ACT-201
    - ACT-227
    - ACT-285
    - ACT-286
    - ACT-287
  system:
    - SYS-320
    - SYS-365
    - SYS-505
    - SYS-506
    - SYS-507
    - SYS-508
    - SYS-509
    - SYS-510
  constraint:
    - CON-288
    - CON-428
    - CON-429
    - CON-430
    - CON-431
    - CON-432
  information:
    - INF-144
    - INF-198
    - INF-199
    - INF-200
    - INF-201
  objective:
    - OBJ-096
  time:
    - TIM-003
---

# Game: American Truck Simulator

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official Steam Windows base game, app `270880`, at stable update `1.60`,
  one single-player introductory Quick Job on the original California/Nevada
  map, fatigue simulation and traffic offences enabled, automatic transmission,
  and no mods, DLC, Convoy or World of Trucks.
- Primary decision loop: create a fresh profile and accept the employer-supplied
  introductory Quick Job; read the cargo, destination, deadline, GPS, vehicle,
  damage and rest state; directly steer, accelerate, brake and signal through
  live traffic; optionally edit the route or take an eligible rest; enter the
  destination depot, choose a drop-off treatment, park and detach the trailer;
  then settle the delivery's income and experience.
- Entry and exit: begins at the fresh-profile city and company setup immediately
  before the first job; succeeds when the introductory cargo reaches its depot
  and the delivery-results screen settles the job. The resulting company state
  is described only as an official save/autosave outcome, not as a locally
  reload-verified observation.
- Included: one employer-provided tractor, trailer, cargo and operating-cost
  boundary; steering, throttle, braking, transmission, lights, indicators,
  wipers and cruise control as vehicle parameters; GPS route and one player
  waypoint; traffic, signals, speed limits and fines; truck, trailer and cargo
  damage; fuel state; Rest State, microsleep pressure, fourteen driving hours
  and ten consecutive hours of mandatory rest; destination-gate parking choice,
  reversing, detachment, income and experience settlement; official save and
  autosave only as persistence evidence.
- Reproducible parameterisation: use a new unmodded profile, select a base-map
  starting city and accept the first tutorial-selected Quick Job. Cargo, truck,
  route, traffic and weather are sampled parameters. If the short first route
  does not make rest tactically useful, the visible rest clocks and legal rest
  affordance remain rules of the live job, not a claim that rest was required.
- Excluded: all map, truck, trailer and cargo DLC; multiplayer, Convoy and World
  of Trucks; owned trucks or trailers; fuel or repair purchases; Freight,
  Cargo and External Markets; bank loans, garages, hired drivers, fleet growth,
  skills, achievements, exhaustive discovery and all later jobs.
- Potential scoped modules: one owned-truck Freight Market delivery, one
  company-management cycle, Convoy authority, or one DLC-state haul.
- Direct-play status: no local installation, save directory or Steam userdata
  for app `270880` was available, so no fresh play or reload was conducted. The
  official manual directly establishes profile creation, the introductory Quick
  Job, supplied vehicle, controls, fatigue option, completion and save/autosave;
  released SCS 1.58 and 1.60 notes establish the current tutorial, physics,
  route/job widgets and expanded-rest rules. Exact sampled values remain
  parameters. The selection hypothesis requiring local reload verification is
  therefore replaced by this evidence-bounded completion claim.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ATS-001` | Steam app `270880` is the SCS base product and stable `1.60` is the scoped released ruleset | Confirmed | Direct | High | P1, P2 |
| `ATS-002` | A fresh profile chooses a city and company, then begins with an introductory employer-supplied Quick Job | Confirmed | Direct | High | P3 |
| `ATS-003` | Quick Jobs provide an already-laden borrowed truck and remain the initial income source before truck ownership | Confirmed | Direct | High | P3 |
| `ATS-004` | The player directly operates the truck and trailer while current physics and traffic resolve movement and collision | Confirmed | Direct | High | P3, P4 |
| `ATS-005` | GPS and job widgets expose route, ETA, remaining time, cargo, income and vehicle/rest state | Confirmed | Direct | High | P2, P5 |
| `ATS-006` | Traffic law, speed and signals constrain the road through detected monetary fines | Observation | Corroborated | High | P3, P4 |
| `ATS-007` | Truck, trailer and cargo condition remain distinct delivery-relevant states | Confirmed | Direct | High | P4, P5 |
| `ATS-008` | ATS 1.60 separates Rest State from a fourteen-hour driving allowance reset by ten consecutive rest hours | Confirmed | Direct | High | P2, P6 |
| `ATS-009` | Destination handling offers parking treatments whose bay validation and difficulty affect experience | Confirmed | Direct | High | P7, P8 |
| `ATS-010` | Delivery settlement converts time, damage and parking into one job's money, experience and evaluation | Observation | Corroborated | High | P3, P7 |
| `ATS-011` | The profile is saved automatically or manually, but this unit did not locally test a reload | Confirmed | Direct | High | P3 |

## Basic data

- Release / origin: developed and published by SCS Software; released 2
  February 2016; scoped stable update `1.60` released 16 June 2026.
- Platform or physical form: Windows PC single-player road-haul simulation;
  Steam base-game introductory Quick Job is scoped.
- Puzzle family: physics and object manipulation; real-time system pressure.
- Primary sources:
  - `P1` — [official Steam product page](https://store.steampowered.com/app/270880/American_Truck_Simulator/),
    app identity, developer, publisher and release date, checked 2026-09-13.
  - `P2` — [official ATS 1.60 release](https://blog.scssoft.com/2026/06/american-truck-simulator-160-update-release.html),
    stable release, Job Details and expanded rest, checked 2026-09-13.
  - `P3` — [official Steam manual](https://cdn.cloudflare.steamstatic.com/steam/apps/270880/manuals/ATS_manual_digital.pdf?t=1613412188),
    profile, Quick Jobs, supplied truck, controls, fatigue, completion and
    save/autosave, checked 2026-09-13.
  - `P4` — [official ATS 1.58 release](https://blog.scssoft.com/2026/02/american-truck-simulator-158-update.html),
    redesigned first-job tutorial, vehicle physics, collisions and Route
    Advisor, checked 2026-09-13.
  - `P5` — [official Job Details widget](https://blog.scssoft.com/2026/05/160-update-job-details-widget.html),
    cargo, weight, destination, income and timing disclosures, checked
    2026-09-13.
  - `P6` — [official expanded-rest mechanic](https://blog.scssoft.com/2026/05/160-update-expanded-rest-mechanic.html),
    Rest State, Mandatory Break, fourteen driving hours and ten-hour reset,
    checked 2026-09-13.
  - `P7` — [official trailer drop-off design](https://blog.scssoft.com/2015/10/trailer-drop-off-redesign.html),
    destination gate, parking choices, skip and difficulty-linked experience,
    checked 2026-09-13.
  - `P8` — [official tractor-trailer challenge](https://blog.scssoft.com/2015/10/tractor-trailer-challenges.html),
    articulated turning and reverse-parking geometry, checked 2026-09-13.
- Secondary sources: none admitted.
- Claim IDs: `ATS-001`–`ATS-011`.

## Mechanical decomposition

### Action Genes

- `ACT-201` — directly operate the supplied tractor through steering, throttle,
  braking and compatible road equipment.
- `ACT-227` — place a waypoint that changes the calculated road route.
- `ACT-285` — accept the introductory Quick Job and its supplied cargo contract.
- `ACT-286` — choose a rest duration at an eligible stopping place.
- `ACT-287` — choose and commit one destination drop-off treatment.
- Parameters: city, offer, tractor, trailer, transmission, controls, waypoint,
  rest duration, parking treatment and camera.
- Claim IDs: `ATS-002`–`ATS-005`, `ATS-008`, `ATS-009`.

### System Behaviour Genes

- `SYS-320` — integrate direct truck control, traction, fuel and collision
  damage.
- `SYS-365` — route ambient traffic through roads and signals and resolve local
  collision response.
- `SYS-505` — instantiate the accepted Quick Job with the supplied loaded truck
  and declared delivery state.
- `SYS-506` — resolve tractor-trailer articulation, cargo mass and separate
  trailer/cargo damage.
- `SYS-507` — detect eligible road-law and break-limit violations and debit
  immediate fines.
- `SYS-508` — deplete Rest State and driving allowance, produce exhaustion
  effects and restore both through eligible rest.
- `SYS-509` — settle time/damage-adjusted income and parking-sensitive
  experience.
- `SYS-510` — calculate and recalculate route, ETA, remaining time and distance.
- Resolution order: profile setup exposes the first contract; acceptance creates
  the supplied vehicle-cargo state; direct input, articulation, traffic, law and
  rest clocks advance together; parking and detachment validate the destination;
  settlement closes the job and save/autosave can retain the resulting profile.
- Claim IDs: `ATS-002`–`ATS-011`.

### Constraint Genes

- `CON-288` — direct operation needs a viable driver position, operating truck
  and traversable geometry.
- `CON-428` — only one offered employer-supplied contract can be the active
  Quick Job.
- `CON-429` — road class, direction, signal and posted limit define legal
  vehicle movement even when violation is physically possible.
- `CON-430` — fourteen driving hours require ten consecutive rest hours before
  legal continuation.
- `CON-431` — delivery evaluation is bounded by deadline and retained truck,
  trailer and cargo condition.
- `CON-432` — a non-skipped drop-off validates only when the assigned trailer
  occupies the selected bay and can be detached.
- Claim IDs: `ATS-003`, `ATS-006`–`ATS-010`.

### Information Genes

- `INF-144` — map and GPS disclose destination and calculated road route.
- `INF-198` — the offer discloses cargo, endpoints, distance, income, deadline
  and supplied truck before acceptance.
- `INF-199` — driving widgets disclose speed, gear, fuel, rest, mandatory break
  and separate truck/trailer/cargo damage.
- `INF-200` — job and GPS widgets disclose cargo type/weight, destination,
  income, remaining time, ETA and route distance.
- `INF-201` — results disclose settled income, penalties, parking experience
  and evaluation.
- Claim IDs: `ATS-003`, `ATS-005`–`ATS-010`.

### Objective Genes

- `OBJ-096` — complete and settle one employer-supplied cargo delivery.
- Success, evaluation and failure: a validated delivery followed by settlement
  succeeds; late or damaged arrival reduces the result; abandonment or failure
  to deliver ends this scoped job, not the profile.
- Claim IDs: `ATS-003`, `ATS-009`, `ATS-010`.

### Time Genes

- `TIM-003` — driving, traffic, physics, fatigue, deadline and local world state
  advance while live input remains available; rest deliberately advances the
  same world/job clock.
- Claim IDs: `ATS-004`–`ATS-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh profile has a chosen starting city | Accept the tutorial-selected Quick Job | The game supplies its loaded tractor-trailer and fixes cargo, destination, income and deadline | Employer-supplied first-job boundary | `ATS-002`, `ATS-003` |
| Destination route is active | Add or move one legal waypoint | GPS recalculates route, ETA, remaining time and distance | Route choice changes risk without automating control | `ATS-005` |
| Articulated vehicle is on a live road | Steer, accelerate, brake and signal | Vehicle motion, traffic contact, fuel and separate damage states advance | Direct physical haul | `ATS-004`, `ATS-006`, `ATS-007` |
| Truck crosses a monitored signal or limit | Continue the violating movement | An offence produces a fine without ending the delivery | Law is an economic constraint | `ATS-006` |
| Driving allowance nears zero at an eligible stop | Select at least ten consecutive rest hours | World and deadline advance; Rest State and legal allowance reset | Rest competes with deadline | `ATS-008` |
| Depot offers drop-off treatments | Choose a bay, reverse and detach | Trailer pose is validated; difficulty determines parking experience | Parking participates in evaluation | `ATS-009`, `ATS-010` |
| Trailer is validly delivered | Confirm completion | Results apply time/damage adjustments and award income and experience | Explicit one-job terminal | `ATS-010` |

## Strategic and experiential structure

- Local decision: preserve lane position, stopping distance and trailer sweep
  while reading traffic, signals, speed, fuel, damage and rest state.
- Medium-term planning: compare route, waypoint, eligible rest, remaining legal
  driving allowance and deadline before detouring or resting.
- Long-term structure: the unit ends after one delivery; retained money and
  experience are acknowledged, while spending and company growth are excluded.
- Common heuristics: brake before a turn, leave trailer clearance, schedule rest
  before the limit, recheck ETA after a waypoint and approach the depot for a
  controllable reverse.
- Failure attribution: GPS, violation notices, rest clocks, damage widgets and
  results distinguish route, handling, compliance, fatigue and parking errors.
- Claim IDs: `ATS-004`–`ATS-010`.

## Replay and variation

- What changes between profiles: starting city, introductory offer, tractor,
  cargo, traffic, weather, route edits, damage and final evaluation.
- Randomness or procedural generation: offers and ambient-road state are
  sampled; their exact seeds are not player decisions in this scope.
- Multiple viable strategies: direct route, lower-risk roads and a waypoint
  through an eligible rest stop can all be valid when deadline slack permits.
- Typical replay motive: cleaner driving and harder parking; career growth is
  outside this one-job unit.
- Claim IDs: `ATS-003`, `ATS-005`–`ATS-010`.

## Adjacent systems and history

- Direct predecessors: road-driving and contract-delivery simulations; this is
  a mechanical adjacency statement, not a title-lineage claim.
- Variants: owned-truck Freight Market shifts fuel and repair responsibility to
  the player; company play adds loans, garages, drivers and fleet accumulation.
- Similar games: Euro Truck Simulator 2 uses the same SCS contract-haul grammar;
  Grand Theft Auto V shares direct road physics, traffic and GPS without the
  supplied cargo, fatigue, parking and job-settlement boundary.
- Important differences: ATS applies American road geography and a fourteen/
  ten-hour rest parameter, but those values do not create new gene boundaries.
- Claim IDs: `ATS-001`–`ATS-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-201`, `ACT-227`, `ACT-285`–`ACT-287` | exact bindings and control layout are parameters |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-505`–`SYS-510` | offer, traffic and weather samples are parameters |
| Constraint | `CON-288`, `CON-428`–`CON-432` | hour values, deadline and bay geometry are parameters |
| Information | `INF-144`, `INF-198`–`INF-201` | widget placement and units are parameters |
| Objective | `OBJ-096` | cargo and endpoint identity are parameters |
| Time | `TIM-003` | rest duration advances the live job clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `288` (`GAME-0001`–`GAME-0288`).
- Exact genome matches: `GAME-0169` — Euro Truck Simulator 2.
- Tied near matches: `GAME-0214` — Mafia (2002) (`6 / 42 = 0.142857`).
- Supported combination subsets: `COMB-0167`.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0169` — Euro Truck Simulator 2 | all twenty-six genes: supplied Quick Job, direct articulated driving, GPS waypoint, live traffic and law, damage, dual rest pressure, drop-off and settlement | American road geography, first-job presentation and fourteen/ten-hour rest values are parameters inside the same transferable boundaries | Exact, `26 / 26 = 1.000000` |
| `GAME-0214` — Mafia (2002) | direct vehicle operation, vehicle physics/damage, ambient traffic, viable driving geometry, regulated roads and live time | ATS adds a player-edited GPS route, supplied articulated cargo contract, fatigue clocks, damage displays, trailer-bay validation and commercial settlement; Mafia binds five taxi fares to police escalation and an on-foot escape | Near, `6 / 42 = 0.142857` |

### Preserved research notes

- New genes: none.
- Classification result: exact recurrence of `GAME-0169` and `COMB-0167`.
- Evidence and reasoning: SCS applies the same one-job decision structure in
  both products. The American fourteen/ten-hour break values replace European
  ten/nine-hour parameters without changing command, state, constraint,
  information, objective or time boundaries.

## Taxonomy impact

- Registry changes: none; twenty-six Active genes are reused.
- Combination change: `COMB-0167` gains a second analysed game and becomes a
  cross-product recurrence.
- Taxonomy-change record: none; no definition is deprecated, merged or split.
- Candidate terms affected: none.

## Negative results

- Fresh-profile creation and company naming are setup parameters, not persistent
  company-management decisions inside the one-job scope.
- Save/autosave supports retained state, but reload is not claimed because no
  local install or profile was available for a direct reload test.
- American rest-hour values and road presentation do not justify new genes;
  they parameterise the existing mandatory-break and regulated-road boundaries.
- DLC and later offers do not silently expand the introductory job.

## Delta summary

## New facts

- [Confirmed | Direct | High] Stable ATS 1.60 combines the first supplied
  Quick Job, direct articulated driving, GPS, road law, damage, two rest
  pressures, parking and delivery settlement (`ATS-001`–`ATS-011`).

## New genes

- [Confirmed | Direct | High] No new genes are required: all twenty-six
  boundaries exactly recur from Euro Truck Simulator 2's normalised genome.

## New combinations

- [Confirmed | Direct | High] No new combination is required; `COMB-0167`
  gains a second carrier and becomes a confirmed cross-game recurrence.

## Taxonomy changes

- [Confirmed | Direct | High] No taxonomy change is required.

## Family classification

- `FAM-007` — Physics and object manipulation: articulated vehicle geometry,
  collision and reverse parking determine legal physical placement.
- `FAM-010` — Real-time system pressure: traffic, deadline, damage, fuel and
  rest clocks advance while the player drives or rests.
- No new family is created from one game.

## Plain-language interpretation

The introductory Quick Job starts with a borrowed loaded truck and one declared
destination. The road is not an abstract connection: the player must steer a
long articulated body through traffic and legal limits while GPS, deadline,
fuel, damage and fatigue remain visible. A waypoint or rest can make the haul
safer but consumes time.

At the depot, arriving is not the whole result. The player chooses a parking
treatment, aligns the trailer in its bay and detaches it, or accepts an easier
option. Settlement then turns delivery time, damage and parking into money,
experience and evaluation. This is the same transferable ruleset as ETS2; the
American map and fourteen/ten-hour rest rule are parameters.

## New questions

- Which delivery game keeps route/deadline settlement but replaces direct
  steering with autonomous scheduling?

## Next recommended game

- [Confirmed | Direct | High] `GAME-0290` — Lies of P.
- Optimisation criterion: continue the immutable selection-018 contrast order
  after an exact road-haul recurrence.
- Expected gene pressure: guard timing, weapon assembly and durability, Fable
  Arts, Legion resources, death-retrieval and boss-gated progression.
- Anti-bias note: do not import ATS vehicle, route, contract or rest boundaries
  into an action-RPG opening.

## Next research step

- Integrate `GAME-0290` — Lies of P after the required thirty-second stop window.

## Design lessons

- Regional rule values can vary without changing a reusable decision boundary.
- A first delivery can expose a complete contract loop before ownership and
  company-management systems become active.

## Open questions

- Does owned-truck fuel, repair and capital responsibility warrant a separate
  future genome even when driving and delivery settlement remain unchanged?
