---
game_id: GAME-0250
slug: tomb-raider-2013
game_title: Tomb Raider (2013)
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0248
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-226
    - ACT-235
    - ACT-341
    - ACT-423
  system:
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-755
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-326
    - CON-335
  information:
    - INF-073
    - INF-115
    - INF-125
    - INF-300
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Tomb Raider (2013)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `203160`, current store package `26016`, public branch Build ID `9573671`,
  built 2022-09-22 and published 2022-09-27, checked 2026-09-05. The build
  identifier and dates are secondary distribution observations. Steam now
  presents the product as **Tomb Raider Game of the Year**; the analysed game
  is the 2013 reboot, not Tomb Raider: Definitive Edition, Rise of the Tomb
  Raider, Shadow of the Tomb Raider or a classic-series release.
- Entry: use a fresh English New Game on `Normal` and the ordinary base-story
  path. Continue the required opening until first retained control at the foot
  of the Mountain Temple stairway with `Follow Dr. Whitman up the Mountain`
  active. Preserve the naturally acquired bow, climbing axe, ammunition,
  salvage, skills and save state; do not import another save or detour through
  Game of the Year extras.
- Primary decision loop: read the current objective, explored map, local sight,
  weapon/ammunition state and bounded Survival Instinct overlay; traverse,
  jump, scramble, climb, balance and use zip lines; move into or out of
  contextual cover; inspect local actors, usable objects and the objective
  beacon; operate authored doors, breakable barriers and route fixtures; loot
  compatible ammunition and supplies; select, aim, fire and reload the bow or
  pistol; preserve stealth where useful, or resolve live combat; pass the
  mandatory escape and burning-building gates; and continue to the authored
  area transition.
- Positive terminal: leave Mountain Temple through the upper cliff crevice,
  accept the authored transition, retain first ordinary control at the Village
  Plateau base camp in Mountain Village and verify the new `Find Roth's Pack`
  objective. Quit after the resulting autosave, select Continue and confirm
  that the same Mountain Village control, objective and carried state return.
- Negative terminal: death during capture escape, fire, traversal or combat
  ends the current attempt. Continue from the failure surface so the latest
  autosaved checkpoint replaces transient position, weapon/ammunition,
  hostile, pickup and objective state. Returning before the Mountain Village
  transition or losing the successor objective rejects the proposed positive
  terminal.
- Included: one base-story Mountain Temple segment on Normal; direct
  third-person traversal and seamless climbing/crouching/cover transitions;
  map and objective state; held Survival Instinct; capture escape prompts as
  an authored gate; acquired pistol; bow and pistol selection, aim, finite
  ammunition and reload; local hostile sight, suspicion, stealth and combat;
  one eligible quiet close neutralisation; body and supply looting; axe, door,
  fire, breakable barrier, ladder and zip-line interactions; Mountain Temple
  base-camp discovery as an intermediate state; autosave retry; authored area
  transition and retained Mountain Village successor control.
- Excluded: Tomb of the Lost Adventurer, outfits, multiplayer maps and
  characters included by the current Game of the Year offer; every other DLC,
  Multiplayer, community features, achievements and exhaustive collectibles;
  optional challenge completion, relic/document/GPS-cache sweep, treasure-map
  detours, weapon upgrades, skill purchases and Fast Travel revisits; Coastal
  Forest before the entry, Mountain Village activity after first retained
  control and the rest of the campaign; other difficulties, imported saves,
  speedrun skips, glitches, mods, trainers, cheats, console editions, macOS,
  Linux/Proton, Definitive Edition, Rise, Shadow and every earlier Tomb Raider.
- Reproducible parameterisation: preserve application, package, public build,
  English, fresh-save history, Normal difficulty and the first Mountain Temple
  visit. From the declared entry, invoke Survival Instinct at least once while
  an objective and one local usable or attackable object can be distinguished;
  enter and leave compatible cover; acquire and retain the pistol; switch
  between available weapons; fire and reload the pistol; perform one quiet
  neutralisation on an eligible unaware hostile; loot one body or compatible
  supply; open one authored door and break one route obstruction; pass the
  capture, first firefight, burning-building, upper ambush and final crevice
  gates; then Continue once from the retained Village Plateau autosave. Exact
  route line, combat order, aiming, enemies defeated, damage, ammunition,
  salvage, pickups, prompt timing, camp use and completion time are run
  parameters.
