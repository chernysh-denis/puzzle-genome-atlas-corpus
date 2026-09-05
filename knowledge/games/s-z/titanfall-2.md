---
game_id: GAME-0253
slug: titanfall-2
game_title: "Titanfall 2"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0251
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-190
    - ACT-341
    - ACT-428
  system:
    - SYS-215
    - SYS-222
    - SYS-369
    - SYS-380
    - SYS-737
    - SYS-780
    - SYS-786
    - SYS-787
  constraint:
    - CON-262
    - CON-269
    - CON-282
    - CON-285
    - CON-598
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Titanfall 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1237970`, offered through current Ultimate Edition package `432912`, public
  branch Build ID `10350970`, built 2023-01-18 and published 2023-02-01,
  checked 2026-09-05. The build identifier and dates are secondary
  distribution observations. Ultimate multiplayer unlocks and cosmetics do not
  enter the base single-player campaign packet.
- Platform, input and difficulty: Windows, English text, keyboard and mouse,
  offline single-player Campaign, fresh `New Game`, `Normal`. Controller,
  another difficulty, Mission Select, multiplayer and community clients are
  separate modules.
- Entry: retain first ordinary control of the on-foot protagonist on the
  post-drop battlefield at the start of campaign chapter `BT-7274`, before the
  required interaction with the fallen Pilot. The preceding Pilot's Gauntlet,
  crash cinematic and any prior loadout are setup, not admitted play.
- Primary decision loop: follow the current waypoint through a fixed authored
  route; use sprint, jump, double jump, wall run, crouch/slide and cloak to
  manage geometry and exposure; select, aim, fire, reload and replenish finite
  weapons or throw a grenade against local wildlife, infantry, drones and
  machines; collect and install two charged power modules in authored order;
  enter the restored allied combat platform after its link gate; learn its
  direct movement, weapon, defensive and offensive abilities; defeat the
  required hostile platform; follow the final waypoint into chapter settlement.
- Positive terminal: the chapter-complete handoff has created retained campaign
  state and ordinary direct control is available at the opening of `Blood and
  Rust`. Exit without advancing its first encounter, reload the retained save
  and verify the same successor-chapter control. Merely installing either
  module, completing the link, defeating the hostile platform or seeing a
  transition cinematic is not terminal.
- Negative terminal: protagonist or allied-platform defeat returns the attempt
  to the latest authored checkpoint without satisfying the retained successor
  test. Quitting, restarting or stopping at a checkpoint is not an evaluated
  terminal.
- Included: direct Pilot traversal; double jump and wall run; crouch/slide;
  local line-of-sight combat; finite carried weapon slots, magazines, reserve
  ammunition and grenades; weapon switching, reload and eligible pickups;
  delayed Pilot health regeneration; Cloak; waypoint and staged tutorial
  guidance; required contextual interactions; the two ordered charged power
  modules; staged allied-platform activation; link-gated entry and transfer of
  direct movement/combat authority; the fixed introductory platform loadout;
  defensive projectile capture/return, offensive ordnance and earned Core use
  only as typed ability parameters; hostile-platform defeat; checkpoint retry;
  explicit chapter settlement and retained successor control.
- Excluded: the complete Pilot's Gauntlet and every chapter after the first
  retained `Blood and Rust` control; later platform loadouts, boss fights,
  dialogue branches, collectibles, helmets, achievements and campaign
  completion; multiplayer modes, maps, factions, loadouts, progression,
  Regeneration, networks and server history; Ultimate/Deluxe/Jump Start
  unlocks and cosmetics; the original Titanfall; Northstar or another community
  client; PlayStation, Xbox, Linux/Proton, cloud or another build; mods,
  trainers, debug commands, speedrun skips, alternate difficulties and control
  schemes; audio, acting and audiovisual analysis.
- Reproducible parameterisation: launch the stated public Windows build with
  English text and keyboard/mouse; choose Campaign, `New Game` and `Normal`.
  From first retained battlefield control, interact with the required wounded
  actor, follow each current marker, collect and install the first charged
  module, follow the newly exposed route for the second, use the taught Cloak
  and required traversal, install the second module, complete the direct-control
  tutorial/link, defeat the required hostile platform, cross the final marker
  and perform the successor-save reload test. Exact path, aim, weapon identity,
  ammunition count, damage and ability timing are parameters when they do not
  alter a required authored predicate.
- Potential scoped modules: one later named campaign chapter, one alternative
  difficulty, one fixed multiplayer mode/build or one non-Windows release each
  requires a separate entry, decision loop, terminal and evidence review.
- Direct-play status: not conducted. Current Valve and EA product material plus
  the official EA PC manual establish lawful availability, product/mode
  separation, controls, Campaign menu and objective surface. Independent text
  walkthroughs establish the chapter route, two-module sequence, direct-control
  tutorial, required final combat and successor chapter. This is an
  evidence-backed rules reconstruction, not a claimed playthrough or
  entitlement. No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TF2-001` | The current lawful Windows product is Steam app `1237970`; current package `432912` is Ultimate Edition and separates campaign from multiplayer extras | Confirmed | Direct | High | P1–P3 |
