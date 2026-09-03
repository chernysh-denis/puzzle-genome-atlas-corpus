---
game_id: GAME-0225
slug: star-wars-squadrons
game_title: "STAR WARS: Squadrons"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0223
gene_ids:
  action:
    - ACT-161
    - ACT-392
    - ACT-393
    - ACT-394
    - ACT-395
    - ACT-396
  system:
    - SYS-215
    - SYS-723
    - SYS-724
    - SYS-725
    - SYS-726
    - SYS-727
    - SYS-728
  constraint:
    - CON-269
    - CON-282
    - CON-565
  information:
    - INF-115
    - INF-125
    - INF-268
    - INF-277
  objective:
    - OBJ-141
  time:
    - TIM-003
---

# Game: STAR WARS: Squadrons

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official Windows PC Standard Edition, Steam public
  build `8101433`, checked 2026-09-02; the latest published client notes are
  Update `4.2` dated 2021-01-19. The current EA and Steam product surfaces plus
  the public build record form the reproducible version packet.
- Reproducible platform and settings: Steam app `1222730`; Windows; English;
  non-VR; keyboard and mouse; first-person cockpit; Standard Pilot Experience
  instruments; difficulty `Pilot`; Story mode. If Mission 1 or its fixed X-wing
  packet is materially revised, this record requires review rather than silent
  substitution.
- Primary decision loop: read the current objective, target, cockpit resources
  and incoming-threat warning; throttle, pitch, yaw and roll toward the required
  encounter; select a target; fire lasers or a locked Concussion Missile; route
  power among engines, lasers and shields; focus shield charge front or rear;
  time a countermeasure against an incoming missile; request repair/resupply
  from Gunny when needed; clear the current predicate and repeat.
- Entry and exit: begins at the first controllable T-65B X-wing cockpit state
  after the Mission 1 briefing and take-off in `Form the Vanguard`. It succeeds
  only after the required final Imperial formation is destroyed, the mission
  debrief is reached and the unconditional `Mission Complete` medal is retained.
- Included: the fixed Mission 1 X-wing; Standard Laser Cannon, Repair Droid,
  Concussion Missile, Seeker Warheads, Standard Hull, Standard Deflector and
  Standard Engine; direct spaceflight and collision; laser and missile combat;
  cockpit targeting; shared engine/laser/shield power; front/rear shield focus;
  incoming-missile warning and countermeasure; AI-wingmate repair/resupply;
  authored objective order; debrief and guaranteed completion medal.
- Reproducible parameterisation: start a fresh Story Mission 1 on `Pilot` with
  its fixed loadout and default Standard instruments; use keyboard/mouse and
  remain non-VR. Exact route, target order inside a wave, power allocation,
  shield facing, resupply timing and combat damage may vary.
- Excluded: both prologues; Mission 2 and the rest of Story; Dogfight, Fleet
  Battles, Custom Matches, Training and AI Fleet Battles; multiplayer, ranks,
  Operations and rewards; component or cosmetic customisation; every other ship
  and faction; controller, HOTAS and VR; optional performance medals; later
  drift, subsystem-targeting and ship-selection lessons; server-balance history
  and the whole product history.
- Potential scoped modules: one named Fleet Battles ruleset, one fixed Dogfight
  map, one later story mission or one VR/control-method study each requires its
  own mode, version, entry, decision loop and terminal.