- Potential scoped modules: the opening through Coastal Forest; the first
  Mountain Village visit; one optional challenge tomb; a later traversal-tool
  packet; one complete story chapter; Multiplayer; a Game of the Year DLC; or
  a named console/Definitive Edition build each requires a separate scope.
- Direct-play status: not conducted. Current Valve product and package data,
  the Square Enix/Feral official manual and static written area evidence
  establish lawful availability, package boundaries, controls, traversal,
  Survival Instinct, combat, resources, checkpoints, Mountain Temple order and
  the Mountain Village successor. This is evidence-backed rules
  reconstruction, not a claimed captured playthrough or entitlement. No video
  or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TR13-001` | The selected product is the current English Windows Steam app `203160`, store package `26016`, titled Tomb Raider Game of the Year and containing the 2013 reboot | Confirmed | Direct | High | P1, P2 |
| `TR13-002` | Steam public Build `9573671` is the current observed Windows distribution state | Observation | Corroborated | High | P1, S1 |
| `TR13-003` | The Game of the Year offer adds one optional tomb, outfits and multiplayer content, all excluded from the base-story packet | Confirmed | Direct | High | P1 |
| `TR13-004` | New Game offers Easy, Normal and Hard; the packet fixes Normal and one fresh save slot | Confirmed | Direct | High | P3, P4 |
| `TR13-005` | Direct movement seamlessly enters climbing, crouching and cover, while ledges, scrambles and recovery prompts gate traversal | Confirmed | Direct | High | P3, P4 |
| `TR13-006` | Map state exposes the current location and objective, while Survival Instinct temporarily highlights usable or attackable objects and the objective beacon | Confirmed | Direct | High | P3, P4 |
| `TR13-007` | The base game supports bow/pistol selection, aimed fire, reload, stealth and close combat with finite ammunition and compatible loot | Confirmed | Direct | High | P3, P4 |
| `TR13-008` | Mountain Temple begins with the Whitman ascent, capture escape and pistol acquisition before the first firearm encounter | Observation | Corroborated | High | S2 |
| `TR13-009` | The route uses contextual cover, axe/door and breakable-building interactions, then teaches silent bow and close stealth attacks across live hostile groups | Observation | Corroborated | High | P3, S2 |
| `TR13-010` | Mountain Temple's base camp and Fast Travel unlock are intermediate; optional collection, upgrades and challenge progress are unnecessary to reach the exit | Observation | Corroborated | High | P3, S2 |
| `TR13-011` | The final zip-line and upper-stair route ends at a narrow cliff crevice that transitions into Mountain Village | Observation | Corroborated | High | S2, S3 |
| `TR13-012` | Autosave checkpoints restore failed attempts, and the successor state exposes Village Plateau with `Find Roth's Pack` | Observation | Corroborated | High | P3, S2, S3 |
| `TR13-013` | The bounded identity is a sensed, cover-aware stealth/combat ascent whose authored environmental gates and finite resources carry into a retained successor area | Strong Pattern | Corroborated | High | `TR13-005`–`TR13-012` |

## Basic data

- Release / origin: developed by Crystal Dynamics with Windows work credited
  on the current store page; published in 2013. Steam currently sells the
  application as **Tomb Raider Game of the Year**.
