---
game_id: GAME-0196
slug: farming-simulator-25
game_title: Farming Simulator 25
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0194
gene_ids:
  action:
    - ACT-201
    - ACT-351
    - ACT-352
  system:
    - SYS-320
    - SYS-629
    - SYS-630
    - SYS-631
  constraint:
    - CON-288
    - CON-515
    - CON-516
  information:
    - INF-067
    - INF-252
    - INF-253
  objective:
    - OBJ-119
  time:
    - TIM-003
---

# Game: Farming Simulator 25

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam base game `1.21.1.0`,
  public build `24466285`, checked 2026-08-29; one single-player **New Farmer**
  save on **Riverbend Springs** and one standard **Fertilizing** contract using
  the employer's borrowed items. The reviewed official product title remains
  **Farming Simulator 25**.
- Reproducible start packet: create a fresh New Farmer save on Riverbend
  Springs with base-game defaults, no downloadable content or mods, open the
  Contracts screen and accept the first currently available Fertilizing offer
  after sorting first by field number and then by displayed reward. Choose
  `Borrow Items`; exact field, farmer, reward, borrowing fee, tractor and
  spreader are sampled offer parameters, not additional genes.
- Primary decision loop: compare the disclosed target field, reward and
  borrowing deduction; accept and collect the spawned equipment at the shop;
  enter the supplied tractor, align and attach the compatible filled spreader;
  drive to the marked field; lower/activate the tool and steer overlapping
  passes from the visible working width, fill and fertilized state; stop waste
  outside the target; reach the contract's accepted coverage threshold; return
  to Contracts and collect the settled net payment.
- Entry and exit: begins on the fresh save's Contracts screen before one
  eligible offer is accepted. It succeeds only after the assigned field reaches
  the contract completion threshold and `Collect` converts the completed offer
  into credited money while closing the active contract and removing or
  releasing its borrowed equipment. Cancel, exhaust the supplied material
  without finishing, or leave the target untreated are non-completion states.
- Included: the sampled Fertilizing offer; field number and owner; gross reward
  and borrowing deduction; supplied tractor and solid-fertilizer spreader;
  shop spawn and vehicle entry/exit; three-point or declared compatible hitch;
  attach/detach, lower/raise and activate/deactivate tool controls; direct
  steering, throttle, braking and camera; working width and overlap; material
  fill; only the assigned field's current crop/soil and fertilized coverage;
  live time, helper-free manual work, completion progress, collection and net
  account credit.
- Excluded: every own-field crop cycle; cultivating, sowing, harvesting,
  baling, forestry, animals, rice, productions and construction projects;
  seasonal optimisation, sleeping and multi-year finance; AI workers and GPS
  steering; buying, leasing, configuring or repairing equipment; land purchase,
  loans, passive income and farm expansion; multiplayer, crossplay, ModHub,
  mods, Precision Farming, DLC, expansions and downloadable machine packs;
  other maps, modes or contracts; repeat farming after the first settlement.
- Potential scoped modules: one complete owned-field crop cycle; a harvesting
  contract with transport and delivery; one AI-worker field task; Precision
  Farming variable-rate treatment; a multiplayer farm; or one construction
  project. Each needs its own assets, state transitions and terminal.
