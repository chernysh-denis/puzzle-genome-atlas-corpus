---
game_id: GAME-0334
slug: quake
game_title: Quake
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-161
    - ACT-164
  system:
    - SYS-057
    - SYS-065
    - SYS-112
    - SYS-215
    - SYS-222
    - SYS-578
    - SYS-949
  constraint:
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Quake

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). E1M1, shotgun,
armour colours, monsters, buttons and the slipgate are carrier parameters, not
gene names.

## Analysis scope

- Version / ruleset: the unmodified `Quake (Original)` application supplied
  with the current licensed English Windows Steam package `2310`, not the 2021
  Enhanced campaign. Valve's product page explicitly distinguishes the
  fully-moddable untouched original from Enhanced content.
- Structured analysis target: licensed Windows Steam access to `Quake
  (Original)`; see `GAME-0334` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: fresh single-player game on Medium, Episode 1 `Dimension of the
  Doomed`, `E1M1: The Slipgate Complex`, from the first controllable frame to
  contact with the exit slipgate and the resulting `E1M2` transition.
- Entry: the player enters E1M1 with the axe, shotgun, starting shells, 100
  Health and no carried level state from an earlier map.
- Primary decision loop: read local three-dimensional geometry and hostile
  sightlines; move, strafe, turn, aim, jump, fire or switch weapon; collect
  compatible ammunition, health and armour; survive perception-triggered
  pursuit and live combat; activate the bridge/lift route and three required
  buttons; pass the opened exit door; enter the slipgate.
- Positive terminal: touching the final change-level trigger loads E1M2. The
  successor level itself is outside this packet.
- Failure terminal: Health reaching zero ends the current attempt. Manual
  save/load exists in the original game but is deliberately excluded from this
  packet because no particular save point or reload trace is observed.
- Included: direct 3D movement, jumping, local aiming and fire; axe and shotgun;
  compatible finite ammunition; local monsters; sight and weapon-noise wake-up;
  health and armour pickups; green/yellow armour protection factors; fractional
  split of incoming damage between armour reserve and Health; ordinary doors,
  moving platform/bridge fixtures, three required buttons, the exit door and
  the E1M2 slipgate.
- Reproducible parameterisation: follow the ordinary authored route on Medium,
  activate the bridge/lift fixtures, press the three exit buttons and enter the
  slipgate. Exact movement, monster kills, ammunition, remaining armour/Health
  and optional pickups are bounded parameters. No speedrun, secret or
  all-kills requirement is admitted.
- Excluded: start-map skill selection; E1M2 and later maps; episode runes;
  secrets; Nightmare; multiplayer; mission packs; Quake 64; Enhanced rendering,
  accessibility, Horde, add-ons and wrapper state; mods; console commands;
  cheats; save/reload persistence; source-port behaviour and later games.
- Direct-play status: not conducted. No entitlement, installation, executable,
  save, screenshot, video, audio or input trace was used. The preserved manual,
  id Software source, pinned rerelease QuakeC and released E1M1 map text support
  a source-bounded reconstruction rather than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `QUA-001` | The packet is untouched `Quake (Original)` E1M1 on Medium, not Enhanced or a later port | Confirmed | Direct | High | P1, P2 |
| `QUA-002` | The player directly moves, aims, jumps, selects a carried weapon and fires in live 3D space | Confirmed | Direct | High | P2, P3 |
| `QUA-003` | Compatible weapons require finite typed ammunition and contact pickups refill only to their caps | Confirmed | Direct | High | P2, P3 |
| `QUA-004` | Monsters acquire a visible or recently exposed hostile target, then turn, pursue and attack autonomously | Confirmed | Direct | High | P3 |
| `QUA-005` | Armour saves a protection-factor share of every compatible hit before the unsaved remainder reduces Health | Confirmed | Direct | High | P3 |
| `QUA-006` | Armour pickup replacement compares protection-factor × reserve rather than colour or reserve alone | Confirmed | Direct | High | P3 |
| `QUA-007` | Three distinct E1M1 buttons feed one count-three trigger; only completion opens the authored exit door | Confirmed | Direct | High | P4 |
| `QUA-008` | The final trigger changes the map to E1M2, making slipgate contact the bounded positive terminal | Confirmed | Direct | High | P2, P4 |
| `QUA-009` | The signature admits only transitions causally available in the fixed E1M1 packet | Observation | Direct | High | P1–P4, V1 |

