---
game_id: GAME-0568
slug: teardown
game_title: Teardown
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-201
    - ACT-202
    - ACT-303
    - ACT-341
    - ACT-446
  system:
    - SYS-036
    - SYS-147
    - SYS-369
    - SYS-862
    - SYS-1662
    - SYS-1663
    - SYS-1664
  constraint:
    - CON-068
  information:
    - INF-125
    - INF-256
  objective:
    - OBJ-310
  time:
    - TIM-003
---

# Game: Teardown

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A local change to voxel collision changes the route available to the same
avatar. The launch event, running deadline, target collection and escape are
separate state boundaries.

## Analysis scope

- Version / ruleset: base Windows Steam Teardown 1.0 full release, 21 April
  2022, App 1167630. Ordinary solo campaign, default 60-second alarm interval,
  standard health and tool settings, no mods, skips, loadout expansion or
  assist changes. Target The Login Devices at Lee Chemicals, not the earlier
  The Lee Computers or the prototype, Early Access, later console or updated
  multiplayer editions. Exact launch depot and cross-patch parity unverified.
- Structured analysis target: PLAT-WINDOWS-PC in knowledge/platforms/games.json.
  Steam's present product page identifies the same app but its current feature
  list does not establish which features existed in the 2022 binary.
- Entry: after completing The Lee Computers, start The Login Devices with the
  ordinary early unupgraded tools and none of its three assigned readers
  collected. Begin on arrival with the alarm countdown inactive, the escape
  van designated and original mission geometry. Earlier missions are setup.
- Primary decision loop: inspect the required positions and exit, choose the
  collection order, then test travel while reshaping eligible obstacles or
  repositioning props and vehicles. Save the prepared state where allowed.
  The first qualifying alarm event begins the shared countdown. Move through
  the route, collect the remaining readers and reach the designated van with
  time left. On failure, choose quickload of the prepared state or a fresh
  mission restart and revise the route.
- Positive exit: settle the mission only after collecting all three distinct
  readers and reaching the escape van before the active clock expires. The
  last reader alone is not a clear; there is no separate carry-and-deposit
  step for each reader. Stop at the successful mission result before a later
  mission or the upgrade menu adds a new loop.
- Negative exit: expiry with the escape predicate unmet fails the attempt.
  Reaching the exit with missing readers does not settle it. Reloading an
  allowed earlier save discards later changes rather than paying for time or
  disarming the alarm within the running attempt.
- Included: direct on-foot movement, jump and crouch through the live collision
  envelope, contextual doors/readers and escape, eligible portable props and
  vehicles, aimed breach and sustained tools, material-sensitive local voxel
  removal, unsupported-body physics, fire spread and extinguishing, mission
  map and status cues, shared alarm, terminal expiry, player-selected prepared
  state quicksave/load and ordinary authored restart. Fire and disturbed
  alarm-linked assemblies can make preparation trigger the response early;
  exact ignition count and circuit tolerances are unverified.
- Time boundary: preparation has no running escape allowance but physics and
  fire still advance. A first eligible trigger starts one countdown, and
  later pickups do not add time. Saving a prepared state does not suspend the
  running clock in place; loading that state replaces the failed progression.
- Excluded: The Old Building Problem demolition target, The Lee Computers
  without this device-tether rule, later pursuit missions and alarm variants,
  optional valuables and tool economy, earned rank, hidden collectibles,
  later weapons/planks, sandbox, DLC, Workshop, assists, multiplayer and native
  build, material radii, fire and damage coefficients. Optional valuables are
  not required to settle the scoped objective. The analysis does not claim
  alarm-active saving, exact slot capacity or persistence after quitting.
- Potential scoped modules: alarm-linked moving cargo, helicopter pursuit,
  settlement-funded loadout development or mission variants with different
  security and terminal predicates.
- Direct-play status: not conducted. The 1.0 release announcement, publisher
  storefront and engine documentation were read. The dated launch-day guide
  and a November 2022 written firsthand route corroborate normal play. The
  later community mission/security entries corroborate the named targets and
  list potential early triggers; they do not prove historical coefficients.
  No game executable, video or audio was played, and no frame-exact replay
  or manual test of the 2022 build was performed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TD-001 | The full Windows campaign released as version 1.0 on 21 April 2022. The currently marketed app also contains later changes. | Confirmed | Direct | High | P1, P2 |
