---
game_id: GAME-0335
slug: rollercoaster-tycoon-deluxe
game_title: RollerCoaster Tycoon Deluxe
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-139
    - ACT-455
    - ACT-485
    - ACT-486
    - ACT-487
    - ACT-488
  system:
    - SYS-045
    - SYS-154
    - SYS-198
    - SYS-950
    - SYS-951
    - SYS-952
    - SYS-953
  constraint:
    - CON-171
    - CON-654
    - CON-655
  information:
    - INF-058
    - INF-072
    - INF-362
  objective:
    - OBJ-196
  time:
    - TIM-003
---

# Game: RollerCoaster Tycoon Deluxe

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Forest Frontiers,
Steel Mini Roller Coaster, guest names, exact ride designs and October Year 1
thresholds are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the current official English Windows Steam application
  `285310`, sold as `RollerCoaster Tycoon: Deluxe`, with the original game's
  base campaign plus Corkscrew Follies and Loopy Landscapes. This packet uses
  only the base-game `Forest Frontiers` scenario.
- Structured analysis target: licensed Windows Steam access to application
  `285310`; see `GAME-0335` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: a fresh player-controlled Forest Frontiers attempt, without
  tutorial automation, from the initially closed and empty park through the
  scenario evaluation at the end of October, Year 1.
- Entry: the player receives an undeveloped park, the park is closed, no guests
  are inside, and the objective requires at least 250 guests with a Park Rating
  of at least 600 when the deadline is evaluated.
- Primary decision loop: inspect the objective, date, finances and guest
  thoughts; place rides, stalls, footpaths and queue lines or design a custom
  tracked ride; connect its entrance and exit; set ride, dispatch and admission
  policies; open rides and the park; hire and zone a mechanic; observe guests,
  queues, purchases, needs, ride operation, breakdowns, cash and Park Rating;
  revise the park before the fixed deadline.
- Positive terminal: the end-of-October Year 1 evaluation finds at least 250
  guests and Park Rating at least 600 and declares the scenario complete.
- Failure terminal: either threshold is below its required value at that same
  evaluation. Continued play after the result is outside this packet.
- Included: fixed-footprint rides and stalls; custom Steel Mini Roller Coaster
  track and station; entrances, exits, paths and queues; park and ride open
  states; admission and ride prices; load and wait policies; live guests with
  money, preferences, needs, happiness and thoughts; queues, boarding, ride
  cycles and exits; itemised finance, loans, construction costs, upkeep and
  wages; mechanics, inspections, breakdowns and repairs; Park Rating, arrivals,
  date and the exact scenario objective.
- Reproducible parameterisation: build a connected, operable park whose guest
  flow and rating cross both declared thresholds before the deadline. Exact
  ride designs, prices, path layout, purchase sequence, loan state, inspection
  interval and guest histories remain bounded decisions rather than a single
  prescribed solution.
- Excluded: tutorial-controlled steps; scenarios after Forest Frontiers;
  Corkscrew Follies and Loopy Landscapes scenarios or expansion-only content;
  marketing campaigns, research progression, land or construction-rights
  purchase, landscape transformation beyond ordinary legal placement, custom
  scenario creation, sandbox tools, cheats, saved-game inheritance, multiplayer,
  OpenRCT2, mobile/console ports and later RollerCoaster Tycoon games. Those
  systems may exist in the product but are not necessary to the bounded result.
