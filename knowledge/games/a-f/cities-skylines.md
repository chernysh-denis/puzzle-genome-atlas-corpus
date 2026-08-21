---
game_id: GAME-0121
slug: cities-skylines
game_title: "Cities: Skylines"
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0117
gene_ids:
  action:
    - ACT-006
    - ACT-023
    - ACT-068
    - ACT-116
    - ACT-117
    - ACT-118
    - ACT-132
  system:
    - SYS-031
    - SYS-151
    - SYS-152
    - SYS-153
    - SYS-154
    - SYS-155
    - SYS-169
  constraint:
    - CON-048
    - CON-050
    - CON-170
    - CON-171
    - CON-179
  information:
    - INF-057
    - INF-058
  objective:
    - OBJ-053
  time:
    - TIM-003
---

# Game: Cities: Skylines

## Analysis scope

- Version / ruleset: current original Windows PC base game, ordinary new-game
  city on a supplied map from the initial tile through the Megalopolis
  population milestone.
- Included: roads; residential, commercial, industrial and office zoning;
  autonomous private development and upgrading; electricity, water, sewage,
  waste and civic services; taxes, service budgets and loans; citizen trips,
  congestion and base-game public-transport lines; districts and base-game
  policies; population milestones, purchasable map areas, pause and simulation
  speed.
- Excluded: all paid and free DLC feature sets, content-creator assets, mods,
  Steam Workshop content, scenarios, unlimited-money / unlock-all options,
  map and asset editors, console Remastered changes and Cities: Skylines II.
