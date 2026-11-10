---
game_id: GAME-0500
slug: pacific-drive
game_title: Pacific Drive
analysis_status: reviewed
reviewed: 2026-10-05
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-049
    - ACT-089
    - ACT-123
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-201
    - ACT-216
    - ACT-295
    - ACT-313
    - ACT-341
    - ACT-381
    - ACT-399
    - ACT-424
    - ACT-607
    - ACT-675
    - ACT-676
    - ACT-677
    - ACT-678
  system:
    - SYS-036
    - SYS-057
    - SYS-223
    - SYS-320
    - SYS-327
    - SYS-353
    - SYS-379
    - SYS-380
    - SYS-511
    - SYS-578
    - SYS-591
    - SYS-700
    - SYS-734
    - SYS-755
    - SYS-982
    - SYS-1203
    - SYS-1368
    - SYS-1369
    - SYS-1370
    - SYS-1371
    - SYS-1372
    - SYS-1373
    - SYS-1374
    - SYS-1375
    - SYS-1376
  constraint:
    - CON-175
    - CON-288
    - CON-297
    - CON-394
    - CON-496
    - CON-629
    - CON-770
    - CON-771
  information:
    - INF-119
    - INF-128
    - INF-132
    - INF-179
    - INF-302
    - INF-368
    - INF-476
    - INF-477
    - INF-478
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
    - TIM-034
---

# Game: Pacific Drive

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

This bounded reconstruction retains source-specific limitations. Research
review does not claim native execution or exact current executable parity.

## Analysis scope

- Version / ruleset: original full-release English Windows base game of 2024,
  Steam application `1458140`, reconstructed with the publisher's explicit
  PC `1.4.0` failure/save contract. The official post is titled 2024-03-19
  and was published 2024-03-20 UTC. Neither a later video upload nor a current
  store page establishes its capture build or current executable parity.
- Structured analysis target: original Windows base-release rules; keyboard
  and mouse, fresh story progression, ordinary unmodified personal/vehicle
  damage and three independently selected `Lose Most Items` penalties for
  `Failed Run`, `Abandon Trip` and `Abandon, Save, Quit`. This specifies the
  intended reproduction settings rather than claiming R1's hidden options.
  The structured platform record carries the same target and limitations.
- Entry: first ordinary control in the Auto Shop's `Fix the Car` task after
  scripted delivery and the introductory trip. Those predecessors establish
  the initial wagon, headset and supplies, not an additional admitted route.
- Primary decision loop: inspect personal health, local vehicle parts,
  faults, fuel, charge, known recipes and current ordered requirements;
  gather, fabricate, carry, install and repair the first wagon; prepare the
  selected Radio Station route; drive and leave the parked car to search,
  dismantle, scan and collect while retaining accessible inventory and
  vehicle state; complete the plasma and transmitter requirements; carry an
  anchor into the ARC; select a currently eligible remote gateway; then
  physically drive through the closing instability field to bank the trip.
- Positive terminal: cross the selected gateway and regain ordinary Auto
  Shop control with the successful `Trip Report` for Radio Station / `JCT E5`,
  before undertaking `Build Antenna`. Merely collecting plasma, a transmitter
  or an anchor, selecting a gateway, or reaching its light pillar is not
  successful settlement.
- Negative and interrupted terminals: critical personal failure or deliberate
  abandonment returns home with its separately configured carried-item
  penalty. `Abandon, Save, Quit` additionally saves that home state before
  leaving play. Ordinary field `Quit to Menu` instead discards unsaved
  current-level progression and resumes its entry state; it is not a mid-field
  suspend or the same home-return path.
- Included: complete initial garage preparation and first `Into the
  Wilderness` expedition; all causally available locomotion, vehicle controls,
  cargo rearrangement, recipe pinning, known fabrication/refinement, component
  mounting/repair, resource harvesting, healing and qualified slight recovery
  outside harm, local illumination/diversion,
  scan/log disclosure, navigation, short car recovery, anchors, exit legality,
  activated storm pressure and terminal persistence paths.
