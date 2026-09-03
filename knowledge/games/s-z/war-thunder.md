---
game_id: GAME-0184
slug: war-thunder
game_title: War Thunder
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0182
gene_ids:
  action:
    - ACT-161
    - ACT-290
    - ACT-330
  system:
    - SYS-320
    - SYS-395
    - SYS-580
    - SYS-581
    - SYS-582
    - SYS-583
  constraint:
    - CON-262
    - CON-348
    - CON-488
    - CON-489
  information:
    - INF-115
    - INF-116
    - INF-237
    - INF-238
  objective:
    - OBJ-108
  time:
    - TIM-003
---

# Game: War Thunder

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Windows PC stable public client patch `2.57.1.111`, Steam
  public build `24927764`, reviewed 2026-08-29; English-language ordinary PvP
  Ground Arcade Battles, one `Domination` mission, with a match-locked USA Rank
  I BR `1.0` lineup of M2A4, LVT(A)(1) and M2A2 and no backups.
- Primary decision loop: select one eligible lineup vehicle; directly steer and
  position its hull and gun; read spotted-target markers, distance and the
  provisional penetration indicator; choose ammunition, aim and fire; let
  ballistics resolve against armour, crew and modules; capture or contest one
  of three points; after vehicle loss select another eligible lineup member;
  then repeat while vehicle destruction and point majority drain team tickets.
- Entry and exit: begins at the first ground-vehicle selection screen of the
  ordinary Domination match. It succeeds when the opposing tickets reach zero
  or the opposing team has no players able to spawn ground vehicles, and fails
  when either terminal applies first to the allied team; the result screen is
  the reproducible exit.
- Included: the declared three-vehicle USA lineup; up to three distinct ground
  spawns without backups; simplified Arcade mobility; direct driving, turret
  aim and ammunition fire; ballistic travel, armour penetration, ricochet,
  crew and module damage; partial module function under Arcade rules; local
  sight and sound; shared spotted-target markers, minimap and distance; impact
  and penetration assistance; reload and ammunition capacity; three capture
  points, contest, ownership, vehicle-loss ticket debit, majority-proportional
  ticket drain and both team terminals.
- Excluded: temporary fighter, attacker or bomber events even if airstrike
  points are earned; every Air and Naval mode; Ground Realistic, Simulator and
  Assault; `Conquest`, `Battle`, custom missions and events; backups; other
  nations, higher ranks, helicopters, guided weapons and nuclear aircraft;
  research, modifications, crew training, Battle Pass, currencies, repair
  economy, matchmaking optimisation and post-match account progression.
- Potential scoped modules: one Ground Realistic spawn-point match; a single
  aircraft ruleset; Naval Arcade; a higher-rank guided-weapon packet; or the
  hangar research and modification economy.
