---
game_id: GAME-0453
slug: age-of-mythology
game_title: Age of Mythology
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-089
    - ACT-121
    - ACT-130
    - ACT-139
    - ACT-140
    - ACT-189
    - ACT-219
    - ACT-316
    - ACT-317
    - ACT-318
    - ACT-598
    - ACT-599
    - ACT-600
    - ACT-601
    - ACT-602
  system:
    - SYS-004
    - SYS-161
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-360
    - SYS-380
    - SYS-549
    - SYS-550
    - SYS-551
    - SYS-552
    - SYS-553
    - SYS-554
    - SYS-555
    - SYS-1094
    - SYS-1188
    - SYS-1189
    - SYS-1190
    - SYS-1191
    - SYS-1192
    - SYS-1193
    - SYS-1194
    - SYS-1195
    - SYS-1196
  constraint:
    - CON-188
    - CON-269
    - CON-273
    - CON-466
    - CON-467
    - CON-469
    - CON-470
    - CON-730
    - CON-731
    - CON-732
  information:
    - INF-059
    - INF-224
    - INF-225
  objective:
    - OBJ-103
  time:
    - TIM-003
---
# Game: Age of Mythology — original Windows Zeus land Conquest

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named gods, unit classes, resource amounts, research costs, attack coefficients, caps and map labels are parameters, not independent gene identities.

## Analysis scope

