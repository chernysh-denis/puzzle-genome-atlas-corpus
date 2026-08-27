---
game_id: GAME-0169
slug: euro-truck-simulator-2
game_title: Euro Truck Simulator 2
analysis_status: reviewed
reviewed: 2026-08-27
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

# Game: Euro Truck Simulator 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official Steam PC base game at stable update `1.60`, one
  single-player Quick Job with fatigue simulation and mandatory breaks enabled,
  standard traffic offences, automatic transmission and no mods or DLC.
- Primary decision loop: compare the currently offered base-map jobs; accept
  one employer-supplied truck, trailer and cargo; inspect the GPS route, ETA,
  deadline, rest and damage state; directly steer, accelerate, brake and signal
  through live traffic; revise the route or take an eligible rest; reach the
  destination; choose a drop-off treatment, park and detach the trailer; then
  settle income and experience from delivery time, damage and parking.
- Entry and exit: begins in the Quick Jobs market before accepting one offer
  whose origin and destination are both on the original-game map; succeeds
  when that cargo reaches its named depot and the delivery-results screen has
  settled the one job.
- Included: the sampled offer's cargo, weight, income, origin, destination,
  deadline, truck and trailer; employer-supplied equipment and operating costs;
  direct articulated-vehicle control; throttle, braking, steering, transmission,
  lights, indicators, wipers and cruise control as vehicle parameters; GPS route
  and player waypoint; live traffic, signals, speed limits and traffic fines;
  truck, trailer and cargo damage; fuel state; Rest State, microsleep pressure,
  ten-hour driving limit and nine-hour mandatory rest; one destination
  drop-off choice, reverse parking, detachment, pay and experience settlement.
- Reproducible parameterisation: use a no-owned-truck profile with the required
  Long Distance access, choose the first displayed non-urgent single-trailer
  diesel Quick Job in ascending route-distance order whose endpoints both carry
  the official site's `ORIGINAL GAME` label and whose current Rest State makes
  one legal rest decision relevant before its deadline. Offer identity, road
  traffic and weather are sampled parameters, not additional genes.
- Excluded: map, truck, trailer and cargo DLC; World of Trucks, Convoy and mods;
  electric Quick Jobs; owned trucks and trailers; buying fuel or repairs;
  Freight/Cargo/External Markets; loans, garages, hired drivers, fleet and
  company-scale accumulation; multiple jobs, skill allocation, achievements,
  exhaustive map discovery, Driving Academy and post-delivery career growth.
- Potential scoped modules: one owned-truck Freight Market loop; one company
  management packet; Convoy authority and shared traffic; or a DLC-map haul.