| TD-002 | On-foot movement, conventional access, eligible tool breaches and driveable vehicles change how the player traverses or reshapes the live location. | Observation | Corroborated | High | P2, S1, S2 |
| TD-003 | Selective material-sensitive removal leaves a still solid remainder. Damage can release unsupported chunks and props to continuous motion. Some openings are usable, depending on the remaining geometry and avatar clearance. | Observation | Corroborated | High | P2, P3, S1 |
| TD-004 | The mission begins with its escape clock inactive. Taking an alarm-linked reader starts one shared 60-second default interval; disturbing its alarm attachment or allowing a large fire can start the response earlier. No later pickup reloads the clock. | Observation | Corroborated | Medium | S1, S2, S3; exact thresholds not certified |
| TD-005 | Three distinct required devices at north factory, storage and west factory are credited locally. The van is still required before expiry. Map and status disclose targets and running time. | Observation | Corroborated | High | S1, S2, S3 |
| TD-006 | Saving after preparation and loading after failure reuses the altered geometry and saved position before pickup. Restart instead re-enters the authored mission. No arbitrary save persistence is claimed. | Observation | Corroborated | Medium | S1, S4 |
| TD-007 | Fire can persist and spread among eligible material during preparation; the ordinary extinguisher acts on local fire. A spray mark is a visual aid, not a new passable link or a route command. | Observation | Corroborated | Medium | P3, S2, S3, S4 |

## Basic data

- Tuxedo Labs; base solo Windows campaign, scoped to a complete alarm heist.
- Families: FAM-007 physics and object manipulation and FAM-010 real-time
  system pressure. The route is authored by
  changing reachable space before passing it under the active deadline.
