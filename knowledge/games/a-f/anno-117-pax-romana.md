---
game_id: GAME-0525
slug: anno-117-pax-romana
game_title: "Anno 117: Pax Romana"
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-068
    - ACT-139
    - ACT-172
  system:
    - SYS-153
    - SYS-154
    - SYS-156
    - SYS-157
    - SYS-245
    - SYS-1505
    - SYS-1506
  constraint:
    - CON-062
    - CON-172
    - CON-173
    - CON-184
    - CON-805
    - CON-806
    - CON-807
  information:
    - INF-060
    - INF-086
    - INF-087
    - INF-509
  objective:
    - OBJ-296
  time:
    - TIM-003
---

# Game: Anno 117: Pax Romana

## Analysis scope

- Version / ruleset: English Windows PC base game under the 13 November 2025
  launch rules. Ubisoft Mainz identifies 1.2 as the included launch patch.
  Standard single-player Endless in Latium, default simulation speed,
  a settled starting island with a Trading Post, and no other island needed.
- Structured analysis target: `PLAT-WINDOWS-PC`, one Latium starter settlement
  through its first Liberti-to-Plebeian residence upgrade.
- Primary decision loop: connect buildings to the trading post, maintain
  workable routes to storage, and balance construction materials, available
  labour and running costs. Route hemp to a spinner and watch the residence
  supply groups. Provide sardines, road-reached market service and tunics.
  Select one eligible home, spend the required construction material, then
  inspect the changed workforce before adding another higher-tier home.
- Entry: fresh Endless start, already founded, before placing the first
  woodcutter. Use a starter island with usable forest, coast and hemp
  production sites. The seed and exact grid positions are parameters.
  Keep additional imported goods, paid specialists and research inactive.
- Exit: one residence converts to Plebeians after the category thresholds
  and material requirement are met. Observe its workforce class change and
  retain other Liberti residences. Stop before starting a Plebeian supply
  chain. A blocked upgrade is a recoverable state, so repair the roads,
  supply or material shortage and eventually reach the declared exit.
- Included: the woodcutter-to-sawmill construction chain and the
  hemp-to-tunic chain, coastal sardines, market coverage, roads, warehouse
  access, Liberti housing and labour, upkeep, attribute returns and the
  first conversion.
- Excluded: campaign-specific quests and grants, later tiers, Aegyptus or Albion
  alternate branches, DLC, inter-island trade, upgrades to road pavement,
  war, religion, research, specialists and exact consumptions or hauling
  capacities. Optional food, service and fashion choices appear as
  counterexamples to mandatory named needs.
- Direct-play status: no native execution or media playback. Ubisoft's launch
  announcement identifies 1.2. Official rules and written launch-era play
  accounts support the route. No exact Windows executable hash, map seed,
  individual fulfilment thresholds below the stated first-tier rule or
  later-version parity were measured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| `A117-001` | Windows was available at launch and 1.2 was the launch patch. The starting-island route exists in single-player Endless Latium. | Confirmed | Direct | High | P1, P2, P3 |
