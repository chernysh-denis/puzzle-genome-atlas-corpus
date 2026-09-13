---
game_id: GAME-0284
slug: cities-skylines-ii
game_title: "Cities: Skylines II"
analysis_status: reviewed
reviewed: 2026-09-09
combination_ids:
  - COMB-0269
gene_ids:
  action:
    - ACT-006
    - ACT-068
    - ACT-116
    - ACT-117
  system:
    - SYS-151
    - SYS-152
    - SYS-153
    - SYS-169
    - SYS-517
  constraint:
    - CON-170
    - CON-171
    - CON-440
  information:
    - INF-057
    - INF-207
  objective:
    - OBJ-169
  time:
    - TIM-003
---

# Game: Cities: Skylines II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `949230`, base package `885642` (containing only that application), default
  public branch build `23700737` (published 2026-06-22 12:00:09 UTC by the
  secondary distribution projection, `CS2-002a`), which Paradox's own dated
  announcement labels `Patch 1.6.0f1 - Summer Solstice` (published
  2026-06-22 12:00:56 UTC, `CS2-002b`); that the two describe the same build
  rests on their 47-second timestamp coincidence alone (`CS2-002c`); checked
  2026-09-09. Under accepted selection amendment 001, the bounded packet is one
  new city on the named base map `River Delta`, with the default economy,
  tutorials disabled and every unlimited option disabled, from new-city
  confirmation to settlement of the first named milestone, `Tiny Village`, in
  the same running city (`CS2-030`). Every admitted rule was checked against
  the post-launch official record rather than pre-release material alone; the
  applicability audit is `CS2-026`.
- Primary decision loop: read the demand bars, milestone bar and treasury;
  freely extend the starting road connection, authorise low-density
  residential, commercial and industrial cells, and place connected base-game
  electricity, water and sewage facilities; choose a simulation speed or
  pause; let the simulation construct private buildings while demand allows,
  recompute sector demand, carry utilities through the road network, and
  credit the progression measure from qualifying construction and periodic
  growth results; repeat until the accumulated measure reaches the first
  milestone's declared total and `Tiny Village` settles.
- Entry: the final new-city confirmation that creates the city on `River
  Delta` with the shipped defaults, followed by first control of the nine map
  tiles the city starts with unlocked, whose only built infrastructure is the
  map's Outside Connections.
- Positive terminal: the first milestone, named `Tiny Village` by the
  publisher (`CS2-005a`), settles when the accumulated progression measure
  reaches its declared total and the capabilities released by that settlement
  become available in the same running city (`CS2-006a`). The exact current
  threshold, one-time award and released list remain run-time parameters shown
  by the milestone surface rather than new genes (`CS2-005c`, `CS2-006b`). The
  named settlement is a finite, observable terminal under ADR-007; save and
  reload are outside the accepted packet (`CS2-030`).
- Negative terminal: none is authored. The product exposes no loss screen,
  bankruptcy settlement or time limit for this packet; the only negative
  boundary is indefinite non-progress, in which the city keeps running and the
  milestone does not settle (bounded negative search).
- Included: drawing and extending two-lane road from the road Outside
  Connection; zoning road-adjacent cells for Low Density Housing, Low Density
  Business and Industrial Manufacturing; choosing and placing one connected
  base-catalogue electricity source, one water source and one sewage discharge;
  selecting a simulation speed or pause; autonomous
  construction of private buildings on authorised cells; sector-demand
  recomputation; the carriage of electricity, water and sewage to those lots
  through the drawn roads; the crediting of the progression measure by each
  qualifying commit and by the periodic award; the milestone gate and its
  settlement; the demand bars, the electricity and water info views and the
  milestone bar; the one-time construction price of every commit and the
  monthly upkeep every retained facility then charges.
- Excluded: every paid and free downloadable application (nine Creator Packs,
  ten radio stations, `Bridges & Ports` and the `San Francisco Set`), the
  Ultimate Edition package, Paradox Mods, custom assets, the map and asset
  editors, custom maps, established saves and whole-city history; every other
  base map, since exactly one is analysed; every milestone after the first and
  everything any milestone releases, including taxation, the city budget and
  statistics panels, service budgets and fees, map-tile purchase, wider roads,
  higher zone densities and every civic service other than electricity and
  water; loans, for which no borrowing capacity before the first milestone is
  evidenced (`CS2-018c`); tile upkeep, which the publisher states the first
  nine tiles do not carry (`CS2-004b`); the alternative utility routes — a
  Small Coal Power Plant or an imported supply through a Transformer Station
  and the map's power-line Outside Connection, and a Water Pumping Station on
  surface water or a Groundwater Pumping Station on a deposit — which exist but
  are not the analysed route; demolition, the road Replace tool, de-zoning,
  terraforming and signature buildings, which the route does not require; the
  complete tutorial, its task list and cards, the historical Advisor and the
  current Encyclopedia as an action surface (`CS2-023b`, `CS2-028`,
  `CS2-029`); saving, loading and reload verification (`CS2-024`, `CS2-030`);
  building levelling,
  abandonment, trip generation and its pathfinding fallbacks, sewage backup,
  congestion and pollution, each of which
  the product produces somewhere but none of which this route needs, observes
  or answers before the terminal (`CS2-025`); the individual citizen Lifepath
  model beyond the aggregate population and satisfaction the measure consumes;
  achievements, photo mode, cinematic camera and climate seasons as a decision
  layer.
- Potential scoped modules: one later milestone chain with taxation and
  service budgets; the imported-utility route through the power-line Outside
  Connection; a surface-water or groundwater supply route; one public-transport
  network; one district and policy scope; the map editor.
- Reproducible parameterisation: install application `949230` from package
  `885642` on the default public branch; start a new city on `River Delta`,
  disable tutorials and every unlimited option, retain the default economy,
  confirm, and build only with the base catalogue available before the first
  milestone until `Tiny Village` settles. Where the road
  runs, how much of each of the three starting zone types is painted, where
  within the nine unlocked tiles the electricity, water and sewage facilities
  stand, how quickly households and companies arrive and exactly when the
  accumulated measure crosses the threshold, the exact facility variants, the
  threshold, award and released capabilities are run-time parameters. The
  bounded route uses an open-water sewage discharge; official map and utility
  rules plus silent visual route evidence establish accessible delta water
  without making any tutorial-card predicate part of the packet
  (`CS2-013c`, `CS2-031a`). No deficit, outage, demolition, abandonment or
  traffic event is required to reach the terminal.