- Version / ruleset: original English 2002 Windows *Age of Mythology*, one single-player Random Map Conquest on Savannah, Greek Zeus against one computer-controlled Greek Zeus with locked enemy teams, ordinary resources, Archaic start, normal speed and ordinary unexplored-map visibility. The 2002 Microsoft manuals bound the rules, not a current wiki or Retold executable. Exact installation patch, AI difficulty, map seed and elapsed timing were not inspected; setup values describe the intended packet rather than a captured save.
- Primary decision loop: scout reachable land, assign villagers between finite material sources, inexhaustible farms, construction, repairs and Temple prayer; spend shared stocks on housing, units and building-local research. Choose one eligible minor god at each Age transition, command human, hero and myth troops, and decide when to spend a once-only god power. Protect income, production and sight while eliminating the opponent's recoverable military and economic state.
- Entry and exit: begin at the Archaic Town Center with the ordinary starting workforce, scout and Zeus resource/power state. Positive exit is Conquest elimination or opponent resignation; symmetric elimination or player resignation is negative exit. Destroying just one Town Center is not declared sufficient. Exact executable defeat predicates for every hidden or stranded entity remain unmeasured.
- Included: land exploration and remembered terrain/buildings; food, wood and gold gather/carry/deposit; claimable herd animals; unlimited farms; worker construction/repair; housing and class-specific live caps; production/rally/research queues; Temple, Armory and Market advancement prerequisites; exclusive Zeus minor-god choices; prayer-generated capped Favor; ordinary counters, terrain/vision/range and periodic myth attacks; Greek hero uniqueness and relic transport/deposit; building garrisons, Town Bell and work restoration; immediate responsive Market exchange and vulnerable round-trip caravan income; one-use local/global god powers, a deployed income vault and an Underworld troop passage; current resource, selection, progress, power and technology information; pause/resume and match terminal.
- Excluded: campaigns, learned campaign powers and fallen-protagonist revival; Titans, Extended Edition, Retold, Chinese/Atlantean additions and recast powers; Egyptian/Norse economy or gods; naval battles, fishing, docks, Scylla/Carcinos and transport ships; multiplayer/team diplomacy or tribute; Deathmatch, Lightning, Supremacy Wonder/settlement countdown wins; editing, cheats, exploits, ranked meta, optimal builds, exact coefficients and AI implementation. A naval or different-civilization packet requires its own review.
- Direct-play status: no CD, executable, save, replay, gameplay video, input trace or direct play was inspected. Microsoft's original mini-manual diagrams for controls and Greek rules were visually reviewed; selected publicly readable pages of the original collector's guide were read as documentation, not an executed match. A dated first-hand written guide corroborates the map and Zeus branches. Source evidence establishes a reconstruction; exact timing, generated arrangement and successful execution remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AM-001` | Material collection uses spatial labour and delivery, whereas Greek prayer consumes labour to accrue Favor directly; Zeus changes its starting amount, rate and ceiling. | Observation | Direct | High | P1, P2 |
| `AM-002` | Ordinary farms do not deplete or require replanting; finite wild/map inputs do. Approaching claimable herd animals changes their ownership rather than collecting inventory. | Observation | Direct | High | P1, P2 |
| `AM-003` | Built capacity, paid local queues and sequential Age prerequisites govern production; choosing a minor patron opens its own power, myth and technology options. | Observation | Direct | High | P1, P2 |
| `AM-004` | Additional Town Centers require vacant Settlements and the Heroic Age. Houses and each Greek hero identity have independent concurrent caps. | Observation | Direct | High | P1, P2 |
| `AM-005` | God-power grants are once-only, may be retained across Ages, and usually require current vision; expressly global powers differ. | Observation | Direct | High | P1, P2 |
| `AM-006` | Garrison acceptance protects eligible units and may enhance the building; destruction releases occupants. Bell commands remember workers' jobs, with finite shelter capacity. | Observation | Direct | High | P2 |
| `AM-007` | Heroes can carry relics, but their bonus begins only after Temple deposit; collecting all relics is not victory. | Observation | Direct | High | P2 |
| `AM-008` | Immediate Market transactions change later prices; separately, caravans repeatedly travel to a Town Center and produce distance-dependent Gold. | Observation | Direct | High | P2 |
| `AM-009` | Greek myth forms and powers change combat, protection, healing, movement or income; Hydra heads grow during battle and Colossi can heal by consuming resources. | Observation | Direct | High | P1, P2 |
| `AM-010` | Sight and remembered information differ; class counters, ranged-only anti-air and terrain restrict effective commands. | Observation | Direct | High | P1, P2 |
| `AM-011` | Conquest uses enemy elimination rather than Supremacy's other wins; Savannah is a period land-map choice and Zeus has the stated minor choices. | Observation | Corroborated | High | P1, S1 |
| `AM-012` | No exact original build, seeded match, timing or direct-play result was inspected. | Confirmed | Direct | High | source-review boundary |

## Basic data

- Origin: Ensemble Studios' 2002 game published by Microsoft; this is the original Windows ruleset, not the remade product.
- Analysis target: `PLAT-WINDOWS-PC`, original English CD edition. Known-release audit is not started; no same-name port or modern purchase entitlement is inferred.
- Mechanical families: tactical counterplay, live system pressure, agent routing and ordered dependencies: `FAM-009`, `FAM-010`, `FAM-015`, `FAM-017`.
- **P1:** [Microsoft's original 2002 mini-manual, X09-14063 0902](https://oldgamesdownload.com/wp-content/uploads/manuals/age-of-mythology_win_manual_en_d5b.pdf), checked 2026-09-30. Sixteen PDF pages; printed pp. 2–3, 7–14 and 18–25 supply HUD, economy, development, deity and outcome rules. Printed pp. 18–19 and 22–25 were visually inspected. The installed manual locator corroborated by P3 supports provenance; an archive host is not a gameplay download or publisher endorsement.
- **P2:** [Microsoft's original collector's-edition guide, publicly readable document scan/OCR](https://www.scribd.com/document/836804724/Age-of-Mythology-Collectors-Edition-Manual-PC), checked 2026-09-30. Selected visible printed pp. 24–26, 31–38 and Greek technology entries were read. Its damaged capital-character OCR was cross-checked against P1 rather than treated as new rules. Shelter, relic, bell, market and caravan descriptions are first-party documentation. The complete 128-page PDF was not downloaded or claimed as visually inspected; no restricted content was bypassed.
- **P3:** [Archived Microsoft KB329564: installed Age of Mythology manual locations](https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/329/564.HTM), checked 2026-09-30. Provenance and separation of original/Gold/Titans documentation only, not an extra observed mechanic.
- **S1:** [Jonathan Galloway's dated original-game written guide, 21 December 2002](https://www.supercheats.com/pc/walkthroughs/ageofmythology-walkthrough02.txt), checked 2026-09-30. Greek/Zeus and Random Map sections corroborate starting workforce, eligible patrons and Savannah. First-hand written testimony, not code, an official executable or a measured current installation. Its campaign routes do not enter this scope.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-318` for worker gathering, building and repair, `ACT-139` for legal foundations/removal, `ACT-316` for unit queues and `ACT-121` for technology/Age orders. Paid wall segments and rally coordinates are placement/queue parameters, not extra genes.
- Reuse `ACT-189` for destinations and attack targets; `ACT-317` for group combat stance. Default formation is automatic under `SYS-554`; no player-selected formation menu is invented.
- Reuse `ACT-140` for the exclusive offered patron at each advancement. Zeus's Classical choices are Athena/Hermes, Heroic Apollo/Dionysus, Mythic Hera/Hephaestus. Choosing one excludes its alternative for this progression; it does not grant every Greek power.
- Reuse `ACT-130` and `ACT-219` for commodity purchase/sale: quantity and an immediate shared-stock destination fit the existing offer/item parameters. The responsive quote, not the generic act of buying, needs a separate system boundary.
- Reuse `ACT-089` for a hero collecting a reachable discrete relic identity, not carrying free continuous rigid physics. Reuse `ACT-019` for an individually commanded Colossus heal; this is distinct from a civilization cast.
- Add `ACT-598` for assigning worship labour, `ACT-599` for a civilization-level invocation, `ACT-600` for building garrison/ejection, `ACT-601` for artifact deposit and `ACT-602` for live caravan route assignment. None is a cosmetic rename of worker terrain collection, a hero cast, vehicle boarding, a character request or a turn-based trade slot (`AM-001`, `AM-005`–`AM-008`).
- Town Bell/return are command parameters of the shelter action; their saved-job system response is independently recorded in `SYS-1194`.

