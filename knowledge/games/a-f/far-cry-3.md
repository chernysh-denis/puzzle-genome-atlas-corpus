---
game_id: GAME-0236
slug: far-cry-3
game_title: Far Cry 3
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0234
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-200
    - ACT-202
    - ACT-235
    - ACT-405
    - ACT-406
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-319
    - SYS-369
    - SYS-373
    - SYS-747
    - SYS-748
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-286
    - CON-330
    - CON-335
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-287
  objective:
    - OBJ-147
  time:
    - TIM-003
---

# Game: Far Cry 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `220240`, public Build ID `13146413`, built 2024-01-11 and published to the
  public branch 2024-03-05, checked 2026-09-03; Ubisoft Connect is the supplied
  launcher. Only the base single-player campaign on `Survivor`, the ordinary
  middle difficulty, is admitted. No unsupported executable-version number is
  inferred from launcher-only updates.
- Entry: on a fresh save, complete the three required introductory missions and
  accept the two Medical syringes and Rucksack produced during `Harvest the
  Jungle`; select `Survivor`, keep the ordinary tutorial loadout without extra
  purchases or crafting, enter Dennis's vehicle, and begin at the first retained
  player control after arrival at the lookout for the fourth story mission.
- Primary decision loop: read the mission objective, local sight, camera tags,
  detection state, health, ammunition and Dennis's exposed health when he joins;
  move and crouch through cover; tag visible hostiles; throw a rock to redirect
  an eligible patrol; take down an unaware reachable target or aim, fire, switch,
  reload and heal under live pressure; clear the closed hostile set; then enter
  the site building and verify the converted location and successor mission.
- Positive terminal: every required pirate and the guard dog is defeated, the
  Amanaki site changes to Rakyat control, the player enters the main building,
  the absent captive is resolved, `Mushrooms in the Deep` becomes the current
  story mission, and the outpost remains an available fast-travel/vendor
  location after exit and relaunch of the same save.
- Negative terminal: Jason's death, Dennis's death after he enters the fight or
  mission-area abandonment fails the attempt and permits only authored
  checkpoint restoration. Detection, open combat, a found body, a spent
  syringe or taking damage are recoverable states, not failure by themselves.
- Included: direct first-person movement and crouch; camera selection and
  target tagging; retained markers; rock diversion; sight-, body- and
  sound-triggered suspicion, search and combat; stealth takedown or ordinary
  unsuppressed firearm combat; finite ammunition, weapon switching and reload;
  two previously required Medical syringes and interruptible healing; Jason and
  conditionally exposed Dennis health; mission failure/checkpoint retry; closed
  hostile clearance; outpost control conversion; safe-house entry, fast-travel
  and vendor availability; successor mission and retained save state.
- Excluded: alarms and reinforcement calls, because this specific first
  outpost has no alarm panel; optional corpse/chest looting, the optional
  AK-47 pickup, animal hunting, skinning, new crafting, skill spending, store
  purchases, Memory Card collection and bounty-board activities; every other
  outpost, radio tower, mission and island route; outpost reset after campaign
  completion; co-op, multiplayer and map editor; their retired online service;
  Deluxe/High Tides/Uplay rewards, Blood Dragon, Classic Edition, consoles,
  mods, trainers, wrappers, cheats and the whole campaign or franchise.
- Reproducible parameterisation: use a clean current English Windows install,
  fresh save, `Survivor`, default mouse/keyboard bindings and default interface
  aids. Preserve the required prior-mission two-syringe state and ordinary
  tutorial weapon; do not buy, craft or collect optional improvements after
  entry. From the lookout, tag the finite hostile set, divert at least one
  eligible patrol with one rock, complete one unaware takedown if a valid state
  remains, finish any remaining defenders by a legal method, enter the main
  building and retain the successor. Exact positions, aim points, damage,
  ammunition, heal use, alert timing and stealth-versus-firefight split are run
  parameters. Repeat only the checkpoint failure branch needed to establish it.
- Potential scoped modules: one later outpost with an alarm and reinforcements,
  one bounded hunting/crafting packet, one later story mission or the lawful
  single-player content of another edition each requires a separate scope.