- Excluded: the setup-only `Delivery Window` / `Olympic Exclusion Zone`;
  subsequent `Build Antenna`, Fabrication Station research, garage expansion,
  `Car Maintenance`, `The Remnant Experiment`, further junctions and biomes;
  later equipment, independent progression, achievements and campaign ending;
  other platforms, accessibility-altered rules, mods, prelaunch demo or Early
  Access; 2025 `Suspend Run`, `Endless Expedition`, cosmetic DLC and
  `Whispers in the Woods`. No current wiki feature is imported merely because
  it now exists in the product.
- Reproduction: obtain the released original Windows rules and PC `1.4.0`
  persistence contract; use ordinary base options and select each stated loss
  penalty independently. Complete setup, then at the first garage control
  inspect the car, repair or replace the required components, obtain the
  Impact Hammer plan, refuel/charge and select Radio Station. Carry tools,
  healing and repair supplies, inspect at least one known recipe deficit,
  manufacture the required gear/hammer, scan a plasma source and separately
  collect its broken output, acquire the transmitter in the disclosed order,
  feed a carried anchor to the ARC and activate an eligible remote exit.
  Escape physically and inspect the retained car, contents and Trip Report.
  Test interruption alternatives from separate preparations, not by asserting
  that R1 reproduces every failure branch. Exact quantities, times, routes,
  radii, vehicle condition and consumable choices are parameters.
- Potential scoped modules: one later named investigation or junction packet;
  Fabrication Station and garage progression; one quirk diagnosis/repair;
  alternate penalties/difficulty modifiers; a later released mode or platform
  requires its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. R1 is attributed original PC review-copy
  footage, inspected through muted, paused frames in a separate headless
  process. It can contain edits omitting deaths, repeated travel or loading.
  Its executable, capture date, hidden options, entitlement and native timing
  are not verified. Official product and patch statements establish the
  released identity and save/penalty contract; independent firsthand written
  accounts support qualified qualitative mechanics. No source artwork,
  screenshot, recording or audio is distributed with the canonical record.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| PD-001 | App 1458140 identifies the released Windows base product, distinct from the later expansions and modes | Observation | Direct | High | P1 |
| PD-002 | The original packet runs from Fix the Car garage control through the complete first Into the Wilderness return, before Build Antenna | Observation | Direct | High | R1 836–4480, P2 |
| PD-003 | Recipes expose ingredients and source counts; accepted gear refinement consumes scrap and immediately credits gear, while a fabricated Crude Door becomes a held physical part before separate installation | Observation | Direct | High | R1 1223–1228, 1230, 2010–2022 |
| PD-004 | Fixed component mounts preserve distinct part condition, compatibility, local faults and remedies rather than one aggregate car health value | Observation | Direct | High | R1 940, 1230, 1320, 1340, 1380, 2510; D1 |
| PD-005 | Putty and compatible kits repair eligible part damage/faults; Flat and Loose Wheel have different remedy classes | Observation | Direct | High | R1 1280, 1300, 1320, 1340; S1 |
| PD-006 | Garage supplies replenish fuel and electrical charge; headlights and short recovery use a shared car battery, but the recording does not independently measure ordinary drain rates | Observation | Direct | Medium | R1 1520–1550, 2510, 3330, 4140, 4480; S1 |
| PD-007 | Retained personal/trunk grids, orientation, carried tools and quick slots constrain compatible collection and preparation | Observation | Direct | High | R1 1070, 1440, 2400, 3990; P3 |
| PD-008 | Contextual dismantling, aimed generator damage and separate material pickup have different action/result boundaries | Observation | Direct | High | R1 1190, 2330, 2440, 2450 |
| PD-009 | An acquired initial physical plan makes Impact Hammer fabrication known; held eligible scanning separately discloses object/anomaly log information | Observation | Direct | High | R1 940, 1510, 2010, 2070, 2180, 2450; S1 |
| PD-010 | Current ordered mission requirements and independently pinned recipe deficits update separately; pinning does not reserve ingredients or fabricate/install the output | Observation | Direct | High | R1 1120, 1205, 1223, 2420, 2450, 3330, 4270, 4280 |
| PD-011 | Personal health, radiation exposure, carried healing and vehicle repair remain distinct; a First Aid Kit declares Health 50 and restoration is capped | Observation | Direct | High | R1 2330, 2400, 2420, 2470, 4480 |
| PD-012 | Carrying one loose anchor into the passenger-side ARC converts it into typed exit energy; locating or carrying it alone does not charge the receiver | Observation | Direct | High | R1 3960, 4070, 4090, 4100, 4320, 4345; D1 |
| PD-013 | The local ARC map distinguishes free navigation pins from energy/radius-gated gateway selection; no solved safe road route is shown | Observation | Direct | Medium | R1 1580, 4140, 4160, 4320, 4345 |
| PD-014 | Perpetual Stability does not start the first site's storm clock on entry; Link Gateway initiates hazardous closure while physical escape remains necessary | Observation | Direct | High | R1 1580, 4345, 4360, 4420, 4480; D1 |
| PD-015 | Successful return retains eligible car/content state and does not demonstrate automatic full healing, component repair or recharging | Observation | Direct | High | R1 4480 |
| PD-016 | PC 1.4.0 defines three independently configured item-loss penalties and separates field Quit to Menu from abandon-to-garage saving | Observation | Direct | High | P2 |
| PD-017 | Original tool use wears finite durability and can break the tool; compatible locked-container use exhausts a nearly depleted Prybar and removes it from the carried slot | Observation | Direct | Medium | R1 1190, 2010, 2450, 2798, 2824–2834; P3, S3 |
| PD-018 | Original eligible anomalies react to proximity or perceived decoys; known Abductor fixation limits make universal diversion success an invalid claim | Observation | Direct | Medium | R1 2070, 2180; P3, S1, S2; L2 |
| PD-019 | Released Fuel Can transfers preserve the same container; Road Flare activation spends one unlit stock unit and its held or released finite burning state supplies local light | Observation | Direct | Medium | R1 625, 635, 655, 1980–2005; P4; S2, S3, L0 |
| PD-020 | The March 26 2024 manual transcription already describes slight recovery outside harm and separate healing; its exact amount, delay and native implementation are unverified | Observation | Limited | Medium | L0; native reproduction could refine or contradict the attributed transcription |

