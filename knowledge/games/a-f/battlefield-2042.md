---
game_id: GAME-0234
slug: battlefield-2042
game_title: Battlefield 2042
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0232
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-187
    - ACT-190
    - ACT-201
    - ACT-215
    - ACT-240
    - ACT-241
    - ACT-403
    - ACT-404
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-320
    - SYS-380
    - SYS-382
    - SYS-386
    - SYS-394
    - SYS-395
    - SYS-742
    - SYS-743
    - SYS-744
    - SYS-745
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-288
    - CON-346
    - CON-347
    - CON-348
    - CON-574
    - CON-575
    - CON-576
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-155
    - INF-283
    - INF-284
    - INF-285
  objective:
    - OBJ-079
  time:
    - TIM-003
---

# Game: Battlefield 2042

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current ordinary Windows Steam product, app `1517290`,
  official Update `9.2.1` deployed 2025-09-09 and Steam public Build ID
  `19798118`, checked 2026-09-03. The bounded packet is one fresh official
  All-Out Warfare Conquest match on the reworked `Orbital` map, in the ordinary
  up-to-128-participant PC ruleset with matchmaking-priority human players and
  permitted server-fill AI. It is not Solo/Co-op or a Portal experience.
- Reproducible match parameters: Windows/Steam; current public branch; standard
  multiplayer Conquest; reworked Orbital; the first fresh round start reached
  through the official playlist; whichever US or Russian side matchmaking
  assigns; `Falck` in the current Support class; one currently legal unmodified
  primary weapon, sidearm, Support gadget and throwable; ordinary squad and
  vehicle availability. If Orbital is not the assigned map or the round has
  already begun, it is not the bounded attempt.
- Entry: begins on the first deployment surface of that fresh Orbital round,
  before the first controlled spawn. Inspect the two reinforcement pools,
  grouped sectors, included control points, squad sources, Falck loadout and
  available vehicles, then select one legal headquarters deployment.
- Primary decision loop: deploy; move through authored cover; aim, fire,
  reload, throw a grenade, communicate and use Support healing, resupply or
  revival; use the Plus surface to replace one available compatible attachment
  when range or pressure changes; enter, operate or repair an available
  vehicle; capture or contest individual points; treat a captured point as a
  foothold while pursuing every point required for its sector; rotate to create
  and preserve sector majority; after a committed death choose a legal
  redeployment source; when shared capacity, cooldown and ground position
  allow, request one ordinary ground vehicle and use it after delivery.
- Terminal: the first ordinary End of Round result caused by either team's
  finite reinforcement pool reaching zero. Success is an allied victory;
  failure is an allied defeat. A kill, captured point, completed sector,
  attachment swap, vehicle delivery, personal score, ribbon, unlock or level is
  intermediate and cannot settle the packet.
- Included: four-person squad structure; current Specialist-to-class mapping;
  Falck's fixed specialty/trait plus Support equipment boundary; infantry
  movement, firearm handling, grenades, gadgets and partial sight/sound;
  downing, squad or Support revival, committed defeat and redeployment; direct
  ground and air vehicle operation when naturally available; one ground-vehicle
  call-in; the Plus attachment surface; point capture and contest; point-to-
  sector aggregation; majority-sector ticket pressure; limited destructible
  cover; ordinary real-time weather only as sampled non-required match state.
- Excluded: Breakthrough, Rush, Team Deathmatch and every other playlist;
  Portal, custom or persistent servers and altered rules; Hazard Zone;
  Solo/Co-op and an AI-only practice packet; Featured Experiences, limited-time
  events and Community Calendar rotations; maps other than Orbital; Battle Pass,
  Road to Battlefield 6 Pass, weekly missions, ribbons, mastery, unlock quests,
  cosmetics, Playercards, Store, account XP and post-match rewards; Phantom;
  campaign/lore, all prior seasons and the complete live-service history;
  console rules, cross-progression, matchmaking quality and anti-cheat.
