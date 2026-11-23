---
game_id: GAME-0565
slug: dome-keeper
game_title: Dome Keeper
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-130
    - ACT-159
    - ACT-161
    - ACT-190
    - ACT-341
  system:
    - SYS-212
    - SYS-213
    - SYS-1285
    - SYS-1648
    - SYS-1649
    - SYS-1650
    - SYS-1651
    - SYS-1652
    - SYS-1653
  constraint:
    - CON-136
    - CON-206
    - CON-304
    - CON-830
    - CON-831
    - CON-832
  information:
    - INF-117
    - INF-235
    - INF-540
    - INF-541
  objective:
    - OBJ-020
  time:
    - TIM-003
---

# Game: Dome Keeper

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The marketed product is broader than this complete opening mining/defence
cycle. Ore colours, node prices, mine seed and wave counts are parameters,
not separate title-derived genes.

## Analysis scope

- Version / ruleset: original English Windows Steam full-release rules of
  27 September 2022, Relic Hunt, Normal difficulty, Small map, Engineer,
  Laser Dome and starting Shield, without a carried-over secondary gadget,
  custom modifier or account-granted later benefit. The exact launch binary,
  depot checksum and native execution are unverified. This is not the
  Dome Romantik prototype, a prerelease demo or the present cooperative game.
- Structured analysis target: PLAT-WINDOWS-PC in knowledge/platforms/games.json,
  evidenced by the dated official release announcement, launch-era developer
  explanations, contemporary independent accounts and release-day recording.
  A current product page identifies the title but does not prove the old
  equipment roster, prices or input scheme.
- Primary decision loop: uncover and drill nearby terrain, attach a
  manageable mineral load, choose a return path and bank it at the dome;
  allocate the bank between tools, movement, protection, information and
  repair, occupy weapon control and prioritise the full approaching assault.
  Return to mining with the changed equipment and surviving dome condition.
- Entry and exit: first playable control after the fresh landing. Include
  the whole initial mining window, physical hauling/deposit, all currently
  legal basic console transactions, accessible preparation and the complete
  first ordinary hostile wave. Stop at the next ordinary mining handoff
  after all arrivals and remaining attackers are resolved, or at dome
  destruction if it occurs first. Landing, the first deposit or killing
  the first attacker is not completion. Clearing this packet is not winning
  the whole Relic Hunt run or retrieving its final relic.
- Reproducible setup/coverage: choose the declared loadout and fresh Small
  Normal run. Drill an opening shaft and reachable side passage, compare
  softer and harder rock, attach loose ore and compare a lighter return
  with a heavier haul or partial drop. Reach the intake, inspect which
  materials actually entered the bank and buy only affordable unlocked
  nodes. Compare movement/carry/drill or laser improvements against the
  separately purchased meters. Where the generated opening provides the
  resources and prerequisites, inspect paid repair and the Shield's
  unlocked pre-battle water overcharge; their availability is conditional,
  not a promised first-cycle yield. Likewise, if a selected Shield battle
  node and readiness are available, request its legal temporary response;
  the default installation does not grant every ability. Exact activation
  reach outside weapon control and automatic-trigger ordering are untested.
  Return before the assault, enter battle
  control and hold/steer the laser until the full wave clears. Contrast
  arriving late: enemies do not wait for the keeper. The route specifies
  observable tests, not an owned executable or a fabricated input replay.
- Included: four-direction jetpack navigation and contact-directed drilling;
  persistent tile removal, hardness/tool eligibility and loose mineral
  bodies; attachment, partial release, load-sensitive speed and physical
  return/deposit; shared typed run bank, offered prices and prerequisite
  nodes, paid local performance/disclosure changes and eligible repair;
  the active mining clock, unprovoked dome assault and clearance handoff;
  station-exclusive manual laser aim/fire, finite mount slew and beam
  exposure; starting Shield interception, mining-time recharge and retained
  underlying integrity; conditional prepared overcharge and acquired Shield battle effects
  (local damage/stun, invulnerability or reflection); local mine reveal,
  surface combat view and separately purchased instrumentation.
