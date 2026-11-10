---
game_id: GAME-0509
slug: mechassault
game_title: MechAssault
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-170
    - ACT-550
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-755
    - SYS-1432
    - SYS-1433
    - SYS-1434
    - SYS-1435
    - SYS-1436
  constraint:
    - CON-175
    - CON-269
    - CON-571
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-480
    - INF-495
  objective:
    - OBJ-185
  time:
    - TIM-003
---

# Game: MechAssault — complete first Cougar sortie

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Weapon labels, chassis statistics, colors, salvage counts, geometry, input
bindings, heat/fuel rates and the named headquarters are parameters, not genes.

## Analysis scope

- Version / ruleset: Original English Xbox retail base MechAssault campaign, complete first Going
  Down Hard mission. The 2002 product is reconstructed from Microsoft booklet
  X09-46559 printed 0103, the licensed Prima guide scan carrying copyright 2004,
  a dated 2002 review and attributed Xbox-labelled frames published 2016-12-16.
  These dates are not a verified launch disc checksum, patch identifier, region,
  captured difficulty or mod audit. No later DLC, sequel or current emulator
  parity is assumed.
- Structured analysis target: PLAT-XBOX, original English retail base campaign;
  knowledge/platforms/games.json is authoritative. No release-platform audit is
  implied.
- Primary decision loop: Steer the fixed Cougar and aim its torso independently, choose its installed
  weapon category, place shots or gain missile lock, alternate fire and cooling,
  use fuel-limited jump jets to cross the blocking ridge or change exposure, and
  decide when to collect armor or typed weapon salvage. Continue through the
  small base, convoy and main-base defenders, demolish the headquarters while
  surviving, accept Mission Successful and stop at exposed Suffer the Silence
  availability before its deployment.
- Entry and exit: The first mission briefing and its sole Cougar selection, followed by ordinary
  control near the crashed Icarus. Include all reachable first-mission
  alternatives rather than only the recorded firing sequence. Positive exit is
  headquarters destruction, Mission Successful and the next mission
  briefing/menu; the observed successor also offers Puma, but no second-mission
  movement or weapons are admitted. Returning physically to Icarus is not
  imposed as an extra first-mission terminal: P2 and the successful recorded
  route finish at the headquarters.
- Included: Direct ground movement and independent torso aim; installed Pulse Lasers,
  Autocannon and Javelin category selection/fire; range, impact, splash and
  recycle cadence as combat parameters; held timed missile acquisition/loss and
  lock-conditioned guidance; shared weapon/jump-jet heat, passive dissipation
  and documented shallow-water cooling/movement tradeoff; held fuel-limited
  lift, gravity/support return and source-qualified reserve recovery;
  ordinary-infantry foot crushing, transported infantry, moving convoy, tanks,
  helicopters, turrets and hybrid power armor; retained armor damage and
  compatible capped recovery; eligible building/vehicle destruction, linked
  falling-building damage and salvage output; energy/ballistic/missile
  promotion, finite stronger-tier consumption and automatic fallback; partial
  local scene, equipped-state and personal-resource HUD, class-filtered sensor
  contacts, current objective instructions and terminal successor availability.
- Excluded: Other missions, selecting among multiple playable chassis during this first
  mission, loadout customization, PPC/Gauss/Hammer weapons, Null Signature,
  Target Jamming, AMS/chaff, hostile full BattleMechs and reactor chain
  explosions, pilot dismount/hijacking, multiplayer, System Link, Xbox Live,
  DLC, whole-campaign unlocks, score/achievement farming, save/reload durability
  experiments, deep-water/lava rules not established on this packet, hidden
  enemy-generation probabilities and exact coefficients. No universal foot-crush
  rule for powered armor, heat reset on weapon selection, unlimited flight or
  perfect homing impact is claimed.
- Potential scoped modules: A later chassis-selection mission, enemy-mech/defensive-countermeasure combat,
  deep-water/lava traversal or multiplayer requires its own dated complete
  packet. No module ID is allocated. Native disc/patch/difficulty, heat/fuel
  timing, resumption and damage measurements remain open, not missing facts
  filled by assumptions.
