---
game_id: GAME-0124
slug: against-the-storm
game_title: Against the Storm
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0122
gene_ids:
  action:
    - ACT-006
    - ACT-036
    - ACT-120
    - ACT-130
    - ACT-139
    - ACT-140
    - ACT-141
    - ACT-142
    - ACT-143
  system:
    - SYS-004
    - SYS-045
    - SYS-046
    - SYS-156
    - SYS-157
    - SYS-161
    - SYS-166
    - SYS-175
    - SYS-176
    - SYS-177
    - SYS-178
    - SYS-179
    - SYS-180
    - SYS-181
    - SYS-182
    - SYS-183
    - SYS-184
  constraint:
    - CON-062
    - CON-172
    - CON-184
    - CON-185
    - CON-186
    - CON-187
    - CON-188
    - CON-189
    - CON-190
    - CON-191
  information:
    - INF-001
    - INF-002
    - INF-003
    - INF-059
    - INF-064
    - INF-065
    - INF-066
    - INF-067
    - INF-068
  objective:
    - OBJ-059
  time:
    - TIM-003
---

# Game: Against the Storm

## Analysis scope

- Version / ruleset: PC base game `1.10.4`, ordinary settlement play plus the
  world-map and Smoldering City metaprogression that connect settlements.
- Included: base species; embarkation; concealed glades; building, recipes and
  staffed production; Drizzle, Clearance and Storm; Hostility, Resolve,
  Reputation and Queen's Impatience; Orders, blueprints, cornerstones, traders,
  Glade Events; settlement rewards and Citadel upgrades.
- Excluded: DLC species and biomes; Ancient Seal finale and Sealed Forest;
  Queen's Hand Trial, Daily and Training Expeditions; multiplayer, mods,
  achievements and prestige modifiers as separate genes.
- Direct-play status: not conducted. Official developer and publisher
  documentation jointly specify the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ATS-001` | A seeded settlement conceals resources and events inside glades | Confirmed | Corroborated | High | P1, P9 |
| `ATS-002` | Buildings require compatible sites, materials, blueprints and staffed jobs | Confirmed | Corroborated | High | P4, P10 |
| `ATS-003` | Settlement time repeats Drizzle, Clearance and Storm while production remains live | Confirmed | Direct | High | P7, P8 |
| `ATS-004` | Expansion and woodcutting raise Hostility tiers that intensify Storm effects | Confirmed | Direct | High | P3, P7 |
| `ATS-005` | Species Resolve can cause departures or generate Reputation | Confirmed | Direct | High | P5 |
| `ATS-006` | Reputation and Queen's Impatience form opposed visible settlement thresholds | Confirmed | Corroborated | High | P2, P6 |
| `ATS-007` | Milestones present bounded persistent blueprint, Order and cornerstone choices | Confirmed | Corroborated | High | P2, P4, P6 |
| `ATS-008` | Staffed Glade Events consume goods and time before a disclosed threat deadline | Confirmed | Direct | High | P8 |
| `ATS-009` | Completed settlements grant persistent resources and extend reach for the current cycle | Confirmed | Corroborated | High | P11, P13 |
| `ATS-010` | Citadel upgrades spend persistent resources behind predecessor requirements | Confirmed | Direct | High | P12 |

## Basic data

- Release / origin: Eremite Games, published by Hooded Horse; full release in
  2023, scoped to current base version `1.10.4` from 9 July 2026.
- Platform or physical form: real-time desktop settlement roguelite.
- Puzzle family: real-time system pressure; agent routing and coordination;
  ordered dependency sequencing; automation and spatial programming.
- Primary sources: **[P1]** [official Steam page](https://store.steampowered.com/app/1336490/Against_the_Storm/);
  **[P2]** [official wiki: Orders](https://wiki.hoodedhorse.com/Against_the_Storm/Orders);
  **[P3]** [official wiki: Hostility](https://wiki.hoodedhorse.com/Against_the_Storm/Hostility);
  **[P4]** [official wiki: Buildings](https://wiki.hoodedhorse.com/Against_the_Storm/Buildings);
  **[P5]** [official wiki: Resolve](https://wiki.hoodedhorse.com/Against_the_Storm/Resolve);
  **[P6]** [official tutorial](https://wiki.hoodedhorse.com/Against_the_Storm/Tutorial_Walkthrough);
  **[P7]** [official wiki: Seasons](https://wiki.hoodedhorse.com/Against_the_Storm/Seasons);
  **[P8]** [official wiki: Glade Events](https://wiki.hoodedhorse.com/Against_the_Storm/Glade_Events);
  **[P9]** [official wiki: Glades](https://wiki.hoodedhorse.com/Against_the_Storm/Glades);
  **[P10]** [official wiki: Recipes](https://wiki.hoodedhorse.com/Against_the_Storm/Recipes);
  **[P11]** [official wiki: World Map](https://wiki.hoodedhorse.com/Against_the_Storm/World_Map);
  **[P12]** [official wiki: Upgrades](https://wiki.hoodedhorse.com/Against_the_Storm/Upgrades);
  **[P13]** [official wiki: Settlements](https://wiki.hoodedhorse.com/Against_the_Storm/Settlements);
  **[P14]** [official 1.10 update](https://eremitegames.com/overhaulers-update-1-10/);
  **[P15]** [official 1.10.4 hotfix](https://store.steampowered.com/news/app/1336490/view/677376450273221364).
- Claim IDs: `ATS-001`–`ATS-010`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-006` changes live speed; `ACT-036` assigns workers;
  `ACT-120` configures recipes and priorities; `ACT-130` buys trader offers.
