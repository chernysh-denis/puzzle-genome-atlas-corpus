---
game_id: GAME-0266
slug: deep-rock-galactic
game_title: Deep Rock Galactic
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0264
gene_ids:
  action:
    - ACT-008
    - ACT-050
    - ACT-093
    - ACT-130
    - ACT-161
    - ACT-218
    - ACT-341
    - ACT-443
  system:
    - SYS-116
    - SYS-215
    - SYS-348
    - SYS-407
    - SYS-810
  constraint:
    - CON-140
    - CON-609
  information:
    - INF-119
  objective:
    - OBJ-160
  time:
    - TIM-003
---

# Game: Deep Rock Galactic

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `548430`, sole one-app package `135552`, observed against public branch build
  `24903151` built 2026-08-24 with its branch record updated 2026-08-25;
  checked 2026-09-06. Ghost Ship Games' own most recent named patch
  announcement is `S06.05.02`, dated 2026-08-06. The branch was updated
  nineteen days after that announcement, so the installed build may carry an
  unannounced patch inside the season 6 line; this unit records both dates
  rather than asserting a single semantic version, and treats the numeric build
  identifier as a secondary distribution observation.
- Product boundary: this is **Deep Rock Galactic** on Windows, not a spin-off
  title or a franchise union. The fourteen listed DLC apps are separate
  products outside this packet. The product is season-based, so the declared
  attempt is made without any seasonal battle-pass content, cosmetic or
  otherwise, and no seasonal progression enters the packet.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, offline single-player. The declared configuration is one
  `Mining Expedition` at a fixed selected `Hazard Level` on one named biome,
  played solo as the `Driller` class, so the drone accompanies the player for
  the whole mission.
- Setup-only predecessor: a loadout carrying only the class's default equipment,
  with no purchased weapon modifications, overclocks, perks or drone upgrades.
  Those are separate persistent progression systems whose effects would change
  every value in this packet, so they contribute no genes or transitions.
- Entry: accept first ordinary control at the moment the drop pod lands and the
  dwarf leaves it at the start of the cave, before the first carve and before
  any mineral is collected.
- Primary decision loop: read the current health, shield, ammunition, carried
  minerals and the drone's remaining revive charges; carve continuous volumes of
  cave rock with the pickaxe or the class drills to open the route the mission
  needs, and take the declared material from any deposit the same carve removes;
  aim and fire at the hostiles the cave releases; point the drone at a deposit
  so it mines it, or at a hostile so it attacks, while it engages nearby threats
  on its own; carry the mined material to the mobile depository and deposit it
  irreversibly against the visible quota; when the deposited balance permits,
  order a resupply pod and take one of its racks to restore ammunition and
  health; and once the quota is filled, press the extraction call and cross the
  cave to the arriving transport.
- Positive terminal: after the declared collection quota is filled and the
  extraction call has been made, reach and board the arriving transport before
  its declared waiting interval expires, and accept the resulting mission-success
  result. The quota alone does not complete the attempt.
- Negative terminal: the attempt fails when the dwarf is downed while the drone
  has no revive charges remaining, and it also fails if the transport departs
  with nobody aboard. A single downing while the drone still holds a charge is
  recoverable and is not a terminal.
- Included: direct first-person traversal; carving continuous terrain volumes
  and taking the material of any deposit the carve removes; direct ranged and
  melee attacks; the pointer dispatch that gives the drone a task from the class
  of the target; the drone's own autonomous movement and engagement; deposits of
  carried material into the mobile depository against the declared quota; the
  quota's completion; the priced resupply call against the deposited balance and
  the finite racks it lands; interaction with the depository, the resupply racks
  and the extraction call as reachable authored objects; the layered shield,
  health, downed and revived combatant state; the drone's finite revive charges
  and the failure that follows their exhaustion; the extraction call, arrival,
  waiting interval and boarding; and the personal resource display.