- Direct-play status: not conducted. No entitlement, installation, executable,
  save, screenshot, video, audio or input trace was used. The official
  Steam-hosted manual and current product listing support a source-bounded
  reconstruction rather than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RCT-001` | The target is the current Steam Deluxe package, but the packet is base-game Forest Frontiers only | Confirmed | Direct | High | P1, P2 |
| `RCT-002` | Forest Frontiers begins closed and empty and evaluates 250 guests plus Park Rating 600 at the end of October, Year 1 | Confirmed | Direct | High | P2, S1 |
| `RCT-003` | Fixed rides, stalls, paths and custom track consume park funds and must satisfy placement and clearance rules | Confirmed | Direct | High | P2 |
| `RCT-004` | An attraction requires a station, entrance, exit and connected guest access; queue and exit paths serve distinct flow | Confirmed | Direct | High | P2 |
| `RCT-005` | The player can test/open a ride and configure price, load, station waits and inspection interval | Confirmed | Direct | High | P2 |
| `RCT-006` | Guests autonomously route, queue, spend or refuse, experience rides and expose needs, happiness and thoughts | Confirmed | Direct | High | P2 |
| `RCT-007` | Park Rating aggregates operational qualities and its reputation contributes to guest arrivals | Confirmed | Direct | High | P2 |
| `RCT-008` | Construction, upkeep, wages, income, debt and cash are visible in an itemised managed budget | Confirmed | Direct | High | P2 |
| `RCT-009` | Rides can be inspected, break down and return to operation after a reachable mechanic completes the job | Confirmed | Direct | High | P2 |
| `RCT-010` | The two threshold predicates are tested together at one fixed deadline | Confirmed | Direct | High | P2, S1 |
| `RCT-011` | No direct play or installed-build parity check is claimed | Observation | Direct | High | V1 |
| `RCT-012` | The signature admits only causal transitions available in the bounded Forest Frontiers packet | Observation | Direct | High | P1, P2, S1, V1 |

## Basic data

- Release / origin: Chris Sawyer Productions; the original RollerCoaster
  Tycoon debuted on Windows in 1999. The current Steam Deluxe package is
  published by Atari and bundles the original game with its two expansions.
- Platform or physical form: licensed digital Windows PC package.
- Puzzle family: route and network construction; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/285310/RollerCoaster_Tycoon_Classic/?l=english),
    for the current licensed Windows product, developer/publisher attribution
    and Deluxe package contents.
  - **[P2]** [official Steam-hosted RollerCoaster Tycoon Deluxe manual](https://cdn.akamai.steamstatic.com/steam/apps/285310/manuals/rollercoaster_tycoon.pdf),
    for Forest Frontiers entry and objective; construction, track, station,
    entrance, exit, paths, queues, test/open states, pricing, dispatch rules,
    guests, rating, finance, staff, inspections, breakdowns and repair.
- Secondary corroboration:
  - **[S1]** [StrategyWiki Forest Frontiers scenario page](https://strategywiki.org/wiki/RollerCoaster_Tycoon/Forest_Frontiers),
    used only to corroborate the empty closed entry and exact deadline/threshold
    statement already present in P2.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1, P2 and S1;
    rules reasoning only, with no direct play or audiovisual observation.
- Claim IDs: `RCT-001`–`RCT-012`.

## Mechanical decomposition

### Action Genes

- `ACT-006`: change the live simulation speed or pause it while inspecting and
  editing the park; pausing does not replace the deadline clock.
- `ACT-139`: place fixed-footprint rides, shops and facilities on legal park
  terrain, paying their construction costs.
- `ACT-455`: draw connected pedestrian paths and distinct queue lines that
  guests and staff can traverse.
- New `ACT-485`: place or remove priced custom track and station segments, then
  place the ride entrance and exit.
- New `ACT-486`: test, open or close one ride and set its admission, load,
  minimum/maximum station waits and inspection policy.
- New `ACT-487`: open or close the whole park and set its available admission
  price independently from ride policies.
- New `ACT-488`: hire and place a mechanic, then optionally constrain its patrol
  area and enabled work without directly steering its steps.
- Claims: `RCT-003`–`RCT-005`, `RCT-008`, `RCT-009`.

### System Behaviour Genes

- `SYS-045`: guests and staff walk autonomously across reachable paths and
  queues rather than awaiting a movement command for every step.
- `SYS-154`: construction, ride upkeep and staff wages repeatedly change one
  shared treasury while the park operates.
- `SYS-198`: each guest's needs, experiences, happiness and thoughts change
  over time and influence later decisions.
- New `SYS-950`: an open attraction admits guests from its queue, boards
  available capacity, dispatches under the configured policy, completes its
  cycle, releases riders at the exit and repeats.
- New `SYS-951`: each guest evaluates reachable rides and services against
  preference, need, price, value and remaining money, then walks, queues, pays,
  refuses or leaves.
- New `SYS-952`: the simulation aggregates service, layout, tidiness, value,
  efficiency and safety into Park Rating, whose reputation affects arrivals.
- New `SYS-953`: an attraction ages, receives scheduled inspections, may break
  down and returns to operation after an eligible reachable mechanic repairs it.
- Resolution order: edits and policies update persistent park state; live time
  advances guest and staff motion, needs, purchases, queues and ride cycles;
  finance settles; inspection or breakdown jobs are assigned; rating and
  arrivals update; the deadline compares both objective thresholds.
- Claims: `RCT-006`–`RCT-010`.

### Constraint Genes

- `CON-171`: the park treasury must pay upfront construction and recurring
  operation; borrowing and deficit rules bound continued expansion.
- New `CON-654`: custom track, station and vehicle geometry must satisfy
  segment connection, grade, direction, support and clearance requirements.
- New `CON-655`: a guest-serving attraction needs a connected station entrance,
  queue/access route and exit path before ordinary service can function.
- Scarce state: cash/loan headroom, land, path connectivity, station capacity,
  queue space, mechanic coverage, time, guest money and rating margin.
- Claims: `RCT-003`, `RCT-004`, `RCT-008`–`RCT-010`.

### Information Genes

- `INF-058`: the finance window exposes itemised income, expenditure, loan,
  cash, Park Value and weekly profit rather than only a single balance.
- `INF-072`: selecting a guest exposes current activity, needs and thoughts,
  allowing local failure attribution without direct control.
- New `INF-362`: park and attraction panels expose the scenario objective,
  date, attendance, Park Rating, ride state, queue, price, reliability,
  inspection and breakdown information needed to operate the bounded park.
- Claims: `RCT-002`, `RCT-005`–`RCT-010`.

### Objective Genes

- New `OBJ-196`: at the end of October, Year 1, have at least 250 guests and
  Park Rating at least 600; both predicates must hold at the same evaluation.
- Claims: `RCT-002`, `RCT-010`.

### Time Genes

- `TIM-003`: guests, staff, rides, queues, needs, finances, wear and the calendar
  continue on the live simulation clock between local player edits.
- Claims: `RCT-006`–`RCT-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Forest Frontiers is closed and empty | open the scenario objective | the panel declares the end-of-October Year 1 deadline, 250-guest threshold and Park Rating 600 threshold | exact entry and terminal | `RCT-002` |
| Legal empty park terrain and sufficient cash exist | place a fixed ride or one custom track segment | the footprint/segment is accepted, becomes persistent and deducts its declared construction cost; illegal clearance is rejected | priced spatial construction | `RCT-003` |
| A custom ride has station and closed legal track | place entrance/exit and draw connected queue/exit paths | the attraction gains separate reachable intake and discharge routes | service connectivity | `RCT-004` |
| A connected ride is closed | choose test, set operating policy, then open | test cycles expose ride state; open operation admits eligible queued guests under load/wait rules | commissioning and dispatch | `RCT-005`, `RCT-006` |
| The park is closed | set admission policy and open it | arriving guests may enter, retain personal money and begin choosing reachable destinations | venue admission | `RCT-005`, `RCT-006` |
| A guest sees a reachable open ride | allow live time to advance | preference, need, price, money and perceived value bound walking, queueing, purchase/refusal and subsequent thought | autonomous decision | `RCT-006` |
| An operating ride reaches inspection or breakdown state | employ a reachable mechanic and advance time | a job is assigned; the mechanic walks to the ride, inspects or repairs it and ordinary operation can resume | spatial maintenance loop | `RCT-009` |
| Park operation changes guest experience, layout or service quality | advance the simulation | bounded Park Rating and later guest arrival pressure update from current operation | aggregate feedback | `RCT-007` |
| Calendar reaches the end of October Year 1 | allow the scenario evaluation to resolve | success occurs only if guests ≥250 and Park Rating ≥600; otherwise the scenario fails | conjunctive fixed deadline | `RCT-010` |

