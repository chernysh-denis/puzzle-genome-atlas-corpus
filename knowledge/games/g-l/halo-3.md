---
game_id: GAME-0315
slug: halo-3
game_title: Halo 3
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-199
    - ACT-341
  system:
    - SYS-215
    - SYS-222
    - SYS-348
    - SYS-369
    - SYS-749
    - SYS-780
    - SYS-913
  constraint:
    - CON-262
    - CON-282
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-349
  objective:
    - OBJ-183
  time:
    - TIM-003
---

# Game: Halo 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Mission, chapter,
weapon, enemy, ally and difficulty labels are parameters, not gene names.

## Analysis scope

- Version / ruleset: the English North American Halo 3 Standard Edition
  released for Xbox 360 on 2007-09-25, reconstructed from Microsoft's launch
  announcement, the launch manual and the contemporaneous licensed strategy
  guide. The disc region, title-update number and installed binary were not
  observed, so this is a launch-content ruleset boundary rather than a claim
  about one locally identified executable.
- Structured analysis target: original Xbox 360 Standard Edition, fresh solo
  Campaign on `Normal`, default controls, Campaign Scoring off and no skulls;
  see `GAME-0315` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: traverse the authored Sierra 117 route, manage two finite-ammunition weapons, grenades, melee, cover and shield recharge through required encounters, release Sergeant Johnson, settle the counterattack and board the Pelican into Crow's Nest.
- Entry: first ordinary Master Chief control after the opening camera-look
  calibration in `Sierra 117`, before the first jungle encounter or pickup.
- Positive terminal: Johnson is released, the required dam counterattack has
  settled, Master Chief boards the extraction Pelican, `Sierra 117` completes
  and the documented Campaign continuation advances to `Crow's Nest`. The
  manual documents Campaign `Continue` and checkpoints, but no local save,
  quit or relaunch was performed; exact storage-device state is not claimed.
- Included: first-person movement and jumping; directly aimed firearm and
  melee combat; primary/reserve weapon switching; manual magazine reload;
  finite ammunition and at most two grenades of each available type; reachable
  weapon replacement and automatic compatible pickups; personal shield before
  underlying health; delayed shield recharge without new damage; moving/firing
  actor contacts on the visor Motion Tracker; local sight and sound; objective
  waypoints, interaction prompts and checkpoint notices; authored encounter
  groups; checkpoint restoration after lethal failure; Johnson's release;
  Pelican boarding; mission settlement and the named successor.
- Excluded: cooperative Campaign; Campaign Scoring; skulls, Rally Point starts
  and non-`Normal` tuning; Xbox LIVE, System Link, split screen, matchmaking,
  Custom Games, Forge, Theater and Saved Films; terminals and optional skull
  collection; dual-wielding as a required route; optional equipment use;
  player-controlled vehicles; later missions; achievements; downloadable map
  packs; backward-compatible Xbox One/Series presentation; Halo 3: ODST; Halo:
  The Master Chief Collection and all later ports or remasters.
- Reproducible parameterisation: start a fresh solo `Normal` campaign with
  scoring and skull modifiers off, pass the look calibration, retain the
  starting Assault Rifle and Magnum or replace either only through a reachable
  weapon prompt, follow the Arbiter and Marines through `Walk It Off`, clear
  required routed Covenant groups through the river, camp, sub-station and
  sniper route, cross the authored transition into `Charlie Foxtrot`, continue
  through the crashed-Pelican and jungle path into `Quid Pro Quo`, defeat the
  dam defenders, activate Johnson's cell release, defeat the required arriving
  forces and enter the Pelican. Exact weapon pair, ammunition expenditure,
  grenade use, ally survival, shield breaks, deaths and optional pickups remain
  parameters; no skull or optional equipment is required.
- Potential scoped modules: performed checkpoint save/quit/relaunch equality;
  dual wield; equipment; skull modifiers; Campaign Scoring; co-op; vehicles;
  later missions; multiplayer; Forge and Theater each require their own entry,
  loop and evidence.