| `A117-002` | Place a woodcutter within usable forest and a road-connected sawmill. Logs become timber for construction. Eligible forest density affects the first stage's productivity. | Observation | Corroborated | High | P2, P3, S1 |
| `A117-003` | Production depends on labour and road access to nearby storage. The trading post can fulfil the warehouse role. Road links to the post also enable residence supply. | Observation | Corroborated | High | P2, P3, P5, S1 |
| `A117-004` | A coastal Fishing Hut supplies sardines. A Market serves connected homes within road reach. The Hemp Farm supplies a Spinner for tunics. These complete Food, Public Service and Fashion respectively. | Observation | Corroborated | High | P2, P3, P4, S1 |
| `A117-005` | The Liberti upgrade gate needs one supply point in each category. Sardines and porridge substitute within Food and can both contribute their attributes. Extra supply in one group cannot fill another group's deficit. | Confirmed | Direct | High | P2, P4 |
| `A117-006` | Individual needs have their own residence attribute bonuses. Partial consumption supply can grant a partial bonus. Meeting additional optional needs can increase attributes beyond the upgrade minimum. | Confirmed | Direct | High | P2, P4 |
| `A117-007` | A working spinner can also add nearby income through an area effect, separate from the tunic need. Construction debits upfront stocks and upkeep is recurring. | Observation | Corroborated | High | P2, P3, S1 |
| `A117-008` | The player explicitly commits the upgrade with construction material available. The residence changes from supplying Liberti labour to supplying Plebeian labour; lower-tier inputs still depend on staffing the original buildings. | Observation | Corroborated | High | P2, P3, S1, S2 |
| `A117-009` | The building grid accepts eligible edge contacts and a 45-degree diagonal road contact with a corner. Merely passing an orthogonal corner does not form a connection. | Observation | Direct | High | P5 |
| `A117-010` | Needs, population, available labour, stock trend and throughput are inspectable. A passing category bar and its individual active attribute bonuses answer different questions. | Observation | Corroborated | High | P2, P4, S1 |

## Basic data

- Release / origin: Ubisoft Mainz, published by Ubisoft, November 2025.
- Platform or physical form: base Windows PC digital release, English.
- Puzzle families: route and network construction (`FAM-005`), automation
  and spatial programming (`FAM-008`) and ordered dependency sequencing
  (`FAM-017`).
