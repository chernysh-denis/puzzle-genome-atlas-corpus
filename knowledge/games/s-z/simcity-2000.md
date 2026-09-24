---
game_id: GAME-0390
slug: simcity-2000
game_title: SimCity 2000
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids:
  - COMB-0117
gene_ids:
  action:
    - ACT-006
    - ACT-068
    - ACT-116
    - ACT-117
    - ACT-118
  system:
    - SYS-151
    - SYS-152
    - SYS-153
    - SYS-154
    - SYS-155
  constraint:
    - CON-170
    - CON-171
  information:
    - INF-057
    - INF-058
  objective:
    - OBJ-053
  time:
    - TIM-003
---

# Game: SimCity 2000

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Terrain, zone
density, tax percentages and accounting amounts are parameters, not genes.

## Analysis scope

- Version / ruleset: the original English PC DOS *SimCity 2000* rules
  documented by Maxis's original manual, in ordinary **Start New City** mode
  with the default Easy difficulty and 1900 starting year. This is not a
  scenario, the terrain editor, a later console port or the GOG Special
  Edition executable. The manual describes multiple computer interfaces;
  its DOS-specific file-name note anchors this target without establishing an
  exact binary revision.
- Structured analysis target: `GAME-0390` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: confirm a newly named city with Easy and 1900; close the founding
  newspaper and first reach control of its initially undeveloped generated
  terrain. Set **No Disasters** on and leave **Auto-Budget** off so the annual
  accounting window remains observable.
- Primary decision loop: inspect residential/commercial/industrial demand and
  the available tiles; draw connected roads and power lines, authorise each of
  the three zone uses, place a power plant and optionally a powered water pump
  with connected underground pipes; adjust the property-tax rate or service
  funding while reading the budget; let the simulation develop private lots,
  distribute power and water, generate journeys and update demand; inspect
  overlays and revise land use or infrastructure until the first January
  budget review **after a complete ordinary city-year** opens.
- Positive terminal: that first post-year January Budget window displays the
  completed year's revenue and expenditure beside the next annual estimate.
  It is an analytic observation checkpoint, not an authored victory or a
  requirement that the treasury be positive. The underlying city can continue.
- Negative terminal: none is authored within this packet. Insufficient access
  or disconnected power may stall development; the observer still ends at the same January
  review if the simulation advances. No bankruptcy or disaster result is
  asserted for the interval.
- Included: three-zone authorisation, road access, power generation and lines,
  optional water pump and pipes, autonomous lot growth, aggregate trips and
  traffic, RCI demand, diagnostic maps, treasury, property tax and funding,
  construction cost, recurring revenue/expense, pause or speed control and
  the January Budget window.
- Excluded: scenarios and their win conditions, pre-foundation terrain editing,
  disasters, cheats, bonds, ordinances, neighbour deals, long-term technology
  unlocks, subway/bus/highway systems not yet available in 1900, airports,
  seaports, arcologies, detailed education/police/fire optimisation, exact
  demand formula, any year after the checkpoint, GOG edition-specific extras
  and any claim of directly captured play.
- Reproducible parameterisation: select ordinary new city, Easy and 1900,
  disable disasters, keep Auto-Budget off, record the generated terrain and
  each road/zone/utility placement, tax or funding change, simulated date,
  demand indication, supplied-lot overlay and cash; let the first full city
  year elapse and read the automatically opened next January Budget window.
  The precise terrain, tile locations, growth amount, traffic load and balance
  are run outputs, not prescribed successes. A waterless low-density start is
  allowed by the manual, while a water-connected route tests the higher-density
  service branch.
- Potential scoped modules: later transport unlocks and a commuter-network
  stress test, long-run water capacity, a disaster scenario, municipal debt,
  ordinances, the terrain editor and Special Edition-specific content.