## Strategic and experiential structure

- Local decision: place one legal path, ride, queue, facility or policy change
  while preserving cash and keeping guest routes intelligible.
- Medium-term planning: balance capacity, value, prices, queue length, guest
  needs, maintenance coverage and borrowing so the park grows without trading
  attendance for a collapsing rating.
- Long-term structure: transform an empty closed plot into a connected live
  service network that simultaneously crosses attendance and quality thresholds
  at a known date.
- Common heuristics: open a small connected ride set early; use guest thoughts
  to locate recurring need or value problems; avoid queues that exceed service
  throughput; cover rides with a mechanic and inspection policy; keep enough
  cash or loan headroom for corrective construction before the deadline.
- Failure attribution: objective, finance, ride and guest panels distinguish
  insufficient attendance, poor rating, disconnected flow, bad value, unmet
  needs, breakdown downtime and insolvency.
- Claims: `RCT-002`–`RCT-012`.

## Replay and variation

- What changes between attempts: ride mix and custom geometry, path/queue graph,
  prices, dispatch rules, construction order, staffing, finances, guest
  histories, breakdown timing, attendance and rating margin.
- Randomness or procedural generation: Forest Frontiers terrain and objective
  are authored; individual arrivals, choices, ride reliability and live timing
  produce bounded operational variation rather than a generated scenario map.
- Multiple viable strategies: many connected ride portfolios and pricing/staff
  policies can satisfy the two thresholds; no specific coaster is mandatory.
- Typical replay motive: finish with more guests, rating, cash or park value;
  build a different layout; or continue to later scenarios. Only the first
  deadline evaluation belongs to this record.

## Adjacent systems and history

