---
game_id: GAME-0444
slug: harvest-moon-back-to-nature
game_title: "Harvest Moon: Back to Nature"
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-213
    - ACT-214
    - ACT-219
    - ACT-512
    - ACT-578
    - ACT-579
  system:
    - SYS-1162
    - SYS-1163
    - SYS-1164
    - SYS-1165
  constraint:
    - CON-311
    - CON-718
    - CON-719
  information:
    - INF-091
    - INF-136
  objective:
    - OBJ-253
  time:
    - TIM-003
    - TIM-031
---

# Game: Harvest Moon: Back to Nature — first spring crop cycle

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Crop prices, growth durations, exact weather, initial cash and the nine-seed footprint are parameters, not extra genes. Farming art and the marketing title are outside the mechanical signature.

## Analysis scope

- Version / ruleset: the original North American English PlayStation release of *Harvest Moon: Back to Nature*, year-one outdoor and farmhouse crop economy, without later remaster conveniences. The 2025 PS4/PS5 conversion is cited only as an official public destination, not as a mechanics source. The 2000 PlayStation manual owns the crop, clock and farm rules; a particular disc revision was not inspected.
- Primary decision loop: use cash and the outdoor day to acquire a spring seed packet, clear and hoe accessible field tiles, scatter a fixed 3 × 3 packet, water reachable plants unless rain supplies water, sleep through daily growth, harvest mature produce and get it into the shipping bin before the 5:00 pm non-holiday pickup. Preserve stamina and leave enough calendar days before the seasonal crop turnover.
- Entry: the first freely playable morning, Spring 2 of year one, after the introductory setup on the inherited farm. The first-day dating follows contemporary original-PlayStation written routes; it was not reproduced from a disc here.
- Local evaluation and exit: wake on Summer 1 after Spring 30 and inspect the paid-shipment count, farm cash and any wilted spring plants. A positive local crop cycle has at least one planted spring crop grown, harvested and paid before turnover; zero paid crop output is an analytic failure of this chosen farm task, not an authored game-over screen. The open-ended game and its eventual three-year village judgement continue beyond this packet.
- Included: walking between field, house, shop and bin; offered seed purchase; removal of plot obstacles; hoe preparation; fixed-footprint sowing and prepared-soil gate; per-crop reachable watering and harvest; rain and daily crop growth; timed shipping and retained money; stamina, collapse risk, rest and day advancement; visible date/hour, farm totals and weather forecast; indoor clock pause; Spring-to-Summer crop turnover. Holiday pickup exceptions inside the month remain included because they alter the same shipping decision.
- Excluded: livestock husbandry, fishing, mining, courtship, festivals as playable contests, recipe cooking, house expansion, hired sprites, upgraded watering-can use, hothouse crops, wild-item shipping, the full three-year farm/village evaluation and port-only rewind or quick-save. Tool upgrades are mentioned solely as the counterfactual that changes center-plot reach, not modelled as an acquired action.
- Reproducible parameterisation: start a new original-English PlayStation farm, reach the first playable Spring morning, buy an offered spring seed packet, prepare an accessible planting footprint, sow and water it over successive days, pick mature produce, deposit it before a normal 5:00 pm pickup and repeat or wait until Summer 1. Compare a dry missed watering, a rainy day, a holiday or late deposit, and an over-dense 3 × 3 patch with the base watering can. These are source-derived reproduction steps, not executed play observations.
- Potential scoped modules: livestock and fodder, tool upgrading, village relationships, festivals, recipes, hothouse growing and the three-year judgement each require separate causal and evidence boundaries.
- Direct-play status: no original disc, PlayStation, executable, video, audio, game-state capture or controller test was inspected or run. The manual is a digitised copy of a primary printed artefact; contemporary player guides bound the start date and crop route. Exact growth day-count arithmetic and weather probabilities are not measured here.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HM-001` | The original PlayStation manual places a running ten-minute-step clock outdoors, pauses it in buildings and uses 30-day seasons. | Confirmed | Direct | High | P1 |
| `HM-002` | A cleared tile must be hoed to hold a seed; one packet spreads over nine fixed positions, and crop care/harvest is individual and reach-dependent. | Observation | Direct | High | P1 |
| `HM-003` | Daily watering or rain supports crop growth; a second watering does not accelerate it, and a base can cannot reach the middle of a dense 3 × 3 patch. | Observation | Corroborated | High | P1, S1 |
| `HM-004` | The collector pays for crops placed in the bin before the 5:00 pm pickup on eligible days, but does not collect on holidays. | Observation | Direct | High | P1 |
| `HM-005` | Spring's ordinary crop selection gives way to Summer's, and remaining Spring plants wilt after turnover. | Observation | Direct | High | P1 |
| `HM-006` | Farm-tool work expends stamina; overwork can cause collapse and loss of a workday, while food, the hot spring or rest can recover energy. | Observation | Direct | High | P1 |
| `HM-007` | The first freely playable farm day is Spring 2, year one; the mayor's later judgement is three years away. | Observation | Corroborated | Medium | P1, S1, S2 |
| `HM-008` | The original North American PlayStation publication was in 2000; the later PS4/PS5 conversion adds conveniences and is not the analysed build. | Confirmed | Direct | High | P2, P3 |

## Basic data

- Release / origin: North American original PlayStation *Harvest Moon: Back to Nature*, published by Natsume in 2000. Its PlayStation manual describes the inherited field and three-year village appraisal; only the first spring crop economy is analysed here.
- Platform or physical form: original English PlayStation disc and standard controller, not the converted PS4/PS5 application.
- Mechanical families: real-time system pressure (`FAM-010`) for the advancing outdoor workday and pickup cutoff; ordered dependency sequencing (`FAM-017`) for clearing, tilling, sowing, watering, harvesting and shipping before seasonal reset.
- **P1:** [Original North American PlayStation instruction manual, digitised copy](https://oldgamesdownload.com/wp-content/uploads/manuals/harvest-moon-back-to-nature_ps1_manual_en_b8i.pdf), printed pp. 5–8, 10, 13–14, 17–18 and 21–22, inspected 2026-09-28. Primary printed rules for the clock, field, crop packets, watering, reach, bin, stamina, forecast and season transition. The copy was read as an artefact, not used as gameplay capture or artwork.
- **P2:** [Natsume publisher announcement](https://www.natsume.com/news/news_pdffiles/pid_329_HM%20Back%20to%20Nature%20Coming%20Soon.pdf), February 2023, inspected 2026-09-28. Confirms the original North American PlayStation release date and distinguishes re-release from original.
- **P3:** [Official PlayStation Store product page](https://store.playstation.com/en-us/concept/10005231/), inspected 2026-09-28. Explicitly calls the PS4/PS5 offering a conversion with rewind, quick save and possible behavioural differences; used as a legal external link, not original-rule evidence.
- **S1:** [Chito10's original-PlayStation crop guide](https://gamefaqs.gamespot.com/ps/446412-harvest-moon-back-to-nature/faqs/11583), inspected 2026-09-28. Contemporary player account of starting Spring 2, crop watering and inaccessible center plots. Individual crop timings are not promoted to universal measured constants.
- **S2:** [Sky Render's original-PlayStation guide](https://gamefaqs.gamespot.com/ps/446412-harvest-moon-back-to-nature/faqs/26294), inspected 2026-09-28. Independent written first-spring route, weather and farm-day corroboration. It is not a substitute for a verified original disc.
- Claim IDs: `HM-001`–`HM-008`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for walking among the field, house and village; `ACT-130` for buying a currently offered seed packet with farm money; `ACT-512` for tool-clearing a blocked farm tile; `ACT-213` for individual watering and crop pickup; `ACT-219` for committing carried harvest to the sale bin; and `ACT-214` for going to sleep and yielding the workday.
- Add `ACT-578` for hoeing one cleared tile and `ACT-579` for broadcasting one packet over a fixed 3 × 3 footprint. A packet action is not nine independent `ACT-213` plant-target decisions.

### System Behaviour Genes

- Add `SYS-1162` for day-boundary water/rain-dependent crop growth; `SYS-1163` for scheduled 5:00 pm non-holiday pickup and delayed payment; `SYS-1164` for Spring-to-Summer crop turnover and wilt; and `SYS-1165` for tool stamina expenditure, recovery and overwork's lost workday.
- Resolution order: current outdoor clock and weather → player field/shop/bin actions with stamina cost → eligible 5:00 pm pickup → sleep or collapse advances date and crop state → on Spring 30 to Summer 1, prior-season field crops wilt and offers change. A paid shipment is retained across later day and season boundaries.

### Constraint Genes

- Reuse `CON-311`: harvest maturity depends on species, viable season, water and elapsed growth. Add `CON-718`: only cleared, tilled packet positions become plants. Add `CON-719`: individual care and picking require spatial reach, so the base can cannot water the surrounded center of a dense 3 × 3 plot. Price, packet size and the 30-day season are parameters.

### Information Genes

- Reuse `INF-136` for date/hour, field condition, cash and farm-status inspection, without claiming a perfect future weather sequence. Reuse `INF-091` for current weather and the household TV's upcoming-weather forecast; the forecast is a planning aid, not an override of actual rain.

### Objective Genes

- Add `OBJ-253` for growing, harvesting and obtaining payment for at least one spring crop in this local analytic packet. The original product does not declare Spring 30 a win screen; the three-year appraisal is outside this genome.

### Time Genes

- Reuse `TIM-003` for outdoor real-time work and travel before pickup. Add `TIM-031` for the place-dependent pause inside buildings, which changes the cost of shopping/planning but does not stop crop/day progression after sleep.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Cleared ordinary soil outdoors | Use the hoe on one reachable tile | That tile becomes tilled; tool use costs stamina and outdoor minutes | Ground preparation precedes planting | `HM-001`, `HM-002`, `HM-006` |
| A bought seed packet and a partly tilled 3 × 3 footprint | Scatter one packet | Seeds occupy only qualifying prepared positions; untilled positions do not produce plants | One commitment can partly fail | `HM-002` |
| Sprouts in a reachable row on a clear day | Water each target once, then water one again | First watering satisfies that day's care; the extra use costs work but adds no growth step | Per-crop care is not accelerated by repetition | `HM-003`, `HM-006` |
| A rainy day with an inaccessible center sprout | Do not reach the center with the base can | Rain can satisfy the water requirement even though ordinary manual reach is blocked | Weather and topology are separate | `HM-003` |
| Mature picked crop before ordinary 5:00 pm pickup | Deposit it in the shipping bin | Scheduled collection credits farm money and shipped count | Harvest alone is not payment | `HM-004` |
| Crop put into the bin after pickup or on a holiday | Wait for that day's ordinary pickup | No eligible same-day payment is credited | The economic gate uses calendar and hour | `HM-004` |
| Late outdoor tool work with low stamina | Continue exertion through collapse | Clinic recovery consumes a later workday; this does not end the game | Energy pressure compounds calendar pressure | `HM-006` |
| Spring 30 field still holds living spring crops | Sleep and wake Summer 1 | Old-season plants wilt; ordinary summer seed options replace spring's | Unharvested commitment loses value at season turn | `HM-005` |

## Strategic and experiential structure

- Local: field geometry is a commitment. A dense 3 × 3 packet may create a center plant that the basic can cannot reach, whereas a path or more modest prepared mask sacrifices potential count for care access. A second watering wastes energy without speed gain.
- Medium term: buy seeds while stock and money permit, schedule enough watered days for maturity, ship by the daily cutoff and avoid holidays. Check the TV forecast to shift care effort when rain will help.
- Long term inside this packet: repeated crop sales replenish purchasing power, but planting late in Spring risks wilt at Summer 1. Three-year farm quality is contextual, not a sampled completion test here.
- Failure attribution: a dry non-growing crop can be traced to missed care; inaccessible center growth to the field pattern/tool range; zero sale to maturity, pickup timing or holiday; lost labour to overwork. The exact random weather sequence is not asserted.

## Replay and variation

Player-chosen species, tilled geometry, day of sowing, weather, store route, stamina recovery and shipment timing change the number of paid crops by Summer 1. The field persists through days; seasonal turnover removes living spring plants. No procedural farm map, exact weather probability or best-profit formula is inferred.

## Adjacent systems and history

`GAME-0089` *Stardew Valley* currently analyses the Boiler Room bundle-to-minecart repair packet, not its crop economy, so thematic farming resemblance does not imply a shared crop signature. `GAME-0142` *Project Zomboid* uses target-based planting and seasonal viability in a survival world, but its apocalypse calendar, utility cutoffs and disease are not imported into this PlayStation farm. `GAME-0196` *Farming Simulator 25* analyses a borrowed-machine fertilising contract, not hand-tended 3 × 3 seed packets or a daily collection bin. The original *Harvest Moon* manual, not later series familiarity, owns this packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-213`, `ACT-214`, `ACT-219`, `ACT-512`, `ACT-578`, `ACT-579` | walking, seed purchase, care, sleep, shipping, clearance, hoeing, packet sowing |
| System Behaviour | `SYS-1162`, `SYS-1163`, `SYS-1164`, `SYS-1165` | daily growth, pickup, season turnover, stamina |
| Constraint | `CON-311`, `CON-718`, `CON-719` | viable crop, prepared soil and reachable care |
| Information | `INF-091`, `INF-136` | weather forecast and current farm state |
| Objective | `OBJ-253` | paid cultivated output before turnover |
| Time | `TIM-003`, `TIM-031` | live outdoor schedule and indoor pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `443` (`GAME-0001`–`GAME-0443`).
- Exact genome matches: none.
- Tied near matches: `GAME-0307` — Slime Rancher (`4 / 28 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0307` — Slime Rancher | `ACT-008`, `ACT-130`, `ACT-219`, `TIM-003` | Both move through a live work space, buy inputs and commit goods for cash, but Slime Rancher vacuums and feeds creatures before selling plorts and buying corral walls. This spring packet instead prepares specific soil, broadcasts seeds, waters reachable crops, uses day-boundary growth and a timed shipping bin, then confronts season turnover. | Tied nearest by genome Jaccard at `0.142857`; not an equivalent farm cycle. |

## Taxonomy impact

`TAXONOMY_CHANGE_181` admits two farm-ground/packet actions, four crop/economy/stamina responses, two soil/access constraints, one local crop-shipment objective and one location-gated time boundary. Earlier signatures and verified combinations are unchanged.

## Negative results

- Do not import Project Zomboid's `SYS-344` apocalypse utility loss, refrigeration or disease as if they occurred on this farm; only its general `CON-311` crop-viability boundary transfers.
- Do not claim a full nine mature plants from every packet: untilled ground rejects seeds and the basic watering can cannot reach a surrounded center tile.
- Do not import the converted PS4/PS5 rewind/quick-save feature, later series crops or a completed three-year village judgement into the original first-spring loop.
- Exact weather probabilities, crop timing arithmetic, one disc revision and direct-play results remain unmeasured.

## Delta summary

## New facts

- [Observation | Direct | High] Preparing tiles, scattering a fixed packet and accessing each crop create distinct field-planning commitments (`HM-002`, `HM-003`).
- [Observation | Direct | High] A daily pickup deadline and seasonal wilt change whether grown output becomes retained income (`HM-004`, `HM-005`).

## New genes

- [Observation | Corroborated | High] Ten typed boundaries in `TAXONOMY_CHANGE_181` are not represented by a generic farming label.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; proper-subset support is recomputed in the comparison section.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_181`; no older signature changes.

## New questions

- Would controlled original-disc play settle exact crop-growth-day arithmetic and weather frequency without changing these action and calendar boundaries?

## Next game

`GAME-0445` *NiGHTS into Dreams* is the next recorded unit, only after this unit's acceptance and the Goal stop window. No push, public publication or deployment is authorised.
