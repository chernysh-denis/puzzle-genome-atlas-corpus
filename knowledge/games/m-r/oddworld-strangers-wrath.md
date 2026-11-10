---
game_id: GAME-0483
slug: oddworld-strangers-wrath
game_title: "Oddworld: Stranger's Wrath"
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-183
    - ACT-341
    - ACT-639
    - ACT-640
    - ACT-641
    - ACT-642
    - ACT-643
  system:
    - SYS-037
    - SYS-045
    - SYS-051
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-755
    - SYS-1264
    - SYS-1265
    - SYS-1266
    - SYS-1267
    - SYS-1268
    - SYS-1269
    - SYS-1270
    - SYS-1271
    - SYS-1272
  constraint:
    - CON-077
    - CON-282
    - CON-578
    - CON-748
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-458
    - INF-459
  objective:
    - OBJ-272
  time:
    - TIM-003
    - TIM-007
---

# Game: Oddworld: Stranger's Wrath — original Xbox first paid bounty

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Creature species, trigger buttons, dollars, stars and named outlaws are carrier parameters, not separate genes.

## Analysis scope

- Version / ruleset: original 2005 English-language Xbox retail base game. The original Electronic Arts booklet and two independent original-Xbox written routes support the reconstruction. Exact disc revision, installed update, collision solver and timings were not inspected. This is not Stranger's Wrath HD, a modern console port, mobile touch/gyro controls or a modified executable.
- Structured analysis target: original English Xbox retail disc, first accepted Filthy Hands Floyd contract; existing `PLAT-XBOX`. Other releases remain unaudited.
- Primary decision loop: inspect cover, hostile attention and available live ammunition; assign two independently fired barrel loads; choose lure, web, gas, electrical stun or damaging critters; advance in first- or third-person mode and subdue a target. Approach and collect a still-eligible living or dead body before recovery or disappearance, replenish ammunition by hunting wild critters, and return to the Bounty Store for state-dependent payment.
- Entry and exit: complete the introductory Blisterz Booty route as setup, cash its existing captures, accept the first Filthy Hands Floyd contract in Gizzard Gulch, and leave without buying ammunition, equipment or upgrades. Preserve the original five basic ammo types introduced in the tutorial. End at the first post-Floyd Bounty Store payout, or abandonment, before buying upgrades or accepting Looten Duke. Include contract retry/Quiksave choices, optional local loot and both living/dead capture strategies; the setup tutorial's own encounters are outside this packet. Record the lawful disc, fresh profile, initial funds/ammunition, acceptance, purchases omitted, input trace, capture states and first payout to reproduce it.
- Included: controlled walking, double jump, fast third-person running and authored rope/ledge traversal; melee; independently assigned/fired live-ammo barrels; manual and automatic clip reload; charge growth of loaded Zappflies; charged-shot fixtures; wild ammo hunting and finite typed stock; Chippunk diversion, Bolamite binding, Stunkz incapacitation and Fuzzle autonomous biting; health versus recoverable hostile incapacitation; close capture channel, corpse expiry and differential deferred payment; personal health/stamina and commanded shake healing; cover/perception, patrol, first-contract encounter/return gates, breakable loot and explosive scenery; HUD/radar/bounty disclosure, authored failure restoration, reversible Quiksave and unpaused real time.
- Excluded: purchases and upgrades in this deliberately unupgraded configuration; exact claim that the first shop is universally empty; later Thudslugs, Boombats, Stingbees, Sniper Wasps and critter upgrades; Looten Duke, water-facility hazards, later towns, surgery, story transformation and whole-campaign victory. No exact enemy counts, damage coefficients, ammo capacity table, duration, collision geometry or optimal bounty route is claimed.
- Potential scoped modules: upgraded bounty loadouts, a later boss with special defences and the post-revelation combat campaign need independent packets.
- Evidence limits: original guide shop descriptions conflict, so no-buy is an explicit configuration, not a proven empty shop; exact Quiksave file retention was not executed.
- Direct-play status: no Xbox, disc executable, emulator, save, gameplay video/audio or input trace was opened or played. The original manual PDF's booklet pages 2–9 were rendered and visually read, including controls, HUD, capture and live ammo. Two full written Xbox guide pages were inspected in their relevant original-game sections. The original developer product description was read through an archival copy. Exact first-shop inventory conflicts between the guides and is not resolved by pretending to have played. Artwork is an original possible scene, not a captured map or an official asset.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SW-001 | First-/third-person switching changes weapon use and fast traversal; two barrels can receive different ammo and fire independently. | Observation | Corroborated | High | P1 pp. 2–3, 6; S1 Controls/Combat |
| SW-002 | Wild critters must be subdued before contact collects compatible stock; finite types have capacity, while Zappflies supply unlimited shots but still reload. | Observation | Corroborated | High | P1 pp. 6–7; S1 Live Ammo/Ammo Stats; S2 tutorial |
| SW-003 | A loaded Zappfly charges with time; its charged hit can stun critters/outlaws or activate a compatible electrical fixture. | Observation | Corroborated | High | P1 p. 7; S1 Zappflies; S2 surge-panel route |
| SW-004 | Chippunks redirect eligible nearby outlaws; Bolamites bind, Stunkz interrupt action through gas, and placed Fuzzles wait then bite a nearby outlaw automatically. | Observation | Corroborated | High | P1 pp. 6–9; S1 Live Ammo |
| SW-005 | Hostile health loss can leave a dead body; incapacitation permits temporary living capture. Recovering targets and disappearing corpses limit the opportunity; some destructive kills leave no collectible body. | Observation | Corroborated | High | P1 pp. 4–5, 9; S1 Combat; S2 Floyd strategies |
| SW-006 | Close held collection has progress and is slower for a resisting live target; captures become deferred bounty inventory, paid at a store, with more for living than dead. | Observation | Corroborated | High | P1 pp. 4–5; S1 Bountying/Moolah; S2 payout |
| SW-007 | Shake healing converts stamina into personal health; melee and impact spend stamina, which can refill in a quiet interval. Capture also restores some stamina. | Observation | Corroborated | Medium | P1 pp. 3–4; S1 Health & Stamina |
| SW-008 | Radar reveals nearby actor classes, direction/attention, mission interest and diversion radius; local cover and grass concealment alter detection. HUD discloses health/stamina and capture state. | Observation | Corroborated | High | P1 p. 4; S1 Combat; S2 first contract |
| SW-009 | Contract acceptance opens the route; panels, cover, encounter clearance, Floyd and a return encounter precede the first payout. | Observation | Corroborated | Medium | S1 Filthy Hands Floyd; S2 5.02 |
| SW-010 | Eligible damage/trigger breaks scenery or releases loot; a crane trap can destroy an outlaw without leaving a collectible bounty. | Observation | Corroborated | Medium | P1 p. 9; S1/S2 first-contract crane/loot |
| SW-011 | Original automatic saves restore a recent section after death. One replaceable Quiksave can preserve a later world state and allow a different continuation. Exact file retention was not executed. | Observation | Limited | Medium | S1 Saving and Quiksaving |
| SW-012 | The two original route accounts differ about early shop supplies. No-buy is an explicit reproducible configuration, not proof that stock is absent. | Observation | Conflicting | Medium | S1 Gizzard Gulch; S2 5.02 |