- Direct-play status: not conducted. The official PC manual supplies the
  zoning, service, transport, economy, policy and milestone rules; the official
  store and publisher pages establish the product and base-game boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CSL-001` | The player zones road-adjacent land while demand and local conditions determine which private buildings grow and upgrade | Confirmed | Direct | High | P1 |
| `CSL-002` | Priced utilities and civic facilities distribute capacity or coverage that changes viability, health, safety and land value | Confirmed | Direct | High | P1, P3 |
| `CSL-003` | Citizen and goods trips load the road network, while player-authored public-transport lines carry bounded passenger flows | Confirmed | Corroborated | High | P1, P2, P3 |
| `CSL-004` | Taxes, service budgets, upkeep, loans and recurring revenue jointly determine municipal solvency | Confirmed | Direct | High | P1 |
| `CSL-005` | The player paints districts and applies persistent local policies or industrial specialisations to their bounded area | Confirmed | Direct | High | P1, P2 |
| `CSL-006` | Population milestones persistently unlock services, zones, policies, loans and additional purchasable map areas | Confirmed | Direct | High | P1 |
| `CSL-007` | Demand bars, information views, building details and the itemised economy panel expose selected city state without revealing the complete simulation formula | Confirmed | Direct | High | P1 |
| `CSL-008` | The scoped PC base game is distinct from DLC, editors, mods, Remastered and the sequel | Confirmed | Corroborated | High | P1, P2, P3 |
| `CSL-009` | At current Atlas resolution Cities: Skylines recurs with SimCity 4's complete twelve-gene zoned-city combination while adding ordered transit lines, districts and milestone gating | Observation | Corroborated | High | P1, GAME-0118, COMB-0117 |

## Basic data

- Release / origin: Colossal Order and Paradox Interactive, 2015.
- Platform or physical form: pausable real-time desktop city simulation.
- Puzzle family: real-time system pressure; route and network construction;
  municipal simulation.
- Primary sources: **[P1]** [official Cities: Skylines PC user manual](https://shared.steamstatic.com/store_item_assets/steam/apps/255710/manuals/CitiesSkylines-UserManual_EN.pdf);
  **[P2]** [official Steam product page](https://store.steampowered.com/app/255710/Cities_Skylines/);
  **[P3]** [official Paradox Cities: Skylines page](https://www.paradoxinteractive.com/games/cities-skylines/cities-skylines-remastered).
- Claim IDs: `CSL-001`–`CSL-009`.

## Mechanical decomposition

### Action Genes

- `ACT-006` changes simulation rate; `ACT-023` edits an ordered public-transport
  line; `ACT-068` edits the persistent road graph; `ACT-116` zones private
  land; `ACT-117` places utilities and civic facilities; `ACT-118` changes tax
  rates or service funding; `ACT-132` paints a district and assigns a local
  policy or industrial specialisation.
- Candidate genes: none.
- Parameters: road geometry, zone class and density, transport mode and stops,
  facility capacity, policy catalogue, district boundary, tax and budget rate.
- Claim IDs: `CSL-001`–`CSL-006`.

### System Behaviour Genes

- `SYS-031` transports passengers along configured lines; `SYS-151` develops
  and upgrades zoned lots; `SYS-152` recomputes sector demand; `SYS-153`
  propagates utility and civic-service capacity; `SYS-154` settles recurring
  municipal accounts; `SYS-155` generates urban trips and congestion;
  `SYS-169` unlocks capabilities when population milestones are reached.
- Resolution order: commit a spatial, fiscal or policy edit; update coverage,
  route and local-rule state; advance simulation time; move citizens, service
  vehicles and goods; recompute demand, land value and eligibility; develop,
  upgrade or abandon lots; settle income and expenditure; persist any crossed
  milestone unlocks.
- Parameters: demand sectors, trip modes, vehicle capacity, service radius,
  budget period, population thresholds and unlocked catalogue.
- Claim IDs: `CSL-001`–`CSL-007`.

### Constraint Genes

- `CON-048` keeps each named transport line an ordered unbranched sequence;
  `CON-050` bounds passenger pickup by vehicle capacity; `CON-170` requires
  access and enabling services for zoned development; `CON-171` requires
  treasury and recurring solvency; `CON-179` withholds milestone-gated tools
  and map-area purchases until their population threshold is reached.
- Scarce strategic resources: buildable land, road and vehicle throughput,
  service capacity, treasury, recurring revenue and tolerable pollution.
- Claim IDs: `CSL-001`–`CSL-006`.

### Information Genes

- `INF-057` exposes RCI demand, building details and selectable spatial
  diagnostic views; `INF-058` exposes an itemised municipal ledger, tax rates
  and service budgets.
- Candidate genes: none.
- Claim IDs: `CSL-007`.

### Objective Genes

- `OBJ-053` evaluates an open-ended city by sustained population, economy,
  services and player-defined growth rather than one authored terminal layout.
- Success, evaluation and failure: population milestones provide intermediate
  progress; debt, abandonment, congestion and service collapse remain
  diagnosable simulation states rather than one fixed loss screen.
- Claim IDs: `CSL-001`–`CSL-007`.

### Time Genes

- `TIM-003` advances citizens, traffic, services, development and finances on a
  live schedule while accepting edits; pause and faster rates are available.
- Candidate genes: none.
- Claim IDs: `CSL-001`–`CSL-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Powered, watered roadside cells are unzoned and residential demand is positive | Paint low-density residential zoning and advance time | Eligible private homes appear autonomously; the player did not select their individual models | zoning authorises rather than directly places private development | `CSL-001` |
| A bus depot exists but no service line connects two districts | Draw a closed ordered sequence of bus stops | Buses repeatedly traverse that line and board only up to vehicle capacity | authored service topology and automatic passenger transport are separate | `CSL-003` |
| A growing district has poor health or fire coverage | Place and fund the relevant service near the road network | Coverage and dispatched-vehicle availability update; nearby viability and land value can improve | placement and recurring funding jointly shape service effect | `CSL-002`, `CSL-004` |
| A bounded industrial area has no specialisation | Paint a district and apply forestry where trees are available | Subsequent eligible industrial development in that boundary follows the specialisation and its trade-offs | policies can alter only a selected spatial region | `CSL-005` |
| Population remains below the next milestone | Attempt to select its service or purchase another gated area | The unavailable option remains locked; crossing the threshold persistently enables it | progression changes the action catalogue through population | `CSL-006` |
| Expenses exceed current tax income | Reduce service budget, adjust tax or accept a loan, then advance time | Capacity, happiness or debt service changes and the recurring balance updates | fiscal repair changes both services and growth conditions | `CSL-004` |

## Strategic and experiential structure

- Local decision: identify whether one warning originates in access, capacity,
  coverage, affordability or an incompatible local policy.
- Medium-term planning: balance zoning, transport, utilities and civic services
  without letting the recurring budget or road network collapse.
- Long-term structure: shape an open city whose individually simulated trips,
  private development, district rules and unlock sequence react indirectly to
  planning decisions.
- Common heuristics: zone in measured increments, inspect overlays before
  expanding, separate pollution from housing, give traffic multiple paths and
  add service capacity only where demand justifies its upkeep.