- Direct-play status: no authenticated Windows Steam run was conducted. The
  current official manual and Academy directly establish New Farmer,
  Riverbend Springs, changing contract offers, borrowed-item fees and shop
  spawn, equipment attachment, field/crop/fertilization state, spreader
  requirements and contract reward presentation. Public-branch metadata pins
  only the build identifier. The completion trace is evidence-based rules
  reasoning, not captured direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FS25-001` | Base-game update 1.21.1.0 / public build 24466285 is the current reviewed Windows Steam ruleset | Confirmed | Corroborated | High | P1, P2, S1 |
| `FS25-002` | New Farmer supplies beginner machinery and Riverbend Springs is an official base environment | Confirmed | Direct | High | P3, P4, P5 |
| `FS25-003` | The Contracts screen presents changing jobs and permits either owned machines or employer items for a displayed borrowing fee | Confirmed | Direct | High | P3, P4 |
| `FS25-004` | Borrowed contract machines appear at the local shop and remain bound to the accepted field job | Confirmed | Direct | High | P4 |
| `FS25-005` | The player enters and steers the tractor, attaches/detaches a compatible tool and controls its working state | Confirmed | Direct | High | P3, P4 |
| `FS25-006` | Solid fertilizer requires a spreader and an eligible field can receive two fertilization stages separated by crop growth | Confirmed | Direct | High | P4, P6 |
| `FS25-007` | Field information exposes owner, crop, growth, yield bonus and fertilized percentage while map filters expose crop, growth and soil-composition state | Confirmed | Direct | High | P7 |
| `FS25-008` | Powered spreader coverage consumes fill and persistently changes the compatible target field's fertilized state | Observation | Corroborated | High | P3, P4, P6, P7 |
| `FS25-009` | Contract UI discloses task, field, farmer, reward, borrow choice and progress needed to decide acceptance and completion | Confirmed | Direct | High | P3, P4 |
| `FS25-010` | Completing and collecting the one accepted contract credits its post-borrowing payment and closes the supplied-equipment job | Observation | Corroborated | Medium | P3, P4, V1 |
| `FS25-011` | Contract identity and reward may vary while the Fertilizing acceptance, coverage and settlement rule remains reproducible as a typed packet | Observation | Direct | High | P4, P6, P7 |
| `FS25-012` | The repository trace stops at one collected contract rather than treating open-ended farm continuation as a terminal | Observation | Direct | High | P1–P7, S1, V1 |

## Basic data

- Release / origin: developed and published by GIANTS Software; released 12
  November 2024 and maintained through the official 2026 update line.
- Platform or physical form: Windows Steam single-player farming simulation;
  only the base-game Riverbend Springs New Farmer contract packet is asserted.
- Puzzle family: physics and object manipulation; resource, logistics and
  optimisation; real-time system pressure.
- Primary and official sources:
  - **[P1]** [official Farming Simulator 25 updates](https://www.farming-simulator.com/updates.php),
    for update `1.21.1.0`, its 2026-07-30 date and automatic current-version
    policy.
  - **[P2]** [official 1.21.1.0 changelog](https://farming-simulator.com/changelogs/fs25.php),
    for the current base-game patch boundary.
  - **[P3]** [official Farming Simulator 25 base-game manual](https://manuals.giants-software.com/Farming_Simulator_25/Basegame/lang/en/FS25-manual_EN.pdf),
    especially controls, New Farmer/maps, finances/contracts, field machines,
    field work, equipment and the illustrated Fertilizing contract offer.
  - **[P4]** [official Academy: How to Start & First Machines](https://www.farming-simulator.com/newsArticle.php?news_id=286),
    for changing contract availability, borrowing fee and shop spawn, beginner
    machinery, tractor/tool coupling and spreader purpose.
  - **[P5]** [official Riverbend Springs preview](https://www.farming-simulator.com/newsArticle.php?campaignIndex=4&country=gb&lang=en&news_id=550),
    for the selected base-game environment.
  - **[P6]** [official Academy: Fertilizing](https://www.farming-simulator.com/newsArticle.php?news_id=292),
    for solid-fertilizer spreaders, material variants and fertilization stages.
  - **[P7]** [official Academy: Introduction to Fields](https://www.farming-simulator.com/newsArticle.php?news_id=290),
    for owner, crop, growth, yield, fertilized percentage and map-layer state.
- Secondary build metadata:
  - **[S1]** [public Steam app-info metadata](https://api.steamcmd.net/v1/info/2300320),
    for public build `24466285` and its 2026-07-30 timestamp only.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P7` and `S1`; rules reasoning, not a direct-play claim.
- Claim IDs: `FS25-001`–`FS25-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-201`: enter, exit and directly steer the supplied contract
  tractor through throttle and braking rather than dispatching an autonomous
  carrier.
- New `ACT-351`: accept the selected Fertilizing offer and commit its displayed
  borrowed-item fee so the job supplies the required fleet.
- New `ACT-352`: align and couple the compatible spreader, raise/lower it and
  activate/deactivate its field-working state while operating the tractor.
- Parameters: offer ordering, field, owner, tractor, tool, hitch, steering,
  throttle, brake, fill, activation, working width and camera.
- Claim IDs: `FS25-003`–`FS25-006`, `FS25-009`.

### System Behaviour Genes

- Existing `SYS-320`: integrate direct tractor steering, acceleration, braking,
  wheel/terrain contact and collision response; combat damage parameters are
  inactive in this non-combat field packet.
- New `SYS-629`: instantiate one accepted field contract, spawn its borrowed
  compatible machinery at the shop and retain target field, reward, deduction
  and active progress.
- New `SYS-630`: resolve the active filled implement's working-width footprint
  over eligible field cells, consume fertilizer and persist accepted coverage
  into the field's fertilized state and contract progress.
