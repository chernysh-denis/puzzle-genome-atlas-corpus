---
game_id: GAME-0254
slug: control-ultimate-edition
game_title: CONTROL Ultimate Edition
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0252
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-190
    - ACT-341
  system:
    - SYS-112
    - SYS-146
    - SYS-215
    - SYS-369
    - SYS-380
    - SYS-398
    - SYS-578
    - SYS-705
    - SYS-706
    - SYS-748
    - SYS-755
    - SYS-788
  constraint:
    - CON-136
    - CON-269
    - CON-282
    - CON-402
    - CON-556
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-271
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: CONTROL Ultimate Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `870780`, sold through the one-application package `275147`, public Windows
  Build ID `21225456`, built 2025-12-17 and published 2025-12-18, checked
  2026-09-05. The build identifier and timestamps are secondary distribution
  observations. The official current PC patch line is `1.30`, released
  2025-03-10; the later public distribution build is not silently assigned a
  different publisher version number.
- Platform, input and settings: Windows, English interface and subtitles,
  keyboard and mouse, base-game single-player story, fresh `New Game`, with
  every Assist Mode feature off as the official ordinary recommended rule.
  The packet does not merge controller, console, macOS or accessibility-rule
  variants.
- Entry: complete only the preceding fresh-save opening, then retain ordinary
  control in Central Executive immediately after the conversation that starts
  main mission `Unknown Caller`. Save/quit and use `Continue` once before the
  admitted trace so the entry has the mission objective active, the initial
  `Grip` weapon form and no acquired supernatural ability.
- Primary decision loop: read the current objective, map, health, weapon
  capacity, ability Energy, reticle and locally visible threats; traverse the
  authored Executive Sector route; aim and fire the self-reloading weapon or
  use movement and hard geometry while its capacity recovers; clear mandatory
  hostile groups and cleanse required world nodes; reach and bind the first
  power object; pull an eligible loose prop into a collision-bounded hold and
  launch it into a barrier, receiver or hostile; alternate the independently
  recovering weapon and Energy reserves; pass the acquired credential and
  boss gates; operate the repeated fixture, room-selection, key and matching
  door sequence in the alternate authored space; reach the communication
  object, finish its traversal test and return to the mission giver.
- Positive terminal: speak with the mission giver after the communication
  sequence, allow `Unknown Caller` to complete and the successor main objective
  `Directorial Override` to become current, then quit without advancing that
  objective and use `Continue`. The terminal is the same retained ordinary
  Central Executive control with `Unknown Caller` complete, `Launch` retained
  and `Directorial Override` active.
- Negative terminal: protagonist death and ordinary retry restore the latest
  authored checkpoint without completing the mission. Reaching the acquired
  ability, defeating the required elevated hostile, taking the communication
  object, cleansing an intermediate node, seeing an autosave or stopping at an
  arbitrary quiet corridor is not positive settlement.
- Included: direct third-person walking, sprinting, jumping, evasion and
  crouch-height traversal; initial `Grip` form only; aimed shots, self-reloading
  weapon capacity, health attrition and spatial health-element recovery;
  mandatory local hostiles and clearance barriers; required Control Point
  cleansing, checkpoint and fast-travel affordance; the Pneumatics hazard;
  acquisition and retention of `Launch`; one loose-object pull, hold, release
  and damaging collision; one breakable barrier and one cube receiver that
  creates a bridge; Energy expenditure and automatic recovery; Clearance
  Level 1 credential use; the required Mail Room fight; the Hotline Chamber,
  Oceanview Motel fixture/room/key sequence and final Astral traversal; map,
  objective and tutorial surfaces; failure retry; mission completion and the
  retained successor-objective test.
- Excluded: `The Foundation`, `AWE`, Expeditions, Photo Mode, the March 2025
  bonus mission, bonus outfits and all expansion or post-campaign content;
  every story mission before the declared entry or after first retained
  `Directorial Override` control; side missions, Board Countermeasures,
  collectibles, hidden locations, exhaustive room clearing and optional
  dialogue; ability-point spending, mods, crafting, weapon upgrades and every
  later weapon form or power, including Shield, Evade, Seize, Levitate and
  Multi-Launch; alternate Assist settings, aim snap, immortality, difficulty
  modifiers, controller, consoles, macOS, cloud versions, mods, trainers,
  debug commands, speedrun skips, screenshots, artwork reuse, video and audio.
