---
game_id: GAME-0498
slug: transport-fever-2
game_title: Transport Fever 2
analysis_status: reviewed
reviewed: 2026-10-05
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-023
    - ACT-024
    - ACT-130
    - ACT-139
    - ACT-232
    - ACT-341
    - ACT-582
    - ACT-670
    - ACT-671
  system:
    - SYS-030
    - SYS-031
    - SYS-154
    - SYS-736
    - SYS-1351
    - SYS-1352
  constraint:
    - CON-062
    - CON-171
    - CON-282
    - CON-764
    - CON-765
  information:
    - INF-058
    - INF-067
    - INF-268
    - INF-471
    - INF-472
  objective:
    - OBJ-286
  time:
    - TIM-003
---

# Game: Transport Fever 2 — complete launch-day Mining Miracle

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Fleet sizes, prices, track dimensions and arrival quotas are parameters.

## Analysis scope

- Version / ruleset: Windows English base campaign, Chapter I, complete
  Mining Miracle, reconstructed from recordings published 2019-12-11.
  Their publication date anchors the researched release-day ruleset, not a
  verified executable hash or an invented same-day hotfix identifier. The
  official manual and a separately dated preview corroborate qualitative
  rules, not current 2026 or preview/release numerical parity.
- Structured analysis target: existing PLAT-WINDOWS-PC, original English base
  PC release; not console, Deluxe or cross-platform equivalence.
- Primary decision loop: inspect current task, station reach, city needs,
  vehicle capability, load and budget; place eligible facilities and connected
  graded rail, compose purchases, edit ordered lines and allocate vehicles;
  run, pause or accelerate automatic transport, inspect actual deliveries and
  revise capacity/service; accept or decline offered bonus tasks and perform
  their currently eligible interactions before the completed mission result.
- Entry and exit: a fresh mission start at the initial camera/mine-search
  instruction with no player routes or prior medal credits. Include the whole
  tutorial chain, road logs, ore rail, local passengers, intercity passengers,
  all available management alternatives, headquarters placement and all three
  bonus tasks. Exit at Mission Completed with the earned independent medals,
  before choosing Continue Playing or Return to Main Menu. Earlier voluntary
  abandonment does not satisfy success. No unseen bankruptcy terminal or
  compulsory all-medals predicate is invented.
- Included: script-tested camera inspection and vehicle ride, contextual map
  interactions, bonus acceptance/decline, priced facility placement and module
  access, compatible depot/network attachment, paid rail alignment, purchase-
  time locomotive/wagon composition, vehicle purchase and assignment, ordered
  line editing and source-departure waits, automatic typed freight and passenger
  service, current demand, paused/accelerated simulation, recurring finances,
  authored stage gates, mine-sale capital grant, separate arrival counters,
  beast-clue chain, ranch logs and ride medal, and the completed result.
- Excluded: other missions, unrestricted free play after the result, unavailable
  aircraft/ship/tram and later-era assets, Deluxe/DLC, mods, map editor and
  unevidenced direct road/terrain construction outside this mission's restricted
  tools. Later owned-train editing and fractional load-ratio controls added on
  2019-12-19 are not launch rules. No manual driving, wave button, exact payment
  formula, hard Ponderosa countdown, universal terminus requirement or native
  pathfinding/event order is asserted. Cosmetic colour/name choices and file
  administration are not separate genes.
- Potential scoped modules: a later mission, free-play economy, signalling,
  station-overload measurement or a precisely pinned later revision require
  independent entry/terminal evidence.
- Direct-play status: no native game, save, complete shipped mission script or
  executable was run. Actual frames, publication metadata and automatic
  transcripts from two launch-day recordings and an explicitly earlier preview
  were inspected, together with official written rules. Narration is not a
  measured engine trace; generated artwork is not gameplay evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| TF2-001 | The target is Windows English base Mining Miracle under evidenced release-day rules, not a verified build or current whole-product union | Confirmed | Corroborated | High | P1, P2, P4; V1, V3 |