- Direct-play status: not conducted. Current official distribution/product
  pages, the official PC manual and official online-service notice establish
  the supported product, controls, base systems and offline boundary. Three
  maintained textual route sources establish the exact fourth-mission entry,
  hostile set, absence of an alarm, detection transitions, ally-failure gate,
  site conversion and retained successor. The trace below is evidence-backed
  rules reconstruction, not a claimed captured playthrough. No video or audio
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FC3-001` | The admitted product is the currently distributed Windows Far Cry 3 base game, Steam app `220240`, public Build `13146413`, not Blood Dragon, Classic Edition or a franchise union | Confirmed | Corroborated | High | P1, P2, S1 |
| `FC3-002` | Campaign, co-op, multiplayer and map editor are distinct surfaces; retired online functions are excluded from this single-player packet | Confirmed | Direct | High | P1, P2, P3, P4 |
| `FC3-003` | The official PC manual exposes direct movement, crouch, aim, shoot, reload, melee/takedown, heal, camera, enemy-tagging and rock-diversion controls | Confirmed | Direct | High | P2 |
| `FC3-004` | `Secure the Outpost` follows `Harvest the Jungle`, begins after the required vehicle ride and is the fourth authored story mission | Observation | Corroborated | High | S2, S3, S4 |
| `FC3-005` | Camera observation can tag the finite hostile set and preserve target markers on the world view and map through ordinary occlusion | Observation | Corroborated | High | P2, S2, S4, S5 |
| `FC3-006` | A thrown rock can redirect an eligible unaware guard, enabling a close takedown before completed detection | Observation | Corroborated | High | P2, S2, S3 |
| `FC3-007` | Visible movement, a discovered body, sound or harm can progress local suspicion into search and active combat | Observation | Corroborated | High | S2, S6 |
| `FC3-008` | This first outpost has a closed set of ordinary defenders and one guard dog but no alarm panel, so alarm-triggered reinforcements are not legal in this packet | Observation | Corroborated | High | S2, S3 |
| `FC3-009` | If gunfire starts Dennis joins with visible health; Jason's or Dennis's death fails the mission and allows checkpoint retry | Observation | Corroborated | High | S2, S3 |
| `FC3-010` | Required prior-story crafting supplies two Medical syringes, and an admitted syringe can trade an interruptible live action and finite stock for health | Observation | Corroborated | Medium | P2, S3 |
| `FC3-011` | Defeating every required hostile converts the site from pirate to Rakyat control and makes it a fast-travel/vendor location | Observation | Corroborated | High | P1, S2, S3, S4 |
| `FC3-012` | Entering the main building resolves the missing captive and exposes `Mushrooms in the Deep`; retained outpost and successor access define the positive terminal | Observation | Corroborated | High | S2, S3, S4 |
| `FC3-013` | The bounded identity is reconnaissance-backed live stealth/combat whose finite clearance permanently changes a local world service node | Strong Pattern | Corroborated | High | FC3-004–FC3-012 |

## Basic data

- Release / origin: Ubisoft Montreal with additional Ubisoft studios; Ubisoft;
  original Windows release 2012, current Steam distribution checked 2026-09-03.
- Platform or physical form: authored single-player first-person action game;
  one fixed early story mission on the current Windows base-game package.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Ubisoft Far Cry 3 page](https://www.ubisoft.com/en-us/game/far-cry/far-cry-3),
    for the base product, open-world mission framing and distinct stealth,
    firearms, co-op, multiplayer and map-editor surfaces.
  - **[P2]** [official Windows manual](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/220240/manuals/FarCry3.pdf?t=1682960396),
    for Windows single-player movement, crouch, aim, fire, reload, heal,
    melee/takedown, interaction, camera, tagging, rock and equipment controls.
  - **[P3]** [official Ubisoft online-service notice](https://news.ubisoft.com/en-us/article/hSeUzlOfqN8ZLYSIw6u34/decommissioning-some-online-services-an-update),
    for the 2022 legacy-service closure and the separation of unsupported
    online features from the local campaign.
  - **[P4]** [official Ubisoft Far Cry collection notice](https://www.ubisoft.com/en-us/games/far-cry-silver-pack),
    which explicitly identifies Far Cry 3 multiplayer and online features as
    unavailable while continuing to offer the product collection.
  - **[P5]** [official Steam product page](https://store.steampowered.com/app/220240/Far_Cry_3/),
    for the current Windows sale, Ubisoft Connect requirement, single-player
    product and supported stealth/firearm/outpost framing.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/220240/depots/), observed
    2026-09-03, for application `220240`, Windows depot `220241`, public Build
    ID `13146413`, build date 2024-01-11 and public update 2024-03-05. SteamDB
    is explicitly a secondary distribution mirror.
  - **[S2]** [GameFAQs `Secure the Outpost` route](https://gamefaqs.gamespot.com/xbox360/632849-far-cry-3/faqs/66781/m-4-secure-the-outpost),
    for vehicle entry, camera tags, closed hostile set, no alarm, rock diversion,
    detection/body discovery, Dennis health, failure, conversion, safe-house
    entry, service unlock and successor. Controller labels are not admitted.
  - **[S3]** [Prima `The North Island` eGuide](https://primagames.com/eguides/far-cry-3-with-interactive-map-eguide/walkthrough/the-main-campaign/the-north-island),
    for the prior two-syringe state, lookout arrival, first-outpost route,
    finite clearance, converted fast-travel location and story continuation.
  - **[S4]** [Far Cry Wiki mission record](https://farcry.fandom.com/wiki/Secure_the_Outpost),
    for fourth-mission identity, predecessor/successor, start/end locations and
    Rakyat-control reward.
  - **[S5]** [Far Cry Wiki camera record](https://farcry.fandom.com/wiki/Camera),
    for target-type markers, minimap transfer and ordinary through-wall
    persistence after a camera tag.
  - **[S6]** [Gamer Guides combat guide](https://www.gamerguides.com/far-cry-3/guide/introduction/gameplay/combat),
    for the directional detection indicator and suspicion-to-detected change.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S6` under the fixed build, difficulty, entry, no-alarm
  exclusion and retained-terminal contract; no audiovisual playback or
  direct-play claim.
