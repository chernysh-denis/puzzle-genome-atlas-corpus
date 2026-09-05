---
game_id: GAME-0261
slug: the-last-of-us-part-i
game_title: The Last of Us Part I
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0259
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-200
    - ACT-202
    - ACT-235
    - ACT-341
    - ACT-406
    - ACT-409
    - ACT-423
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-407
    - SYS-578
    - SYS-780
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-286
    - CON-297
    - CON-335
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-132
    - INF-268
    - INF-300
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: The Last of Us Part I

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1888930`, one-app Standard package `829080`, public Windows Build ID
  `18995818`, built 2025-06-25 and published 2025-07-03, with official PC patch
  `v1.1.5`; checked 2026-09-05. The build identifier and timestamps are
  secondary distribution observations, while the semantic patch version and
  its performance/stability scope come from Naughty Dog.
- Product boundary: this is **The Last of Us Part I** on Windows, not the 2013
  PlayStation 3 original, The Last of Us Remastered, The Last of Us Part II
  Remastered, another platform, a franchise union or an inferred future patch.
  Although the application includes `Left Behind`, that separate story is not
  part of this packet.
- Platform, input and difficulty: English interface and subtitles, Windows,
  keyboard and mouse, fresh base-story `New Game`, default settings and
  `Moderate`. Controller, consoles, Steam Deck-specific settings, accessibility
  presets or assists, `Very Light`, `Light`, `Hard`, `Survivor`, `Grounded`,
  custom difficulty, speedrun mode and permadeath are separate packets.
- Setup-only predecessor: complete the mandatory fresh `Prologue` without
  importing chapter-select or New Game Plus state. It establishes a clean
  story save but contributes no genes or transitions to this packet.
- Entry: after the twenty-year transition, accept first ordinary control at
  the beginning of `20 Years Later`, the first subchapter of `The Quarantine
  Zone`, before following Tess from the apartment. Record Health, carried
  items and ammunition before the first transfer or combat action.
- Primary decision loop: read the current instruction, route cue, local sight,
  Health, carried items, weapon and ammunition; walk, climb, crouch and cross
  the authored quarantine route; lift and place the required ladder and plank
  and move the required dumpster through contextual interaction; toggle the
  flashlight in the dark spore route; hold Listen Mode to inspect bounded
  nearby actor silhouettes through occlusion; collect compatible weapons,
  ammunition, components, a health kit and a melee tool; heal once after
  missing Health; craft exactly one shiv from the known blade-and-binding
  recipe; select, aim, strike, fire and reload; silently grab and neutralise
  one unaware reachable hostile or throw one inert brick or bottle to redirect
  attention; survive recoverable combat; follow the ordered Tess, Robert,
  Marlene and Ellie gates into the next chapter.
- Positive terminal: after the final `The Cargo` route, move the required
  dumpster, enter the apartment and accept the transition into `The Outskirts`
  subchapter `Outside`. At its first ordinary Joel control with Tess and Ellie,
  before moving the bookshelf or operating the hidden generator, create a
  manual save, quit, load that save and verify the same ordinary `Outside`
  control and current route state. Stop without advancing farther.
- Negative terminal: zero Health ends the current attempt; continue or load
  restores the latest authored checkpoint and replaces failed transient
  position, Health, inventory spend, ammunition, hostile, awareness and route
  state. Reaching Robert, meeting Marlene or Ellie, moving the final dumpster
  or watching the transition without the stated reload check is not success.
- Included: direct third-person movement, climbing and crouch; required ladder,
  plank, doors and dumpster; local sight and text/tutorial cues; flashlight;
  ordinary Listen Mode; pickups, carried inventory, weapon selection, finite
  magazine/reserve ammunition and reload; one health-kit treatment; one known
  stationless shiv craft; one inert diversion; one unaware close
  neutralisation; recoverable stealth-to-combat escalation; autonomous
  authored companion follow/combat help; Health, checkpoints, manual saving and
  the retained chapter handoff.
- Excluded: all `Prologue` mechanics beyond clean setup; `Left Behind`; Digital
  Deluxe, preorder or early-unlock content; modifiers, skins, filters, mirror
  world, photo mode, speedrun, permadeath and New Game Plus; enhanced Listen
  Mode, navigation assistance, invisibility, combat assists or other
  accessibility-altered rules; all difficulties, inputs and platforms not
  declared above; `The Outskirts` actions after first control, every later
  chapter, workbench upgrades, supplements, skill trees, weapon holsters,
  locked shiv doors, bows, bombs, smoke bombs, Molotov cocktails and the full
  crafting set; exhaustive kills, stealth, collectibles, conversations,
  jokes, artefacts, pendants, safes, achievements and campaign endings;
  screenshots, official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `1888930` from Standard
  package `829080`, verify public Build `18995818` / PC `v1.1.5`, start a clean
  base-story `New Game` on `Moderate`, retain default keyboard/mouse bindings
  and finish the setup-only `Prologue`. From first `20 Years Later` control,
  follow only required gates; carry and place the ladder and plank, use the
  flashlight in the dark route, observe one hostile through ordinary Listen
  Mode, take one bounded hit and complete one health-kit treatment, collect
  the fixed early components and craft one shiv, perform one unaware close
  neutralisation, throw one brick or bottle to a reachable diversion point,
  fire and reload once, accept companion assistance and complete the Robert,
  Marlene and Ellie handoffs. Enter `Outside`, then perform the stated manual
  save/load terminal. Exact Health, ammunition, components, hostile, diversion
  object, landing point and timing are parameters.
- Potential scoped modules: one later named chapter; `Left Behind`; one
  workbench-upgrade or supplement packet; one locked-shiv-door route; one
  custom-difficulty or accessibility-assist ruleset; New Game Plus, speedrun or
  permadeath; or another platform requires its own version, entry, loop,
  terminal and evidence.
- Direct-play status: not conducted. Valve application/package data, the
  current Steam page and Naughty Dog/PlayStation pages establish lawful
  availability, exact product identity, Windows controls, patch, product-mode
  separation, difficulty/accessibility settings, Listen Mode controls and
  manual saving. Four independent static written route publications
  corroborate subchapter order, traversal objects, flashlight, pickups,
  crafting, stealth, combat, companion gates and the `Outside` transition.
  This is an evidence-backed rules reconstruction, not a claimed playthrough
  or entitlement. No video or audio was opened, played, heard, analysed or
  used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TLO-001` | Steam app `1888930` and one-app Standard package `829080` identify the currently lawfully offered English Windows product, distinct from other series releases | Confirmed | Direct | High | P1–P3 |