| TF2-002 | Current taught predicates advance the ordered camera, freight and passenger tutorial chain | Observation | Corroborated | High | P3; V1–V3 |
| TF2-003 | Priced facilities, graded track, ordered stops, purchases and assignment have distinct consequences | Observation | Corroborated | High | P5–P7; V1–V3 |
| TF2-004 | Station supply/receiver eligibility follows street-reachable catchment, separate from depot/track/vehicle compatibility | Observation | Corroborated | High | P5; V1, V2 |
| TF2-005 | Assigned compatible carriers load and deliver automatically; capacity and departure policy change service without manual driving | Observation | Corroborated | High | P6; V1–V3 |
| TF2-006 | A completed mining stage grants capital; transport and upkeep affect the company budget without player cargo resale | Observation | Corroborated | High | V1–V3 |
| TF2-007 | Intercity success counts arrivals at Carson City and Reno independently, not all passengers aboard one train | Observation | Direct | High | V1 31:28; V3 14:33, 20:28 |
| TF2-008 | Three optional branches produce separate medals: ride, beast inquiry and ranch logs | Observation | Corroborated | High | P2, P3; V2, V3 |
| TF2-009 | Camera/ride commands can satisfy authored task predicates without steering the train or changing world geometry | Observation | Corroborated | High | P3; V2 19:26–19:56; V3 8:53 |
| TF2-010 | Completed mission exposes earned medals and separate menu-return/continued-play choices | Observation | Direct | High | V2 41:04–42:21; V3 20:28 |
| TF2-011 | Later owned-train editing and fractional load ratios cannot be silently backported to launch day | Confirmed | Direct | High | P4 |
| TF2-012 | A hard ranch timer, wave command, exact native hash and later patch parity remain unverified | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Urban Games, original PC release 2019-12-11.
- Platform or physical form: original Windows English base campaign.
- Puzzle family: persistent route/network construction, reusable programmed
  automation, live-system pressure and ordered dependency sequencing;
  existing boundaries, not a transport-genre family.