Sections inherit the listed claim IDs. Supporting transitions are closed at
the stated qualitative source quality, not promoted to exact native timings.
Repository and public-presentation acceptance remain separate unit gates.

## Basic data

- Release / origin: Ironwood Studios, published by Kepler Interactive;
  full release February 2024. P1's date representation is February 21, while
  the official announced calendar date is February 22; no different edition
  is inferred from that display difference.
- Platform or physical form: English Windows base game, keyboard/mouse;
  structured authority remains the analysisTarget record.
- Mechanical families: physical object/vehicle manipulation, live systemic
  pressure, typed inventory/fixture gates and ordered dependency progress. Membership
  must follow the reviewed existing family boundaries, not the market genre.
- Primary sources: P1 official product; P2/P3/P4 developer patch statements;
  R1 attributed original PC recording; S1/S2/S3 firsthand original-release
  written observations with their stated platform/build limitations.
- Secondary sources: L0 dated original and L1 current manual transcriptions,
  and L2 dated Abductor
  description are routing/corroboration, not independent native 2024 execution.
- Claim IDs: PD-001–PD-020.

## Mechanical decomposition

### Action Genes

- ACT-008/048/049 separate on-foot movement, physical object carry and local
  switches. Ignition, Park/Drive and lights require addressed control state;
  they do not make movement autonomous. ACT-201 directly steers the car.
- ACT-089/164/199/216/424/607 distinguish collection, active-tool selection,
  compatible transfer, container search, rectangular rearrangement and
  recoverable release. An anchor or door held in world space is not assumed
  to occupy an ordinary backpack footprint.
- ACT-123 requests a known manual recipe, whereas ACT-675 changes only its
  gathering checklist. ACT-341 addresses fixture/tool interactions; ACT-381
  commits held repair and ACT-399 supplies a compatible chargeable technology.
- ACT-131 spends eligible restorative stock. Its fit must retain the
  immediate effect boundary rather than silently asserting an unproved
  interrupted-use cancellation rule. ACT-295 is a kick; ACT-161 is the aimed
  Impact Hammer strike, not a firearm, ore-cell mine or ordinary contextual
  dismantle. ACT-313 is the headset's held eligible scan.
