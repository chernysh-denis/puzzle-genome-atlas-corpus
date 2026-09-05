---
game_id: GAME-0251
slug: hades
game_title: Hades
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0249
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-140
    - ACT-161
    - ACT-190
    - ACT-356
  system:
    - SYS-004
    - SYS-166
    - SYS-167
    - SYS-215
    - SYS-222
    - SYS-362
    - SYS-380
    - SYS-456
    - SYS-467
    - SYS-578
    - SYS-781
    - SYS-782
  constraint:
    - CON-175
    - CON-188
    - CON-269
    - CON-402
    - CON-596
  information:
    - INF-002
    - INF-119
    - INF-179
    - INF-305
    - INF-306
  objective:
    - OBJ-156
  time:
    - TIM-003
---

# Game: Hades

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1145360`, current one-app store package `415372` and public branch Build ID
  `10929685`, built 2023-04-04 and published 2023-04-12, checked 2026-09-05.
  The build identifier and dates are secondary distribution observations.
  This is the completed original **Hades**, not Early Access, Hades II, a
  console/mobile port, soundtrack, soundtrack bundle or mod.
- Entry: choose an unused save slot, ordinary New Game, English text and the
  default non-Hell rules. Keep God Mode off. The packet begins at the first
  controllable frame of the first escape attempt in Tartarus with the starting
  weapon, no purchased Mirror talent, no Keepsake, no unlocked alternative
  weapon and no prior attempt state.
- Primary decision loop: read current Life, ability and Boon state, visible
  hostiles/projectiles/traps and available chamber exits; navigate, use Attack,
  Special or Cast, or commit a directional protected Dash; clear every required
  enemy wave; claim the declared chamber reward; when a Boon appears, compare
  its eligible finite offer and commit one run-local modifier; when several
  exits open, compare their reward symbols and any elevated-risk marker before
  entering one; carry health, Obols, Boons, rewards and other admitted attempt
  state into the successor chamber; repeat until the attempt itself settles.
- Positive terminal: survive the boss-gated region chain, defeat the final
  escape guardian, accept the first clear/result transition, reach the first
  surface story visit and let the rules return Zagreus to the House of Hades.
  The first retained controllable House state after that return closes the
  successful branch. A room clear, regional boss, staircase, autosave, pause,
  quit or surface arrival before the resulting House return is not terminal.
- Negative terminal: Life reaches zero with no available revival, the death
  transition returns Zagreus through the Pool of Styx and the first retained
  controllable House state appears. The chamber graph, current Life, Obols and
  run-local Boon/build state are gone; eligible collected metaprogression
  resources and attempt/story state remain. This is the reproducible default
  evaluation branch: after at least one Boon choice, one complete combat-room
  settlement and one reward-preview exit choice, continue ordinary play and,
  if necessary, deliberately stop evading until lethal damage produces the
  formal death transition. No arbitrary room or elapsed-time stop is accepted.
- Included: one complete first fresh-save escape attempt; starting weapon;
  direct movement, Attack, Special, Cast and protected Dash; reusable Cast
  ammunition as a resource/readiness parameter; real-time enemy, projectile,
  trap and damage resolution; persistent attempt health; visible chamber
  state; finite enemy waves and exit locking; reward materialisation and
  collection; run-progress and metaprogression reward classes; Boon selection,
  prerequisites, exclusive core ability slots, rarity/level and triggered or
  passive effects; run-local Obols and an encountered Charon purchase; visible
  successor reward symbols; region guardians; death or first-clear settlement;
  transient-build reset and retained eligible first-attempt progression.
- Excluded: all later escape attempts; spending Darkness at the Mirror of
  Night; unlocking or changing Infernal Arms or Aspects; Keepsakes, Companions,
  gifting, relationships, House Contractor purchases, Wretched Broker trades
  and the Fated List; God Mode, Hell Mode, Pact of Punishment, Heat, Extreme
  Measures, Erebus and speedrun categories; fishing, cosmetics, achievements,
  exhaustive Codex or prophecy completion; later clears, ten-clear ending,
  epilogue and the complete story; seeded manipulation, Give Up replay,
  imported/cross-save state, mods, trainers, debug/console commands; Hades II,
  consoles, mobile, macOS and Linux/Proton.
- Reproducible parameterisation: preserve app, package, public build, Windows,
  English, the unused save slot, non-Hell New Game and God Mode off. During the
  attempt, use Attack, Special, Cast and Dash; fully settle at least one hostile
  chamber; claim its reward; commit one displayed Boon option; after a chamber
  exposes at least two successor doors, record both reward symbols and select
  one; preserve a current-room and post-transition state record; and continue
  to the game's own death or first-clear House return. Exact seed, room layout,
  enemy set, Boon identities, rarities, reward symbols, branch, shop presence,
  purchase, damage, healing, Obols, metaprogression quantities, regional reach
  and duration are attempt parameters. If no shop appears before terminal,
  `ACT-130` remains a documented legal branch rather than a fabricated trace.
- Potential scoped modules: one later Mirror-prepared attempt; one named
  weapon/Aspect; one successful clear; one Pact/Heat configuration; one fixed
  regional chamber packet; the ten-clear ending; epilogue; God Mode; Hell Mode;
  or a named non-Windows build each requires a separate analysis.
- Direct-play status: not conducted. Valve and Supergiant material establishes
  lawful availability, completed release, solo action, distinct escape
  attempts, changing divine builds and permanent progression. Static written
  rules references establish first-save entry, starting weapon, controls,
  room/reward transitions, Boon eligibility, health, death, successful escape
  and House return. This is an evidence-backed rules reconstruction, not a
  claimed playthrough or entitlement. No video or audio was opened, played,
  heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HADES-001` | The selected product is the completed single-player English Windows Steam app `1145360` in one-app package `415372`, not Hades II or Early Access | Confirmed | Direct | High | P1–P4 |