- Direct-play status: no fresh paid-account delivery was conducted. SCS's
  stable 1.60 release, current product site, official Steam manual and released
  feature notes directly establish the job, vehicle, route, HUD, rest and
  parking transitions. Exact offer, traffic, weather and reward values remain
  parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ETS-001` | Stable Steam update `1.60` is the scoped current PC ruleset | Confirmed | Direct | High | P1 |
| `ETS-002` | Quick Jobs supply a borrowed, already laden truck and cover operating responsibility for the single job | Confirmed | Direct | High | P2, P3 |
| `ETS-003` | A job offer commits cargo, origin, destination, income, truck and delivery time while later skills can widen available offers | Confirmed | Corroborated | High | P2, P3, P4 |
| `ETS-004` | The player directly controls throttle, brake, steering, transmission and road equipment while the current physics resolves response and collision | Confirmed | Direct | High | P2, P5 |
| `ETS-005` | The map permits route customisation through waypoints and the GPS recalculates the road route, ETA, remaining time and distance | Confirmed | Direct | High | P1, P6 |
| `ETS-006` | Live traffic, signals, local rules and collision occupy the road while speeding, red-light and excess-driving violations can produce fines | Observation | Corroborated | High | P4, P7, P8 |
| `ETS-007` | Truck, trailer and cargo damage are separate visible job-relevant states | Confirmed | Direct | High | P7 |
| `ETS-008` | Update 1.60 splits fatigue into depleting Rest State and a ten-hour Mandatory Break limit cleared by nine consecutive rest hours | Confirmed | Direct | High | P1, P9 |
| `ETS-009` | Destination handling permits a parking treatment, articulated manoeuvre and trailer detachment before delivery settlement | Observation | Corroborated | High | P2, P10, P11 |
| `ETS-010` | Job details expose cargo type/weight, destination, income and remaining time; GPS and widgets expose ETA, vehicle and rest state | Confirmed | Direct | High | P1, P7, P8 |
| `ETS-011` | Delivery settlement distinguishes time, damage and parking performance and awards one-job income and experience | Observation | Corroborated | Medium | P3, P4, P10 |

## Basic data

- Release / origin: developed and published by SCS Software; original release
  2012; scoped stable update `1.60` released 18 June 2026.
- Platform or physical form: PC single-player road-haul simulation; Steam base
  game Quick Job is scoped.
- Puzzle family: physics and object manipulation; real-time system pressure.
- Primary sources:
  - `P1` — [official Euro Truck Simulator 2 update 1.60 release](https://blog.scssoft.com/2026/06/euro-truck-simulator-2-160-update.html?m=1),
    stable release, Job Details Widget, GPS ETA and expanded rest rules, checked
    2026-08-27.
  - `P2` — [official Steam manual](https://cdn.cloudflare.steamstatic.com/steam/apps/227300/manuals/ETS2_manual_en.pdf?t=1612571132),
    Quick Jobs, controls, trailer detachment and fatigue option, checked
    2026-08-27.
  - `P3` — [official ETS2 freight design](https://blog.scssoft.com/2012/02/ets2-freight.html),
    one-time employee/Quick Job boundary, wage and experience, checked 2026-08-27.
  - `P4` — [official Euro Truck Simulator 2 site](https://eurotrucksimulator2.com/about.php),
    live traffic, base-map labels, deliveries, skills and distinct company
    management, checked 2026-08-27.
  - `P5` — [official update 1.58 vehicle physics release](https://blog.scssoft.com/2026/02/euro-truck-simulator-2-158-update.html),
    current throttle, coasting, handling and collision model inherited by 1.60,
    checked 2026-08-27.
  - `P6` — [official GPS route-customisation release](https://blog.scssoft.com/2015/09/ets2-update-120-is-live-now.html),
    persistent map waypoints and route editing, checked 2026-08-27.
  - `P7` — [official update 1.59 release](https://blog.scssoft.com/2026/05/euro-truck-simulator-2-159-update.html?m=0),
    truck, trailer and cargo damage widgets, finances and recovery, checked
    2026-08-27.
  - `P8` — [official Route Advisor design](https://blog.scssoft.com/2026/02/the-new-route-advisor-why-and-how-its.html?m=0),
    speed, gear, fuel, delivery time, rest, damage and local regulations,
    checked 2026-08-27.
  - `P9` — [official expanded rest mechanic](https://blog.scssoft.com/2026/05/160-update-expanded-rest-mechanic.html),
    Rest State, microsleep, ten-hour limit, nine-hour rest and violation,
    checked 2026-08-27.
  - `P10` — [official trailer drop-off design](https://blog.scssoft.com/2015/10/trailer-drop-off-redesign.html),
    parking choices, skip and difficulty-linked experience, checked 2026-08-27.
  - `P11` — [official Driving Academy release](https://blog.scssoft.com/2024/10/driving-academy-release.html),
    articulated reversing and complex parking as truck-control mechanics,
    checked 2026-08-27.
- Secondary sources: none admitted.
- Claim IDs: `ETS-001`–`ETS-011`.

## Mechanical decomposition

### Action Genes

- `ACT-201` — directly operate the supplied truck through steering, throttle,
  braking and compatible road equipment.
- `ACT-227` — place a waypoint that changes the calculated road route without
  automating vehicle control.
- `ACT-285` — accept one Quick Job offer and its supplied truck-cargo contract.
- `ACT-286` — choose a rest duration at an eligible stopping place.
- `ACT-287` — choose and commit one offered destination drop-off treatment.
- Parameters: offer ordering, truck and trailer identity, transmission, control
  device, waypoint, rest duration, parking difficulty and camera.
- Claim IDs: `ETS-002`–`ETS-005`, `ETS-008`, `ETS-009`.

### System Behaviour Genes

- `SYS-320` — integrate direct truck steering, acceleration, traction, fuel and
  collision damage.
- `SYS-365` — route ambient traffic through roads and signals and resolve its
  local collision response.
- `SYS-505` — instantiate the accepted Quick Job with an employer-supplied
  loaded truck and declared delivery state.
- `SYS-506` — resolve tractor-trailer articulation, cargo mass and separate
  trailer/cargo damage during movement and parking.
- `SYS-507` — detect eligible road-law and mandatory-break violations and debit
  their immediate fines.
- `SYS-508` — deplete Rest State and Mandatory Break allowance, produce
  exhaustion effects and restore both through eligible rest.
- `SYS-509` — settle the delivered job into time/damage-adjusted income and
  parking-sensitive experience.
- `SYS-510` — calculate and recalculate the road route, ETA, time and distance
  through the active destination and player waypoints.
- Resolution order: accepting an offer creates the supplied vehicle-cargo
  state; GPS calculates its route; direct input, articulated physics, traffic,
  law and rest clocks advance together; eligible rest advances world time;
  destination parking and detachment validate delivery; settlement commits the
  one-job result.
- Claim IDs: `ETS-002`–`ETS-011`.

### Constraint Genes

- `CON-288` — direct operation requires an available viable driver position,
  operating truck and traversable geometry.
- `CON-428` — only one currently offered employer-supplied contract may become
  the active Quick Job.
- `CON-429` — road class, direction, signal and posted limit define legal
  vehicle movement even when the truck could physically violate them.
- `CON-430` — ten driving hours require nine consecutive rest hours before
  legal continuation.
- `CON-431` — delivery evaluation is bounded by the job deadline and retained
  truck, trailer and cargo condition.
- `CON-432` — a non-skipped drop-off validates only when the assigned trailer
  occupies the selected bay and may be detached.
- Claim IDs: `ETS-002`, `ETS-003`, `ETS-006`–`ETS-011`.

### Information Genes

- `INF-144` — map and GPS disclose the current destination and calculated road
  route.
- `INF-198` — Quick Jobs disclose offer cargo, endpoints, distance, income,
  deadline and supplied truck before acceptance.
- `INF-199` — driving widgets disclose speed, gear, fuel, rest, mandatory-break
  and truck/trailer/cargo damage state.
- `INF-200` — job and GPS widgets disclose cargo type/weight, destination,
  income, remaining delivery time, ETA and remaining route distance.
- `INF-201` — delivery results disclose the settled one-job income, penalties,
  parking experience and resulting evaluation.
- Claim IDs: `ETS-003`, `ETS-005`–`ETS-011`.

### Objective Genes

- `OBJ-096` — complete and settle one employer-supplied cargo delivery.
- Success, evaluation and failure: a validated destination delivery followed by
  results settlement is success; late or damaged arrival can reduce the result;
  abandoning the job, exhausting its viable settlement boundary or failing to
  deliver is terminal for this scoped job, not for the profile.
- Claim IDs: `ETS-002`, `ETS-009`, `ETS-011`.

### Time Genes

- `TIM-003` — driving, traffic, physics, fatigue, delivery time and local world
  state advance while live input remains available; selected rest deliberately
  advances the same world/job clock without direct driving input.
- Claim IDs: `ETS-004`–`ETS-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Quick Jobs lists eligible base-map offers | Accept the first scoped offer under the declared ordering | The game supplies the listed loaded truck and fixes cargo, endpoints, income and deadline | Employer-supplied one-job boundary | `ETS-002`, `ETS-003` |
| Destination route is active | Add or move one legal map waypoint | GPS recalculates the road route, ETA, remaining time and distance | Route choice changes delivery risk without automatic driving | `ETS-005` |
| Supplied articulated vehicle is on a live road | Steer, accelerate, brake and signal | Truck and trailer motion, traffic contact, fuel and separate damage states advance | Direct physical haul rather than abstract network flow | `ETS-004`, `ETS-006`, `ETS-007` |
| Truck crosses a monitored limit or signal state | Continue the violating movement | The offence is detected and an immediate fine is debited without ending the job | Law is an economic constraint, not impassable geometry | `ETS-006` |
| Mandatory Break allowance approaches zero at an eligible stop | Select at least nine consecutive rest hours | World and deadline time advance; Rest State restores and the driving allowance resets | Fatigue competes with deadline and route | `ETS-008` |
| Destination offers parking treatments | Choose the standard non-skip bay, reverse into it and detach | Articulated pose is validated before delivery can settle; easier/skip treatment changes experience | Parking is part of job evaluation | `ETS-009`, `ETS-011` |
| Trailer is validly delivered | Confirm completion | Results apply time and damage adjustments, award income and parking-sensitive experience, and close the active contract | Explicit one-job terminal | `ETS-010`, `ETS-011` |