- Reproducible parameterisation: install the stated public Windows build, use
  English text and keyboard/mouse, choose fresh `New Game`, leave every Assist
  option disabled and establish the retained entry. Follow only the current
  main-objective marker; clear mandatory groups; cleanse the required Control
  Point; bind the power object; launch a cube through the barrier and another
  into the receiver; defeat the tutorial targets; use both weapon fire and one
  launched prop in later combat; take and use the required Level 1 credential;
  settle the required elevated hostile; pull the chamber fixture three times,
  ring the lobby bell until the required room opens, take the key, open its
  matching door and pull the return fixture three times; reach the Hotline,
  finish its traversal sequence, return and speak with the mission giver, then
  perform the `Continue` retention test. Exact health, capacity, Energy, loose
  prop, aim, damage, pickup and combat timing are parameters.
- Potential scoped modules: the preceding opening mission, one later base-game
  mission with a fixed incoming build, one side mission, one declared
  expansion, Expeditions or one alternative Assist configuration each requires
  its own entry, loop, terminal and evidence review.
- Direct-play status: not conducted. Current Valve, Remedy, Control and 505
  Games material establishes lawful availability, exact package, offline
  single-player operation, Ultimate-content boundaries, current patch line,
  ordinary Assist-off settings, weapon/Energy recovery and the telekinetic
  combat premise. Independent static written walkthroughs establish the exact
  mission order and transitions. This is an evidence-backed rules
  reconstruction, not a claim of a captured playthrough or entitlement. No
  video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CTRL-001` | The currently sold product is Windows Steam app `870780`, package `275147`, titled `CONTROL Ultimate Edition`, and supports single-player offline after download | Confirmed | Direct | High | P1, P2, P7 |
| `CTRL-002` | Public Windows Build `21225456` is the observed current distribution boundary, while official PC patch notes identify version line `1.30` | Observation | Corroborated | Medium | P4, S1 |
| `CTRL-003` | Ultimate Edition bundles the base game, `The Foundation`, `AWE`, Expeditions, Photo Mode and updates, but the declared packet admits only one base-story mission | Confirmed | Direct | High | P2, P3, P8 |
| `CTRL-004` | All Assist Mode features off preserve the officially recommended ordinary rules; Assist options can alter Energy recovery, self-reload, damage, death and aiming | Confirmed | Direct | High | P5 |
| `CTRL-005` | Direct third-person gun combat and telekinetic powers operate in a reactive environment, with the weapon and Energy reserves automatically recovering on separate rules | Confirmed | Direct | High | P3, P5, P6 |
| `CTRL-006` | `Launch` remotely acquires an eligible loose prop, holds it visibly and releases it into live collision for barrier, receiver or hostile consequences | Observation | Corroborated | High | P3, P6, S2–S4 |
| `CTRL-007` | The required power-object binding permanently grants `Launch`, and the immediate Astral challenge teaches barrier breaking, receiver placement and combat use | Observation | Corroborated | High | S2–S4 |
| `CTRL-008` | Mandatory hostile clearance removes authored barriers, and cleansing the required Control Point retains a checkpoint/travel node on the route | Observation | Corroborated | High | S2–S4 |
| `CTRL-009` | The required alternate-space sequence uses repeated fixture activation, a bell-selected room, a carried key and its matching door before the return transition | Observation | Corroborated | High | S2–S4 |
| `CTRL-010` | Damage reduces one health pool, compatible spatial elements restore missing health and death routes the attempt through authored checkpoint recovery | Observation | Corroborated | Medium | S3, S4 |
| `CTRL-011` | Speaking with the mission giver after the Hotline sequence completes `Unknown Caller` and starts `Directorial Override`, yielding the declared retained successor-objective test | Observation | Corroborated | High | S2–S4, V1 |
| `CTRL-012` | The bounded loop joins two automatically recovering combat resources to retained telekinetic world-object authority, fixture dependencies and a saved authored mission handoff | Strong Pattern | Corroborated | High | `CTRL-005`–`CTRL-011` |

## Basic data

- Release / origin: developed by Remedy Entertainment and originally
  published by 505 Games; base game released 2019-08-27 and the current Steam
  Ultimate Edition product released 2020-08-27.
- Platform or physical form: current lawfully offered English Windows Steam
  single-player application; one base-game authored mission packet.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; spatial logic and topology; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=870780&cc=ua&l=english),
    for exact current title, app identity, Windows, single-player category,
    package relation, current Ukraine offer and release date.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=275147&cc=ua&l=english),
    for package `275147`, application membership, Windows support and current
    lawful offer.
  - **[P3]** [official Control overview](https://legacy.controlgame.com/), for
    Ultimate Edition content, transforming weaponry, telekinetic powers,
    reactive environments, missions and upgrades.
  - **[P4]** [official March 2025 PC update notes](https://legacy.controlgame.com/control-march-2025-update-notes-pc/),
    for PC version `1.30`, supported Windows storefronts, unlocked outfits and
    the newly added bonus mission that this packet excludes.
  - **[P5]** [official August Update `1.11` notes](https://legacy.controlgame.com/de/control-august-update-notes/)
    and [official AWE FAQ](https://legacy.controlgame.com/awe-expansion-faq-guide/),
    for separately toggled Assist features, the recommendation to begin with
    all of them off, Energy regeneration, weapon self-reload, damage/death/aim
    modifiers, later Multi-Launch and expansion separation.
  - **[P6]** [official Remedy Control page](https://www.remedygames.com/games/control),
    for PC identity and the combination of supernatural abilities, modifiable
    loadouts and reactive environments in third-person action.
  - **[P7]** [official 505 Games offline-play answer](https://support.505games.com/support/solutions/articles/150000147304-do-i-have-to-be-online-to-play-control-ultimate-edition-),
    for offline play after the digital product and updates are downloaded.
  - **[P8]** [official Ultimate Edition announcement](https://legacy.controlgame.com/introducing-control-ultimate-edition/),
    for the base game, two expansions, Expeditions, Photo Mode and update
    package boundary.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/870780/depots/),
    for observed Windows public Build `21225456`, timestamps and depot/package
    separation. SteamDB is secondary and not treated as the publisher.
  - **[S2]** [Control Wiki `Unknown Caller`](https://control.fandom.com/wiki/Unknown_Caller),
    for the main-mission predecessor/successor, objective list, Control Point,
    power acquisition, clearance barriers, Hotline route and final return.
  - **[S3]** [GameFAQs `Unknown Caller` text walkthrough](https://gamefaqs.gamespot.com/ps4/241157-control/faqs/78194/unknown-caller),
    for the complete static route, Launch challenge, credential, required
    fight, health elements, alternate-space fixture sequence and mission end;
    platform-specific input glyphs are not imported.
  - **[S4]** [Neoseeker `Unknown Caller` text walkthrough](https://www.neoseeker.com/control/walkthrough/Unknown_Caller),
    for independent route, telekinetic barrier/receiver mechanics, authored
    gates, Hotline sequence and return corroboration; optional collection is
    excluded.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P8` and `S1`–`S4` under the declared build, entry, Assist-off settings,
  base-game exclusions and `Continue` terminal test; rules reasoning, not
  direct play.