- Direct-play status: not conducted. The current official changelog, official
  game and vehicle documentation and official Arcade rules establish the build,
  lineup, marker, spawn, damage, point, ticket and terminal transitions. The
  repository trace below is evidence-based rules reconstruction, not a claimed
  captured live match.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WT-001` | Patch 2.57.1.111 is the current stable official client boundary and Steam public build 24927764 is the reproducible PC package | Confirmed | Corroborated | High | P1, P2, S1 |
| `WT-002` | The scoped USA lineup consists of M2A4, LVT(A)(1) and M2A2 at Rank I / Arcade BR 1.0 | Confirmed | Direct | High | P5–P7 |
| `WT-003` | Ground Arcade simplifies vehicle handling and permits at most three ground-vehicle spawns | Confirmed | Direct | High | P3 |
| `WT-004` | Spotted enemies receive world/minimap markers with identity and distance, while the gunner predicts impact and armour-penetration chance | Confirmed | Direct | High | P3, P9 |
| `WT-005` | Ground-vehicle fire resolves through finite ammunition, armour geometry and spatial crew/module damage rather than one target health bar | Confirmed | Direct | High | P4–P7 |
| `WT-006` | Arcade-damaged engine, gun and other modules retain reduced functionality instead of becoming wholly unusable at the first terminal damage state | Confirmed | Direct | High | P3, P4 |
| `WT-007` | Domination uses three contestable capture points and point majority drains opposing tickets proportionally to the ownership difference | Confirmed | Direct | High | P3, P9 |
| `WT-008` | Destroying enemy ground vehicles also drains tickets, and zero tickets or no players able to spawn ground vehicles loses the match | Confirmed | Direct | High | P3 |
| `WT-009` | Without backups, a naturally destroyed used vehicle gives way to another not-yet-spawned eligible lineup vehicle until the three-ground-spawn scope is exhausted | Observation | Corroborated | High | P3, P8 |
| `WT-010` | The bounded decisions couple armour-angle forecast, internal damage, three-point control and a short heterogeneous vehicle-life budget | Observation | Corroborated | High | P3–P9, V1 |

## Basic data

- Release / origin: developed and published by Gaijin Entertainment; the
  official current product title is **War Thunder**.
- Platform or physical form: networked real-time combined-arms game; this
  record admits only the current Windows PC Ground Arcade rules declared above.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; agent routing and coordination.
- Primary and official sources:
  - **[P1]** [official Update 2.57.1.111 notes](https://warthunder.com/en/game/changelog/current/1889),
    for the newest stable patch identifier and date; its Naval-only changes do
    not alter the scoped ground rules.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/236390/War_Thunder/),
    for the maintained product title, developer/publisher and Windows package.
  - **[P3]** [official War Thunder Wiki — Arcade Battles](https://wiki.warthunder.com/gamemode/arcade_battles),
    for simplified ground handling, markers, aim assistance, partial module
    function, three ground spawns, three-point Domination, ticket effects and
    terminal conditions.
  - **[P4]** [official War Thunder Wiki — ground vehicle modules](https://wiki.warthunder.com/mechanics/4775-ground-vehicle-modules),
    for spatial ammunition, crew, aiming, engine and other functional damage.
  - **[P5]** [official War Thunder Wiki — M2A4](https://wiki.warthunder.com/unit/us_m2a4),
    for Rank I / AB BR 1.0 reserve status, four crew, armour, mobility, 37 mm M5
    gun, ammunition and reload boundaries.
  - **[P6]** [official War Thunder Wiki — LVT(A)(1)](https://wiki.warthunder.com/unit/us_lvt_a_1),
    for Rank I / AB BR 1.0 beginner status, six crew, armour, amphibious
    mobility and 37 mm M6 armament.
  - **[P7]** [official War Thunder Wiki — M2A2](https://wiki.warthunder.com/unit/us_m2a2),
    for Rank I / AB BR 1.0 status, four crew, twin-turret geometry and finite
    heavy/light machine-gun ammunition.
  - **[P8]** [official War Thunder Wiki — Crew Lock](https://wiki.warthunder.com/mechanics/183-crew-lock),
    for not-yet-spawned lineup eligibility, naturally destroyed used vehicles
    and the separate backup exception.
  - **[P9]** [official CDK reference](https://wiki.warthunder.com/cdk/7439-cdk-reference),
    for shipped ground-capture instructions, ticket/zone interface text and the
    uncontested-presence capture boundary.
- Secondary build metadata:
  - **[S1]** [SteamDB depots for app 236390](https://steamdb.info/app/236390/depots/),
    used only to pin public Build ID `24927764`; it is not treated as a rules
    authority.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P9` under the declared lineup and exclusions; rules reasoning, not a
  direct-play claim.