- New `SYS-631`: when enough assigned-field coverage is accepted, expose the
  completed contract and on collection remove/release borrowed items, subtract
  the declared borrowing cost and credit the net reward.
- Resolution order: accept and instantiate contract; enter and couple the
  supplied fleet; integrate vehicle/tool motion; intersect active working width
  with eligible target-field state; consume fill and update treatment/progress;
  on threshold mark complete; on explicit collection settle money and close
  the job.
- Parameters: vehicle pose, tool footprint, target-field mask, application
  rate, fill amount, treated cells, overlap, progress threshold, gross reward,
  fee, net credit and borrowed-item disposition.
- Claim IDs: `FS25-003`–`FS25-010`.

### Constraint Genes

- Existing `CON-288`: tractor control requires a viable driver seat, operating
  machine and traversable field/road geometry; an exposed fuel parameter is not
  decision-relevant inside the one short contract.
- New `CON-515`: field treatment is legal only when tractor power, hitch,
  implement type, remaining compatible fill, activation state and assigned
  field/crop state all admit the operation.
- New `CON-516`: contract completion requires accepted treatment coverage of
  the assigned field; work outside it, inactive passes and redundant overlap
  cannot substitute for the remaining eligible area.
- Scarce strategic resources: working time, turning space, fertilizer fill,
  clean working-width coverage and expected net reward after borrowing.
- Claim IDs: `FS25-004`–`FS25-010`.

### Information Genes

- Existing `INF-067`: the contract view discloses the required field task and
  promised reward before commitment.
- New `INF-252`: field and vehicle views expose owner, crop/growth, fertilized
  state, active tool, fill level and working controls needed to plan each pass.
- New `INF-253`: contract views expose the selected farmer, field, task,
  borrowing choice/cost, completion progress and collectable reward state.
- Claim IDs: `FS25-003`, `FS25-006`–`FS25-010`.

### Objective Genes

- New `OBJ-119`: accept, manually finish and collect one borrowed-equipment
  Fertilizing contract on Riverbend Springs.
- Success, evaluation and failure: accepted target coverage followed by
  explicit reward collection is the positive terminal. Inefficient overlap or
  borrowing changes economic evaluation without creating another objective.
  Cancellation or unfinished/exhausted work closes or strands the attempt
  without the asserted completion; the farm save itself remains playable.
- Claim IDs: `FS25-003`, `FS25-008`–`FS25-012`.

### Time Genes

- Existing `TIM-003`: vehicle motion, tool application, live contract state and
  the world clock advance continuously while field-driving input remains
  available. Sleeping, fast time, seasons and multi-cycle crop growth are
  excluded from this short accepted contract.