- P1: [Tuxedo Labs, version 1.0 release announcement, 21 April 2022](https://store.steampowered.com/news/posts/?appgroupname=Teardown&appids=1167630&enddate=1655386552&feed=steam_community_announcements),
  complete campaign and explicit transition out of Early Access. Checked
  2026-11-20. The legacy article redirect failed, so use the original full
  announcement retained in the app news feed.
- P2: [Teardown publisher storefront](https://store.steampowered.com/app/1167630/Teardown/),
  exact app, release date, voxel environment, tools and vehicle interaction.
  Current multiplayer copy is excluded from the 1.0 target.
- P3: [Tuxedo Labs materials/connectivity documentation](https://www.teardowngame.com/modding/index.html)
  and [Lua API reference](https://teardowngame.com/modding/api.html),
  material-based voxel removal and distinction between shapes and bodies.
  Current references corroborate engine abstractions only. No mod or API
  command constitutes a legal player input in the chosen campaign mission.
- S1: [Victor Tan, dated PC route report, 21 April 2022](https://www.gamepur.com/guides/how-to-complete-mission-3-the-login-devices-in-teardown),
  three readers, material openings, vehicles, saving after preparation,
  60-second countdown and departure. Direct written account with screenshots,
  no installed build ID recorded.
- S2: [November 2022 first-hand written mission walkthrough](https://teardownmechanicswalkthrough.blogspot.com/2022/11/the-login-devices.html),
  map, route preparation, tools and vehicles, first pickup, timer and escape.
- S3: [community mission entry](https://teardown.fandom.com/wiki/The_login_devices)
  and [security entry](https://teardown.fandom.com/wiki/Security), indexed
  passages corroborate three positions, alarm boxes and fire as an early
  trigger. Later values and platform/mode variants do not fix the 1.0 build.
- S4: [GameStar 07/2022 full-release review](https://download.gamestar.de/public/110500/110512/07_2022_060.pdf),
  published worked example of untimed setup, live clock and pre-alarm save;
  its illustrated mission is an independent common-rules example, not
  evidence of Lee Chemicals' exact geometry.
- Claim IDs: TD-001–TD-007. Sources last checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 and ACT-202 cover direct navigation/jumping and changing posture.
  Walking through a gap depends on locally remaining geometry, not a path
  command or a teleported crossing. ACT-201 covers direct driving of a
  reachable site vehicle, separately from the escape interaction.
- ACT-048 covers held and released eligible props. ACT-303 covers committing
  a compatible tool against one construction surface. ACT-446 covers a held
  stream directed at its local region, with different effects for spray paint
  and extinguishing. Marking a route does not create collision or guidance.
- ACT-341 covers ordinary contextual access and collection. A reader pickup
  is a credited target interaction, not carrying a physics prop to the van.
- Claim IDs: TD-002–TD-005, TD-007.

### System Behaviour Genes

- SYS-1662 owns partial local voxel removal. SYS-147 owns the later loss of
  structural support and collapse; SYS-036 handles free rigid body motion.
  A surviving wall stays collidable even beside a large opening. No claim
  maps every material to a universal tool, sufficient hit count or radius.
- SYS-862 covers growing and extinguishing local fire; the alarm rule is
  distinct. The small active fire itself is not a countdown. SYS-1663
  activates the shared clock once via an eligible event. Thereafter suppressing
  a cause or collecting a later reader does not reset live alarm progression.
- SYS-1664 restores the player-saved prepared state. SYS-369 separately
  covers choosing or restarting from the authored initial state. An ordinary
  reset does not retain a prepared passage from an abandoned attempt.
- Claim IDs: TD-002–TD-007.

### Constraint Genes

- CON-068 binds success to the shared remaining escape allowance. Before
  activation there is no countdown debit; its start transition belongs to
  SYS-1663. Tool/material eligibility and passage clearance are explicit
  parameters of ACT-303 and SYS-1662, not a global life bar for each wall.
- Claim IDs: TD-003–TD-005.

### Information Genes

- INF-125 covers the mission map and marked objective locations, allowing
  planning before collection. INF-256 covers local objective, alarm state,
  remaining time and exit information. A map marker does not certify that a
  preferred newly opened route is physically traversable.
- Claim IDs: TD-004, TD-005.

### Objective Genes

- OBJ-310 requires the entire set of three distinct targets and timely escape
  at the van. The attached target's pickup gives immediate objective credit;
  no valuables deposit and no separate second success horizon is required.
- Claim IDs: TD-004, TD-005.

### Time Genes

- TIM-003 covers continuously active physics, fire and motor control during
  preparation and execution. The independent timer is active only after
  the first qualified trigger. Saving and loading are separate state changes,
  not optional slow-motion controls.
- Claim IDs: TD-002–TD-007.

## Reproducible transitions

These are source-reconstructed game conditions, not reports of native tests.

| Before | Action | Rule resolution | Boundary | Claim ID |
| --- | --- | --- | --- | --- |
| None of three readers credited; clock inactive. | Inspect the marked sites and move without triggering security. | Live geometry and movement change without spending the escape interval. | Preparation is live simulation, not planning in a frozen menu. | TD-002, TD-004, TD-005 |
| A solid eligible surface separates two accessible spaces. | Apply a compatible impact to part of the surface. | Local volume disappears while the connected remainder stays; passing requires sufficient clearance. | Partial geometry is more than whole-object durability. | TD-003 |
| Local changes remove the last support of a fragment. | Let the simulation advance. | The detached body can fall and collide. | Voxel removal and free-body collision are separate responses. | TD-003 |
| An eligible scene prop or site vehicle is reachable. | Grip and release the prop, or enter and drive the vehicle. | Straightforward manipulation changes obstacle positions; vehicle movement can also contribute physical breach. | Direct controls produce spatial effects, not a preselected route. | TD-002, TD-003 |
| Preparation is ongoing and a pickup is linked to its alarm. | Collect the first reader. | It gives credit and starts the shared alarm interval under default settings. | Starting the clock is part of the world action. | TD-004, TD-005 |
| An active small fire is propagating before pickup. | Direct the extinguisher at its current region before the alarm triggers. | Covered flames can be suppressed; sufficiently large active fire is still an early trigger. | Fire is an independent sim state, not an automatic fail on ignition. | TD-004, TD-007 |
| A timed attempt already credited one reader. | Take another distinct reader. | The credited set grows without restarting the countdown. | No per-target clock. | TD-004, TD-005 |
| Only two readers are credited or all three are held but time reaches zero before the van. | Reach the departure region too early in collection or too late in time. | No successful result. | Count, spatial departure and time are conjunctive. | TD-005 |
| All three readers are credited and time remains. | Reach the designated van and depart. | The active mission settles successfully. | Completion takes the whole mission, not the last pickup. | TD-005 |
| Preparation saved with an opening before the first pickup; later attempt failed. | Quickload, then separately try an ordinary mission restart. | Quickload returns the saved opening and position; restart returns to the authored layout. | The two retry anchors differ. | TD-006 |

## Strategic and experiential structure

- Local decision: choose an opening and tool whose result is suitable for the
  avatar or vehicle. A damaged-looking surface is not necessarily a passage.
- Medium-term planning: every traversal link and the last approach to the van
  compete for the same clock after activation. Test the resulting route while
  the clock is inactive, then use its stable geometry for the timed attempt.
- Failure attribution: a wrong order, insufficient opening, premature trigger
  or slow last segment each leaves different evidence in the world and HUD.
- Trust factors: the objective set and expiry are visible. Fire, body collision
  and actual usable clearance can be inspected before the run. Exact engine
  constants are unnecessary to discriminate the causal branches.
- Claim IDs: TD-002–TD-007.

## Replay and variation

- The assigned reader positions and exit are authored. Different orders,
  passages, moved props and eligible vehicles form alternative solutions.
  No procedurally reshuffled target set or required one true sequence is
  asserted. Prepared quickload supports iterating on execution without
  rebuilding the same geometry.
- Claim IDs: TD-002–TD-006.

## Adjacent systems and history

- The preceding Lee Computers mission is another use of Lee Chemicals but
  does not establish the three-reader attachment and countdown contract.
- Siege soft breach and PAYDAY alarm phases contribute useful existing
  boundaries; neither supplies this whole combination of individual voxel
  edits, prepared snapshot and collection-to-escape clock.
- Claim IDs: TD-001–TD-006.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-048, ACT-201, ACT-202, ACT-303, ACT-341, ACT-446 | Input, passage height and tool coverage |
| System Behaviour | SYS-036, SYS-147, SYS-369, SYS-862, SYS-1662, SYS-1663, SYS-1664 | Material footprint, detached bodies and exact trigger thresholds |
| Constraint | CON-068 | Default 60-second active allowance |
| Information | INF-125, INF-256 | Displayed map, objective set, clock and escape cues |
| Objective | OBJ-310 | Three attributed pickups and one departure |
| Time | TIM-003 | Live simulation in both phases |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `567` (`GAME-0001`–`GAME-0567`).
- Exact genome matches: none.
- Tied near matches: `GAME-0279` — PowerWash Simulator (`5 / 24 = 0.208333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0279` — PowerWash Simulator | ACT-008, ACT-048, ACT-202, ACT-446, TIM-003 | Both use direct navigation, posture, props and a spatially aimed continuous stream in live space. PowerWash Simulator measures removal of dirt from retained surfaces. Teardown instead reshapes collision, restores prepared geometry and requires alarm-bound target collection plus departure. | Tied near: 5 / 24 = 0.208333 |

### Preserved research notes

- New genes: SYS-1662, SYS-1663, SYS-1664 and OBJ-310.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_314](../../../research/taxonomy-changes/TAXONOMY_CHANGE_314.md)
  records four new operational boundaries. No predecessor definitions,
  signatures or lifecycles are revised.

## Negative results

- None. Rejected substitute definitions are recorded in TAXONOMY_CHANGE_314.

## Delta summary

## New facts

- [Observation | Corroborated | High] TD-003–TD-006 separate preparation,
  local route alteration, alarm phase and full timed settlement.

## New genes

- [Observation | Corroborated | Medium] Four typed additions in
  TAXONOMY_CHANGE_314.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.
  Verified existing subsets are owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Four added definitions without edits
  to predecessors.

## New questions

- Exact historical material radii, failure tie order, active-alarm save
  permissions and fire thresholds require a native version-addressed test.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0569, original Apple II Lode Runner.
- Optimisation criterion: alternate platforms and eras; compare created
  passages in live voxel space with temporary dug cells on an authored grid.
- Expected information gain: distinguish timed hole recovery and guard
  traversal from irreversible physical removal and snapshot restoration.
- Backlog impact: second Selection 046 unit, followed by Cult of the Lamb.

## Why this game

- [Hypothesis | Limited | Medium] A complete alarm heist couples physical
  route editing to a later shared deadline and provides a measurable
  counterexample to both fixed-route heists and free-form demolition sandboxes.