### System Behaviour Genes

- Reuse `SYS-004` for variable Random Map arrangement, with no invented seed or distribution; `SYS-161` for finite map-source depletion; `SYS-549` for worker extraction/carry/drop-off of wild food, trees and mines. Do not silently extend its finite-source boundary to inexhaustible farms.
- Reuse `SYS-550` for worker construction/repair, `SYS-551` for concurrent paid site queues and rally release, `SYS-552` for retained research, Age progression and patron-conditioned unlocks, and `SYS-553` for occupied population versus completed housing capacity.
- Reuse `SYS-297` for commanded path/acquisition, `SYS-554` for ordinary group formations and stance response, `SYS-305` for allied sight propagation, and `SYS-215` for live combat. Infantry/cavalry/archer/siege/hero/myth class relations, terrain modifiers and periodic myth attacks are effect/eligibility parameters. A hero counters myth; an ordinary melee unit does not hit a flying scout merely because it sees it.
- Reuse `SYS-360` for Hydra's retained battle-local head state modifying later combat. Heads are a form-specific combat resource, not generic experience levels; exact head-growth trigger, cap and coefficients are not claimed. This is a bounded interpretation of the documented battle-growth rule, not proof of a kill-counter implementation.
- Reuse `SYS-380` for legal selected powers' typed effects: Bolt, Restoration, Ceasefire, Bronze, Lightning Storm, deployment of Plenty or a passage, and the individually selected Colossus heal. Their geometry, duration and target classes differ without requiring a gene for each god name. Routine automatic myth attacks remain `SYS-215`, not falsely claimed as manual spells.
- Reuse `SYS-1094` for the completed Plenty vault's direct income, and `SYS-555` for the Conquest terminal.
- Add `SYS-1188`: assigned Temple prayer produces bounded shared Favor without a carry trip; Zeus begins with 25 and has a 200 cap, rather than the ordinary 100. Labour opportunity cost remains part of this transition.
- Add `SYS-1189`: eligible garrison occupants are protected and may enhance attack, then exit on destruction. No guarantee of surviving the subsequent exterior battle is made.
- Add `SYS-1190`: a carried relic becomes an active shared bonus only after Temple deposit; no unsupported destruction/recovery permanence is added.
- Add `SYS-1191` for responsive immediate exchange and `SYS-1192` for autonomous distance-yield return journeys. Market–Market trading is not the declared caravan route, and current price is not a guaranteed future quote.
- Add `SYS-1193`: farm labour repeatedly harvests and delivers without ordinary exhaustion or reseeding. Changing gather rate, drop-off distance or construction cost does not change this eligibility boundary.
- Add `SYS-1194` for bell-dispatched workers' retained jobs and return; excess workers without shelter space keep working. Add `SYS-1195` for proximity ownership of eligible herd animals, which can subsequently be moved and harvested rather than vanishing into inventory.
- Add `SYS-1196` for commanded troops using Apollo's placed passage link. This is not Portal's continuous body-plane/velocity mapping. Link lifetime, exact throughput and destruction behavior require a trace and are not invented.