- Failure attribution: itemised accounts and overlays expose symptoms and
  spatial bottlenecks, while internal demand and route-choice details remain a
  model the player must infer.
- Player-trust factors: delayed consequences remain revisable, but useful
  attribution depends on readable overlays and stable policy effects.
- Claim IDs: `CSL-001`–`CSL-007`.

## Replay and variation

- What changes between sessions: map, starting connection, district layout,
  zoning, networks, policies, service placement and endogenous population.
- Randomness or procedural generation: supplied maps and autonomous building
  choices vary presentation; the principal variation comes from coupled
  simulation response to the player's city design.
- Multiple viable strategies: yes; road hierarchy, transit emphasis, density,
  service levels, specialisation and fiscal policy admit many stable forms.
- Typical replay motive: different urban forms, transport experiments,
  self-imposed constraints and map-specific growth.
- Claim IDs: `CSL-001`–`CSL-008`.

## Adjacent systems and history

- Direct predecessors: SimCity established zoning-mediated city simulation;
  Colossal Order's Cities in Motion established detailed transport simulation.
- Variants: DLC extends transport, industry, campuses, parks, airports,
  weather and other systems; those mechanics are outside this record.
- Similar games: SimCity 4 Deluxe Edition, Mini Metro and Mini Motorways.
- Important differences: unlike SimCity 4 at this Atlas boundary, Cities:
  Skylines adds explicitly drawn ordered transport lines, capacity-bounded
  passenger service, spatial districts with local policies and
  population-gated land/tool progression. Unlike Mini Metro, private zoning,
  services and a municipal budget drive the city rather than station queues
  alone.
- Claim IDs: `CSL-003`, `CSL-005`, `CSL-006`, `CSL-008`, `CSL-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-023`, `ACT-068`, `ACT-116`, `ACT-117`, `ACT-118`, `ACT-132` | road, line, zoning, facility, fiscal and district parameters |
| System Behaviour | `SYS-031`, `SYS-151`, `SYS-152`, `SYS-153`, `SYS-154`, `SYS-155`, `SYS-169` | demand, travel, coverage, finance and milestone parameters |
| Constraint | `CON-048`, `CON-050`, `CON-170`, `CON-171`, `CON-179` | line, vehicle, service, treasury and unlock thresholds |
| Information | `INF-057`, `INF-058` | overlay and ledger detail |
| Objective | `OBJ-053` | player-defined growth horizon |
| Time | `TIM-003` | pausable multi-rate simulation |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-006,ACT-023,ACT-068,ACT-116,ACT-117,ACT-118,ACT-132; SYS-031,SYS-151,SYS-152,SYS-153,SYS-154,SYS-155,SYS-169; CON-048,CON-050,CON-170,CON-171,CON-179; INF-057,INF-058; OBJ-053; TIM-003`.
- Indexed games scanned: 121, including this record.
- Indexed combinations scanned: 119.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0118` — SimCity 4 Deluxe Edition
  at `16 / 23 = 0.695652`.