- ACT-676 changes a free navigation pin; ACT-677 commits an eligible remote
  gateway; ACT-678 requests the retained car's short relocation while the
  avatar remains outside. These do not collapse into one fast-travel command.
- Parameters: aim, input, reachable source, recipe, carried output, current
  quantities, orientation, compatible mounts and eligible map locations.
- Claim IDs: PD-003–PD-013, PD-017–PD-019.

### System Behaviour Genes

- SYS-036/320 govern free physical object/car motion and retained drivable
  vehicle state. SYS-327/578 preserve exposure and personal survival health;
  SYS-327 also accommodates the dated manual's limited outside-harm recovery
  without claiming full regeneration, a delay, cap or last-hit refund formula.
  The car's local faults do not substitute for the driver's health.
- SYS-591 resolves compatible resource harvest; SYS-755 breaks a destructible
  fixture after eligible damage; SYS-223 removes the exhausted tool after
  its compatible use, corroborated by the Prybar cabinet transition. Released
  materials still require ACT-089 acquisition.
- SYS-353 turns owned scrap into a retained refined gear in the demonstrated
  inventory recipe. SYS-1369 instead creates a separately held physical part;
  SYS-1368 adds a recipe from an acquired physical plan. A manual bench is
  not SYS-545's powered fabricator, and no later research tree is imported.
- SYS-700/734 settle eligible repair and technology supply. SYS-1370 preserves
  mounted-part properties/faults; SYS-1371 couples electrical consumers to
  one battery. SYS-1376 retains finite carried fuel contents
  and donor/receiver limits; fixed garage supplies are a separate parameter.
- SYS-982 records held scan disclosure. SYS-379 advances authored mission
  state; its compatible progression branch is reused without importing
  every earlier example's narrative alternatives or ally changes.
- SYS-057/511 preserve qualified perceived-target/proximity reactions, not
  omniscient pursuit or guaranteed distraction. SYS-1375 keeps
  a disposable light's active carried/released burning state. SYS-1203 retains
  eligible released objects for later recovery. SYS-380 resolves the car's
  accepted typed short relocation; the direct outside request is ACT-678.
- SYS-1372 turns a deposited anchor into ARC energy. SYS-1373 begins closing
  field pressure after eligible gateway activation; SYS-1374 settles success
  or configured failure/abandonment at home. Anchor energy remaining on the
  activation display does not prove an immediate debit or universal amount.
- Resolution order: prepare and validate action prerequisites; resolve the
  specific transfer/craft/repair/scan; update own, component and requirement
  state; continue live hazards where not paused; validate exit choice;
  activate closure; physically cross; retain or penalise the stated outcome.
  This is a causal order, not a reverse-engineered native event scheduler.
- Claim IDs: PD-003–PD-020.

### Constraint Genes

- CON-175 retains survival within the attempt; CON-288 requires controllable
  drivable-vehicle state and geometric travel legality.
- CON-297 checks known recipes, materials and compatible station capability;
  CON-394 checks non-overlapping rectangular cargo fit and orientation;
  CON-496 checks source/reach/tool compatibility and remaining durability.
- CON-629 restricts saving to allowed context. CON-770 requires typed ARC
  energy and an exit outside the current exclusion radius; CON-771 requires
  one compatible part class at its fixed mount, distinct from cargo fit.
- Scarce resources: personal health, local parts, compatible repair stock,
  tool durability, finite ingredients/cargo space, battery and ARC energy.
  Ordinary fuel state exists but its first-trip drain rate is not measured.
- Claim IDs: PD-003–PD-017.

### Information Genes

- INF-119/128/179 preserve own resource/state, item/equipment identity and
  local visible geometry. INF-132/302 retain known recipes and rectangular
  inventory state. INF-368 retains disclosed scan findings rather than
  omniscience about undiscovered anomalies or future areas.
- INF-476 separates component faults/remedies, fuel, charge and exposure.
  INF-477 exposes route conditions and local energy-gated escape candidates,
  not a safe solved road. INF-478 distinguishes the currently disclosed task
  from user-pinned gathering counts and output/installation completion.
