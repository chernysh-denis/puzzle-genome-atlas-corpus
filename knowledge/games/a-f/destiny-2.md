---
game_id: GAME-0193
slug: destiny-2
game_title: Destiny 2
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0191
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-190
    - ACT-215
    - ACT-341
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-348
    - SYS-380
    - SYS-605
    - SYS-623
    - SYS-624
  constraint:
    - CON-262
    - CON-269
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-247
  objective:
    - OBJ-116
  time:
    - TIM-003
---

# Game: Destiny 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official Windows Steam client at Update `9.7.0.4`,
  Steam public build `24238629` and Bungie manifest
  `244213.26.06.29.2000-1-bnet.65583`; one direct-launched **Fireteam Ops / The
  Devil's Lair / Customize / Normal** run with no player-selected modifiers and
  one player in the supported `1–3` participant envelope.
- Fixed character and loadout: Titan / Void with Sentinel Shield, Towering
  Barricade, Catapult Lift, Shield Throw and Vortex Grenade; Common Khvostov
  7G-02 in the first slot, Common Stubborn Oak in the second and Uncommon
  Butler RS/2 in the Power slot. The three current manifest items must already
  be legally owned; perks, armour statistics and cosmetic state are parameters.
- Primary decision loop: read the objective marker, radar, score and nearby
  threats; move to cover or a legal firing angle; aim, fire, switch, reload or
  spend a ready Void ability; collect reachable ammunition; activate the mesh
  generator; survive its waves; defeat the Walker and later Sepiks Prime; then
  accept activity completion, grade and the terminal reward chest.
- Entry and exit: begins when the fixed solo Normal customization is launched
  from Fireteam Ops and first Guardian control appears in the Cosmodrome.
  Success is Sepiks Prime defeated, ordinary activity-complete state issued and
  the end chest/result admitted. The post-activity Director, inventory
  inspection and another launch are outside the terminal.
- Included: first-person navigation; the fixed three-weapon loadout, magazines
  and reserves; aiming, critical/body hits, switching and reloading; the fixed
  Void abilities and readiness; shield/health damage; ammunition bricks; local
  radar, team/objective/score HUD and result grade; Ghost terminal interaction;
  the authored mesh-defence, Walker and Sepiks sequence; Restricted Zone solo
  checkpoint restart; current Normal `B` / Tier-1 settlement and end chest.
- Excluded: matchmaking and human teammates; revive-token economy; Quickplay,
  Advanced–Ultimate, selected modifiers, time-bonus optimisation and farming;
  every other Op, strike, destination and campaign; PvP, Gambit, raids,
  dungeons, patrol, seasonal/event content, expansion stories, Guardian Rank,
  Power grind, vendor/account reward unions, random perk catalogues, Exotic
  gear, build crafting, monetisation, legacy rules and live-service history.
- Potential scoped modules: one three-human matchmade Fireteam Op; one
  modifier-bearing higher difficulty with revive tokens; one raid encounter;
  or one current PvP ruleset.
- Direct-play status: no authenticated current PC run was conducted. Bungie's
  current update, help guides and live manifest directly establish the version,
  entry envelope, item/ability legality, free-access systems, scoring and
  terminal. Maintained route and Restricted Zone references corroborate the
  exact encounter order and wipe transition; the repository trace is rules
  reasoning, not a claim of direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `D2-001` | The current service boundary is Update `9.7.0.4`; the live manifest version and Steam public build are pinned above | Confirmed | Direct | High | P1, P2, S1 |
