---
game_id: GAME-0200
slug: delta-force
game_title: Delta Force
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0198
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
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-320
    - SYS-380
    - SYS-382
    - SYS-394
    - SYS-395
    - SYS-643
    - SYS-644
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-288
    - CON-346
    - CON-347
    - CON-348
    - CON-524
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-150
    - INF-155
  objective:
    - OBJ-123
  time:
    - TIM-003
---

# Game: Delta Force

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: unmodified Windows PC live client through Steam, public
  build `24584641`, observed current on `2026-08-31` during Season 10
  `Meltdown`; ordinary unranked Warfare playlist `A/D - Coliseum`, defender
  side; Luna (`Recon`) with the legal current base `QBZ-95` primary after all
  optional attachment slots are cleared, standard sidearm and melee slots,
  Luna's Compound Bow equipment and the Recon Respawn Beacon; one match from
  deployment map to the declared result.
- Primary decision loop: read the active sector, objectives, attacker troop
  force, remaining time, squad/deployment network, visible or marked opponents,
  ammunition, health and equipment readiness; choose a legal deployment source;
  move, aim, fire, reload, throw equipment, place a beacon, revive, communicate
  or operate an available vehicle; let live damage, marks, capture presence and
  committed deaths resolve; hold the current objectives or fall back after a
  completed sector until attacker troop force reaches zero before the final
  sector is secured.
- Entry and exit: select the current `A/D - Coliseum` Warfare card and accept
  matchmaking. The accepted trace begins at defender deployment with Luna and
  the declared loadout visible. If matchmaking assigns the attacking side,
  leave before deployment and requeue rather than merge both objectives. The
  trace ends at the first explicit `Victory` or `Defeat` result: defender
  success occurs when attacker troop force reaches zero; defender failure
  occurs when attackers complete the final sector first.
- Reproducible parameterisation: choose Luna whenever her Recon slot is free;
  otherwise requeue. Select the already-available current QBZ-95, remove every
  optional attachment and cosmetic, retain the ordinary sidearm, melee,
  Compound Bow and Respawn Beacon slots, and deploy from the first legal
  headquarters source shown in UI order. Player identities, aim values,
  vehicle use, objective route, exact duration and intermediate sector count
  are parameters. Weapon acquisition history is an entry predicate, not part of
  the game state under analysis.
- Included: operator and role selection; one legal bounded Warfare loadout;
  direct infantry movement, aimed fire, reload, grenade/equipment use and team
  cues; Luna's detection/Volt-arrow effects; local sight and sound; squad state;
  downing, teammate revive, committed death and timed redeployment; headquarters,
  squad and beacon deployment sources; vehicle entry and operation when an
  ordinary Coliseum vehicle is available; active objective occupancy, contest
  and capture; ordered sector completion, defender fallback, attacker troop-
  force debit/replenishment, time pressure and the result screen.
- Excluded: Operations extraction, gear tiers, stash, auction, loot and Black
  Site; Black Hawk Down campaign; King of the Hill, Victory Unite, Team
  Deathmatch, Ranked, events, custom rooms and other Warfare maps; account,
  weapon, season, badge and Battle Pass progression; paid gear, appearances and
  collaboration content; weapon-unlock unions, tuning alternatives and every
  operator or primary other than the fixed Luna/QBZ-95 packet; anti-cheat,
  matchmaking quality and post-match currencies or rewards.
- Potential scoped modules: attacker-side Coliseum with final-sector capture;
  one ordinary King of the Hill match; one Operations extraction; one vehicle-
  first Warfare packet; one auxiliary-objective trace. Each changes the resource
  or terminal boundary and requires a separate current packet.