- New: `ACT-139` builds settlement structures; `ACT-140` commits one bounded
  offer; `ACT-141` favours one species; `ACT-142` chooses embarkation;
  `ACT-143` buys Citadel upgrades.
- Parameters: site, building, recipe, worker species, offer pool, rerolls,
  destination, embark budget and upgrade cost.
- Claim IDs: `ATS-002`, `ATS-007`–`ATS-010`.

### System Behaviour Genes

- Reused: `SYS-004`, `SYS-045`, `SYS-046`, `SYS-156`, `SYS-157`, `SYS-161`,
  `SYS-166`, `SYS-175` cover random selection, worker execution, recipes,
  logistics, finite extraction, triggered modifiers and run reset.
- New: `SYS-176`–`SYS-184` cover concealed seeded glades, season cycling,
  Hostility, species Resolve, Reputation, Impatience, milestone offers, timed
  Glade Events and settlement-to-world-map rewards.
- Resolution order: accept edits; advance live time; perform extraction,
  transport and recipes; update season and Hostility; update needs and Resolve;
  accrue Reputation or departures; advance events and Impatience; test the two
  settlement thresholds.
- Claim IDs: `ATS-001`–`ATS-009`.

### Constraint Genes

- Reused: `CON-062` footprint compatibility and `CON-172` recipe-flow
  compatibility.
- New: `CON-184`–`CON-191` bind blueprints and materials, population, the
  Impatience limit, event deadlines and inputs, exclusive offers, embarkation
  range and Citadel prerequisites.
- Scarce strategic resources: workers, time, Resolve, fuel, food, building
  materials, glade safety, blueprint access and embarkation / Citadel currency.
- Claim IDs: `ATS-002`, `ATS-006`–`ATS-010`.

### Information Genes

- `INF-001` exposes the explored settlement; `INF-002` and `INF-003` distinguish
  future offers and currently concealed glades; `INF-059` exposes recipe
  dependencies; `INF-064`–`INF-068` expose pressure, population, progress,
  task and world-map state.
- Claim IDs: `ATS-001`–`ATS-010`.

### Objective Genes

- `OBJ-059` fills Reputation before Queen's Impatience reaches its maximum.
- Success, evaluation and failure: victory awards meta resources and a world-map
  foothold; maximum Impatience or abandonment loses the settlement while
  authored metaprogression persists.
- Claim IDs: `ATS-006`, `ATS-009`.

### Time Genes

- `TIM-003`: seasons, production, events, Hostility effects and Impatience
  continue in real time, with pause and speed controls.