- Direct-play status: none. The original Maxis manual supplies the start,
  zoning, network, growth, budget and traffic rules. No DOS executable, save,
  controller trace, video or audio was inspected. The GOG product page proves
  a licensed related Special Edition is offered, not that its current binary
  was the one analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC2K-001` | Ordinary new city defaults to Easy and 1900, then presents an initially undeveloped tiled landscape. | Confirmed | Direct | High | P1 |
| `SC2K-002` | A small city needs residential, commercial and industrial zones, a power source and lines, and roads; residents build private structures on authorised land. | Confirmed | Direct | High | P1 |
| `SC2K-003` | Zone demand, growth and maps change with city state; the RCI indicator can lag an intervention. | Confirmed | Direct | High | P1 |
| `SC2K-004` | Pumps require power, pipes are laid underground, and an absent water system limits density rather than forbidding a city. | Confirmed | Direct | High | P1 |
| `SC2K-005` | The January budget review itemises last-year totals and next-year estimates, and allows tax and funding adjustments; Auto-Budget suppresses its automatic opening. | Confirmed | Direct | High | P1 |
| `SC2K-006` | The simulation generates trips by building and zone type rather than tracking every citizen; road load can produce congestion and pollution. | Confirmed | Direct | High | P1 |
| `SC2K-007` | The manual's No Disasters setting removes random disasters from the tutorial-like ordinary-city interval. | Confirmed | Direct | High | P1 |
| `SC2K-008` | GOG offers a licensed SimCity 2000 Special Edition, but this packet does not establish binary equivalence with the original DOS target. | Observation | Limited | Medium | P2, R1 |
| `SC2K-009` | The exact original DOS executable revision, generated map, quantitative growth, cash outcome and demand algorithm were not inspected. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: original Maxis *SimCity 2000* PC DOS release and its
  English instruction manual. The nearby licensed GOG Special Edition is a
  distribution reference, not substituted as an inspected ruleset.
- Platform or physical form: mouse-driven isometric city simulation on DOS;
  the structured target is `PLAT-DOS`.
- Puzzle families: `FAM-005` route and network construction and `FAM-010`
  real-time system pressure.
- Primary source, checked 2026-09-24: **[P1]** [original Maxis SimCity 2000
  manual](https://classicreload.com/sites/default/files/sim-city-2000-manual.pdf),
  a scan of the original publisher booklet. The mirror hosts the booklet but
  is not an independent gameplay witness.
- Product reference, checked 2026-09-24: **[P2]** [licensed GOG Special Edition
  page](https://www.gog.com/en/game/simcity_2000_special_edition), used only
  for related current availability and edition distinction.
- **[R1]** bounded source, edition and direct-play audit in this record.
- Claim IDs: `SC2K-001`–`SC2K-009`.

## Mechanical decomposition

### Action Genes

- `ACT-006` changes simulation rate; `ACT-068` edits the connected road graph;
  `ACT-116` authorises residential, commercial and industrial parcels rather
  than selecting each private building; `ACT-117` places paid power and water
  facilities and distribution segments; `ACT-118` changes tax or service
  funding. Claim IDs: `SC2K-002`, `SC2K-004`, `SC2K-005`.
- Candidate genes: none. The underground water layer is a placement parameter
  of `ACT-117`, not a separate action type.

### System Behaviour Genes

- `SYS-151` develops eligible zoned lots, `SYS-152` recalculates RCI demand,
  `SYS-153` propagates power and optional water, `SYS-154` settles recurring
  city accounts, and `SYS-155` generates aggregate journeys and road load.
- Resolution order: commit zoning/network/fiscal change; advance simulated
  time; recompute coverage, access, demand and journeys; permit private growth
  on eligible lots; credit/debit recurring accounts; present the annual review.
  Claim IDs: `SC2K-002`–`SC2K-006`.

### Constraint Genes

- `CON-170` gates a given development stage on road access and its enabling
  service prerequisites. Water is **not** a universal prerequisite: the manual
  explicitly permits a city without it but limits density. `CON-171` gates
  paid construction and sustainable upkeep on municipal funds.
- Scarce resources: buildable tiles, road and utility reach, capacity, cash
  and time before the review. Claim IDs: `SC2K-002`, `SC2K-004`, `SC2K-005`.

### Information Genes

- `INF-057` shows the RCI bars and selectable spatial overlays, including
  power/water coverage and traffic. `INF-058` itemises the current fiscal
  balance, completed-year figures and projected next-year accounts.
- The internal demand formula and exact future growth remain hidden; the
  visible indicators are diagnostic projections, not omniscience. Claim IDs:
  `SC2K-003`, `SC2K-005`, `SC2K-006`.

### Objective Genes

- `OBJ-053` describes ongoing city viability and growth, not the analytical
  stop at one annual review. The January window evaluates policy consequences
  without turning open-ended play into a prescribed win or loss.
- Claim IDs: `SC2K-002`, `SC2K-005`.

### Time Genes

- `TIM-003` advances city demand, construction, travel and finances while the
  mayor can edit; pausing/speed choice is represented by `ACT-006`. The
  January window is an observation checkpoint inside this continuing clock.
- Claim IDs: `SC2K-003`, `SC2K-005`, `SC2K-006`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty accessible tiles and a funded treasury | Draw roads, three zone uses, plant and connecting lines; advance | Eligible lots may grow privately as power and demand reach them | zoning authorises rather than places buildings | `SC2K-002`, `SC2K-003` |
| An occupied district lacks water | Connect a powered pump by underground pipe; inspect water map | Supplied status changes and a density limit can be lifted | water is a conditional density enabler, not universal start gate | `SC2K-004` |
| Residential and job districts are separated | Keep a road path, advance time and inspect traffic map | Building-level trip generation loads roads, potentially congesting them | road topology affects simulated activity | `SC2K-006` |
| The city has operating expenses | Change property tax or service funding, leave Auto-Budget off, advance through year end | The next January window shows completed-year amounts and next-year estimate | recurring policy and accounts have a visible review | `SC2K-005` |
| Available cash is limited and a planned utility has a price | Compare its cost with the itemised budget before placement | A placed facility spends city funds and adds ongoing obligations | fiscal limits constrain layout choices | `SC2K-005` |

## Strategic and experiential structure

- Local decision: diagnose demand, reach and cost before zoning or adding a
  facility. Medium-term planning: align the three zone uses with roads, power
  and a chosen water-density path while preserving a workable budget.
- Long-term structure: indirect private development responds to municipal
  authorisation and coverage, and the player-defined city can continue after
  the one-year observation point.
- Failure attribution: demand bars and overlays show symptoms; the itemised
  fiscal window makes annual consequences auditable, but not every inner
  parameter of growth is visible. Claim IDs: `SC2K-002`–`SC2K-006`.

## Replay and variation

- New terrain, zone layout, route graph, pump location, tax settings, growth
  and travel produce different city states. No fixed solution, prescribed
  treasury result or win screen belongs to this ordinary packet.
- The generated landscape is a recorded run parameter. We do not claim a
  deterministic replay seed or a particular revenue outcome. Claim IDs:
  `SC2K-001`, `SC2K-009`.

## Adjacent systems and history

- *SimCity 4 Deluxe Edition* uses the same sixteen-gene signature at this
  taxonomy resolution, but its Rush Hour neighbour and transport options are
  not silently inserted into this 1900 first-year packet. Exact genome match
  means structural equality, not equal simulation parameters or editions.
- Later transport and ordinance systems in *SimCity 2000* are deferred as
  potential scoped modules rather than smuggled into the first-year sample.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-006`, `ACT-068`, `ACT-116`, `ACT-117`, `ACT-118` | speed, layout, zone density, facility and rate |
