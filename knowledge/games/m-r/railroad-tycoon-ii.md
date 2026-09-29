---
game_id: GAME-0446
slug: railroad-tycoon-ii
game_title: Railroad Tycoon II
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-130
    - ACT-582
    - ACT-583
    - ACT-584
    - ACT-585
  system:
    - SYS-266
    - SYS-1170
    - SYS-1171
  constraint:
    - CON-171
    - CON-237
    - CON-721
  information:
    - INF-058
    - INF-430
    - INF-431
  objective:
    - OBJ-255
  time:
    - TIM-003
---

# Game: Railroad Tycoon II — first Tutorial railway service

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Slough, Oxford, wool and the Eight-Wheeler are parameters of the manual's suggested Tutorial route, not universal railway genes.

## Analysis scope

- Version / ruleset: the original English 1998 Windows PC *Railroad Tycoon II* Tutorial saved scenario described by its contemporary printed manual. The exact CD-ROM revision was not inspected. *Second Century*, Platinum additions and later ports are excluded.
- Primary decision loop: found a funded railway company; compare source and destination on the resource map; pay to build a connected, graded single track and stations whose coverage reaches the relevant suppliers and consumers; buy a locomotive, assign an ordered itinerary with cargo/passenger consist and per-stop departure rules; let the train carry eligible traffic; inspect transport revenue and the separate corporate and personal accounts; revise the route or timetable if service is unprofitable.
- Entry: load the original Tutorial save before founding the company. The manual's example starts near Slough and Oxford; supply positions can vary between plays, so the sampled positions must be verified on the loaded map rather than assumed fixed.
- Positive terminal for this bounded packet: the new railway has completed its first paid eligible delivery from the origin station to the destination station and the corporate ledger shows the resulting transport income. The itinerary is programmed to return, but a wool-to-goods conversion and paid goods return are not required for this checkpoint: the manual warns that goods might not be available on the first return.
- Local failure / revision state: disconnected track, a station outside a producer's or receiver's radius, an unsuitable consist, an unreachable stop or inadequate company cash can prevent the paid delivery. These call for construction or schedule repair; they are not a declared Game Over for the Tutorial.
- Wider scenario objective: grow **personal**, not corporate, net worth (personal cash plus stock holdings) to at least $10 million by 1900; $25 million and $50 million are higher award tiers. This long-horizon goal frames why company equity matters but is not claimed as attained by the first-delivery checkpoint.
- Included: company founding with personal/outside capital and ownership split; resource/demand and construction previews; priced rail segments, bridge/grade trade-offs, two track-connected stations and coverage; water/sand/roundhouse services as Tutorial station upgrades; a purchased 4-4-0 Eight-Wheeler; ordered Slough–Oxford stops, consist and green/yellow/red departure rules; automatic movement, pickup and delivery; wool supplied by sheep, textile conversion to goods when available; transport revenue, corporate ledger, personal portfolio, pause and speed controls.
- Excluded: the remainder of the $10 million campaign, hostile takeovers, complex stock trading and bonds, additional railroads, later scenarios, expert-only dynamic market pricing, fixed claims about randomized resource locations, detailed economic arithmetic, accidents, track signalling beyond this route, a guaranteed goods car on the first return, and Platinum expansion rules.
- Reproducible source-derived route: load Tutorial; inspect the resource overlay; fund a company; join the sheep-serving Slough area to Oxford by one grade-aware track; place stations aligned to track and verify catchment; buy the Eight-Wheeler; set Slough to take one wool and one passenger car with yellow departure, Oxford to carry passengers and goods with green departure; run until a qualifying delivery pays, then compare the company ledger and personal portfolio. This is a manual reconstruction, not an executed play trace.
- Potential scoped modules: sustained service profitability, multi-train signalling, economic-stock strategy, the full $10 million scenario and expert market settings require separate evidence and terminals.
- Direct-play status: no original disc, executable, save state, input capture, video, audio or game session was inspected. Rules and suggested route derive from the original publisher/developer manual; exact starting supply layout, first-arrival load, payment values and travel times remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RRT-001` | Tutorial starts from a saved scenario and separately targets $10 million personal net worth by 1900, with higher tiers. | Observation | Direct | High | P1 |
| `RRT-002` | The resource map exposes supply and demand; positions vary by play, so the manual's named route is an example. | Observation | Direct | High | P1 |
| `RRT-003` | Company founding can combine the player's investment with outside investors, changing corporate cash and personal share ownership. | Observation | Direct | High | P1 |
| `RRT-004` | Dragged track has priced segments, bridges and grades; a less direct grade can improve train service. | Observation | Direct | High | P1 |
| `RRT-005` | A station must be placed on track and its service radius must cover the intended industries or houses. | Observation | Direct | High | P1 |
| `RRT-006` | The suggested route buys an Eight-Wheeler, adds station services and programs Slough/Oxford stops with per-stop consist and wait lights. | Observation | Direct | High | P1 |
| `RRT-007` | Trains execute the programmed stop sequence, load eligible traffic and resolve paid deliveries; the first goods return is not guaranteed. | Observation | Direct | High | P1 |
| `RRT-008` | Sheep supply wool, textile receivers can turn delivered wool into goods, and towns demand goods. | Observation | Direct | High | P1 |
| `RRT-009` | Railroad income is payment for transport, not purchase and resale of the cargo; amount depends on demand, distance, speed and cargo class. | Observation | Direct | High | P1 |
| `RRT-010` | Corporate accounts/ledger and personal cash/share portfolio are distinct visible financial states. | Observation | Direct | High | P1 |
| `RRT-011` | The Tutorial may pause and resume at accelerated simulation speed. | Observation | Direct | High | P1 |
| `RRT-012` | No direct PC play or measured route/payment trace was performed for this packet. | Confirmed | Direct | High | R1 |

## Basic data

- Origin: PopTop Software's 1998 *Railroad Tycoon II* for PC; the [official Steam product page](https://store.steampowered.com/app/7620/Railroad_Tycoon_II_Platinum/) identifies the title and later Platinum bundle but does not supply separate original-Tutorial rule evidence.
- Platform: original English Windows PC rules as printed. Mouse interaction, station names, capital values and rolling-stock model are scoped parameters.
- Mechanical families: route/network construction (`FAM-005`) and automation/spatial programming (`FAM-008`).
- **P1:** [Original *Railroad Tycoon II* manual, digitised text](https://manualzilla.com/doc/5757182/railroad-tycoon-ii%C2%A9), inspected 2026-09-28: Tutorial chapter on save, goal, resources, founding, track/stations/train/consist/ledger; Railroading, Running Trains and Finances chapters on catchment, industry, transport payments, schedule loops and separate equity. The digitised publisher artefact is rules evidence, not a gameplay capture or image source.
- **R1:** local preflight found no original disc, executable or direct-play trace in this unit.
- Claim IDs: `RRT-001`–`RRT-012`.

## Mechanical decomposition

### Action Genes

- `ACT-585` founds a railway company with chosen personal and outside capital. This creates a corporate treasury and allocates ownership; it is neither a freight payment nor a mere UI selection.
- `ACT-582` lays connected priced rail with a chosen grade and bridge path. A shorter steep climb can cost service performance even if cheaper to lay.
- `ACT-583` places a track-aligned station with chosen size/catchment; water, sand and roundhouse upgrades support service rather than adding new route endpoints.
- Reuse `ACT-130` for purchasing the offered locomotive. `ACT-584` configures ordered train stops, per-stop cargo/passenger consist and departure wait light; changing this is different from editing the physical track.
- Reuse `ACT-006` for accelerating the running simulation; pause is a time-mode parameter.

### System Behaviour Genes

- Reuse `SYS-266`: an assigned train autonomously traverses its connected rail service, stops, picks up allowed traffic and may need station facilities. One purchased train and one loop suffice; no manual driving is asserted.
- `SYS-1170` turns delivered wool into goods at an eligible textile industry when output becomes available. This is not an instantaneous guaranteed first-return load.
- `SYS-1171` settles a completed transport into company revenue according to cargo class, demand, distance and speed. The railroad is paid to convey, not to own/trade, the wool or passengers.

### Constraint Genes

- Reuse `CON-171` for company cash versus track, station, train and operating expenditure. Reuse `CON-237` for a mode-compatible continuous rail path and usable station/facility service.
- `CON-721` requires a station's displayed catchment to contain a supplier or receiver for that local cargo to enter service. Merely passing track beside sheep or a textile mill is insufficient.

### Information Genes

- `INF-430` exposes present resource supply/demand, proposed route grade/cost and station catchment before committing. It does not disclose an immutable future goods stock.
- Reuse `INF-058` for the itemised railway-company income, costs and treasury. `INF-431` separately exposes the founder's personal cash, shares and net worth, avoiding the mistaken equation of company cash with scenario progress.

### Objective and Time Genes

- `OBJ-255` names the local acceptance outcome: establish a working railway and obtain one paid eligible delivery, then inspect the ledger. The $10 million personal target remains a disclosed, explicitly out-of-packet scenario objective.
- Reuse `TIM-003`: once unpaused, vehicles, industrial supply and finances progress while the player can edit the railway. Pausing and fast-forwarding alter the rate, not the underlying rule.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Tutorial loaded, no company | Commit personal and outside investment | Corporate cash is funded; personal equity reflects investor split | Personal and company money are not identical | `RRT-003` |
| Two candidate paths, one steep | Preview and lay the connected lower-grade alternative | Paid rail network reaches the destination with a different grade | Geometry changes both build cost and service | `RRT-004` |
| Track passes near sheep but no station | Put an aligned station where its radius covers sheep | Wool becomes eligible for pickup at that stop | Track proximity alone does not collect cargo | `RRT-005` |
| Connected stations, no train | Buy Eight-Wheeler; set ordered stops and consist | A programmed vehicle begins cyclic station service | Construction and itinerary are distinct controls | `RRT-006`, `RRT-007` |
| Train at Slough with wool available | Load one wool car and carry it to accepting Oxford textile | Eligible delivery produces railway transport revenue; textile may later make goods | The paid leg establishes local success | `RRT-007`–`RRT-009` |
| Train returns before goods are ready | Continue service without a goods load | No fictional first-return goods payment is credited | Production availability is a separate gate | `RRT-007`, `RRT-008` |
| Delivery paid | Open company ledger, then personal portfolio | Company revenue is visible; personal net worth remains separate | Scenario target cannot be inferred from one freight payment | `RRT-009`, `RRT-010` |

## Strategic and experiential structure

The first decision is not simply shortest rail: available company capital, grade, station radius, industrial demand, consist and departure policy jointly determine whether a running train can earn. A yellow wait at Slough can allow partial loading; green at Oxford prevents waiting for goods that may not yet exist. The longer scenario then asks the founder to translate corporate service into personal share value, but this packet stops at its first verified paid service. Resource locations, precise costs and revenue are parameters rather than copied constants.

## Replay and variation

The resource map may shift sheep and demand positions between Tutorial loads; track grade, station size, funding split, assigned cars and wait lights produce different costs and first-trip earnings within the same source-described rules. An empty first goods return is a documented permitted outcome, not evidence of a broken route.

## Adjacent systems and history

*Mini Metro* also builds transit service, but its player edits abstract lines between system-created stations and optimises passengers against overcrowding; *Railroad Tycoon II* buys physical graded rail, places catchment stations, configures train consist and settles freight revenue through corporate accounts. The original 1998 PC Tutorial is distinct from Platinum's expansion and later ports.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-130`, `ACT-582`, `ACT-583`, `ACT-584`, `ACT-585` | speed, train purchase, rail, station, itinerary, equity |
| System Behaviour | `SYS-266`, `SYS-1170`, `SYS-1171` | scheduled service, textile output, transport payment |
| Constraint | `CON-171`, `CON-237`, `CON-721` | solvency, rail/facility compatibility, catchment |
| Information | `INF-058`, `INF-430`, `INF-431` | company accounts, spatial preview, personal portfolio |
| Objective | `OBJ-255` | first paid company delivery, not full scenario victory |
| Time | `TIM-003` | running simulation, with pause and speed controls |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `445` (`GAME-0001`–`GAME-0445`).
- Exact genome matches: none.
- Tied near matches: `GAME-0118` — SimCity 4 Deluxe Edition (`4 / 29 = 0.137931`); `GAME-0390` — SimCity 2000 (`4 / 29 = 0.137931`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0118` — SimCity 4 Deluxe Edition | `ACT-006`, `CON-171`, `INF-058`, `TIM-003` | Both can accelerate a solvent live managed domain and inspect its ledger. The city zones services and observes population, whereas the railroad funds graded rail, covers industries with stations, schedules wagon cargo and earns paid carriage separately from personal equity. | Tied nearest at `4 / 29 = 0.137931`; not the same transport loop. |
| `GAME-0390` — SimCity 2000 | `ACT-006`, `CON-171`, `INF-058`, `TIM-003` | City growth, tax and utility zoning do not author a particular train's per-stop consist or make a station radius admit wool to an industry; neither corporate rail freight nor founder share ownership is the city's local terminal. | Tied nearest at `4 / 29 = 0.137931`; not the same financial objective. |

## Taxonomy impact

`TAXONOMY_CHANGE_183` admits ten source-supported boundaries without revising prior game signatures or combinations.

## Negative results

- Do not equate company treasury with personal net worth.
- Do not assume fixed sheep placement, a guaranteed goods return, expert dynamic prices or an automatic Tutorial victory after one delivery.

## Delta summary

## New facts

- [Observation | Direct | High] Station catchment and a physical rail connection jointly gate the first Tutorial pickup and delivery (`RRT-004`–`RRT-007`).
- [Observation | Direct | High] Company transport income and the founder's personal scenario target are distinct financial states (`RRT-009`, `RRT-010`).

## New genes

- [Observation | Direct | High] Ten typed boundaries distinguish founding, route construction, station coverage, itinerary, industrial transformation, revenue and dual financial visibility.

## New combinations

- [Observation | Limited | Medium] None proposed; existing proper-subset support is recomputed.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_183`; no earlier signature is changed.

## New questions

- Would direct original-CD play measure the randomized starting supply positions, first-trip cargo and ledger values without changing the documented catchment and payment rules?

## Next game

`GAME-0447` *Punch-Out!!* is the next selected unit only after this unit's acceptance and Goal stop window. No push, public publication or deployment is authorised.