- Claim IDs: `FC3-001`–`FC3-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate the first-person body through lookout,
  cover, fence gaps and the main building; `ACT-161`: aim and commit firearm or
  ordinary melee attacks; `ACT-164`: select a carried weapon; `ACT-183`: reload
  from finite reserve; `ACT-200`: begin one interruptible Medical-syringe use;
  `ACT-202`: enter or leave crouch; `ACT-235`: neutralise one eligible unaware
  target from valid close range.
- New `ACT-405`: hold the optical device on a visible eligible living target
  long enough to request a retained tactical mark; new `ACT-406`: aim and throw
  one inert non-damaging diversion at a reachable world point.
- The optional AK-47 pickup, loot, crafting and store interactions are outside
  scope rather than action genes. Mission and character names are parameters.
- Claim IDs: `FC3-003`, `FC3-005`, `FC3-006`, `FC3-009`, `FC3-010`.

### System Behaviour Genes

- Existing `SYS-057`: an eligible patrol replaces its route when it perceives
  the explicit rock stimulus; `SYS-208`: ranged shots resolve through body,
  cover and hit state; `SYS-215`: player, pirates, dog and conditionally Dennis
  exchange live attacks; `SYS-319`: an uninterrupted syringe use consumes its
  finite item and restores allowed health; `SYS-369`: accepted death or mission
  failure restores an authored checkpoint; `SYS-373`: sight, discovered bodies,
  sound and harm escalate local suspicion through search to combat.
- New `SYS-747`: a completed optical observation binds a persistent world/map
  marker to that living actor through ordinary occlusion until its state or the
  encounter invalidates the mark. New `SYS-748`: clearing the closed hostile
  set converts the site to the allied state and retains its local travel,
  service and successor affordances.
- Resolution order: accept movement, posture, camera, rock, healing or attack
  input; validate visibility, reach, inventory and awareness; create or update
  marks and diversion/perception state; resolve stealth or live combat; update
  health, ammunition and hostile membership; restore on failure; when the last
  required hostile is defeated, convert the site; on building entry expose the
  successor and retain both states.
- Claim IDs: `FC3-005`–`FC3-012`.

### Constraint Genes

- Existing `CON-262`: current weapon slots, magazine/reserve ammunition and
  syringe stock are finite; `CON-282`: the prior story missions, hostile clear,
  building entry and successor follow authored order; `CON-285`: fire, reload
  and switching require a compatible live weapon state; `CON-286`: a syringe
  requires missing health, compatible stock and an uninterrupted use; `CON-330`:
  Jason, the mission area and conditionally active Dennis must remain viable;
  `CON-335`: close stealth neutralisation requires an eligible unaware target.
- No alarm/reinforcement constraint is admitted: the exact site lacks an alarm
  panel. Hostile identity and count, companion identity, syringes, mission area
  and difficulty are parameters rather than canonical labels.
- Scarce strategic resources: cover and unseen approach time, ammunition,
  syringe stock, Jason health and, after open combat begins, Dennis health.
- Claim IDs: `FC3-006`–`FC3-010`, `FC3-012`.

### Information Genes

- Existing `INF-073`: active weapon, magazine/reserve and carried healing state
  are visible; `INF-115`: avatar-centred sight and explicit spatial effects
  expose only local untagged hostiles; `INF-119`: Jason's health and Dennis's
  conditionally exposed health are visible; `INF-125`: the current objective,
  discovered map, converted travel point and successor gate are inspectable.
- New `INF-287`: the recon interface exposes tagged target identity and
  retained world/map position together with directional suspicion progress, so
  the player can distinguish unobserved, investigating and detected states.
- Exact icon art, colour and screen position are presentation parameters.
- Claim IDs: `FC3-005`, `FC3-007`, `FC3-009`, `FC3-011`, `FC3-012`.

### Objective Genes

- New `OBJ-147`: clear the closed hostile set from one occupied site, enter its
  required local terminal and retain the site's converted control, services
  and authored successor after relaunch.
- One tag, takedown, kill, discovered body, firefight victory or immediate
  liberation banner is intermediate. Optional loot and rewards are not part of
  success; Jason/Dennis death and mission abandonment are explicit failures.
- Claim IDs: `FC3-008`, `FC3-009`, `FC3-011`, `FC3-012`.

### Time Genes

- Existing `TIM-003`: patrols, detection, diversion, combat, damage and ally
  exposure continue while the player observes and supplies live input.
- Menus and checkpoint loading may pause or replace that state without becoming
  a second time model.
- Claim IDs: `FC3-006`–`FC3-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh `Survivor` save has completed the required prior mission | Enter Dennis's vehicle and retain the authored ride | The fourth mission delivers the player to its lookout with ordinary tutorial loadout and two Medical syringes | fixed entry and prerequisites | `FC3-004`, `FC3-010` |
| One eligible hostile is visible from the lookout | Observe it through the camera until tagging completes | A target marker and map symbol bind to that actor and persist through ordinary occlusion | active reconnaissance changes later information | `FC3-003`, `FC3-005` |
| One unaware guard can perceive the chosen ground point | Throw one rock away from the intended route | The guard investigates the explicit stimulus, opening a different approach relation | decoy-driven route diversion | `FC3-006` |
| Diverted guard is unaware and reachable from behind | Commit a takedown | The guard leaves the required hostile set without beginning ordinary firearm exchange if no detection completes | constrained stealth clearance | `FC3-006`, `FC3-008` |
| A pirate sees the player, finds a body or receives harmful/sound evidence | Remain exposed or fire | Suspicion completes, eligible survivors search or fight, and Dennis may enter with visible health | recoverable transition from stealth to combat | `FC3-007`, `FC3-009` |
| Jason has missing health and one required syringe remains | Complete the heal action without cancellation | One syringe is consumed and allowed health is restored | finite recovery under live pressure | `FC3-010` |
| Jason or active Dennis reaches the mission failure state | Accept retry | The current attempt ends and the latest authored checkpoint is restored | reproducible negative terminal and recovery | `FC3-009` |
| Every required pirate and guard dog is defeated | Allow the clearance settlement | The site converts from pirate to Rakyat control and its local services become available | hostile clearance writes persistent world state | `FC3-008`, `FC3-011` |
| Converted site is active | Enter the main building | The captive search resolves and `Mushrooms in the Deep` becomes available | named story handoff after mechanical conversion | `FC3-012` |
| Converted site and successor are saved | Exit and relaunch the same campaign | Travel/vendor access and the successor mission remain available | retained positive terminal | `FC3-011`, `FC3-012` |