- Direct-play status: No own native executable, controller input, original save, reload or hardware
  test was performed. P1 and the relevant P2
  weapon/equipment/terrain/combat/first-mission pages were read, including the
  actual first-mission map; the entire strategy book was not claimed as read. R1
  is EightBitHD’s Xbox-labelled walkthrough, published 2016-12-16, metadata
  length 14338 seconds. Selected paused frames were inspected with matching
  video identity, actual duration, muted state, target-time and no-ad checks:
  80/160/180/190/210/240/245/255/265/280/315/350/370/390/420/470/500/525/530/535/545/560/570/580/610/700.
  Mission Successful is visible at 530 and the successor briefing at 580. Frames
  from successor selection/deployment are exclusion checks, not admitted
  mechanics. This is attributed sampled observation, not continuous direct play
  or proof of captured difficulty, unmodified software, exact frame timing or
  persistent save reload. Fuel recovery remains Limited/Medium qualitative
  evidence. Research playback stayed headless, muted and paused; no
  foreground/fullscreen, focus, user-window, user-tab or system-sound change
  occurred. No audio was played or analyzed. Source frames and working prompts
  remain outside Git; original illustration is not an official asset or copied
  screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| MA-001 | Microsoft announces Xbox in-store availability on 2002-11-12; documentary print and recording dates do not establish the captured disc build. | Observation | Direct | High | P3; P1 imprint; P2 copyright; R1 metadata |
| MA-002 | The complete first mission uses only Cougar and closes at headquarters demolition and exposed successor availability, not at a fabricated return-to-Icarus requirement. | Observation | Corroborated | High | P2 p36–38; S2 first mission; R1 180/190/530/580/610 |
| MA-003 | Ground movement and torso aiming are independently commanded; the installed category can be selected without firing or spending its ammunition. | Observation | Corroborated | High | P1 controller/p3/p4; P2 Cougar; S1 controls; R1 255/315/350 |
| MA-004 | Held equipped jets cross the blocking ridge using finite flight reserve and return to supported traversal; qualitative later usable reserve does not prove exact recovery scheduling. | Observation | Limited | Medium | P1 p8; P2 p9/p25/p37; R1 240/245/255/265; S2 special/recharge tip |
| MA-005 | Weapons and jets share chassis heat; overheat prevents renewed fire until cooling, and documented shallow water accelerates cooling while slowing movement. | Observation | Corroborated | High | P1 p3/p8; P2 p9/p26/p31; S1 heat |
| MA-006 | Matching salvage advances or refills finite stronger weapon tiers; exhaustion supplies a lower tier and eventually unlimited weaker base fire, while full top-tier supply rejects matching pickup. | Observation | Corroborated | High | P1 p3/p8; P2 p33–34; R1 315/350/370/390/470/500/525 |
| MA-007 | Sustained aim acquires a missile lock, delayed aim departure loses it, and Javelin guidance is conditioned on acquisition rather than a guaranteed impact. | Observation | Direct | High | P1 p7; P2 weapon account |
| MA-008 | Ordinary infantry may be crushed underfoot; powered armor, turrets, vehicles and helicopters retain their own combat eligibility instead of universal contact defeat. | Observation | Corroborated | High | P2 p20/p37–38; S2 infantry/first mission; R1 210/420/470 |
| MA-009 | Armor damage persists across the sortie; compatible salvage heals missing armor up to capacity, while zero armor ends the attempt. | Observation | Corroborated | High | P1 p3/p8; P2 p34; R1 resource HUD |
| MA-010 | The sensor omits foot soldiers, classifies eligible local threats and switches objective disclosure between an outside-range bearing and an in-range mark; local view is separately partial. | Observation | Direct | High | P1 p3; R1 210/265/350/470/525 |
| MA-011 | Eligible structures and vehicles can be destroyed into debris, linked damage or salvage; destroying the first base's tall structures can take out its grounded helicopter. | Observation | Corroborated | High | P1 p8; P2 p23/p35/p37; R1 265/280 |
| MA-012 | Current actionable instructions change as the route reaches base, convoy and headquarters stages; live combat/movement continue outside pause without a universal mission deadline. | Observation | Corroborated | High | P2 p36–38; S2 first mission; R1 160/240/255/350/420/530 |
| MA-013 | Six bounded additions and seventeen unchanged transfers encode this packet without changing earlier definitions or signatures. | Observation | Direct | High | Registry boundary review; TAXONOMY_CHANGE_246 |
| MA-014 | The exact complete prior-signature scan has no exact match, three tied selected neighbours and no proper verified combination subset. | Observation | Direct | High | Corpus comparison; deterministic validator |

## Basic data