### Constraint Genes

- Reuse `CON-466` for reachable funded unlocked foundations and `CON-467` for completed-site, prerequisite, stock and capacity gates. Temple → Classical, Armory → Heroic and Market → Mythic are designated prerequisites, not `CON-468`'s Age of Empires building-count/Castle rule.
- Reuse `CON-469` for resource source/drop-off access, `CON-470` for terrain, path and attack reach, and `CON-273` for ordinary fog-limited enemy action. Reuse `CON-188` for exclusive patron choice and `CON-269` for the separate unit heal's current resource/target eligibility.
- Add `CON-730`: each power needs its unspent grant and permitted target. Most local casts need current sight; Hermes's expressly global Ceasefire does not. Advancing an Age does not recharge an already spent Bolt, but unspent powers can be saved.
- Add `CON-731`: additional Town Centers use vacant predefined Settlements only from Heroic onward. Site identity and current occupancy, not ordinary empty ground alone, matter.
- Add `CON-732`: each capped creation type has its own concurrent allowance. Ten Houses and one living hero of each eligible Greek identity are parameters. A fallen ordinary Greek hero can be recruited again; campaign protagonist revival is excluded.

### Information Genes

- Reuse `INF-224` for current resource/Favor/population, Age, selected unit/building, queue progress and power readiness; `INF-225` for unexplored versus remembered versus currently seen terrain/buildings. A remembered hostile building is not proof of current occupancy.
- Reuse `INF-059` for F1/F2 help/technology dependency and exposed prerequisites, costs, minor choices and relic descriptions. These surfaces disclose rules, not future AI orders or an omniscient enemy state.

### Objective Genes

- Reuse `OBJ-103` for eliminating the opponent's recoverable civilization state under Conquest. One destroyed Town Center, gathered relics, a Wonder or all settlements are not independent wins in this packet.

### Time Genes

- Reuse `TIM-003`: gathering, prayer, construction, queues, movement and combat progress while commands are issued. Ordinary explicit pause suspends play; Lightning's altered speed and frame-exact pause manipulation are excluded.

## Reproducible transitions