## Strategic and experiential structure

- Planning horizon: camera tags convert partial local sight into retained
  target information, then rock placement and cover determine whether the
  finite clearance stays quiet or becomes a live firefight that exposes Dennis.
- Local tactics: observe before crossing the fence; place a rock where one
  guard, not the whole group, can investigate; approach from behind; if alert
  completes, use cover, reload windows and finite healing while protecting both
  mission-critical health states.
- Long-term structure: the closed encounter is not merely a kill count. Its
  clearance rewrites local control, travel/service access and the next authored
  story gate on the persistent save.
- Reversible versus irreversible: movement, tag order, rock placement and
  stealth/open approach vary within the attempt; checkpoint retry replaces a
  failed local state; site conversion and successor availability persist.
- Failure attribution: marker/detection state, health, ammunition, Dennis's
  conditional health and the current mission objective distinguish a failed
  stealth approach from terminal actor loss or incomplete hostile clearance.
- Player trust: camera and directional detection feedback expose risk before
  it commits; the no-alarm exception prevents an undocumented reinforcement
  branch; the converted map/service state confirms terminal persistence.
- Claim IDs: `FC3-005`–`FC3-013`.

## Replay and variation

- What changes between attempts: patrol positions, tag order, rock landing,
  detection timing, takedown count, firearm exchanges, damage, heal use,
  ammunition and checkpoint use.
