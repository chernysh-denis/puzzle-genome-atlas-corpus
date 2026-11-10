---
game_id: GAME-0491
slug: elite
game_title: Elite
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-161
    - ACT-219
    - ACT-482
    - ACT-663
    - ACT-664
  system:
    - SYS-045
    - SYS-215
    - SYS-723
    - SYS-738
    - SYS-1312
    - SYS-1313
    - SYS-1314
    - SYS-1315
    - SYS-1316
    - SYS-1317
    - SYS-1318
    - SYS-1319
    - SYS-1320
    - SYS-1321
  constraint:
    - CON-571
    - CON-757
    - CON-758
    - CON-759
    - CON-760
  information:
    - INF-117
    - INF-277
    - INF-468
  objective:
    - OBJ-281
  time:
    - TIM-003
---

# Game: Elite — original BBC Micro disc first trading leg

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Prices, ship identities, tonnage, fuel range, pulse interval, chart coordinates
and government values are parameters, not separately named genes.

## Analysis scope

- Version / ruleset: original 1984 Acornsoft BBC Micro disc release, the
  `_IB_DISC` variant in Mark Moxon's documented reconstruction pinned at
  `5af23a31c33ad159ff0b33c9f304741b4bc05fd6`. Inspect its conditional branches,
  not the repository's default `_STH_DISC` bug-fixed build. No original binary
  identity, assembled-output parity or native execution is claimed.
- Structured analysis target: new `PLAT-BBC-MICRO`, supported by the Science
  Museum's Acorn BBC model B record. Original licensed physical disc rules,
  not cassette, Master, 6502 Second Processor, sideways RAM, Elite-A or a
  modern franchise release. Other platform releases remain unassessed.
- Primary decision loop: read local prices, quantity, cash and unit-specific
  hold occupancy; inspect chart distance, economy and government; buy a cargo
  quantity or affordable fourth missile; depart once; change throttle, pitch,
  roll and view, select a fuel-reachable system, request hyperspace or an
  eligible local shortcut, fire the front pulse laser or arm/acquire/fire a
  missile; let live flight, attacks, regeneration, heat, law and possible
  misjump resolve; approach a station and match its rotating entrance; decide
  how much surviving cargo to sell and evaluate the retained cash outcome.
- Entry and exit: stock Jameson docked at Lave, 100 credits, full 7.0-light-year
  fuel, empty 20-tonne hold, front pulse laser, three missiles, clean legal
  state, zero tally and no optional equipment. Begin before choosing initial
  cargo and destination. Include one departure and its complete path to the
  next docking and cargo-sale decision, or death. Returning to Lave closes
  this leg too; it is not a loophole for a second launch or later equipment.
  Intermediate hyperspace diversions and misjump escape remain inside the
  flight. The sale decision may be partial or zero; no mandatory positive
  profit, externally imposed deadline or whole-game victory is invented.
- Included: all affordable initial commodity choices, including available
  contraband and small-unit goods; optional fourth missile at 30 credits;
  direct speed/pitch/roll, four views, front pulse heat/pulsing and shared
  energy debit; T acquisition, U cancellation, M successful launch, guided
  pursuit, enemy missiles and capable enemy E.C.M.; range checks, live
  countdown, cancellation and random witchspace with Thargoids, no station
  and remaining fuel risk; mass-locked local J shortcut; loaded-blueprint
  encounter limits, traders, police and pirates; front/rear shields, energy
  regeneration and threshold-paid shield charging, terminal damage and
  sampled cargo-class loss; legal contraband, protected-target/station anger,
  police-kill mark and normal-arrival decay; planet collision, solar cabin
  heating, station approach/roll alignment, slow bad bump and fast bad death;
  combat tally and conditional bounty; local economy, cockpit and chart data.
  Flight continues on information screens: no safe chart pause is inferred.