- Clock boundary: ordinary movement, mining, hauling and battle are live.
  Console selection/upgrading pauses active simulation, and battle control
  resumes it. An attack does not teleport the keeper home or forbid a late
  return; abandoning the dome instead exposes it to attack. A paused menu
  is not free mining or simultaneous weapon control.
- Excluded: complete-run relic/chamber-button/final-wave settlement, Prestige
  exports and score, later unlock selection or permanent account benefits;
  Sword, Orchard/Repellent, Assessor and later keeper/dome alternatives;
  optional secondary-gadget operation and special chambers; multi-player,
  assignments, supplements, later early-warning/exit-route features, current
  mouse controls and post-2024 overcharge revisions. This is the approved
  complete opening cycle, not an exhaustive union of future equipment.
- Potential scoped modules: a complete Relic Hunt extraction run with its
  selected secondary gadget, Prestige resource export, Sword combat, a
  named optional gadget or a separately versioned later cooperative mode.
- Direct-play status: not conducted. Read dated original developer/publisher
  material and contemporary independent descriptions. Inspected the first
  three static ten-second storyboard sheets, 160×90 source cells, of
  Northernlion's 41:04 recording from the release-day stream: landing,
  initial mine/hauls, console nodes, first laser assault and subsequent
  mining are visible; later sheets also show out-of-packet gadget selection.
  These sparse views corroborate phase order and layout, not exact input
  edges, a recorded Small/Normal seed or a certified native binary. No video
  or audio playback, desktop focus change, direct controller trace or
  frame-perfect timing experiment was used. Wiki pages that deny full
  access are used only for explicitly identified indexed passages.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DK-001 | The 27 September 2022 full Windows release is distinct from the demo and later keepers, controls and cooperative content. | Observation | Direct | High | P1, P2, P5, S2 |
| DK-002 | Engineer movement/contact drilling opens discrete local terrain and exposes loose materials in a procedurally generated mine. | Observation | Corroborated | High | P1, P2, S1, S2, V1 |
| DK-003 | Materials must be physically hauled and deposited; a heavier attached load slows the return and can be partly dropped. | Observation | Corroborated | High | P1, S1, S2, V1 |
| DK-004 | Run-bank purchases change tools, travel, defence or information, and console planning pauses the live clock. | Observation | Corroborated | High | P1, S1, S2, V1 |
| DK-005 | Mining time leads to an assault regardless of keeper position, and complete clearance permits the next mining interval. | Observation | Corroborated | High | P1, P2, S1, S2, V1 |
| DK-006 | A present console operator directs a slewing continuous laser; returning late and target-switch travel have costs. | Observation | Corroborated | High | P3, S1, S2, V1 |
| DK-007 | Shield protection and persistent dome integrity are distinct; battle suspends shield recharge and dome destruction ends the attempt. | Observation | Corroborated | Medium | P4, S1, S2, S3, S4 |
| DK-008 | Launch Shield overcharge requires its upgrade and local water-funded activation outside the assault. | Observation | Direct | High | P4, P6 |
| DK-009 | Basic resource, integrity and hostile-proximity meters are separate paid disclosures, not universal starting HUD. | Observation | Corroborated | High | S1, S2, V1 |
| DK-010 | Exact launch seed, spawn table, hit ordering, recharge speed and all first-cycle resource opportunities are not reproduced. | Observation | Limited | Medium | V1; no owned launch executable |
| DK-011 | An acquired ready Shield battle branch supplies its temporary field, invulnerability or reflection; activation and advanced automatic predicates depend on the acquired node. | Observation | Corroborated | Medium | P4, S5 |

## Basic data

- Release / origin: Bippinbits, published by Raw Fury, Windows full release
  27 September 2022. The unit targets the original released rules, not an
  earlier press-copy title alone or current store features.