- Primary sources:
  - P1. [Ubisoft Mainz's launch and patch announcement](https://www.anno-union.com/anno-117-pax-romana-its-launch-day/)
    and [Ubisoft PC platform specification](https://news.ubisoft.com/en-au/article/52rVna7ggbsmPejs9MXwHj/anno-117-pax-romana-pc-specs-revealed).
  - P2. [Ubisoft Mainz's getting-started guide](https://www.anno-union.com/getting-started-in-anno-117-pax-romana/),
    Endless and Latium setup, starting transport, needs, production and upgrade.
  - P3. [Ubisoft's release-day starter guide](https://news.ubisoft.com/de-de/article/4fvALjiPTxYODChSgRb1Mk/anno-117-pax-romana--5-tips-for-getting-started),
    trading post, starting residence services, construction materials and tiers.
  - P4. [Ubisoft Mainz game-design account of need groups](https://www.anno-union.com/devblog-fulfil-needs-your-way/),
    category supply points, attributes and partial fulfilment.
  - P5. [Ubisoft Mainz grid and frontage rules](https://www.anno-union.com/devblog-roads-building-in-the-grid/),
    diagonal corner eligibility and connection indicators.
- Secondary sources:
  - S1. [Into Indie Games launch-week beginner route](https://intoindiegames.com/walkthroughs/anno-117-pax-romana-beginners-guide/),
    corroborating the staffing, housing and operating order. Official need
    attributes take precedence where the guide's individual numbers differ.
  - S2. [PC Gamer's Windows release review](https://www.pcgamer.com/games/city-builder/anno-117-pax-romana-review/),
    first-hand observation of upgrading houses and losing lower-tier labour.
- Claim IDs: `A117-001`–`A117-010`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-068` edit persistent roads; `ACT-139` place
  houses, production, service and storage buildings; `ACT-172` commit the
  available residence-tier upgrade.
- Claim IDs: `A117-002`–`A117-005`, `A117-008`, `A117-009`.

### System Behaviour Genes

- Existing gene IDs: `SYS-153` expose the effect of market coverage,
  `SYS-154` settle income and upkeep, `SYS-156` repeat supplied production,
  `SYS-157` move goods through operating logistics and `SYS-245` allocate
  the island's tier-specific labour to production.
- New gene IDs: `SYS-1505` aggregate individually fulfilled needs into
  residence attributes, including partial returns; `SYS-1506` apply a
  production building's separate local attribute effect.
- Resolution order: placement and road eligibility, resource and workforce
  supply, production and delivery, home consumption or covered service,
  separate category and attribute updates, paid tier conversion. The order
  describes dependencies, not per-frame execution.
- Claim IDs: `A117-002`–`A117-008`, `A117-010`.

### Constraint Genes

- Existing gene IDs: `CON-062`, `CON-172`, `CON-173`, `CON-184` for
  legal footprints and extracting sites, recipe input and output, and
  constructed buildings' costs and access.
- New gene IDs: `CON-805` independently meet each need category before
  paying to upgrade; `CON-806` accept qualifying 45-degree corner
  attachments; `CON-807` require road continuity to the port network
  and reachable storage for production.
- Scarce resources: stocked timber, land within working road reach, and
  enough Liberti labour to keep lower-tier production running.
- Claim IDs: `A117-002`–`A117-005`, `A117-007`–`A117-009`.

### Information Genes

- Existing gene IDs: `INF-060` exposes production and bottleneck state,
  `INF-086` residence and workforce diagnostics, and `INF-087` island
  stock through warehouse and post panels.
- New gene ID: `INF-509` displays the independent need-category supply
  tests and optional individual attribute effects.
- Claim IDs: `A117-003`–`A117-007`, `A117-010`.

### Objective Genes

- New gene ID: `OBJ-296`. Establish the first staffed settlement
  loop and pay to convert one residence after its supply-category gates.
  Verify its new labour class while the first-tier production base remains.
- A blocked conversion does not itself end a run. Continue diagnosing
  resources, category supply or transport until the target is reachable.
- Claim IDs: `A117-001`–`A117-008`, `A117-010`.

### Time Genes

- Existing gene ID: `TIM-003`. In the active simulation, recipes,
  deliveries, availability and upkeep continue while the player plans.
- Claim IDs: `A117-002`, `A117-003`, `A117-007`, `A117-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Trading post, starting stock and usable forest | Place and connect woodcutter and sawmill inside storage reach | Logs feed the sawmill and timber enters usable stock as production runs | A construction good can renew before expansion | `A117-002`, `A117-003` |
| Connected homes, no food | Build and staff a coastal Fishing Hut, wait for sardine supply | Food category gains its first choice and connected homes gain applicable population and income | Food supply generates workers as well as qualification | `A117-004`–`A117-006` |
| Home near a market geographically but outside its connected street reach | Repair the road link or move the service into working road reach | Its public-service need becomes eligible when coverage reaches it | A service and an inventory commodity have separate access rules | `A117-003`, `A117-004` |
| Existing food and service with no clothing | Connect a Hemp Farm and Spinner, staff them and supply the route to storage | The farm's hemp becomes tunics and can satisfy Fashion | Upstream stock alone cannot complete the downstream need | `A117-003`–`A117-005` |
| Sardines supplied and Fashion still empty | Add the second food option and inspect this residence | Food attributes can rise while the upgrade remains locked | Surplus points in one category cannot substitute for another | `A117-005`, `A117-006`, `A117-010` |
| All three needs categories pass and timber is available | Select and upgrade one Liberti residence | Construction stock is debited and that home becomes Plebeian | A manual tier change is distinct from ordinary occupancy growth | `A117-008` |
| The other homes remain Liberti | Inspect available workforce after the first conversion | Jobs can still be filled by remaining Liberti; the upgraded house now contributes to the other tier | The same population cannot be treated as one fungible labour pool | `A117-008`, `A117-010` |
| A candidate road passes a frontage only by its corner | Join it through eligible diagonal contact and inspect the connection mark | The eligible 45-degree contact works. A merely adjacent right-angle corner does not. | Road drawing changes the legal topology, not just its look | `A117-009` |

## Strategic and experiential structure

- Local decision: separate road reach from mere visual closeness and keep
  production transport short.
- Medium-term planning: meet category minima to advance cheaply, or supply
  alternatives for higher per-house returns. A nearby spinner offers a local
  zoning gain distinct from island-wide tunic supply.
- Long-term structure: an upgrade changes workforce composition and unlocks
  another tier's needs. Leave enough first-tier homes to sustain the original
  wood, food and textile chains.
- Failure attribution: inspect category bars, trip reach, material stock and
  worker balances separately. A full Food category is no evidence that
  Fashion or storage access is ready.
- Claim IDs: `A117-002`–`A117-010`.

## Replay and variation

- Replace sardines with oat porridge, market with tavern or tunics with an
  eligible hat supply by keeping each category independently met.
- Geometry, available building space and route length change between starter
  islands while the threshold structure remains.
- Claim IDs: `A117-001`, `A117-004`–`A117-007`, `A117-009`.

## Adjacent systems and history

- Anno 1800 likewise routes goods through local storage, settles upkeep and
  distinguishes island workforces. Its bounded packet needs each declared
  basic supply for a tier upgrade and includes a later World’s Fair, whereas
  the Latium packet allows substitution within each need category.
- The rule admits situational surplus: porridge can grow population, sardines
  also grant income, and both can be supplied without changing the minimum.
- Claim IDs: `A117-003`–`A117-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-068`, `ACT-139`, `ACT-172` | road segment, selected site, residence |
| System Behaviour | `SYS-153`, `SYS-154`, `SYS-156`, `SYS-157`, `SYS-245`, `SYS-1505`, `SYS-1506` | service reach, timers, stock, labour and attributes |
| Constraint | `CON-062`, `CON-172`, `CON-173`, `CON-184`, `CON-805`, `CON-806`, `CON-807` | authorized land, recipes, categories and storage path |
| Information | `INF-060`, `INF-086`, `INF-087`, `INF-509` | supply, labour, stock and category display |
| Objective | `OBJ-296` | first residence conversion |
| Time | `TIM-003` | active settlement simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `524` (`GAME-0001`–`GAME-0524`).
- Exact genome matches: none.
- Tied near matches: `GAME-0132` — Anno 1800 (`16 / 58 = 0.275862`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0132` — Anno 1800 | `ACT-068`, `ACT-139`, `ACT-172`, `CON-062`, `CON-172`, `CON-173`, `CON-184`, `INF-060`, `INF-086`, `INF-087`, `SYS-153`, `SYS-154`, `SYS-156`, `SYS-157`, `SYS-245`, `TIM-003` | Both grow road-connected settlements through production, goods logistics, recurring costs and tier-specific workers. Anno 1800 requires its named needs and follows the campaign toward the World’s Fair. Anno 117 substitutes different supplies within each category and ends after the first paid residence conversion. | Tied near (`0.275862`) |

### Preserved research notes

- New genes: `SYS-1505`, `SYS-1506`, `CON-805`, `CON-806`, `CON-807`, `INF-509`, `OBJ-296`.
- Classification result: `New gene`.
- Evidence and reasoning: category eligibility, optional need returns and local production buffs are independent.

## Taxonomy impact

- Registry changes: seven Active additions and sixteen unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_272](../../../research/taxonomy-changes/TAXONOMY_CHANGE_272.md).
- Candidate terms affected: category supply, residence attribute, local
  production effect, diagonal frontage and reachable store.

## Negative results

- None.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first residence upgrade requires
  satisfaction of independent need categories. Optional supply adds
  attribute returns and does not replace a missing category (`A117-005`, `A117-006`).

## New genes

- [Observation | Corroborated | High] Seven definitions in
  `TAXONOMY_CHANGE_272`.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_272`.

## New questions

- How does the introduction of two-point needs affect the optimal mix of
  first- and second-tier goods at a later threshold?

## Next recommended game

- [Hypothesis | Limited | Medium] Rez, original North American PlayStation 2.
- Optimisation criterion: contrast building a persistent supply network with
  batching target selection along a continuously moving route.
- Expected information gain: separate lock acquisition and volley release
  from scripted motion through one complete area.
- Backlog impact: advance Selection 041 to its fourth candidate.

## Why this game

- [Hypothesis | Limited | Medium] A correctly supplied local settlement
  illustrates the difference between a categorical upgrade predicate and the
  independent value of supplying more needs than the gate requires.