- Excluded: all fourteen DLC apps; every seasonal battle-pass and event
  content; cooperative play with other players, which removes the drone
  entirely and replaces its revive rule with player revives; every other
  mission type, including the ones with different waiting intervals; every
  other class, its weapons and its traversal tool; weapon modifications,
  overclocks, perks and drone upgrades; the optional secondary-objective
  resource, which the declared route does not collect; the Space Rig, its
  vendors and all persistent progression; assignments, promotions and deep
  dives; achievements; all inputs and platforms not declared above;
  screenshots, official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `548430` from package
  `135552`, confirm the public branch build and the current named patch, and
  start an offline solo `Mining Expedition` at a fixed selected hazard level on
  one named biome as the `Driller` with default equipment only. From the drop
  pod, carve at least one tunnel that opens a route the natural cave did not
  provide, take material from at least one deposit removed by a carve, point
  the drone at one deposit and at one hostile, deposit carried material into the
  depository at least twice, order one resupply once the deposited balance
  permits and take exactly one rack, allow one downing and one drone revive,
  fill the declared quota, press the extraction call and board the transport.
  Exact hazard level, biome, quota size, mineral totals, hostile counts,
  ammunition values and remaining time are parameters.
- Potential scoped modules: another mission type; a cooperative session; another
  class; the modification, overclock and perk economy; a seasonal ruleset; or a
  deep dive requires its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus
  the current Steam product record establish lawful availability, exact product
  identity, Windows support, the sole package, the single-player and online
  co-op categories, adjustable difficulty and the fourteen separate DLC apps.
  Ghost Ship Games' own dated announcement supplies the current named patch.
  The public SteamCMD info projection supplies one dated secondary build
  observation. The official product wiki corroborates the mission's quota range
  and its deposit requirement, the extraction call, the transport's waiting
  interval and the failure that follows nobody boarding, the hazard levels and
  what they change, the shared pickaxe and its terrain and mineral effects, the
  class drills and their inability to mine certain minerals, the drone's
  availability in solo play, its pointer-commanded mining, its automatic
  engagement and its finite revive charges with the resulting solo failure, the
  resupply cost, its four racks and what each restores, and the shield, health,
  incapacitation and revival rules. This is an evidence-backed rules
  reconstruction, not a claimed playthrough or entitlement. No video or audio
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DRG-001` | Steam app `548430` and its sole one-app package `135552` identify the currently lawfully offered English Windows product, which has fourteen separate DLC apps | Confirmed | Direct | High | P1, P2 |
| `DRG-002` | The public branch carries build `24903151`, built 2026-08-24 and updated 2026-08-25, while the publisher's most recent named patch announcement is `S06.05.02` dated 2026-08-06 | Observation | Corroborated | Medium | P3, S1 |
| `DRG-003` | A Mining Expedition's primary objective is a Morkite quota of 200 to 400 units, varying with mission length and cavern count | Observation | Corroborated | High | S2 |
| `DRG-004` | Mined Morkite counts toward the quota only once deposited into the mobile depository | Observation | Corroborated | High | S2 |
| `DRG-005` | Completing the primary objective lights the extraction call on the depository; the transport then waits five minutes for this mission type before departing | Observation | Corroborated | High | S2, S3 |
| `DRG-006` | If no player is extracted by the transport, the mission counts as failed | Confirmed | Corroborated | High | S3 |
| `DRG-007` | Five standard hazard levels change enemy damage, resistance, speed, spawn counts, revive health and the reward bonus | Observation | Corroborated | High | S4 |
| `DRG-008` | The pickaxe is available to every class, destroys terrain when swung, and transfers a destroyed deposit's material directly into the player's mineral inventory | Observation | Corroborated | High | S5 |
| `DRG-009` | The Driller's power drills are its traversal tool and are excellent at digging through terrain but cannot mine certain minerals | Observation | Corroborated | High | S6 |
| `DRG-010` | The drone accompanies the player for the entire mission in solo play, mines only what the laser pointer orders it to mine, and automatically engages threats within range | Observation | Corroborated | High | S7 |
| `DRG-011` | The drone holds a limited number of revive charges shown on the interface, restores 40% of maximum health on a revive, and the mission fails if the player is downed with no charges left | Observation | Corroborated | High | S7 |
| `DRG-012` | A resupply costs 80 Nitra from the depository, lands a pod with four racks, and each rack restores 50% of ammunition and half of overall health | Observation | Corroborated | High | S8 |
| `DRG-013` | A resupply cannot be ordered too close to a landed pod, on insufficiently flat terrain, or when the depository holds less than the cost, and a short delay separates consecutive orders | Observation | Corroborated | High | S8 |
| `DRG-014` | Dwarves share a base health and shield value; zero health causes incapacitation that removes equipment use and movement, and a revive restores a hazard-scaled fraction of health | Observation | Corroborated | High | S9 |
| `DRG-015` | The bounded identity is excavation used as the ordinary means of travel, where the same deposited material funds both the objective and the resupply, and the collected quota is worthless unless physically carried out | Strong Pattern | Corroborated | High | `DRG-003`–`DRG-014` |

## Basic data

- Release / origin: Ghost Ship Games; published on Windows by Coffee Stain
  Publishing and released 2020-05-13.
- Platform or physical form: lawfully offered English Windows Steam application
  `548430`; one offline solo `Mining Expedition` at a fixed hazard level on one
  named biome, played as the `Driller`.
- Puzzle family: real-time system pressure; inventory and fixture
  dependencies; world topology and perspective; agent routing and coordination.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=548430&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, the `Action` genre with no Early Access marker, the single-player and
    online co-op categories, `Adjustable Difficulty`, the fourteen DLC apps,
    the sole package and the current Ukraine offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=135552&cc=ua&l=english),
    for package `135552` containing only app `548430`, its Windows-only
    platform support and its current Ukraine offer.
  - **[P3]** [Ghost Ship Games' own `PATCH NOTES - S06.05.02` announcement](https://store.steampowered.com/news/app/548430),
    dated 2026-08-06, for the publisher's most recent named patch. Embedded
    media was not opened or used.
- Corroborating textual sources, accessed 2026-09-06:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/548430),
    for public branch build `24903151` and its timestamps. This mirrors Valve's
    public product data and is treated as a secondary distribution observation,
    not a publisher claim.
  - **[S2]** [official product wiki, Mining Expedition](https://deeprockgalactic.wiki.gg/wiki/Mining_Expedition),
    for the 200-to-400 Morkite quota varying with cavern count, the requirement
    that Morkite be deposited into the depository to count, the optional
    secondary objective and the extraction button that lights on the depository
    after the primary objective completes.
  - **[S3]** [official product wiki, Drop Pod](https://deeprockgalactic.wiki.gg/wiki/Drop_Pod),
    for the retrieval transport being launched by the call, the five-minute
    wait for this mission type, and the statement that if no player is
    successfully extracted the mission counts as failed.
  - **[S4]** [official product wiki, Hazard Level](https://deeprockgalactic.wiki.gg/wiki/Hazard_Level),
    for the five standard levels and the enemy damage, resistance, speed,
    spawn-count, revive-health and reward-bonus changes they apply.
  - **[S5]** [official product wiki, Pickaxe](https://deeprockgalactic.wiki.gg/wiki/Pickaxe),
    for the pickaxe being available to every class, destroying terrain when
    swung, transferring a destroyed deposit's material directly into the
    mineral inventory, and its charged power attack.
  - **[S6]** [official product wiki, Driller](https://deeprockgalactic.wiki.gg/wiki/Driller),
    for the power drills as the class traversal tool, their excellence at
    digging through terrain and their inability to mine certain minerals.
  - **[S7]** [official product wiki, Bosco](https://deeprockgalactic.wiki.gg/wiki/Bosco),
    for the drone accompanying solo players for the entire mission, the
    laser-pointer commands, the requirement that it be ordered to mine rather
    than mining on its own, its automatic engagement of threats in range, its
    limited revive charges shown on the interface, the 40% health restored and
    the mission failure when the player is downed with no charges left.
  - **[S8]** [official product wiki, Resupply Pod](https://deeprockgalactic.wiki.gg/wiki/Resupply_Pod),
    for the 80 Nitra cost, the four racks, each rack restoring 50% of
    ammunition and half of overall health, and the delay, spacing, flat-terrain
    and depository-balance conditions on ordering one.
  - **[S9]** [official product wiki, Health](https://deeprockgalactic.wiki.gg/wiki/Health),
    for the shared base health and shield values, incapacitation at zero
    health with equipment and movement removed, the revive channel and the
    hazard-scaled fraction of health it restores.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S9` under the declared app, package, build, platform,
  input, mission type, hazard level, class, default loadout, solo state,
  exclusions and terminal; rules reasoning, not direct play.