- Claim IDs: `FS25-003`, `FS25-005`, `FS25-008`–`FS25-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh default New Farmer save is active on Riverbend Springs | Open Contracts and sort eligible Fertilizing offers by field then displayed reward | The first matching current offer exposes farmer, field, reward and borrow choice; identity may vary but the typed packet is fixed | reproducible dynamic-offer selection | `FS25-002`, `FS25-003`, `FS25-009`, `FS25-011` |
| Selected Fertilizing offer is uncommitted | Choose Borrow Items and accept | The borrowing deduction is committed, one active target field is retained and its compatible tractor/spreader appear at the shop | supplied one-contract boundary | `FS25-003`, `FS25-004` |
| Tractor and spreader are separate at the shop | Enter the tractor, align its compatible hitch and attach | The tool becomes coupled and its fill/control state is available to the driver | attachment is productive state, not cosmetic proximity | `FS25-004`, `FS25-005` |
| Coupled spreader is outside or raised over the target | Activate/lower it and drive | Vehicle moves, but only eligible working-width intersections on the assigned field consume fill and advance accepted fertilized coverage | geometry, compatibility and consumable application couple | `FS25-005`–`FS25-008` |
| One strip is treated and the next remains untreated | Turn and overlap the next pass minimally | New footprint changes remaining eligible cells while redundant overlap spends time/fill without equivalent progress | coverage planning creates optimisation pressure | `FS25-007`, `FS25-008` |
| Tractor crosses beyond the assigned boundary with tool active | Continue briefly outside the target | Non-target ground cannot replace remaining contract coverage, so the completion predicate does not advance from that pass | field ownership/assignment gates useful work | `FS25-007`–`FS25-009` |
| Accepted coverage reaches the contract threshold | Stop the implement and reopen Contracts | The offer changes from live progress to completed/collectable state while the farm remains otherwise open-ended | mechanical completion precedes settlement | `FS25-009`, `FS25-010` |
| Contract is collectable | Select Collect | Borrowed-equipment disposition resolves, the displayed deduction is applied, net money is credited and the active contract closes | explicit bounded economic terminal | `FS25-010`, `FS25-012` |

## Strategic and experiential structure

- Local decision: line up the hitch and each pass; choose steering angle, speed,
  activation edge and turn geometry from working width, boundary and fill.
- Medium-term planning: minimise untreated gaps and wasteful overlap while
  preserving enough fertilizer and road/field access to finish the assigned
  area, rather than optimising a whole farm year.
- Long-term structure: compare gross reward with the borrowed-item deduction,
  convert one temporary supplied fleet into accepted field state and collect
  the resulting net credit. The unit stops before spending it.
- Common heuristics: attach before travelling; inspect field ownership and
  fertilized layer; switch the spreader off during road travel and headland
  turns; use parallel passes slightly inside working width; check progress
  before assuming visual coverage is sufficient.
- Failure attribution: hitch/control prompts, fill level, field information,
  map soil layer, contract progress and settlement values separate incompatible
  equipment, wrong field, inactive tool, gaps, overlap waste and fee effects.
- Player-trust factors: the offer declares economic terms before acceptance;
  field state changes under the visible implement footprint; collection is a
  distinct action after completed coverage instead of an arbitrary save point.
- Claim IDs: `FS25-003`–`FS25-012`.

## Replay and variation

- What changes between saves: available farmer/field offers, displayed reward,
  borrowed fleet, crop/field state, exact path, overlap, fill use and net result.
- Randomness or procedural generation: the map is authored; the Contracts
  screen changes over world time, so the declared sorting rule samples an
  eligible typed offer instead of claiming a fixed field or reward.
- Multiple viable strategies: perimeter-first, long-axis parallel passes and
  shorter contour-following passes can all satisfy coverage with different
  turning/overlap cost.
- Typical replay motive: reduce wasted fill and time, try owned equipment or a
  different contract type. All repeats and owned-farm accumulation are outside
  the first collected-contract terminal.
- Claim IDs: `FS25-003`, `FS25-006`–`FS25-011`.

## Adjacent systems and history

- Direct predecessors: earlier Farming Simulator contracts and vehicle/tool
  controls establish series context, but the canonical claims are pinned to
  current FS25 manual/Academy and update evidence.
- Variants: other contract types change implement, material, product or
  delivery requirements; owned farming adds crop calendar, capital equipment
  and repeated soil-state recurrence; Precision Farming adds sampled soil and
  variable application; multiplayer changes authority.
- Similar games: Euro Truck Simulator 2 also samples one paid offer and supplies
  a directly controlled employer vehicle, but its state is a loaded trailer,
  road route, fatigue/deadline and depot settlement. Stardew Valley applies
  tools to crop tiles inside a repeated calendar economy but has no coupled
  powered implement or borrowed field contract. Farming Simulator 25 makes
  productive coverage the contract state itself.
- Important differences: this packet has no delivery destination, combat,
  autonomous fleet or whole-season yield terminal. The central decision is
  whether a compatible coupled footprint changes the correct persistent field
  cells efficiently enough to unlock one explicit payment.
- Claim IDs: `FS25-003`–`FS25-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-201`, `ACT-351`, `ACT-352` | offer order, bindings, tractor, hitch and spreader are parameters |
| System Behaviour | `SYS-320`, `SYS-629`–`SYS-631` | field, fleet, footprint, rate, threshold and values are parameters |
| Constraint | `CON-288`, `CON-515`, `CON-516` | compatibility, fill, boundary and coverage threshold are parameters |
| Information | `INF-067`, `INF-252`, `INF-253` | crop/state filters, progress and monetary values are parameters |
| Objective | `OBJ-119` | sampled offer identity is a parameter |
| Time | `TIM-003` | ordinary continuous field work only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `195` (`GAME-0001`–`GAME-0195`).
- Exact genome matches: none.
- Tied near matches: `GAME-0169` — Euro Truck Simulator 2 (`4 / 37 = 0.108108`).
- Supported combination subsets: `COMB-0194`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0169` — Euro Truck Simulator 2 | enter and directly operate an employer-supplied world vehicle, simulate its motion, require viable driver/terrain state and resolve play in continuous time | FS25 supplies separate tractor and powered spreader through a field offer, requires hitch/tool compatibility, consumes fertilizer across a persistent surface, validates assigned-area coverage and settles through Collect; ETS2 supplies an already loaded articulated truck, then binds route, traffic law, cargo damage, fatigue, deadline, depot parking and delivery results | Near, `0.108108` |