- Excluded: all later trading legs, further spending after this terminal,
  explicit save/load and recovery as another attempt, missions, other galaxies,
  galactic drive, mining, fuel/cargo scooping, energy bomb, escape pod, docking
  computer, own E.C.M., extra energy unit and non-front lasers. Initial cash
  cannot buy their cheapest 400-credit module; bounty money cannot be spent
  before the terminal station. Player stock has no scoop merely because
  enemies drop cargo. Original `_IB_DISC` ordinary asteroid spawning is
  suppressed by its retained test jump; later fixes do not supply asteroids
  to this signature. No alternate toggles, deliberate refund/hyperspace
  exploit, emulator convenience, imported save or later port rule is admitted.
- Potential scoped modules: a named equipped trading leg, intentional mining
  with a specified bug-fixed disc revision, a complete Constrictor mission,
  another galaxy or an explicitly evidenced save/recovery cycle.
- Direct-play status: not conducted. The complete creator draft guide
  Version 7, 1984-03-24, with Ian Bell's 2015 preface, was read. It is not a
  final published-disc numeric authority: its 25-credit missile differs from
  the inspected 30-credit table. Docked and flight source text at the pinned
  reconstruction commit and the researcher's own related articles were read.
  No ROM/disc image, original Commander file, native executable, emulator,
  assembly/CRC reproduction, game video/audio or input trace was used.
  Repository transition reasoning below is not personal flight. The creator
  guide was retrieved by HTTP after a hostname-certificate error on HTTPS;
  certificate verification was not disabled.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `EL-001` | A self-financed buy/travel/dock/sell leg uses stock Jameson with 100 credits, 7.0 fuel, 20 tonnes, front pulse and three missiles | Confirmed | Direct | High | P1 trading; P2 Commander/default and PRXS; P3 |
| `EL-002` | Visit economy/fluctuation prices remain fixed under trades; buys debit offered stock, sales do not restore it; tonne and small-unit capacity differ | Confirmed | Direct | High | P2 TT151, GVL, TT219, TT210, tnpr; P4 |
| `EL-003` | Charts and system data expose distance, economy, government and technology, not future sampled quotes or exact ships | Confirmed | Direct | High | P1 red-key charts/data; P2 chart/report routines |
| `EL-004` | Stock front pulses and T/U/M missile acquisition/fire differ from own unavailable E.C.M.; capable enemies can disrupt missiles | Confirmed | Direct | High | P2 flight parts 3, 11, FRMIS, TACTICS |
| `EL-005` | Undocked nonzero in-fuel hyperspace counts down live, spends distance and can misjump to hostile stationless space | Confirmed | Direct | High | P2 hyp, wW, TT102, TT18, MJP |
| `EL-006` | Local J checks significant craft, station, witchspace and forward bodies, then moves planet/sun while minor objects remain local | Confirmed | Direct | High | P2 WARP |
| `EL-007` | Directional shields overflow into common energy; lasers and threshold-gated shield recharge consume that regenerating bank | Confirmed | Direct | High | P2 OOPS, DENGY, SHD, LASLI, flight part 13 |
| `EL-008` | Launch contraband, protected-target anger, police destruction and normal-arrival legal decay are distinct causal rules | Confirmed | Direct | High | P2 BAD, TT110, ANGRY, SOLAR, flight part 12 |
| `EL-009` | Government/law/local-state spawning is limited by the current blueprint file; first `_IB_DISC` retains the asteroid-suppressing jump | Confirmed | Direct | High | P2 main game loop, LOMOD, NWSHP; P5–P6 |
| `EL-010` | Qualifying survived shield overflow can clear an entire carried class; occupied message state also gates this loss | Confirmed | Direct | High | P2 OOPS, OUCH |
| `EL-011` | Planet altitude and sun-distance cabin-heat checks can kill the ship; absent scoops do not grant solar refuelling | Confirmed | Direct | High | P2 flight part 15 |
| `EL-012` | Qualifying ship or missile tally and cash bounty have different predicates; occupied message state or witchspace can skip cash credit | Confirmed | Direct | High | P2 EXNO2, flight part 12 |
| `EL-013` | Disc ISDK accepts friendly approach/entry/roll alignment; a slow bad bump damages, a faster bad collision kills | Confirmed | Direct | High | P2 ISDK; P7 only with disc-specific correction |
| `EL-014` | The bounded next-docking sale checkpoint is an analytical leg boundary, not the product's victory or a guaranteed gain | Observation | Direct | High | P1 trading loop; P2 market and continuing Commander state |