- Potential scoped modules: another map, player-count platform, class,
  Specialist, mode, Portal rules packet, event, Solo/Co-op session or progression
  route needs its own build, entry, terminal and exclusions.
- Direct-play status: no authenticated live match was played. Current official
  update, product, mode, class, Plus, vehicle, sector, ticket and map material
  was inspected and combined into a repository-side transition trace. No video
  or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BF2042-001` | Update 9.2.1 and Steam public Build 19798118 are the reviewed current Windows boundary | Confirmed | Corroborated | High | P1, P2, S1 |
| `BF2042-002` | App 1517290 is the released Windows online product and All-Out Warfare keeps Conquest distinct from Portal and Hazard Zone | Confirmed | Direct | High | P2, P3 |
| `BF2042-003` | Conquest uses two teams, point capture, grouped sectors and finite shared reinforcements with a zero-pool match result | Confirmed | Corroborated | High | P3–P6 |
| `BF2042-004` | A team gains complete control of a sector only while it owns every included control point, although one captured point can remain a foothold | Confirmed | Direct | High | P5, P6 |
| `BF2042-005` | Committed combatant defeats and sustained majority-sector control reduce the corresponding reinforcement pool | Confirmed | Corroborated | High | P4, P5 |
| `BF2042-006` | Current Specialists sit inside Assault, Engineer, Recon and Support equipment roles while primary weapons remain unrestricted | Confirmed | Direct | High | P7 |
| `BF2042-007` | Squad revival, Support-wide revival and redeployment make downing distinct from a committed return cycle | Confirmed | Corroborated | High | P6–P8 |
| `BF2042-008` | The Plus surface replaces an available compatible sight, barrel, ammunition or underbarrel option during live control | Confirmed | Direct | High | P6, P9 |
| `BF2042-009` | Any Specialist can request an available ground vehicle at a chosen legal location, subject to map/mode, shared team budget and personal cooldown | Confirmed | Direct | High | P6, P10 |
| `BF2042-010` | Reworked Orbital remains an official Battlefield 2042 map with its changed Conquest headquarters, additional point and denser routes/cover | Confirmed | Corroborated | High | P11, P12 |
| `BF2042-011` | Multiplayer may use AI only to fill server vacancies while human players retain matchmaking priority; Solo/Co-op is a distinct excluded ruleset | Confirmed | Direct | High | P6 |
| `BF2042-012` | The repository trace reproduces deployment, live attachment replacement, vehicle delivery, point/sector aggregation, revival, ticket pressure and both zero-ticket outcomes | Observation | Direct | High | V1 |

## Basic data

- Release / origin: DICE developed and Electronic Arts published Battlefield
  2042; the Windows product released 2021-11-19 and remains available as an
  online live-service shooter.
- Platform or physical form: online Windows Steam first-person combined-arms
  shooter; one current official large-team Conquest match.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; world topology and vehicle physics.
- Primary and official sources:
  - **[P1]** [official Update 9.2.1 notes](https://www.ea.com/games/battlefield/battlefield-2042/news/battlefield-2042-update-notes-9-2-1),
    for the 2025-09-09 current update boundary and the excluded live-service
    material shipped beside it.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/1517290/Battlefield_2042/),
    for app identity, Windows availability, release, developer/publisher,
    online requirements and the current Conquest/Portal product distinction.
  - **[P3]** [official current modes page](https://www.ea.com/games/battlefield/battlefield-2042/features/all-modes),
    for Conquest inside All-Out Warfare, the up-to-128-participant boundary and
    separation from Breakthrough, Portal and Hazard Zone.
  - **[P4]** [official ticket guide](https://www.ea.com/sv/games/battlefield/battlefield-2042/tips-and-tricks-hub/how-tickets-work),
    for finite team reinforcements, combatant defeats, majority-sector bleed
    and the zero-pool result.
  - **[P5]** [official sector guide](https://www.ea.com/sv/games/battlefield/battlefield-2042/tips-and-tricks-hub/how-to-capture-sectors),
    for points grouped into sectors, all-point ownership, majority pressure and
    match victory.
  - **[P6]** [official reveal-question briefing](https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-briefing-answering-your-reveal-questions),
    for Specialist loadouts, squad revival, four-person squads, Conquest
    clustering/sectors, footholds, call-in budgets/cooldowns, deployment-screen
    aircraft and multiplayer server-fill AI.
  - **[P7]** [official Update 3.2.0 class notes](https://www.ea.com/games/battlefield/battlefield-2042/news/battlefield-2042-update-notes-3-2-0),
    for the retained current four-class structure, Specialist assignments,
    class equipment and unrestricted primary weapons.
  - **[P8]** [official Update 3 notes](https://www.ea.com/games/battlefield/battlefield-2042/news/battlefield-2042-update-notes-3),
    for visible downed/reviver state and the revival channel.
  - **[P9]** [official Plus guide](https://www.ea.com/de/games/battlefield/battlefield-2042/tips-and-tricks-hub/how-plus-system-works),
    for live category selection and immediate attachment replacement.
  - **[P10]** [official call-in guide](https://www.ea.com/sv/games/battlefield/battlefield-2042/tips-and-tricks-hub/call-in-system),
    for tablet selection, vehicle choice, delivery targeting and confirmation.
  - **[P11]** [official map hub](https://www.ea.com/en/games/battlefield/battlefield-2042/maps-hub/battlefield-2042-maps-hub),
    for Orbital's retained current map identity.
  - **[P12]** [official Update 2.2 Orbital notes](https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-2042-update-notes-2-2),
    for the reworked Conquest headquarters, new point, traversal routes, cover
    and terrain boundary used by the current map.
- Secondary source:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/1517290/depots/), for
    public Build `19798118`, its 2025-08-30 build timestamp and 2025-09-09
    public-branch update timestamp.
- Reproducible control: **[V1]** repository-side state trace derived from
  `P1`–`P12` and `S1` under the fixed client, mode, map, fresh-round entry and
  zero-ticket terminal; it is rules reasoning, not a direct-play claim.
- Claim IDs: `BF2042-001`–`BF2042-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`, direct soldier movement; `ACT-161`, aimed firearm,
  melee or launcher attack; `ACT-164`, switch carried weapon or gadget;
  `ACT-183`, reload; `ACT-184`, throw a tactical grenade; `ACT-187`, send a
  squad/team cue; `ACT-190`, activate a typed Specialist or class gadget;
  `ACT-201`, enter, operate and leave an available vehicle; `ACT-215`, configure
  one legal class/Specialist deployment loadout; `ACT-240`, select a legal
  deployment source; `ACT-241`, revive one eligible downed ally.
- New `ACT-403`: replace one currently available compatible attachment through
  the live Plus surface. New `ACT-404`: select one available support vehicle
  and one legal world delivery position through the call-in tablet.
- Parameters: side, squad, Specialist, class, weapon, attachment categories,
  gadget, grenade, communication channel, deployment source, vehicle, seat,
  support option and delivery target.
- Claim IDs: `BF2042-006`–`BF2042-009`, `BF2042-012`.

### System Behaviour Genes

- Existing `SYS-208`, resolve aimed fire through range, cover and hit region;
  `SYS-215`, live hostile combat; `SYS-292`, grenade trajectory and typed
  field; `SYS-320`, occupied vehicle motion and damage; `SYS-380`, typed
  ability/gadget effect; `SYS-382`, timed return after knockout; `SYS-386`,
  destruction of eligible cover; `SYS-394`, downing, revival and committed
  ticketed death; `SYS-395`, point occupancy, contest and ownership.
- New `SYS-742`: group points into complete sector ownership while preserving
  point footholds. New `SYS-743`: combine committed defeats and majority-sector
  pressure into shared ticket loss and zero-ticket settlement. New `SYS-744`:
  apply the chosen live attachment to current weapon behaviour. New `SYS-745`:
  reserve shared vehicle capacity and deliver the requested operable entity.
- Resolution order: sample live input; resolve movement, combat, gadget,
  vehicle or attachment state; update downing and revival; commit unresolved
  defeats; convert eligible point occupancy into ownership; aggregate every
  sector's required points; evaluate sector majority; debit the corresponding
  reinforcement pool; if either pool reaches zero, settle End of Round.
- Claim IDs: `BF2042-003`–`BF2042-010`, `BF2042-012`.

### Constraint Genes

- Existing `CON-262`, magazine, reserve, gadget and grenade capacity;
  `CON-269`, gadget target, charge and cooldown legality; `CON-272`, no direct
  body control after committed death; `CON-288`, vehicle seat, motion and
  geometry legality; `CON-346`, current class/Specialist equipment boundary;
  `CON-347`, elapsed redeployment and legal source; `CON-348`, uncontested
  eligible presence for capture progress.
- New `CON-574`: a live attachment must be an available compatible option in
  the selected current-weapon category. New `CON-575`: vehicle delivery needs
  admitted map/mode, shared availability, elapsed requester cooldown and legal
  target geometry. New `CON-576`: sector ownership requires every included
  control point rather than only one foothold.
- Scarce strategic resources: team reinforcements, living squad state, revive
  time, safe deployment sources, point/sector control, vehicle capacity and
  health, ammunition, gadget charges, attachment options, cooldowns and cover.
- Claim IDs: `BF2042-003`–`BF2042-009`.

### Information Genes

- Existing `INF-073`, current weapon, ammunition and gadget state; `INF-115`,
  partial hostile information through local perception; `INF-116`, allied
  radar, squad and broad objective state; `INF-119`, personal health, class,
  status and readiness; `INF-155`, deployment-map objectives and legal sources.
- New `INF-283`: live Plus categories, current attachments and available
  alternatives. New `INF-284`: call-in options, availability, cooldown and
  delivery-position legality. New `INF-285`: points grouped into sectors,
  complete ownership, both ticket pools and majority pressure.
- Claim IDs: `BF2042-003`–`BF2042-009`, `BF2042-012`.

### Objective Genes

- Existing `OBJ-079`: deplete the opposing finite Conquest reinforcement pool
  before the allied pool reaches zero. Battlefield 2042 parameterises the
  territorial contribution through complete sectors and sector majority rather
  than Battlefield 6's flat per-point drain.
- Claim IDs: `BF2042-003`–`BF2042-005`, `BF2042-012`.

### Time Genes

- Existing `TIM-003`: movement, combat, downing, revival, capture, vehicle
  delivery, weather sampling and ticket pressure advance in real time while
  human and server-fill participants act.
- Claim IDs: `BF2042-003`–`BF2042-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Orbital deployment surface; Falck fixed | Select one legal Support loadout and headquarters source | Falck enters with her fixed specialty/trait, class equipment and chosen unrestricted weapon set | Specialist identity and class equipment jointly bound deployment | `BF2042-006` |
| Held weapon exposes several available Plus options | Open the Plus surface, select one compatible category option and release the command | The option replaces that category immediately and its weapon effects become current | attachment adaptation occurs inside the live life | `BF2042-008` |
| Neutral or enemy point contains only eligible allied presence | Remain inside its capture area | Progress neutralises and then transfers that point to the allied team | local occupancy changes one tactical foothold | `BF2042-003`, `BF2042-004` |
| One point in a multi-point sector is allied but another is not | Preserve the foothold and attack the remaining point | The first point can remain a spawn foothold, but the sector stays incomplete | point ownership and sector ownership are distinct | `BF2042-004` |
| Allied team owns every point in that sector | Clear the final contest and complete capture | The aggregate sector changes to allied control | all-member aggregation creates the strategic unit | `BF2042-004` |
| Allied side controls a majority of sectors | Maintain the complete sector set | Opposing reinforcements repeatedly decline while committed allied defeats still debit the allied pool | sector majority converts map control into shared pressure | `BF2042-005` |
| Falck reaches an eligible downed ally before the revive opportunity closes | Complete the Support revive | Ally returns to live control and avoids the corresponding committed return cycle | revival preserves team presence and tickets | `BF2042-007` |
| Downed state closes without revival | Commit the death and select a legal deployment source | The defeat debit applies and the player returns only after the redeployment gate | downing, committed defeat and return are separate | `BF2042-005`, `BF2042-007` |
| Call-in surface offers a ground vehicle; team capacity and cooldown are ready | Select the vehicle and a legal nearby position, then confirm | Capacity is reserved, the vehicle is delivered and becomes an operable world entity | shared match support is spatially player-requested | `BF2042-009` |
| Same request while capacity is full, cooldown active or target illegal | Confirm the unavailable request | The interface rejects delivery and no vehicle enters world state | call-in is not an unlimited summon | `BF2042-009` |
| Opposing reinforcement pool reaches zero | No further input required | Server presents allied End of Round victory; the inverse zero state is defeat | one finite team predicate closes the packet | `BF2042-003`, `BF2042-005`, `BF2042-012` |