- Direct-play status: not conducted. No Xbox 360 console, disc, entitlement,
  installed build, controller trace, campaign save or storage device was
  available. No video or audio was opened, played or analysed. Microsoft and
  Xbox establish the product and release; the original manual and licensed
  guide establish controls, HUD and combat state; written mission references
  corroborate the route and terminal. This is a source-bounded reconstruction,
  not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `H3-001` | Microsoft released Halo 3 Standard Edition for Xbox 360 on 2007-09-25, developed by Bungie Studios | Confirmed | Direct | High | P1, P2 |
| `H3-002` | Campaign supports solo continuation separately from co-op, multiplayer, Forge and Theater | Confirmed | Direct | High | P2 |
| `H3-003` | Default controls provide movement, jump, crouch, aim/fire, melee, reload, weapon swap, grenade selection/throw and contextual action | Confirmed | Direct | High | P2 |
| `H3-004` | The HUD exposes primary and reserve weapons, ammunition or charge, grenades, shield, Motion Tracker, waypoint, interaction and checkpoint notices | Confirmed | Direct | High | P2, S1 |
| `H3-005` | Incoming damage depletes the personal energy shield; after several damage-free seconds it refills, while further damage after depletion can kill Master Chief | Observation | Corroborated | High | P2, S1 |
| `H3-006` | The carried combat state has one primary and one reserve weapon, finite ammunition or charge and at most two grenades of each type | Observation | Corroborated | High | P2, S1 |
| `H3-007` | The Motion Tracker exposes nearby moving or firing entities by relative bearing and allegiance while withholding elevation and stationary contacts | Confirmed | Direct | High | P2, S1 |
| `H3-008` | Halo 3 checkpoints are authored save requests that wait for safe state; lethal failure may restore the latest accepted checkpoint | Observation | Corroborated | Medium | P3, S1, S2 |
| `H3-009` | `Sierra 117` proceeds through `Walk It Off`, `Charlie Foxtrot` and `Quid Pro Quo` to Johnson's rescue and a required dam counterattack | Observation | Corroborated | High | S1–S3 |
| `H3-010` | Boarding the arriving Pelican completes `Sierra 117` and begins the transition to `Crow's Nest` | Observation | Corroborated | High | S2, S3 |
| `H3-011` | No player-controlled vehicle is required in the scoped mission; the Pelican is an extraction interaction and cutscene transition | Observation | Corroborated | High | S1–S3 |
| `H3-012` | No original-console run or save/relaunch comparison was performed, so exact retained checkpoint fields remain unobserved | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Bungie Studios / Microsoft Game Studios; North American
  Xbox 360 launch on 2007-09-25.