- Claim IDs: `CTRL-001`–`CTRL-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint, evade, jump and use crouch-height
  route geometry; `ACT-161`: aim and fire the initial weapon or direct an
  eligible launched prop toward a reachable hostile; `ACT-190`: activate the
  acquired telekinetic ability with its legal target and Energy; `ACT-341`:
  cleanse, bind, take or operate each required authored object and speak with
  the mission giver.
- Existing `ACT-048`: remotely acquire one eligible free rigid prop, maintain
  its controlled relative pose and release it back into the live world. Reach,
  hold offset and release force are parameters rather than a branded action.
- New action genes: none. `Launch`, weapon, character, room and object names
  remain game-scoped parameters.
- Claims: `CTRL-005`–`CTRL-011`.

### System Behaviour Genes

- Existing `SYS-146`: advance a released prop under live gravity and
  collision; `SYS-215`: resolve directly commanded hostile combat;
  `SYS-369`: replace a failed attempt with the latest authored checkpoint;
  `SYS-380`: apply the selected telekinetic ability's typed displacement and
  damage effect; `SYS-398`: retain the newly acquired world-interaction
  capability in the save; `SYS-578`: apply damage and compatible spatial
  recovery to one continuous attempt-health pool.
- Existing `SYS-705`: resolve remote pull, attachment and collision-bounded
  view-relative holding before release; `SYS-706`: attribute eligible physical
  prop collision damage to the launching player; `SYS-755`: break an eligible
  world barrier after accepted damage reaches its threshold.
- Existing `SYS-112`: an accepted cube-receiver, bell, key or matching-door
  operation exposes its authored downstream mechanism state; `SYS-748`: after
  required local clearance and cleansing, convert a corrupted occupied node
  into a retained safe checkpoint/travel service.
- New `SYS-788`: independently restore inactive weapon capacity and ability
  Energy toward their caps, so spending one channel while the other recovers
  creates the ordinary alternating combat rhythm without ammunition pickups or
  a manual reload.
- Resolution order: current objective, local state and reticle expose legal
  inputs; direct movement, shots and hostile attacks update combat state;
  inactive capacity and Energy recover independently; required clearance opens
  a route and cleansing retains its node; binding grants the telekinetic
  capability; an eligible prop pulls into a held pose and release returns it to
  collision; damage, breakage or receiver compatibility settles; authored
  credential and repeated-fixture dependencies expose the Hotline path; the
  final return interaction completes the mission and writes successor state.
- Claims: `CTRL-005`–`CTRL-012`.

### Constraint Genes

- Existing `CON-269`: telekinetic use requires compatible target, range,
  Energy and readiness; `CON-556`: remote acquisition accepts only an eligible
  physical world target within the manipulation trace and clearance relation.
- Existing `CON-282`: mission, clearance, power acquisition, credential,
  fight, alternate-space sequence and final hand-in follow authored order;
  `CON-402`: mandatory barriers remain until the finite required hostile set is
  cleared; `CON-136`: each later fixture operation requires its retained prior
  activation, acquired item or matching unlock state.
- Scarce strategic resources: health, current weapon capacity, Energy, usable
  loose props, cover geometry, hostile-clearance state, acquired credential,
  authored checkpoint and route position. Exact quantities and named objects
  remain parameters.
- Claims: `CTRL-005`–`CTRL-011`.

### Information Genes

- Existing `INF-073`: the active weapon and its recovering capacity are
  visible; `INF-115`: local geometry and sight expose only presently perceived
  hostiles, attacks and loose props; `INF-119`: health, Energy and current
  ability readiness are visible; `INF-125`: explored map, tracked objective and
  authored gate state are inspectable; `INF-268`: the Astral tutorial states
  and confirms the current taught action.
- Existing `INF-271`: the reticle, telekinetic effect and visible prop response
  disclose target acceptance, pull, held pose, release or rejection without
  predicting the later impact. The canonical label is wording-generalised in
  this unit from its earlier tool-specific phrasing while preserving its exact
  boundary and every reviewed signature.
- Claims: `CTRL-005`–`CTRL-011`.

### Objective Genes

- Existing `OBJ-026`: make the bounded authored route traversable and return
  to the designated mission giver after the Hotline sequence; the objective is
  satisfied only when mission completion and retained successor control have
  settled.
- Ability acquisition, boss defeat, Hotline pickup, one Control Point or one
  autosave is intermediate. Death/checkpoint restoration fails only the
  current attempt and does not create an alternate positive terminal.
- Claims: `CTRL-007`–`CTRL-012`.

### Time Genes

- Existing `TIM-003`: movement, hostile attacks, projectiles, physical props,
  health damage, weapon/energy recovery and live ability effects advance
  continuously outside blocking menus and authored transitions.
- Claims: `CTRL-005`, `CTRL-006`, `CTRL-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current public Windows build; fresh `New Game`; English; keyboard/mouse; every Assist feature off | Establish the retained post-briefing entry and use `Continue` | Initial weapon form, no supernatural ability and `Unknown Caller` objective resume in Central Executive | exact ordinary entry | `CTRL-001`–`CTRL-004` |
| A mandatory local hostile set remains active | Move through cover, aim and fire | Live damage and weapon capacity settle; the route barrier remains until the finite required set is cleared | clearance-gated combat | `CTRL-005`, `CTRL-008` |
| Weapon capacity or ability Energy is below cap and its spending action has ceased | Use the other legal channel or preserve distance | Each inactive reserve recovers by its own timing rule toward its cap | alternating self-recovery loop | `CTRL-004`, `CTRL-005` |
| The route Control Point is available after local clearance | Commit cleansing | Corrupted local state settles and a retained checkpoint/travel service becomes available | persistent node conversion | `CTRL-008` |
| A loose eligible prop is addressed with sufficient Energy and clearance | Hold the telekinetic command | The prop pulls into a visible collision-bounded relative pose; an incompatible target rejects | remote physical acquisition | `CTRL-006` |
| A compatible prop is held before a barrier, receiver or hostile | Aim and release | The prop returns to live ballistic collision, then breaks, activates or damages the contacted eligible state | one world object has route and combat roles | `CTRL-006`, `CTRL-007` |
| The power object is reached and its authored binding is accepted | Complete the acquisition and Astral instruction | `Launch` becomes retained, the barrier/receiver steps teach it and the route returns to the Executive Sector | persistent capability acquisition | `CTRL-007` |
| A Level 1 credential is carried at the matching locked route | Commit the authored door interaction | The credential relation opens the required continuation without becoming a generic gene label | acquired access gate | `CTRL-008` |
| The elevated required hostile remains active | Alternate aimed shots, launched props and movement | The target evades or takes compatible attacks while health, weapon capacity and Energy continue resolving | combined boss pressure | `CTRL-005`, `CTRL-006` |
| The chamber fixture is reachable | Pull it three times | The authored threshold transfers the protagonist into the alternate-space lobby | repeated transition dependency | `CTRL-009` |
| The lobby sequence is active | Ring the bell to expose the required room, take its key and open the matching door | Repeated fixture state selects the downstream room; acquired compatibility opens the required door | authored room/key mechanism | `CTRL-009` |
| The alternate-space door is open and the return fixture is reachable | Pull the fixture three times, then complete the Hotline traversal | Control returns to the Hotline Chamber and the communication-object sequence settles | reversible authored-space route | `CTRL-009`, `CTRL-011` |
| The communication sequence is complete | Return to Central Executive and speak with the mission giver | `Unknown Caller` completes and `Directorial Override` becomes the current main objective | mission settlement | `CTRL-011` |
| Successor objective is active without further progress | Quit, use `Continue` and accept ordinary control | The same completed mission, retained `Launch` and successor objective return | retained positive terminal | `CTRL-011`, `CTRL-012` |
| Health reaches zero before mission settlement | Accept ordinary retry | The latest authored checkpoint replaces transient combat position, damage and hostile state | negative boundary | `CTRL-010` |