- Claim IDs: `DRG-001`–`DRG-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: advance the controlled dwarf through the cave;
  `ACT-161`: aim and commit a direct attack against a reachable hostile;
  `ACT-341`: address the depository, a resupply rack or the extraction call as
  a reachable authored object and commit its legal interaction.
- Existing `ACT-093`: address the visible quota requirement and irreversibly
  transfer the carried quantity of the accepted mineral into its filled state.
  The Stardew Valley bundle boundary already covers a displayed collection
  requirement filled by irreversible contributions, so no deposit gene was
  created.
- Existing `ACT-130`: spend the deposited balance to execute the priced
  resupply call. `ACT-050`: point at a world target so the target's class
  determines the task the drone begins, exactly as the Pikmin dispatch boundary
  describes. `ACT-218`: start the required extraction call and enter the
  arriving transport's boarding zone before it closes, as the ARC Raiders and
  Helldivers 2 extraction boundary describes.
- New `ACT-443`: carve a continuous volume of reachable terrain, permanently
  opening it as traversable space, and take the material of any deposit the
  same carve removed. `ACT-159` breaks one discrete cell, block or wall;
  `ACT-203` removes bounded ground volume for cover and explicitly excludes
  unlimited voxel mining; `ACT-122` holds an extraction command on a discrete
  resource entity rather than on terrain; and `ACT-245` explicitly excludes
  destroying terrain for a drop. None covers excavation used as the ordinary
  means of travel that also yields the objective material.
- Mineral, biome, class, tool, drone and exact quantity names remain
  parameters. Claims: `DRG-003`–`DRG-013`.

### System Behaviour Genes

- Existing `SYS-215`: the dwarf and the cave's hostiles exchange range-,
  cadence-, damage- and defeat-dependent effects in real time. `SYS-407`: the
  drone persists beside direct control and independently selects legal
  movement, attack or support actions.
- Existing `SYS-116`: each accepted deposit is consumed and retained as filled
  requirement, and filling the declared quota marks the collection complete.
- Existing `SYS-348`: damage passes through the shield and health layers, zero
  health produces the downed state, and a completed revival returns control,
  with knockout when no revival remains. Left 4 Dead 2 already supports this
  boundary without requiring a persistent shield layer.
- New `SYS-810`: an authorised call debits the same deposited pool the
  objective draws on and lands a physical supply object exposing a fixed number
  of separate charges, each restoring a declared fraction of ammunition and
  health. `SYS-715` splits contribution and spending authority across a squad
  and delivers an effect rather than a finite physical object; `SYS-600` emits
  a continuous field from a moving objective; `SYS-788` refills a reserve by
  itself; `SYS-364` restores resources on rest. None couples a physical finite
  supply object to the objective's own deposited material.
- Split-first review of `SYS-810`, required by `BATCH_015_GENE_AUDIT_001`
  finding `A-07`, compared its four clauses against the lower-ID registry.
  `SYS-745` is the closest delivery boundary and is genuinely different: it
  reserves a shared *asset capacity* rather than the resource the objective
  itself consumes, and it excludes entering the delivered vehicle because a
  vehicle is a general-purpose entity whose later use the call does not
  determine. `SYS-454` and `SYS-376` are personal charge pools the character
  carries and a checkpoint or cooldown refills, not a positioned world object
  with a fixed one-shot budget. `SYS-714` answers attrition through
  class-eligible or station sources beside a partial passive-recovery cap, which
  this packet has neither of. `SYS-768` is triggered by crossing a location
  rather than bought. All four are now named in the gene's `Excludes`.
- The gene is retained as one transaction on an atomicity argument stronger than
  co-occurrence. Every term of the second half is fixed by the first: the call
  sets the price, the quantity of charges, the landing position and the fraction
  each charge restores, and no later decision can change any of them. The two
  admitted player authorities are already separate Action genes — `ACT-130`
  spends the balance to execute the priced call and `ACT-341` addresses a rack —
  so the system gene is the single settlement those two commands share, and the
  pod is the materialised form of the purchase rather than an independent
  fixture that happens to hold charges. Splitting here would produce a delivery
  clause that largely restates `SYS-745` and a consumption clause that no
  reviewed gene covers, fragmenting the objective-versus-resupply trade the
  record is about.
- Resolution order: a carve removes terrain volume and transfers any contained
  deposit into inventory; the pointer dispatch gives the drone a task from its
  target's class while the drone also engages threats on its own; a deposit is
  consumed into the quota's filled state; filling the quota marks the collection
  complete and enables the departure call; a resupply call debits the deposited
  pool and lands its racks; damage passes through shield and health into the
  downed state, from which a drone charge or nothing decides continuation; and
  boarding the arriving transport settles the attempt. Claims:
  `DRG-004`–`DRG-014`.

### Constraint Genes

- Existing `CON-140`: the collection declares its accepted mineral identity and
  the quantity required, and completion requires that quota.
- New `CON-609`: with no other player able to revive, the drone's finite,
  visible revive charges gate continuation, and going down with none remaining
  ends the attempt. `SYS-396` and `SYS-644` debit shared team ticket pools;
  `CON-183` spends one life per failed encounter; `ACT-339` uses a carried
  revival item. None makes the attempt's survivability a countable property of
  an autonomous helper.
- Scarce resources: health, shield, ammunition, the deposited balance shared
  between the quota and resupply, the drone's revive charges, the transport's
  waiting interval and carried mineral capacity. Exact values are parameters.
  Claims: `DRG-003`–`DRG-014`.

### Information Genes

- Existing `INF-119`: the interface exposes the dwarf's health, shield,
  ammunition, carried minerals and equipped state. The quota's own disclosure is
  carried inside `ACT-093`, whose boundary requires a visible collection
  requirement with a displayed quantity, and the drone's remaining charges are
  a declared parameter of `CON-609`.
- Exact HUD geometry, icons, colours and interface positions are presentation
  parameters. Claims: `DRG-004`, `DRG-011`, `DRG-012`, `DRG-014`.

### Objective Genes

- New `OBJ-160`: fill the declared quota, which alone enables the departure
  call, then reach and board the arriving transport before its waiting interval
  expires. `OBJ-087` explicitly excludes extraction as a prerequisite for
  mission success, but this product states that if no player is extracted the
  mission counts as failed, so that boundary cannot be reused here.
- Filling the quota without boarding, or boarding after the transport has
  departed, is not success. Claims: `DRG-005`, `DRG-006`, `DRG-015`.

### Time Genes

- Existing `TIM-003`: carving, movement, hostile attacks, the drone's actions,
  the resupply delay and the transport's waiting interval all advance in real
  time while inputs remain accepted.
- Claims: `DRG-005`–`DRG-014`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A solo mission has just begun and the dwarf has left the transport | Accept first ordinary control | The cave begins with default equipment, no seasonal content and the drone present for the whole mission | fixed clean entry | `DRG-010` |
| Solid cave rock blocks the shortest route | Carve it with the pickaxe or the class drills | A continuous volume is removed and stays open as traversable space | excavation as travel | `DRG-008`, `DRG-009` |
| A mineral deposit lies inside the volume being carved | Carve through it | The declared material transfers directly into the mineral inventory by the same action | carve yields material | `DRG-008` |
| A deposit contains a mineral the class drills cannot mine | Use the drills on it | The drills open the terrain but do not yield that mineral, so the pickaxe is required | tool-specific yield | `DRG-009` |
| A deposit is visible and the drone is idle | Point at the deposit | The drone begins mining it, which it does not do unprompted | pointer dispatch by target class | `DRG-010` |
| A hostile approaches while no order is given | Continue working | The drone engages it automatically within range | autonomous engagement | `DRG-010` |
| Mined material is carried and the depository is reachable | Deposit it | The quantity is consumed irreversibly and the visible quota advances by that amount | deposit-gated progress | `DRG-004` |
| Mined material is carried but never deposited | Reach the end of the mission | That material does not count toward the quota | uncounted carry | `DRG-004` |
| The depository holds at least the resupply cost and the ground is flat | Order a resupply | The pool is debited and a pod lands exposing four separate racks | objective-funded resupply | `DRG-012`, `DRG-013` |
| A resupply rack is reachable | Take one | Ammunition and health are each restored by their declared fraction and that rack is consumed | finite charges | `DRG-012` |
| The depository holds less than the resupply cost | Order a resupply | The order is refused | shared pool competition | `DRG-013` |
| Damage reduces health to zero while the drone holds a charge | Wait for the drone | One charge is consumed and control returns with a hazard-scaled fraction of health | recoverable downing | `DRG-011`, `DRG-014` |
| Damage reduces health to zero while the drone holds no charge | Continue | The attempt ends immediately | companion-gated continuation | `DRG-011` |
| The declared quota is filled | Press the extraction call | The transport is launched and begins its declared waiting interval | quota-gated departure | `DRG-005` |
| The transport has landed and is waiting | Board it before the interval expires | The attempt settles as a success | positive terminal | `DRG-006`, `DRG-015` |
| The transport's waiting interval expires with nobody aboard | Continue | The mission counts as failed despite the filled quota | extraction is a prerequisite | `DRG-006` |

## Strategic and experiential structure

- Planning horizon: the visible quota, the deposited balance, remaining
  ammunition and the drone's charges decide whether to keep carving deeper,
  return to deposit, spend the pool on a resupply or call the departure.
- Local tactics: carve straight lines toward known deposits rather than
  following the natural cave, keep a return tunnel open so the depository stays
  reachable, spend the pointer on the deposits that are furthest out of reach,
  and treat each resupply as material subtracted from the objective.
- Medium-term structure: the cave rewards excavating away from its authored
  geometry, so the route the player carves becomes the map they must retreat
  through when the departure call starts its clock.
- Reversible versus irreversible: carved volume, deposits and the deposited
  balance never come back; movement and pointer orders are freely changed; a
  downing is recoverable only while the drone holds a charge.
- Failure attribution: the visible health, shield, ammunition, deposited
  balance and drone charges make a loss traceable to a specific overspend, an
  unreachable retreat route or a departure called too late.
- Player trust: the quota states its requirement, the resupply states its cost
  against the same balance, the drone's remaining charges are displayed before
  the risk is taken, and the transport's waiting interval is declared.

## Replay and variation

- What changes: the generated cave layout, where deposits fall, how much
  terrain is carved rather than walked, how many resupplies are bought, how many
  downings occur and how much time the departure leaves.
- Randomness or procedural generation: the cave system, its cavern count and
  the placement of deposits and hostiles are generated per mission within the
  declared mission parameters; the quota range, hazard effects, resupply cost
  and waiting interval are authored.
- Multiple strategies: the mission admits carving directly to deposits,
  following the natural caverns, or banking the pool for a late resupply. The
  control demonstrates one carved shortcut, one pointer-mined deposit, one
  resupply and one drone revive rather than making a no-resupply or no-downing
  route the terminal.
- Typical replay motive: fill the same quota with less material spent on
  resupply, or leave a shorter retreat to the transport.

## Adjacent systems and history

- Once Human shares direct first-person traversal, aimed attacks, contextual
  world-object interaction, a personal resource display and real-time combat.
  Its world is persistent and its resources are gathered from discrete sources;
  this packet makes excavation itself the means of travel and settles a single
  bounded mission by carrying the collected material out.
- DOOM (2016) shares the same six-gene action-combat backbone but keeps its
  level geometry fixed, has no collection quota and no extraction requirement.
- Helldivers 2 shares the extraction call and boarding boundary, but its
  mission success is owned by the main objective alone, with extraction only a
  separable departure bonus, which is exactly the distinction that forced a new
  objective gene here.
- Stardew Valley shares the collection-slot boundary reused for the quota, but
  its bundles persist across visits in a safe hub rather than gating a single
  timed departure.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-050`, `ACT-093`, `ACT-130`, `ACT-161`, `ACT-218`, `ACT-341`, `ACT-443` | class, tool, mineral, drone and biome names are parameters |