- `SAFE` with a clock is time of day, not a storm countdown. A recipe's
  displayed consumption specification is interface information, not an
  independently timed engine measurement.
- Claim IDs: PD-003–PD-014, PD-017–PD-019.

### Objective Genes

- OBJ-155: complete the ordered authored first survival expedition and retain
  its successful handoff. Discovery, material acquisition, remote activation
  and the full product's ending are different boundaries.
- Critical failure and abandonment have configured settlement rather than
  irreversible deletion of the whole campaign or all earlier home storage.
- Claim IDs: PD-002, PD-010, PD-014–PD-016.

### Time Genes

- TIM-003: live movement/hazards coexist with declared paused inspection;
  R1's Logbook explicitly shows pause. Do not claim that every interaction
  screen halts the world or that its displayed clock measures danger.
- TIM-007: permitted garage saves preserve continuation and alternative
  preparation. TIM-034: ordinary quit/load in a field level restores its
  boundary snapshot rather than the latest position. These do not grant
  2025's later Suspend Run or automatic penalty-free expedition banking.
- Claim IDs: PD-009, PD-014, PD-016.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Known Crude Door, scrap 11/3, plastic 4/4, tape 5/3, glass 6/2 at R1 1223 | Complete the compatible workbench craft | Ingredients become 8, 0, 2 and 4; 1226–1227 show Carrying Crude Door; 1228 separately requests installation | Material expenditure and held output precede fixed-mount installation | PD-003 |
| Scrap 5 and gear 1 before R1 2020 | Craft one known Gear | R1 2021 shows scrap 2 and gear 2; hammer recipe now lacks required scrap | A refinement can satisfy one requirement while making another insufficient | PD-003 |
| Crude Door held, empty compatible car mount | Install the part | Later part inspection shows mounted door and condition | Having/crafting a part does not alone install it | PD-003, PD-004 |
| Damaged panel/bumper and putty stock | Commit compatible held repair | Eligible condition rises and putty stock falls | Personal healing, part repair and fault cure are distinct | PD-005 |
| Flat tyre versus Loose Wheel | Inspect their remedy lists | Flat accepts sealing/replacement; Loose Wheel requires mechanical remedy | Identical-looking impairment does not permit arbitrary repair stock | PD-004, PD-005 |
| Garage tank preparation incomplete | Address gas cap with fixed nozzle; charge at desk | Fuel task advances 28% to 95%; electrical desk shows connected | Distinct reserves and preparation requirements, no finite pump assertion | PD-006 |
| Generator intact and collected plasma quota 0/5 | Aim and strike with Impact Hammer, then collect released material | Generator breaks before separate quota increase to 2/5 | Destruction is not automatic pickup credit | PD-008 |
| Health 59 with a known First Aid Kit declaring Health 50 | Complete carried use | Later readout 100, consistent with capped restoration | High later health does not alone prove a cheat or unlimited recovery | PD-011 |
| Nearly depleted carried Prybar; locked Hazmat Cabinet at R1 2824 | Apply the compatible held tool | R1 2828 shows opened cabinet and empty quick slot 1; 2834 shows the tool absent from pack/hands while material pickup fills freed cells | Exhaustion removes the tool rather than retaining a merely weakened item; exact native final value is unmeasured | PD-017 |
| Road Flare stock 2, unlit at R1 1980 | Activate one flare | R1 1990 shows lit held flare and stock 1; 1998/2000 show illumination with a decreasing bar; P4 independently describes dropped lit flares and increased burn duration | Finite disposable light, not a recharging lamp or a guaranteed distraction | PD-018, PD-019 |
| Same retained Fuel Can, available after setup | Hold Siphon Fuel on an eligible donor, then Fill Tank on the wagon | R1 setup 635 shows can 24%; 655 shows same can 11% during delivery; L0 retains surplus in the can | Available retained-container transfer, not an additional admitted setup route or measured field fuel rate | PD-019 |
| Known recipe but no required Gear | Inspect, pin and attempt preparation | Missing ingredient is visible; pin alone does not spend/craft/install | Gathering checklist and legal craft are different state changes | PD-003, PD-010 |
| Outside avatar and nearby retained car | Hold T toward an eligible warp location | Display scans the placement before accepted recovery | Outside-operated vehicle relocation is not avatar teleport or direct steering | PD-006, PD-013 |
| Loose Stable Anchor; ARC not yet supplied | Carry anchor and deposit in passenger receiver | Physical anchor converts to displayed typed energy | Anchor possession is not backpack storage or immediate exit | PD-012 |
| Radio Station route preview | Inspect current conditions | Perpetual Stability and required 1 kLIM are disclosed | First-site storm is not asserted to begin at entry | PD-013, PD-014 |
| Charged ARC; visible exit candidates and exclusion circle | Select an eligible remote gateway and confirm Link Gateway | Exit becomes active; Drive Into Gateway and danger phase appear | Pin, legality, activation and traversal are separate | PD-013, PD-014 |
| Activated gateway; car still outside it | Drive through the hazardous closure and physically cross | Garage Trip Report shows SUCCESS / JCT E5, health 69, charge 12.7 and retained damaged parts | Successful settlement is not automatic full restoration | PD-014, PD-015 |
| Unsaved progression inside current field level | Ordinary Quit to Menu and reload | Official PC 1.4.0 resumes current level's start without its unsaved progression | No continuous mid-field suspend | PD-016 |
| Same expedition, three explicit ordinary penalty settings | Select abandonment-to-home save/quit instead | Configured loss applies; car returns to garage and home state is saved before menu | Quit-to-level-boundary and abandon-to-home are different contracts | PD-016 |