- Claim IDs: `WT-001`–`WT-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate, reverse and brake the
  currently assigned ground vehicle without an enter/exit world-vehicle loop.
- Existing `ACT-161`: aim the current turret weapon at a reachable hostile and
  commit a shot; the later armour and internal result remains systemic.
- New `ACT-330`: choose one eligible M2A4, LVT(A)(1) or M2A2 from the locked
  lineup for the next ground sortie.
- Parameters: vehicle, hull orientation, throttle, steering, gun traverse,
  elevation, ammunition type, target point, lineup eligibility and spawn.
- Claim IDs: `WT-003`–`WT-005`, `WT-009`, `WT-010`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the active vehicle's simplified Arcade motion,
  terrain contact and broad vehicle-damage envelope.
- Existing `SYS-395`: convert eligible ground-vehicle presence inside a point
  into capture, contest and team ownership.
- New `SYS-580`: resolve each fired round through ballistic path, impact angle,
  armour layers and spatial internal crew/modules.
- New `SYS-581`: translate crew/module damage into Arcade partial function and
  vehicle loss.
- New `SYS-582`: after loss, consume one ground spawn and return the player to
  another eligible lineup selection while capacity remains.
- New `SYS-583`: debit tickets for ground-vehicle destruction, apply
  point-majority drain proportional to the three-point ownership difference and
  settle either team terminal.
- Resolution order: accept vehicle and gun inputs; integrate hull and turret
  motion; release a loaded round; resolve ballistic impact and internal damage;
  update partial functions or vehicle loss; update point occupancy/ownership;
  apply loss and majority ticket effects; then either settle the match or offer
  another legal lineup vehicle.
- Parameters: motion, projectile, armour, crew/module damage, point occupancy,
  lineup state, tickets, drain cadence and result.
- Claim IDs: `WT-003`, `WT-005`–`WT-010`.

### Constraint Genes

- Existing `CON-262`: each vehicle carries finite ammunition and each weapon
  obeys its compatible ammunition inventory.
- Existing `CON-348`: point progress requires eligible uncontested team
  presence inside the authored capture area.
- New `CON-488`: a shot requires remaining ammunition, completed reload and a
  legal gun/line solution; the penetration colour is not a guarantee.
- New `CON-489`: Ground Arcade permits at most three scoped ground spawns and,
  with backups excluded, does not re-offer a used lineup vehicle.
- Scarce strategic resources: team tickets, three point owners, remaining
  lineup spawns, vehicle crew and modules, ammunition, reload time, viable armour
  angle, cover, sightline and safe capture-zone occupancy.
- Claim IDs: `WT-003`–`WT-009`.

### Information Genes

- Existing `INF-115`: local sight and sound expose only the currently perceived
  armour, movement, firing and impact context; off-screen threats remain hidden.
- Existing `INF-116`: the shared HUD exposes allied/enemy tickets, point
  ownership, capture/contest state and match result phase.
- New `INF-237`: world/minimap target markers, identity, distance, predicted
  impact and red/yellow/green penetration chance expose a provisional solution.
- New `INF-238`: ammunition, reload and active crew/module damage expose the
  current vehicle's remaining combat authority.
- Claim IDs: `WT-004`–`WT-010`.

### Objective Genes

- New `OBJ-108`: exhaust the opposing Ground Domination team by zeroing its
  tickets or eliminating all remaining player ground-spawn capacity before the
  allied team reaches either state.
- Success, evaluation and failure: the result is shared by the team; personal
  kills, captures, research and currency matter only where the admitted rules
  convert them into point ownership, tickets or remaining spawn capacity.
- Claim IDs: `WT-007`–`WT-010`.

### Time Genes

- Existing `TIM-003`: vehicles, projectiles, reloads, damage, point occupancy
  and ticket drain advance in real time while players act; a post-loss lineup
  screen temporarily removes direct vehicle control but does not turn the match
  into discrete turns.
- Claim IDs: `WT-003`–`WT-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First ground selection screen, all three USA BR 1.0 vehicles unused | Select M2A4 and one ground spawn | M2A4 enters direct control and one of at most three ground spawns becomes consumed | lineup choice creates the current combat body | `WT-002`, `WT-003`, `WT-009` |
| M2A4 is live with a loaded 37 mm round | Steer and traverse the gun toward a marked enemy | Hull and turret change orientation continuously while target distance and provisional penetration colour update | driving, gun geometry and information are coupled but distinct | `WT-003`–`WT-005` |
| Aim aid is green on one visible armour point | Fire once | Dispersion, impact angle and armour still resolve; green does not guarantee penetration or internal damage | interface forecast does not replace ballistics | `WT-004`, `WT-005` |
| A round penetrates the target's outer armour | Give no further input during impact | The surviving projectile path affects only contacted crew, ammunition or modules and may leave other functions intact | damage is spatially decomposed | `WT-005`, `WT-006` |
| Active vehicle has a damaged engine or gun but has not met the loss predicate | Continue moving or aiming | Arcade retains reduced module functionality rather than converting every severe module hit into total loss | impairment precedes terminal destruction | `WT-006` |
| Neutral point contains only eligible allied ground vehicles | Remain inside its outlined area | Capture progresses to allied ownership; an enemy entering contests and blocks completion | point control arises from spatial occupancy | `WT-007` |
| Allied team owns two points and enemy owns one | Maintain that majority | Opposing tickets drain repeatedly at the lower proportional rate than a three-to-zero majority | ownership difference controls shared pressure | `WT-007` |
| Enemy ground vehicle is destroyed | Complete the damaging transition | Enemy tickets are debited independently of current point-majority drain | tactical destruction and territorial pressure share a terminal resource | `WT-008` |
| M2A4 is lost and LVT(A)(1) and M2A2 remain unused | Select LVT(A)(1) | Lost M2A4 stays ineligible without a backup; LVT(A)(1) becomes the next direct-control body | heterogeneous bounded respawn rather than revival | `WT-009` |
| All three scoped ground spawns are consumed | Attempt no further ground selection | No scoped lineup vehicle remains; if the team has no other players able to spawn, it loses even with positive tickets | spawn-capacity exhaustion is an alternate terminal | `WT-003`, `WT-008`, `WT-009` |
| Opposing tickets reach zero first | Give no further action | Domination resolves as allied victory and opens the result screen; the inverse state is defeat | one reproducible shared-resource terminal | `WT-008` |