| `TLO-002` | The ordinary public Windows branch reports Build `18995818`, published 2025-07-03, and Naughty Dog identifies the current semantic PC patch as `v1.1.5` | Confirmed | Corroborated | High | P4, S1 |
| `TLO-003` | `Left Behind` is included but separate, while Digital Deluxe and early unlocks add content outside the Standard base-story packet | Confirmed | Direct | High | P1–P3, P5 |
| `TLO-004` | A clean `Moderate` route reaches `20 Years Later` after the mandatory setup-only `Prologue` and then advances through `Beyond the Wall`, `The Slums` and `The Cargo` | Observation | Corroborated | High | S2–S5 |
| `TLO-005` | Required ladder, plank, door and dumpster interactions change reachable route geometry in the declared subchapters | Observation | Corroborated | High | S2–S5 |
| `TLO-006` | Ordinary Listen Mode is a held local overlay that exposes bounded nearby actor silhouettes through occlusion and ends when released | Confirmed | Corroborated | High | P6, S2, S5 |
| `TLO-007` | Pickups supply finite compatible weapons, ammunition, components and health items; firearm use validates selection, magazine and reserve state | Observation | Corroborated | High | P2, S2–S5 |
| `TLO-008` | The early route teaches a known stationless shiv recipe whose accepted craft consumes blade and binding into one carried shiv | Observation | Corroborated | High | S3, S6, S7 |
| `TLO-009` | A carried health kit restores missing Health only after its interruptible treatment completes | Observation | Corroborated | High | P6, S2, S5 |
| `TLO-010` | Unaware reachable hostiles admit close grab/neutralisation, while a deliberately thrown inert brick or bottle can redirect eligible attention | Observation | Corroborated | High | S2–S5 |
| `TLO-011` | Perception can escalate stealth into live combat without invalidating the chapter, and zero Health restores an authored checkpoint on retry | Observation | Corroborated | High | S2–S5 |
| `TLO-012` | Tess and other authored allies follow, traverse and provide autonomous local combat or fixed route assistance without becoming a second player-controlled role | Observation | Corroborated | High | S2–S5 |
| `TLO-013` | The final Cargo apartment transition closes `The Quarantine Zone` and admits first ordinary `The Outskirts: Outside` control before the bookshelf/generator route | Observation | Corroborated | High | S2–S5 |
| `TLO-014` | Manual saving and loading can retain that first successor-control state, making it a reproducible positive terminal | Confirmed | Corroborated | High | P5, P6, S2–S5 |
| `TLO-015` | The bounded identity is listening-mediated stealth, finite stationless preparation and companion-supported authored traversal settling into reload-verified successor control | Strong Pattern | Corroborated | High | `TLO-004`–`TLO-014` |