- Platform or physical form: English Halo 3 Standard Edition for Xbox 360,
  source-bounded launch-content rules, fresh solo `Normal` Campaign.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; world topology and perspective; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [Microsoft launch announcement](https://news.microsoft.com/source/2007/09/24/starting-at-midnight-the-worldwide-wait-for-halo-3-ends/),
    for 2007-09-25 availability, Xbox 360 exclusivity, Bungie authorship and
    Standard Edition identity.
  - **[P2]** [official Halo 3 Xbox 360 manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/Halo3_MNL_EN-US.pdf),
    for the original control map, HUD, weapons, grenade capacity, equipment,
    Campaign lobby and separation from multiplayer, Forge and Theater.
  - **[P3]** [Microsoft Halo 3 HaloScript checkpoint documentation](https://learn.microsoft.com/en-us/halo-master-chief-collection/h3/individual/haloscriptoverview#checkpoints),
    for authored `game_save` requests and their safe-state wait. The current
    editing-kit documentation corroborates engine semantics but is not treated
    as proof of one installed 2007 binary.
- Corroborating textual sources, accessed 2026-09-19:
  - **[S1]** [Piggyback Halo 3 guide sample](https://www.piggyback.com/us/wp-content/uploads/sites/6/2020/04/H3_E_SamplePages.pdf),
    a launch-era licensed guide for shield recharge, primary/reserve weapon
    HUD, grenade cap, Motion Tracker, waypoints, interaction prompts,
    checkpoint notices and the first `Sierra 117` route sectors.
  - **[S2]** [Sierra 117 mission reference](https://www.halopedia.org/Sierra_117),
    for the original mission identity, chapters, starting weapons, objectives,
    dam rescue and transition toward `Crow's Nest`.
  - **[S3]** [Sierra 117 walkthrough](https://www.halopedia.org/H3%3ASierra_117/Walkthrough),
    for required route order, final reinforcements and boarding the Pelican to
    complete the level.
- Research record: **[R1]** local 2026-09-19 preflight found no original Xbox
  360 product, disc, installed build, save or controller trace; no direct play,
  video, audio or save/relaunch test was performed.
- Claim IDs: `H3-001`–`H3-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns direct local traversal and jumping; `ACT-161` aimed firearm
  and ordinary melee attacks; `ACT-164` switching primary and reserve weapons;
  `ACT-183` magazine reload; `ACT-184` one finite grenade throw; `ACT-199`
  prompted weapon pickup or replacement; and `ACT-341` contextual world
  actions including Johnson's cell release and Pelican boarding. Claims:
  `H3-003`, `H3-006`, `H3-009`–`H3-011`.

### System Behaviour Genes

- `SYS-215` resolves live hostile combat; `SYS-222` accepts compatible world
  ammunition and grenade pickups; `SYS-348` routes damage through shield and
  underlying health toward lethal defeat; new `SYS-913` restores the ordinary
  personal shield after a damage-free interval; `SYS-749` instantiates finite
  authored encounter groups; `SYS-369` restores the latest accepted checkpoint
  after lethal failure; and `SYS-780` carries the settled mission into the
  documented `Crow's Nest` continuation.
- Resolution order: weapon, ammunition, aim, range and target state resolve a
  shot or melee contact; incoming compatible damage first reduces shield, then
  threatens underlying life state; another hit interrupts recharge while a
  quiet interval refills the shield; encounter clearance and route position
  advance authored groups and checkpoints; releasing Johnson admits the
  counterattack; its settlement admits the Pelican; boarding closes the mission
  and names the successor. Claims: `H3-005`, `H3-008`–`H3-012`.

### Constraint Genes

- `CON-262` owns the primary/reserve weapon slots, grenade caps and finite
  carried ammunition; `CON-578` requires compatible ammunition or charge to
  fire; `CON-282` requires ordered authored route, rescue and extraction gates;
  and `CON-402` keeps declared combat progression blocked until required finite
  hostiles and reinforcements settle. Optional enemy bypasses and surviving
  incidental actors do not become a claim that every spawned body must die.
  Claims: `H3-006`, `H3-008`–`H3-010`.

### Information Genes

- `INF-073` owns the active/reserve weapon, ammunition or charge, grenade and
  equipment surface; `INF-119` owns shield/health readiness; `INF-115` local
  sight and sound; `INF-125` waypoints and current mission gates; `INF-268`
  contextual control/objective instructions; and new `INF-349` the passive
  moving/firing-contact Motion Tracker with allegiance but no elevation or
  stationary disclosure. Claims: `H3-003`–`H3-009`.

### Objective Genes

- New `OBJ-183` owns the whole first-mission terminal: traverse to the dam,
  release Johnson, settle the required counterattack, board the Pelican and
  retain `Crow's Nest` as the named continuation. Reaching the dam, freeing
  Johnson without surviving the response, or seeing the Pelican without
  boarding is not the declared result. Claims: `H3-009`, `H3-010`, `H3-012`.

### Time Genes

- `TIM-003` owns real-time movement, combat, shield delay, reinforcement and
  extraction inputs. Checkpoint retention is a state-restoration System, not a
  rewind command or branchable manual-save timeline. Claims: `H3-005`,
  `H3-008`–`H3-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Master Chief has one active firearm with compatible magazine ammunition | Aim and fire | the shot spends ammunition and resolves range, collision, defence and damage against the reached target | finite direct real-time offence | `H3-003`, `H3-006` |
| Active magazine is depleted while compatible reserve remains | Commit reload | firing readiness is given up during the reload and the active magazine refills from reserve | reload and firing are separate commitments | `H3-003`, `H3-006` |
| A third reachable weapon is offered while primary and reserve are occupied | Hold the pickup prompt | the selected carried weapon is replaced and becomes available while the displaced one returns to world state | two-slot carrying creates a keep-or-replace choice | `H3-004`, `H3-006` |
| One selected grenade remains | Throw it toward reachable space | its count decreases and the projectile follows its fuse and typed blast result | grenade capacity is distinct from firearm ammunition | `H3-003`, `H3-006` |
| Compatible damage reaches Master Chief while shield remains | Receive the hit | shield charge decreases before underlying lethal state is exposed | layered defence precedes defeat | `H3-004`, `H3-005` |
| Shield is not full and no new damage arrives for the required interval | Remain out of damage | shield recharge starts and refills toward its cap; another hit interrupts or resets the interval | withdrawal converts time without damage into renewable protection | `H3-005` |
| A nearby actor moves or fires within tracker range | Observe the visor tracker | a relative contact appears with friendly or hostile colour, but no elevation or stationary identity is supplied | local sensor knowledge remains partial | `H3-007` |
| An authored checkpoint request occurs while the player is safe | Cross the checkpoint state | the checkpoint is accepted and briefly reported; an unsafe state may delay or reject that save request | checkpoint placement and acceptance are not arbitrary manual saves | `H3-008` |
| Master Chief reaches lethal failure after an accepted checkpoint | Allow failure settlement | the unfinished mission restores the latest eligible authored checkpoint state | death does not consume a finite life or preserve the failed transient fight | `H3-008` |
| Johnson is captive at the dam and the release control is reachable | Activate the control | the cell barrier opens, Johnson and survivors become free and the final counterattack begins | rescue is an authored world-state gate | `H3-009` |
| Required post-rescue Covenant pressure has settled | Approach the arriving Pelican | extraction becomes reachable without player-controlled vehicle operation | finite combat settlement admits exit | `H3-009`–`H3-011` |
| Pelican cargo bay is reachable after rescue | Board it | `Sierra 117` completes and the campaign transitions toward `Crow's Nest` | mission result and named successor, with reload equality still unobserved | `H3-010`, `H3-012` |

## Strategic and experiential structure

- Local decision: trade exposed fire for cover long enough to recharge shield,
  choose weapon range and target order, and spend scarce magazine, reserve and
  grenade stock without losing the second carried option.
- Medium-term planning: replace weapons around the next encounter's range,
  preserve accurate or shield-breaking tools for Brutes and Jackal marksmen,
  and recognise which clearance or interaction advances the authored route.
- Long-term structure: the mission alternates movement, staged combat,
  checkpoint safety and explicit rescue gates before one extraction settlement
  transfers authority to the successor mission.
- Common heuristics: withdraw immediately after shield break; reload behind
  cover; use Motion Tracker contacts as bearing rather than complete knowledge;
  inspect waypoints and prompts; do not confuse optional skull or equipment
  routes with the required rescue path.
- Failure attribution: empty ammunition, a rejected replacement, exposed
  shield recharge, unseen elevation, an uncleared required group and missed
  interaction are separately disclosed through HUD, local effects or route
  state; checkpoint restoration bounds repeated loss.
- Player-trust factors: weapon/ammunition state, shield status, tracker
  contacts, waypoint, prompt and checkpoint acceptance are visible before or
  immediately after the decisions they govern.
- Claim IDs: `H3-003`–`H3-012`.

## Replay and variation

- What changes between sessions: weapon pair, ammunition and grenade spending,
  dropped pickups, ally survival, enemy positioning, shield breaks, deaths and
  checkpoint timing.
- Randomness or procedural generation: the mission geometry, chapters,
  encounter regions, rescue and exit are authored; local AI movement and combat
  outcomes vary. No generated map or random objective is claimed.
- Multiple viable strategies: firefights allow different range, cover,
  weapon, grenade and melee choices, but Johnson's release, the final response
  and Pelican boarding remain the ordered terminal chain.
- Typical replay motive: higher difficulty, skulls, scoring, co-op, optional
  collectibles, achievements and alternate weapon routes are excluded modules.
- Claim IDs: `H3-003`–`H3-012`.

## Adjacent systems and history

- Direct predecessors: Halo and Halo 2 establish the series context, but this
  packet does not import their health, dual-wield, checkpoint or mission rules
  without Halo 3 evidence.
- Variants: Heroic, Legendary, skulls, co-op and scoring change damage,
  checkpoint pressure, actor count or evaluation; MCC and later
  backward-compatible builds are separate software/presentation boundaries.
- Similar games: DOOM (2016) shares direct real-time weapon combat, finite
  ammunition, triggered encounter groups and checkpoint restoration;
  STAR WARS Battlefront II (2017) shares a retained authored mission successor
  but regenerates health rather than a separate damage-first shield.
- Important differences: the visor Motion Tracker conceals elevation and
  stationary actors; shield recovery is automatic after safety rather than an
  item; the first mission ends by rescuing an ally and boarding transport, not
  by a boss defeat, score threshold or player-controlled vehicle route.
- Claim IDs: `H3-001`–`H3-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-341` | route, aim, weapon pair, reload, grenade and rescue/extraction interactions |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-348`, `SYS-369`, `SYS-749`, `SYS-780`, `SYS-913` | combat, pickup, layered damage, checkpoints, encounter groups, successor and shield recharge |
| Constraint | `CON-262`, `CON-282`, `CON-402`, `CON-578` | two weapons, grenade/ammunition caps, authored gates and required clearance |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-349` | loadout, local actors, shield, waypoint, prompts and Motion Tracker |
| Objective | `OBJ-183` | rescue Johnson and extract into the named successor |
| Time | `TIM-003` | continuous live mission state |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `314` (`GAME-0001`–`GAME-0314`).
- Exact genome matches: none.
- Tied near matches: `GAME-0253` — Titanfall 2 (`18 / 36 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0253` — Titanfall 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-341`, `SYS-215`, `SYS-222`, `SYS-369`, `SYS-780`, `CON-262`, `CON-282`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `TIM-003` | Both traverse an authored real-time campaign route with a two-weapon finite-ammunition loadout, grenade use, contextual gates, checkpoint return and retained successor control. Titanfall 2 adds high-mobility wall traversal, cloak and a staged allied-Titan restoration/control transfer; Halo 3 instead centres on replaceable world weapons, a separate damage-first rechargeable shield, partial allegiance-coded motion sensing, required finite encounter clearance and a captive-release-to-Pelican terminal. | Near, `0.500000` |

### Preserved research notes

- New genes: `SYS-913`, `INF-349`, `OBJ-183`.
- Classification result: `New gene`; the deterministic subset scan found no
  verified combination as a proper subset.
- Evidence and reasoning: existing combat, weapon, ammunition, authored-group,
  checkpoint and mission-transfer genes own compatible established boundaries.
  `SYS-730` is rejected because it owns an extra Overshield above ordinary
  Shield and Health; Halo 3 instead recharges its ordinary damage-first shield.
  `INF-311` is rejected because Alien: Isolation's sensor must be raised and
  reports anonymous direction/distance, while Halo 3's always-present visor
  tracker reports moving/firing contacts with allegiance but no elevation.
  No existing objective joins captive release, mandatory counterattack,
  extraction boarding and retained named successor.

## Taxonomy impact

- Registry changes: add one System Behaviour, one Information and one
  Objective boundary; add Halo 3 support to twenty-three compatible existing
  genes.
- Taxonomy-change record: none; no earlier definition or signature changes.
- Candidate terms affected: Halo 3, Xbox 360, Standard Edition, Master Chief,
  Sierra 117, Walk It Off, Charlie Foxtrot, Quid Pro Quo, Sergeant Johnson,
  the Arbiter, Covenant, Pelican, Crow's Nest, Normal, Motion Tracker and all
  weapon/enemy labels remain product or instance parameters.

## Negative results

- No original Xbox 360 build, disc-region inspection, direct control, death,
  checkpoint reload, save/quit/relaunch or successor-load comparison was
  available. The checkpoint and continuation boundaries are source-backed,
  not measured local persistence equality.
- Player-controlled vehicles are rejected: the scoped Pelican is only an
  interaction and authored extraction transition. Dual wield, equipment,
  skulls, scoring, terminals and optional collectibles are excluded rather
  than inferred from their availability elsewhere in Halo 3.
- `SYS-730` and `INF-311` do not fit the ordinary shield and passive visor
  tracker. `SYS-737` does not fit because it regenerates one health pool rather
  than a separate shield. `OBJ-166` does not fit because Sierra 117's terminal
  requires rescue and boarding rather than merely eliminating a declared force.

## Delta summary

## New facts

- [Observation | Corroborated | High] The original Halo 3 HUD joins a primary/
  reserve weapon pair, finite typed grenades, a damage-first rechargeable
  shield, partial Motion Tracker contacts, waypoint and checkpoint feedback
  (`H3-003`–`H3-008`).
- [Observation | Corroborated | High] `Sierra 117` closes only after Johnson's
  release, the required response and Pelican boarding into the named
  `Crow's Nest` continuation (`H3-009`–`H3-012`).

## New genes

- [Observation | Corroborated | High] `SYS-913`, `INF-349` and `OBJ-183`
  isolate ordinary-shield recharge, the passive allegiance-coded motion
  tracker and the rescue-to-successor mission terminal.

## New combinations

- None. No verified combination is a proper subset of this 26-gene signature.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary or signature
  changed.

## New questions

- Which exact weapon, ammunition, grenade, ally and checkpoint fields survive
  an original Xbox 360 save/quit/relaunch at each Sierra 117 checkpoint?
- Does the final retail disc without title updates differ from later original-
  game title updates in any scoped solo Normal checkpoint condition?

## Next recommended game

- [Hypothesis | Limited | Medium] No next ID is reserved. Battletoads, Contra
  Force and one region-specific original PlayStation Gran Turismo release
  remain future audience-priority candidates.
- Optimisation criterion: begin a new reviewed nine-game horizon only after
  choosing edition-specific, legally accessible subjects and platform balance.
- Expected information gain: compare legacy co-op action, NES run-and-gun and
  licensed circuit racing against the now-complete 307–315 platform contrast.
- Backlog impact: closes unit 9/9; no later game starts implicitly.

## Why this game

- [Hypothesis | Limited | Medium] Halo 3 adds a culturally recognisable legacy
  Xbox campaign packet whose shield safety rhythm, partial visor sensing and
  rescue-to-extraction terminal differ from prior modern shooters without
  importing MCC rules.

## Research checklist

- [x] exact platform, edition, source-bounded ruleset, mode and difficulty declared
- [x] primary loop, entry, positive terminal and exclusions declared
- [x] direct-play, build, checkpoint and reload limitations disclosed
- [x] shield, weapon, grenade, tracker, route and mission transitions sourced
- [x] vehicles, skulls, co-op, scoring and MCC overreach rejected
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