- Direct-play status: not conducted. Current official PC/console patch and map
  material establishes the live season, Coliseum, A/D changes and Luna's legal
  weapon/equipment boundary. The official Warfare guide establishes side,
  objective, revive, ticket, replenishment and terminal rules. A current
  unmodified 4K PC recording inspected `2026-08-31` fixes defender entry as
  Luna, the deployment surface, active objectives, attacker-ticket exhaustion,
  explicit `Victory` and result transition. The reconstruction is evidence-
  based rules reasoning, not a claim of authenticated play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DF-001` | Steam public build `24584641` is the current Windows package and Season 10 Meltdown remains the official live content boundary | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| `DF-002` | Coliseum is a current Warfare Attack and Defend map whose ordinary A/D objective geometry received current mid-season adjustments | Confirmed | Direct | High | P1, P2 |
| `DF-003` | Attackers must capture every objective before finite troop force is exhausted, while defenders have unlimited redeployment and win by holding until attacker exhaustion | Confirmed | Direct | High | P4 |
| `DF-004` | Capturing a sector replenishes attacker troop force and advances play to the next objective set | Confirmed | Direct | High | P4, P5 |
| `DF-005` | Downed players may be revived before committed death; defender deaths do not debit a symmetric troop-force pool | Confirmed | Corroborated | High | P4, S2 |
| `DF-006` | Luna is a Recon operator whose Compound Bow supplies Detection and Volt arrows; QBZ-95 is in Luna's current legal Warfare weapon pool | Confirmed | Direct | High | P6, P7 |
| `DF-007` | Current Warfare admits role loadouts, squad/team cues, legal redeployment sources, Respawn Beacons, call-ins and combined infantry/vehicle combat | Confirmed | Corroborated | High | P4, P8 |
| `DF-008` | The current PC trace starts from defender deployment as Luna and ends in explicit Victory after the attacking side fails before final-sector completion | Observation | Direct | High | S2 |
| `DF-009` | Operations, Black Hawk Down and progression are separable from this one ordinary Warfare A/D result | Confirmed | Direct | High | P3, P8 |

## Basic data

- Release / origin: Team Jade / TiMi Studio Group and Level Infinite; global PC
  release 2024, maintained as a cross-platform live service.
- Platform or physical form: networked first-person shooter on Windows through
  Steam; console/mobile versions are not used as the build authority.
- Puzzle family: operator-bound squad combat, combined-arms spatial control and
  asymmetric resource defence across an advancing real-time front.
- Primary and official sources:
  - `P1` — [official Meltdown patch notes](https://deltaforce.garena.com/en/news/all/2MX7J4),
    for the 2026-06-30 season boundary, Coliseum and current A/D mechanics.
  - `P2` — [official mid-season update](https://deltaforce.garena.com/en/news/all/JQTVNF),
    for the live 2026-07-30 Coliseum B/D objective, route and vehicle changes.
  - `P3` — [official current Delta Force product page](https://deltaforce.garena.com/),
    for Warfare, Operations and Black Hawk Down as separable product modes and
    current PC availability.
  - `P4` — [official Warfare guide](https://deltaforce.garena.vn/news/chien-truong/huong-dan-chien-truong),
    for Attack and Defend sides, capture, revive/redeploy, finite attacker troop
    force, replenishment, unlimited defender redeployment and both terminals.
  - `P5` — [official Warfare optimisations](https://deltaforce.garena.com/en/news/announcement/F2MA9T),
    for ordinary A/D's 200-ticket starting boundary and current-class combat
    adjustments; the numeric value remains a parameter rather than a gene.
  - `P6` — [official World of Ahsarah operator record](https://www.playdeltaforce.com/act/wikimap/),
    for Luna's Recon identity, Detection Arrow and Volt Arrow.
  - `P7` — [official Eclipse Vigil patch notes](https://deltaforce.garena.com/en/news/announcement/M3DB35),
    for QBZ-95 in Luna's Warfare weapon pool and current arrow/mark behaviour.
  - `P8` — [official Delta Force channel Warfare guide](https://www.youtube.com/watch?v=iIybTgng22M),
    for large-scale squad, objective and combined-arms Warfare presentation.
- Secondary and reproducible sources:
  - `S1` — [Steam public-depot record](https://steamdb.info/app/2507950/depots/),
    observed `2026-08-31`, for Windows public build `24584641`, published
    2026-08-06, only.
  - `S2` — [current unmodified Coliseum A/D PC recording](https://www.youtube.com/watch?v=D3IRcqrdX48),
    published 2026-08-25 and inspected `2026-08-31`, for defender-side Luna,
    deployment, objectives, ticket terminal, `Victory` and result screen.
- Claim IDs: `DF-001`–`DF-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move, sprint, crouch, jump and position Luna.
- Existing `ACT-161`: aim and fire the selected primary, sidearm, vehicle weapon
  or damaging operator equipment at a legal target.
- Existing `ACT-164`: switch among carried weapon, sidearm, melee and equipment
  slots; `ACT-183`: reload the current firearm.
- Existing `ACT-184`: throw the legal tactical grenade/equipment item;
  `ACT-187`: ping or send an ordinary squad/team cue.
- Existing `ACT-190`: activate or place Luna/Recon equipment, including arrow
  mode and Respawn Beacon, at a legal target or surface.
- Existing `ACT-201`: enter an available vehicle seat, operate its movement or
  weapon and leave it.
- Existing `ACT-215`: configure the bounded Luna/QBZ-95 role-compatible loadout
  before deployment.
- Existing `ACT-240`: choose a ready headquarters, squad or beacon deployment
  source and redeploy; `ACT-241`: revive one eligible downed teammate.
- Parameters: stance, aim, weapon slot, equipment charge, arrow, beacon, vehicle
  and source. Claim IDs: `DF-005`–`DF-008`.

### System Behaviour Genes

- Existing `SYS-208`, `SYS-215` and `SYS-292`: resolve aimed attacks, live
  hostile combat and typed thrown trajectories/effects.