- Primary sources, inspected 2026-10-05:
  - **P1:** [Official Steam product](https://store.steampowered.com/app/1066780/Transport_Fever_2/),
    release/platform identity, not a chart or native-version measurement.
  - **P2:** [Official Chapter I manual](https://wiki.transportfever2.com/doku.php?id=gamemanual:campaign:chapter_i),
    first mission and named bonus medals; later documentation.
  - **P3:** [Official mission examples](https://wiki.transportfever2.com/doku.php?id=modding:missions),
    cameraChanged and Ponderosa Accept/Decline excerpts, not the full mission Lua.
  - **P4:** [Official release notes](https://wiki.transportfever2.com/doku.php?id=releasenotes),
    launch-day fixes and 2019-12-19 train-edit/load-ratio additions.
  - **P5:** [Stations and depots](https://wiki.transportfever2.com/doku.php?id=gamemanual:stationsdepots).
  - **P6:** [Lines and vehicles](https://wiki.transportfever2.com/doku.php?id=gamemanual:linesvehicles).
  - **P7:** [Streets and tracks](https://wiki.transportfever2.com/doku.php?id=gamemanual:streetstracks).
    P5–P7 corroborate observed operation; later menus are screened against P4.
- Recorded primary gameplay, not native personal play:
  - **V1:** [Trophygamers](https://www.youtube.com/watch?v=7gDvzbT3Zaw),
    published 2019-12-11, 34:58; main chain, current state and beast/log branches.
  - **V2:** [MontePlaysGames](https://www.youtube.com/watch?v=W-YzIYjaTKw),
    published 2019-11-27, 42:42; explicitly pre-release, all alternatives and
    three-medal result. Its later guide date is not the footage date.
  - **V3:** [Sin's Gaming Channel](https://www.youtube.com/watch?v=iIFbKqNT21g),
    published 2019-12-11, 20:33, linked by
    [Sin317's Chapter I guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1934681780).
    Actual 8:53, 14:33, 14:52 and 20:28 frames establish ride credit,
    bonus offer/acceptance and the three-medal completed result.
- **R1:** [Complete dated packet and counterexamples](../../../research/checkpoints/TRANSPORT_FEVER_2_SCOPE_001.md).
  Automatic transcripts are narration aids, not independent sources. An
  unavailable later video and title-only metadata were not admitted as proof.
- Claim IDs: TF2-001–TF2-012.

## Mechanical decomposition

### Action Genes

- Existing ACT-006/023/024/130/139/232/341/582: accelerated time, ordered
  service editing, vehicle allocation, purchase, service-site placement,
  offered task response, contextual map target and priced rail geometry.
  Ordinary facility categories include depot, station and optional headquarters;
  module/footprint settings are parameters, not new named-building genes.
- New ACT-670: a view command is causal where a script explicitly tests it;
  a ride view does not become direct control or Echochrome projection physics.
- New ACT-671: choose powered unit and eligible wagons before committing the
  purchase. This is not ACT-584's per-stop consist substitution or a later
  existing-train editing menu.
- Claim IDs: TF2-002–TF2-005, TF2-008, TF2-009, TF2-011.

### System Behaviour Genes

- Existing SYS-030/031/154/736: autonomous waiting passenger demand,
  configured passenger service, recurring budget and predicate-led teaching.
- New SYS-1351: typed source-to-receiver freight carriage with finite current
  load, not ownership trading, distribution-office dispatch or fuel simulation.
- New SYS-1352: fulfilled authored tasks apply declared one-time grants or
  independent bonus credits. Guidance reveal and reward application are
  distinct; accepting a bonus is not already earning its medal.
- Resolution order: a legal build/purchase/assignment changes the persistent
  network/fleet; running time evolves demand, movement, loading and deliveries;
  actual eligible predicates change guidance, budget/rewards and finally the
  mission result. This is qualitative causality, not recovered engine ordering.
- Claim IDs: TF2-002–TF2-010.

### Constraint Genes

- Existing CON-062/171/282: compatible fixed facility footprint, sufficient
  managed construction/operating budget and ordered authored prerequisites.
  Allowed paid demolition is a footprint exception, not universal overlap.
- New CON-764: compatible mode, depot access, connected service path,
  terminal and vehicle capability; no unobserved player fuel supply.
- New CON-765: street-reachable station service admits local demand/supply.
  Circular radius and track adjacency alone are counterexamples, not an
  unchanged transfer of CON-721.
- Claim IDs: TF2-003–TF2-007.

### Information Genes

- Existing INF-058/067/268: itemised recurring ledger, visible task terms and
  the current tested tutorial instruction. INF-067's deadline field applies
  only where disclosed; Ponderosa does not establish a numeric clock.
- New INF-471: prospective cost, facility reach and train-purchase capability.
- New INF-472: current line, destination, load, waiting demand and separately
  credited arrival progress. Capacity is not an already settled task counter.
- Claim IDs: TF2-002–TF2-008, TF2-012.

### Objective Genes

- New OBJ-286: complete the authored freight/passenger chain and settle its
  independent bonus credits. The final pair of city-arrival predicates is not
  a first-payment terminal, exhaust-all-passengers objective or one pooled quota.
- Main completion does not require earning every optional medal. Voluntary
  earlier abandonment is not success; unseen insolvency endings are not asserted.
- Claim IDs: TF2-007, TF2-008, TF2-010, TF2-012.

### Time Genes

- Existing TIM-003: carriers and demand evolve on live time while management
  decisions remain available. Pause and selectable speed are parameters.
  No separate hard ranch deadline is established by hurry narration.
- Claim IDs: TF2-005, TF2-012.

## Reproducible transitions

| Before | Action | Resolution | Decision boundary | Claim ID |
|---|---|---|---|---|
| Current initial camera instruction | Reframe the map | Script acknowledges its view predicate and exposes the next task | Inspection is causal here, not world rotation | TF2-002, TF2-009 |
| No cargo service | Place compatible facilities, create stops, buy carts and assign | Running carts repeatedly load eligible logs and deliver them | Building a line alone supplies no vehicle | TF2-003–TF2-005 |
| Station near an industry but street access insufficient | Change legal placement or access modules | Eligible highlighted reach changes | Nearby rail does not itself admit cargo | TF2-004 |
| Connected rail and depot, no carrying capacity | Compose locomotive and freight cars, buy and assign | Physical freight service gains eligible capacity | Engine purchase is not passenger/cargo equivalence | TF2-003, TF2-005 |
| Loading cart on a repeating source line | Choose full-load departure, or depart with available load | Departure timing/current carried amount differs | Wait policy is not another ordered line or a hard mission deadline | TF2-005, TF2-012 |
| Bonus ride offered | Accept, then enter freight vehicle ride view | Enjoy a ride credit is earned | No wave input or steering authority is invented | TF2-008, TF2-009 |
| Beast inquiry accepted | Address reporter, saloon, ranch and lake clues in their exposed order | Hoax resolution earns Monstrous beast | Skipping the bonus does not satisfy its medal | TF2-008 |
| Ponderosa offer alongside unfinished city counters | Accept or decline; on acceptance supply additional ranch logs | Independent bonus progress/credit differs | Hurry prose does not prove a countdown | TF2-008, TF2-012 |
| Intercity train has passengers aboard | Continue to an eligible destination | That city's arrival counter progresses | Onboard load is not already credited arrival or the other city's quota | TF2-007 |
| Required tutorial chain complete | Settle the result | Mission Completed exposes independently earned medals and continued-play/menu choices | Whole free-play economy is outside the terminal | TF2-010 |

These are source-reproducible qualitative transitions, not a native test run.

## Strategic and experiential structure

- Local decisions separate reach, compatible cargo capability and sufficient
  capacity; price/capacity feedback precedes commitment.
- Medium-term revision separates physical geometry from stop order and fleet
  assignment. Extra carts or wagons are not automatically useful if reach fails.
- Pause/fast time manages observation cost, not direct train control.
- Optional medal commitments coexist with the main chain; their distinct
  interaction and freight requirements explain why one successful delivery
  cannot stand for the complete mission.
- Player-trust factors: distinguish present load from credited arrivals,
  disclose version/source limitations and do not turn narrative urgency into
  an undocumented loss timer.
- Claim IDs: TF2-003–TF2-012.

## Replay and variation

- The authored map/tasks persist; construction alignment, station/module
  choices, fleet sizes, consist and service timing vary.
- No exact seed, demand distribution, queue-priority formula or native
  pathfinding result is claimed. Restarting the mission is a new packet.
- Better capacity and earlier optional commitment can alter the visible
  service/result without creating a different campaign branch ending.
- Claim IDs: TF2-003–TF2-012.

## Adjacent systems and history

- Railroad Tycoon II's first-paid-delivery scope has different ownership,
  catchment and per-stop consist assumptions; it is not borrowed wholesale.
- Current manuals describe later functionality; P4 identifies explicit
  additions that must not silently enter this release-day genome.
- Unrestricted signals, newer vehicles and later campaign economy remain
  possible scoped modules, not features inferred merely from the product.
- Claim IDs: TF2-001, TF2-004, TF2-011, TF2-012.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-006, ACT-023, ACT-024, ACT-130, ACT-139, ACT-232, ACT-341, ACT-582, ACT-670, ACT-671 | Counts, prices, orientations, view and purchase choices |
| System Behaviour | SYS-030, SYS-031, SYS-154, SYS-736, SYS-1351, SYS-1352 | Demand, finite load, intervals and authored reward flags |
| Constraint | CON-062, CON-171, CON-282, CON-764, CON-765 | Footprint, solvency, predecessor and reach parameters |
| Information | INF-058, INF-067, INF-268, INF-471, INF-472 | Current/preview field representation |
| Objective | OBJ-286 | Separate city-arrival quotas and earned medals |
| Time | TIM-003 | Live simulation, pause and speed |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `497` (`GAME-0001`–`GAME-0497`).
- Exact genome matches: none.
- Tied near matches: `GAME-0121` — Cities: Skylines (`7 / 44 = 0.159091`).
- Supported combination subsets: none.
- Scan date: 2026-10-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0121` Cities: Skylines | ACT-006/023, SYS-031/154, CON-171, INF-058, TIM-003: simulation acceleration, ordered transit, automatic passenger movement, recurring finances, paid operation, ledger and live time | The city packet includes municipal zoning, utilities and service funding. Mining Miracle instead has street-reachable typed freight, depot/consist compatibility, taught staged predicates, one-time mine-sale grant and three independent bonus commitments before mission settlement; it does not silently inherit fuel management or the city's whole growth loop. | Near, `0.159091` |

### Preserved research notes

- New genes: ACT-670/671, SYS-1351/1352, CON-764/765, INF-471/472, OBJ-286.
- Classification result: New gene.
- Evidence and reasoning: nine separate command, resolution, eligibility,
  information and settlement boundaries; nineteen unchanged transfers.
  No external novelty or recurring-combination claim follows from one carrier.

## Taxonomy impact

- Registry changes: the nine reviewed additions listed above; no previous
  signature or English definition change.
- Taxonomy-change record: TAXONOMY_CHANGE_235, complete release-day mission.
- Candidate terms affected: none; artwork and generic transport theme are
  not candidate gene names.

## Negative results

- No new standalone negative-result ID. Rejected unchanged transfers and
  source/version counterexamples are recorded in R1 and this unit's taxonomy
  review; they do not silently mutate earlier records.

## Delta summary

This English record owns researched facts and boundaries. Ukrainian public
research presentation is generated from the separately reviewed locale layer.

## New facts

- [Observation | Corroborated | High] Complete release-day Mining Miracle
  joins compatible transport construction, automatic service and independent
  bonus decisions before the mission result; TF2-002–TF2-010.
- [Confirmed | Direct | High] 2019-12-19 train-edit/load-ratio additions and
  unobserved hard deadlines are not release-day evidence; TF2-011, TF2-012.

## New genes

- [Observation | Corroborated | High] ACT-670/671, SYS-1351/1352,
  CON-764/765, INF-471/472 and OBJ-286; source and counterexample boundaries
  above, without a claimed external discovery.

## New combinations

- [Observation | Corroborated | High] No new combinations; no verified proper
  subset applies and one new carrier does not establish recurrence.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_235 records this
  complete packet and nine additions without prior signature changes.

## New questions

- [Hypothesis | Limited | Medium] What native launch binary implements the
  inspected recordings, and what exact completion cutoff affects Ponderosa?
  These questions do not justify a fabricated build or timer gene.
- [Hypothesis | Limited | Medium] Which independent transport packet reuses
  street-reachable catchment and purchase-time consist without refuelling?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0499 Vagrant Story, original English
  PlayStation, follows only after this unit's complete acceptance and commit.
- Optimisation criterion: preserve Selection 039's mixed-era/platform order.
- Expected information gain: position/equipment and chained attack decisions
  contrast with persistent transport infrastructure.
- Backlog impact: no later unit is started while GAME-0498 is incomplete.

## Why this game

- [Hypothesis | Limited | High] The approved replacement preserves transport
  research and the modern/retro balance while providing a fully evidenced
  released mission rather than admitting an incomplete prospective product.