## Strategic and experiential structure

- Local decision: choose whether a disclosed repair/recipe deficit justifies
  leaving protection, spending a worn tool or carrying an awkward object.
- Medium-term planning: keep fuel, battery, local part condition and cargo
  separately viable, then position the car so an eligible exit remains
  reachable after activation. A pinned recipe does not reserve shared stock.
- Long-term structure within this packet: the prepared vehicle and collected
  contents must survive the complete return; later research remains excluded.
- Failure attribution: disclosed incompatibility, missing ingredients, local
  faults and exit eligibility can explain blocked actions. Unknown R1 options,
  native hazard rates and documented quest-order defects limit claims that
  every failure is transparent or avoidable.
- Player-trust factors: P2 clarifies three independent penalties and warns
  about unsaved-level loss. Treat known out-of-order Into the Wilderness or
  garage-quit softlocks as defects, not intentional additional mechanics.
- Claim IDs: PD-003–PD-020.

## Replay and variation

- Carried preparation, compatible repairs, approach, local pins, scavenge
  detours and activation timing can vary without changing the signature.
- D1/S2 describe fluctuating destinations in the product. This recording does
  not prove a seed, exact first-site generation algorithm or independently
  persistent whole-world map; none is added from a genre assumption.
- Distinct success/abandon/ordinary-quit branches motivate separate tests;
  edited footage does not establish continuous live performance.
- Claim IDs: PD-002, PD-006, PD-013–PD-020.

## Adjacent systems and history

- This is the original released Windows packet, not a union with the later
  survival settings, expansions or other platforms.
- The mathematically selected neighbour below shares retained preparation,
  embodied traversal and authored survival progress. Genre or visual
  similarity does not replace the complete prior-signature scan.