- Claim IDs: `ATS-003`–`ATS-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A production building has workers and a recipe but lacks one input | Supply the missing compatible good | logistics deliver it and the staffed recipe repeatedly produces | staffing, recipe and flow are coupled | `ATS-002` |
| Storm approaches while woodcutters and opened glades raise Hostility | Let the season advance | the Storm phase activates every mystery whose Hostility threshold is met | expansion becomes forecast pressure | `ATS-003`, `ATS-004` |
| One species remains above its blue Resolve threshold | Sustain its needs | the group continuously adds Reputation, while falling below stops the gain | welfare is a success engine, not only a satisfaction score | `ATS-005` |
| A dangerous Glade Event is active but unsupplied | Advance time past its deadline | the disclosed threat resolves instead of the selected reward path | event requirements and timers are causal | `ATS-008` |
| Reputation increases before victory | Complete an Order or sustain high Resolve | the success bar rises and Queen's Impatience is reduced | the two terminal tracks are coupled | `ATS-006` |
| A settlement reaches the Reputation target first | Complete the final source of Reputation | the settlement ends in victory, grants persistent resources and becomes a cycle foothold | bounded run success changes metaworld reach | `ATS-009` |

## Strategic and experiential structure

- Local decision: move workers, select recipes, supply needs and choose whether
  a glade or event is safe to open now.
- Medium-term planning: build one production web that satisfies Orders and
  species needs without pushing Hostility beyond the coming Storm capacity.
- Long-term structure: use successive settlement rewards and Citadel upgrades
  to extend world-map reach across Blightstorm cycles.
- Common heuristics: inspect the next Storm before expanding; avoid idle
  specialists; treat offered blueprints as path commitments; preserve event
  goods and fuel buffers.
- Failure attribution: visible Resolve, Hostility, event timers and paired
  progress tracks usually expose why a crisis happened, though offer variance
  makes recovery paths uneven.
- Player-trust factors: declared thresholds and needs make most consequences
  inspectable before commitment.
- Claim IDs: `ATS-002`–`ATS-010`.

## Replay and variation

- What changes between sessions: biome, map seed, glades, species mix, Orders,
  blueprint and cornerstone offers, traders and modifiers.
- Randomness or procedural generation: seeded geography and bounded offers vary;
  resource, recipe and pressure rules remain inspectable.
- Multiple viable strategies: yes; Resolve, Orders and events can contribute
  different shares of Reputation through different production chains.
- Typical replay motive: adapt to a new mechanical economy while extending
  metaworld reach and upgrades.
- Claim IDs: `ATS-001`–`ATS-010`.

## Adjacent systems and history

- Direct predecessors: city builders, production-chain simulations and run-based
  metaprogression.
- Variants: DLC, Sealed Forest and Queen's Hand Trial are out of scope.
- Similar games: Frostpunk, Banished, Anno, Factorio and Slay the Spire.
- Important differences: Against the Storm compresses settlement planning into
  bounded runs with forecast seasonal pressure, opposed win/loss tracks and
  random persistent offers.
- Claim IDs: `ATS-001`–`ATS-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-036`, `ACT-120`, `ACT-130`, `ACT-139`–`ACT-143` | assignment, offer and embark parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-046`, `SYS-156`, `SYS-157`, `SYS-161`, `SYS-166`, `SYS-175`–`SYS-184` | rates, thresholds, pools and rewards |
| Constraint | `CON-062`, `CON-172`, `CON-184`–`CON-191` | costs, slots, timers and range |
| Information | `INF-001`–`INF-003`, `INF-059`, `INF-064`–`INF-068` | forecast granularity |
| Objective | `OBJ-059` | paired thresholds |
| Time | `TIM-003` | live phase progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `123` (`GAME-0001`–`GAME-0123`).
- Exact genome matches: none.
- Tied near matches: `GAME-0119` — Factorio (`10 / 60 = 0.166667`).
- Supported combination subsets: `COMB-0122`.
- Scan date: 2026-08-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0119` Factorio | `ACT-120`, `SYS-045`, `SYS-156`, `SYS-157`, `SYS-161`, `CON-062`, `CON-172`, `INF-001`, `INF-059`, `TIM-003` | Factorio builds a continuous unstaffed factory toward a rocket and turns pollution into attacks; Against the Storm assigns finite workers inside bounded settlements and couples seasonal Hostility, species Resolve, offers and two terminal tracks | Near, `0.166667` |

### Preserved research notes

- New genes: `ACT-139`–`ACT-143`, `SYS-176`–`SYS-184`, `CON-184`–`CON-191`, `INF-064`–`INF-068`, `OBJ-059`.
- Classification result: `New gene` and `New combination of known genes`.
- Evidence and reasoning: new boundaries require the forecast seasonal pressure,
  population-welfare conversion, paired settlement tracks and timed staffed
  events to survive comparison beyond one title.

## Taxonomy impact

- Registry changes: 28 new Active genes and 19 reused Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: bounded persistent offer; settlement hostility;
  species Resolve; staffed timed event; cycle foothold.

## Negative results

- `SYS-160` was not reused: Hostility is an explicit tiered pressure score and
  does not diffuse spatially or spawn attack groups like Factorio pollution.
- `OBJ-053` was not reused: one settlement has authored success and failure
  thresholds even though the metagame supports repeated play.
- Separate blueprint, cornerstone, Order and event-choice genes were rejected:
  they share one normalized bounded persistent-offer rule.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Against the Storm makes settlement growth a
  bounded run against forecast seasonal, welfare and impatience pressure
  (`ATS-001`–`ATS-010`).

## Нові гени

- [Observation | Corroborated | High] 28 genes record the new offer, seasonal,
  welfare, event and metaworld boundaries without encoding UI nouns as genes.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0122` records staffed settlement
  management under escalating Storm pressure.

## Зміни таксономії

- [Observation | Corroborated | High] No new family is needed; the genome joins
  four existing causal families.

## Нові питання

- Does Frostpunk reuse the welfare-to-progress relation, or only the settlement
  pressure and staffed production layers?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Oxygen Not Included.
- Optimisation criterion: compare autonomous staffed production under visible
  environmental pressure without Against the Storm's bounded offers.
- Expected information gain: tests whether pressure, population and logistics
  genes recur outside a roguelite settlement structure.
- Backlog impact: approved game eight of the current nine-game batch.

## Чому саме вона

- [Hypothesis | Limited | High] It should reuse agent assignment and live
  production while replacing season / impatience pressure with simulated gas,
  heat and biological constraints.