- Existing `SYS-320`: resolve directly operated vehicle motion, collision,
  damage and seat weapons; existing `SYS-380`: resolve Luna's typed Detection
  Arrow, Volt Arrow and Respawn Beacon effects under their current readiness.
- Existing `SYS-382` and `SYS-394`: after downing, permit revival before
  committed death, then time legal redeployment and apply the side-specific
  ticket consequence.
- Existing `SYS-395`: eligible uncontested presence converts an active A/D
  objective through capture progress into ownership; opposing presence contests.
- New `SYS-643`: owning every objective in the active sector closes that front,
  moves the combat boundary and exposes the next sector.
- New `SYS-644`: committed attacker deaths debit finite troop force, sector
  completion replenishes it, defender redeployment remains unlimited, and
  attacker zero/final-sector completion settle opposite results.
- Resolution order: live damage can down a soldier; a revive restores control,
  otherwise death commits and the applicable attacker ticket debit occurs;
  legal redeployment restores combat authority; objective presence updates
  capture/contest; a complete objective set advances the sector and replenishes
  attackers; zero attacker troop force or final-sector completion settles.
- Parameters: damage, mark, capture rate, revive window, respawn delay, sector,
  replenishment and result. Claim IDs: `DF-002`–`DF-008`.

### Constraint Genes

- Existing `CON-262`: magazines, ammunition, grenades and equipment charges are
  finite within a life; existing `CON-269`: operator equipment obeys target,
  charge, placement and cooldown legality.
- Existing `CON-272`: a dead soldier has no direct combat authority before a
  legal redeployment; existing `CON-288`: vehicle entry and operation require a
  compatible seat, state and geometry.
- Existing `CON-346`: weapon and equipment slots must remain legal for Luna's
  Recon class; existing `CON-347`: redeployment requires a ready legal team
  source; existing `CON-348`: objective progress requires uncontested eligible
  presence.
- New `CON-524`: capture, deployment and combat-area legality are limited to the
  active A/D sector; a completed sector forces defender fallback before the next
  objectives become contestable.
- Scarce strategic resources: attacker troop force, living squadmates, safe
  deployment sources, capture time, ammunition, equipment readiness, beacon
  durability, vehicle availability and defensible space.
- Claim IDs: `DF-003`–`DF-008`.

### Information Genes

- Existing `INF-073`: current weapon, ammunition and equipment slots are visible;
  `INF-115`: local sight and sound expose only partial enemy state.
- Existing `INF-116`: HUD exposes team, active objectives, capture/contest,
  sector, attacker troop force, timer and result pressure.
- Existing `INF-119`: health, downed state, equipment readiness and current
  personal role state are visible.
- Existing `INF-150`: operator selection exposes Luna's Recon role, kit and
  allied occupancy before confirmation.
- Existing `INF-155`: deployment map exposes current objectives, squad members,
  beacons, vehicles and source legality.
- Claim IDs: `DF-002`–`DF-008`.

### Objective Genes

- New `OBJ-123`: on the fixed defender side, prevent attackers from completing
  every ordered sector until attacker troop force reaches zero and `Victory`
  is declared. Final-sector completion first is `Defeat`; personal kills or
  points matter only through objective survival and shared attrition.
- Claim IDs: `DF-003`, `DF-004`, `DF-008`.

### Time Genes

- Existing `TIM-003`: movement, fire, down/revive windows, equipment readiness,
  vehicle state, capture progress, sector time and ticket loss continue in real
  time while every participant acts.