- Claim IDs: PD-001–PD-020.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-008, ACT-048, ACT-049, ACT-089, ACT-123, ACT-131, ACT-161, ACT-164, ACT-199, ACT-201, ACT-216, ACT-295, ACT-313, ACT-341, ACT-381, ACT-399, ACT-424, ACT-607, ACT-675, ACT-676, ACT-677, ACT-678 | 22 uses; input, item and location are parameters |
| System Behaviour | SYS-036, SYS-057, SYS-223, SYS-320, SYS-327, SYS-353, SYS-379, SYS-380, SYS-511, SYS-578, SYS-591, SYS-700, SYS-734, SYS-755, SYS-982, SYS-1203, SYS-1368, SYS-1369, SYS-1370, SYS-1371, SYS-1372, SYS-1373, SYS-1374, SYS-1375, SYS-1376 | 25 uses; source-qualified supporting transitions retained |
| Constraint | CON-175, CON-288, CON-297, CON-394, CON-496, CON-629, CON-770, CON-771 | 8 uses; no invented universal energy/radius |
| Information | INF-119, INF-128, INF-132, INF-179, INF-302, INF-368, INF-476, INF-477, INF-478 | 9 uses; only currently disclosed information |
| Objective | OBJ-155 | Complete retained first-return boundary |
| Time | TIM-003, TIM-007, TIM-034 | Live/paused inspection, home saves and interrupted field boundary |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `499` (`GAME-0001`–`GAME-0499`).
- Exact genome matches: none.
- Tied near matches: `GAME-0261` — The Last of Us Part I (`16 / 91 = 0.175824`).
- Supported combination subsets: none.
- Scan date: 2026-10-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0261 The Last of Us Part I | ACT-008/048/123/161/164/199/341, SYS-057/578, CON-297, INF-119/128/132, OBJ-155 and TIM-003/007 retain embodied traversal, held objects, known preparation, compatible carried equipment, perception, survival state and saved authored progress | The reviewed Quarantine Zone packet uses finite firearm preparation, unaware neutralisation, Listen Mode, authored companions and checkpoint restoration. Pacific Drive instead retains a component-based vehicle, distinct repair/charge/fuel state, scanned hazards, physical anchor-to-ARC energy, a selected remote exit, triggered storm escape and different level-boundary versus home-settlement paths | Near, 0.175824 |

- New genes: nineteen source-bounded operational additions; supporting
  transitions are closed at their stated qualitative evidence quality.
- Reused genes: forty-nine unchanged English boundaries; no earlier signature
  or definition may be mutated to accommodate this packet.
- Classification result: New gene.
- Evidence and reasoning: parameter-free complete signature, not a
  target gene quota. No exact match or proper verified combination subset;
  one new carrier does not establish a recurring new combination.

### Preserved research notes

- New genes: nineteen source-bounded operational additions; supporting
  transitions are closed at their stated qualitative evidence quality.
- Reused genes: forty-nine unchanged English boundaries; no earlier signature
  or definition may be mutated to accommodate this packet.
- Classification result: New gene.
- Evidence and reasoning: parameter-free complete signature, not a
  target gene quota. No exact match or proper verified combination subset;
  one new carrier does not establish a recurring new combination.

## Taxonomy impact

- Registry changes: ACT-675–678, SYS-1368–1376, CON-770–771,
  INF-476–478 and TIM-034.
- Taxonomy-change record: TAXONOMY_CHANGE_237.
- Candidate terms affected: no word or commercial genre gains an ID merely
  from similarity. Existing boundaries must remain unchanged.

## Negative results

- None as an independent negative-result record. Rejected substitute
  boundaries and uncertain observations remain local research dispositions,
  not changes to previously accepted signatures.

## Delta summary

## New facts

- [Observation | Direct | High] Door fabrication consumes the recipe stock
  into a held part before installation; refinement credits gear separately
  and can leave insufficient scrap for the next recipe; PD-003.
- [Observation | Corroborated | High] The first Perpetual Stability site
  becomes a pressured escape after selected gateway activation, not a storm
  timer assumed from entry or its time-of-day clock; PD-013, PD-014.
- [Observation | Direct | High] PC 1.4.0 separates unsaved current-level
  restoration from configured abandonment and saved garage return; PD-016.

## New genes

- [Observation | Limited | Medium] Nineteen source-bounded operational additions
  cover distinct request, fabrication/vehicle/exit/retention, eligibility,
  disclosure and persistence boundaries. Their individual evidence remains
  explicit, including the closed supporting-transition dispositions.

## New combinations

- [Observation | Direct | High] No new combinations; the complete
  scan finds no proper existing verified subset or new recurring carrier.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_237 reviews
  operational counterexamples without changing an earlier English boundary.
  No earlier signature or English operational definition changes.

## New questions

- [Hypothesis | Limited | Medium] Native original-rule reproduction may
  refine exact health-recovery amounts/delays, field fuel handling, burn
  lifetime and transfer rates. Qualitative tool-slot exhaustion, burning and
  retained fuel transfer have source-backed dispositions; the unmeasured
  parameters are not treated as proof of absence or new IDs.