## Strategic and experiential structure

- Local decision: expose hull or turret for a shot, angle armour, reposition
  through cover, select an armour point, trust or discount the penetration aid,
  remain in a point, retreat with impaired modules or spend the current vehicle
  to deny an enemy capture.
- Medium-term planning: choose the next lineup vehicle for the map and point
  state; preserve the two cannon-armed vehicles for armoured targets; use the
  M2A2's mobility and machine gun only where its lower penetration remains
  useful; rotate before an enemy majority converts into sustained ticket loss.
- Long-term structure: preserve enough distributed vehicle lives to keep
  contesting while converting penetrations and point majority into faster
  opposing ticket exhaustion than the allied team's own losses.
- Common heuristics: shoot flatter or thinner armour; avoid exposing ammunition
  and crew; use markers as forecasts rather than certainty; repair or withdraw
  when a damaged mechanism makes a second shot unlikely; break point majority
  before chasing a low-value kill.
- Failure attribution: markers, penetration colour, hit feedback, internal
  damage panel, point owners and ticket pools expose much of the local chain;
  dispersion, unobserved enemies, teammate spawn capacity and simultaneous
  team pressure keep causal attribution incomplete.
- Player-trust factors: visible distance and predicted impact support learning,
  spatial damage explains many non-lethal hits and ticket/point state is shared;
  the aid's approximate penetration colour must not be mistaken for a promise.
- Claim IDs: `WT-004`–`WT-010`.

## Replay and variation

- What changes between sessions: authored Domination map, spawn side, human
  lineups, movement, selected vehicle order, visible armour angles, shot results,
  point owners, ticket trajectory and whether all three personal spawns are used.
- Randomness or procedural generation: maps and vehicles are authored;
  matchmaking and human simultaneous decisions create most variation, with
  weapon dispersion and ballistic outcomes adding bounded uncertainty.
- Multiple viable strategies: early point rush, covered overwatch, flank for
  thinner armour, deliberate contest, vehicle preservation or aggressive
  ticket trades can pursue the same team terminal.
- Typical replay motive: improve armour recognition, shot placement, vehicle
  ordering, point rotation and coordination under changing opposing lineups.
- Claim IDs: `WT-003`–`WT-010`.

## Adjacent systems and history

- Direct predecessors: no historical client rules are imported; current patch
  `2.57.1.111` is the full version boundary.