| System Behaviour | `SYS-116`, `SYS-215`, `SYS-348`, `SYS-407`, `SYS-810` | quota sizes, charge counts, restored fractions and hazard scaling are parameters |
| Constraint | `CON-140`, `CON-609` | accepted identity, required quantity and charge count are parameters |
| Information | `INF-119` | HUD geometry and icons are parameters |
| Objective | `OBJ-160` | quota, waiting interval and boarding zone are parameters |
| Time | `TIM-003` | carve rate, spawn cadence and interval length are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `265` (`GAME-0001`–`GAME-0265`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`6 / 26 = 0.230769`).
- Supported combination subsets: `COMB-0264`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `INF-119`, `TIM-003` | Both advance a directly controlled first-person character through a hostile world, commit aimed attacks, interact with reachable authored objects, expose the character's personal resources and resolve everything in real time. Once Human gathers from discrete world sources inside a persistent shared world that keeps its geometry. This packet makes carving continuous terrain the ordinary means of travel and the same act that yields the objective material, spends the deposited objective material on its own resupply, delegates mining and combat to a drone whose finite revive charges are the only thing standing between a downing and failure, and settles only when the collected quota is physically carried onto a departing transport. | Near, `0.230769` |

### Preserved research notes

- New genes: `ACT-443`, `SYS-810`, `CON-609`, `OBJ-160`.
- Reused genes: `ACT-008`, `ACT-050`, `ACT-093`, `ACT-130`, `ACT-161`,
  `ACT-218`, `ACT-341`, `SYS-116`, `SYS-215`, `SYS-348`, `SYS-407`, `CON-140`,
  `INF-119`, `TIM-003`.