## Strategic and experiential structure

- Planning horizon: read the next authored gate, preserve safe geometry and
  decide whether the current threat is better answered by recovering gunfire,
  recovering telekinetic Energy or repositioning for a loose prop.
- Local tactics: emptying one capacity does not end combat authority because
  the other channel can remain available; a held world object can become a
  damaging projectile, barrier breaker or receiver input, while hard cover
  also blocks hostile fire and incoming environmental hazards.
- Medium-term structure: cleansing creates retained route infrastructure;
  binding permanently changes the interaction vocabulary; later credential,
  hostile and alternate-space fixture gates test that new state before the
  mission can return to its giver.
- Reversible versus irreversible: shots, damage, Energy and loose-object poses
  are attempt-local and checkpoint-recoverable; cleansed nodes, acquired
  ability, mission completion and successor-objective state persist.
- Failure attribution: visible resources, reticle response, objective marker,
  barrier state, tutorial instruction and retained mission state distinguish
  combat, eligibility, dependency, route and terminal errors.
- Player trust: illegal objects reject visibly; independent meters visibly
  recover; required hostile barriers settle only after closure; authored
  fixture changes are inspectable; `Continue` reproduces the terminal.

## Replay and variation

- The mission, main gate order, ability acquisition, required hostile and
  alternate-space sequence are authored. Exact cover, prop, aim, attack order,
  health recovery and checkpoint use can vary.