- Variants: Realistic removes Arcade markers and changes module/spawn handling;
  Simulator changes optics and allowable lineups; Air and Naval replace the
  directly controlled bodies and combat geometry.
- Similar games: Battlefield 6 shares real-time vehicle control, contested
  capture areas, team tickets and territory pressure; PUBG shares occupied
  vehicle motion and spatial part/occupant damage; Rocket League shares a
  dedicated directly controlled vehicle but not armoured combat.
- Important differences: War Thunder's ordinary Ground Arcade match selects a
  short sequence of distinct pre-match vehicles, forecasts a specific armour
  point, resolves internal crew/module geometry and combines vehicle-loss debit
  with proportional three-point-majority drain.
- Claim IDs: `WT-001`–`WT-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-161`, `ACT-290`, `ACT-330` | driving, aim, fire and lineup vehicle |
| System Behaviour | `SYS-320`, `SYS-395`, `SYS-580`–`SYS-583` | motion, ballistics, internal damage, respawn, points and tickets |
| Constraint | `CON-262`, `CON-348`, `CON-488`, `CON-489` | ammunition, uncontested capture, shot legality and three spawns |
| Information | `INF-115`, `INF-116`, `INF-237`, `INF-238` | marker, minimap, aim aid, tickets and damage panel |
| Objective | `OBJ-108` | zero tickets or no spawnable players |
| Time | `TIM-003` | continuous battle and ticket-drain cadence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `183` (`GAME-0001`–`GAME-0183`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`8 / 46 = 0.173913`).
- Supported combination subsets: `COMB-0182`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0149` — Battlefield 6 | `ACT-161`, `SYS-320`, `SYS-395`, `CON-262`, `CON-348`, `INF-115`, `INF-116`, `TIM-003` | Both combine direct vehicle combat, contested control areas, ammunition, partial opponent knowledge and shared ticket state under live pressure. War Thunder removes infantry classes, downing/revival, squad deployment, destructible cover and one-ticket infantry death, replacing them with a three-vehicle personal lineup, armour-point assistance, spatial crew/module damage, proportional three-point majority drain and a no-spawnable-players terminal | Near, `0.173913` |

### Preserved research notes

- New genes: `ACT-330`, `SYS-580`–`SYS-583`, `CON-488`, `CON-489`,
  `INF-237`, `INF-238` and `OBJ-108`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: nine generic direct-control, damage, capture,
  ammunition, team-state, partial-information and real-time boundaries fit
  without change; ten new records isolate the lineup, armour forecast, internal
  damage and Ground Domination terminal distinctions.

## Combination status

- `COMB-0182` is a verified strict sixteen-gene subset of the nineteen-gene
  genome, coupling a selected
  ground vehicle, armour-directed fire, internal functional damage, contested
  three-point ownership, bounded lineup replacement and shared ticket terminal.
- Every earlier verified combination is tested deterministically after
  registration.

## Taxonomy impact

- Registry changes: ten new Active genes, links on nine reused genes,
  `COMB-0182` and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or reviewed game
  signature changes.
- Candidate terms affected: lineup vehicle spawn, armour-path damage, Arcade
  partial module function, bounded heterogeneous respawn, proportional
  Domination tickets, assisted ballistic legality and internal vehicle HUD.

## Negative results

- `ACT-201` is not reused because the player does not enter or leave an already
  embodied world vehicle; each sortie begins by assigning a selected lineup
  vehicle.
- `ACT-291` is not reused because it excludes changing vehicles inside a locked
  event and models an owned free-roam collection rather than expendable match
  lives.
- `SYS-396` and `OBJ-079` are not reused because Battlefield Conquest couples
  unrevived infantry deaths to point-count drain, while this scope couples
  destroyed ground vehicles to proportional three-point majority and an
  alternate no-spawnable-players terminal.
- `CON-347` is not reused because War Thunder chooses an eligible vehicle from
  a match-locked lineup, not a spatial headquarters, squad, beacon or vehicle
  seat after a deployment timer.
- Temporary aircraft are not admitted merely because Ground Arcade can award
  airstrike points; taking one would cross the declared ground-only body and
  action boundary.