## Strategic and experiential structure

- Local decision: preserve lane position, stopping distance and trailer sweep
  while reading traffic, signals, speed, fuel, damage and Rest State.
- Medium-term planning: compare the GPS route, custom waypoints, legal rest
  locations, remaining driving allowance and deadline before committing to a
  detour or break.
- Long-term structure: the scoped unit ends after one delivery; money and
  experience persist on the profile, but fleet and skill spending are excluded.
- Common heuristics: brake before the trailer loads the tractor through a turn;
  leave extra space in traffic; schedule the nine-hour break before zero;
  compare ETA against the deadline after every waypoint; approach the depot so
  the trailer can reverse into its bay.
- Failure attribution: GPS, law notifications, rest clocks, separate damage
  widgets and the result breakdown distinguish route, handling, compliance,
  fatigue and parking mistakes.
- Claim IDs: `ETS-004`–`ETS-011`.

## Replay and variation

- What changes between sessions: displayed offers, truck, cargo, endpoints,
  traffic, weather, route edits, damage and final evaluation.
- Randomness or procedural generation: offer and ambient-road state are sampled;
  their exact seeds are not player choices in this scope.
- Multiple viable strategies: fastest route, lower-risk motorway route and a
  waypoint through a legal rest stop can all be valid depending on current
  Rest State and deadline slack.