- Platform or physical form: lawfully available English Windows Steam client,
  current package `26016`; one offline single-player base-story segment.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=203160&cc=ua&l=english),
    for current title, app identity, Windows availability, release date,
    purchase options and current Game of the Year content statement.
  - `P2` — [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=26016&cc=ua&l=english),
    for the selected store package and its one `203160` application.
  - `P3` — [official Tomb Raider Steam manual](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/203160/manuals/TRpcMANOLeUS.pdf),
    for New Game/save slots, Normal difficulty, Windows controls, direct
    traversal, map/objective state, camps, Survival Instinct, pickups, weapons,
    stealth, combat, salvage, skills and upgrades.
  - `P4` — [Square Enix support manual](https://support.na.square-enix.com/document/manual/6501/Manual.pdf),
    for an independent official copy of the same PC control, difficulty,
    traversal, map, camp, sensing, combat and resource rules.
- Corroborating textual sources, accessed 2026-09-05:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/203160/depots/),
    for Windows depots and public Build `9573671`, built 2022-09-22 and
    published 2022-09-27. SteamDB is a secondary distribution mirror.
  - `S2` — [Stella's Mountain Temple text walkthrough](https://tombraiders.net/stella/walks/TR9walk/04-mountain-temple.html),
    for autosave semantics, ordered objectives, capture escape, pistol,
    cover/firefight, fire and door gates, stealth teaching, base camp, upper
    ambush, zip line and final crevice transition. Optional collection advice
    and linked audiovisual material were not used.
  - `S3` — [Stella's Mountain Village text walkthrough](https://tombraiders.net/stella/walks/TR9walk/05-mountain-village.html),
    for the retained Village Plateau control and `Find Roth's Pack` successor
    objective. No Mountain Village activity enters this packet.
- Claim IDs: `TR13-001`–`TR13-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly traverse, jump, scramble, climb, balance and
  ride authored route edges; `ACT-226`: move into, along or out of compatible
  contextual cover; `ACT-423`: hold Survival Instinct to inspect bounded
  nearby actor, objective and interactable state; `ACT-341`: operate an
  eligible door, barrier, ladder, pickup or route object.
- Existing `ACT-164`: select an available bow or pistol; `ACT-161`: aim and
  commit a ranged or close attack; `ACT-183`: reload the pistol from compatible
  reserve; `ACT-235`: neutralise one eligible unaware target from close range;
  `ACT-199`: transfer one reachable compatible weapon, ammunition or supply
  pickup into carried state.
- Prompt identity, route object, weapon, ammunition, hostile, cover surface and
  area names are parameters. The mandatory capture struggle remains an
  authored transition gate: its displayed responses do not create an editable
  sequence, graded timing policy or reusable choice vocabulary in this packet.
  Claims: `TR13-005`–`TR13-012`.

### System Behaviour Genes

- Existing `SYS-208`: aimed bow and pistol shots resolve through range, cover
  and body hit; `SYS-215`: hostile movement, attack and player combat resolve
  in live time; `SYS-373`: sight, sound and harmful action advance local
  awareness from hidden approach into search or combat; `SYS-755`: sufficient
  accepted interaction or damage removes an eligible barrier or exposes its
  route opening; `SYS-369`: death and Continue replace failed transient state
  with the latest authored checkpoint.
- Resolution order: expose local route and bounded information; accept
  traversal, sensing, cover, interaction, pickup, selection, attack, reload or
  stealth input; validate geometry, awareness, weapon and ammunition; update
  perception and live combat; settle barriers and pickups; replace death from
  checkpoint; advance mandatory objectives; then cross the crevice trigger and
  retain Mountain Village state. Claims: `TR13-005`–`TR13-012`.

### Constraint Genes

- Existing `CON-262`: carried weapon choices and finite ammunition constrain
  the live route; `CON-285`: fire, selection and reload require a compatible
  weapon, magazine, reserve and action state; `CON-326`: contextual cover
  attachment and exposure require compatible reachable geometry; `CON-335`:
  the quiet close neutralisation requires an unaware reachable target;
  `CON-282`: capture, firefight, door, fire, stealth, ambush and exit states
  advance only through their authored dependencies.
- Scarce strategic resources: safe route position, concealment, cover,
  ammunition, weapon readiness and retained checkpoint progress. Salvage,
  skill points, collectible counts and exact hostile numbers are parameters or
  excluded optional progress, not canonical constraints. Claims:
  `TR13-007`–`TR13-012`.

### Information Genes

- Existing `INF-073`: available carried weapon and ammunition state are
  visible; `INF-115`: ordinary sight, spatial sound and local effects expose
  only nearby opponents and actions; `INF-125`: explored terrain, camps,
  objective marker and current authored requirement are inspectable;
  `INF-300`: invoked Survival Instinct distinguishes nearby usable or
  attackable objects and the objective beacon while leaving future state
  unknown.
- Exact icon, colour, silhouette, prompt art, marker and screen position are
  presentation parameters. Claims: `TR13-005`–`TR13-012`.

### Objective Genes

- Existing `OBJ-026`: traverse one bounded authored environment and make its
  designated successor location reachable; here success is retained first
  control at Village Plateau with `Find Roth's Pack` after reload.
- Pistol acquisition, first firefight, the Mountain Temple camp, the upper
  ambush and final zip line are intermediate. Death and checkpoint return are
  retries, not alternate positive terminals. Claims: `TR13-008`–`TR13-013`.

### Time Genes

- Existing `TIM-003`: traversal hazards, hostile perception, attacks, aim,
  reload, fire pressure and route interactions progress continuously outside
  the map, pause and authored transition surfaces. Claims:
  `TR13-005`–`TR13-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Normal story save reaches the first Mountain Temple stair | Accept control and follow the current objective | Whitman ascent advances into capture with the declared prior equipment and story state | reproducible entry | `TR13-004`, `TR13-008` |
| Capture escape has begun | Follow each currently displayed struggle, aim and fire response | Accepted responses free the protagonist, grant the pistol and restore the bow; a missed required response causes death/checkpoint retry | authored prompt gate, not an editable sequence puzzle | `TR13-008`, `TR13-012` |
| A low protective surface is reachable during hostile pressure | Move into cover, shift along it, aim from it and deliberately leave | Seamless posture follows compatible geometry; exposure resumes when the movement leaves protection | contextual cover decision | `TR13-005`, `TR13-009` |
| Pistol is active with a partly empty magazine and compatible reserve | Reload | Fire readiness pauses while compatible reserve enters the magazine | finite ammunition timing | `TR13-007` |
| A living hostile is unaware and reachable from behind | Approach without completed detection and commit the shown close interaction | A legal quiet neutralisation resolves; detection or lost reach removes the opportunity | stealth eligibility | `TR13-007`, `TR13-009` |
| One local objective and eligible object are nearby | Hold Survival Instinct, inspect, then release | The bounded overlay distinguishes usable or attackable state and the objective beacon without disclosing the complete future route | local decision information | `TR13-006` |
| The first burning building is sealed and fire pressure continues | Force the door, cross the interior and break the boarded opening | Accepted authored interactions remove the local route barriers before lethal delay | environment-gated escape | `TR13-009` |
| The upper burning-building hostile group is active | Preserve stealth or fight, then use the available zip line | Live perception and combat settle enough of the authored route for traversal to continue | mixed stealth/combat ascent | `TR13-009`–`TR13-011` |
| The final stair and narrow upper crevice are reachable | Enter the crevice and advance through the transition | Mountain Temple closes into first Village Plateau control and exposes `Find Roth's Pack` | authored positive terminal | `TR13-011`, `TR13-012` |
| Village Plateau state has autosaved | Quit, choose Continue and inspect location, objective and carried state | The successor control and objective return from retained storage | terminal retention verification | `TR13-012` |
| Death occurs before the successor transition | Choose Continue | Latest checkpoint state replaces transient position, resources, hostiles and objective progress | reproducible negative terminal | `TR13-012` |

## Strategic and experiential structure

- Planning horizon: preserve enough ammunition, safe route position and
  concealment to pass the next authored gate; distinguish mandatory ascent
  from optional camp, challenge and collectible detours.
- Local tactics: invoke Survival Instinct for bounded state, move with seamless
  cover, use quiet bow or close attacks before detection, switch to pistol and
  reload when pressure escalates, then convert cleared space into traversal.
- Medium-term structure: capture removes options, the struggle grants a pistol,
  the first firefight teaches cover, fire/door gates couple movement to
  interaction, later groups test stealth and the crevice writes successor
  state.
- Reversible versus irreversible: aim, sensing, cover and route positioning are
  locally revisable; spent ammunition, defeated actors and collected supplies
  change the attempt; death replaces the branch from checkpoint; the area
  transition and autosave retain Mountain Village progress.
- Failure attribution: current objective, Survival Instinct overlay, cover
  pose, weapon/ammunition HUD, hostile awareness, route opening and autosave
  return distinguish route, information, combat, resource and retention
  failures.
- Player trust: highlights describe current local state rather than future
  solutions; cover must correspond to protective geometry; weapon operations
  must obey the visible stock; a checkpoint retry must discard failed
  transient state; the positive terminal must survive Continue. Claims:
  `TR13-005`–`TR13-013`.

## Replay and variation

- What changes between attempts: exact cover line, sensing cadence, hostile
  order, quiet versus loud engagement, shots, reload timing, damage, pickups,
  ammunition, salvage, checkpoint state and completion time.
- Randomness or procedural generation: the admitted geometry, objectives,
  capture, combat regions, burning-building gates and successor are authored.
  Live hostile positions and resource outcomes may vary within that route.
- Multiple viable strategies: some encounters permit quiet bow/close removal
  or open pistol combat, while optional supplies can change ammunition margin.
  Mandatory struggle and traversal gates still fix the packet's order.
- Typical replay motive: cleaner traversal, stealth, combat or resource use.
  Full collection, challenges, upgrades and campaign continuation remain
  outside this unit.
- Claims: `TR13-004`–`TR13-012`.

## Adjacent systems and history

- Direct product corridor: the current store title and Game of the Year offer
  are distribution boundaries, not permission to merge DLC, Multiplayer,
  Definitive Edition, Rise or Shadow into the 2013 base story.
- Similar lower-ID games: STAR WARS Jedi: Fallen Order shares authored
  third-person traversal, local combat, map/objective state, checkpoint return
  and a retained next-region route; Far Cry 3 shares local detection, stealth,
  aimed weapons, finite ammunition and a retained story transition; Half-Life
  2 shares an authored environmental route, ranged combat, breakable objects
  and checkpointed chapter succession.
- Important differences: this packet uses seamless context-sensitive climbing
  and cover, a bounded object/objective highlighting overlay, a forced capture
  reversal and mixed stealth/combat environmental ascent into an area autosave;
  it has no Jedi guard/Force loop, optical actor marks/site conversion or
  Gravity Gun object physics. Claims: `TR13-005`–`TR13-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-226`, `ACT-235`, `ACT-341`, `ACT-423` | traversal, weapon, pickup, cover, prompt and interaction values |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-755` | hit, perception, checkpoint and breakage values |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-326`, `CON-335` | equipment, ammunition, cover, awareness and route dependencies |
| Information | `INF-073`, `INF-115`, `INF-125`, `INF-300` | local overlay, map, objective and interface presentation |
| Objective | `OBJ-026` | entry, successor location, autosave and retained objective |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `249` (`GAME-0001`–`GAME-0249`).
- Exact genome matches: none.
- Tied near matches: `GAME-0248` — HITMAN World of Assassination (`20 / 39 = 0.512821`).
- Supported combination subsets: `COMB-0248`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0248` — HITMAN World of Assassination | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-235`, `ACT-341`, `ACT-423`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `CON-262`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-125`, `INF-300`, `TIM-003` | Both combine an invoked bounded overlay with direct traversal, local awareness, stealth, live aimed combat, authored interactions and checkpoint retry. HITMAN adds a thrown diversion, acquired disguises, role-dependent legality, exceptional recognition, a two-target exit and aggregate conduct debrief; Tomb Raider adds seamless contextual cover, compatible pickup transfer, destructible route barriers and a retained successor location. | Near, `0.512821` |

### Preserved research notes

- New genes: none.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`,
  `ACT-226`, `ACT-235`, `ACT-341`, `ACT-423`, `SYS-208`, `SYS-215`,
  `SYS-369`, `SYS-373`, `SYS-755`, `CON-262`, `CON-282`, `CON-285`,
  `CON-326`, `CON-335`, `INF-073`, `INF-115`, `INF-125`, `INF-300`,
  `OBJ-026` and `TIM-003`.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: existing movement, combat, contextual cover,
  stealth, interaction, pickup, checkpoint, weapon, perception, map and
  situational-overlay boundaries fit without revision. Product title, area,
  character, weapon, route, prompt, pickup and numeric values remain
  parameters.
- Lower-ID scan: reject `ACT-202`, because crouching and cover transitions are
  seamless consequences of direct movement rather than a free-standing
  posture command; reject `ACT-370`, because Survival Instinct exposes local
  objective/interactable state rather than submitting investigative evidence;
  reject `SYS-735`, because the overlay does not survey resource identities and
  bearings into retained markers; reject `SYS-398`, because the acquired
  pistol is carried equipment, not a source-free traversal/world-interaction
  capability; reject `OBJ-155`, because Mountain Temple has no explicit
  numbered chapter-completion/save surface. The mandatory struggle prompts are
  kept as parameters of `CON-282`: they neither reproduce a previously shown
  sequence (`ACT-076`) nor grade a freely chosen combat action (`ACT-222`).

## Taxonomy impact

- Registry changes: none. All 25 genes retain their reviewed portable
  definitions, lifecycle states and lower-ID supporting signatures.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Tomb Raider,
  Game of the Year, Mountain Temple, Mountain Village, Village Plateau, Lara,
  Whitman, Roth, Survival Instinct, pistol, bow, climbing axe, Normal and the
  objective strings remain product, interface or game-scoped parameters.

## Negative results

- No direct-play, local-entitlement, screenshot, video or audio claim.
- No DLC, Multiplayer, collectible sweep, challenge, upgrade, later-area,
  whole-campaign, sequel, remaster, platform or live-history union.
- No earlier reviewed signature, gene definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry is tested as a proper
  subset of this 25-gene signature; none of the 247 earlier combinations fits
  completely. `COMB-0248` records the strict contextual-cover, bounded-sensing,
  stealth/combat, environmental-gate and retained-area core; it omits generic
  pickup, weapon switching, ammunition, body-hit and map-detail support.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current Windows product/package availability,
  Normal difficulty and official base mechanics are fixed in `TR13-001`–
  `TR13-007`.
- [Observation | Corroborated | High] Mountain Temple's ordered route,
  checkpoints and retained Mountain Village boundary are fixed in `TR13-008`–
  `TR13-012`.

## New genes

- [Confirmed | Corroborated | High] None; the complete decomposition reuses 25
  reviewed portable genes without semantic revision.

## New combinations

- [Observation | Corroborated | High] `COMB-0248` captures a bounded sensed
  ascent where contextual cover, stealth/combat and environmental interactions
  carry one authored route into retained successor-area control.

## Taxonomy changes

- [Observation | Corroborated | High] None; no prior signature, definition or
  lifecycle state changes.

## New questions

- Does the next selected horror-action packet preserve authored checkpoint
  pressure while replacing directed traversal and sensing with a fixed-room
  enemy/resource puzzle?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0251` — Hades.
- Optimisation criterion: retain real-time combat, finite attempt resources and
  checkpoint consequence while changing the authored route into one bounded
  escape-attempt chamber sequence with offered-build choices.
- Expected information gain: distinguish run-local boon composition, room
  reward forecasting and death-settled meta progression from contextual cover,
  highlighted traversal and a fixed successor-area route.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Hades keeps continuous combat and short-horizon
  route pressure near-constant while replacing Tomb Raider's fixed ascent,
  cover and Survival Instinct with run-local power choices, chamber rewards and
  an explicit death settlement.