- Several local weapon/telekinesis rhythms can reach the same terminal. Assist
  features would change recovery, damage, death or aim rules and therefore
  define a different packet rather than harmless presentation.
- Optional dialogue, documents, containers, side missions and build choices
  motivate replay but do not enter this fixed fresh-save trace. Expansion and
  post-campaign modules remain separately bounded.

## Adjacent systems and history

- Half-Life 2 shares direct movement, remote physics-object acquisition,
  collision-bounded holding and attributed prop impact. Its Gravity Gun is a
  carried tool with explicit physical eligibility and conventional finite
  firearms; CONTROL retains a newly bound ability and alternates its Energy
  with a self-reloading transforming weapon through a mission dependency chain.
- STAR WARS Jedi: Fallen Order shares a retained capability, resource-gated
  abilities, authored third-person combat and a successor objective. Its first
  Bogano visit couples meditation, attack-fed Force and a reachability-coloured
  Holomap to Wall Run; CONTROL uses passive independent recovery, free rigid
  props, cleansed service nodes and an alternate-space fixture sequence.
- Max Payne (2001) shares Remedy-authored real-time third-person combat,
  checkpoint restoration and a bounded successor transition, but its reviewed
  packet uses conventional reloads, delayed carried medicine and Bullet Time
  rather than telekinetic world objects and two self-restoring combat channels.