## Strategic and experiential structure

- Local decision: choose exposure, shot, grenade, gadget, revive, attachment,
  vehicle seat or delivery position while threats and support remain partial.
- Medium-term planning: preserve safe squad/point spawns, complete every point
  in a chosen sector, adapt a weapon without surrendering live position, and
  spend scarce vehicle capacity where it can change the sector network.
- Long-term structure: hold enough complete sectors that majority pressure and
  avoided committed deaths reduce the opposing ticket pool first.
- Common heuristics: revive before giving up a ticket; treat one flag as a
  foothold rather than a finished sector; switch the current weapon only to the
  attachment the next engagement needs; call a ground vehicle onto clear usable
  terrain; rotate when sector majority changes.
- Failure attribution: attachment, target-legality, cooldown, point, sector and
  ticket surfaces separate most immediate failures; remote fights, sampled
  teammates and server-fill participants make exact global causation partial.
- Player-trust factors: explicit point/sector/ticket and request feedback makes
  the central transitions auditable; network quality and team balance remain
  outside the packet.
- Claim IDs: `BF2042-003`–`BF2042-009`.

## Replay and variation

- What changes between sessions: assigned side, human/AI fill, squad
  composition, Specialist choices, weapons, point routes, local destruction,
  vehicle availability, call-in timing and weather occurrence.