- Classification result: `New gene`.
- Lower-ID scan: reuse `ACT-093` with `SYS-116` and `CON-140` for the deposited
  quota rather than creating a deposit gene, because the Stardew Valley
  collection boundary already covers a visible requirement filled by
  irreversible contributions; reuse `ACT-050` for the pointer dispatch, because
  the Pikmin boundary already makes the target's class determine the follower's
  task; reuse `ACT-218` for the extraction call and boarding; reuse `SYS-348`
  for shield, health, downed and revival, which Left 4 Dead 2 already supports
  without a shield layer; reuse `ACT-130` for the priced resupply call and
  `ACT-341` for the rack, depository and call interactions. Reject `ACT-159`,
  `ACT-203`, `ACT-122` and `ACT-245` for excavation, each on a stated boundary.
  Reject `OBJ-087`, which excludes extraction as a prerequisite for success.
  Reject `SYS-715`, `SYS-600`, `SYS-788` and `SYS-364` for the resupply.
  Reject a mineral-, class-, drone-, biome- or mission-named gene.

## Taxonomy impact

- Registry changes recorded by `BATCH_015_GENE_AUDIT_001` finding `A-07`:
  `SYS-810` is retained after a split-first review and gains four named
  exclusions — `SYS-745`, `SYS-454`/`SYS-376`, `SYS-714` and `SYS-768` — that
  state boundaries it always had. Its definition, lifecycle, this signature and
  `COMB-0264` are unchanged, so this is a boundary clarification rather than a
  taxonomy decision.