| `TF2-002` | Public Build `10350970` is the current observed Windows distribution boundary | Observation | Corroborated | Medium | S1 |
| `TF2-003` | Campaign supports `New Game`, Mission Select for unlocked sections and a visible current objective; this packet fixes fresh `Normal` keyboard/mouse play | Confirmed | Direct | High | P3 |
| `TF2-004` | The bounded chapter requires direct Pilot movement, double jumps/wall runs, local combat, Cloak and contextual route interaction | Observation | Corroborated | High | P3, S2–S4 |
| `TF2-005` | Pilot combat uses selectable magazine-fed weapons, reload, finite ammunition/grenades and eligible world replenishment | Confirmed | Direct | High | P3, S2, S3 |
| `TF2-006` | Two charged power modules are recovered and installed sequentially before the allied combat platform becomes fully operable | Observation | Corroborated | High | S2–S5 |
| `TF2-007` | Completed restoration and operator link permit entry and transfer direct movement, attack and typed ability control to the allied platform | Confirmed | Corroborated | High | P3, S2–S4 |
| `TF2-008` | The introductory platform sequence teaches defensive, offensive and Core actions before or during the required hostile-platform battle | Observation | Corroborated | High | P3, S2–S4 |
| `TF2-009` | Pilot health returns after a quiet interval, while defeat restores authored checkpoint state rather than retaining transient combat positions | Observation | Corroborated | Medium | S3, S4 |
| `TF2-010` | Clearing the required platform fight and final marker settles `BT-7274` into `Blood and Rust`, providing a retained successor-control terminal | Observation | Corroborated | High | S2–S5 |
| `TF2-011` | The bounded loop couples high-mobility on-foot traversal, staged restoration and a link-gated embodiment transfer rather than representing a generic shooter corridor | Strong Pattern | Corroborated | High | `TF2-004`–`TF2-010` |

## Basic data

- Release / origin: developed by Respawn Entertainment and published by
  Electronic Arts; original release 2016-10-28; current Windows product state
  checked 2026-09-05.