- Randomness or procedural generation: Orbital geometry and sector membership
  are authored; matchmaking, participant choice, weapon dispersion, weather
  timing and concurrent combat create bounded variation.
- Multiple viable strategies: infantry concentration can complete one sector;
  dispersed squads can protect footholds; vehicles can cross the long map;
  Support sustain can preserve tickets; live attachment changes can trade close
  pressure for range without a redeploy.
- Typical replay motive: improve sector rotation, squad sustain, attachment
  timing and fleet allocation under a different live opposition.
- Claim IDs: `BF2042-003`–`BF2042-011`.

## Adjacent systems and history

- Direct predecessors: Battlefield V uses flat capture points, Fortifications
  and squad-leader Reinforcement points; Battlefield 6 returns to flat
  per-objective ticket drain and adds its own class/Training Path packet.
- Variants: Solo/Co-op, Portal, Hazard Zone, events, other maps, console player
  counts and other standard modes materially change participants, rules,
  geometry or terminal and are separate.
- Similar games: Battlefield 6 and Battlefield V share squads, firearms,
  vehicles, revival, point control and finite team tickets. World of Tanks and
  War Thunder share direct vehicle operation, while Overwatch and Marvel Rivals
  share role-composed live team combat.
- Important differences: this Conquest packet nests points inside all-owned
  sectors, applies continuing pressure from sector majority, permits weapon
  attachment replacement during a life and allows any eligible Specialist to
  request a shared-capacity ground vehicle at a chosen world location.