- Typical replay motive: improve clean driving, select a different cargo/truck
  and attempt a harder parking treatment; career accumulation is not analysed.
- Claim IDs: `ETS-003`, `ETS-005`–`ETS-011`.

## Adjacent systems and history

- Direct predecessors: driving simulations and contract-delivery games; this is
  a mechanical adjacency claim, not a title-ancestry claim.
- Variants: Freight Market adds owned-truck fuel/repair responsibility; company
  play adds garages, fleet and hired-driver accumulation; DLC expands the map
  and cargo/trailer catalogue.
- Similar games: Grand Theft Auto V shares direct road-vehicle physics, GPS and
  ambient traffic, while Mini Metro represents transport as an abstract
  player-authored network without a directly steered cargo vehicle.
- Important differences: ETS2 binds articulated handling, road compliance,
  damage, fatigue, route ETA and deadline to one explicit paid delivery and
  parking settlement.
- Claim IDs: `ETS-002`–`ETS-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-201`, `ACT-227`, `ACT-285`–`ACT-287` | exact bindings, transmission and camera are parameters |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-505`–`SYS-510` | offer, traffic and weather samples are parameters |
| Constraint | `CON-288`, `CON-428`–`CON-432` | exact limits, deadline and bay geometry are parameters |
| Information | `INF-144`, `INF-198`–`INF-201` | widget placement and unit notation are parameters |
| Objective | `OBJ-096` | cargo and endpoint identity are parameters |
| Time | `TIM-003` | selected rest duration advances the live job clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `168` (`GAME-0001`–`GAME-0168`).
- Exact genome matches: none.
- Tied near matches: `GAME-0145` — Grand Theft Auto V (`7 / 67 = 0.104478`).
- Supported combination subsets: `COMB-0167`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0145` — Grand Theft Auto V | direct vehicle operation, a personal map waypoint, occupied-vehicle physics/damage, ambient road traffic, viable driving geometry, GPS route presentation and live time | ETS2 supplies a loaded articulated truck through one commercial offer and binds road law, cargo condition, two fatigue clocks, delivery deadline, trailer bay and pay/experience settlement; GTA V instead combines freely acquired vehicles with on-foot combat, wanted pursuit, protagonist switching, authored missions, heist planning and a campaign terminal | Near, `0.104478` |