- Platform or physical form: authored first-person single-player action
  campaign on Windows; one fresh fixed-difficulty chapter packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; agent routing and coordination; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1237970&cc=ua&l=english),
    for current exact product identity, Windows support, single-player and
    multiplayer categories, current offer and package relation.
  - **[P2]** [official EA product page](https://www.ea.com/games/titanfall/titanfall-2),
    for current Windows/Steam availability, Pilot/Titan campaign framing and
    Ultimate Edition's separately described multiplayer unlocks and cosmetics.
  - **[P3]** [official EA English PC manual](https://eaassets-a.akamaihd.net/eahelp/manuals/titanfall-2-pc-uk.pdf),
    for Pilot and Titan keyboard/mouse controls, Campaign objective display,
    New Game/Mission Select boundary, weapon/reload/grenade interaction, embark
    control, defensive/offensive/utility/Core inputs and mode separation.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1237970/depots/),
    for public Build `10350970`, Windows/English depots and the secondary
    build/publish timestamps.
  - **[S2]** [StrategyWiki `BT-7274` text route](https://strategywiki.org/wiki/Titanfall_2/BT-7274),
    for battlefield entry, wall runs, two batteries, Cloak, platform tutorial,
    hostile waves and final waypoint.
  - **[S3]** [GameFAQs campaign text guide](https://gamefaqs.gamespot.com/pc/134594-titanfall-2/faqs/74352),
    for Pilot health recovery, module installation, link training, defensive
    projectile return, offensive abilities and the required platform fight.
  - **[S4]** [TrueAchievements Mission 2 text walkthrough](https://www.trueachievements.com/walkthroughpage.aspx?pageid=11521),
    for fixed mission ordering, traversal/Cloak, module sequence, platform
    training, final hostile platform and handoff to Mission 3. Achievement
    advice is excluded.
  - **[S5]** [Titanfall Wiki.gg `BT-7274` level record](https://titanfall.wiki.gg/wiki/BT-7274_(level))
    and [successor `Blood and Rust` record](https://titanfall.wiki.gg/wiki/Blood_and_Rust),
    for chapter identities and immediate successor relation; these are
    community-maintained corroboration, not official publisher sources.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S5` under the declared build, entry, settings and terminal;
  rules reasoning, not direct play.
- Claim IDs: `TF2-001`–`TF2-011`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move, sprint, jump, double jump, wall run,
  crouch and slide the on-foot operator through the authored route;
  `ACT-161`: aim and attack reachable hostiles; `ACT-164`: switch among carried
  weapon slots; `ACT-183`: reload a magazine-fed weapon; `ACT-184`: aim and
  throw a finite grenade; `ACT-190`: activate Cloak or a directly controlled
  platform ability; `ACT-341`: interact with the wounded actor, charged
  modules and required authored objects.
- New `ACT-428`: enter the restored allied combat platform and commit the
  transfer from on-foot locomotion/fire controls to that platform's direct
  movement, weapon and ability controls. Platform identity, hatch pose and
  named loadout remain parameters.
- Claim IDs: `TF2-004`–`TF2-008`.

### System Behaviour Genes

- Existing `SYS-215`: resolve Pilot and platform combat in real time;
  `SYS-222`: transfer eligible weapon or ammunition pickups into carried state;
  `SYS-369`: restore the latest authored checkpoint after failure; `SYS-380`:
  apply Cloak, defensive projectile capture/return, ordnance and Core as typed
  live ability effects; `SYS-737`: apply Pilot damage and delayed quiet-interval
  health restoration; `SYS-780`: close the chapter and retain successor control.
- New `SYS-786`: each accepted compatible power module advances one disabled
  allied platform through its authored staged activation, with the final
  required module enabling the link/operation gate. New `SYS-787`: after a legal
  entry, rebind direct locomotion, attack, ability and HUD state from the
  on-foot operator to the allied combat platform while preserving the operator
  as its occupant rather than spawning an unrelated vehicle or character.
- Resolution order: waypoint and tutorial expose the next legal task; direct
  movement and combat update local position/resources; a compatible module is
  collected and installed; staged activation reveals the next route; the final
  module enables link and entry; accepted entry transfers direct control and
  HUD; typed platform actions settle the required fight; the final marker
  closes the chapter, writes retained state and admits successor control.
- Claim IDs: `TF2-004`–`TF2-011`.

### Constraint Genes

- Existing `CON-262`: carried weapons, grenades, magazines and reserves obey
  finite slot/capacity limits; `CON-269`: Cloak and platform abilities require
  their legal state and readiness; `CON-282`: modules, link, tutorial, fight and
  chapter handoff require authored predecessors; `CON-285`: fire/reload/switch
  requires compatible current weapon, ammunition and body state.
- New `CON-598`: direct operation of an allied combat platform requires its
  declared power-restoration threshold, compatible operator link and reachable
  entry state; an incomplete stage rejects the transfer.
- Scarce resources: Pilot/platform health, ammunition, loaded magazine,
  grenades, ability readiness, compatible power modules, safe traversal
  geometry and latest checkpoint. Exact values and named equipment are
  parameters. Claims: `TF2-004`–`TF2-010`.

### Information Genes

- Existing `INF-073`: carried weapon, active slot, magazine and reserve state
  are visible; `INF-115`: local sightlines expose only currently visible
  hostiles and attacks; `INF-119`: current Pilot or platform health and ability
  readiness are visible; `INF-125`: objective text and route marker expose the
  current authored gate; `INF-268`: the instructional surface explains the
  current movement, module, link or platform action and confirms it before
  advancing.
- Audio cues are neither required nor used as evidence for this packet. Actor,
  marker text, gauges, colours and control glyphs remain parameters. Claims:
  `TF2-003`–`TF2-010`.

### Objective Genes

- Existing `OBJ-155`: survive and complete the mandatory interactions of one
  authored action chapter, accept explicit settlement and retain ordinary
  control in the immediate successor chapter. Here the two-module restoration,
  link, required platform fight and final waypoint lead to reload-verified
  `Blood and Rust` control.
- Collecting either module, merely linking, defeating the final hostile before
  settlement or stopping at a checkpoint does not satisfy the terminal. Claims:
  `TF2-006`–`TF2-011`.

### Time Genes

- Existing `TIM-003`: traversal, hostile movement, shots, reload, ability
  duration/readiness, damage and combat-platform control advance continuously
  outside blocking menus or authored transitions. Claims: `TF2-004`–`TF2-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current public Windows build; Campaign; fresh `Normal`; keyboard/mouse | Start and retain first post-drop battlefield control | On-foot body, current objective, fixed opening weapon state and authored route become active | exact entry | `TF2-001`–`TF2-004` |
| A marked path crosses separated vertical surfaces | Sprint, jump, double jump or wall run through it | Direct momentum and contact determine whether the operator reaches the next connected surface | high-mobility traversal | `TF2-004` |
| A visible hostile is reachable and compatible ammunition remains | Select weapon, aim, fire and reload as needed | Magazine/reserve state changes while real-time damage, defence and defeat settle | finite direct combat | `TF2-005` |
| A current encounter admits concealment or explosive response | Activate Cloak or throw a grenade | Readiness/stock is spent and the typed effect changes visibility or hostile damage in live space | bounded tactical choice | `TF2-004`, `TF2-005` |
| The first compatible charged module is reachable | Collect, return and install it | Carried module is consumed; allied platform enters its first activation stage and exposes the second route | staged restoration | `TF2-006` |
| The second route's combat and traversal predicates are complete | Collect, return and install the second module | Final restoration threshold is met and platform link/operation becomes available | operation gate | `TF2-006`, `TF2-007` |
| Restored platform and compatible operator link are ready | Enter the platform and complete the taught controls | Direct movement, weapon, defensive/offensive ability and HUD authority transfer to the platform | embodiment transfer | `TF2-007`, `TF2-008` |
| Required hostile platform remains active | Aim/fire, use defensive capture/return and commit offensive/Core actions when legal | Live damage and ability effects continue until the required hostile reaches defeat | platform combat | `TF2-008` |
| Final hostile is defeated and the last waypoint is active | Reach the marker and accept chapter handoff | `BT-7274` closes, retained campaign state is written and `Blood and Rust` ordinary control begins | positive settlement | `TF2-010` |
| Successor control has appeared without advancing its encounter | Exit, reload retained Campaign save and accept control | The same successor chapter/control state returns | retained terminal proof | `TF2-010`, `TF2-011` |
| Pilot or platform health reaches defeat before settlement | Choose checkpoint retry | Latest authored checkpoint state replaces transient failure positions and damage | negative boundary | `TF2-009` |

## Strategic and experiential structure

- Planning horizon: read the next marker, choose a traversable high-mobility
  line, conserve ammunition/ability readiness through local resistance and
  return each required module before attempting the link gate.
- Local tactics: use geometry and speed to reduce exposure, switch/reload before
  pressure closes space, conceal or throw a grenade when its typed effect has
  leverage, then coordinate platform defence and offence against the required
  heavy hostile.
- Medium-term structure: the first module changes the same disabled ally but
  does not admit direct operation; the second completes restoration, after
  which link and entry replace the on-foot control vocabulary with a heavier
  direct-combat vocabulary.
- Reversible versus irreversible: movement, damage and ammunition return to an
  authored checkpoint after failure; installed restoration stages, link,
  chapter settlement and successor access are retained campaign progress.
- Failure attribution: route marker, instructional state, ammunition/HUD,
  module stage, link gate, current controlled body and checkpoint distinguish
  traversal, resource, combat, restoration and terminal errors.
- Player trust: each module visibly changes platform availability, illegal
  entry remains rejected before the threshold, accepted entry changes the full
  direct-control surface and the reload test reproduces the successor state.

## Replay and variation

- The chapter geometry, module order, activation thresholds, tutorial, required
  heavy hostile and successor are authored. Exact movement line, weapon choice,
  ammunition pickup, damage and ability timing can vary.
- `Normal` permits several local combat approaches but does not change the
  required restoration/link/settlement chain. Another difficulty is a separate
  packet rather than silently merged balance history.
- Mission Select, collectibles and cleaner execution motivate replay but do not
  enter this fresh-save terminal. Multiplayer's configurable Pilot/Titan
  loadouts, progression and live-service rules are absent.

## Adjacent systems and history

- Crysis Remastered and DOOM (2016) share fast first-person movement, finite
  weapon combat and authored checkpoint return, but neither uses two installed
  restoration stages to gate a direct operator-to-allied-platform transfer.
- STAR WARS Jedi: Fallen Order shares wall traversal, abilities, checkpointed
  combat and an authored successor objective; its bounded packet retains a
  traversal capability and companion map rather than changing the directly
  controlled body into a restored combat platform.
- Battlefield 2042 directly operates infantry and vehicles inside a complete
  Conquest match, but vehicle availability is a spawn/world choice rather than
  a two-module authored ally restoration and campaign link gate.
- The original Titanfall, multiplayer modes and community clients are related
  products or rulesets, not historical state merged into this campaign chapter.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-190`, `ACT-341`, `ACT-428` | movement, weapons, grenade, ability, interaction and platform entry |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-369`, `SYS-380`, `SYS-737`, `SYS-780`, `SYS-786`, `SYS-787` | combat, pickup, retry, typed effects, regeneration, settlement, restoration and control transfer |
| Constraint | `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-598` | capacity, readiness, authored order, weapon state and link gate |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268` | equipment, local, body, objective and tutorial state |
| Objective | `OBJ-155` | complete one action chapter into retained successor control |
| Time | `TIM-003` | continuous traversal and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `252` (`GAME-0001`–`GAME-0252`).
- Exact genome matches: none.
- Tied near matches: `GAME-0238` — Max Payne (2001) (`16 / 37 = 0.432432`).
- Supported combination subsets: `COMB-0251`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0238` — Max Payne (2001) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-341`, `SYS-215`, `SYS-369`, `CON-262`, `CON-269`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Both traverse one authored real-time combat chapter with selectable magazine weapons, contextual gates, finite resources and checkpoint return. Max Payne turns a personal meter into slow-time movement, applies carried delayed medicine, adapts opposition and breaches a rail barrier before a generic location terminal; Titanfall instead uses high-mobility wall traversal, two-stage allied-platform restoration, a compatible operator link and full embodied combat-control transfer before retained successor-chapter control. | Near, `0.432432` |

### Preserved research notes

- New genes: `ACT-428`, `SYS-786`, `SYS-787` and `CON-598`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`,
  `ACT-190`, `ACT-341`, `SYS-215`, `SYS-222`, `SYS-369`, `SYS-380`,
  `SYS-737`, `SYS-780`, `CON-262`, `CON-269`, `CON-282`, `CON-285`,
  `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `OBJ-155` and
  `TIM-003`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing direct locomotion, weapon operation, typed
  abilities, combat, checkpoint, HUD, authored order and retained chapter
  boundaries transfer without product names. New terms isolate staged
  allied-platform restoration and the link-gated transfer into that platform.
- Lower-ID scan: reject `ACT-201`/`SYS-320`, because the admitted platform is a
  restored linked ally whose entire embodied combat authority replaces the
  on-foot control surface, not an available driver seat plus road/terrain
  steering and optional exit; reject `ACT-052`, because the transfer does not
  switch freely among independent persistent bodies; reject `SYS-739`, because
  no remote companion ability replaces an independently controlled drone;
  reject `SYS-398`, because the modules do not retain a newly learned traversal
  capability; reject `CON-288`, because fuel, viable driver seat and road
  geometry do not gate operation; reject a new Vortex-specific gene because
  projectile capture/return is an instance of typed protection/displacement
  under `SYS-380`, not a portable product label.

## Taxonomy impact

- Registry changes: four additive Active boundaries and twenty-three reused
  transfers. No earlier definition, lifecycle state or reviewed game signature
  changes.
- Taxonomy-change record: none; this is additive game-unit taxonomy work.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; protagonist,
  platform, module, chapter, ability, weapon and numeric labels remain
  game-scoped parameters.

## Negative results

- No direct-play, entitlement, local-build, video, audio, screenshot or acting-
  analysis claim. Build ID and dates remain secondary observations.
- No multiplayer, Ultimate unlock, whole-campaign, later-loadout, platform,
  difficulty, control-method or live-service union.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry is tested as a proper
  subset of this twenty-eight-gene signature. `COMB-0251` records the strict
  restoration, embodiment-transfer and chapter-settlement core; supported
  earlier subsets, if any, are listed after deterministic regeneration.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] The current Windows product and Campaign/control
  boundaries are fixed in `TF2-001`, `TF2-003`, `TF2-005` and `TF2-007`.
- [Observation | Corroborated | High] The exact two-module route, linked
  platform fight and retained successor terminal are fixed in `TF2-004`,
  `TF2-006`, `TF2-008` and `TF2-010`.

## New genes

- [Observation | Corroborated | High] `ACT-428` and `SYS-787` isolate legal
  transfer from an on-foot operator into direct control of a linked allied
  combat platform.
- [Observation | Corroborated | High] `SYS-786` and `CON-598` isolate ordered
  compatible-module restoration and its power/link/entry threshold.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0251` couples high-mobility
  on-foot traversal, staged allied-platform restoration, link-gated embodiment
  transfer, typed heavy combat and retained chapter settlement.

## Taxonomy changes

- [Observation | Corroborated | High] None: all boundaries are additive and no
  earlier reviewed signature changes.

## New questions

- Does CONTROL's early telekinetic route reuse typed abilities and authored
  chapter retention, or require distinct object-selection and checkpoint
  boundaries?

## Next recommended unit

- [Hypothesis | Limited | High] `GAME-0254` — CONTROL Ultimate Edition.
- Optimisation criterion: isolate one current base-game `Unknown Caller`
  mission without importing expansions or later powers.
- Expected information gain: test telekinetic object use, live cover and
  retained Control Point state against existing physics and checkpoint genes.
- Backlog impact: second game unit in the ordered Batch 014 horizon.

## Why this unit

- [Hypothesis | Limited | High] It is the next fixed ID after completing the
  first selected high-mobility combat and embodiment-transfer packet.