| `HADES-002` | Steam public Build `10929685` is the current observed Windows distribution state | Observation | Corroborated | High | P1, S1 |
| `HADES-003` | An unused slot immediately begins a first escape attempt; ordinary New Game is fixed to non-Hell rules with God Mode off and no imported progression | Observation | Corroborated | High | P3, S2, S3 |
| `HADES-004` | The starting weapon supports direct Attack and Special, while Zagreus also has Cast and a freely timed directional Dash with a protected interval | Confirmed | Corroborated | High | P3, P5, S3, S4 |
| `HADES-005` | Hostile chambers resolve in real time through finite waves; complete clearance opens successor access and produces the declared chamber reward | Confirmed | Corroborated | High | P5, S5, S6 |
| `HADES-006` | Eligible successor doors preview reward class and elevated encounter risk before the player commits a route | Confirmed | Corroborated | High | P5, S5 |
| `HADES-007` | A Boon presents a bounded eligible choice whose displayed effect, rarity/level and affected capability shape the current attempt build | Confirmed | Corroborated | High | P3, P5, S7 |
| `HADES-008` | Core Attack, Special, Cast, Dash and Call Boon slots are exclusive, and first-attempt eligibility removes later exchange and metaprogression options | Observation | Corroborated | High | P5, S7, S8 |
| `HADES-009` | Current Life, Obols, Boons and admitted reward state persist from chamber to chamber; Life zero without revival formally ends the attempt | Confirmed | Corroborated | High | P3, S9, S10 |
| `HADES-010` | Defeating each regional guardian admits the next region; the final guardian and surface story transition define first-clear success | Observation | Corroborated | High | P3, S5, S11, S12 |
| `HADES-011` | Death or successful surface closure returns control to the House, clears chamber and run-build state, and retains eligible metaprogression resources plus attempt/story progress | Confirmed | Corroborated | High | P3, P5, S2, S9–S13 |
| `HADES-012` | One complete attempt is the bounded ruleset; a chamber clear, regional boss, quit or arbitrary stop does not settle that unit | Strong Pattern | Corroborated | High | `HADES-003`–`HADES-011` |

## Basic data

- Release / origin: developed and published by Supergiant Games; Hades v1.0
  left Early Access and launched on Steam on 2020-09-17.
- Platform or physical form: lawfully available single-player English Windows
  Steam client, app `1145360`, package `415372`; one fresh-save attempt.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  branching risk-route selection; run-local build composition and
  multi-encounter resource attrition.