| System | `SYS-151`–`SYS-155` | demand, capacity, accounting and trip cadence |
| Constraint | `CON-170`, `CON-171` | access, water-density threshold and cash |
| Information | `INF-057`, `INF-058` | overlays and estimate detail |
| Objective | `OBJ-053` | player-defined growth horizon |
| Time | `TIM-003` | simulation rate and January observation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `389` (`GAME-0001`–`GAME-0389`).
- Exact genome matches: `GAME-0118` — SimCity 4 Deluxe Edition.
- Tied near matches: `GAME-0121` — Cities: Skylines (`16 / 23 = 0.695652`).
- Supported combination subsets: `COMB-0117`.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0118` — SimCity 4 Deluxe Edition | All sixteen genes cover zoning, services, private growth, sector demand, journeys, budgets and open-ended city viability. | SimCity 2000 starts in 1900 with a yearly January review and underground water pipes; SimCity 4 Deluxe includes a later transport expansion and neighbouring-city interactions. Those edition, parameter and bounded-route differences do not change this complete signature. | Exact, `16 / 16 = 1.000000` |
| `GAME-0121` — Cities: Skylines | The same sixteen city-planning genes recur across zoning, priced infrastructure, private growth, demand, service distribution, generated trips and fiscal review. | Cities: Skylines additionally makes transit-line editing, district policy and progression milestones decision-relevant; none belongs to the first-year SimCity 2000 packet. | Near, `16 / 23 = 0.695652` |

## Taxonomy impact

- Registry changes: no new gene or combination. Original manual evidence
  independently corroborates the existing city-management combination.
- Taxonomy-change record: none. No existing signature is revised.

## Negative results

- An annual January Budget popup is not a new time gene: it exposes an
  instance of recurring budget settlement (`SYS-154`, `INF-058`).
- Underground water pipes do not form a new gene: spatial placement and
  coverage are already represented by `ACT-117` and `SYS-153`.
- A city without water remains possible at low density, so the analysis does
  not claim water is a universal settlement prerequisite.
- GOG Special Edition may share this core, but product availability does not
  prove binary equivalence. No such equivalence enters the genome claim.

## Delta summary

## New facts

- [Confirmed | Direct | High] Maxis's original manual supports the one-year
  zoning, utility, traffic and annual-budget packet (`SC2K-001`–`SC2K-007`).

## New genes

- [Observation | Direct | High] No new genes; all sixteen are reused.

## New combinations

- [Observation | Direct | High] No new combination; `COMB-0117` gains a third
  supporting game.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy change and no older signature
  revision.

## New questions

- Does the licensed Special Edition preserve this exact one-year DOS rule
  packet? Availability alone does not establish its binary equivalence.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0391` Uncharted 2: Among Thieves.
- Optimisation criterion: contrast open-ended mayor planning with an authored
  traversal and combat expedition.
- Backlog impact: follows the approved nine-game order after the Goal stop
  window; not started in this game commit.

## Why this game

- [Hypothesis | Limited | Medium] A visually and mechanically distinct
  cinematic expedition tests the next action-versus-system boundary.