## Basic data

- Release / origin: id Software; original PC release 1996-06-22. The current
  Steam package is published by Bethesda Softworks and includes the untouched
  original alongside, but distinct from, Enhanced.
- Platform or physical form: licensed digital Windows PC package, launching the
  bundled original ruleset.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/2310/Quake/),
    for current licensed access, original/Enhanced distinction, developer,
    publisher and release identity.
  - **[P2]** [preserved original Quake manual](https://quakeone.com/q1files/downloads/q1manual.pdf),
    for movement, shooting, absence of a Use command, contact pickup, buttons,
    doors, platforms, weapon selection, HUD, goal and slipgate level transfer.
  - **[P3]** [id Software rerelease QuakeC at commit `634eefab`](https://github.com/id-Software/quake-rerelease-qc/tree/634eefab09a77eb7b5f5ca7078ba3d8784a91142/quakec),
    used only where base-campaign operations remain explicit: `combat.qc`
    establishes fractional armour save and Health remainder; `items.qc`
    establishes 0.3/0.6/0.8 armour factors and replacement; `ai.qc` establishes
    visible-target acquisition and pursuit; `buttons.qc` establishes touch,
    damage, movement and target firing. The repository warns that rerelease
    localisation, fixes and modifications exist, so it does not prove
    Enhanced-only behaviour for Original.
  - **[P4]** John Romero's released `E1M1.MAP`, preserved by the
    [Quake map-source mirror](https://github.com/plankatron/quakemash/blob/master/E1M1.MAP),
    for three `func_button` targets, the `trigger_counter` count of three,
    exit-door message, `trigger_changelevel` target `e1m2` and slipgate prompt.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1–P4; rules and
    map-graph reasoning only, with no direct play or audiovisual observation.
- Claim IDs: `QUA-001`–`QUA-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk, strafe, turn and jump the persistent player body
  through E1M1 rather than selecting an automatic destination.
- `ACT-049`: contact or shoot reachable buttons to command their linked route
  mechanism and the three-button exit latch.
- `ACT-161`: aim the active axe or firearm and commit a strike or shot against
  one reachable monster or shootable fixture.
- `ACT-164`: select one owned weapon as the current firing input.
- Claims: `QUA-002`, `QUA-003`, `QUA-007`.

### System Behaviour Genes

- `SYS-057`: an eligible monster that sees the player, observes a propagated
  hostile sight entity or reacts to a visible shot impact replaces idle state
  with pursuit and attack.
- `SYS-065`: an activated route platform or bridge moves along its fixed
  authored path while world time advances.
- `SYS-112`: accepted buttons expose the downstream bridge, route or exit-door
  mechanism; the final door waits for all three counter inputs.
- `SYS-215`: player and monsters exchange cadence-, range-, armour-, Health-
  and defeat-dependent effects in real time.
- `SYS-222`: touching compatible ammunition, weapon or carried key-state items
  transfers the accepted amount into the player's bounded inventory.
- `SYS-578`: unsaved damage reduces one Health pool, compatible health pickups
  restore missing points and zero Health closes the attempt.
- New `SYS-949`: for every compatible hit, `ceil(protection factor × incoming
  damage)` is capped by current armour and removed from that reserve; only the
  unsaved remainder reduces Health. Green and yellow armour parameterise the
  factor and capacity independently.
- Resolution order: inputs update motion, aim, weapon or switch contact;
  autonomous monsters acquire and pursue targets; shot/contact effects resolve;
  armour computes its saved share before the Health remainder; zero Health
  closes the attempt; button targets update route state; final slipgate contact
  changes the map.
- Claims: `QUA-003`–`QUA-008`.

### Constraint Genes

- `CON-578`: the shotgun and other ammunition-consuming weapons can fire only
  while the compatible finite reserve can pay the shot; pickups refill only to
  the fixed cap. The axe remains the no-ammunition fallback.
- Scarce route state: Health, armour reserve/factor, shells, current weapon,
  button progress, hostile position and live exposure.
- Claims: `QUA-003`, `QUA-005`, `QUA-007`.

### Information Genes

- `INF-073`: the Inventory Bar exposes weapons and typed ammunition, highlights
  the active weapon and the Status Bar shows current active-weapon ammunition.
- `INF-115`: first-person sight, spatial architecture, monster motion, weapon
  sound and effects expose only local opponent state rather than an omniscient
  enemy map.
- `INF-119`: the Status Bar exposes armour and Health, including low-state
  colour feedback.
- Claims: `QUA-002`–`QUA-006`.

### Objective Genes

- `OBJ-026`: make the exit route traversably connected by operating the
  authored mechanisms, then reach and enter the E1M1 slipgate.
- Claims: `QUA-007`, `QUA-008`.

### Time Genes

- `TIM-003`: movement, monsters, projectiles, platform travel, attacks and
  damage continue on the live simulation clock between local inputs.
- Claims: `QUA-002`–`QUA-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| E1M1 is live | move, turn, strafe or jump | the player body traverses current collision geometry while monsters and mechanisms continue | direct live navigation | `QUA-002` |
| A monster is eligible and the player becomes visible | cross its sight test or expose a visible attack stimulus | it stores the player as enemy, turns toward that target and enters pursuit/attack state | perception-driven hostility | `QUA-004` |
| Shotgun is active with compatible shells | fire once | the shot spends the declared shell cost, resolves traces/damage and exposes weapon noise; empty incompatible reserve cannot pay it | finite ammunition | `QUA-003` |
| Player has 100 yellow armour at factor 0.6 and 100 Health | receive one compatible 10-damage hit | `ceil(0.6 × 10) = 6` armour is removed and the remaining 4 reduces Health | fractional protection | `QUA-005` |
| Current armour protection product exceeds a candidate pickup's | touch that weaker armour | pickup is rejected; a better product replaces factor, reserve and armour type | armour replacement order | `QUA-006` |
| One E1M1 route switch is reachable | touch or legally shoot it | the button moves and fires its authored target, changing the linked platform/door state | switch-directed route | `QUA-007` |
| Fewer than three exit buttons have fired `t9` | activate another required button | the count-three trigger retains progress; the exit door remains shut until the third input | ordered latch | `QUA-007` |
| All three exit buttons have fired | allow the counter target to resolve | target `t10` opens the final door and makes the slipgate corridor traversable | exposed exit mechanism | `QUA-007` |
| Exit corridor is open | walk into the slipgate trigger | `trigger_changelevel` loads `e1m2`; ordinary E1M1 decision-making ends | bounded terminal | `QUA-008` |

## Strategic and experiential structure

- Local decision: trade movement, aim, weapon choice and ammunition against
  visible monster position, cover, Health and current armour protection.
- Medium-term planning: preserve shells and Health while opening the authored
  route, then remember which of the three exit buttons remain unresolved.
- Long-term structure: convert a hostile spatial route into one traversable
  exit without any requirement to kill every monster or discover every secret.
- Common heuristics: keep moving across exposed sightlines; use the axe only
  when its range is safe or shells are scarce; prefer an armour pickup only
  when its protection product improves current state; verify all three button
  branches before returning to the exit door.
- Failure attribution: visible Health, armour, ammunition and local enemy
  feedback distinguish resource depletion from navigation or switch omission.
- Claims: `QUA-002`–`QUA-009`.

## Replay and variation

- What changes between attempts: route timing, kills, damage taken, armour and
  Health pickups, ammunition use and remaining state at E1M2 transfer.
- Randomness or procedural generation: E1M1 geometry, fixtures and placements
  are authored; combat variation follows timing, target acquisition and damage
  resolution rather than procedural layout.
- Multiple viable strategies: optional kills, pickups and secret routes vary,
  but the ordinary positive terminal still requires the three exit buttons and
  final slipgate contact.
- Typical replay motive: faster completion, more retained combat resources,
  more kills/secrets or a different weapon route; only the bounded exit route
  enters this signature.

## Adjacent systems and history

- Direct predecessors: Doom supplies direct real-time shooting, finite ammo,
  pickups and authored switch routes; Quake's packet makes those operations
  fully three-dimensional and adds factor-based armour splitting.
- Variants: Enhanced, Quake 64, mission packs, source ports and multiplayer
  require separate evidence and cannot inherit this signature automatically.
- Similar games: DOOM (2016), DOOM Eternal and Half-Life (1998) share direct
  traversal, firearm combat, finite resources, local opponent information and
  authored route gates.
- Important difference: Quake armour saves a fraction of each hit while a
  reserve remains; `SYS-655` instead requires an armour capacity to absorb
  damage before Health, so it is explicitly not reused.

## Normalised genome

The front matter is canonical. The complete signature contains 17 Active
genes: four Action, seven System Behaviour, one Constraint, three Information,
one Objective and one Time gene. Carrier labels remain parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `333` (`GAME-0001`–`GAME-0333`).
- Exact genome matches: none.
- Tied near matches: `GAME-0237` — Serious Sam HD: The First Encounter (`11 / 19 = 0.578947`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0237` — Serious Sam HD: The First Encounter | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `OBJ-026`, `TIM-003` | Both use direct real-time first-person traversal, aimed weapon combat, finite typed ammunition, contact pickups, local opponent information and a spatial exit. Serious Sam adds mandatory encounter-clearance gates. Quake instead adds reachable switches, perception-driven pursuit, moving route mechanisms, a three-button latch, continuous Health restoration and factor-split armour damage. | Near, `11 / 19 = 0.578947` |

## Taxonomy impact

`SYS-949` is new. `SYS-655` fails the two-way transfer test because its armour
capacity must deplete before Health, whereas Quake consumes a factor-based
share of each hit and passes the unsaved remainder to Health immediately.
Existing switch, route, combat, pickup, health, ammunition and information
boundaries transfer without wording changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, installed-build parity, audiovisual observation, save/reload
  test, secret route or all-kills trace is claimed.
- Enhanced-only fixes and behaviours in the rerelease repository are not
  projected into `Quake (Original)`.
- `SYS-655` is rejected because sequential armour-before-Health is not the
  observed fractional split.
- No reload gene is admitted: base Quake spends typed reserve directly.
- No encounter-clearance gate is admitted: ordinary E1M1 completion does not
  require killing every monster.

## Delta summary

## New facts

- [Confirmed | Direct | High] The manual, base source and pinned QuakeC close
  the direct combat, inventory, perception, Health and armour transitions.
- [Confirmed | Direct | High] Released E1M1 map text closes the three-
  button counter, exit-door and E1M2 slipgate terminal.

## New genes

- [Confirmed | Direct | High] `SYS-949` isolates protection-factor damage split
  between a depleting armour reserve and Health.

## New combinations

- [Observation | Direct | High] None; recurrence remains evidence-driven.

## Taxonomy changes

- [Observation | Direct | High] None to lower IDs; `SYS-655` remains distinct
  after the explicit two-way transfer test.

## New questions

- Which later shooter independently uses the same factor-times-damage armour
  split rather than an armour-first layer?
- Does a separately scoped full episode introduce a persistent level-to-level
  inventory-transfer gene beyond this single slipgate boundary?

## Next recommended game

- `GAME-0335` RollerCoaster Tycoon Deluxe, as reserved by selection 023.

## Why this game

- Quake is a recognisable PC anchor whose E1M1 turns three-dimensional combat,
  resource conservation and an explicit three-switch spatial dependency into
  one compact, source-verifiable route.

## Completion checklist

- [x] Exact original ruleset, level, entry, terminal and exclusions declared.
- [x] Product, manual, code and deterministic map evidence separated.
- [x] Navigation, switch, combat, perception, ammunition, armour and terminal decomposed.
- [x] Reviewed Ukrainian, presentation, platform, families, salience and plain language integrated.
- [x] Original artwork and responsive variants integrated.
- [x] Repository, localisation, build, browser and accessibility gates passed.

## Search-demand continuation

The unit fulfils the first reserved subject in
[`SEARCH_DEMAND_GAME_SELECTION_023`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_023.md).
`GAME-0335` RollerCoaster Tycoon Deluxe is the next recorded Goal unit.