- [Hypothesis | Limited | Medium] A native PC 1.4.0 reproduction may sharpen
  exit radius, energy debit timing, warp fallback and penalty exceptions.
  Reject any claim of exact binary parity based only on R1's upload date.

## Next recommended game

- [Hypothesis | Limited | Medium] Original Windows F.E.A.R. (2005), GAME-0501.
- Optimisation criterion: the maintainer-approved mixed-era/platform horizon,
  after this entire unit and its single local commit pass.
- Expected information gain: a released first-person combat packet may
  contrast embodied danger with the present repair/anchor/escape decisions.
- Backlog impact: original Homeworld remains future coverage. No next unit
  starts before complete unit acceptance; no push or publication is authorised.

## Why this game

- [Hypothesis | Limited | Medium] Released 2024 vehicle preparation and
  selected-exit survival fill the approved modern Windows slot without
  importing an Early Access product or claiming external novelty.

## Source ledger

- P1: [official Steam product, app 1458140](https://store.steampowered.com/app/1458140/Pacific_Drive/), checked 2026-10-05. Current modes/DLC are excluded.
- P2: [official developer PC 1.4.0 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5686430301712408263), iwblake, 2024-03-20T00:37:21Z; title dated March 19. Full original body retrieved through Valve's ISteamNews API; separate penalties, saving and documented ordering defects, not proof of R1's executable.
- P3: [official developer original 1.1.3 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5728086065187626864), iwblake, publication 1708742924, title dated 2024-02-22. Rotation/hand-slot repair, breakable hammer and known Abductor fixation; no universal diversion guarantee.
- R1: [fgw original PC walkthrough](https://www.youtube.com/watch?v=VylIMawVf6M), published 2024-08-22T08:00:35-07:00, declared runtime 54,455 seconds, actual player runtime 54,454.501. Creator declares review-copy footage and possible cuts. Paused frame inspection checks source identity, target time, dimensions, mute, pause, no advertisement and image digest. Source times above are seconds. No native play, capture date, hidden option or binary assertion.
- D1: [Blake Dove / Ironwood Studios developer loop](https://blog.playstation.com/2023/11/30/unravel-the-gameplay-loop-of-pacific-drive-launching-on-ps5-feb-22/), 2023-11-30. Prelaunch qualitative corroboration only, not a Windows patch or independent native test.
- S1: [Christopher Livingston's original firsthand account](https://www.pcgamer.com/pacific-drive-tips/), 2024-02-22, reports forty-plus hours. Used only for qualified kicking, scanning, short car recovery and repair classes; later deconstruction/upgrades excluded.
- S2: [TJ Denzer's firsthand PC-copy review](https://www.shacknews.com/article/138774/pacific-drive-review-score), 2024-02-20, early publisher copy. Used for qualified anomaly/flare observations. Its all-resource-loss account does not override the later explicit PC 1.4.0 selectable penalty contract.
- S3: [Adrian Hon's original firsthand account](https://mssv.net/2024/02/27/pacific-drive/), 2024-02-27, explicitly PS5. Qualitative fuel-can/tool/control corroboration, not independent Windows patch parity; its impressions do not prescribe a taxonomy.
- P4: [official developer original PC 1.1.1 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5728086065181124933), iwblake, publication 1708588864, title dated 2024-02-22. Full body read through Valve ISteamNews; lit-flare dropping, finite burn balance and interaction-warning fixes. No numeric rate or later weapon is imported.
- L0: [historical User Manual transcription](https://pacificdrive.wiki/index.php?title=User_Manual&oldid=2137), first revision published 2024-03-26T18:49:14Z. Complete historical wikitext and revision history inspected separately via MediaWiki. Community attribution, not native play or a developer-hosted manual; only qualified slight outside-harm recovery and retained fuel-transfer corroboration, with no thresholds/rates inferred.
- L1: [community User Manual transcription](https://pacificdrive.wiki/index.php?title=User_Manual&oldid=6881), last edit 2026-07-24. Current secondary routing only; uncertain unlocks and later manual text do not prove original full-release mechanics.
- L2: [dated community Abductor description](https://pacificdrive.wiki/index.php?oldid=4555&title=Abductor), 2024-12-14. Secondary proximity/diversion routing; later defensive equipment is excluded.