### Preserved research notes

- New genes: `ACT-285`–`ACT-287`, `SYS-505`–`SYS-510`, `CON-428`–`CON-432`,
  `INF-198`–`INF-201` and `OBJ-096`.
- Classification result: bounded new genes plus reuse and one new combination.
- Evidence and reasoning: the corpus already owns direct vehicle control,
  vehicle physics/damage, ambient traffic, a player waypoint, GPS route and live
  time. New boundaries isolate the supplied Quick Job, articulated cargo state,
  legal-road fines, 1.60 rest clocks, deadline/damage settlement, parking
  treatment and job-specific displays.

## Taxonomy impact

- Registry changes: nineteen Active genes and `COMB-0167`.
- Taxonomy-change record: none; no existing definition is deprecated, merged or split.
- Candidate terms affected: none.

## Negative results

- Mini Metro's line construction, station demand and autonomous trains are not
  reused: ETS2's road graph is authored and the player directly drives one load.
- Fleet, garage, loan, hired-driver and recurring-company economy are excluded:
  one Quick Job only writes its result to the profile.
- Driving Academy is corroborating evidence for articulated parking, not part
  of the selected delivery mode.
- DLC does not silently enter through currently displayed map or cargo offers;
  both endpoints must carry the official original-game label.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний Quick Job у базовій версії 1.60 поєднує
  позичену вантажівку з вантажем, пряме керування, GPS, дорожні правила,
  пошкодження, Rest State/Mandatory Break, дедлайн, паркування й розрахунок
  одного рейсу (`ETS-001`–`ETS-011`).

## Нові гени

- [Observation | Corroborated | High] Дев'ятнадцять нових меж ізолюють Quick
  Job, керований відпочинок, спосіб здачі причепа, зчленовану фізику вантажу,
  штрафи, два годинники втоми, розрахунок рейсу та спеціальні job/HUD/result
  представлення.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0167` — один оплачуваний Quick Job від
  вибору пропозиції через керовану доставку й обов'язковий відпочинок до
  парковки та фінального розрахунку.

## Зміни таксономії

- [Confirmed | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-007` — Physics and object manipulation: steering and braking must move a
  tractor and articulated trailer through collision geometry into a valid bay.
- `FAM-010` — Real-time system pressure: traffic, deadline, damage, fuel and two
  fatigue clocks keep changing while the player drives or rests.
- No new family is created from one game.

## Plain-language interpretation

A Quick Job begins with a meaningful trade-off before the engine starts. The
offer fixes a borrowed truck, a loaded trailer, destination, route length,
deadline and advertised income. After acceptance, the road is not an abstract
connection: the player must control a heavy articulated body through traffic,
signals, speed limits and collision geometry. A shorter route can be harder to
drive; a safer route or rest stop consumes deadline slack.

Version 1.60 makes fatigue a two-clock planning problem. Rest State declines
toward microsleep while Mandatory Break separately limits legal driving to ten
hours and needs nine consecutive hours of rest. At the depot, the trailer must
still be placed in a chosen bay or the player must accept an easier/skip option.
Only the result screen closes the unit by turning time, damage and parking into
income, experience and a visible evaluation.

## New questions

- Which delivery game preserves the same route/deadline/damage settlement while
  replacing direct steering with autonomous fleet scheduling?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0170` — S.T.A.L.K.E.R. 2: Heart of Chornobyl.
- Optimisation criterion: continue the recorded four-game Goal in immutable
  demand-led order after one bounded road-haul settlement.
- Expected gene pressure: open-world survival combat, anomalies, artefacts,
  radiation, inventory burden and authored branching mission state.
- Anti-bias note: do not import ETS2's road law, employer contract or vehicle
  settlement into a Zone exploration scope.

## Next research step

- Integrate `GAME-0170` — S.T.A.L.K.E.R. 2: Heart of Chornobyl after the required thirty-second stop window.

## Design lessons

- A transport job becomes mechanically rich when route, vehicle geometry,
  fatigue and contract settlement all share one clock.
- A road-law rule can be economically binding without making illegal movement
  physically impossible.

## Open questions

- Does a later owned-truck scope warrant a separate genome when fuel, repair and
  company capital become player-paid instead of employer-supplied?