- Registry changes: add `ACT-443`, `SYS-810`, `CON-609`, `OBJ-160` and
  `COMB-0264`, plus independent evidence for fourteen reused genes.
- Taxonomy-change record: none; no split, merge, deprecation, lifecycle change,
  wording generalisation or earlier signature change. Every reused gene is used
  inside its existing boundary and its definition is unchanged.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, mission,
  mineral, class, drone, biome, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official product data, the
  publisher's own announcement and the official product wiki support this
  packet.
- The publisher's most recent named patch and the public branch update differ
  by nineteen days. Rather than assert a single semantic version, the record
  states both dates and treats the build identifier as secondary. This repeats
  the pattern recorded for `GAME-0265` and is now a batch-level observation
  about live-service products rather than a one-off.
- The optional secondary-objective resource is excluded because the declared
  route does not collect it and its collection changes only the reward, not the
  completion predicate.
- Cooperative play is excluded rather than treated as a variant, because it
  removes the drone entirely and replaces the revive rule that produces this
  packet's negative terminal. It is named as a potential scoped module.
- Carried mineral capacity was considered and not admitted: the sources
  establish that mined material enters a mineral inventory but do not establish
  a capacity limit binding inside this route. This is a recorded uncertainty,
  not a claim that no limit exists.
- Filling the quota without boarding the transport is not the terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] `DRG-001`–`DRG-015`: one bounded solo
  expedition makes excavation the ordinary means of travel, funds its own
  resupply out of the objective's deposited material, and completes only when
  the filled quota is physically carried onto a departing transport.

## New genes

- [Observation | Corroborated | High] `ACT-443`, `SYS-810`, `CON-609`,
  `OBJ-160` — terrain carving that also yields the objective material, the
  objective-funded finite supply drop, the companion revive charges that gate
  continuation, and the quota-then-board objective.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0264` — excavated travel whose
  deposited yield funds both the objective and the resupply that reaches it.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Does a cooperative session reuse this signature with the companion constraint
  replaced by a player revive, or does removing the drone change the objective
  and resupply boundaries as well?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0267` — Kerbal Space Program.
- Optimisation criterion: keep the constructed-solution corridor but replace
  excavated traversal with staged vehicle assembly resolved by continuous
  orbital physics.
- Expected information gain: separate assembly and staging from the carving and
  extraction boundaries admitted here.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection admitted this product to test
  whether fully destructible traversal is a distinct action boundary from
  placing or removing discrete blocks. The completed scan answers that
  directly: `ACT-159`, `ACT-203`, `ACT-122` and `ACT-245` each exclude it on a
  stated boundary, so one new action gene was required while fourteen other
  genes were reused unchanged.