- Direct predecessors: theme-park management and construction simulations
  already combine spatial layout with service capacity; this packet isolates
  the authored pedestrian/queue/ride graph and per-guest decision economy.
- Variants: later base and expansion scenarios alter objective parameters;
  OpenRCT2, console/mobile ports and later series entries require independent
  version evidence and cannot inherit this signature automatically.
- Similar games: Theme Park, Zoo Tycoon and Cities: Skylines share managed
  construction, live agents, budgets and service feedback, but not this exact
  attraction-station/queue/dispatch and guest-thought boundary set.
- Important difference: a ride queue is not a generic road or scheduled route:
  it terminates at attraction capacity and configured dispatch, then discharges
  riders through a distinct exit path.

## Normalised genome

The front matter is canonical. The complete signature contains 22 Active
genes: seven Action, seven System Behaviour, three Constraint, three
Information, one Objective and one Time gene. Ride names, layouts, guests and
threshold values remain carrier parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `334` (`GAME-0001`–`GAME-0334`).
- Exact genome matches: none.
- Tied near matches: `GAME-0118` — SimCity 4 Deluxe Edition (`5 / 33 = 0.151515`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0118` — SimCity 4 Deluxe Edition | `ACT-006`, `SYS-154`, `CON-171`, `INF-058`, `TIM-003` | Both let the player pace a live managed domain whose construction and recurring costs flow through an itemised treasury. SimCity 4 adds zoning, utilities, transport, civic services, taxation and open-ended municipal growth. Forest Frontiers instead adds authored rides, pedestrian paths and queues, per-guest needs and purchases, capacity-governed dispatch, mechanics and breakdowns, Park Rating feedback and one fixed two-threshold deadline. | Near, `5 / 33 = 0.151515` |

## Taxonomy impact

`ACT-485`–`ACT-488`, `SYS-950`–`SYS-953`, `CON-654`, `CON-655`, `INF-362`
and `OBJ-196` are new. `TAXONOMY_CHANGE_078` generalises `SYS-198`,
`CON-171`, `INF-058` and `INF-072` from their first resident/municipal carriers
to the same transferable person-state and managed-domain operations in a park.
`ACT-139` gains fixed rides and stalls as supporting carriers without changing
its ordinary fixed-footprint boundary. No earlier signature changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, installed-build parity, exact hidden formula, precise arrival
  RNG, optimal layout or prescribed construction trace is claimed.
- Marketing, research, land purchase and expansion content are not admitted
  merely because the full product contains them.
- Guest thoughts are information about causal state, not proof that every
  internal preference or rating weight is visible.
- The scenario threshold is not converted into an endless score target: it is
  checked conjunctively at one declared deadline.

## Delta summary

## New facts

- [Confirmed | Direct | High] The official manual closes Forest Frontiers'
  entry, exact deadline/thresholds and all required construction, service,
  guest, finance, rating and maintenance transitions.
- [Confirmed | Direct | High] The current official product listing bounds the
  licensed Deluxe package while the record explicitly excludes its expansions.

## New genes

- [Confirmed | Direct | High] Twelve new boundaries isolate custom attraction
  construction and commissioning, venue admission, autonomous staff, queues,
  guest transactions, park feedback, ride maintenance, geometry/access gates,
  operating panels and the fixed two-threshold deadline.

## New combinations

- [Observation | Direct | High] None; recurrence remains evidence-driven.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_078` generalises four stable
  lower IDs without changing any earlier game signature.

## New questions

- Which independent park or venue simulation reproduces the complete
  queue-capacity-dispatch-exit boundary without inheriting RCT terminology?
- Which later carrier supports the same rating-to-arrival feedback while making
  its component weights directly observable?

## Next recommended game

- `GAME-0336` Pokémon Red Version, as reserved by selection 023.

## Why this game

- RollerCoaster Tycoon Deluxe is a recognisable PC management anchor whose
  simplest scenario exposes how spatial construction, autonomous people,
  service capacity, finance, maintenance and a deadline interact.

## Completion checklist

- [x] Exact product, base scenario, entry, terminal and exclusions declared.
- [x] Product identity, official manual and secondary objective corroboration separated.
- [x] Construction, guest flow, ride operation, finance, rating, maintenance and objective decomposed.
- [x] Deterministic comparison migration completed.
- [x] Reviewed Ukrainian, presentation, platform, families, salience and plain language integrated.
- [x] Original artwork and responsive variants integrated.
- [x] Repository, localisation, build, browser and accessibility gates passed.

## Search-demand continuation

This unit fulfils the second reserved subject in
[`SEARCH_DEMAND_GAME_SELECTION_023`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_023.md).
`GAME-0336` Pokémon Red Version is the next recorded Goal unit.