- Direct-play status: no authenticated client or mission was played. Official EA
  product, manual, settings, gameplay and release-note pages establish the live
  control vocabulary and bounded mechanics; official GDC material establishes
  Mission 1's instructional corridor. Repository reasoning does not claim
  personal play. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SWSQ-001` | EA and Steam currently present the Windows product as `STAR WARS™: Squadrons`; public Steam build is `8101433` | Confirmed | Direct | High | P1, P2, S1 |
| `SWSQ-002` | Story is a first-person single-player starfighter experience distinct from multiplayer modes | Confirmed | Direct | High | P1, P3 |
| `SWSQ-003` | Keyboard/mouse directly controls throttle, pitch, yaw and roll, weapons, targeting, countermeasures, shield focus and power allocation | Confirmed | Direct | High | P4 |
| `SWSQ-004` | The fixed Mission 1 craft is a shielded T-65B X-wing and the mission teaches missiles, power, shields and targeting | Confirmed | Direct | High | P3, P6, S2 |
| `SWSQ-005` | Live power can be shifted among engines, lasers and shields, changing subsystem performance | Confirmed | Direct | High | P3, P4 |
| `SWSQ-006` | Shield charge can be focused front or rear independently of power allocation | Confirmed | Direct | High | P3, P4 |
| `SWSQ-007` | Cockpit targeting supports guided missile locks, incoming threats and finite countermeasure response | Confirmed | Direct | High | P3, P4 |
| `SWSQ-008` | Single-player exposes a request-resupply command for AI wingmates, used by the Mission 1 support wingmate | Confirmed | Direct | High | P5, S2, S3 |
| `SWSQ-009` | `Form the Vanguard` ends after its required final Imperial formation and awards a retained `Mission Complete` medal independently of optional medals | Confirmed | Corroborated | High | S2, S4 |
| `SWSQ-010` | Update 4.2 is the latest official client-note page; later server balancing does not alter the fixed Story Mission 1 packet | Confirmed | Direct | High | P7 |
| `SWSQ-011` | The repository trace reproduces the bounded flight, combat, power, shield, countermeasure, resupply and terminal transitions without direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Motive Studios / Electronic Arts; original release
  2020-10-02, with the current PC product still distributed by EA and Steam.
- Platform or physical form: Windows PC client; Standard Edition; one local
  Story mission with no admitted multiplayer account progression.
- Puzzle family: embodied spatial reasoning; tactical forecast and counterplay;
  real-time system pressure; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official current EA product page](https://www.ea.com/games/starwars/squadrons),
    for current title, platforms, Story and product availability.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/1222730/STAR_WARS_Squadrons/),
    for app identity, Windows distribution and release metadata.
  - **[P3]** [official Pilot Briefing gameplay overview](https://www.ea.com/games/starwars/battlefront/news/pilot-briefing-gameplay-overview),
    for first-person flight, T-65B X-wing, components, power and shields.
  - **[P4]** [official PC text manual](https://www.ea.com/able/resources/star-wars/star-wars-squadrons/pc/text-manual),
    for keyboard/mouse flight, weapon, targeting, countermeasure, shield and
    power controls.
  - **[P5]** [official PC gameplay settings](https://www.ea.com/able/resources/star-wars/star-wars-squadrons/pc/gameplay-settings),
    for difficulty, Standard instruments, objectives and AI-wingmate resupply UI.
  - **[P6]** [official GDC 2022 design slides](https://media.gdcvault.com/GDC%2B2022/Speaker%2BSlides/StarWarsSquadrons_Frazier_Ian.pdf),
    for Rebel Mission 1's authored flight/combat, missile/power and
    shield/targeting learning corridor.
  - **[P7]** [official Update 4.2 notes](https://www.ea.com/news/update-4-2-release-notes),
    for the latest published client update boundary.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depot record](https://steamdb.info/app/1222730/depots/),
    for public build `8101433` and branch timestamp.
  - **[S2]** [StrategyWiki Mission 1 record](https://strategywiki.org/wiki/Star_Wars%3A_Squadrons/Form_the_Vanguard),
    for fixed loadout, encounter sequence and final formation.
  - **[S3]** [EA Forums Mission 1 resupply report](https://forums.ea.com/discussions/star-wars-games-discussion-en/cannot-request-resupply-in-mission-1/10604849),
    corroborating the support request in the exact mission.
  - **[S4]** [Speedrun mission-medal guide](https://www.speedrun.com/de-DE/squadrons/guides/ma4ry),
    distinguishing guaranteed completion from optional medals.
  - **[V1]** repository-side transition trace from `P1`–`P7` and `S1`–`S4`;
    rules reasoning, not direct play.
- Claim IDs: `SWSQ-001`–`SWSQ-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-161`: directly attack a selected reachable hostile with lasers
  or the fixed guided offensive auxiliary.
- New `ACT-392`: directly pilot the X-wing with throttle, pitch, yaw and roll.
- New `ACT-393`: reallocate the shared live budget among engines, lasers and
  shields or restore balance.
- New `ACT-394`: focus existing shield charge toward the front or rear facing.
- New `ACT-395`: time one finite countermeasure against an incoming missile.
- New `ACT-396`: request repair and resupply from Gunny's AI U-wing.
- Parameters: craft, target, throttle, orientation, weapon, lock, power channel,
  shield facing, countermeasure warning, support request and result.
- Claim IDs: `SWSQ-003`–`SWSQ-008`.

### System Behaviour Genes

- Existing `SYS-215`: direct attacks and hostile response resolve in real time.
- New `SYS-723`: flight inputs continuously update three-dimensional motion,
  with solid collisions able to damage shields or hull.
- New `SYS-724`: current power allocation changes subsystem performance and
  permits channel-specific overcharge.
- New `SYS-725`: the struck directional deflector absorbs damage before hull,
  while focus commands transfer charge between facings.
- New `SYS-726`: target selection, missile lock/pursuit, incoming warning and
  countermeasure interception form one cockpit threat chain.
- New `SYS-727`: a legal support request routes the AI wingmate's repair and
  ordnance payload to the player's moving craft.
- New `SYS-728`: authored objectives advance in order and the final required
  formation settles into debrief plus the guaranteed completion medal.
- Resolution order: objective exposes an encounter; flight establishes target
  geometry; current power/shield state changes performance and damage routing;
  lasers or locked missile resolve against the selected target; warnings allow
  countermeasure response; support can restore the fixed combat state; clearing
  the predicate reveals the next objective; the final predicate writes terminal.
- Claim IDs: `SWSQ-003`–`SWSQ-011`.

### Constraint Genes

- Existing `CON-269`: offensive auxiliaries and support/countermeasure actions
  require legal target, range, resource and readiness state.
- Existing `CON-282`: the fixed story objectives must be satisfied in authored
  order before later encounters and debrief become available.
- New `CON-565`: engines, lasers and shields share one bounded live power
  budget; emphasis in one channel withholds allocation from another.
- Scarce resources: hull, directional shield charge, laser/auxiliary readiness,
  finite countermeasures, support availability, target geometry and shared power.
- Claim IDs: `SWSQ-004`–`SWSQ-010`.

### Information Genes

- Existing `INF-115`: current visible local obstacles, ships and hazards.
- Existing `INF-125`: current authored objective, marker and route dependency.
- Existing `INF-268`: staged instruction and completion feedback.
- New `INF-277`: cockpit instruments expose power, shields, hull, auxiliaries,
  countermeasures, selected target, lock state and incoming threat warning.
- Claim IDs: `SWSQ-003`–`SWSQ-009`.

### Objective Genes

- New `OBJ-141`: complete `Form the Vanguard`, reach its debrief and retain the
  unconditional `Mission Complete` medal.
- Optional medals, Mission 2 and campaign completion are explicitly independent
  and do not enter this objective.
- Claim IDs: `SWSQ-004`, `SWSQ-009`–`SWSQ-011`.

### Time Genes

- Existing `TIM-003`: flight, hostile movement, weapon effects, locks, power,
  shield damage and support delivery advance concurrently in real time outside
  blocking interfaces.
- Claim IDs: `SWSQ-003`–`SWSQ-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Public build `8101433`; Story; Pilot; Standard instruments; non-VR; keyboard/mouse | Start Mission 1 and accept the first controllable X-wing cockpit | Fixed craft, loadout, first objective and cockpit resources become active | exact entry packet | `SWSQ-001`–`SWSQ-004` |
| Current objective marker lies off-axis | Apply throttle, pitch, yaw and roll | Craft position/orientation update continuously; collision can damage the craft | direct spatial flight | `SWSQ-003`, `SWSQ-004` |
| Required hostile is visible | Select it, establish geometry and fire lasers or a locked Concussion Missile | Live hit, damage, evasion and destruction resolve | target-combat loop | `SWSQ-003`, `SWSQ-007` |
| One subsystem needs emphasis | Route power to engines, lasers or shields | Shared allocation changes subsystem performance and can create overcharge | live power trade-off | `SWSQ-005` |
| Threat approaches one facing | Focus shield charge front or rear | Charge transfers and the struck facing absorbs damage before hull | directional defence | `SWSQ-006` |
| Incoming-missile warning is active and a charge is ready | Deploy Seeker Warheads in the response window | The finite countermeasure attempts to defeat the guided threat | timed active defence | `SWSQ-007` |
| Hull or ordnance is depleted and support is legal | Request resupply from Gunny | AI U-wing routes a payload that restores bounded hull/ordnance state | mobile AI logistics | `SWSQ-008` |
| A required objective remains incomplete | Leave its target or formation unresolved | Later objective and mission-completion medal remain unavailable | negative terminal boundary | `SWSQ-009` |
| Final Arquitens, two jammers and required TIE escorts are destroyed | Accept mission settlement and debrief | `Mission Complete` is retained; optional medal predicates settle separately | positive terminal | `SWSQ-009`–`SWSQ-011` |