- Dishonored shares ordered mission gates, active powers, contextual authored
  objects and a returned mission settlement. Its reviewed mission centres on
  stealth perception and one learned target disposition; CONTROL centres on
  reactive physics, power acquisition and fixture-gated spatial routing.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-190`, `ACT-341` | movement, weapon, telekinesis and authored interaction |
| System Behaviour | `SYS-112`, `SYS-146`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-398`, `SYS-578`, `SYS-705`, `SYS-706`, `SYS-748`, `SYS-755`, `SYS-788` | fixtures, physics, combat, retry, retained ability, health, node and dual recovery |
| Constraint | `CON-136`, `CON-269`, `CON-282`, `CON-402`, `CON-556` | dependencies, Energy/target, authored order, clearance and object eligibility |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-271` | weapon, local, personal, route, tutorial and manipulation response |
| Objective | `OBJ-026` | complete and retain the bounded mission handoff |
| Time | `TIM-003` | continuous traversal, combat, physics and recovery |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `253` (`GAME-0001`–`GAME-0253`).
- Exact genome matches: none.
- Tied near matches: `GAME-0212` — Half-Life 2 (`16 / 38 = 0.421053`).
- Supported combination subsets: `COMB-0252`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0212` — Half-Life 2 | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-341`, `SYS-146`, `SYS-215`, `SYS-369`, `SYS-705`, `SYS-706`, `CON-556`, `INF-073`, `INF-115`, `INF-119`, `INF-271`, `OBJ-026`, `TIM-003` | Both traverse one authored live route, visibly pull and hold eligible physics props, release them into attributed collision damage, use direct weapons and recover from checkpoints before a fixed location terminal. Half-Life 2 adds conventional finite magazines, local zombie routing and tool-specific mass/trace behaviour through a complete chapter. CONTROL instead retains the acquired telekinetic ability, alternates two independently recovering combat reserves, cleanses persistent service nodes and resolves receiver, credential and alternate-space fixture dependencies before a mission-objective handoff. | Near, `16 / 38 = 0.421053` |

### Preserved research notes

- New genes: `SYS-788`.
- Reused genes: `ACT-008`, `ACT-048`, `ACT-161`, `ACT-190`, `ACT-341`,
  `SYS-112`, `SYS-146`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-398`,
  `SYS-578`, `SYS-705`, `SYS-706`, `SYS-748`, `SYS-755`, `CON-136`,
  `CON-269`, `CON-282`, `CON-402`, `CON-556`, `INF-073`, `INF-115`,
  `INF-119`, `INF-125`, `INF-268`, `INF-271`, `OBJ-026` and `TIM-003`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: generic traversal, combat, telekinetic cast,
  contextual interaction, live physics, damage, checkpoint, retained
  capability, health, node conversion, authored dependencies and visible
  state transfer. The one new boundary isolates two separately recovering
  combat authorities whose alternating availability is decision-relevant.