## Basic data

- Release / origin: Naughty Dog and Iron Galaxy Studios; published on Windows
  by PlayStation Publishing LLC on 2023-03-28.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `1888930`; one fresh `Moderate` base-story `The Quarantine
  Zone` packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1888930&cc=ua&l=english),
    for the exact title, app, Windows support, single-player category,
    developers, publisher, release date, accessibility fields, packages and
    current Ukraine offer.
  - **[P2]** [Valve Standard-package data](https://store.steampowered.com/api/packagedetails?packageids=829080&cc=ua&l=english),
    for package `829080` containing only app `1888930`, Windows support and its
    current Ukraine offer.
  - **[P3]** [current Steam product page](https://store.steampowered.com/app/1888930/The_Last_of_Us_Part_I/?l=english),
    for lawful availability, base single-player story, Windows input/features,
    included `Left Behind`, Digital Deluxe separation and early unlocks.
    Embedded media was not opened or used.
  - **[P4]** [Naughty Dog PC `v1.1.5` patch note](https://feedback.naughtydog.com/hc/en-us/articles/38999289857556-The-Last-of-Us-Part-I-v1-1-5-Patch-Notes-for-PC),
    updated 2025-07-03, for the current semantic patch and its performance,
    stability and FSR scope.
  - **[P5]** [Naughty Dog PC features and specifications](https://www.naughtydog.com/blog/the_last_of_us_part_i_pc_features_specs),
    for the PC adaptation, keyboard/mouse remapping, base campaign, separate
    `Left Behind` and mode framing.
  - **[P6]** [official PlayStation accessibility feature list](https://blog.playstation.com/2022/08/26/the-last-of-us-part-i-full-list-of-accessibility-features/),
    together with the [current product page](https://www.playstation.com/en-us/games/the-last-of-us-part-i/),
    for ordinary Listen Mode hold/toggle, crafting/treatment hold controls,
    adjustable difficulty, manual saving and the separation of optional
    assists from the default ruleset.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1888930/depots/),
    for public Windows Build `18995818`, its build/publish timestamps and
    English no-DLC depot observation. SteamDB is secondary and is not treated
    as the publisher.
  - **[S2]** [Walkthroughs.games static Quarantine Zone route](https://walkthroughs.games/lorebase/the-last-of-us/missions/quarantine-zone),
    for subchapter sequence, ladder, plank, flashlight, Listen Mode, runners,
    health kit, pistol, stealth, brick/bottle, Robert, Marlene, Ellie and the
    final gate. Images were not opened or used.
  - **[S3]** [GameFAQs static written walkthrough](https://gamefaqs.gamespot.com/pc/370167-the-last-of-us-part-i/faqs/67221),
    for independent Slums/Cargo traversal, pickup, shiv, stealth, diversion,
    combat, companion and apartment-transition corroboration.
  - **[S4]** [Gamer Guides static `The Cargo` route](https://www.gamerguides.com/the-last-of-us-part-i/guide/walkthrough/the-quarantine-zone/the-quarantine-zone-the-cargo),
    together with its linked Quarantine Zone subchapters, for the authored
    chapter order, Robert/Marlene/Ellie chain, final dumpster/door and next-
    chapter transition. Images and embedded media were not opened or used.
  - **[S5]** [Push Square static Part I walkthrough index](https://www.pushsquare.com/guides/the-last-of-us-1-guide-a-full-100percent-walkthrough),
    together with its linked Cargo page, for the four Quarantine Zone
    subchapters and the transition from Cargo to `The Outskirts: Outside`.
    Images and embedded media were not opened or used.
  - **[S6]** [TrueTrophies static Quarantine Zone walkthrough](https://www.truetrophies.com/game/The-Last-of-Us-Part-I/walkthrough/5),
    for the early shiv pickup and unlocked shiv-crafting capability.
  - **[S7]** [PlayStationTrophies static crafting record](https://www.playstationtrophies.org/game/the-last-of-us-part-i/trophy/482703-geared-up.html),
    for independent blade-plus-binding shiv-recipe corroboration in the
    Quarantine Zone route.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S7` under the declared app, package, build, patch,
  platform, input, difficulty, clean setup, exclusions and retained terminal;
  rules reasoning, not direct play.
- Claim IDs: `TLO-001`–`TLO-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk, sprint, climb and traverse reachable authored
  space; `ACT-202`: crouch for low passages and concealment; `ACT-048`: lift,
  carry and place the required ladder or plank; `ACT-341`: operate authored
  doors, the final dumpster and fixed companion-assist gates; `ACT-409`: toggle
  the personal flashlight.
- Existing `ACT-199`: collect compatible weapons, ammunition, components,
  health items and melee tools; `ACT-164`: select a carried weapon or item;
  `ACT-183`: reload a magazine-fed firearm; `ACT-161`: aim and commit a direct
  firearm or melee attack; `ACT-200`: complete one interruptible health-kit
  treatment.
- Existing `ACT-123`: select the known shiv recipe and craft one output from
  blade and binding; `ACT-423`: hold and release ordinary Listen Mode;
  `ACT-235`: grab and neutralise one unaware reachable hostile; `ACT-406`:
  throw one inert brick or bottle toward a reachable diversion point.
- Actor, item, weapon, component, object, fixture, binding and exact quantity
  names remain parameters. Claims: `TLO-005`–`TLO-012`.

### System Behaviour Genes

- Existing `SYS-208`: firearm aim, obstruction and struck region resolve the
  hit; `SYS-215`: movement, perception, attacks, damage and defeat continue in
  real time; `SYS-578`: attacks change continuous Health, completed treatment
  restores missing Health and zero ends the attempt; `SYS-369`: retry restores
  an authored checkpoint.
- Existing `SYS-373`: local movement, sight, sound or harm escalates suspicion
  into detection and combat; `SYS-057`: an eligible hostile can replace its
  current attention with a perceived player or deliberately positioned inert
  stimulus; `SYS-407`: an authored allied companion follows and independently
  supplies eligible traversal, attack or support behaviour beside direct
  protagonist control.
- Existing `SYS-780`: completing the final Cargo transition and saving retains
  ordinary control in the immediate `Outside` successor state.
- Resolution order: direct movement changes reach and sight; Listen Mode
  exposes bounded current actor state; pickup/crafting validates compatibility
  and ingredients; weapon/treatment inputs validate live equipment and meter
  state; thrown stimuli and player exposure update hostile attention;
  companions resolve only their authored autonomous help; zero Health restores
  a checkpoint; the final apartment gate admits the reloadable successor.
  Claims: `TLO-006`–`TLO-015`.

### Constraint Genes

- Existing `CON-262`: carried weapon classes, item slots, magazines and reserve
  ammunition are finite; `CON-285`: fire and reload require compatible weapon,
  ammunition and current action state; `CON-286`: the health kit requires
  missing Health and an uninterrupted eligible treatment interval.
- Existing `CON-297`: the shiv craft requires the known recipe, blade, binding,
  output capacity and no workstation; `CON-335`: close neutralisation requires
  an eligible unaware hostile in the required reach and position; `CON-282`:
  ladder, plank, spore route, Slums, Robert, Marlene, Ellie, dumpster and
  apartment transitions require their authored predecessors.
- Scarce resources: Health, treatment time, compatible blade and binding,
  shiv output, magazine/reserve ammunition, inert diversion objects, cover,
  unseen reach and checkpoint-local progress. Exact values are parameters.
  Claims: `TLO-005`–`TLO-014`.

### Information Genes

- Existing `INF-073`: active weapon/item, magazine and reserve state are
  visible; `INF-119`: Health and immediate personal state remain visible;
  `INF-128`: reachable pickups and inventory expose identity, quantity,
  compatibility and available capacity; `INF-132`: the crafting surface
  exposes the known shiv output and required components before commitment.
- Existing `INF-115`: current avatar-centred sight and documented spatial cues
  expose partial nearby actor state; `INF-300`: held ordinary Listen Mode
  distinguishes eligible nearby actor silhouettes through occlusion while the
  remainder stays unknown; `INF-125`: current route/objective cues expose the
  next known authored gate; `INF-268`: contextual tutorial text exposes the
  current movement, healing, crafting, stealth or combat instruction before
  advancing.
- Exact silhouette art, range, opacity, icons, prompts, bindings and UI
  positions are presentation parameters. Claims: `TLO-004`–`TLO-010`.

### Objective Genes

- Existing `OBJ-155`: survive and complete the ordered `The Quarantine Zone`
  survival-action chapter, accept its final apartment transition and retain
  reloadable ordinary control in immediate successor `The Outskirts: Outside`
  before the bookshelf/generator route.
- Robert's defeat, meeting Ellie or entering the final door without the stated
  successor save/load check is not success. Claims: `TLO-013`–`TLO-015`.

### Time Genes

- Existing `TIM-003`: movement, perception, diversion, companion behaviour,
  attacks, reload and treatment advance in real time.
- Existing `TIM-007`: a checkpoint or manual successor save can be restored so
  another stealth, craft, diversion or combat choice replaces the failed or
  previously observed continuation; this is not an in-world rewind command.
- Claims: `TLO-006`–`TLO-015`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A clean Moderate New Game has completed only the setup Prologue | Accept first ordinary control at `20 Years Later` | The Quarantine Zone begins without chapter-select, New Game Plus or imported inventory state | fixed clean entry | `TLO-003`, `TLO-004` |
| A required ladder or plank is reachable and its destination is open | Lift, carry and place it at the authored fixture | The object remains at the new support position and admits the next traversal | portable route geometry | `TLO-005` |
| The dark spore route hides ordinary local detail | Toggle the personal flashlight | A local light field becomes active without replacing movement authority | reversible illumination | `TLO-005` |
| One eligible nearby hostile is outside ordinary line of sight | Hold ordinary Listen Mode, inspect, then release | The overlay exposes a bounded current silhouette through occlusion and ordinary view returns without a retained mark | reversible local information | `TLO-006` |
| A compatible firearm and ammunition pickup is reachable | Collect, select, fire and reload once | Inventory, active slot, magazine and reserve update under typed compatibility and capacity | finite weapon state | `TLO-007` |
| Health is below its cap and one health kit is carried | Hold treatment until it completes | One item is consumed and missing Health is restored; interruption before completion withholds the result | interruptible recovery | `TLO-009` |
| The shiv recipe is known and compatible blade and binding are carried | Select the recipe and craft exactly one shiv | Ingredients leave inventory and one compatible shiv enters carried state | stationless finite preparation | `TLO-008` |
| One hostile is unaware and reachable from the required position | Grab and complete one close neutralisation | The target leaves active perception/combat without a normal exchange of fire | awareness-gated stealth | `TLO-010` |
| An eligible hostile watches the intended route and a brick or bottle is available | Throw the inert object toward another reachable point | The landing stimulus can replace the hostile's current attention/search path | positioned diversion | `TLO-010` |
| A hostile completes detection | Hide, neutralise or fight | Suspicion becomes active combat; chapter progress remains recoverable rather than automatically invalid | stealth-to-combat transition | `TLO-010`, `TLO-011` |
| Tess or another current authored ally enters an eligible local encounter | Continue direct protagonist movement or combat | The ally autonomously follows and performs its admitted attack, traversal or support behaviour without receiving individual tactical orders | companion causality without co-control | `TLO-012` |
| Health reaches zero before the chapter boundary | Continue or load the latest checkpoint | Failed position, Health, inventory spend, ammunition, hostiles, awareness and route state are replaced by the retained snapshot | reproducible negative recovery | `TLO-011` |
| Robert has been pursued and the Marlene/Ellie handoffs have occurred | Move the final dumpster and enter the apartment | Cargo closes and `The Outskirts: Outside` begins | explicit chapter transition | `TLO-013` |
| First ordinary `Outside` control is available before the bookshelf/generator | Create a manual save, quit and load it | The same ordinary successor control and unadvanced route return | reproducible positive terminal | `TLO-014`, `TLO-015` |

## Strategic and experiential structure

- Planning horizon: the current instruction and authored route expose the next
  gate, while Health, ammunition, ingredients, carried items, hostile position
  and companion state determine whether to pass, craft, treat, distract,
  neutralise or fight.
- Local tactics: hold Listen Mode from cover, release it before moving, route
  around current silhouettes, place a brick/bottle stimulus away from the
  desired path, approach an unaware hostile from the required side and keep
  treatment/reload time outside immediate attack pressure.
- Medium-term structure: traversal fixtures introduce movement, the dark route
  introduces partial perception, Slums turns pickups into crafting and stealth
  choices, Cargo layers companion-supported combat and fixed handoffs, and the
  final apartment becomes a named successor boundary rather than an arbitrary
  stop.
- Reversible versus irreversible: movement, crouch, flashlight and Listen Mode
  can be changed; ammunition, ingredients, diversion objects and treatment are
  spent; a takedown, alert and route fixture alter the attempt; checkpoint load
  replaces failure; manual successor retention persists.
- Failure attribution: current Health, weapon/ammunition, pickup compatibility,
  recipe components, treatment completion, local view, listening silhouettes,
  hostile awareness, instruction and checkpoint state separate missing
  resources, unsafe timing, failed stealth and lethal combat.
- Player trust: a valid craft consumes the disclosed components, Listen Mode
  disappears on release, hostile attention follows perceived stimuli, authored
  gates advance in order and the loaded successor save proves settlement.

## Replay and variation

- What changes: route timing, flashlight use, pickup quantities, ammunition,
  Health, treatment, craft timing, listened hostile positions, diversion point,
  takedown target, detection, combat and checkpoint use.
- Randomness or procedural generation: topology, major actors, fixtures,
  chapter order and transition are authored. Minor encounter timing can vary;
  no procedural-generation claim enters this packet.
- Multiple strategies: several human encounters admit avoidance, distraction,
  stealth neutralisation or open combat. The control demonstrates one craft,
  one Listen observation, one diversion and one close neutralisation without
  making no-alert, no-kill or exhaustive clearing the terminal.
- Typical replay motive: conserve ammunition and Health, shorten exposure and
  find a cleaner stealth path through the same authored chapter.

## Adjacent systems and history

- Metro Exodus shares direct survival combat, posture, pickups, healing,
  flashlight, inert diversion, unaware neutralisation, detection, checkpoints
  and retained successor control. Metro spends replaceable breathing time and
  manipulates light-to-perception pressure; The Last of Us instead exposes
  occluded actors through held listening, crafts a finite shiv and runs an
  autonomous authored companion beside the protagonist.
- Far Cry 3 shares firearm stealth, an inert thrown diversion, unaware close
  neutralisation and recoverable alert-to-combat escalation. Its camera creates
  persistent actor marks and its outpost becomes an allied service node; this
  packet uses a reversible short-range overlay and a linear chapter handoff.
- Tomb Raider (2013) shares authored traversal, firearm/stealth pressure and a
  held situational overlay. Survival Instinct highlights a broader local
  environment around a lone protagonist; this packet couples actor silhouettes
  to stationless finite crafting and companion-supported encounters.
- Resident Evil 4 (2023 remake) shares survival inventory, stationless crafting,
  treatment, direct combat and a retained next-chapter terminal. It centres
  case arrangement, knife durability/parry and stagger follow-ups; this packet
  centres listening, inert diversion and unaware grappling.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-200`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-406`, `ACT-409`, `ACT-423` | actor, route, object, weapon, item, recipe and fixture names are parameters |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-407`, `SYS-578`, `SYS-780` | attention, companion, damage, checkpoint and settlement values are parameters |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-286`, `CON-297`, `CON-335` | capacity, ingredients, compatibility, order, reach and timing are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-132`, `INF-268`, `INF-300` | silhouette art, prompts, bindings and UI layout are parameters |
| Objective | `OBJ-155` | chapter, successor and retained state are parameters |
| Time | `TIM-003`, `TIM-007` | perception, combat, treatment and load timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `260` (`GAME-0001`–`GAME-0260`).
- Exact genome matches: none.
- Tied near matches: `GAME-0260` — Metro Exodus (`29 / 48 = 0.604167`).
- Supported combination subsets: `COMB-0259`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0260` — Metro Exodus | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-406`, `ACT-409`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`, `SYS-780`, `CON-262`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `OBJ-155`, `TIM-003`, `TIM-007` | Both carry finite weapons, healing, stealth, diversion and authored gates through recoverable real-time combat into a retained successor. Metro consumes replaceable breathing-filter time and turns personal/world illumination into detection pressure. The Last of Us instead lifts route objects, crafts a shiv, channels treatment, invokes listening through occlusion and receives autonomous companion help. | Near, `0.604167` |

### Preserved research notes

- New genes: none.
- Reused genes: all 39 admitted genes in the Normalised genome.
- Classification result: `New combination of known genes`.
- Lower-ID scan: reuse `ACT-423` + `INF-300` for the held bounded Listen Mode
  overlay rather than creating a game-named listening gene; reuse `ACT-123` +
  `CON-297` + `INF-132` for the known stationless shiv recipe; reuse
  boundary-preserving `SYS-407` for autonomous authored companion follow and
  help. Reject a gas-mask/filter gene because the early mask is automatic and
  has no player-managed filter reserve; reject a co-op/role gene because only
  one human controls the protagonist; reject a quest-, room-, character-, item-
  or reward-named gene.

## Taxonomy impact

- Registry changes: add `COMB-0259` and independent evidence for 39 reused
  genes. Generalise only the wording of `SYS-407` from a product-specific
  Palico/hunter label to the same portable autonomous-companion boundary; its
  definition semantics, lifecycle and all earlier signatures remain unchanged.
- Taxonomy-change record: none; no split, merge, deprecation, lifecycle change
  or signature change.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, actor,
  chapter, location, item, recipe, fixture, app, package, build and patch names
  remain parameters.

## Negative results

- No video or audio evidence was used; only official static text/data and
  static written routes support this packet.
- `Prologue`, `Left Behind`, Deluxe unlocks, optional assists, later chapters,
  wider crafting/upgrades and the whole campaign are excluded even though the
  current product exposes them elsewhere.
- The automatic gas-mask animation, fixed dialogue, cutscenes and scripted
  boost positions are authored gates, not new resource, dialogue or
  companion-command genes.
- Ordinary Listen Mode reuses a held situational overlay and bounded occluded-
  actor disclosure; enhanced navigation/combat listening assists are excluded.
- Meeting Ellie or entering `Outside` without the manual save/load retention
  test is not the terminal.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `TLO-001`–`TLO-015`:
  one early chapter combines held listening, finite crafting, recoverable
  stealth/combat and autonomous companion help before retained successor
  control.

## New genes

- None. Every admitted boundary is already Active and transferable.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0259` — listening-mediated
  crafted stealth with autonomous companion support into a retained chapter.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] `SYS-407` receives a
  boundary-preserving portable label/wording generalisation; no prior signature
  or lifecycle changes.

## New questions

- Does the completed 253-to-261 horizon preserve strict product, chapter,
  terminal, language, artwork and comparison parity across all nine units?

## Next recommended game

- [Hypothesis | Limited | High] no new game; run
  `SEARCH_DEMAND_BATCH_014_AUDIT` independently across `GAME-0253`–`GAME-0261`.
- Optimisation criterion: verify the entire selected horizon rather than
  extending it.
- Expected information gain: detect cross-unit scope, evidence, signature,
  localisation, artwork, index, artifact or comparison drift.
- Backlog impact: closes the approved batch-014 Goal if all gates pass.

## Why this game

- [Hypothesis | Limited | High] The final audit can now compare nine complete
  mechanically bounded action/survival packets against one shared 261-game
  corpus baseline.