- Supported combination subsets: `COMB-0117`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `0 / 37 = 0.000000`; `GAME-0002`: `0 / 30 = 0.000000`; `GAME-0003`: `0 / 32 = 0.000000`; `GAME-0004`: `2 / 36 = 0.055556`.
- `GAME-0005`: `0 / 30 = 0.000000`; `GAME-0006`: `0 / 32 = 0.000000`; `GAME-0007`: `0 / 31 = 0.000000`; `GAME-0008`: `0 / 30 = 0.000000`.
- `GAME-0009`: `0 / 39 = 0.000000`; `GAME-0010`: `0 / 32 = 0.000000`; `GAME-0011`: `0 / 36 = 0.000000`; `GAME-0012`: `0 / 32 = 0.000000`.
- `GAME-0013`: `0 / 36 = 0.000000`; `GAME-0014`: `0 / 38 = 0.000000`; `GAME-0015`: `0 / 37 = 0.000000`; `GAME-0016`: `2 / 36 = 0.055556`.
- `GAME-0017`: `0 / 36 = 0.000000`; `GAME-0018`: `6 / 36 = 0.166667`; `GAME-0019`: `0 / 33 = 0.000000`; `GAME-0020`: `0 / 37 = 0.000000`.
- `GAME-0021`: `1 / 31 = 0.032258`; `GAME-0022`: `0 / 35 = 0.000000`; `GAME-0023`: `0 / 33 = 0.000000`; `GAME-0024`: `1 / 34 = 0.029412`.
- `GAME-0025`: `1 / 33 = 0.030303`; `GAME-0026`: `1 / 34 = 0.029412`; `GAME-0027`: `1 / 34 = 0.029412`; `GAME-0028`: `1 / 39 = 0.025641`.
- `GAME-0029`: `2 / 33 = 0.060606`; `GAME-0030`: `2 / 35 = 0.057143`; `GAME-0031`: `0 / 34 = 0.000000`; `GAME-0032`: `0 / 34 = 0.000000`.
- `GAME-0033`: `1 / 35 = 0.028571`; `GAME-0034`: `1 / 36 = 0.027778`; `GAME-0035`: `1 / 40 = 0.025000`; `GAME-0036`: `0 / 35 = 0.000000`.
- `GAME-0037`: `2 / 30 = 0.066667`; `GAME-0038`: `1 / 38 = 0.026316`; `GAME-0039`: `0 / 32 = 0.000000`; `GAME-0040`: `0 / 31 = 0.000000`.
- `GAME-0041`: `1 / 33 = 0.030303`; `GAME-0042`: `0 / 32 = 0.000000`; `GAME-0043`: `0 / 37 = 0.000000`; `GAME-0044`: `0 / 33 = 0.000000`.
- `GAME-0045`: `0 / 37 = 0.000000`; `GAME-0046`: `0 / 33 = 0.000000`; `GAME-0047`: `0 / 37 = 0.000000`; `GAME-0048`: `0 / 37 = 0.000000`.
- `GAME-0049`: `0 / 32 = 0.000000`; `GAME-0050`: `0 / 38 = 0.000000`; `GAME-0051`: `3 / 36 = 0.083333`; `GAME-0052`: `1 / 32 = 0.031250`.
- `GAME-0053`: `0 / 32 = 0.000000`; `GAME-0054`: `0 / 34 = 0.000000`; `GAME-0055`: `0 / 33 = 0.000000`; `GAME-0056`: `0 / 31 = 0.000000`.
- `GAME-0057`: `0 / 31 = 0.000000`; `GAME-0058`: `0 / 32 = 0.000000`; `GAME-0059`: `0 / 30 = 0.000000`; `GAME-0060`: `0 / 30 = 0.000000`.
- `GAME-0061`: `0 / 33 = 0.000000`; `GAME-0062`: `0 / 31 = 0.000000`; `GAME-0063`: `0 / 30 = 0.000000`; `GAME-0064`: `0 / 28 = 0.000000`.
- `GAME-0065`: `0 / 30 = 0.000000`; `GAME-0066`: `0 / 33 = 0.000000`; `GAME-0067`: `0 / 31 = 0.000000`; `GAME-0068`: `0 / 31 = 0.000000`.
- `GAME-0069`: `0 / 31 = 0.000000`; `GAME-0070`: `0 / 31 = 0.000000`; `GAME-0071`: `0 / 30 = 0.000000`; `GAME-0072`: `0 / 31 = 0.000000`.
- `GAME-0073`: `0 / 30 = 0.000000`; `GAME-0074`: `0 / 32 = 0.000000`; `GAME-0075`: `0 / 32 = 0.000000`; `GAME-0076`: `0 / 30 = 0.000000`.
- `GAME-0077`: `0 / 30 = 0.000000`; `GAME-0078`: `0 / 30 = 0.000000`; `GAME-0079`: `0 / 30 = 0.000000`; `GAME-0080`: `0 / 30 = 0.000000`.
- `GAME-0081`: `0 / 31 = 0.000000`; `GAME-0082`: `0 / 31 = 0.000000`; `GAME-0083`: `0 / 31 = 0.000000`; `GAME-0084`: `0 / 33 = 0.000000`.
- `GAME-0085`: `0 / 34 = 0.000000`; `GAME-0086`: `0 / 36 = 0.000000`; `GAME-0087`: `1 / 32 = 0.031250`; `GAME-0088`: `0 / 32 = 0.000000`.
- `GAME-0089`: `0 / 32 = 0.000000`; `GAME-0090`: `0 / 38 = 0.000000`; `GAME-0091`: `1 / 31 = 0.032258`; `GAME-0092`: `2 / 31 = 0.064516`.
- `GAME-0093`: `0 / 32 = 0.000000`; `GAME-0094`: `1 / 32 = 0.031250`; `GAME-0095`: `1 / 34 = 0.029412`; `GAME-0096`: `1 / 32 = 0.031250`.
- `GAME-0097`: `1 / 30 = 0.033333`; `GAME-0098`: `1 / 29 = 0.034483`; `GAME-0099`: `0 / 31 = 0.000000`; `GAME-0100`: `1 / 33 = 0.030303`.
- `GAME-0101`: `0 / 33 = 0.000000`; `GAME-0102`: `0 / 30 = 0.000000`; `GAME-0103`: `0 / 32 = 0.000000`; `GAME-0104`: `0 / 32 = 0.000000`.
- `GAME-0105`: `1 / 32 = 0.031250`; `GAME-0106`: `0 / 30 = 0.000000`; `GAME-0107`: `0 / 31 = 0.000000`; `GAME-0108`: `0 / 33 = 0.000000`.
- `GAME-0109`: `0 / 39 = 0.000000`; `GAME-0110`: `1 / 30 = 0.033333`; `GAME-0111`: `0 / 30 = 0.000000`; `GAME-0112`: `1 / 30 = 0.033333`.
- `GAME-0113`: `1 / 36 = 0.027778`; `GAME-0114`: `1 / 29 = 0.034483`; `GAME-0115`: `0 / 29 = 0.000000`; `GAME-0116`: `1 / 28 = 0.035714`.
- `GAME-0117`: `0 / 31 = 0.000000`; `GAME-0118`: `16 / 23 = 0.695652`; `GAME-0119`: `1 / 45 = 0.022222`; `GAME-0120`: `0 / 52 = 0.000000`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0118` — SimCity 4 Deluxe Edition | `ACT-006`, `ACT-068`, `ACT-116`, `ACT-117`, `ACT-118`, `SYS-151`, `SYS-152`, `SYS-153`, `SYS-154`, `SYS-155`, `CON-170`, `CON-171`, `INF-057`, `INF-058`, `OBJ-053`, `TIM-003` | Cities: Skylines additionally represents ordered public-transport lines and bounded vehicles, spatially local district policy and population-milestone gating | unique near match at `69.57%` |

- New genes: `ACT-132`, `SYS-169`, `CON-179`.
- Classification result: recurring known combination with three new bounded genes.
- Evidence and reasoning: the complete `COMB-0117` zoned-city structure recurs
  independently in another city simulator. Cities: Skylines remains a distinct
  signature because districts, milestone progression and explicit
  capacity-bounded ordered transport lines add seven admitted genes.

## Taxonomy impact

- Registry changes: three Active genes; twenty existing genes gain a second or
  additional analysed carrier.
- Taxonomy-change record: none.
- Candidate terms affected: district-local policy; population-milestone
  catalogue unlock; milestone-gated map-area acquisition.

## Negative results

- `ACT-024` was not reused: the scoped base-game evidence supports drawing
  transport lines and adjusting service funding, not assigning a finite owned
  vehicle inventory between lines as Mini Metro does.
- `INF-001` was not reused: diagnostic views reveal selected projections and
  queried details, not the complete internal demand and route-choice state.
- DLC production chains, weather, campus, park, airport and financial systems
  were not admitted through base-game resemblance.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Cities: Skylines reproduces the complete
  zoned-development, municipal-service and recurring-budget interaction from
  `COMB-0117` while adding district and milestone structure (`CSL-001`–`CSL-009`).

## Нові гени

- [Observation | Corroborated | High] `ACT-132`, `SYS-169`, `CON-179`.

## Нові комбінації

- [Pattern | Corroborated | High] Нових ID немає; `COMB-0117` becomes a
  recurring two-game combination supported by SimCity 4 and Cities: Skylines.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does Against the Storm retain zoning-mediated settlement growth, or does its
  directly placed production chain require a separate settlement boundary?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] shapez 2.
- Optimisation criterion: test Factorio's production-and-logistics recurrence
  without combat, pollution or a character-bound manual bootstrap.
- Expected information gain: distinguish generic continuous factory flow from
  the specific resource, power and research constraints of Factorio.
- Backlog impact: continues the approved editorial batch as `GAME-0122`.

## Чому саме вона

- [Hypothesis | Corroborated | High] shapez 2 should create the batch's second
  strong familiar relationship while testing whether a highly abstract factory
  preserves the same causal production genome.