- Primary and official sources, accessed 2026-09-05:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=1145360&cc=ua&l=english),
    for current title, developer/publisher, release, Windows support, product
    description and store availability.
  - `P2` — [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=415372&cc=ua&l=english),
    for current package availability and its sole `1145360` application.
  - `P3` — [Supergiant Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/),
    for the completed v1.0 boundary, Steam availability, single-player scope,
    combat-oriented randomized runs, changing divine builds, permanent
    progression and separate God, Hell and Pact difficulty systems.
  - `P4` — [official Hades page](https://www.supergiantgames.com/games/hades/),
    for the original game's product identity and escape premise.
  - `P5` — [Supergiant latest Hades updates](https://www.supergiantgames.com/blog/hades-updates/),
    for the current completed-update line, escape-attempt records, opening
    attempt transition, chamber/region presentation and v1.0 result surfaces.
  - `P6` — [Supergiant Big Bad patch notes](https://www.supergiantgames.com/blog/hades-big-bad-update-patch-notes/),
    for chamber-door unlock after encounter clearance, Boon exchange language,
    Death Defiance healing and the final-battle boundary.
  - `P7` — [Supergiant Welcome to Hell patch notes](https://www.supergiantgames.com/blog/hades-welcome-to-hell-update-patch-notes/),
    for first-attempt exclusions, chamber reward previews, first-run exchange
    restrictions, Cast-ammunition feedback and Boon/ability terminology.
- Corroborating textual sources, accessed 2026-09-05:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/1145360/depots/),
    for Windows depots and public Build `10929685`, built 2023-04-04 and
    published 2023-04-12. SteamDB is a secondary distribution mirror.
  - `S2` — [Saving Your Progress](https://hades.fandom.com/wiki/Saving_your_Progress),
    for unused save slots, Hell Mode selection, autosave boundaries, Quit/Give
    Up distinction and seed continuity.
  - `S3` — [How to Play](https://hades.fandom.com/wiki/How_to_play_guide_for_Hades),
    for Windows controls, Attack, Special, Cast, Dash and run-build decisions.
  - `S4` — [Gameplay Mechanics](https://hades.fandom.com/wiki/Gameplay_mechanics),
    for the capability set, Cast token and protected Dash resolution.
  - `S5` — [Chambers and Encounters](https://hades.fandom.com/wiki/Chambers_and_Encounters),
    for wave closure, reward previews, risk markers, chamber rewards, exits and
    region ordering.
  - `S6` — [Chamber Reward](https://hades.fandom.com/wiki/Chamber_Reward),
    for first-chamber and later reward sampling and run/meta reward classes.
  - `S7` — [Boons](https://hades.fandom.com/wiki/Boons), for run lifetime,
    offer effects and exclusive core ability slots.
  - `S8` — [first-attempt Patch 034 reference](https://hades.fandom.com/wiki/Patch_034),
    for later-system exclusions from the very first attempt.
  - `S9` — [Health](https://hades.fandom.com/wiki/Health), for persistent Life,
    healing, zero-Life death and House revival.
  - `S10` — [House of Hades](https://hades.fandom.com/wiki/House_of_Hades),
    for the Pool of Styx return and retained escape-attempt records.
  - `S11` — [Tartarus](https://hades.fandom.com/wiki/Tartarus), for first-region
    placement and boss-gated continuation.
  - `S12` — [Temple of Styx](https://hades.fandom.com/wiki/Temple_of_Styx), for
    the final-region route and final-guardian escape transition.
  - `S13` — [Greece](https://hades.fandom.com/wiki/Greece), for the first
    surface visit and rules-mandated return to the House.
- Claim IDs: `HADES-001`–`HADES-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate Zagreus within a chamber and through a
  selected exit; `ACT-161`: aim and commit the starting weapon's Attack;
  `ACT-190`: activate Special or Cast with its current target/resource state;
  `ACT-356`: commit a freely timed directional Dash and its protected movement.
- Existing `ACT-140`: commit one option from a bounded Boon offer for the
  current attempt; `ACT-130`: spend run-local Obols on one currently offered
  Charon asset when that optional branch occurs.
- Character, weapon, god, Boon, rarity, effect, chamber, enemy, direction,
  target, Cast token, Obol price and control binding are parameters. Claims:
  `HADES-004`–`HADES-009`.

### System Behaviour Genes

- Existing `SYS-004`: select unresolved chamber, enemy, reward and Boon-offer
  outcomes from first-attempt eligible pools; `SYS-215`: resolve directly
  commanded live combat; `SYS-380`: resolve Special and Cast into their typed
  current effects; `SYS-456`: move the Dash and ignore eligible damage overlap
  during its protected interval; `SYS-578`: apply damage and compatible healing
  to one continuous attempt health pool.
- Existing `SYS-362`: convert complete encounter clearance or an authorised
  reward source into its reward before traversal resumes; `SYS-222`: transfer
  compatible spatial drops/resources on collection; `SYS-167`: carry health,
  Obols, Boons, reward state and ability readiness across resolved chambers;
  `SYS-166`: trigger retained Boon effects at their declared combat, damage,
  reward, movement or chamber events; `SYS-467`: compose accepted Boons and
  compatible upgrades into the current disposable attempt build.
- New `SYS-781`: advance the same attempt through boss-gated regions toward
  the scoped escape; `SYS-782`: at death or first-clear closure, discard the
  transient chamber/build state and return control to the persistent hub while
  retaining eligible metaprogression and attempt/story state.
- Resolution order: sample current chamber state; expose local hazards and
  successor reward information; accept movement, attack, ability, Dash, Boon
  or purchase input; validate resource, target and offer eligibility; resolve
  live combat, damage and modifier triggers; settle all waves; expose and grant
  the chamber reward; carry admitted state into one chosen successor; advance
  boss-gated regions; then settle death or first clear into retained House
  control. Claims: `HADES-004`–`HADES-012`.

### Constraint Genes

- Existing `CON-269`: Special and Cast require compatible target, Cast token,
  readiness and current state; `CON-402`: successor exits remain unavailable
  until the chamber's finite required waves are cleared; `CON-175`: health loss
  persists between chambers and zero without revival terminates the attempt;
  `CON-188`: each finite Boon offer permits one persistent attempt choice.
- New `CON-596`: a run-modifier offer may contain only options whose
  prerequisites and exclusive capability-slot rules are legal for the current
  build; first-attempt exclusions are part of this eligibility state.
- Scarce strategic resources: Life, Cast availability, Dash readiness and safe
  space; Obols and purchase opportunities; compatible Boon slots, reward and
  upgrade opportunities; region depth and the remaining attempt. Exact numeric
  values, identities and frequencies are parameters. Claims:
  `HADES-004`–`HADES-010`.

### Information Genes

- Existing `INF-179`: the current chamber exposes Zagreus, enemies,
  projectiles, traps, obstacles, drops and exit states; `INF-119`: Life, Cast
  state, Obols, current Boons/levels and ability readiness are inspectable;
  `INF-002`: exact future chambers, enemies, rewards and offers stay unknown.
- New `INF-305`: each available successor exit previews its chamber reward
  class and any elevated-risk marker before route commitment; `INF-306`: the
  Boon offer exposes each choice's effect, rarity/level, affected capability
  and any replacement consequence needed to attribute the build choice.
- Exact HUD position, symbol, wreath, colour, icon art, font and effect
  animation are presentation parameters. Claims: `HADES-005`–`HADES-010`.

### Objective Genes

- New `OBJ-156`: carry one ordinary boss-gated escape attempt from its first
  chamber through the final guardian before terminal health loss, then let the
  result return to the persistent hub. Success is first retained House control
  after the first surface visit; formal death and retained House control is the
  bounded failure settlement. Claims: `HADES-009`–`HADES-012`.

### Time Genes

- Existing `TIM-003`: navigation, enemies, projectiles, traps, attack windows,
  Dash protection and damage progress in real time. Boon choice, menus and
  authored transitions may pause that flow but do not convert the attempt to
  turns. Claims: `HADES-004`–`HADES-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An unused slot has no attempt history | Choose ordinary New Game with Hell and God Mode off | First controllable Tartarus attempt begins with starting weapon and no imported Mirror, weapon or Keepsake progression | exact entry and incoming persistent state | `HADES-003` |
| A hostile attack or projectile is approaching and Dash is ready | Commit a direction before overlap | Zagreus moves along the declared Dash path and eligible overlap during its protected interval does not remove Life | freely timed protected repositioning | `HADES-004` |
| One Cast token is ready and a reachable hostile is present | Aim and Cast | The projectile applies its current effect and the token becomes unavailable until its legal release/recovery | typed ability resource, not an unlimited basic attack | `HADES-004` |
| A chamber has living required enemies or an unfinished wave | Defeat the visible set and any declared reinforcements | Live attacks, abilities and hazards resolve; only complete wave closure changes the chamber to cleared and admits its reward/exit state | finite room clearance gate | `HADES-005` |
| A god reward has materialised after clearance | Interact and inspect the finite offer | Eligible options expose effect and rarity/level; one committed choice persists in the current attempt and unselected alternatives close | informed exclusive build choice | `HADES-007`, `HADES-008` |
| A retained Boon matches a later Attack, Dash, damage or reward event | Trigger that event | The Boon's declared passive or triggered modifier composes with current weapon/ability state | Boons are rule changes rather than score labels | `HADES-007`–`HADES-009` |
| Two successor exits are open after reward settlement | Compare their symbols and enter one | The chosen symbol fixes the next admitted reward class; the unchosen branch is left behind and future contents remain undisclosed | previewed route commitment under uncertainty | `HADES-006` |
| Charon offers an affordable run asset in an encountered shop | Purchase one displayed option | Current Obols fall by the shown price and the selected health, Boon or run benefit changes the attempt; unaffordable options remain unavailable | optional run-local economy | `HADES-009` |
| A regional guardian has been defeated and its reward settled | Enter the admitted region transition | The same Life, Obols and run build continue into the next region rather than forming a new attempt | boss-gated multi-region continuity | `HADES-009`, `HADES-010` |
| Life reaches zero with no available revival before escape | Let the death transition settle | Current chamber, health, Obols and Boon build are removed; Zagreus emerges in the House while eligible collected meta resources and attempt/story state remain | formal reproducible negative terminal | `HADES-009`, `HADES-011`, `HADES-012` |
| The final guardian falls on a possible first-attempt clear | Accept the result and complete the first surface visit | First-clear state settles; the surface story closes and returns Zagreus to retained House control | success branch and common terminal locus | `HADES-010`–`HADES-012` |

## Strategic and experiential structure

- Planning horizon: preserve Life and safe movement while choosing visible
  successor reward classes and Boons that reinforce a coherent Attack,
  Special, Cast or Dash plan before later region pressure rises.
- Local tactics: read projectile and trap geometry, use ordinary movement for
  spacing, Dash through eligible attack intervals, alternate direct Attack with
  resource/readiness-bound Special or Cast, and close each finite enemy wave.
- Medium-term structure: every room clear turns immediate execution into a
  reward/build decision; carried damage and build state make the next door's
  visible reward more or less valuable; guardians gate later regions without
  resetting the attempt.
- Reversible versus irreversible: local motion and aim remain revisable; damage,
  spending, accepted Boons, collected rewards and abandoned door alternatives
  alter the attempt; death or clear discards the transient build but retains
  eligible hub progression.
- Failure attribution: current room threats, Life/readiness, door symbols and
  fully described Boon offers separate execution, route, resource and build
  errors while future random contents remain honestly hidden.
- Player trust: a reward symbol must describe the reward class before entry;
  a Boon must disclose its effect before commitment; exit locking must end only
  after the finite required wave; and both formal terminal branches must return
  to the House with the declared transient/persistent split. Claims:
  `HADES-004`–`HADES-012`.

## Replay and variation

- What changes between attempts: seed, chamber layouts, enemies, reward doors,
  Boon gods/options/rarities, shops, purchases, health route, build synergies,
  region reach, terminal cause and story events.
- Randomness or procedural generation: eligible pools sample chambers,
  encounters, rewards and offers, while door previews disclose the next reward
  class but not complete successor contents.
- Multiple viable strategies: Attack-, Special-, Cast- and Dash-centred builds,
  safer meta-reward routes, immediate run-power routes and Obol/shop choices
  trade current survival against later attempt or hub value.
- Typical replay motive: adapt another temporary build, reach a later region,
  unlock permanent options or advance remembered story. Only the first attempt
  and its first House return enter this unit.
- Claims: `HADES-003`–`HADES-012`.

## Adjacent systems and history

- Direct product corridor: Hades v1.0 is a completed standalone game. Hades II,
  Early Access history, ports, soundtrack products and later save history do
  not enter this Windows first-attempt packet.
- Selection comparison corridor: The Binding of Isaac: Rebirth also carries a
  disposable random action build through locked combat rooms and boss-gated
  stages; Slay the Spire carries health and modifiers through a previewed
  branching route but resolves cards in turns; Vampire Survivors converts
  spatial XP into paused build drafts on an authored stage clock; Loop Hero
  carries equipment/resources along an autonomous fixed circuit and offers a
  voluntary risk-sensitive retreat.
- Important differences: Hades combines direct Attack/Special/Cast/Dash combat,
  reward-labelled successor doors, ability-slot-compatible divine offers and a
  common House return after either death or surface success. Isaac explores a
  generated floor graph with keys/bombs and pedestal items; Slay exposes an act
  map and deck; Vampire Survivors automates weapons; Loop Hero automates both
  locomotion and combat. Claims: `HADES-004`–`HADES-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-190`, `ACT-356` | controls, target, Boon, route, purchase and Dash values |
| System Behaviour | `SYS-004`, `SYS-166`, `SYS-167`, `SYS-215`, `SYS-222`, `SYS-362`, `SYS-380`, `SYS-456`, `SYS-467`, `SYS-578`, `SYS-781`, `SYS-782` | seed, combat, reward, build, health, region and terminal values |
| Constraint | `CON-175`, `CON-188`, `CON-269`, `CON-402`, `CON-596` | Life, ability, wave, offer, prerequisite and slot values |
| Information | `INF-002`, `INF-119`, `INF-179`, `INF-305`, `INF-306` | room, HUD, door-preview and Boon-offer presentation |
| Objective | `OBJ-156` | attempt entry, guardians, escape, death and House return |
| Time | `TIM-003` | continuous chamber simulation and paused offer surfaces |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `250` (`GAME-0001`–`GAME-0250`).
- Exact genome matches: none.
- Tied near matches: `GAME-0164` — The Binding of Isaac: Rebirth (`14 / 44 = 0.318182`).
- Supported combination subsets: `COMB-0249`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0164` — The Binding of Isaac: Rebirth | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-190`, `SYS-004`, `SYS-215`, `SYS-222`, `SYS-467`, `CON-175`, `CON-402`, `INF-002`, `INF-119`, `INF-179`, `TIM-003` | Both directly navigate and attack through locked random rooms, carry finite health and a disposable build, spend run currency and conceal later content. Isaac exposes an explored floor graph and prices access with keys/bombs while cumulative pedestal items lead to the first Mom ending; Hades adds protected directional Dash, typed abilities, reward-labelled successor doors, compatible one-of-many Boon offers, boss-gated regions and a common House return retaining meta resources/story state after either death or escape. | Near, `0.318182` |

### Preserved research notes

- New genes: `SYS-781`, `SYS-782`, `CON-596`, `INF-305`, `INF-306` and
  `OBJ-156`.
- Reused genes: `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-190`,
  `ACT-356`, `SYS-004`, `SYS-166`, `SYS-167`, `SYS-215`, `SYS-222`,
  `SYS-362`, `SYS-380`, `SYS-456`, `SYS-467`, `SYS-578`, `CON-175`,
  `CON-188`, `CON-269`, `CON-402`, `INF-002`, `INF-119`, `INF-179` and
  `TIM-003`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing live movement/combat, Dash, ability,
  continuous health, chamber reward, run-state carry, modifier trigger and
  random outcome boundaries transfer without game-specific labels. New terms
  isolate the portable region progression, hub-retained terminal split,
  capability-slot offer legality and two distinct information contracts.
- Lower-ID scan: reject `SYS-464`, because Hades samples a forward chamber
  chain rather than an explorable floor graph; reject `SYS-465`, because the
  chamber reward is previewed before entry rather than first sampled at
  clearance; reject `SYS-468`, because its reviewed floor/trapdoor ending does
  not cover a four-region escape and House return; reject `SYS-469`, because
  Hades retains collected metaprogression currency and attempt/story state, not
  only eligible save unlocks; reject `SYS-575`/`SYS-576`, because a Boon offer
  is reward-triggered and capability-slot-compatible rather than caused by an
  XP level and weapon/passive cap; reject `INF-180`, because future Hades
  chambers are not retained as an explored room graph; reject `OBJ-091`,
  because Mom/Depths/Epilogue are game-scoped parameters, not a portable escape
  objective. Cast-token identity and exact reward values remain parameters of
  `ACT-190`, `CON-269`, `SYS-380` and `SYS-362`, not quest-item genes.

## Taxonomy impact

- Registry changes: six new Active genes; one reused definition (`SYS-467`) is
  broadened from a pedestal-only instance to its already portable run-build
  label and now cites both supporting games. No lifecycle state or earlier
  reviewed signature changes.
- Taxonomy-change record: none; this is additive game-unit taxonomy work.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Hades, Zagreus,
  Tartarus, House of Hades, Pool of Styx, Charon, Mirror of Night, Infernal
  Arms, God Mode, Hell Mode, Pact of Punishment, Heat, Boon, Obol and named
  gods, weapons, regions, rewards and numeric values remain product,
  interface or game-scoped parameters.

## Negative results

- No direct-play, local-entitlement, screenshot, video or audio claim.
- No later attempt, Mirror, weapon, Keepsake, relationship, House economy,
  Pact/Heat, God/Hell, whole-story, Hades II, platform or live-history union.
- No earlier reviewed signature or lifecycle state changes. The generic
  `SYS-467` wording correction preserves every earlier carrier's meaning.

## Combination subset scan

- Every verified combination in the pre-unit registry is tested as a proper
  subset of this 30-gene signature; none of the 248 earlier combinations fits
  completely. `COMB-0249` records the strict eighteen-gene direct-combat,
  Boon-build, previewed-door, region and hub-settlement core; it omits generic
  purchase, spatial pickup, encounter-loot, typed-ability resolution, random
  future information and detailed room-state support.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current Windows product/package availability,
  completed v1.0/solo boundaries and official attempt/build systems are fixed
  in `HADES-001`–`HADES-003` and `HADES-007`–`HADES-011`.
- [Observation | Corroborated | High] First-attempt entry, chamber transitions,
  Boon eligibility, region sequence and common House terminal are fixed in
  `HADES-003`–`HADES-012`.

## New genes

- [Observation | Corroborated | High] `SYS-781` advances one carried build
  through boss-gated regions; `SYS-782` separates discarded attempt state from
  retained hub metaprogression; `CON-596` gates offered run modifiers by
  prerequisites and exclusive capability slots.
- [Observation | Corroborated | High] `INF-305` previews reward/risk on
  successor exits; `INF-306` exposes complete build-choice consequences;
  `OBJ-156` fixes the multi-region escape-versus-health attempt objective.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0249` captures direct protected
  action combat whose cleared rooms produce compatible temporary build choices
  and reward-previewed branches, carrying health/build through guardians until
  death or escape returns to a progression-retaining hub.

## Taxonomy changes

- [Observation | Corroborated | High] `SYS-467` now states the portable
  run-local upgrade meaning already implied by its label; no prior signature or
  carrier interpretation changes.

## New questions

- Does the next branching-narrative packet replace run-local build and
  execution pressure with authored evidence/state choices while retaining a
  formally reloadable chapter terminal?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0252` — Detroit: Become Human.
- Optimisation criterion: preserve visible consequences, alternate routes and
  a retained terminal while changing live chamber/build adaptation into one
  authored chapter's evidence, dialogue and action branches.
- Expected information gain: distinguish complete attempt settlement from a
  chapter flowchart and retained story state without merging later chapters.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Detroit: Become Human can hold bounded
  consequence attribution near-constant while replacing Hades' random room
  rewards, temporary build and death-return loop with authored investigative
  and dialogue branches inside one chapter.