- Claim IDs: `DF-002`–`DF-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Defender deployment exposes Luna, legal sources and the cleared QBZ-95 loadout | Select the first legal headquarters source and deploy | Luna enters the active Coliseum sector with the fixed slots | entry fixes role, loadout, side and front | `DF-006`–`DF-008` |
| Detection Arrow is ready and a surface lies in its legal trajectory | Fire the arrow across an approach | the typed arrow emits its detection effect and eligible dynamic targets become team-readable | information is produced by operator equipment | `DF-006` |
| A teammate is downed inside the revive window | Reach and complete revive | the teammate returns without committing a death or any attacker-side ticket effect | downing and death are separate states | `DF-005` |
| A downed attacker is not revived | Allow the window to expire or the player gives up | death commits, attacker troop force drops and redeployment begins | only one side spends the shared finite pool | `DF-003`, `DF-005` |
| Both sides occupy objective A | Continue contesting | capture does not complete until opposing eligible presence clears | eliminations matter through spatial occupancy | `DF-003` |
| Attackers own every objective in the current sector | Stop contesting after the final capture | the sector closes, attackers receive replenishment and the legal front advances | capture changes both map legality and ticket state | `DF-004` |
| A former defender position lies behind the new fallback boundary | Remain after sector completion | warning/closed-front rules remove it as a legal defence or deployment area | old geometry is no longer an open Conquest point | `DF-004` |
| Attacker troop force reaches zero before final-sector completion | No further input is required | the match declares defender `Victory` and opens result presentation | bounded defender terminal is reproducible | `DF-003`, `DF-008` |
| Attackers complete the final sector with troop force remaining | No further input is required | the match declares defender `Defeat` | opposite terminal uses the same front state | `DF-003`, `DF-004` |

## Strategic and experiential structure

- Local decision: hold cover for a shot, expose to revive, spend an arrow,
  place a beacon, enter a vehicle, contest the objective or preserve a fallback.
- Medium-term planning: distribute Recon information and spawn access across
  squad lanes, trade space for attacker tickets, protect objectives that jointly
  gate the sector and avoid losing the beacon network during fallback.
- Long-term structure: make every completed attacker life cost more time and
  troop force than each captured sector replenishes, then stop the front before
  the final sector.
- Failure attribution: objective and troop-force state are explicit, while
  partial information, many simultaneous players and vehicles limit individual
  causal certainty.
- Claim IDs: `DF-003`–`DF-008`.

## Replay and variation

- Player/operator composition, spawn network, vehicle allocation, objective
  route, revive timing and sector attrition vary; Coliseum geometry, side,
  objective order, legal loadout boundary and result predicates remain fixed.
- Human simultaneous choice, aim dispersion and partial information create the
  meaningful variation; no procedural map generation is admitted.
- Viable plans include layered objective defence, beacon-enabled flanks,
  vehicle-backed denial, concentrated revives and deliberate fallback.
- Claim IDs: `DF-002`–`DF-008`.

## Adjacent systems and history

- Battlefield 6 is closest mechanically through squad loadouts, revival,
  deployment sources, vehicles, contested points and tickets, but Conquest
  leaves points open and debits symmetric pools.
- Overwatch shares hero-bound kits, team communication, contested ownership and
  respawn but scores symmetric Control rounds without vehicles or attacker-only
  tickets.
- War Thunder shares combined arms, objective capture and ticket pressure but
  substitutes match-locked vehicle lineups for operator kits and revival.
- Operations extraction and Black Hawk Down contain recognizable weapons and
  characters but have incompatible resources, authority and terminals.
- Claim IDs: `DF-002`–`DF-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241` | infantry, loadout, equipment, vehicle, deployment and revive actions |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-394`, `SYS-395`, `SYS-643`, `SYS-644` | live combat, capture, sector advancement and asymmetric ticket settlement |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`, `CON-347`, `CON-348`, `CON-524` | capacity, class/source legality, contest and active-front bounds |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-150`, `INF-155` | equipment, partial enemies, operator, team objective and deployment state |
| Objective | `OBJ-123` | defend until attacker troop force reaches zero |
| Time | `TIM-003` | continuous squad combat and capture pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `199` (`GAME-0001`–`GAME-0199`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`32 / 40 = 0.800000`).
- Supported combination subsets: `COMB-0198`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Battlefield 6 (`GAME-0149`) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-394`, `SYS-395`, `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`, `CON-347`, `CON-348`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155`, `TIM-003` | Both coordinate role loadouts, squad revival, deployment sources, vehicles and contested points. Battlefield Conquest keeps the whole map open and converts deaths plus held points into two symmetric ticket pools; Delta Force closes ordered sectors and replenishes only the finite attacker pool while defenders redeploy without a matching debit. | Near, `0.800000` |

### Preserved research notes

- New genes: `SYS-643`, `SYS-644`, `CON-524`, `OBJ-123`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: Battlefield 6, Overwatch and War Thunder cover the
  reusable live combat, role, deployment, vehicle, revive, capture and ticket
  corridor. New records isolate only the ordered-front transition, one-sided
  replenishable ticket settlement, active-sector legality and exact defender
  terminal.

## Taxonomy impact

- Registry changes: four new Active definitions; new Delta Force support for
  thirty-three existing records. No earlier game signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: Attack and Defend, Coliseum, troop force, sector,
  fallback, defender redeployment, Respawn Beacon, Detection Arrow and Volt Arrow.

## Negative results

- `SYS-396` is rejected because its own boundary excludes attacker-only tickets
  that replenish after sectors; using it would erase the defining asymmetry.
- Overwatch Control round/overtime settlement is rejected because Coliseum uses
  one advancing front and one match result, not first-to-two symmetric rounds.
- War Thunder lineup-loss and no-spawn terminal genes are rejected because the
  fixed player is an operator with ordinary revive/redeployment, not a finite
  three-vehicle lineup.
- Operations extraction, gear tiers, loot, account progression and call-in
  reward optimisation are excluded parameters, not latent genes in this unit.