## Strategic and experiential structure

- Local: keep target geometry while steering, select the right weapon, read the
  warning, and match power and shield facing to the immediate threat.
- Medium-term: trade engine mobility, laser pressure and shield recovery across
  ordered encounters while preserving countermeasure and support availability.
- Long-term: convert the fixed instructional mission from first controllable
  X-wing state into a retained completion medal without importing later lessons.
- Heuristics: align before locking; move power before the demand peaks; face or
  focus the healthier shield; counter only after a warning; request support
  before hull/ordnance loss prevents clearing the next objective.
- Failure attribution: target panel, lock indicator, power channels, shield
  facings, hull, countermeasure count, warning and objective/debrief feedback
  separate steering, allocation, timing, combat and terminal mistakes.
- Player trust: each learned control exposes an immediate instrument response;
  authored objective feedback and the final medal make progression inspectable.
- Claim IDs: `SWSQ-003`–`SWSQ-011`.

## Replay and variation

- Exact flight path, target order within a formation, weapon mix, power/shield
  allocation, damage and support timing vary; mission, craft, loadout, authored
  objective order and retained terminal remain fixed.
- Combat is live, but no procedural map, multiplayer opponent or random loadout
  enters the packet. Restarting or replaying does not broaden the signature.
- A future build that changes Mission 1's craft, required objectives or terminal
  requires a new review boundary.