| `D2-002` | The current manifest contains a non-playlist `The Devils' Lair: Customize` activity that permits one to three participants | Confirmed | Direct | High | P2 |
| `D2-003` | Arc, Solar, Void and Stasis subclasses plus the current Ops/Portal system are available to all players after their required unlock path | Confirmed | Direct | High | P3, P4 |
| `D2-004` | The fixed Titan abilities and three named weapon items remain legal current manifest objects in their declared slots and ammunition classes | Confirmed | Direct | High | P2, P5 |
| `D2-005` | Direct movement, weapon combat, reload/resource pressure and typed abilities remain the activity's continuous decision layer | Confirmed | Direct | High | P5, P6 |
| `D2-006` | The route requires mesh-generator activation and defence, a Walker encounter and Sepiks Prime defeat before the end chest | Observation | Corroborated | High | P7, S2, S3 |
| `D2-007` | A solo defeat in the route's Restricted Zone restores the current authored checkpoint rather than completing the activity | Observation | Corroborated | Medium | S2, S4 |
| `D2-008` | Current Normal maps to grade `B` and Tier-1 rewards; activity scoring is shared and the result is settled after objective completion | Confirmed | Direct | High | P6, P8, P9 |
| `D2-009` | The terminal is bounded at Sepiks defeat, activity completion and the reward chest, not later inventory or account progression | Confirmed | Corroborated | High | P6, P8, S3 |

## Basic data

- Release / origin: Bungie; Destiny 2 first released in 2017; scoped live
  service at Update `9.7.0.4` on 2026-08-29.
- Platform or physical form: online Windows PC software through Steam, direct-
  launched in one-player Fireteam Ops customization.
- Puzzle family: authored cooperative-shooter activity played solo, joining
  live weapon/ability resource timing to ordered encounter gates and a scored
  reward terminal.
