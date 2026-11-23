---
game_id: GAME-0517
slug: homeworld
game_title: Homeworld
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-121
    - ACT-189
    - ACT-316
    - ACT-317
    - ACT-318
    - ACT-710
    - ACT-711
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-549
    - SYS-551
    - SYS-554
    - SYS-1467
    - SYS-1468
    - SYS-1469
    - SYS-1470
    - SYS-1471
  constraint:
    - CON-282
    - CON-467
    - CON-469
    - CON-796
  information:
    - INF-224
    - INF-502
  objective:
    - OBJ-029
    - OBJ-292
  time:
    - TIM-003
---

# Game: Homeworld

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Ship classes, resource amounts, formations, keys and mission labels are
parameters.

## Analysis scope

- Version / ruleset: original English Windows retail base campaign released
  by Sierra in 1999, fresh single-player start with the Kushan fleet.
  Ordinary orders only. The launch manual and published Windows routes
  define the product boundary. A pinned mirror of the later Relic source
  release specifies implementation evidence where identified. The exact
  retail patch and distribution binary remain unverified.
- Structured analysis target: `PLAT-WINDOWS-PC`, original retail game.
- Primary decision loop: sustain the fleet by ordering a Resource Collector
  to deposit cargo and committing ship orders from the same stock. Read
  the tactical and sensor views, issue destinations with elevation and
  assign formation or stance before attacking the appropriate drone group.
  Build a Salvage Corvette, deliver the last drone and use the first
  hyperspace handoff once all primary checks are complete.
- Entry and exit: first normal fleet control after the Mothership departs the
  scaffold in Mission 01, Kharak System. Finish when the committed first
  jump arrives in Mission 02, before any order there. Mission 02 combat,
  intervention and exploration are outside the unit.
- Included: seven Scouts and the initial collector, stable Mothership,
  autonomous hauling and delivery, spending and live production, selectable
  three-dimensional move and attack orders, ship formation and tactics,
  service through docking, optional early ship research and construction,
  target marking, both qualifying drone clears and their local retries,
  capture and delivery of the last intact practice drone, and the
  player-triggered campaign jump with fleet and stock retention.
- Excluded: separate Training mode, alternate Taiidan route, first orders at
  Khar-Selim, later research and combat, removed Interceptor trial, competing
  multiplayer failure and jump rules, Homeworld 2, Remastered rules and
  unofficial ports. Arbitrary paths, fuel coefficients and timings are
  outside the evidence.
- Potential scoped modules: escorting the Khar-Selim salvage team, resource
  controller routing and combat capture of armed ships after the training
  packet.
- Direct-play status: no original executable, console, video or audio was
  played. The Sierra and Relic manual, licensed first-mission guide and
  separately authored Windows routes establish the documented path.
  Read-only inspection of the later published source corroborates ordered
  predicates and limits claims about exact patch behaviour. The legal
  collection includes a compatible Classic product and a separate remaster.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| HW-001 | Relic and Sierra released the original English Windows game in 1999. The later collection distinguishes Classic from the remaster. | Confirmed | Direct | High | P1, P3 |
| HW-002 | A selected ship or group can commit a cursor-picked horizontal destination with a separately set elevation. Ship sensors provide current local detail and scripted markers guide the route at overview scale. | Observation | Corroborated | High | P1, S1, R1 |
| HW-003 | A collector gathers and unloads finite resources. The deposit credits spendable stock and a separate mission collection total. The examined source checks 500 collected units. | Observation | Corroborated | High | P1, P2, S1, S2, R1, R2 |
| HW-004 | Construction of a Research Ship is a primary check. Fighter Chassis research is secondary and unlocks the Interceptor. The examined script does not start the old advanced drone trial. | Observation | Corroborated | High | P1, P2, S1, S3, R1, R2 |
| HW-005 | The first group requires qualifying formation use and clearance. The second requires qualifying non-neutral tactics and clearance. Cleared groups can be replenished when their method was missed. | Observation | Corroborated | High | P1, P2, S1, R1, R2 |
| HW-006 | A Salvage Corvette takes the practice drone back to the Mothership. The training drone is not retained as an operable captured ship. | Observation | Corroborated | High | P1, P2, S1, S4, R1, R2 |
| HW-007 | All five primary objectives grant jump readiness. The player starts the first campaign jump to an authored destination with the surviving qualifying fleet and completed investments. | Observation | Corroborated | High | P2, S1, S5, R1, R2 |
| HW-008 | An eligible docking service can restore fuel and damaged hull. Production and research can advance while different craft are carrying out accepted orders. | Observation | Corroborated | High | P1, S2, S3, R2 |
| HW-009 | Exact changes between the original retail patches and the inspected released source are not established. | Observation | Limited | High | P1–P3, S1–S5, R1, R2 |