- Platform or physical form: English keyboard-controlled Windows game; one
  embodied Engineer, one fixed Laser Dome, initial Shield and generated Small
  mine. Exact seed values, costs and rates are not universal constants here.
- Puzzle family: tactical counterplay, real-time pressure and ordered
  dependencies. The equipment bank links mining choices to later defence.
- Primary material, accessed 2026-11-20:
  - **P1** [official full-release announcement](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1637320&count=30&maxlength=0&enddate=1665057600),
    27 September 2022. Complete article read through Valve's public
    [dated news API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1637320&count=30&maxlength=0&enddate=1665057600),
    which preserves the announcement, launch identity and dig/defend/develop loop.
  - **P2** [official game site](https://www.domekeeper.com/) and
    [Steam product](https://store.steampowered.com/app/1637320/Dome_Keeper/),
    product identity, procedural mines and the recurring loop. Their current
    expanded rosters and multiplayer are not evidence of launch availability.
  - **P3** [Dome Deep-Dive](https://store.steampowered.com/news/app/1637320/view/3374905159834235255),
    18 August 2022, full text read through the same dated Valve API: default
    held-fire laser, mount travel and launch dome differences. It is developer
    design documentation, not direct play of a prerelease build.
  - **P4** [Primary Gadgets With Combat Abilities](https://store.steampowered.com/news/app/1637320/view/3298345868515675262),
    15 September 2022, complete official text via the API. Launch trees and
    water overcharge differ from the prototype's operating costs.
  - **P5** the API's original Patch 1, 29 September, and Patch 2, 5 October
    2022: v41.2 and 41.3.7 respectively. Later rebinding and gadget changes
    are not silently projected back to release day.
  - **P6** [launch-day overcharge explanation and developer acknowledgement](https://steamcommunity.com/app/1637320/discussions/0/3369279376438779108/),
    27 September 2022. The original instructions and René/Bippinbits reply
    support local generator, water and phase requirements; later comments
    are not mistaken for the original version.
- Independent corroboration, accessed 2026-11-20:
  - **S1** [Jon Bailes, PC Gamer, 27 September 2022](https://www.pcgamer.com/dome-keeper-review/),
    original reviewed loop, directed drilling, physical hauling, slowdown,
    partial drops, paid meters and slow target switching.
  - **S2** [Nick Tan, Shacknews, 27 September 2022](https://www.shacknews.com/article/132448/dome-keeper-review),
    full relevant mining/console/defence sections read; confirms distinct
    resources, pausing, original gadget roles, meters and Normal difficulty.
  - **S3** [Antal Bokor, Third Coast Review, 6 October 2022](https://thirdcoastreview.com/games-tech/2022/10/06/review-dome-keeper),
    corroborates transport/upgrades, original one-keeper/two-dome state and
    destruction as loss. Its compressed relic-win description is outside scope;
    its colloquial gold is not adopted as a fourth material beside iron.
  - **S4** [community FAQ](https://domekeeper.wiki.gg/wiki/Frequently_Asked_Questions)
    and [Shield summary](https://domekeeper.wiki.gg/wiki/Primary): indexed
    passages only, full page denied. The quoted old-FAQ rule suspends gadget
    charging during battle. No instant end-of-wave full-refill claim follows.
    Current site facts and a third-party modified FAQ mirror are not original
    developer execution evidence.
- Recorded observation **V1**: [Northernlion, 2022's best strategy game?](https://www.youtube.com/watch?v=KyOG1SF4k-0),
  published 28 September, explicitly from the 27 September 2022 stream.
  First three 160×90-cell sheets sampled every ten seconds were inspected;
  no continuous playback or exact frame claims. The first cycle is visible,
  and later gadget prompts remain outside the declared opening packet.
- **S5** [Goose, original-era mechanics guide, 7 November 2022](https://steamcommunity.com/sharedfiles/filedetails/?id=2869939597),
  relevant dated Engineer, dome, Shield and strategy sections read. It lists
  the original three battle branches; its incomplete or current-compatible
  status is not a native build certification. Its later optional-gadget
  operations are not admitted into this opening packet.
- Claim IDs: DK-001–DK-011.

## Mechanical decomposition

### Action Genes

- Reuse ACT-008 for direct four-direction jetpack navigation. It has no
  asserted finite fuel bar; depth and return distance still matter.
- Reuse ACT-159 for holding direction into one reachable terrain cell to
  request drilling; a dedicated extra drill key is not invented.
- Reuse ACT-048 for attaching reachable loose mineral bodies and releasing
  all or part of the haul. They are not instant discrete inventory claims.
- Reuse ACT-130 for a currently legal paid console node or repair service;
  ACT-341 separately commits console entry, control selection and the
  eligible addressed Shield generator activation.
- Reuse ACT-161 for direct laser aim/held fire. ACT-113's released physics
  projectile and chosen launch strength do not fit the continuous beam.
- Reuse ACT-190 for a currently available active capability request,
  parameterised here by the equipped Shield ability, not an ordinary shot
  or personal temporary combat form.
- Claims: DK-002–DK-006, DK-008, DK-011.

### System Behaviour Genes

- Reuse SYS-212 for completed discrete tile removal and eligible loose
  output; SYS-213 for the generated persistent tile mine. No particular
  launch seed, algorithm or later fixed-map interface is certified.
- New SYS-1648 distinguishes world cargo from bank credit at the intake.
  An assigned autonomous RTS worker job, SYS-549, is a different operation.
- New SYS-1649 applies purchased run-local nodes and preserves their effects
  through an ordinary cycle. Prices and upgrade levels remain parameters.
- New SYS-1650 owns clock-to-assault, hostile approach/attack and complete
  clearance-to-mining handoff; it neither waits for the keeper nor teleports
  them home. Unobserved spawn tables and exact timings remain qualified.
- New SYS-1651 owns mount slew and sustained beam contact. New SYS-1652
  resolves the initial shield before retained dome condition and recharges
  it outside battle. It does not substitute personal quiet-gap regeneration.
- Reuse SYS-1285 for the paid cobalt repair result when the node and stock
  permit it. This is separate from automatic shield recovery.
- New SYS-1653 applies the selected acquired temporary Shield response.
  Only the chosen legal field/invulnerability/reflection branch occurs; no
  uniform exact charge count, cooldown or automatic trigger is invented.
- Claims: DK-002–DK-008, DK-011.

### Constraint Genes

- Reuse CON-206 for reachable compatible terrain/tool contact; harder rock
  affects work rather than implying every surface breaks in one touch.
- Reuse CON-304 for carried-load-dependent movement performance. No hard
  backpack slot quota or unlimited full-speed haul is inferred.
- Reuse CON-136 for retained earlier-node dependencies. ACT-130 and each
  node's typed price still require an affordable offered transaction.
- New CON-830 assigns terminal loss to the defended dome rather than the
  miner's hypothetical personal health; CON-831 prevents simultaneous
  manual mining and console firing; CON-832 separately bounds unlocked
  generator overcharge by local reach, water and the non-battle phase.
- Claims: DK-002–DK-008.

### Information Genes

- New INF-540 owns the local mining frontier and exposed material cues,
  without a fully visible hidden map. Reuse INF-235 for the surface battle
  view's present threats, body and beam effects, not underground omniscience.
- Reuse INF-117 for inspectable bank, transaction price and offered state.
  New INF-541 distinguishes the separately purchased live instruments from
  the unchanged underlying resource/health/clock state before purchase.
- Claims: DK-002, DK-004, DK-006, DK-009.

### Objective Genes

- Reuse OBJ-020: neutralise the complete finite initial assault before the
  defended dome falls, then resume mining. OBJ-159's escaped-hostile debit
  through an authored final numbered schedule is not this objective.
- This packet's success is a mining handoff, not a complete-run relic win.
- Claims: DK-005, DK-007.

### Time Genes

- Reuse TIM-003: mining, hauling, countdown and battle run while input is
  accepted. Its pause parameter covers console selection/upgrading without
  adding a duplicate personal-radial or crew-command pause gene.
- No exact seconds, fixed late-return allowance or free battle-time recharge
  is assumed. Claims: DK-004–DK-007.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim |
| --- | --- | --- | --- | --- |
| Reachable intact rock | Hold direction toward its cell | Work completes, geometry opens and eligible loose mineral appears | No instant bank credit | DK-002, DK-003 |
| Loose mineral within reach | Attach and move away | Mineral follows as world cargo | Not an inventory-only icon | DK-003 |
| Heavy haul, approaching assault | Drop part of the load | Released bodies remain while movement becomes less burdened | No hard slot count is asserted | DK-003 |
| Loose ore still underground | Open console with existing bank | Unreturned ore cannot pay the node | Extraction is not delivery | DK-003 |
| Haul reaches dome intake | Deliver the material bodies | Bodies are removed and typed bank increases | No RTS worker job or Prestige points | DK-003 |
| Affordable offered node, prerequisites met | Buy at console | Bank price is spent and capability changes for this run | Not permanent account power | DK-004 |
| Clock running | Open upgrade/selection console | Live simulation pauses for planning | No simultaneous paid mining | DK-004 |
| Initial unpurchased instrument | Buy that meter | Corresponding value becomes visible | Underlying health/time already existed | DK-009 |
| Keeper still below ground | Let interval expire | Hostiles attack the dome anyway | No forced return or waiting enemies | DK-005 |
| Keeper reaches console | Enter weapon control and hold/steer fire | Mount traverses and beam exposure affects targets | Cannot simultaneously drill elsewhere | DK-006 |
| Shield available, attack hits | Resolve compatible damage | Shield is consumed before exposed dome condition | Shield loss is not immediate loss | DK-007 |
| Active assault and reduced shield | Avoid a hit briefly | Battle still prevents ordinary shield recharge | Not a personal quiet-gap shield | DK-007 |
| Overcharge node bought, water available, outside battle | Use left generator | Water payment enables the declared coming-wave enhancement | Buying the node alone is not activation | DK-008 |
| Acquired ready Shield battle node | Request its eligible active response | The declared temporary field, invulnerability or reflection occurs | Not all abilities at landing or an ordinary laser shot | DK-011 |
| Eligible repair and cobalt bank | Buy repair service | Stock pays for the declared health recovery | Not automatic wave-clear hull healing | DK-004, DK-007 |
| No pending entries or surviving attackers | Settle the ordinary wave | Next mining interval resumes with retained state | First kill is not cycle completion | DK-005 |
| Dome integrity exhausted | Continue trying to haul or fire | The attempt ends | Healthy operator cannot replace the base | DK-007 |

## Strategic and experiential structure

- Local choice: exchange digging time against return distance and the
  currently bearable load; drop surplus rather than treat all mined ore as
  already secured. Use exposure time and mount travel to prioritise threats.
- Medium horizon: tools, carry strength, information, laser performance and
  protection compete for the same delivered bank. A meter can improve a
  decision without adding time or health itself.
- Longer context: the relic belongs to the continuing run; this unit ends
  after the first complete cycle rather than claiming its final extraction.
- Failure attribution: retained cracks, late return, cargo speed and target
  switching explain costs, but exact hidden health/clock values may still be
  absent before their instrument purchases. No optimal build is promised.
- Trust: learning the time budget and deposit boundary matters more than
  assuming a new player begins with complete numerical telemetry.
- Claims: DK-002–DK-010.

## Replay and variation

- Opening mine layout, material location/hardness, route and purchased choices
  vary. No exact seed, ore guarantee, first-wave composition or native RNG
  distribution is inferred from one recording.
- Later optional gadgets or a full relic run are separate scope extensions;
  the visible full product is not silently flattened into this first cycle.
- Claims: DK-002–DK-010.

## Adjacent systems and history

- The official launch texts distinguish the growing released game from
  Dome Romantik and its demo gadget economics. Assessor, cooperative play,
  new domes and post-2024 overcharge are not launch facts.
- Compare the canonical selected neighbours only after the complete scan;
  thematic mining resemblance is not a signature match.
- Claims: DK-001, DK-008.

## Normalised genome

| Type | Genes |
| --- | --- |
| Action | `ACT-008`, `ACT-048`, `ACT-130`, `ACT-159`, `ACT-161`, `ACT-190`, `ACT-341` |
| System | `SYS-212`, `SYS-213`, `SYS-1285`, `SYS-1648`, `SYS-1649`, `SYS-1650`, `SYS-1651`, `SYS-1652`, `SYS-1653` |
| Constraint | `CON-136`, `CON-206`, `CON-304`, `CON-830`, `CON-831`, `CON-832` |
| Information | `INF-117`, `INF-235`, `INF-540`, `INF-541` |
| Objective | `OBJ-020` |
| Time | `TIM-003` |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `564` (`GAME-0001`–`GAME-0564`).
- Exact genome matches: none.
- Tied near matches: `GAME-0405` — Fable II (`7 / 37 = 0.189189`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0405` — Fable II | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-341`, `CON-136`, `INF-117`, `TIM-003` | Both link direct world actions, paid choices, retained prerequisite states and inspectable transaction offers. Fable II follows authored childhood deeds and its purchase/activation handoff; Dome Keeper physically banks loose ore against an unattended base-assault clock, then occupies a slewing laser and preserves a separate dome through the whole first wave. | Tied near: 7 / 37 = 0.189189. |

### Preserved research notes

- New genes: eleven; seventeen unchanged definitions reused.
- Classification result: New gene.

## Taxonomy impact

- Registry additions: SYS-1648–SYS-1653, CON-830–CON-832, INF-540–INF-541.
- [Taxonomy Change 311](../../../research/taxonomy-changes/TAXONOMY_CHANGE_311.md)
  records accepted boundaries and rejected alternatives.

## Negative results

- None as a separate prior-claim rejection. Uncertified launch timing and
  current-versus-original source limits remain explicit qualifications.

## Delta summary

## New facts

- [Observation | Corroborated | High] DK-002–DK-006 and DK-009: physically
  banked mining, paid telemetry and station-bound live defence form one cycle.
- [Observation | Corroborated | Medium] DK-007: the recharging shield does
  not erase underlying persistent dome damage or recharge during combat.

## New genes

- [Observation | Corroborated | Medium] SYS-1648–SYS-1653, CON-830–CON-832,
  INF-540–INF-541.

## New combinations

- [Observation | Direct | High] No new combination proposal; proper-subset
  applicability is checked against every accepted combination.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_311; no earlier
  signature, definition or lifecycle changes.

## New questions

- Which exact launch executable and seed would reproduce the declared route?
- What precise ordering governs expiry, pending entries and assault completion?
- What are the original per-tier slew, contact-damage and shield recharge rates?

## Next recommended game

- [Hypothesis | Limited | High] English European Nintendo DS Elite Beat
  Agents, GAME-0566, under approved Selection 045.
- Optimisation criterion: native touch-rhythm performance after mining defence.
- Expected information gain: the complete performance's tap/hold/spin mapping
  and timing-to-team-state relation without later rhythm-game substitutions.
- Backlog impact: two approved subjects remain; stop after GAME-0567.
  No push, publication, Actions, merge or deploy is authorised.

## Why this game

- [Hypothesis | Limited | High] The approved complete mining/defence cycle
  separates finding, hauling, banking, investing and protecting a different
  survival-bearing body, broadening the mixed-platform full-release horizon.