- Primary sources:
  - `P1` — [Bungie Destiny Server and Update Status](https://help.bungie.net/hc/en-us/articles/360049199271-Destiny-Server-and-Update-Status),
    naming Update `9.7.0.4` on 2026-07-28, checked 2026-08-29.
  - `P2` — [Bungie Destiny 2 manifest endpoint](https://www.bungie.net/Platform/Destiny2/Manifest/)
    and its current English `DestinyActivityDefinition` /
    `DestinyInventoryItemDefinition` components, checked 2026-08-29; activity
    hash `3610118907` is `The Devils' Lair: Customize`, non-matchmade,
    non-playlist, minimum one and maximum three players.
  - `P3` — [Bungie Available Content guide](https://help.bungie.net/hc/en-us/articles/44243991218196-Available-Content-Expansions-Seasons-and-More),
    current free-access content and subclasses, checked 2026-08-29.
  - `P4` — [Bungie current Update 9.7.0](https://www.bungie.net/7/en-us/News/Article/destiny_update_9_7_0),
    current Ops location and difficulty/grade/reward rules, checked 2026-08-29.
  - `P5` — [Bungie Guardian, Subclasses, Abilities and Gear guide](https://help.bungie.net/hc/en-us/articles/45080200239892--3-Your-Guardian-Subclasses-Abilities-and-Gear),
    class abilities, weapon slots, ammunition and Ghost functions, checked
    2026-08-29.
  - `P6` — [Destiny 2 Steam product page](https://store.steampowered.com/app/1085660/Destiny_2/),
    current title, platform, free-to-play status, combat and strike chest,
    checked 2026-08-29.
  - `P7` — [Bungie Update 9.1.5.4](https://www.bungie.net/7/en/News/Article/destiny_update_9_1_5_4),
    current-era Devil's Lair scoring registration, checked 2026-08-29.
  - `P8` — [Bungie Update 9.1.0.1](https://www.bungie.net/7/en/News/Article/destiny_update_9_1_0_1),
    Devil's Lair activity timer and two end-activity engrams, checked 2026-08-29.
  - `P9` — [Bungie Destiny 2 Activities guide](https://help.bungie.net/hc/en-us/articles/360048720992-Destiny-2-Activities),
    strike objectives, encounter pressure and end rewards, checked 2026-08-29.
- Secondary sources:
  - `S1` — [SteamDB Destiny 2 depots](https://steamdb.info/app/1085660/depots/),
    public Windows build `24238629`, checked 2026-08-29.
  - `S2` — [Destinypedia Devil's Lair walkthrough](https://www.destinypedia.com/The_Devils%27_Lair_%28strike%29/Walkthrough),
    mesh defence, Darkness Zone, Walker and Sepiks route, checked 2026-08-29.
  - `S3` — [Destiny 2 Wiki Devil's Lair](https://d2.destinygamewiki.com/wiki/The_Devils%27_Lair),
    current D2 encounter and end chest, checked 2026-08-29.
  - `S4` — [Destinypedia Darkness Zone](https://www.destinypedia.com/Darkness_Zone),
    solo/full-fireteam checkpoint reset, checked 2026-08-29.
- Claim IDs: `D2-001`–`D2-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the Titan through the authored 3D route;
  `ACT-161`, aim and attack with the active firearm or compatible melee;
  `ACT-164`, switch among the three carried weapon slots; `ACT-183`, reload a
  magazine; `ACT-190`, activate the fixed grenade, melee, class or Super
  ability; `ACT-215`, configure the fixed legal character/loadout before
  launch; `ACT-341`, activate the mesh terminal or open the admitted end chest.
- New genes: none; every player-issued command has an active generic boundary.
- Parameters: Titan, subclass components, weapon identity/slot, aim, target,
  magazine, reserve, ability, readiness, interaction object and route state.
- Claim IDs: `D2-004`–`D2-006`, `D2-009`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve aimed shots through obstruction, defence
  and hit region; `SYS-215`, resolve directly commanded real-time combat;
  `SYS-222`, transfer compatible ammunition bricks on contact; `SYS-348`, apply
  shield, health and defeated-state transitions; `SYS-380`, apply each legal
  Void ability's typed live effect; `SYS-605`, advance the authored activity
  through terminal, defence and combat gates.
- New genes: `SYS-623`, settle Sepiks defeat and completed objectives into one
  activity score, grade and admitted reward chest; `SYS-624`, restore the most
  recent authored activity checkpoint when the solo Guardian is defeated in a
  Restricted Zone.
- Resolution order: launch the fixed activity; resolve movement, combat,
  ammunition and abilities continuously; activate and clear the mesh defence;
  clear the Walker gate; enter and defeat Sepiks; issue completion; calculate
  score/grade and admit the end chest. A legal solo wipe restores the current
  checkpoint without issuing completion.
- Claim IDs: `D2-005`–`D2-009`.

### Constraint Genes

- Existing genes: `CON-262`, the three weapon slots, magazine/reserve and heavy
  ammunition are finite; `CON-269`, each ability requires its legal target,
  range, resource/charge and readiness.
- New genes: none. Normal difficulty, the solo participant count, fixed gear
  and no selected modifiers are entry parameters rather than reusable
  continuation predicates.
- Claim IDs: `D2-002`, `D2-004`, `D2-005`.

### Information Genes

- Existing genes: `INF-073`, expose active weapon, slots and ammunition;
  `INF-115`, expose only locally visible/audible hostile state; `INF-116`,
  expose activity score and current objective/phase; `INF-119`, expose the
  Titan's shield/health, build and ability readiness.
- New gene: `INF-247`, expose current Ops difficulty and projected grade before
  launch, then completion score, time contribution, final grade, reward tier
  and chest admission after the activity.
- Claim IDs: `D2-004`, `D2-005`, `D2-008`, `D2-009`.

### Objective Genes

- New gene: `OBJ-116`, complete one solo Normal Devil's Lair Fireteam Op by
  clearing its authored gates, defeating Sepiks Prime and reaching ordinary
  activity-complete / end-chest state.
- Success, evaluation and failure: Sepiks defeat plus completion/chest
  admission is success; mesh defence, Walker defeat and boss damage are
  intermediate. A Restricted Zone wipe restarts a checkpoint and therefore
  fails that attempt segment without becoming the positive terminal.
- Claim IDs: `D2-006`–`D2-009`.

### Time Genes

- Existing gene: `TIM-003`, the Titan, hostiles, projectiles, ability readiness,
  objective pressure and activity score evolve while input remains available.
- Claim IDs: `D2-005`–`D2-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current Fireteam Ops customization is open | Select The Devil's Lair, Normal, no player-selected modifiers and launch solo with the pinned Titan/loadout | Manifest-supported one-player activity instance starts and first Guardian control appears | bounded current entry | `D2-001`–`D2-004` |
| Hostile occupies a visible firing lane | Aim, fire, switch or reload; optionally activate a ready Void ability | Hit region, defence, damage, ammunition, shield/health and typed effects resolve in real time | layered shooter decision loop | `D2-004`, `D2-005` |
| Mesh generator is reachable after the refinery clear | Activate its Ghost interaction and hold the route | Authored hostile waves run until the defence flag clears and the next path opens | interaction-gated defence | `D2-006` |
| Walker blocks The Blast | Attack its legal body/weak-point states while preserving ammunition and cover | Walker defeat clears the next authored route gate | bounded miniboss gate | `D2-005`, `D2-006` |
| Solo Titan is defeated in a Restricted Zone before completion | Accept the wipe transition | Current encounter state restores from its authored checkpoint with no activity-complete result | reproducible failure policy | `D2-007` |
| Sepiks Prime remains active in the terminal arena | Survive adds and continue legal weapon/ability damage until defeat | Final objective reaches completion and the activity result is admitted | boss-gated terminal | `D2-006`, `D2-009` |
| Activity objectives are complete | Inspect completion and open the admitted chest | Score settles to its eligible grade/reward tier and the bounded reward becomes available | scored reward settlement | `D2-008`, `D2-009` |

## Strategic and experiential structure

- Local decision: choose cover and range, select the correct weapon slot,
  preserve heavy ammunition, reload before exposure and spend grenade, melee,
  barricade or Super readiness against the current threat density.
- Medium-term planning: carry enough reserve/heavy damage through the mesh and
  Walker gates for Sepiks rather than converting every intermediate enemy into
  maximum speed or score.
- Long-term structure: a fixed chain converts route traversal into defence,
  miniboss and boss completion, then settles one separately legible grade and
  reward boundary.
- Common heuristics: clear ranged threats before terminal commitment; reload
  between waves; use Barricade to create a safer firing line; break the
  Walker's exposed weak state; keep a Power-weapon reserve for the final arena.
- Failure attribution: weapon/ammunition HUD, shield/health and ability
  readiness, objective markers, local radar, score and checkpoint restart
  distinguish aim, resource, positioning, gate and terminal errors.
- Claim IDs: `D2-004`–`D2-009`.

## Replay and variation

- What changes between sessions: hostile timing and positions, ammunition
  drops, combat damage, ability use, checkpoint restarts, completion time,
  score and reward sample.
- Randomness or procedural generation: the authored route and mandatory gates
  remain fixed; enemy/drop variation does not create a new route topology.
- Multiple viable strategies: weapon emphasis, cover, ability timing and pace
  may vary while the pinned loadout and terminal remain unchanged.
- Typical replay motive: improve survival, route execution, completion time or
  grade and receive another eligible reward; repeated farming is excluded.
- Claim IDs: `D2-005`–`D2-009`.

## Adjacent systems and history

- Direct predecessor: Destiny established the original Devil's Lair route; the
  current record concerns Destiny 2's live Fireteam Ops implementation only.
- Variants: matchmade versions, higher difficulties, selected modifiers,
  Nightfall/Grandmaster state and other Ops require separate scopes.
- Similar games: Helldivers 2 shares prepared shooter abilities and mission
  scoring; Warframe shares solo route combat, drops and shield/health state;
  Left 4 Dead 2 shares an authored co-op-shooter route but uses bots and a
  Director-populated checkpoint terminal.
- Important differences: the scoped activity has no extraction decision,
  shared Reinforce stock, adaptive Survivor Director, persistent Mod/Affinity
  preparation or campaign union. It closes at a boss-triggered score/grade and
  reward chest.
- Claim IDs: `D2-002`, `D2-006`–`D2-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-215`, `ACT-341` | fixed Titan, weapons, abilities and interactables are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-380`, `SYS-605`, `SYS-623`, `SYS-624` | encounter population, drop sample, score and checkpoint are parameters |
| Constraint | `CON-262`, `CON-269` | slot, ammunition and ability readiness values are parameters |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-247` | HUD layout and result values are parameters |
| Objective | `OBJ-116` | Sepiks completion and terminal chest are fixed |
| Time | `TIM-003` | network latency and maintenance are excluded |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `192` (`GAME-0001`–`GAME-0192`).
- Exact genome matches: none.
- Tied near matches: `GAME-0159` — Helldivers 2 (`16 / 41 = 0.390244`); `GAME-0168` — Warframe (`16 / 41 = 0.390244`).
- Supported combination subsets: `COMB-0191`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0159` — Helldivers 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-215`, `SYS-208`, `SYS-215`, `SYS-380`, `CON-262`, `CON-269`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | both prepare a finite shooter loadout and join direct movement, aimed combat, reloads, typed abilities, live resources and objective HUD state; Destiny 2's solo authored route instead activates a Ghost defence, clears a Walker and Sepiks, restores local checkpoints on wipes and settles one score/grade/chest, while Helldivers uses a four-player stratagem code layer, friendly fire, patrol alarms, shared Reinforce, optional extraction and Galactic War impact | Near, `0.390244` |
| `GAME-0168` — Warframe | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-215`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-380`, `CON-262`, `CON-269`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | both support solo live route combat, weapon switching, ammunition pickups, typed abilities and shield/health state; Destiny fixes one authored Fireteam Op and finishes at a shared scoring/grade chest, while Warframe assembles tile routes, solves timed ciphers, installs capacity-and-polarity Mods, ranks gear through Affinity, extracts and restores an opening quest hub | Near, `0.390244` |

### Preserved research notes

- New genes: `SYS-623`, `SYS-624`, `INF-247` and `OBJ-116`.
- Classification result: bounded new genes, substantial reuse and one new
  verified interaction combination.
- Evidence and reasoning: direct shooter commands, shield/health, abilities,
  carried ammunition, authored gates and real time reuse safely. The exact
  boss-to-score/grade/chest settlement, solo Restricted Zone restore, Ops
  result disclosure and Devil's Lair terminal require narrower records.

## Combination status

- `COMB-0191` is a verified strict twenty-two-gene subset of the twenty-four-
  gene genome. It couples the prepared shooter loop and ordered authored gates
  to Sepiks completion and score/grade/chest settlement; optional ammunition-
  brick collection and failure-only checkpoint restoration remain outside the
  successful core.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: four new Active genes, evidence links on reused genes,
  `COMB-0191` and existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or reviewed-game
  signature changes.
- Candidate terms affected: Ops result settlement, Restricted Zone restore,
  activity grade disclosure and solo Devil's Lair terminal.

## Negative results

- `SYS-346` is not reused: this scope launches a fixed authored activity rather
  than sampling an extraction raid's map condition, world loot and participants.
- `SYS-429`, `SYS-430`, `SYS-596`, `CON-382` and `CON-512` are not reused: the
  scoped one-player Normal run has no active teammate, paired return, ghost
  survivor, shared Reinforce stock or ally-only disabled-state authority.
- `SYS-503` and `CON-426` are not reused: Devil's Lair has no objective-gated
  extraction region; Sepiks completion itself admits the result and chest.
- `SYS-619` is not reused: enemy variation does not establish a Left 4 Dead 2
  intensity Director that modulates hidden population around team state.
- Matchmaking, higher difficulty modifiers and time-bonus optimisation do not
  enter merely because the current client also exposes them.
- Account Power, reward inventory, campaigns, seasons and expansions do not
  silently expand a single activity-complete boundary.