| Before | Action/event | Source-derived resolution | Boundary | Claim ID |
|---|---|---|---|---|
| Villager gathers at a finite source | Assign a nearer drop-off route | Carried material reaches the shared stock after delivery; source reserve shrinks | Field stock versus shared credit | `AM-001`, `AM-002` |
| Completed farm and compatible drop-off | Assign a worker and continue harvesting | Food continues without a normal reseed order | Infinite field versus finite source | `AM-002` |
| Zeus Temple and idle villager; Favor below cap | Assign prayer | Favor accrues directly while that worker stops other work | Labour-priced direct resource | `AM-001` |
| Zeus reaches the Favor cap | Keep worshipping | No further stock beyond the cap | A cap is not failure | `AM-001` |
| Eligible claimable herd animal near an owned unit | Approach, then command the animal | Ownership changes and later relocation is possible | Ownership, not inventory pickup | `AM-002` |
| Classical advance requirements satisfied | Commit Athena rather than Hermes | Completed advance opens Athena's declared options, not both branches | Exclusive offer and permanent unlock | `AM-003` |
| Mythic cost available but Market absent | Request advancement | Required-site gate prevents the order | Designated prerequisite, not building count | `AM-003` |
| Heroic reached, ordinary ground empty | Request another Town Center | Ordinary terrain is insufficient; use a vacant Settlement | Fixed site identity | `AM-004` |
| One living hero of a given type, population space free | Request the same type | Type cap blocks it; a different eligible hero type has its own allowance | Per-type cap versus population | `AM-004` |
| Unspent Bolt and legal seen enemy | Commit the power, then wait | Effect resolves once; waiting does not grant another use | Single grant versus recast | `AM-005` |
| Unspent earlier power and new Age reached | Inspect power availability | Earlier unspent grant remains available | Retention, not recharge | `AM-005` |
| Eligible workers with jobs and limited shelter | Ring bell, then return to work | Sheltered workers return to saved tasks; overflow did not gain infinite shelter | Finite containment and remembered work | `AM-006` |
| Occupied building under attack | Destroy shelter | Occupants exit into exterior risk | Release, not guaranteed survival | `AM-006` |
| Hero carries a relic | Deposit it at the Temple | Its declared shared bonus becomes active | Pickup is not activation | `AM-007` |
| Market, Food/Wood and a disclosed quote | Sell a large amount, inspect next quote | Stock exchange resolves now and later prices respond | Reactive quote versus fixed shop | `AM-008` |
| Caravan and reachable Market/TC route | Assign and let it return | Shared Gold arrives through travel; distance affects yield | Logistics versus instantaneous exchange | `AM-008` |
| Completed Plenty vault | Let live time pass | Shared income accrues without prayer or gather-return worker | Passive facility versus labour | `AM-009` |
| Apollo passage and eligible troops | Command entry | Troops resume at the linked exit | Nonlocal movement without Portal pose mapping | `AM-009` |
| Old hostile building outline outside current sight | Scout its place again | Current sight updates the remembered state | Remembered evidence versus current truth | `AM-010` |
| One hostile base destroyed but recoverable opponent units remain | Continue the match | Do not assume the whole Conquest terminal follows one building | Civilization versus local target | `AM-011` |

These are falsifiable source-derived cases, not executed tests. Exact queue cancellation/refund, passage throughput, special attack schedules, relic destruction/recovery and original AI behavior remain future measurements.

## Strategic and experiential structure

Prayer competes with material labour: a Favor balance does not itself provide food, gold or population space for a myth unit. A shorter gather route can protect income, whereas a longer caravan route trades higher nominal yield for travel/exposure. Current scouting enables local god casts but a remembered building does not. Saving a one-use power changes later intervention options; it is not an indefinitely rechargeable panic button. Patron choice removes an alternative branch, so unit composition and technology investment must follow the selected option. These are source-led causal interpretations, not optimal strategies or measured player responses.

## Replay and variation

Random-map geography, resource placement, opposing decisions and patron choice vary one declared land match. No probability, seed, AI policy, optimal build or replay outcome was measured. A different major deity changes available decisions; that does not justify inheriting an unreviewed cross-civilization union into this Zeus packet.

## Adjacent systems and history