### Preserved research notes

- New genes: `ACT-351`, `ACT-352`, `SYS-629`–`SYS-631`, `CON-515`,
  `CON-516`, `INF-252`, `INF-253` and `OBJ-119`.
- Classification result: bounded new genes plus reuse and one new combination.
- Evidence and reasoning: the corpus already owns embodied vehicle operation,
  generic vehicle motion, viable driving geometry, visible rewarded tasks and
  live time. New boundaries isolate contract-supplied field machinery,
  attachment/tool authority, footprint-based persistent treatment, target
  coverage, material compatibility and explicit net settlement.

## Taxonomy impact

- Registry changes: fifteen Active genes and `COMB-0194`.
- Taxonomy-change record: none; no existing definition is deprecated, merged or split.
- Candidate terms affected: field-work contract, powered implement coupling,
  treatment footprint, accepted field coverage and borrowed-equipment settlement.

## Negative results

- `ACT-285` and `SYS-505` are not reused: ETS2 accepts a preloaded road-cargo
  job whose employer vehicle starts as the transport object; FS25 separately
  spawns compatible field machinery that the player must couple and operate to
  transform a target surface.
- `SYS-506` is not reused: the spreader is a powered working implement, not a
  cargo trailer with separate collision damage and depot pose.
- `ACT-213`, `CON-311` and `SYS-344` are not reused: the scope does not plant,
  grow or harvest one owned crop across seasonal time.
- The exact field/reward is not promoted into rules identity. Official evidence
  says offers change over time; ordering makes the entry repeatable without
  pretending a dynamic contract is fixed content.
- AI workers, GPS steering, own-field yield and post-payment spending remain
  excluded rather than silently inherited from the full product.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний base-game контракт Fertilizing у версії
  1.21.1.0 має видимі умови, позичену техніку з окремою платою, сумісне
  зчеплення трактора й розкидача, стійкий стан поля та явне отримання винагороди
  (`FS25-001`–`FS25-012`).

## Нові гени

- [Observation | Corroborated | High] Десять нових меж ізолюють прийняття
  контракту з позикою техніки, керування робочим агрегатом, покриття поля,
  сумісність, прогрес і фінальний розрахунок.

## Нові комбінації

- [Observation | Direct | High] `COMB-0194` — один контракт від вибору
  пропозиції через зчеплення та ручне внесення добрива до collectable payment.

## Зміни таксономії

- [Confirmed | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-007` — Physics and object manipulation: tractor pose, hitch alignment,
  tool footprint and field boundary determine legal productive contact.
- `FAM-017` — Ordered dependency sequencing: accept, collect, couple, cover and
  settle form a mechanically gated one-contract chain.
- `FAM-010` — Real-time system pressure: steering, material application and
  field progress resolve continuously during manual passes.
- No new family is created from one game.

## Plain-language interpretation

A Farming Simulator 25 contract can turn a huge open-ended farm into one clear
mechanical problem. The offer identifies a field task and payment. Borrowing
equipment reduces the eventual income but supplies a tractor and compatible
spreader, so the player does not need a developed farm before the attempt.

The main puzzle is coverage. The tool must be attached, filled, lowered and
active over the correct field. Every pass trades turning room, overlap, gaps,
material and time. The field's fertilized layer and contract progress make the
result persistent and inspectable. Reaching the accepted coverage is not yet
the arbitrary end of a farming session: selecting Collect closes the one job,
releases the borrowed fleet and turns the declared terms into net money.

## New questions

- Which contract game reuses temporary supplied machinery but changes a
  persistent surface through discrete turns rather than continuous coverage?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0197` — Valheim.
- Optimisation criterion: continue the authorised demand-led Goal after one
  complete borrowed-equipment field settlement.
- Expected gene pressure: seeded world generation, manual survival production,
  boss summoning, cooperative exclusions and trophy-gated progression.
- Anti-bias note: do not import FS25's contract, field ownership, powered hitch
  or payment terminal into Valheim's solo Eikthyr packet.

## Next research step

- Integrate `GAME-0197` — Valheim after the required thirty-second stop window.

## Design lessons

- A sandbox becomes bounded when a typed offer fixes target state, temporary
  tools, progress predicate and explicit settlement.
- Coverage feedback matters because visible treated area separates a missing
  strip from mere slow execution or an uneconomic borrowing choice.

## Open questions

- Does the current engine return borrowed machines immediately on collection
  or only make them unavailable for further work before later cleanup? The
  canonical system deliberately records removal/release as one disposition
  parameter until authenticated direct play confirms the exact presentation.