## Basic data

- Release / origin: Relic Entertainment and Sierra Studios, Windows, 1999.
- Platform or physical form: original Windows retail CD-ROM campaign,
  mouse and keyboard.
- Puzzle family: real-time system pressure, agent routing and coordination,
  and ordered dependency sequencing. Independent workers and combat groups
  operate concurrently while scripted tests impose prerequisites.
- Primary publisher and developer materials:
  - P1 [Sierra and Relic: original Homeworld manual](https://sierrachest.com/gfx/games/Homeworld/box/manual.pdf).
    Gameplay sections 3.2–3.7 and 4.2 describe commands, views and managers.
  - P2 [Prima's licensed Homeworld strategy guide](https://homeworldarchives.com/media/Homeworld_Prima_Official_eGuide.pdf),
    first mission, printed pp. 74–75.
  - P3 [Publisher's collection listing](https://store.steampowered.com/app/244160/Homeworld_Remastered_Collection/)
    describes the included classic editions separately from the remaster.
- Published source mirror, read as text at commit
  `163a124378e92933d290882e32de9fd8bca4c806`:
  - S1 [Mission01.kas, final objectives and unlocks](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Missions/SinglePlayer/Mission01.kas#L2156).
    Compare the repopulation states and the checks from lines 2156–2328.
  - S2 [Dock.c, resource return and service](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Game/Dock.c#L1311).
    The mission counter uses deposited cargo via
    [KASFunc.c](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Game/KASFunc.c#L1914).
  - S3 [ResearchAPI.c, lab scheduling and unlock](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Game/ResearchAPI.c#L459).
    A topic's timer is advanced according to its assigned laboratories.
  - S4 [SalCapCorvette.c, delivery handling](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Ships/SalCapCorvette.c#L803).
    The target-drone branch removes the object from capture retention.
  - S5 [SinglePlayer.c, fleet departure and arrival](https://github.com/rcarmo/homeworld/blob/163a124378e92933d290882e32de9fd8bca4c806/src/Game/SinglePlayer.c#L2410).
    Later source details are qualified separately from the retail documents.
- Independent practical routes:
  - R1 [Giovanni's Windows mission walkthrough](https://gamefaqs.gamespot.com/pc/141615-homeworld/faqs/10852),
    mission 01 target order and optional research before the jump.
  - R2 [BKerensky's original Windows walkthrough](https://cdn.nivoli.com/the-spoiler/STRATEGY/Sierra/homeworld.5.html),
    mission 01 initial fleet, drone groups, salvage, optional preparation
    and docking.
- Claim IDs: HW-001–HW-009.

## Mechanical decomposition

### Action Genes

- `ACT-121` selects an eligible research topic when a working lab is available.
- `ACT-189` commits a target or a movement order that the selected ships
  subsequently execute. `ACT-710` separately sets the flat position and the
  height of a single destination before issuing it.
- `ACT-316` inserts a currently buildable craft into the Mothership's
  production list. `ACT-318` assigns the Resource Collector a particular
  reachable source or the ordinary nearest-source harvest command.
- `ACT-317` sets formation and tactics on selected ships. For example,
  set the Scouts in Delta for the first fight and use Evasive or Aggressive
  when engaging the second group.
- `ACT-711` assigns a Salvage Corvette to the eligible intact target drone.
  The craft brings it back after securing it.
- Claim IDs: HW-002–HW-006.

### System Behaviour Genes

- `SYS-297` resolves unit travel and target acquisition from an accepted
  order. `SYS-215` resolves the live exchanges. `SYS-554` applies the set
  formation to group movement and the selected tactics during engagement.
  Tactical choices can change evasion, maneuverability and firepower.
- `SYS-305` updates the region revealed in detail by current friendly
  sensors. A scripted objective marker can still direct an approach.
- `SYS-549` converts a return trip with asteroid cargo into a deposit at
  the Mothership, which is the stationed production and drop-off site for
  this mission. Deposits increment the spendable and cumulative totals.
  `SYS-551` advances paid construction while the fleet follows other orders.
- `SYS-1469` allocates the available ship laboratory to an eligible topic.
  The reference implementation can combine labs on one topic or run
  distinct topics when additional capacity and topics are available.
  Completing Fighter Chassis allows Interceptor production and opens the
  Corvette Drive research opportunity. Building more labs is optional.
- `SYS-1467` renews only the targets in a failed practice stage. Current
  fleet and economic activity can continue. The inspected script can
  replace the whole formation or tactics group when it is eliminated
  without the respective qualification, or the salvage target after
  destruction without capture.
- `SYS-1468` separates a Corvette's attachment from successful delivery.
  An intact target can be towed to the Mothership. The practice target
  is consumed by the task and does not add a controllable drone.
- `SYS-1471` recovers missing fuel and damaged hull through service at a
  compatible dock. A craft may stay inside if launch is held, or return
  to play after servicing.
- `SYS-1470` resolves the requested hyperspace handoff, carrying the
  eligible fleet, remaining spendable stock and completed technologies
  into the authored successor. No claim is made about every transient
  order, uncollected asteroid or in-progress job surviving the jump.
- Claim IDs: HW-002–HW-009.

### Constraint Genes

- `CON-282` orders formation, tactics and salvage and requires the economic
  and research-ship milestones before the jump readiness signal.
- `CON-467` restricts construction by owned site, stock and technology.
  Interceptors depend on optional research; the prescribed salvage
  craft can be built for the trial without completing that research.
- `CON-469` requires accessible asteroid material and an eligible owned
  drop-off site for the collector's full economy loop.
- `CON-796` requires both qualifying tactic or formation use by engaged
  attackers and depletion of that target group. Merely selecting a
  stance on unrelated craft does not qualify the trial.
- Claim IDs: HW-003–HW-007.

### Information Genes

- `INF-224` locates selected ships, hull and current fuel and displays the
  stockpile and active production or research in their managers.
- `INF-502` distinguishes detailed current sensor regions from coarse regions
  at overview scale and displays objective pings. The separate movement disc
  displays a pending three-dimensional destination as part of `ACT-710`.
- Claim IDs: HW-002–HW-005, HW-008.

### Objective Genes

- `OBJ-029` defeats the finite required group in each drone-clear stage.
- `OBJ-292` certifies the bounded multistage fleet exercise and initiates
  the authored successor jump. Harvest, Research Ship, qualifying formation
  clear, qualifying tactics clear and delivered intact drone are the five
  mandatory flags. Fighter Chassis is an optional research result.
- Claim IDs: HW-003–HW-007.

### Time Genes

- `TIM-003` runs travel, mining, construction, research and combat together
  while the player issues orders. Leaving the sector is a separate choice
  after the required flags settle.
- Claim IDs: HW-002–HW-008.

## Reproducible transitions

| Before | Action | Result | What it establishes | Claim |
|---|---|---|---|---|
| Initial fleet with one Resource Collector and no lab | Give the collector a harvest order and queue a Research Ship | Collection and live construction can advance together | Economy does not require continuous direct steering | HW-003, HW-004 |
| An asteroid is reachable and the collector has cargo | Let it return and unload while spending available stock on ships | Cargo delivery increases both stock and a gross-collected counter. The examined mission watches the latter for 500 units | Starting or remaining stock is separate from delivery credit | HW-003 |
| Scouts are selected during an unpaused exercise | Bring up the movement disc, set a flat destination and adjust its height before committing | The selected craft travel toward a point above or below the initial plane | One command sets three-dimensional intent | HW-002 |
| A lab is completed and Fighter Chassis is available | Research the topic and let it finish, or leave it alone until all primary flags settle | Completion opens Interceptor construction. The jump can be enabled without the optional completion | Building the lab and completing its research are distinct | HW-004, HW-007 |
| The nine-drone formation group is active | Attack using a supported formation until the group is gone | Registration of formation use and zero remaining targets together finish the first trial | A valid method and its outcome are separately checked | HW-005 |
| The next group is active after the briefing | Fight in Evasive or Aggressive. Compare clearing it in Neutral throughout | Qualifying engagement followed by zero targets clears. In the reference script, clearing without that qualification brings replacement targets | A local retry preserves the rest of the mission | HW-005 |
| A single salvage target exists and the Corvette is ready | Issue capture and wait for it to bring the target to the Mothership | Delivery credits the trial. Destroying the target instead can cause replacement | Attacking, towing and delivering differ | HW-006 |
| A strike craft has spent fuel or suffered damage | Dock at an eligible service bay and wait for service | Bounded stock and hull condition recover while that craft is unavailable in space | Docking affects later live readiness | HW-008 |
| All five primary flags are complete | Continue harvesting or researching, then choose Hyperspace | The first successor is fixed. Fleet and completed investments arrive rather than a fresh reset | Readiness grants a choice to commit | HW-007 |

## Strategic and experiential structure

Start extraction early so its returns can pay the required new ships while
the Scouts perform drills. In the first drill, the player can choose a usable
formation. In the second, choose whether to prioritize evasion or aggression.
Changing the input matters only when the group uses the setting during the
exercise. A wrong clear is recoverable without rebuilding the economy.
Leave the last target intact for towing. Delaying the jump can improve the
next fleet but exposes extra waiting and additional resource choices.
HW-002–HW-008.

## Replay and variation

The mandatory objective sequence, successor and trial roles are authored.
Travel paths, composition, construction order, optional research, time spent
gathering and use of local retries can vary. The mirrored mission script
uses randomized briefing offsets. Those offsets do not establish procedural
enemy locations or a different objective sequence. HW-003–HW-009.

## Adjacent systems and history

The nearest RTS signatures share issuing orders while the worker economy
and build channels advance. Homeworld's first packet tests each attack
method and resource delivery separately, adds a height axis to movement
orders and uses a salvage trial before a retained fleet jump. Measured
similarity and causal comparison belong to the selected-neighbour table.
No development lineage claim follows.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-121, ACT-189, ACT-316, ACT-317, ACT-318, ACT-710, ACT-711 | Select research, issue group orders, build, harvest, choose formation and tactics, set height and order salvage |
| System Behaviour | SYS-215, SYS-297, SYS-305, SYS-549, SYS-551, SYS-554, SYS-1467, SYS-1468, SYS-1469, SYS-1470, SYS-1471 | Movement, live combat, sensors, stock delivery, queue, formation, retry, tow, research, jump and dock |
| Constraint | CON-282, CON-467, CON-469, CON-796 | Order of trials, purchasing and drop-off eligibility, qualifying attack method |
| Information | INF-224, INF-502 | Fleet and production status, local and sensor scale, pending movement coordinates |
| Objective | OBJ-029, OBJ-292 | Finite groups, required exercise and first campaign jump |
| Time | TIM-003 | Live concurrent ship activity |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `516` (`GAME-0001`–`GAME-0516`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`15 / 41 = 0.365854`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` Age of Empires II: Definitive Edition | ACT-121, ACT-189, ACT-316, ACT-317, ACT-318, SYS-215, SYS-297, SYS-305, SYS-549, SYS-551, SYS-554, CON-467, CON-469, INF-224, TIM-003 | Both advance harvesting, production and ranged engagements under live group orders. Age of Empires uses land workers and local buildings in the selected scope. Homeworld coordinates movement with elevation and tests the combat method, intact salvage delivery and a committed fleet transfer. | Near, `0.365854` |

## Taxonomy impact

- [TAXONOMY_CHANGE_264](../../../research/taxonomy-changes/TAXONOMY_CHANGE_264.md)
  records ten additions and seventeen unchanged transfers.

## Negative results

- The Research Ship is mandatory. Researching Fighter Chassis is a separate
  secondary objective. The archived lines intended to start an advanced
  Interceptor test are disabled. That dormant route is excluded.
- The first mission's reference code counts deposited resources, rather
  than the current balance or the number of harvest orders. The
  `500` threshold comes from the inspected source. Some adjacent
  comments only say one load. No exact equivalence across patches is claimed.
- The captured practice drone is consumed. Broader ownership changes and
  refitting of captured warships need a separate later mission.
- The first departure is an authored campaign transition. Tactical
  multiplayer jumps, their destination choice and possible fees are excluded.

## Delta summary

## New facts

- [Observation | Corroborated | High] Supported formation and tactics must
  have been used in their separate fights before clearance can qualify.
  The reference implementation can restore the rejected target group. HW-005.
- [Observation | Corroborated | High] Successful salvage requires taking
  the trial drone home intact. Primary checks then authorize the jump.
  Research completion remains optional. HW-004, HW-006, HW-007.

## New genes

- ACT-710, ACT-711, SYS-1467, SYS-1468, SYS-1469, SYS-1470, SYS-1471, CON-796,
  INF-502 and OBJ-292.

## New combinations

- No new combination; compare the recognised subsets above.

## Taxonomy changes

- Ten new stable definitions. All earlier game signatures remain unchanged.

## New questions

- A native retail reproduction could identify the precise patch behaviour
  of the collected-resource threshold and the fleet-readiness exceptions.

## Next recommended game

- `GAME-0518` Pokémon Pokopia, released Nintendo Switch 2 base game.

## Why this game

- [Hypothesis | Limited | Medium] Combining freely elevatable orders,
  concurrent logistics and demonstration predicates distinguishes this opening
  from otherwise similar production-led RTS packets.