## Basic data

- Release / origin: David Braben and Ian Bell; Acornsoft, original 1984 BBC
  Micro disc. No exact retail day, current ownership or native checksum claim.
- Platform or physical form: BBC Micro keyboard-controlled licensed disc;
  source archaeology identifies the first release independently of later
  bug-fixed versions. The new platform identity is not Acorn Archimedes.
- Puzzle family: spatial physics, tactical counterplay, live system pressure
  and ordered resource/departure/arrival dependencies. All seventeen current
  family boundaries were tested. No one-game family or authored-network,
  hidden-state puzzle, employer-fixture delivery or party roster is invented.
- Primary sources, accessed 2026-10-04:
  - **P1:** [Ian Bell's creator draft Players' Guide](http://www.elitehomepage.org/playguide.htm),
    Version 7 dated 1984-03-24, with 2015-08-26 creator preface. Entire text
    read; supports trade purpose, controls and qualitative risk. Future
    preview, prototype prices and promises are not final disc facts.
  - **P2:** Mark Moxon's own documented source reconstruction,
    [docked code](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/5af23a31c33ad159ff0b33c9f304741b4bc05fd6/1-source-files/main-sources/elite-source-docked.asm)
    and [flight code](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/5af23a31c33ad159ff0b33c9f304741b4bc05fd6/1-source-files/main-sources/elite-source-flight.asm).
    Exact text/conditional rules, not an asserted original author ASM file or
    locally reproduced executable. Comment and instruction disagreements
    use instructions: small-unit total 200 is rejected; MCNT mod 8 gives
    shield recharge scheduling, not the surrounding prose's seven loops.
  - **P3:** [Commander save/default structures](https://elite.bbcelite.com/deep_dives/commander_save_files.html),
    the researcher's own original analysis of the current/last-saved buffers.
  - **P4:** [Market price/availability analysis](https://elite.bbcelite.com/deep_dives/market_item_prices_and_availability.html).
    Compare each actual disc routine; no transaction-volume elasticity.
  - **P5:** [Documented disc release differences](https://elite.bbcelite.com/disc/releases.html),
    original `_IB_DISC` versus fixed `_STH_DISC` and sideways RAM.
  - **P6:** [Disc blueprint-file analysis](https://elite.bbcelite.com/deep_dives/ship_blueprints_in_the_disc_version.html).
    Only currently loaded designs can instantiate; witchspace installs its
    Thargoid packet. This is not the Second Processor all-ships rule.
  - **P7:** [Docking-check analysis](https://elite.bbcelite.com/deep_dives/docking_checks.html),
    used only alongside disc ISDK: do not import its generic third check or
    33.6-degree roll statement into the disc's omitted check/36.6 comment.
  - **P8:** [Science Museum Acorn BBC model B](https://collection.sciencemuseumgroup.org.uk/objects/co64142/bbc-model-b-microcomputer),
    platform identity only; no museum image or unsupported release audit.
- Secondary sources: none required for the admitted mechanical claims.
- Claim IDs: `EL-001`–`EL-014`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008` directly navigate the persistent craft with local inputs;
  `ACT-130` offered cargo/missile purchase; `ACT-161` aimed legal discharge;
  `ACT-219` irreversible sale of owned cargo; `ACT-482` chart destination and
  committed inter-system travel.
- New: `ACT-663` arm/acquire/cancel a finite missile's stored target;
  `ACT-664` request one mass-eligible directional local shortcut.
- Parameters: cargo class and quantity, price, speed, pitch, roll, current
  view, missile stock/arming/target, destination, range and shortcut request.
- Claim IDs: `EL-001`–`EL-006`.

### System Behaviour Genes

- Existing: `SYS-045` hostile autonomous movement; `SYS-215` live attack/hit
  resolution; `SYS-723` integrated craft motion and damaging contact;
  `SYS-738` shot heat and passive cooling, with no active-cooling window.
- New: `SYS-1312` visit-priced commodity/cash settlement; `SYS-1313` live
  distance-fuel hyperspace and misjump; `SYS-1314` local body displacement;
  `SYS-1315` directional shields sharing laser/recharge/survival energy;
  `SYS-1316` cargo/target legal state and arrival decay; `SYS-1317` conditional
  loaded-blueprint encounter creation; `SYS-1318` guided missiles and enemy
  disruption and nearby destruction damage; `SYS-1319` sampled whole-class cargo loss; `SYS-1320` celestial
  altitude/thermal defeat; `SYS-1321` tally and conditional bounty settlement.
- Parameters: economy/table/visit byte, remaining fuel, countdown and
  misjump, local positions, shields/bank threshold, law/hostility, blueprint,
  target/field, damaged class, altitude/heat, tally and cash predicates.
- Claim IDs: `EL-002`, `EL-004`–`EL-013`.

### Constraint Genes

- Existing: `CON-571` heat-gated discharge; pulse and view readiness remain
  instance conditions, not fictitious carried laser ammunition.
- New: `CON-757` funds/stock plus tonne-shared or small-unit-specific load;
  `CON-758` undocked nonzero range fuel without concurrent countdown;
  `CON-759` mass/station/witchspace/forward-body local-jump refusal;
  `CON-760` friendly aligned rotating-mouth docking with bad-contact fallback.
- Parameters: unit and quantity bounds, money and stock, current fuel,
  destination distance, local masses, station permission, entry and roll.
- Claim IDs: `EL-002`, `EL-004`–`EL-007`, `EL-013`.

### Information Genes

- Existing: `INF-117` pre-commit cash/stock/price offers; `INF-277` cockpit
  resources, scanner/compass, weapons and threat cues currently applicable.
- New: `INF-468` chart distance/economy/government/technology without future
  market fluctuation or exact encounter disclosure. Commander legal status
  is shown in the status view, not an invented moral-honour meter.
- Parameters: current offers, balance, owned and available quantity, cockpit
  shields/energy/fuel/heat/missiles, local targets and selected system data.
- Claim IDs: `EL-001`–`EL-004`, `EL-007`–`EL-013`.

### Objective Genes

- New `OBJ-281`: complete a personally financed cargo leg and evaluate its
  surviving resale and capital, not an employer manifest or score victory.
- Parameters: acquisition and optional missile costs, retained cargo,
  next station, selected sale quantity, proceeds and current capital.
- Claim IDs: `EL-001`, `EL-014`.

### Time Genes

- Existing `TIM-003`: outside explicit pause, ship motion, hostile tactics,
  damage, recovery and hyperspace countdown continue while inputs remain.
  Non-space charts suppress aim/space drawing, not the whole flight loop.
  Docked transactions lack flight pressure; they do not create turn combat.
- Parameters: main-loop schedule, screen type, pulse timer, recharge cadence,
  countdown, docking boundary and explicit pause.
- Claim IDs: `EL-004`–`EL-013`.

## Reproducible transitions

These are source-derived rule traces, not executed native flight.

| Entry and command | Accepted transition | Refusal or counterexample |
|---|---|---|
| Fresh Jameson buys offered food | Cash decreases, held food rises, AVL food falls at the same quote | Quantity beyond cash/stock/tonnage is rejected |
| Sell part of that food in the same visit | Own stock decreases and cash rises at the current quote | AVL is not replenished and a price increase is not inferred |
| Fill the standard tonne bay | Twenty total tonnes fit | A twenty-first tonne fails; a small-unit class uses its different bound |
| Buy one optional stock missile | Spend 30 credits, three become four | A fifth is refused/refunded; 25 is the earlier draft price, not this table |
| Request H while docked or to the current system | No countdown starts | A different in-fuel destination must be selected while undocked |
| Spend six of seven light years | One light year's fuel remains at jump resolution | An additional two-light-year request is out of range |
| Complete hyperspace with the misjump predicate | Fuel is spent and the Thargoid interstitial packet replaces normal arrival | No ordinary station or guaranteed in-fuel escape is invented |
| Request J with a station/significant ship or in witchspace | Local shortcut refuses | Minor debris alone is not the significant-craft predicate |
| T, crosshair acquisition, then M | Store an eligible target, launch if a universe slot exists, consume one missile | U clears acquisition; failed launch does not consume the missile |
| Enemy activates eligible E.C.M. | The active field can remove missiles, including the player's | Stock Jameson cannot issue the same defence without owned equipment |
| A missile is destroyed sufficiently close to Jameson | Its destruction can inflict local damage | E.C.M. removal is not necessarily harmless; a destroyed missile is not a destroyed enemy ship |
| Laser heat at or above native threshold | New discharge refuses while passive cooling advances | Rear/side views have no fitted stock laser; pulse readiness also applies |
| Incoming front damage exceeds front shield | Front shield becomes zero, excess drains common energy | Aft shield is not automatically pooled or manually rebalanced |
| Scheduled regeneration with banks below half threshold | Energy recovers but shields do not receive threshold-gated charge | Above threshold, charging each deficient shield spends bank energy |
| Survived unshielded damage and accepted OUCH class | Entire held quantity of the sampled class becomes zero | Empty class, failed sample or occupied message refuses that loss |
| Launch contraband / attack protected ship | Raise legal evaluation / anger station through separate predicates | A normal system arrival halves FIST, not all persistent state |
| Remove a qualifying destroyed ship or missile | Tally can increase and eligible nonzero ship bounty can credit cash | Witchspace or DLY occupancy can suppress cash; an explosion alone proves neither |
| Approach friendly rotating entrance with accepted alignment | Dock and expose the arrival market/sale decision | Bad contact at DELTA below five dents; faster bad contact kills |
| Continue toward planet or excessive sun heat | Altitude/thermal boundary kills this attempt | No planet landing or scoop-based fuel restoration without equipment |

## Strategic and experiential structure

- Local decision: preserve aim and energy while avoiding collision, choose
  whether to spend a finite missile, or wait for a safe local shortcut.
- Medium-term planning: allocate 100 credits between cargo and the optional
  fourth missile; choose a fuel-reachable economy and retain sufficient energy,
  cargo and fuel for docking or a misjump diversion.
- Long-term structure: subsequent trading, upgrades and missions are excluded.
- Common heuristics: read unit-specific capacity and current offers, compare
  chart distance with remaining fuel, avoid protected targets and match the
  rotating station mouth before contact. These are not guaranteed profit.
- Failure attribution: distinguish price/capacity refusal, mass lock, spent
  fuel, shield overflow, cargo-class loss, hostile docking and terminal impact.
- Player-trust factors: charts are not safe pauses or future-price previews;
  combat tally does not guarantee cash. Source comments are checked against
  instructions and original-release conditions.
- Claim IDs: `EL-001`–`EL-014`.

## Replay and variation

- What changes between sessions: cargo, destination, route, encounter state,
  expenditure, damage, surviving stock and chosen sale quantity.
- Randomness or procedural generation: seeded system data, arrival-market
  fluctuation, conditional encounters, misjump and damage sampling. The initial
  Commander market is predefined. No independent sampling probabilities or
  emulator timing are asserted.
- Multiple viable strategies: commodity/unit selection, shorter or longer
  reachable travel, avoiding or fighting traffic, missile expenditure and
  partial sale. Each remains subject to the complete flight/docking rules.
- Typical replay motive: improve retained capital and survival through a
  different leg; not an invented first-leg victory score.
- Claim IDs: `EL-001`–`EL-014`.

## Adjacent systems and history

- Direct predecessors: none established as a mechanical genealogy claim.
- Variants: original disc is separated from cassette, fixed disc, Master,
  Second Processor and later franchise products.
- Important differences: own-financed cargo settlement, live fuel-distance
  travel, loaded-blueprint threats and rotating-mouth docking are not an
  employer contract, responsive order book or automatically safe fast travel.
- Claim IDs: `EL-001`–`EL-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-219`, `ACT-482`, `ACT-663`, `ACT-664` | Local control, quantity, destination, target and shortcut |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-723`, `SYS-738`, `SYS-1312`, `SYS-1313`, `SYS-1314`, `SYS-1315`, `SYS-1316`, `SYS-1317`, `SYS-1318`, `SYS-1319`, `SYS-1320`, `SYS-1321` | Prices, fuel, movement, bank, law, encounters and settlement |
| Constraint | `CON-571`, `CON-757`, `CON-758`, `CON-759`, `CON-760` | Heat, storage, range, local mass and docking alignment |
| Information | `INF-117`, `INF-277`, `INF-468` | Market, cockpit and selected-system disclosure |
| Objective | `OBJ-281` | Self-financed leg and chosen sale checkpoint |
| Time | `TIM-003` | Live flight, countdown and explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `490` (`GAME-0001`–`GAME-0490`).
- Exact genome matches: none.
- Tied near matches: `GAME-0405` — Fable II (`6 / 41 = 0.146341`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0405` Fable II | Direct movement, purchase, aimed attacks, current transaction disclosure, live combat and real-time input | Its childhood one-coin errands and purchased music-box activation do not imply spacecraft, unit-priced cargo, fuel-distance flight, directional shields, missile targeting, manual rotating-mouth docking or self-financed sale settlement; shared generic inputs are not historical derivation or full gameplay equivalence | Tied near: `6 / 41 = 0.146341` |

## Taxonomy impact

- Registry changes: `ACT-663`–`ACT-664`, `SYS-1312`–`SYS-1321`,
  `CON-757`–`CON-760`, `INF-468`, `OBJ-281`.
- Taxonomy-change record:
  [TAXONOMY_CHANGE_228](../../../research/taxonomy-changes/TAXONOMY_CHANGE_228.md).
- Candidate terms affected: none promoted by lexical or duplicate routing.

## Negative results

- No new combination is asserted for one independently analysed carrier.
- Self-financed visit-priced cargo risk differs from employer delivery,
  autonomous ship-route editing and volume-responsive exchange. Sharing a
  trader theme does not establish the same complete signature.
- Directional shield overflow into laser/recharge energy differs from
  undirected shield-plus-hull and player-transferred deflector systems.
- A future equipped, bug-fixed or mission packet must be separately scoped;
  it cannot retroactively turn stock Jameson into a mining/ECM platform.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original disc instructions distinguish fixed
  visit prices, unit-specific load, conditional tally/bounty, live chart use
  and manual docking; `EL-002`–`EL-013`.

## New genes

- [Confirmed | Direct | High] Eighteen bounded additions with thirteen
  unchanged transfers; `TAXONOMY_CHANGE_228`.

## New combinations

- [Observation | Direct | High] No new recurring combination asserted.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_228`; no earlier signature,
  verified combination or production mapping is changed.

## New questions

- Native first-disc binary, timing, input traces and reproducible assembly
  parity remain uninspected; separate release and equipped-leg reviews would
  need their own evidence.

## Next recommended game

Continue with `GAME-0492`, *Resistance: Fall of Man*, original PlayStation 3
rules, in the next recorded unit. This game does not authorise push,
public-corpus publication or deployment.

## Why this game

- [Hypothesis | Limited | Medium] Preserve the approved varied-platform order
  and test original own-capital flight/trading boundaries, not a modern space
  genre assumption.