## Basic data

- Release / origin: Oddworld Inhabitants, original 2005 Xbox title, published by Electronic Arts. No conflicting day-of-release claim is required for this packet.
- Platform or physical form: original English Xbox retail disc; existing identity does not audit every later release.
- Mechanical families: `FAM-010` live system pressure and `FAM-017` ordered dependency sequencing. Active body recovery/capture and contract clearance/payment supply the causal boundaries, not the action genre alone.
- Primary sources accessed 2026-10-02:
  - **P1:** [Original Electronic Arts English Xbox instruction booklet](https://db.hfsplay.fr/files/2020/06/19/Oddworld_Strangers_Wrath_-_2005_-_Electronic_Arts_W9VPeBR.pdf), archival document, rendered pages 2–9: original controls, game screen, health/stamina, capture, critter effects and gameplay tips. Its later-ammunition inventory is not evidence that every type exists in the first contract.
  - **P2:** [Archived original Oddworld developer product page](https://oddworldlibrary.net/archives/web/oddworld.com/games/ow_stranger.shtml), first-party description preserved by Oddworld Library, establishes original identity and live-ammo bounty premise, not a first-contract input trace.
- Secondary scope sources:
  - **S1:** [Syonyx's original Xbox guide](https://www.supercheats.com/xbox/walkthroughs/oddworldstranger-walkthrough01.txt), version 1.60, 2 May 2005. Relevant controls, Combat, Health & Stamina, Saving and Quiksaving, Live Ammo and first Filthy Hands Floyd route were read. Numeric capacities and shop claims remain source-limited.
  - **S2:** [Independent original Xbox walkthrough](https://www.supercheats.com/xbox/walkthroughs/oddworldstranger-walkthrough02.txt), originally written in 2005, version 1.4 updated in 2007, section 5.02, tutorial and first-contract living/dead strategies. It independently corroborates contract order, panels, wild ammo, concealment, boss and store return. Its early shop description conflicts with S1.
- Claim IDs: `SW-001`–`SW-012`; manual rules, reconstructed route and untested save details retain separate confidence.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly moving, jumping and climbing; `ACT-161` for melee/eligible breakable strikes; `ACT-183` for optional early reload; `ACT-341` for reachable clerk/door activation. Clerk activation accesses the single first offered bounty; it is not a branching dialogue gene.
- New `ACT-639` assigns live ammo independently to left/right barrels, unlike choosing one active inventory item. `ACT-640` switches embodied perspective with changed shooting/running affordances, not merely decorative camera orbit. `ACT-641` holds the close bounty collection command. `ACT-642` requests shake healing without consuming a carried medicine. `ACT-643` launches the loaded live critter toward an actor, fixture or placement surface; hostiles are not its only valid targets. `SW-001`–`SW-007`.

### System Behaviour Genes

- Reuse `SYS-037` contact loot; `SYS-045` patrol locomotion; `SYS-051` automatic engagement by a deployed Fuzzle; `SYS-057` perceived actor/decoy pursuit; `SYS-215` live combat; `SYS-369` failure restoration; `SYS-578` continuous personal health; `SYS-755` damage/trigger-driven scenery breakage. No global shared alarm, procedural hunt or retained death-world is asserted.
- New `SYS-1264` converts subdued wild critters into typed ammunition on contact; `SYS-1265` charges the loaded electrical shot while waiting; `SYS-1266` separates recoverable hostile incapacitation from expiring death; `SYS-1267` gives typed web/gas temporary incapacity; `SYS-1268` completes a held body collection into deferred captures; `SYS-1269` settles living/dead-valued captures into store currency; `SYS-1270` couples personal exertion, commanded stamina-funded healing and quiet refill; `SYS-1271` automatically reloads empty typed clips with fire unavailable; `SYS-1272` resolves a charged compatible hit into a linked fixture state. These are distinct state transitions, not nine names for ammo species. `SW-002`–`SW-011`.

### Constraint Genes

- Reuse `CON-077` directed occlusion-bounded perception, with grass/cover as concealment classes; `CON-282` ordered authored mission gates; `CON-578` finite compatible ammo with the explicitly separate unlimited Zappfly exception. Do not import a magazine limit into the definition of reserve capacity.
- New `CON-748`: close facing, third-person collection and a still-incapacitated or retained dead body are required for bounty collection; a removed or recovered body is no longer eligible. `SW-005`, `SW-006`, `SW-008`, `SW-009`.

### Information Genes

- Reuse `INF-073` current barrel/ammo state, `INF-115` local sight/sound, `INF-119` personal health/stamina. Their carrier fields do not assert experience growth.
- New `INF-458` shows local classified radar with facing/attention and diversion range, without Metal Gear Solid's radar-suppression rule. New `INF-459` discloses hostile incapacitation/damage, held capture progress and pending alive/dead bounty state so subduing is distinguishable from banking payment. `SW-005`–`SW-008`.

### Objective Genes

- New `OBJ-272`: fulfil the accepted target contract and return captured bounties for settlement, choosing higher live payment against exposure and recovery risk. Required target, optional additional captures/loot and payout are separate from complete-campaign surgery or mere target killing. `SW-006`, `SW-009`.

### Time Genes

- Reuse `TIM-003` for unpaused motion, charge, recovery, collection and reload; `TIM-007` for source-described Quiksave restoration and alternative continuation. Exact history granularity and persistence are source-limited, not tested; ordinary pause is not tactical frozen action selection. `SW-001`–`SW-011`.

## Reproducible transitions

| Initial state and input | Accepted transition | Distinguishing edge | Claims |
|---|---|---|---|
| Different available species assigned left/right; fire one trigger | Only the selected barrel launches its current critter | Not replacing one globally active weapon | SW-001 |
| Loaded Zappfly waits, then hits compatible panel | Charge rises, powered hit changes linked gate/crane state | An early weak hit is not guaranteed to activate it | SW-003, SW-009 |
| Wild critter subdued; cross its position with capacity | Typed stock increases | A mobile unstunned critter or full stock is not an automatic acquisition | SW-002 |
| Chippunk placed in a reachable response area | Eligible outlaw investigates the stimulus | Range/path matter; no universal whole-map lure | SW-004, SW-008 |
| Bolamite/gas incapacitates an outlaw; delay collection | Temporary vulnerability eventually ends | Webbing/retching alone does not bank a bounty | SW-004–SW-006 |
| Living subdued body versus dead intact body; close held capture | Progress completes and a deferred capture is recorded | Live resistance lengthens collection; recovery/disappearance removes opportunity | SW-005, SW-006 |
| Captures returned to clerk after Floyd | Pending captures pay by their captured alive/dead state | A killed but uncollected body is not paid as a capture | SW-006, SW-009 |
| Injured Stranger requests shake while stamina remains | Stamina is converted into restored personal health | Not an automatic health refill or medicine consumption | SW-007 |
| Typed clip reaches empty | Automatic reload temporarily prevents firing that ammo | Infinite Zappfly supply does not imply zero reload downtime | SW-002 |
| Deployed Fuzzle encounters eligible outlaw | Critter automatically engages and bites | Not one manual strike command per bite | SW-004 |
| Crane activated onto outlaw or barrel breaks | Eligible scenery resolves destruction/loot | Destructive gib kill can deny body capture | SW-005, SW-010 |
| Death after section save or later Quiksave | Saved state is restored for a new continuation | No original save-file experiment has been performed | SW-011 |

## Strategic and experiential structure

The pressure comes from moving between cover and collection while other outlaws remain active. Spending finite disabling ammo can preserve higher-value live targets; lethal damage can simplify exposure yet reduce or erase recoverable payout. Charged electrical shots replenish wild ammo without a finite reserve but require waiting and clip readiness. Optional local loot and live captures can improve one contract result without adding a universal kill quota. No optimal trace, exact economy, difficulty coefficient or deterministic hostile seed was measured.

## Replay and variation

The accepted no-buy configuration holds initial equipment and contract order fixed while allowing different barrel pairings, cover routes, optional loot and alive/dead outcomes. Source-described section saves and one replaceable Quiksave permit another continuation; neither exact file persistence nor a measured restart trace is claimed. Improving payment is a different motive from unlocking a later contract. No random level generator or inferred all-release rule parity is admitted. `SW-001`–`SW-012`.

## Adjacent systems and history

Original Xbox has embodied perspective switching, not the mobile edition's later input system. Both written authors distinguish the introduction from the first accepted paid contract; neither full-product ammunition lists nor post-Floyd shop menus prove later ammo availability in this no-buy packet. The conflicting initial-shop description remains disclosed. Narrative surgery and transformation are outside the first payout endpoint; no lineage is inferred from numerical neighbours.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-183`, `ACT-341`, `ACT-639`–`ACT-643` | traversal, melee, reload, clerk, paired loads, view mode, capture, shake, critter launch |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-051`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-755`, `SYS-1264`–`SYS-1272` | contact, patrol, deployed combat, attention, live combat, retry, health, breakage and bounty/ammo transitions |
| Constraint | `CON-077`, `CON-282`, `CON-578`, `CON-748` | perception, authored order, typed reserve, collectable body |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-458`, `INF-459` | loads, local cues, personal resources, radar and bounty progress |
| Objective | `OBJ-272` | accepted contract and return settlement |
| Time | `TIM-003`, `TIM-007` | live activity and source-described restorable snapshots |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `482` (`GAME-0001`–`GAME-0482`).
- Exact genome matches: none.
- Tied near matches: `GAME-0352` — DOOM (1993) (`11 / 43 = 0.255814`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0352` DOOM (1993) | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-578`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | Both packets combine direct live traversal/combat, local hostile perception, finite ammunition, personal health and visible equipment. DOOM's ordinary no-save Hangar route selects one active weapon, gathers compatible resource pickups, uses factor-split armour and ends at an exit switch. Stranger instead assigns two live-ammo loads, changes embodied mode, hunts replenishment and trades temporary incapacitation/capture risk against deferred living/dead payment on return. It admits source-described retry snapshots, not DOOM's excluded save/load. | Near, `11 / 43 = 0.255814`; structural overlap, not equivalent play or inferred lineage. |

## Taxonomy impact

`TAXONOMY_CHANGE_220` admits eighteen bounded additions and twenty unchanged reuses. The named role review partitions the full thirty-eight-use packet by causal role rather than rarity. No earlier signature, definition, combination or platform identity changes.

## Negative results

- Reject probabilistic creature recruitment, a firearm-only target action for placed critters, one global equipped-item selection for two independently loaded barrels, and automatic health regeneration for commanded shake healing.
- Reject permanent knockout, corpse capture without a retained body, immediate bounty cash at defeat, compulsory killing, universal shop emptiness and HD controls.
- Reject importing later ammo, upgrades, water-facility hazards or surgery into the first no-buy contract. Source-described Quiksave persistence is not an executed reload observation.

## Delta summary

## New facts

- [Observation | Corroborated | High] Paired live ammo supports diversion, temporary incapacitation and independent body collection before deferred store settlement.
- [Observation | Conflicting | Medium] Early store descriptions disagree; the explicit no-buy configuration avoids treating either as proven inventory.

## New genes

- [Observation | Corroborated | Medium] Eighteen boundaries distinguish paired load/perspective/capture/heal/launch inputs, live-ammo and bounty transitions, eligibility, disclosed capture information and first-contract settlement.

## New combinations

- [Observation | Limited | Medium] No new verified combination; all existing proper subsets are checked against the complete signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_220`; no prior definitions or signatures change.

## New questions

- Verify lawful original-disc shop availability, exact clip/capture/recovery timing, stamina conversion, save-state retention and collision/attention rules before quantitative claims.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0484` *Impossible Mission*, original Commodore 64, follows complete acceptance and the Goal stop window.
- Optimisation criterion: change platform and move from live capture economics to timed room search and information assembly.