- Randomness or procedural generation: the site, story order, required hostile
  closure and conversion terminal are authored; continuous actor trajectories
  and combat outcomes vary within that fixed encounter.
- Multiple viable strategies: a mostly silent route, early open assault or a
  mixed route can reach the same terminal, provided the finite set is cleared
  and mission-critical actors survive.
- Typical replay motive: approach optimisation or later outpost-reset play,
  but reset requires completed-campaign state and is excluded here.
- Claim IDs: `FC3-006`–`FC3-012`.

## Adjacent systems and history

- Direct franchise corridor: later Far Cry games may reuse optical marking,
  decoys and outpost conversion, but no franchise-wide signature is inferred.
- Similar lower-ID games: Cyberpunk 2077 shares crouched stealth, constrained
  takedowns, local suspicion and live firearm combat; PAYDAY 2 shares a stealth
  state that can escalate into a recoverable firefight; XCOM 2 shares
  detection-aware hostile clearance but resolves it through discrete tactical
  turns rather than direct real-time embodiment.
- Important differences: this packet makes deliberate optical marking and
  inert-world diversion first-class decisions, excludes alarms for the exact
  site, and makes finite clearance persist as a converted travel/service node
  plus a successor story gate.
- Claim IDs: `FC3-005`–`FC3-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-200`, `ACT-202`, `ACT-235`, `ACT-405`, `ACT-406` | Amanaki, camera model, rock, loadout and target count are parameters |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-319`, `SYS-369`, `SYS-373`, `SYS-747`, `SYS-748` | patrol path, alert timing, health and service identities are parameters |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-286`, `CON-330`, `CON-335` | `Survivor`, two syringes, Dennis and the no-alarm site are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-287` | marker art, colour and HUD placement are presentation |
| Objective | `OBJ-147` | mission, occupied site, factions, services and successor are parameters |
| Time | `TIM-003` | frame rate, animation and checkpoint load duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `235` (`GAME-0001`–`GAME-0235`).
- Exact genome matches: none.
- Tied near matches: `GAME-0222` — Call of Juarez: Gunslinger (`14 / 43 = 0.325581`).
- Supported combination subsets: `COMB-0234`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0222` — Call of Juarez: Gunslinger | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `SYS-215`, `SYS-369`, `CON-262`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Gunslinger follows one authored firefight/duel episode with combo, Concentration and narrator-driven scene replacement. This packet replaces those systems with camera-acquired actor marks, rock diversion, stealth constraints, local alert escalation, finite healing and persistent conversion of a cleared service node. | Near, `0.325581` |

### Preserved research notes

- New genes: `ACT-405`, `ACT-406`, `SYS-747`, `SYS-748`, `INF-287`, `OBJ-147`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-200`,
  `ACT-202`, `ACT-235`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-319`,
  `SYS-369`, `SYS-373`, `CON-262`, `CON-282`, `CON-285`, `CON-286`,
  `CON-330`, `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing combat, stealth, perception, recovery and
  mission gates fit without renaming. New boundaries are limited to deliberate
  optical tagging, persistent actor-bound tactical marks, inert-point
  diversion, retained hostile-site conversion and the terminal that requires
  that conversion plus local service/successor persistence.

## Taxonomy impact

- Registry changes: six new Active genes with portable names and game-scoped
  examples; no existing definition, lifecycle or reviewed signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; mission, site,
  faction, character, target count, difficulty, reward and service names remain
  parameters and do not enter canonical labels.

## Negative results

- No alarm or reinforcement gene is admitted: the exact first outpost has no
  alarm panel and its finite hostile set is closed.
- No looting, inventory-transfer, crafting, skill-allocation, vendor-purchase or
  experience-progression genes are admitted because those transitions are
  optional before or after the declared terminal.
- No open-world traversal, vehicle-operation or general territorial-control
  gene is inferred from the scripted passenger ride and one local site change.
- No previous reviewed signature changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the 30-gene signature. None fit completely. `COMB-0234` is added as
  the strict site-reconnaissance/clearance core and omits optional recovery and
  presentation support.
- Comparison and subset scan date: 2026-09-03.