- Direct-play status: not conducted. Valve application and package data
  establish lawful availability, the base package and the downloadable-content
  boundary; the SteamCMD projection establishes the current branch build, and
  Paradox's own dated announcement separately establishes the `1.6.0f1`
  version label and its content. Paradox's official Economy 2.0 material and
  the `1.1.5f1` patch establish the current money model, including the removal
  of government subsidies and the addition of tile upkeep; the official Maps &
  Themes page establishes the base maps, their Outside Connections and the nine
  unlocked starting tiles; the official Feature Highlight pages establish the
  progression, zoning, road and utility rules that the post-launch record does
  not supersede; and the publisher's dated Steam announcements establish the
  post-launch chronology, the in-game Encyclopedia and the current trip,
  demand and occupancy behaviour. The Paradox-hosted `cs2.paradoxwikis.com`
  wiki states that "Anyone can contribute to the wiki", so despite its
  publisher domain it is one community-maintained source family; its pages
  additionally carry their own version tags, and this record uses only pages
  whose tag is `1.1.5f1` or `1.5` for current claims, treating its `Version
  1.0` Economy and Services pages as superseded historical evidence
  (`CS2-026`). A public downloadable manual was not located on any surface
  searched, but the product does ship an in-game Encyclopedia, so no claim is
  made that no official rules source exists (`CS2-023a`, `CS2-023b`). This is
  an evidence-backed rules reconstruction, not a claimed captured playthrough.
  Two videos were inspected visually with audio muted throughout; no audio was
  heard or analysed, their frames were not reused, and their timestamps support
  only spatial route facts (`CS2-031a`, `CS2-031b`). No save or reload was
  performed or claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CS2-001` | The admitted product is the Windows Steam application `949230` Cities: Skylines II, developed by Iceflake Studios and Colossal Order, published by Paradox Interactive, released 2023-10-24, sold in Ukraine, in base package `885642` that contains only that application, separate from the Ultimate Edition package `885643` | Confirmed | Direct | High | P1, P2 |
| `CS2-002a` | The default public branch is build `23700737`, updated 2026-06-22 12:00:09 UTC | Observation | Limited | Medium | S1 (a secondary projection of Valve data; one family) |
| `CS2-002b` | Paradox's own dated announcement on the product's official Steam channel names `Patch 1.6.0f1 - Summer Solstice`, published 2026-06-22 12:00:56 UTC, and lists its gameplay, interface, visual, modding and Paradox Mods changes | Observation | Direct | High | P12 |
| `CS2-002c` | Build `23700737` is the build that carries `1.6.0f1`; this rests on the 47-second timestamp coincidence alone | Observation | Limited | Medium | S1, P12 (times only) |
| `CS2-003` | Twenty-one downloadable applications exist for the product — nine Creator Packs, ten radio stations, `Bridges & Ports` and the `San Francisco Set` — and none is contained in base package `885642` | Confirmed | Direct | High | P1, P2 |
| `CS2-004a` | A new city starts with nine map tiles **unlocked**, which is roughly the same starting area as in the first game; further tiles are unlocked as the game progresses | Confirmed | Direct | High | P13 |
| `CS2-004b` | The first nine tiles already unlocked when a city starts carry no tile-upkeep cost; tile upkeep applies only to tiles acquired afterwards and scales from 5% to 25% of their purchase cost as more are taken | Observation | Direct | High | P16 |
| `CS2-004c` | `River Delta` is a base-game map with a European theme, a −4 °C to 34 °C climate, 42% buildable area of the map's 441 tiles, and road, rail, ship, air and electricity Outside Connections | Observation | Corroborated | Medium | P13 (base map and its road, rail, ship and air connections), S2 (Maps, `Version 1.5`: theme, climate, buildable share, electricity connection) |
| `CS2-005a` | Each milestone is unlocked by reaching a declared amount of Expansion Points; passive points are awarded sixteen times through an in-game day as a result of increases in both Population and Happiness, and active points are granted immediately for actions such as placing or upgrading a service building, constructing a signature building or expanding the city's road network | Confirmed | Direct | High | P3; still current under the applicability audit `CS2-026` |
| `CS2-005b` | Expansion Points remain a tracked city quantity after Economy 2.0: the publisher's `Hotfix 1.2.3f1` announcement of 2025-01-22 fixes save files displaying incorrect Population and Expansion Points data | Observation | Direct | High | P14 |
| `CS2-005c` | The exact Expansion Point amount required for the first milestone was **not recovered from the enumerated sources**: the publisher's feature, news and support pages, the community wiki's `Progression` page and one press guide. This is a bounded research gap, not a claim that the value is never stated; the in-game progression bar exposes the current amount and the requirement to the player during play (`CS2-016`), and the two questions are distinct | Observation | Limited | Low | bounded negative search over P3, P13–P20 and S2 (Progression); recorded as an open evidence gap |
| `CS2-006a` | Reaching a milestone grants a mix of monetary reward, Development Points and Expansion Permits and gives access to new City Services, Policies and Management Options | Observation | Direct | Medium | P3 alone; `Direct` for what the publisher states, and one publisher family, so not `Corroborated` |
| `CS2-006e` | Milestone-gated unlocking is still live after launch: the publisher's `Detailer's Patch #2` announcement states that new park assets "unlock once you hit the Grand Village milestone", which also shows the named tiers still in use | Observation | Direct | High | P15 alone; the same publisher family as `CS2-006a`, so the two do not corroborate one another |
| `CS2-006b` | The first milestone's exact declared threshold, exact one-time award and exact released list were not established for `1.6.0f1` by the enumerated sources. The only table located is the community wiki's, whose page carries the version tag `1.1.5f1`, five minor versions behind the analysed build, and no official or independent current source corroborates it. Pass 01's enumeration of that table as the terminal bundle is withdrawn. The player-facing UI is not claimed to withhold these values | Observation | Limited | Low | S2 (Progression, `{{Version\|1.1.5f1}}`); bounded negative search over P3–P20; recorded as an open evidence gap |
| `CS2-006c` | Taxation, the city budget and statistics panels, service budgets, map-tile purchase, wider roads, higher zone densities and every civic service other than electricity and water are milestone-gated rather than available at the start; the sources disagree about which milestone releases each item, but every reading places each of them behind at least one milestone, so none is available before the first milestone settles | Observation | Limited | Medium | S2 (Progression `1.1.5f1`; Economy and Services, `Version 1.0`, superseded on numbering but agreeing on the gating) |
| `CS2-007` | At the start of a new city only the two-lane road is available; more road types unlock afterwards, and the publisher's 2026-03-18 patch records that roads "now properly unlock upon tutorial completion" | Observation | Corroborated | Medium | S2 (Roads, `Version 1.5`), P17 |
| `CS2-008a` | Roads are the backbone of the city, providing buildable zone area around them, paths for agents to travel on and the basic infrastructure for water and electricity distribution, because water pipes and electric cables run pre-built under the roads | Confirmed | Direct | High | P4, P7 |
| `CS2-008b` | All road types apart from highways carry a 40 MW low-voltage line, and those that are not bridges also carry water and sewage pipes | Observation | Limited | Medium | S2 (Roads, `Version 1.5`) |
| `CS2-009` | When an empty zone is assigned a zone type, buildings are built there automatically over time as long as there is demand; zoning is applied by Fill, Marquee or Paint mode | Observation | Corroborated | Medium | P5, S2 (Zoning) |
| `CS2-010` | Low Density Housing, Low Density Business and Industrial Manufacturing are the general zone types available at the start of a new city; the next residential density is milestone-gated | Observation | Limited | Medium | S2 (Zoning, Progression) |
| `CS2-011` | Zone demand is cyclic: residential demand increases with jobs, industrial demand grows when commercial zones need goods, commercial demand depends on manufacturing output and citizen purchasing power, and office demand rises with software production and workforce needs; `1.6.0f1` adjusted commercial demand slightly lower | Confirmed | Direct | High | P5, P12 |
| `CS2-012a` | Electricity exists as low voltage carried by the cables built into most road types and high voltage carried by power lines from power plants; a Transformer Station converts between them and can import or export through Outside Connections | Confirmed | Direct | High | P4 |
| `CS2-012b` | `Windmill` is a distinct named electricity asset with a 3 × 3 footprint, ₡8.5K construction cost, ₡2.5K monthly upkeep and 2 MW output, carrying only the `Basic Electricity Services` development-tree requirement that arrives with the service itself. `Small Wind Turbine` (8 × 8, ₡17.0K, ₡5.0K, 4 MW), `Wind Turbine`, `Small Transformer Station`, `Transformer Station` and `Small Coal Power Plant` are separate assets and are not interchangeable with it | Observation | Limited | Medium | S2 (Service buildings, `Version 1.5`); P21 confirms `Windmill`, `Small Wind Turbine` and `Small Transformer Station` are separately named assets |
| `CS2-013a` | Water is pumped from surface water areas or from groundwater deposits; sewage is either pumped into open water through a Sewage Outlet or treated in a treatment plant | Confirmed | Direct | High | P4 |
| `CS2-013b` | `Multi-Column Elevated Water Tower`, `Small Water Tower` and `Water Tower` are three distinct named assets, none of which declares a water source, unlike `Water Pumping Station` (surface water) and `Groundwater Pumping Station` (groundwater). `Multi-Column Elevated Water Tower` is 1 × 1, ₡20.0K, ₡5.0K upkeep, 10,000 output; `Sewage Outlet` is 2 × 2, ₡25.0K, ₡10.0K upkeep, 100,000 treatment. All carry only the `Basic Water & Sewage Services` requirement that arrives with the service itself | Observation | Limited | Medium | S2 (Service buildings, `Version 1.5`); P21 confirms `Multi-Column Elevated Water Tower` as a separately named asset |
| `CS2-013c` | `Sewage Outlet` discharges into open water. The official map page establishes `River Delta` and its ship connection, while silent visual inspection of the bounded route at `15:24` and `38:36` shows an early city beside accessible delta water. This establishes the spatial parameter only; it does not identify a current tutorial predicate or an exact facility variant | Observation | Limited | Medium | P13 and V1; P4 and S2 establish the discharge rule |
| `CS2-014` | A lack of electricity or water reduces citizens' Well-being; a lack of water and backed-up sewage also harm their Health, and affected companies lose Efficiency | Confirmed | Direct | High | P4 |
| `CS2-015` | The interface exposes the residential, commercial, industrial and office demand bars and selectable spatial info views, among them Electricity and Water & Sewage, which report total availability and any current trade | Observation | Limited | Medium | S2 (Info views) |
| `CS2-016` | The requirements to reach each milestone, and what it subsequently unlocks, are viewed by clicking the bar in the bottom-left of the screen | Observation | Limited | Medium | S3 (one press family) |
| `CS2-018a` | Government subsidies were **removed** from the city budget by Economy 2.0 to make the economy more challenging and transparent, because they "removed agency and consequences from the game"; city-service construction and upkeep together with roads are where most or all of the city's money goes, and service upkeep costs rose significantly in the same update | Observation | Direct | High | P8, P9 |
| `CS2-018b` | Economy 2.0 shipped as `Patch 1.1.5f1` on 2024-06-24, and no later official announcement through `1.6.0f1` restores government subsidies; the only later official use of the word describes player-set subsidies as a tax lever | Observation | Direct | High | P10, P18 (chronology search over the publisher's 59 dated announcements) |
| `CS2-018c` | The city pays a construction price once at each commit and a monthly upkeep for every retained facility thereafter; a construction price is not charged again at the monthly settlement | Observation | Direct | High | P8 and P9 (one publisher family) for upkeep as the recurring cost; `CS2-012b` and `CS2-013b` for the per-object prices |
| `CS2-018d` | No pre-terminal city revenue is evidenced: government subsidies are removed and taxation is milestone-gated, and no borrowing capacity before the first milestone is documented. This is an inference from two established rules plus a bounded negative search over the sources enumerated below, not a positive statement by any source | Observation | Limited | Medium | inference from `CS2-018a` and `CS2-006c`; bounded negative search over P3–P20 and S2 |
| `CS2-019` | The Economy Panel's Budget section displays Revenue, Expenses and the current Monthly Balance; zone tax rates range from -10% to 30%; service budgets are adjustable from 50% to 150%; and a single adjustable loan is sized with a slider — all of them behind their milestone gate for this packet | Confirmed | Direct | High | P6 |
| `CS2-023a` | No public downloadable manual was located on the Steam store page, in the Paradox helpdesk category or on the publisher's product and feature pages. This bounded negative does not imply that the product lacks official rules documentation | Observation | Limited | Low | bounded negative search over P1, P10, P11 and the publisher product surfaces |
| `CS2-023b` | The current client includes an in-game Encyclopedia for systems, tutorials and features; it replaced the Advisor on 2026-03-18, and `1.5.9f1` later fixed Encyclopedia and Glossary defects. Its contents were unavailable in this environment, so this record makes no claim about their text | Observation | Direct | High | P17, P19, P20 |
| `CS2-024` | The product loads existing maps and save games across the `1.6.0f1` update; saving and loading exist as commands but no reload was performed for this record | Observation | Direct | High | P12 |
| `CS2-025` | Building levelling, abandonment, citizen trip generation with its per-trip-type pathfinding fallbacks, sewage backup, congestion and pollution all exist in the product, and `1.6.0f1` adjusted several of them, but none of them is required to reach the first milestone and the analysed route neither observes nor answers any of them | Observation | Limited | Medium | P5, P12 and P4 are one publisher family for the existence half; the "not required here" half is this record's own route audit, which is not a second family, so the row inherits its weakest material clause |
| `CS2-026` | Version applicability was audited before any rule was admitted. Where a 2023 pre-release page and a post-launch official source disagree, the later source governs and the earlier statement is historical only; the community wiki's own page version tags were read, and its `Version 1.0` Economy and Services pages are treated as superseded | Observation | Direct | High | P8–P20, S2 page version tags; table reproduced in the pass-02 checkpoint |
| `CS2-028` | The 2023 opening tutorial used a locked ordered task list and non-skippable Task Cards. This is historical adjacent evidence only: the 2026 record says the Advisor was replaced by the Encyclopedia, and accepted amendment 001 disables the tutorial for this packet | Observation | Direct | Medium | P22 for the 2023 behaviour; P17 for the 2026 replacement |
| `CS2-029` | Static visual observation of the official 2023 task-list figure linked from `P22`, accessed 2026-09-09, shows seven ordered task names and locked later rows but no instruction predicates, facility variants, prices or quantities. It is historical tutorial evidence only and was not copied, reused or converted into artwork | Observation | Direct | Medium | P22 (figure) |
| `CS2-030` | The maintainer accepted `SEARCH_DEMAND_GAME_SELECTION_017_AMENDMENT_001` on 2026-09-09. The binding packet therefore disables tutorials and ends when `Tiny Village` settles in the same running city; save and reload are explicitly outside scope | Confirmed | Direct | High | accepted amendment 001 and the maintainer's recorded instruction |
| `CS2-031a` | Silent visual inspection of `Cities Skylines II - River Delta - Tiny Village`, accessed 2026-09-09 with audio muted throughout, shows the bounded city beside accessible open water with a utility route at `15:24` and a running city of 562 population beside the delta at `38:36`. It supports spatial route feasibility only, not version identity, the milestone instant or reload | Observation | Limited | Medium | V1, third-party visual method |
| `CS2-031b` | Silent visual inspection of the official Cities: Skylines channel's `How to: Start Your City`, accessed 2026-09-09 with audio muted throughout, visually shows an early connected electricity route beside open water at `3:01`–`3:09`. It is auxiliary route evidence only, not current-version proof | Observation | Direct | Low | V2, official visual method |
| `CS2-027` | The bounded identity is one new city on one named map advanced from nine unlocked tiles to its first progression milestone, where the player only draws road, authorises land use and places three priced utilities, while the simulation builds the private buildings, recomputes demand, carries electricity and water to them through those roads, and credits one accumulating measure both from every qualifying commit and from recorded growth until that measure reaches the declared total the milestone gate is waiting for | Observation | Limited | Medium | `CS2-004`–`CS2-026`; inherits the weakest material clause |

## Basic data

- Release / origin: Iceflake Studios and Colossal Order for Paradox
  Interactive; Steam release 2023-10-24; current announced version
  `Patch 1.6.0f1 - Summer Solstice`, 2026-06-22.
- Platform or physical form: lawfully available English Windows Steam client,
  base package `885642`; one new city on `River Delta` advanced to its first
  milestone.
- Puzzle family: real-time system pressure; route and network construction;
  municipal simulation.
- Primary and official sources, accessed 2026-09-09:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=949230&cc=ua&l=english).
  - `P2` — [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=885642&cc=ua&l=english).
  - `P3` — [Paradox, "Feature Highlight #10: Game Progression"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/game-progression),
    for Expansion Points, the passive sixteen-times-per-day award from
    Population and Happiness, the active award for placing or upgrading a
    service building, constructing a signature building or expanding the road
    network, the twenty milestones and the milestone reward mix. A 2023
    pre-release page, admitted for the clauses the post-launch record confirms
    rather than supersedes (`CS2-026`).
  - `P4` — [Paradox, "Feature Highlight #6: Electricity & Water"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/electricity-water).
  - `P5` — [Paradox, "Feature Highlight #4: Zones & Signature Buildings"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/zones-signature-buildings).
  - `P6` — [Paradox, "Feature Highlight #9: Economy & Production"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/economy-production).
  - `P7` — [Paradox, "Feature Highlight #1: Road Tools"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/road-tools).
  - `P8` — [Paradox, "Dev Diary: Economy 2.0 Part 1"](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/dev-diary-economy-part-one)
    (2024-06-03), for the removal of Government Subsidies and its stated
    reason, the significant increase in city-service upkeep, the new service
    import fee and its `Import City Services` policy toggle, and the reduced
    production and adjusted wages.
  - `P9` — [Paradox, "Dev Diary: Economy 2.0 Part 2"](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/dev-diary-economy-part-two),
    for "With Government Subsidies removed and City Service upkeep increased,
    the cost of running your city just increased", the rent formula, and
    building condition, levelling and deterioration.
  - `P10` — [Paradox, "The Economy Patch is here"](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/economy-patch-is-here),
    for Economy 2.0 shipping as `Patch 1.1.5f1` on 2024-06-24 and for the added
    Tile Upkeep.
  - `P11` — [Paradox Interactive helpdesk, Cities: Skylines 2 category](https://support.paradoxplaza.com/hc/en-us/categories/14628201653394-Cities-Skylines-2),
    whose articles are technical support only.
  - `P12` — [Paradox, "Patch 1.6.0f1 - Summer Solstice"](https://store.steampowered.com/news/app/949230/view/699893179027031259),
    the publisher's dated announcement, for the version label, the
    per-trip-type pathfinding limits, the lower commercial demand, households
    re-evaluating moving home, the road-access fix after levelling and support
    for loading old maps and save games.
  - `P13` — [Paradox, "Feature Highlight #7: Maps & Themes"](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/maps-themes),
    for "9 map tiles unlocked which is roughly the same starting area as in
    Cities: Skylines", for the base-map list with each map's Outside
    Connections including `River Delta`'s road, train, ship and air, and for
    all maps including power lines for electricity connections.
  - `P14` — the publisher's dated `Hotfix 1.2.3f1` announcement of 2025-01-22
    on its [official Steam announcement channel](https://store.steampowered.com/news/app/949230),
    for Expansion Points remaining a tracked city quantity after Economy 2.0.
  - `P15` — the publisher's dated `Detailer's Patch #2` developer diary of
    2024-12-11 on the same channel, for park assets that "unlock once you hit
    the Grand Village milestone", confirming post-launch that milestones still
    gate unlocks and still carry their named tiers.
  - `P16` — [Paradox, "Tile Upkeep explained"](https://www.paradoxinteractive.com/games/cities-skylines-ii/news/tile-upkeep-explained)
    (2024-06-28), for "The first 9 tiles already unlocked when you start a city
    do not have a cost" and for the 5%-to-25% upkeep curve on later tiles.
  - `P17` — the publisher's dated `Office Evolution & City Stations` patch
    announcement of 2026-03-18 on the same channel, for "A first version of the
    new in-game Encyclopedia is also included. It gathers useful information
    about game systems, tutorials, and features into one searchable place", for
    "New feature: Encyclopedia. Advisor has been removed and is replaced by
    Encyclopedia", and for "Roads now properly unlock upon tutorial
    completion".
  - `P18` — the publisher's [official Steam announcement channel](https://store.steampowered.com/news/app/949230)
    for application `949230`, enumerated for this record as the 59 dated
    official announcements from 2024-10-23 to 2026-09-09 and keyword-scanned
    for subsidy, milestone, Encyclopedia, Expansion Point and progression
    changes; individual announcements opened in full are cited separately.
  - `P19` — the publisher's dated `City Corner #1 — Upcoming Visual Updates` of
    2026-01-29 on the same channel, for the announced in-game Encyclopedia
    "which has all the information at your disposal during gameplay".
  - `P20` — the publisher's dated `Patch 1.5.9f1 - Morning Dew` announcement of
    2026-05-27 on the same channel, for fixes to encyclopedia typos and
    incorrect information and to the Glossary, confirming that both shipped
    surfaces are live in the current build.
  - `P21` — the publisher's dated Bike Patch announcement on the same channel,
    [`https://store.steampowered.com/news/app/949230/view/633446704518004755`](https://store.steampowered.com/news/app/949230/view/633446704518004755),
    for `Windmill`, `Small Wind Turbine`, `Small Transformer Station` and
    `Multi-Column Elevated Water Tower` appearing as four separately named
    assets, which is why this record never substitutes one for another.
  - `P22` — [Colossal Order, "Behind the Scenes #6: Tutorials & Advisor"](https://colossalorder.fi/news/behind-the-scenes-6-tutorials-advisor/),
    the developer's own article, for the task list, its locking and
    skippability rules, the Task Card contents and completion mark and the
    Advisor's appearance after completion, together with its linked static
    task-list figure inspected once for `CS2-029`. Colossal Order is the
    game's developer and part of the same publisher family as `P3`–`P21`.
- Corroborating textual sources, accessed 2026-09-09:
  - `S1` — [public SteamCMD info projection](https://api.steamcmd.net/v1/info/949230),
    for the `public` branch build `23700737`; a secondary distribution mirror.
  - `S2` — [Cities Skylines 2 Wiki](https://cs2.paradoxwikis.com/Cities_Skylines_II_Wiki),
    hosted on a Paradox domain but community-maintained — its own front page
    states that "Anyone can contribute to the wiki" — read on the pages
    Progression (`{{Version|1.1.5f1}}`), Service buildings (`Version 1.5`),
    Maps (`Version 1.5`), Roads, Zoning, Info views, Sewage, Groundwater, Map
    Creation: Outside Connections, and the superseded Economy and Services
    pages (`Version 1.0`); one family however many pages agree, never sole
    support for a product or version claim, and each page's own version tag is
    recorded in the applicability audit.
  - `S3` — [Dexerto, "Cities Skylines 2 Milestones explained"](https://www.dexerto.com/gaming/cities-skylines-2-milestones-explained-all-rewards-2348210/),
    for the milestone requirement bar in the bottom-left of the screen and the
    three simulation speeds; one press family of lower reliability.
- Negative searches, 2026-09-09: no `View manual` link on the Steam store page;
  no gameplay manual in the Paradox helpdesk category; no manual linked from
  the publisher's product or feature pages; no located source states the exact
  Expansion Point requirement for the first milestone; no located current
  source states the first milestone's exact award or unlock list; no borrowing
  capacity before the first milestone is documented; no official announcement
  from Economy 2.0 through `1.6.0f1` restores government subsidies; and no
  loss, bankruptcy or time-limit terminal is documented for a new city. The
  in-game Encyclopedia was not accessible in this research environment, so it
  is inventoried as an existing official rules surface rather than searched.
- Evidence independence: sources are counted by independent family or method,
  not by page count or by hostname. Valve data (`P1`, `P2`, `S1`) is one
  family; every Paradox and Colossal Order statement (`P3`–`P22`, on
  paradoxinteractive.com, colossalorder.fi, the Paradox helpdesk and the
  publisher's own Steam announcement channel) is **one** family, because
  Colossal Order is the developer of the game Paradox publishes and a
  publisher-owned studio page does not independently corroborate a publisher
  page merely by having a different hostname; a bounded negative search is not
  a second positive method; the Paradox-hosted but
  community-edited wiki (`S2`) is a second family; the press guide (`S3`) is a
  third of lower reliability. `Corroborated` requires two families; `S2` alone
  is `Limited`; a single publisher statement is `Direct` for what it states.
- Visual evidence: `V1` is
  [Cities Skylines II - River Delta - Tiny Village](https://www.youtube.com/watch?v=01Yw1SWcTaA),
  inspected at `15:24` and `38:36`; `V2` is the official Cities: Skylines
  channel's
  [How to: Start Your City](https://www.youtube.com/watch?v=j8QkSxavoys),
  inspected at `3:01`–`3:09`. Both were accessed 2026-09-09 with audio muted
  throughout. No audio was heard or analysed; no frame, transcript or video
  asset was reused in artwork.
- Reproducible control: repository-side transition reconstruction across
  `P1`–`P22`, `S1`–`S3` and `V1`–`V2` under the declared application, package,
  branch, map, options and milestone terminal; rules reasoning, not direct
  play.
- Claim IDs: `CS2-001`–`CS2-031`; lettered sub-rows split composite claims so
  that each clause carries its own grade.

## Mechanical decomposition

### Action Genes

- Existing `ACT-006`: select one of the three simulation speeds or pause the
  running city without changing what the simulation will do (`CS2-016`);
  `ACT-068`: draw and extend the persistent two-lane road graph from the map's
  road Outside Connection, whose branching intersections are used automatically
  (`CS2-007`, `CS2-008a`); `ACT-116`: paint the road-adjacent zone cells with
  Low Density Housing, Low Density Business or Industrial Manufacturing,
  authorising rather than placing the private buildings (`CS2-009`,
  `CS2-010`); `ACT-117`: freely choose and commit priced base-catalogue
  electricity, water and sewage facilities, each with its construction cost,
  monthly upkeep and network attachment (`CS2-012b`, `CS2-013b`, `CS2-013c`,
  `CS2-018c`). Exact facility variants and positions are route parameters, not
  separate genes.
- Input audit, classified by immediate mechanical result: road drawing edits
  the persistent network; zoning paints an authorisation and places nothing;
  facility placement commits a priced object into the coverage network; the
  speed selector changes only the rate of automatic progression. The new-city
  configuration precedes the entry checkpoint and is this packet's declared
  parameterisation. Demolition, the road Replace tool, de-zoning, terraforming
  and signature buildings are available but are not required, are not
  instructed and are excluded. Manual saving and loading are excluded: the
  product supports them (`CS2-024`), but the terminal is the milestone
  settlement, no reload was executed, and no save command is causally required.
- Rejected `ACT-118`, `ACT-132`, `ACT-023`: taxation and service funding,
  districts and policies, and transport lines are all milestone-gated and
  therefore outside a packet that ends at the first milestone (`CS2-006c`).
  Rejected `ACT-139`: private buildings are not placed by the player, and the
  placed objects here are priced utilities already owned by `ACT-117`. Rejected
  `ACT-148`: no material-backed construction plan exists; a facility is paid
  once from the treasury. Rejected `ACT-149`: the Development Tree spend is not
  available before the first milestone grants its first point. Rejected
  `ACT-120`: no recipe, stop or filter is configurable in this packet.
- Parameters: road geometry and length, zone class and parcel shape, tool
  mode, the position of each of the three facilities inside the nine unlocked
  tiles, simulation speed and pause.
  Claims: `CS2-007`–`CS2-013`, `CS2-016`, `CS2-018c`.

### System Behaviour Genes

- Existing `SYS-151`: private buildings are constructed automatically on the
  authorised cells wherever demand and the enabling services allow
  (`CS2-009`); building levelling and abandonment are excluded, because the
  route neither needs nor answers them before the terminal (`CS2-025`).
  `SYS-152`: residential, commercial, industrial and office demand is
  recomputed continuously, and an authorised cell develops only while its
  sector's demand lasts (`CS2-011`). `SYS-153`: electricity, water and sewage
  reach the developing lots through the cables and pipes built into the drawn
  roads, and a lot without them loses Well-being, Health or company Efficiency
  (`CS2-008a`, `CS2-012a`, `CS2-013a`, `CS2-014`).
- Existing `SYS-517`, generalised by
  [`TAXONOMY_CHANGE_050`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_050.md)
  from completed activity results to any declared qualifying result: every
  qualifying commit credits its own configured amount to the city's one
  retained progression measure, and the periodic award credits recorded
  increases in population and satisfaction to the same measure, so building and
  growing substitute for one another on the way to the milestone (`CS2-005a`,
  `CS2-005b`, `CS2-012b`, `CS2-013b`).
- Existing `SYS-169`, generalised by
  [`TAXONOMY_CHANGE_048`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_048.md)
  so that the compared measure is a declared settlement progression measure
  rather than population alone: when the accumulated measure first reaches the
  milestone's declared total, the simulation settles that milestone,
  permanently adds the capabilities it releases to the available catalogue and
  pays its declared one-time award (`CS2-005a`, `CS2-006a`). What exactly is
  released and paid is an open evidence gap (`CS2-006b`), so this record
  admits the act and not its contents.
- Rejected `SYS-736`, `SYS-159`, `SYS-194`: accepted amendment 001 disables the
  tutorial, so no staged tutorial predicate, produced-resource queue or
  technology queue is exercised by this packet (`CS2-030`).
- Split-first: crediting the measure, comparing it against the threshold and
  withholding the capability beforehand were tested as one boundary and kept
  apart, because the corpus already separates them: `SYS-517` credits,
  `CON-440` withholds and `INF-207` discloses in two existing carriers, while
  `SYS-169` performs the municipal catalogue addition that those carriers do
  not have. Household and company occupancy remains `SYS-151`'s occupancy
  parameter, as the two existing city carriers keep it. The two producers of
  the measure were tested as separate rules and kept as parameters of one,
  because they feed the same number toward the same gate and neither is
  independently transferable.
- Rejected `SYS-154`: its boundary credits taxes and deals and debits
  maintenance at a recurring settlement. In this packet there is no credit
  side at all — Economy 2.0 removed government subsidies and taxation is
  milestone-gated — so only its debit clause is exercised, and that clause is
  `CON-171`'s own recurring-expenditure boundary rather than a settlement
  (`CS2-018a`, `CS2-018c`). Rejected `SYS-155`: trip generation and congestion
  exist, but the route reaches the terminal without them and neither observes
  nor answers them (`CS2-025`). Rejected `SYS-031`: no line or vehicle service
  exists. Rejected `SYS-262`: the measure is not produced by staffed science
  workplaces and is never spent. Rejected `SYS-299`: its recipient is a
  character whose thresholds raise character levels. Rejected `SYS-171`,
  `SYS-210`: both need a delivered quantity submitted to a receiver, while half
  of this measure arrives with nothing delivered. Rejected `SYS-342`: no
  personal skill improves. Rejected `SYS-180`: the measure has two declared
  sources rather than one sustained condition. Rejected `SYS-182`: the
  milestone pays a declared award, not a finite set of offers. `SYS-377` was
  deprecated by `TAXONOMY_CHANGE_016` and is history rather than a candidate.
  The pass-01 proposal to create a new System gene for this measure is
  withdrawn in
  [`TAXONOMY_CHANGE_050`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_050.md):
  the generalised `SYS-517` owns that boundary, and two producers of one
  measure are parameters rather than an independently transferable rule.
- Resolution order: accept the road, zone, facility or speed commit; credit the
  active award; advance the simulation clock; carry electricity, water and
  sewage; recompute sector demand; construct private buildings on authorised
  cells wherever demand and supply allow; move households and companies in;
  update population and satisfaction; credit the periodic award on its tick;
  charge the monthly upkeep; test the milestone total and, when it is first
  reached, settle the milestone and add what it releases.
  Claims: `CS2-005`, `CS2-006`, `CS2-008`–`CS2-014`, `CS2-018`.

### Constraint Genes

- Existing `CON-170`: an authorised cell develops only where the zone grid
  exists, which is the frontage the drawn road creates, because roads "provide
  buildable zones around them" (`CS2-008a`). The gene's utility-prerequisite
  clause is **not** asserted here: the located sources prove that a shortage of
  electricity or water reduces well-being, health and company efficiency
  (`CS2-014`), which is a downstream penalty rather than a precondition for a
  lot to begin developing, and no located source states that a lot cannot
  develop without them. Utilities are selected infrastructure in the amended
  route, not a universal development prerequisite; `CON-171`: every road and
  facility is paid once from the treasury
  and every retained facility then charges a monthly upkeep against a treasury
  that no government subsidy replenishes and that no pre-terminal revenue
  refills (`CS2-018a`, `CS2-018c`); `CON-440`: the capabilities a milestone
  releases stay unavailable until the city's accumulated progression total
  reaches that milestone's declared amount, and reaching it makes them legal
  without any single payer providing the whole amount (`CS2-005a`,
  `CS2-006a`, `CS2-006c`).
- Rejected `CON-179`: its boundary gates the municipal catalogue on a
  population milestone. Pass 01 proposed widening it to any settlement
  progression measure, which would have duplicated `CON-440`; that proposal is
  withdrawn in
  [`TAXONOMY_CHANGE_049`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_049.md)
  and `CON-179` keeps its committed wording and its two population-gated
  carriers. Rejected `CON-048`, `CON-050`: no ordered line or vehicle capacity.
  Rejected `CON-062`: the placement legality here is road frontage and supply,
  not exclusive anchors between machine footprints. Rejected `CON-184`: a
  facility needs treasury, not an owned design and delivered materials.
  Rejected `CON-185`: no finite staff slot is filled. Rejected `CON-172`,
  `CON-173`: no recipe flow or extraction locus is exercised. Rejected
  `CON-191`: the milestone is not purchased against a predecessor level.
- Scarce strategic resources: the starting treasury, which only depletes;
  monthly upkeep capacity; electricity and water capacity; buildable area
  inside the nine unlocked tiles; road frontage; and the demand that decides
  whether an authorisation is worth painting.
  Claims: `CS2-004`, `CS2-005a`, `CS2-006`, `CS2-008a`, `CS2-014`, `CS2-018`.

### Information Genes

- Existing `INF-057`: the interface exposes current residential, commercial,
  industrial and office demand plus the selectable Electricity and Water &
  Sewage info views that report total availability, which are the two views
  this route reads before extending supply (`CS2-015`); `INF-207`: the bar in
  the bottom-left exposes the city's current progression measure, the
  requirement for the next milestone and what that milestone will release, so
  the player can see before committing whether the successor is still locked
  (`CS2-005a`, `CS2-016`). The `INF-207` instance is graded `Limited` because
  the displayed measure and requirement rest on one press family.
- Rejected `INF-268`, `INF-329`, `INF-067`, `INF-103`: the tutorial and its
  task-card information are outside the accepted packet; no other admitted
  surface exposes an authored next instruction, measured checklist, task
  reward, deadline, branch or construction quota (`CS2-028`–`CS2-030`).
- Excluded: the itemised municipal ledger, tax rates and service budgets, all
  behind their milestone gate (`CS2-006c`, `CS2-019`), so `INF-058` is
  rejected; the per-building notification catalogue, because the route does not
  produce or answer a shortage, an abandonment or a lost access (`CS2-025`);
  and the bare persistent money and population readouts, which are
  undifferentiated scalars that `INF-058` explicitly excludes and for which no
  itemisation before the terminal is evidenced. Rejected `INF-060`: no live
  production panel exists before its milestone. Rejected `INF-063`: no exact
  delivery shape or quota is disclosed. Rejected `INF-066`: no opposed failure
  track exists. Rejected `INF-001`: the info views reveal selected projections,
  not the complete simulation state.
- Claims: `CS2-005a`, `CS2-006c`, `CS2-015`, `CS2-016`, `CS2-019`.

### Objective Genes

- New `OBJ-169`: raise the city's retained progression measure to the first of
  its declared thresholds and reach the persistent state in which that
  threshold has settled and the capabilities it releases stay available, while
  the city itself is not completed and the same measure keeps accumulating
  toward the later thresholds this packet excludes (`CS2-005a`, `CS2-006a`).
- Rejected `OBJ-165`: it requires the bounded region to count as *resolved*
  once its measure is filled, with authored successors then selectable. The
  smallest counterexample is that a Cities: Skylines II city is never resolved:
  the same measure continues past this terminal toward nineteen further
  thresholds on the same subject, and what becomes available is a set of
  commands rather than a choice among authored successors. Rejected `OBJ-053`:
  it requires an open-ended horizon in place of a declared threshold. Rejected
  `OBJ-056`: it settles the *final* qualification of an ordered chain, while
  this is the first of twenty. Rejected `OBJ-150`: it needs a finite ordered
  event judged by finishing place against rivals. Rejected `OBJ-059`: no
  opposed failure track bounds the attempt. Rejected `OBJ-001`: it compares one
  produced element's value and has no persistence clause. Rejected `OBJ-088`,
  `OBJ-098`: their advancing subject is a rank or membership earned by named
  designated events.
- Success, evaluation and failure: success is the first settlement of the first
  milestone with what it releases retained; there is no authored failure
  terminal, and indefinite non-progress leaves the city running without
  settling it (bounded negative search).
  Claims: `CS2-005`, `CS2-006`.

### Time Genes

- Existing `TIM-003`: construction, occupancy, demand, utility flow, the
  monthly upkeep charge and the periodic progression award all advance on a
  live clock while the road, zoning, facility and speed commands remain
  available, with pause and the three speeds as rate controls (`CS2-016`,
  `CS2-018c`).
- Rejected `TIM-001`, `TIM-005`: no turn or phase structure exists. Rejected
  `TIM-021`: persistence here is the settled milestone, not an irreversible
  autosave contract. The day-night cycle and seasons are presentation and
  climate parameters this packet does not turn into a decision layer.
  Claims: `CS2-016`, `CS2-018c`.

## Reproducible transitions

Every row is labelled **F** for a freely chosen commit or **A** for autonomous
resolution. Tutorials are disabled, so the construction order within the
declared route is a reproducible choice rather than an authored task chain.

| # | Class | Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|---|---|
| 1 | F | The new city exists on `River Delta` with nine unlocked tiles and tutorials disabled | Draw two-lane road from the road Outside Connection | The treasury pays once; the persistent road graph extends with embedded cable and pipes; roadside zone cells appear; the commit credits the progression measure | road as network, frontage and utility carrier | `CS2-005a`, `CS2-007`, `CS2-008a`, `CS2-018c`, `CS2-030` |
| 2 | F | Road-adjacent cells are available | Paint Low Density Housing | The cells authorise residential use without placing private buildings | zoning authorises rather than places | `CS2-009`, `CS2-010` |
| 3 | F | Road-adjacent cells are available | Paint Low Density Business | The cells authorise commercial use | a second freely chosen zone class | `CS2-009`, `CS2-010` |
| 4 | F | Road-adjacent cells are available | Paint Industrial Manufacturing | The cells authorise industrial use | a third freely chosen zone class | `CS2-009`, `CS2-010` |
| 5 | F | The road-carried grid can accept a producer | Choose and place one base-catalogue electricity source | The treasury pays its price once; the asset joins the grid, monthly upkeep begins and the commit credits the measure | priced generation as a route parameter | `CS2-012a`, `CS2-012b`, `CS2-018c` |
| 6 | F | The road-carried pipe network can accept supply | Choose and place one base-catalogue water source | The treasury pays once; water capacity joins the pipe network, monthly upkeep begins and the commit credits the measure | priced water supply as a route parameter | `CS2-013a`, `CS2-013b`, `CS2-018c` |
| 7 | F | Accessible delta water and the pipe network are available | Place one sewage discharge connected to the network and open water | The treasury pays once; sewage capacity joins the network, monthly upkeep begins and the commit credits the measure | priced sewage disposal and spatial feasibility | `CS2-013a`, `CS2-013c`, `CS2-018c`, `CS2-031a` |
| 8 | F | Planning is needed, or time should pass faster | Select one of three simulation speeds, or pause | The rate of automatic change alters; nothing else does | direct control of simulation rate | `CS2-016` |
| 9 | A | Authorised cells have frontage and their sectors' demand is positive | None | Private buildings are constructed; households and companies move in; population and satisfaction rise; sector demand is recomputed | autonomous development under demand | `CS2-009`, `CS2-011` |
| 10 | A | The city has connected facilities and a month elapses | None | Utilities are carried through roads; retained facilities charge monthly upkeep against a treasury with no evidenced incoming side | supply propagation and one-directional money | `CS2-008a`, `CS2-014`, `CS2-018c`, `CS2-018d` |
| 11 | A | Qualifying commits, population or satisfaction changes are recorded | None | Construction credits and the periodic award feed the same retained progression measure | one measure with two declared source classes | `CS2-005a`, `CS2-005b` |
| 12 | A | The accumulated measure first reaches the milestone's declared total | None | `Tiny Village` settles and its released capabilities become available in the same running city | the finite gate and settlement terminal | `CS2-005a`, `CS2-005c`, `CS2-006a`, `CS2-006b`, `CS2-030` |

Exact road geometry, zoning area, facility variants, facility positions,
threshold, award and released capabilities are run-time parameters. Tutorial
predicates and save/reload are outside the accepted packet.

## Strategic and experiential structure

- Planning horizon: reach the first milestone before the treasury, which has no
  incoming side, is exhausted by construction prices and accumulated monthly
  upkeep.
- Local tactics: extend road in increments that create just enough frontage;
  paint only as much of each zone as current demand supports; choose the
  cheapest starting utility that covers the lots, because every facility adds a
  permanent monthly charge; remember that each commit itself credits the
  measure, so the cheapest useful commit is also progress.
- Medium-term structure: every commit is paid twice — once in price and again
  every month — while also crediting the measure, so over-building buys
  progress and insolvency together, and the only other source of progress is
  letting the city grow.
- Reversible versus irreversible: demand, supply and the treasury change from
  moment to moment; the road graph, the zoned cells and the placed facilities
  persist and were paid for; the settled milestone and what it releases are the
  retained successor that later play cannot revoke.
- Failure attribution: the demand bars say which authorisation is worth
  painting and the electricity and water views say whether supply reaches the
  lots; the exact progression threshold is never stated, so the player reads
  the milestone bar rather than a number.
- Player trust: an authorised cell with frontage, power and water must
  eventually develop while demand lasts, a placed facility must keep supplying
  what it covers, and the milestone must settle permanently the first time its
  measure reaches the total.
  Claims: `CS2-005`–`CS2-018`.

## Replay and variation

- What changes between cities: where the road runs on `River Delta`, the mix
  and placement of the three starting zone types, where the three utilities
  stand, how quickly households and companies arrive and when the measure
  crosses the threshold.
- Randomness or procedural generation: the map and rules are fixed; variation
  comes from the coupled simulation's response to the city's shape and from
  the arrival order of households and companies.
- Multiple viable strategies: a compact housing-first start, an
  industry-first start, and a minimal-footprint start that leans on commit
  credits rather than growth all reach the first milestone.
- Typical replay motive: test how small a footprint can still reach the
  milestone, or compare a growth-led against a construction-led route to the
  same threshold.
  Claims: `CS2-004c`, `CS2-005a`, `CS2-009`–`CS2-013`.

## Adjacent systems and history

- Direct product corridor: `GAME-0121` Cities: Skylines is the same series and
  is audited gene by gene in the delta table below.
- Same-corpus corridors: SimCity 4 Deluxe Edition, the mathematically selected
  neighbour, shares zoning, priced utility placement, autonomous development,
  demand recomputation, coverage propagation, access and solvency legality, the
  demand and overlay disclosure, road editing, speed control and live time, but
  adds tax and funding control, an itemised ledger, a recurring settlement with
  a credit side and an open-ended mayoral horizon that this packet does not
  reach. Forza Horizon 6 and Far Cry 5 are the unexpected corridor: this packet
  joins their progression structure exactly, sharing the credited measure, its
  threshold gate and its disclosure as the verified `COMB-0269`.
- Important differences: this packet ends at an authored progression threshold
  instead of continuing open-ended; its measure is credited both by the
  player's construction and by the city's own growth; and its treasury has no
  incoming side at all, because Economy 2.0 removed government subsidies and
  taxation waits behind the milestone that ends the packet.
  Claims: `CS2-005`, `CS2-006`, `CS2-018`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-068`, `ACT-116`, `ACT-117` | road geometry, zone class, tool mode, the three facility positions, speed and pause |
| System Behaviour | `SYS-151`, `SYS-152`, `SYS-153`, `SYS-169`, `SYS-517` | occupancy, demand sectors, cable and pipe capacity, the two credit sources and their rates, the milestone's released capabilities |
| Constraint | `CON-170`, `CON-171`, `CON-440` | frontage, supply, construction price, monthly upkeep, the nine unlocked tiles and the milestone total |
| Information | `INF-057`, `INF-207` | demand bars, electricity and water views, the milestone bar and its requirement |
| Objective | `OBJ-169` | the first of twenty thresholds on a continuing subject |
| Time | `TIM-003` | monthly upkeep charge, the periodic credit tick, three speeds and pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `283` (`GAME-0001`–`GAME-0283`).
- Exact genome matches: none.
- Tied near matches: `GAME-0118` — SimCity 4 Deluxe Edition (`11 / 21 = 0.523810`).
- Supported combination subsets: `COMB-0269`.
- Scan date: 2026-09-09.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0118` — SimCity 4 Deluxe Edition | `ACT-006`, `ACT-068`, `ACT-116`, `ACT-117`, `SYS-151`, `SYS-152`, `SYS-153`, `CON-170`, `CON-171`, `INF-057`, `TIM-003` | Both zone land for autonomous private development, place priced utility infrastructure on an edited road graph, recompute sector demand, propagate coverage, gate development on access and solvency, expose demand bars and spatial overlays, and run live with speed control. SimCity 4 additionally lets the mayor set taxes and service funding, exposes an itemised budget ledger, settles a recurring budget with a real credit side and evaluates an open-ended city with no authored terminal. This packet has none of those four: taxation and the budget panel are milestone-gated, its treasury has no incoming side after Economy 2.0 removed government subsidies, and its objective instead raises a credited progression measure to the first declared milestone settlement and keeps what that threshold releases. | Near, `0.523810` |

### Preserved research notes

- New genes: `OBJ-169`.
- Reused genes: `ACT-006`, `ACT-068`, `ACT-116`, `ACT-117`, `SYS-151`,
  `SYS-152`, `SYS-153`, `SYS-169`, `SYS-517`, `CON-170`, `CON-171`,
  `CON-440`, `INF-057`, `INF-207` and `TIM-003`.
- Classification result: `New gene`.
- Evidence and reasoning: twelve boundaries transfer from the reviewed corpus
  without any definition change. `SYS-517` and `CON-440` transfer after the
  minimal generalisation recorded in `TAXONOMY_CHANGE_050`, which keeps the
  Forza Horizon 6 and Far Cry 5 instances true sentence by sentence because a
  completed activity result is one kind of declared qualifying result;
  `SYS-169` transfers after `TAXONOMY_CHANGE_048`, which keeps the Cities:
  Skylines and Anno 1800 instances true with population as the measure's
  parameter value. One gene is new: no existing objective settles the *first*
  of several declared thresholds on a subject that is not completed by
  crossing it, which is what separates `OBJ-169` from every retained-successor
  objective whose subject finishes when its measure fills. It is portable to
  any tiered settlement or campaign progression and is named after no map,
  milestone, building, service or product.

## Taxonomy impact

- Registry changes: one new Active gene; `SYS-169` generalised by
  [`TAXONOMY_CHANGE_048`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_048.md)
  and `SYS-517` with `CON-440` generalised by
  [`TAXONOMY_CHANGE_050`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_050.md);
  the pass-01 proposal to widen `CON-179` is withdrawn in
  [`TAXONOMY_CHANGE_049`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_049.md)
  and that gene keeps its committed wording; twelve further Active genes
  gain this game as an additional carrier. No lifecycle, ID or earlier reviewed
  signature changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_048` and `TAXONOMY_CHANGE_050`
  accepted; `TAXONOMY_CHANGE_049` rejected.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`;
  `Cities: Skylines II`, `River Delta`, Expansion Points, Development Points,
  Expansion Permits, Outside Connection, Windmill, Water Tower, Sewage Outlet,
  `Patch 1.6.0f1` and every application, package and build identifier remain
  parameters or literal product terms.

## Negative results

- No direct play, audio, save or reload was executed or claimed. Two bounded
  video fragments were inspected visually with audio muted throughout; their
  frames were not reused and only their logged spatial observations enter the
  evidence ledger (`CS2-031a`, `CS2-031b`).
- Government subsidies are not part of the current ruleset. Economy 2.0 removed
  them and no official announcement through `1.6.0f1` restores them, so every
  pass-01 claim that a shrinking subsidy funds the early city is withdrawn
  (`CS2-018a`, `CS2-018b`).
- The first milestone's exact threshold, award and released capabilities are
  not established for the analysed build and are recorded as run-time gaps
  rather than enumerated (`CS2-005c`, `CS2-006b`). They do not prevent the
  named milestone surface from settling the bounded terminal.
- No claim is made that no official rules source exists: the product ships an
  in-game Encyclopedia and a Glossary, and the located negative is limited to a
  public downloadable manual on the surfaces actually searched (`CS2-023a`,
  `CS2-023b`).
- `ACT-118`, `ACT-132`, `ACT-023`, `ACT-139`, `ACT-148`, `ACT-149`,
  `ACT-120`, `SYS-031`, `SYS-154`, `SYS-155`, `SYS-171`, `SYS-180`,
  `SYS-182`, `SYS-210`, `SYS-262`, `SYS-299`, `SYS-342`, `CON-048`,
  `CON-050`, `CON-062`, `CON-172`, `CON-173`, `CON-179`, `CON-184`,
  `CON-185`, `CON-191`, `INF-001`, `INF-058`, `INF-060`, `INF-063`,
  `INF-066`, `OBJ-001`, `OBJ-053`, `OBJ-056`, `OBJ-059`, `OBJ-088`,
  `OBJ-098`, `OBJ-150`, `OBJ-165`, `TIM-001`, `TIM-005` and `TIM-021` are
  rejected with the smallest counterexamples recorded above; `SYS-736` and
  `INF-268` are excluded because accepted amendment 001 disables the tutorial;
  `SYS-377` was
  deprecated by `TAXONOMY_CHANGE_016` and is recorded here only as history.
- The pass-01 proposal to create a new System gene for the credited measure is
  withdrawn, its identifier is retained `Deprecated` with no carrier so that it
  is never reused, and the decision is recorded in
  [`TAXONOMY_CHANGE_050`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_050.md):
  the generalised `SYS-517` owns that boundary, and two producers of one
  measure are parameters rather than an independently transferable rule.
- No deficit, outage, abandonment, levelling, traffic event or pollution event
  is instructed or admitted; each exists in the product but none is needed,
  observed or answered by this route before the terminal.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current base-package Windows availability, the
  nine unlocked starting tiles, the Expansion Point progression rule and its
  two sources, the road-carried electricity and water networks, the cyclic zone
  demand, the shortage consequences and the Economy Panel's structure are fixed
  in `CS2-001`, `CS2-004a`, `CS2-005a`, `CS2-008a`, `CS2-011`, `CS2-012a`,
  `CS2-013a`, `CS2-014` and `CS2-019`.
- [Observation | Direct | High] Paradox's own material establishes that
  Economy 2.0 removed government subsidies and raised service upkeep, that it
  shipped as `Patch 1.1.5f1` and added tile upkeep from which the first nine
  tiles are exempt, that no later announcement through `1.6.0f1` restores
  subsidies, that Expansion Points remain tracked, that milestones still gate
  unlocks after launch, and that the client now ships an in-game Encyclopedia
  that replaced the Advisor (`CS2-002b`, `CS2-004b`, `CS2-005b`, `CS2-006a`,
  `CS2-018a`, `CS2-018b`, `CS2-023b`, `CS2-024`, `CS2-026`).
- [Observation | Corroborated | Medium] `River Delta`'s identity and
  connections, the starting road catalogue with its tutorial-completion unlock,
  the automatic demand-driven construction, the one-directional pre-terminal
  money flow and the excluded later branches are bounded in `CS2-004c`,
  `CS2-007`, `CS2-009`, `CS2-018c` and `CS2-025`.
- [Observation | Limited | Medium] The build identifier and its link to the
  version label, the starting zone catalogue, the starting utility costs and
  requirements, the road power and pipe capacities, the info views, the
  milestone bar and the milestone gating of the fiscal and service catalogue
  rest on one family each (`CS2-002a`, `CS2-002c`, `CS2-006c`, `CS2-008b`,
  `CS2-010`, `CS2-012b`, `CS2-013b`, `CS2-015`, `CS2-016`, `CS2-027`); the
  first milestone's threshold, award and released list (`CS2-005c`,
  `CS2-006b`) are `Limited | Low` run-time gaps. The official map and utility
  rules plus the muted visual route inspection close the spatial water
  parameter at `Limited | Medium` without promoting it to version proof
  (`CS2-013c`, `CS2-031a`).

## New genes

- [Observation | Limited | Medium] `OBJ-169` isolates crossing the first of a
  continuing subject's declared progression thresholds and keeping what it
  releases, while the subject is not completed and its measure continues.

## New combinations

- [Pattern | Corroborated | High] No new combination ID is registered, and the
  verified `COMB-0269` — one credited progression measure, its accumulated
  successor gate and their shared disclosure — becomes a strict proper subset
  of this signature and gains `GAME-0284` as its third supporting carrier,
  after Forza Horizon 6 and Far Cry 5.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_048` generalises `SYS-169`'s
  compared measure and `TAXONOMY_CHANGE_050` generalises `SYS-517` and
  `CON-440` from completed activity results to any declared qualifying result;
  `TAXONOMY_CHANGE_049` is rejected because widening `CON-179` would have
  duplicated `CON-440`. `GAME-0121`, `GAME-0132`, `GAME-0171` and `GAME-0271`
  keep their wording, carriers and signatures, and no prior signature,
  lifecycle or committed ID changes.

## New questions

- Does an authored survival challenge such as The Long Dark's `Hopeless
  Rescue` need a different Objective boundary from a progression threshold,
  because its subject really is finished when the attempt settles?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0285` — The Long Dark, only under a new
  game-specific prompt after this unit's independent audit.
- Optimisation criterion: replace a construction-and-growth threshold with an
  authored timed challenge that has both completion and failure settlements.
- Expected information gain: separate survival substrate genes from the
  authored challenge objective and its failure boundary.
- Backlog impact: advances the recorded 280-to-288 calibration horizon.

## Why this game

- [Hypothesis | Limited | High] The fourth transfer test had to succeed on a
  direct sequel whose predecessor is already in the corpus, so success depended
  on auditing the first game's entire signature rather than inheriting it, on
  checking the post-launch rework history before trusting any pre-release page,
  and on finding that the sequel's progression belongs to an existing
  cross-genre corridor rather than to the municipal one it superficially
  resembles.