## Adjacent systems and history

- Similar games: War Thunder, Battlefield V, Half-Life 2 and STAR WARS Jedi:
  Fallen Order connect real-time spatial control, combat and authored objectives.
- War Thunder's Ground Realistic Battle uses multi-crew armoured vehicles,
  capture points and ticket attrition; Squadrons instead concentrates direct
  six-degree flight, live three-channel power and two-facing shields in a fixed
  single-player cockpit mission.
- Jedi: Fallen Order uses on-foot guard, Force, traversal and checkpointed
  authored exploration; Squadrons replaces character build and navigation with
  vehicle energy geometry, guided-threat response and AI logistics.
- Fleet Battles, component builds, multiplayer roles, VR presentation and later
  campaign lessons are adjacent modules rather than parameters.
- Claim IDs: `SWSQ-002`–`SWSQ-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-161`, `ACT-392`, `ACT-393`, `ACT-394`, `ACT-395`, `ACT-396` | attack, direct flight, power, shield focus, countermeasure, AI support |
| System Behaviour | `SYS-215`, `SYS-723`, `SYS-724`, `SYS-725`, `SYS-726`, `SYS-727`, `SYS-728` | live combat, flight, allocation, directional defence, targeting, logistics, settlement |
| Constraint | `CON-269`, `CON-282`, `CON-565` | readiness, authored order, shared power |
| Information | `INF-115`, `INF-125`, `INF-268`, `INF-277` | local, objective, tutorial and cockpit state |
| Objective | `OBJ-141` | complete Mission 1 and retain its medal |
| Time | `TIM-003` | concurrent live flight and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `224` (`GAME-0001`–`GAME-0224`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`7 / 29 = 0.241379`).
- Supported combination subsets: `COMB-0223`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-161`, `SYS-215`, `CON-282`, `INF-115`, `INF-125`, `INF-268`, `TIM-003` | both use staged local/objective guidance through ordered live combat; Once Human routes an account-gated character tutorial into scenario-selection authority, while Squadrons directly pilots a fixed cockpit craft whose power allocation, directional shields, guided threats and AI resupply settle one medal-bearing mission; the seven shared genes cover `7 / 14 = 0.500000` of Once Human's smaller genome | Near, `7 / 29 = 0.241379` |

## Combination status

- `COMB-0223` is the verified strict subset coupling direct cockpit flight,
  shared live power, directional shields, guided-threat response and authored
  Mission 1 settlement.
- Every earlier verified combination is tested after registration; supporting
  subsets are recorded rather than inferred from shared science-fiction theme.

## Taxonomy impact

- Adds fourteen Active boundaries and one combination; direct hostile combat,
  ability legality, authored order, local/objective/tutorial information and
  real-time progression are reused.
- No previously reviewed signature or lifecycle changes.
- The new boundaries separate cockpit flight-resource decisions from generic
  vehicle handling and from wider multiplayer or campaign systems.

## Negative results

- War Thunder capture/ticket, penetration, crew and respawn genes are absent;
  Mission 1 has no admitted PvP vehicle roster or match economy.
- Jedi: Fallen Order guard, Force, character traversal, Meditation and Holomap
  genes are absent despite the shared franchise.
- Component customisation, ranks, Operations, team composition, Fleet Battles,
  VR and optional medal optimisation do not enter merely because the product
  supports them elsewhere.