- Claim IDs: `BF2042-003`–`BF2042-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`, `ACT-403`, `ACT-404` | soldier, squad, loadout, attachment and call-in commands |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-386`, `SYS-394`, `SYS-395`, `SYS-742`, `SYS-743`, `SYS-744`, `SYS-745` | combat, vehicles, point/sector/ticket aggregation and live deliveries |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`, `CON-347`, `CON-348`, `CON-574`, `CON-575`, `CON-576` | equipment, redeployment, capture, attachment, delivery and sector gates |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155`, `INF-283`, `INF-284`, `INF-285` | local combat, deployment, Plus, call-in, sector and ticket state |
| Objective | `OBJ-079` | opposing reinforcement pool reaches zero first |
| Time | `TIM-003` | continuously advancing match |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `233` (`GAME-0001`–`GAME-0233`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`34 / 47 = 0.723404`).
- Supported combination subsets: `COMB-0232`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0149` — Battlefield 6 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-386`, `SYS-394`, `SYS-395`, `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`, `CON-347`, `CON-348`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155`, `OBJ-079`, `TIM-003` | Both combine squad infantry/vehicle combat, class-bound support, point capture, revival, redeployment and finite team reinforcements. Battlefield 6 drains through each held point and fixes a different class/Training Path, deployment and destruction packet. Battlefield 2042 instead aggregates every point into all-owned sectors, drains through sector majority, changes current attachments through Plus and creates player-positioned vehicle deliveries from shared team capacity. | Near, `0.723404` |