- Lower-ID scan: reuse `ACT-048`, `SYS-705`, `SYS-706`, `CON-556` and
  `INF-271` after wording-generalising their existing physical-manipulation
  names without changing their boundaries or the reviewed Half-Life 2
  signature. Reject `ACT-183`, `CON-262` and `CON-285`, because the initial
  weapon self-reloads without carried reserve ammunition or manual magazine
  transfer; reject `SYS-707`, because Energy recovers passively rather than
  through successful attacks; reject `SYS-737`, because health does not return
  after a quiet interval; reject `SYS-771`, because no selected powered mode
  continuously drains one shared reserve; reject `SYS-780` and `OBJ-155`,
  because `Unknown Caller` is a mission-objective handoff, not an explicit
  numbered chapter transition; reject later powers, forms, upgrades and
  expansion mechanics because they are unreachable in the admitted packet.

## Taxonomy impact

- Registry changes: one additive Active system boundary; wording-generalise
  `SYS-705`, `CON-556` and `INF-271` from tool-specific labels to their already
  accepted transferable remote-object boundary and add CONTROL support. No
  earlier reviewed signature, lifecycle state or conclusion changes.
- Taxonomy-change record: none; the three wording edits preserve their existing
  causal boundary and the new gene is ordinary additive game-unit taxonomy.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; mission, actor,
  weapon form, power object, ability, room, hostile, credential and numeric
  labels remain game-scoped parameters.

## Negative results

- No direct play, entitlement, local-build, screenshot, video, audio, acting or
  audiovisual-analysis claim. Build ID/timestamps remain secondary and the
  later distribution build is not assigned an invented publisher version.
- No expansion, bonus mission, post-campaign, whole-campaign, side-mission,
  collectible, build, platform, input, Assist-rule or live-history union.
- No earlier reviewed game signature or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry is tested as a proper
  subset of this thirty-gene signature. `COMB-0252` records the strict retained
  telekinetic-object, dual-recovery, authored-dependency and mission-terminal
  core; supported earlier subsets, if any, are listed after deterministic
  regeneration.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] The current lawful Windows product, bundled
  content, offline use and ordinary Assist-off boundary are fixed in
  `CTRL-001`–`CTRL-005`.
- [Observation | Corroborated | High] The exact power acquisition, object
  manipulation, fixture chain and retained mission terminal are fixed in
  `CTRL-006`–`CTRL-011`.

## New genes

- [Confirmed | Direct | High] `SYS-788` isolates the independent automatic
  recovery of weapon capacity and ability Energy after their respective spend
  actions cease.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0252` joins remote physical
  object authority, independently recovering combat channels, persistent power
  acquisition, cleansed route infrastructure and authored fixture dependencies
  before a retained mission handoff.

## Taxonomy changes

- [Observation | Corroborated | High] Three canonical labels are wording-
  generalised without a boundary, lifecycle or reviewed-signature change.

## New questions

- Does Batman: Arkham Asylum's bounded predator route require a distinct
  information-and-fear loop beyond reviewed stealth perception and authored
  clearance structures?

## Next recommended unit

- [Hypothesis | Limited | High] `GAME-0255` — Batman: Arkham Asylum Game of
  the Year Edition.
- Optimisation criterion: isolate one early base-story predator/combat packet
  under one current lawful Windows build and a retained mission checkpoint.
- Expected information gain: test detective information, predator routing and
  counter-based melee against existing stealth and combat genes.
- Backlog impact: third game unit in the ordered Batch 014 horizon.

## Why this unit

- [Hypothesis | Limited | High] It is the next fixed ID after the selected
  telekinetic base-story mission and preserves the ordered horizon.