Age of Empires II supplies the finite worker economy, production, housing, command and Conquest boundaries, but its finite replanted fields and specific Age-building-count gate do not transfer. Civilization VI's turn-based route slots and trade-post range do not implement a vulnerable live caravan. Portal's aperture-plane mapping is not an RTS passage command. Greek heroes are not the campaign's reviving named protagonists, and original once-use powers are not Retold recasts.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-019`, `ACT-089`, `ACT-121`, `ACT-130`, `ACT-139`, `ACT-140`, `ACT-189`, `ACT-219`, `ACT-316`, `ACT-317`, `ACT-318`, `ACT-598`, `ACT-599`, `ACT-600`, `ACT-601`, `ACT-602` | labour, orders, patrons, powers, shelter, relic and trade |
| System Behaviour | `SYS-004`, `SYS-161`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-360`, `SYS-380`, `SYS-549`, `SYS-550`, `SYS-551`, `SYS-552`, `SYS-553`, `SYS-554`, `SYS-555`, `SYS-1094`, `SYS-1188`, `SYS-1189`, `SYS-1190`, `SYS-1191`, `SYS-1192`, `SYS-1193`, `SYS-1194`, `SYS-1195`, `SYS-1196` | material logistics, live resolution, modifiers, direct income and transfer |
| Constraint | `CON-188`, `CON-269`, `CON-273`, `CON-466`, `CON-467`, `CON-469`, `CON-470`, `CON-730`, `CON-731`, `CON-732` | stock, sight, target, population, sites and per-type caps |
| Information | `INF-059`, `INF-224`, `INF-225` | current versus remembered state and prerequisites |
| Objective | `OBJ-103` | civilization-wide Conquest |
| Time | `TIM-003` | simultaneous live processes with explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `452` (`GAME-0001`–`GAME-0452`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`28 / 56 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` Age of Empires II: Definitive Edition | Worker gathering/delivery, construction, housing, paid local queues, research, group commands, live combat, fog, dependency display and Conquest | Zeus adds labour-based Favor, exclusive patrons and one-use powers. Farms do not require reseeding, new Town Centers require predefined Settlements, and named advancement buildings replace the neighbour's building-count/Castle gate. Relic deposit, garrison work restoration and live Market/caravan decisions remain explicit; COMB-0177 does not transfer without its required CON-468. | Near 0.500000; not exact. |

## Taxonomy impact

`TAXONOMY_CHANGE_190` admits seventeen boundaries; thirty-eight existing genes are reused without rewriting an earlier definition, signature or verified combination. The named GAME-0453 salience/plain-language review partitions all fifty-five admitted uses after rereading this complete scope. Roles are interpretive, not inferred weights or rarity scores.

## Negative results

- No `CON-468`, `SYS-299`, `SYS-059`, `SYS-143`, turn-based caravan, repeated god cast, arbitrary Town Center footprint, pickup-activated relic bonus, unlimited shelter or campaign revival is inherited.
- Damaged source OCR, a current wiki and modern product branding do not establish original binary coefficients or direct play.
- Rule-derived cases and an illustrative artwork position do not become an executed match by being internally consistent.

## Delta summary

## New facts

- [Observation | Direct | High] Separate worship labour, exclusive patrons and once-only powers alter the live production-to-Conquest decisions (`AM-001`, `AM-003`, `AM-005`).

## New genes

- [Observation | Direct | High] `ACT-598`–`ACT-602`, `SYS-1188`–`SYS-1196`, `CON-730`–`CON-732`; class names and values remain parameters.

## New combinations

- [Observation | Limited | Medium] No new combination proposed; every existing proper subset is checked by the deterministic scan.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_190`; older canonical boundaries are unchanged.

## New questions

- How do an exact original-CD build, seeded map and ordinary trace resolve passage throughput, relic destruction and special-attack scheduling?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0454` *Rhythm Heaven* for Nintendo DS, next in selection 034 after this unit's acceptance and stop window.
- Optimisation criterion: alternate live economy and army control with prompted rhythmic input.
- Expected information gain: distinguish rhythm judgement and response gates from free movement or turn selection.
- Backlog impact: six approved subjects remain; no push, publication or deployment is authorised.