### Preserved research notes

- New genes: `ACT-403`, `ACT-404`, `SYS-742`, `SYS-743`, `SYS-744`,
  `SYS-745`, `CON-574`, `CON-575`, `CON-576`, `INF-283`, `INF-284`, `INF-285`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`,
  `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`,
  `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`,
  `SYS-386`, `SYS-394`, `SYS-395`, `CON-262`, `CON-269`, `CON-272`,
  `CON-288`, `CON-346`, `CON-347`, `CON-348`, `INF-073`, `INF-115`,
  `INF-116`, `INF-119`, `INF-155`, `OBJ-079` and `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: established movement, combat, squads, classes,
  vehicles, revival, point capture and real-time state retain their portable
  boundaries. New records isolate the two-level sector aggregation, its
  distinct ticket calculation, live attachment mutation and shared-capacity
  player-positioned vehicle delivery without naming Orbital, Falck or a weapon.

## Taxonomy impact

- Registry changes: twelve new Active genes. No earlier reviewed signature or
  lifecycle state changes.
- Portable labels: each new label describes an attachment, support-vehicle,
  point/sector, capacity or information transition. Orbital, Falck, concrete
  vehicles, attachment names, player count, key bindings and ticket values
  remain game-scoped parameters.
- Taxonomy-change record: none.
- Candidate terms affected: live attachment swap, grouped sector, sector
  majority, vehicle call-in, shared vehicle capacity and delivery position.

## Negative results

- Existing `SYS-396` is rejected: it encodes continuous drain for each held
  control point, whereas this packet first resolves all-point sectors and then
  checks sector majority.
- Existing `SYS-318` is rejected: it couples attachments with regional armour
  durability and does not describe a live replacement action.
- Battlefield V `ACT-389`, `SYS-715`, `CON-561` and `INF-275` are rejected:
  ordinary 2042 vehicle call-ins do not spend earned squad points and do not
  require squad-leader authority.
- Portal, Hazard Zone, Solo/Co-op, events, passes, unlocks and the service
  history are excluded rather than unioned into Conquest.