- Release / origin: Day 1 Studios and Microsoft Game Studios, Xbox 2002.
  P3 announces retail availability on November 12, not an exact captured-build
  date. Original platform identity is PLAT-XBOX; successor-console compatibility
  and every port are not inferred.
- Mechanical family: existing FAM-010 real-time system pressure. Weapon
  recovery, shared cooling, reserve flight, moving threats and retained damage
  constrain live interventions. No one-game family is invented.
- P1: [Microsoft Xbox instructions, X09-46559](https://www.gamesdatabase.org/Media/SYSTEM/Microsoft_Xbox/Manual/formated/MechAssault_-_Microsoft_Game_Studios.pdf),
  18-page scan, print code 0103. The same booklet was retrieved through the
  [document mirror](https://db.hfsplay.fr/files/2020/06/19/MechAssault_-_Microsoft_Game_Studios_zucDkes.pdf)
  when the first host rejected a direct fetch. Printed p3 HUD, p4 Cougar,
  p6–8 weapons/specials/salvage and controller diagram were read; HUD and Cougar
  figures were visually inspected. The January-2003 imprint is preserved, not
  relabelled as a November-2002 binary. PDF-conversion metadata is not release
  evidence.
- P2: [Joe Grant Bell, licensed Prima Official Strategy Guide](https://www.ogxbox.co.uk/media/com_eshop/attachments/Mech_Assault_Strategy_Guide_2004_Book.pdf),
  110-page scan with copyright 2004 and ISBN 0-7615-3989-1. The weapon/equipment,
  Cougar, vehicle/terrain, combat/resource and complete first-mission material
  was actually read. Printed p36's first-mission map and p37's Cougar/traversal
  figures were rendered and inspected, not inferred from text alone. Relevant
  pages include 3–11, 13, 20–27 and 30–38. Other-mission rules and the guide's
  precise statistical tables are not native measurements or launch-patch proof.
- P3: [Microsoft retail announcement](https://news.microsoft.com/source/2002/11/12/mechassault-offers-xbox-players-the-ultimate-action-experience/),
  November 12, 2002, actually read. Product/platform and lawful historical
  destination; its overall multi-chassis marketing is not first-mission
  selection authority.
- S1: [Jeff Gerstmann's contemporary GameSpot review](https://www.gamespot.com/reviews/mechassault-review/1900-2897126/),
  November 8, 2002, actually read. Firsthand control/heat/cover account,
  not own play or every quantitative simulation property. Its full-mech
  explosion discussion is excluded from this first-mission packet.
- S2: [Marcus Hirshhorn / Marcush, attributed guide](https://gamefaqs.gamespot.com/xbox/559823-mechassault/faqs/21569),
  version 1.10, February 15, 2003. Controls, Cougar/specials, salvage, first
  mission and relevant general tips were read. The broad recharge tip only
  corroborates qualitative renewed reserve, not a frame-perfect fuel rule.
  Simplified two-upgrade pickup wording does not override P2's finite-tier
  refill/depletion edge cases. Later DLC/mission sections are not admitted.
- R1: [EightBitHD's Xbox-labelled full walkthrough](https://www.youtube.com/watch?v=2VnnlEDpP80),
  published December 16, 2016; metadata length 14338 seconds, actual player
  duration 14337.461. Source identity, muted/paused/time/no-ad guards were
  checked for the selected frames listed in Direct-play status. First success
  at 530 and successor at 580 are terminal evidence. An attributed recording is
  not proof of native hardware, region, patch, difficulty or an unmodified disc.
- Claim IDs: MA-001–MA-014. Source rules are documentary facts; automatic
  software behavior is source-qualified rather than relabelled own execution.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: ACT-008, ACT-161, ACT-170, ACT-550.
- Candidate genes: none. Direct grounded movement, aimed shot, equipped mecha
  takeoff and category cycling are existing boundaries. Held activation and
  fitted availability instantiate ACT-170; its Dyson Sphere Program examples
  do not require this game to possess a warp drive. ACT-308 excludes boost
  thrust without jump authority and is not added as a second name for takeoff.
- Parameters: fixed Cougar; left-stick body motion and right-stick torso aim;
  Pulse Lasers, Autocannon and Javelin; cycle input or direct category buttons;
  target and shot; held jump-jet control. First-mission chassis selection is a
  single offered identity, not a decision among a future roster.
- Claim IDs: MA-003/004/007.

### System Behaviour Genes

- Existing gene IDs: SYS-045, SYS-215, SYS-578, SYS-755.
- Added genes: SYS-1432, SYS-1433, SYS-1434, SYS-1435, SYS-1436.
- Resolution order: ground inputs update body/torso; eligible fire uses the
  selected category, its recycle state and any current missile lock; weapon
  effects meet target/range/cover and settle combat/object damage. Firing and
  lift add shared heat while elapsed cooling remains live. Jet reserve funds
  temporary lift; ending lift restores gravity/support traversal. A foot contact
  can defeat ordinary infantry without a shot. Eligible wrecks/structures emit
  typed salvage; armor recovery and weapon-tier mutation are different outputs.
  Headquarters destruction closes the mission and exposes its successor.
- Parameters: simultaneous weapons of a selected type, projectile speed,
  homing/obstruction, damage/splash, cycle duration, thermal capacity, reserve,
  armor cap, salvage category and finite tier capacity. No native coefficient
  is certified from a printed statistic. Moving convoy and arriving transport
  are SYS-045 rather than player-directed pathing.
- Claim IDs: MA-004–MA-009/011/012.

### Constraint Genes

- Existing gene IDs: CON-175, CON-269, CON-571.
- Candidate genes: none. Persistent zero armor is terminal; held equipped
  thrust requires reserve; overheat gates further fire. Installed-category
  recycle cadence remains a combat parameter, not a new cooldown gene for
  each weapon. Unlimited base ammunition does not waive heat or readiness.
- Scarce strategic resources: current armor, flight reserve, shared thermal
  headroom and stronger-tier rounds. Delay may recover readiness/heat, but
  cannot independently erase damage or restore unlimited strong ammunition.
- Claim IDs: MA-004–MA-006/009.

### Information Genes

- Existing gene IDs: INF-073, INF-115, INF-119, INF-480.
- Added gene: INF-495. Equipped-state HUD, personal armor/heat/fuel and local
  partial view reuse existing boundaries. The current actionable assignment
  reuses INF-480, not a fixed omniscient prebriefed checklist. Sensor class
  eligibility and outside-range objective bearing are separate from explored
  terrain contours or Metal Gear Solid's directed perception cones.
  INF-458 additionally discloses actors' facing/attention and placed diversion
  radius; those Stranger's Wrath fields do not occur in this first sensor packet.
- Parameters: selected category, power tier, rounds/recycle, resource bars,
  reticle lock cue, current instruction, sensor range/class/color and objective
  arrow. Omitted infantry can still appear in ordinary world view; no enemy
  BattleMech occurs merely because P1 documents a square icon for other missions.
- Claim IDs: MA-003–MA-007/009/010/012.

### Objective Genes

- Existing gene ID: OBJ-185. Destroy the headquarters in the bounded mission
  while Cougar survives, accept successful settlement and retain successor
  access. Clearing assigned earlier bases/convoy supports that terminal, not
  a fabricated universal every-hostile-on-map requirement.
- Success, evaluation and failure: P2 and R1 show headquarters demolition,
  Mission Successful, then Suffer the Silence. Failure at zero armor is a
  constraint, not another objective; save reload durability is untested.
- Claim IDs: MA-002/009/012.

### Time Genes

- Existing gene ID: TIM-003. Navigation, firing, heat, lift and live threats
  advance together outside pause. Recycle and acquisition intervals parameterize
  their own state rules; there is no evidenced universal first-mission countdown.
- Claim IDs: MA-003–MA-012.

## Reproducible transitions

1. Enter Going Down Hard before any future chassis unlock: the sole offered
   Cougar carries the three named weapon categories and jets (MA-002/003).
2. Compare walking into the blocking ridge with holding eligible jump jets:
   lift reaches the route beyond the ridge. Release/exhaustion is not permanent
   flight; no exact recovered-fuel delay is asserted (MA-004).
3. Fire a heat-generating category, switch category and observe shared chassis
   condition: weapon choice does not create a separate cool reservoir. Waiting
   and documented shallow water affect cooling; water also slows travel
   (MA-005). Native rates remain an open measurement.
4. Apply matching salvage at level 1: full level 2 results. With any level-2
   reserve remaining, another matching pickup gives full level 3. At partial
   level 3, pickup refills; at full level 3, it remains uncollected. Empty level
   3 supplies full level 2; empty level 2 returns to infinite weaker level 1
   (MA-006). These are documented counterfactual branches, not all own tests.
5. Maintain aim to acquire the red-crosshair relation, then move away beyond
   loss delay. Guidance qualification changes; no lock guarantees impact through
   a building or makes Cougar possess a jammer (MA-007).
6. Traverse over ordinary infantry rather than fire: foot contact can remove
   that class. The main-base powered-armor encounter is not automatically the
   same foot-crush target class (MA-008).
7. Take armor loss at one encounter and move to the next: loss persists until
   eligible armor salvage. Collect with little missing armor versus later:
   capped healing can waste recovery. Zero armor closes the attempt (MA-009).
8. Compare a foot soldier in world view with its sensor: absence of a sensor
   mark is not absence of the hostile. Compare a remote objective edge bearing
   with a nearby objective mark (MA-010).
9. Destroy a tall first-base building next to the grounded helicopter: linked
   collapse damage and salvage differ from merely changing a wall texture
   (MA-011). Destruction can also remove useful cover.
10. Clear the local stages, destroy the designated headquarters, accept the
    visible success and inspect the successor briefing. Stop before the Puma
    deployment; later controls do not leak into this first signature (MA-002/012).

## Strategic and experiential structure

### Cognitive demands

- Required deduction: decide whether present armor, heat, fuel and stronger
  ammunition support exposure, withdrawal or destruction of a salvage source.
- Planning horizon: local firing/cooling windows plus the retained sortie route;
  incomplete sensor classes make ordinary visual inspection necessary.
- Common heuristics: alternate weapons while a category recycles without
  assuming heat reset; leave excess armor or full-tier matching salvage; use
  buildings/ridges as cover and avoid their collapse; fight powered armor in
  open space; reserve guided shots for a usable aim relation.
- Failure attribution: depleted armor is terminal; blocked jets, rejected
  top-tier pickup and temporary fire lock are distinct from failed aim.
- Player-trust factors: visible resource/weapon cues, staged instruction and
  explicit mission success. Exact damage and fuel-recovery timing remain unknown.
- Claim IDs: MA-002–MA-012.

## Replay and variation

- What changes: movement, aim, weapon choice, cooling exposure, destruction
  order and timing of salvage collection. Authored route, Cougar and terminal
  headquarters remain fixed for this packet.
- Randomness: no native seed or precise enemy/spawn distribution inspected.
  A real-time convoy is not evidence of procedural map generation.
- Multiple viable strategies: shoot or crush eligible infantry; select different
  installed categories; use cover, jets and delayed pickups subject to current
  state. No universal harmless strategy or exact optimal route is claimed.
- Replay motive: complete the sortie with better survival/resource decisions.
- Claim IDs: MA-003–MA-012.

## Adjacent systems and history

- BattleTech setting and publisher attribution are P3 product facts, not
  transferable MechWarrior simulation rules. MechAssault 2's dismount/hijack
  is another game, not an omitted first-mission gene.
- Later missions expand chassis and enemy-mech/defense choices; their printed
  descriptions cannot retroactively create those first-mission decisions.
- Decision comparison is restricted to the computed exact/tied selections below.
- Claim IDs: MA-001/002/013/014.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-170, ACT-550 | No additional candidate IDs; scoped parameters above |
| System Behaviour | SYS-045, SYS-215, SYS-578, SYS-755, SYS-1432, SYS-1433, SYS-1434, SYS-1435, SYS-1436 | No additional candidate IDs; scoped parameters above |
| Constraint | CON-175, CON-269, CON-571 | No additional candidate IDs; scoped parameters above |
| Information | INF-073, INF-115, INF-119, INF-480, INF-495 | No additional candidate IDs; scoped parameters above |
| Objective | OBJ-185 | No additional candidate IDs; scoped parameters above |
| Time | TIM-003 | No additional candidate IDs; scoped parameters above |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `508` (`GAME-0001`–`GAME-0508`).
- Exact genome matches: none.
- Tied near matches: `GAME-0272` — Serious Sam 4 (`8 / 31 = 0.258065`); `GAME-0352` — DOOM (1993) (`8 / 31 = 0.258065`); `GAME-0474` — Metroid Fusion (`8 / 31 = 0.258065`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0272 Serious Sam 4 | ACT-008, ACT-161, SYS-215, SYS-578, INF-073, INF-115, INF-119, TIM-003 | Shared direct live combat, persistent health and local equipment/resource disclosure do not supply Cougar's held flight, shared chassis heat, promotion/fallback salvage, sensor omissions or headquarters-successor terminal. Serious Sam's distinct enemy/wave and arsenal rules do not transfer. | Tied near: `8 / 31 = 0.258065` |
| GAME-0352 DOOM (1993) | ACT-008, ACT-161, SYS-215, SYS-578, INF-073, INF-115, INF-119, TIM-003 | Shared movement, aimed combat and health/equipment exposure do not create mecha lift or shared thermal resource. DOOM's key/exit rules differ from typed stronger-tier fallback and headquarters demolition; its level structure is not this authored mission. | Tied near: `8 / 31 = 0.258065` |
| GAME-0474 Metroid Fusion | ACT-008, ACT-161, SYS-045, SYS-215, SYS-578, INF-073, INF-119, TIM-003 | Shared body movement, autonomous agents, combat and resource HUD do not supply torso/category control, sensor-class filtering or chassis heat. Metroid's scoped terrain/progression and enemy rules differ from the Cougar's entire first-sortie settlement. | Tied near: `8 / 31 = 0.258065` |

- New genes: SYS-1432–1436 and INF-495; no external novelty claim.
- Classification result: New gene.
- Evidence and reasoning: all 508 prior signatures and 274 combinations are
  computed exactly; no genre-only ranking or convenient three-item sample is
  substituted. Shared IDs remain unchanged English boundaries (MA-013/014).

### Preserved research notes

- New genes: SYS-1432–1436 and INF-495; no external novelty claim.
- Classification result: New gene.
- Evidence and reasoning: all 508 prior signatures and 274 combinations are
  computed exactly; no genre-only ranking or convenient three-item sample is
  substituted. Shared IDs remain unchanged English boundaries (MA-013/014).

## Taxonomy impact

- Registry changes: six Active additions; seventeen unmodified transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_246](../../../research/taxonomy-changes/TAXONOMY_CHANGE_246.md).
- Candidate terms affected: none. Existing definitions, signatures and the
  published r000024 mapping remain unchanged; no platform release audit is implied.
- Claim IDs: MA-013/014.

## Negative results

- No new structured negative-result record. Existing heat, pending-volley,
  near-aim correction, radar-cone, platformer-stomp and future-module boundaries
  fail explicit transfer tests without being declared globally invalid.
- Claim IDs: MA-004–MA-010/013.

## Delta summary

## New facts

- [Observation | Corroborated | High] Complete fixed-Cougar first sortie closes
  at headquarters demolition and successor availability (MA-002).
- [Observation | Corroborated | High] Shared heat and stronger-tier salvage
  exhaustion distinguish live traversal/fire/resource decisions (MA-005/006).
- [Observation | Limited | Medium] Reserve recovery is qualitative and its
  exact eligibility/scheduling remains unverified (MA-004).

## New genes

- [Observation | Corroborated | High] SYS-1432–1434, SYS-1436 and INF-495
  separate thermal coupling, tier fallback, timed lock, foot crushing and
  sensor eligibility. MA-007/010 retain direct documentary evidence.
- [Observation | Limited | Medium] SYS-1435 records bounded lift and qualified
  renewed reserve, not measured native fuel recovery (MA-004).

## New combinations

- [Observation | Direct | High] No new verified combination; every existing
  combination was tested as a proper subset (MA-014).

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_246 accepts six bounded
  additions without revising any existing English gene or game signature.

## New questions

- [Hypothesis | Limited | Medium] Native original-disc fuel eligibility and
  timings may refine MA-004; a controlled release/exhaustion/landing/refill
  experiment could reject an assumed recovery schedule. No schedule is encoded.
- [Hypothesis | Limited | Medium] Exact captured difficulty, disc/patch and
  save reload could alter quantitative conclusions; inspect the original
  artifact before claiming parity or retained successor durability after reload.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0510 Indiana Jones and the Great Circle,
  released Xbox Series target, follows this unit's complete gates and local
  commit. No early version is substituted.
- Optimisation criterion: restore the approved modern/retro alternation and
  contrast guided mecha combat with embodied exploration and contextual action.
- Expected information gain: complete released exploration packet, not an
  invented genome or promised number of additions.
- Backlog impact: unit 15/18 in Selection 039; no push/publication/deploy.

## Why this game

- [Hypothesis | Limited | Medium] Its original Xbox fixed-chassis resource loop
  tests whether retained combat, heat, salvage and sensor boundaries transfer
  without inventing simulation features from setting or later missions.
