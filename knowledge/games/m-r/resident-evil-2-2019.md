---
game_id: GAME-0280
slug: resident-evil-2-2019
game_title: Resident Evil 2 (2019 remake)
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-183
    - ACT-199
    - ACT-341
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-776
  constraint:
    - CON-210
    - CON-282
    - CON-285
    - CON-296
    - CON-579
    - CON-621
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-303
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Resident Evil 2 (2019 remake)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `883710`, Standard Edition package `280800`, default public branch Build ID
  `11636119`, built 2023-07-06 and published 2023-08-14; checked 2026-09-08.
  The build identifier and dates are secondary distribution observations.
  Capcom's 2023-08-14 update notice for that branch movement names no semantic
  version, so none is asserted. The retired `dx11_non-rt` beta branch (Build
  `11055033`, technical support ended 2023-07-12) is excluded.
- Product boundary: this is the 2019 remake published by Capcom as
  `RESIDENT EVIL 2 / BIOHAZARD RE:2`, not the 1998 original, not the separate
  2026 Steam listing `Resident Evil 2 (1998)` (application `4249110`), not the
  Deluxe Edition package `281610`, the Raccoon City Edition `597332`, the
  Resident Evil Remake Trilogy `1142889`, any of the thirteen listed DLC
  applications, a console or macOS release, or a franchise union.
- Platform, input, scenario and mode: Windows, English interface, keyboard and
  mouse or the default `Type A` controller layout, Story → New Game → Scenario
  Select `Leon S. Kennedy` → game mode `Standard`, on fresh save data with no
  cleared-scenario records, unlocked bonuses, costumes or Online Store items.
  `Assisted`, `Hardcore`, the game-over offer to switch to `Assisted`, Claire's
  scenario, both `2nd run` scenarios and every bonus mode are separate packets.
- Entry: first ordinary Leon control on the Mizoil gas-station forecourt after
  the opening and arrival cutscenes, before entering the store, with the
  starting `Matilda` handgun and its starting ammunition recorded as the
  incoming state.
- Primary decision loop: read the current objective, the loaded and reserve
  ammunition, the interact icon and the inventory health condition; walk, run
  or quick-turn through the store, its back corridor, the streets and the
  station approach; ready, aim, wait for reticle focus or fire immediately at a
  zombie's head or legs, reload, or evade it; collect the Gas Station Key and
  apply it to the locked door; follow the single open street route while
  zombies pursue until arrival settles the station objective; collect the Main
  Hall First Aid Spray and Handgun Ammo; if a grab has lowered the condition
  below Fine, decide whether to spend the spray before the save or carry it;
  then commit the first manual typewriter save while no hostile is nearby and
  verify after reload that the settled arrival persists.
- Positive terminal: arrival at the Raccoon Police Station settles the
  authored `Make it to the police station` objective and hands ordinary
  control to the Main Hall. That settlement is verified as persistent, before
  the east shutter lever is pulled, by interacting with the reception-desk
  typewriter, saving into a fresh manual slot, quitting to the main menu,
  loading that slot and confirming Leon, `Standard`, the Main Hall area label
  and the successor objective. The save is the retention check of the settled
  arrival, not an authored chapter boundary; no action after the reload is
  admitted.
- Negative terminal: health reaching zero is game over. Select `Continue`, so
  the most recent save data replaces transient position, health, ammunition,
  inventory, hostile and objective state; this is recovery, not completion.
  Reaching the Main Hall or the typewriter without the reload check is not
  success.
- Included: direct third-person traversal, running and quick turn; ready, aim,
  focused shot and fire with a magazine-fed handgun; reload from finite
  reserve; body-region-dependent shot results on zombies; zombie perception,
  pursuit, grab and bite damage; the graded health condition and game over;
  prompted pickup of ammunition, a restorative and a key item into finite
  slots; the damaged-branch decision to spend or carry one immediate
  restorative; a key-locked door; the ordered gas-station, street and station
  objective chain, its settlement on arrival and its explored map and
  objective display; the first fixture-bound manual save, its hostile-proximity
  legality, autosave checkpoints, `Continue` and multi-slot reload.
- Excluded: everything after the first Main Hall save, including the east
  shutter, Elliot, the Officer's Notebook, Marvin, the Combat Knife and every
  sub-weapon counterattack, wooden boards, the item box, item combining and
  gunpowder recipes, examining items, weapon parts, medallions, the rest of the
  station and campaign; the optional CCTV computer scene; poison, herb effects
  and the reduced-damage icon; `Assisted`, `Hardcore` and its ink ribbons;
  Claire, `2nd run`, The 4th Survivor, The Tofu Survivor, The Ghost Survivors,
  Records, bonus weapons, costumes, the NOIR filter, DLC, soundtrack swap;
  ranks, clear time, achievements as goals, speedrun routing, mods, trainers,
  console and macOS versions, the 1998 game and its 2026 relisting;
  screenshots, official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install application `883710` from package
  `280800` on the default branch; start Story → New Game → Leon → Standard
  on fresh save data with `Type A` controls. From forecourt control, enter the
  store, follow the only open door into the back corridor, ready and aim at the
  first zombie until the reticle closes, fire at least once, reload once, and
  either finish it or pass it while it is down; take the Gas Station Key from
  the wall, apply it to the locked storeroom door, leave through the shelves;
  after the forecourt and crash cutscenes, run the single open street route to
  the station without clearing every zombie; in the Main Hall collect the
  First Aid Spray and Handgun Ammo, save at the typewriter into a fresh slot,
  quit and reload. Exact shots, hits taken, ammunition counts, health condition
  at the save, which zombies were downed, slot number and elapsed time are run
  parameters; no hit, detour or resource spend is instructed. Live combat
  leaves the ordinary route in one of two outcome branches at the Main Hall:
  undamaged, where the condition reads Fine, the spray stays carried and the
  restorative row is not exercised; or damaged, where a grab has lowered the
  condition to Caution or Danger and the player decides whether to spend the
  spray before the save or carry it into the retained state. Both branches
  are ordinary; neither is chosen deliberately. Observing the full-health
  refusal or the spray's effect is an evidence-verification branch outside the
  ordinary route and is documented from the manual, not instructed.
- Potential scoped modules: the east wing through Marvin and the knife; one
  medallion-gated station packet; one `Hardcore` ink-ribbon packet; Claire's
  scenario; one `2nd run`; The 4th Survivor; The Ghost Survivors; the 1998
  game or its 2026 relisting each requires a separate scope.
- Direct-play status: not conducted. Valve application, package and
  achievement data plus Capcom's product catalogue, support index and official
  web manual establish lawful availability, product separation, scenarios,
  modes, controls, shooting, reticle focus, reload, interaction, inventory,
  health, map, objectives and saving. Capcom's Steam update notices establish
  the current branch state. Three independent static written routes establish
  the gas-station, street and Main Hall order and contents. This is an
  evidence-backed rules reconstruction, not a claimed captured playthrough or
  entitlement. No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RE2R-001` | The admitted product is the 2019 Windows Steam remake, application `883710`, Standard Edition package `280800`, separate from the Deluxe, Raccoon City and Trilogy packages, thirteen DLC applications and the 2026 `Resident Evil 2 (1998)` listing `4249110` | Confirmed | Direct | High | P1, P2, P6, P7 |
| `RE2R-002` | Default public branch Build `11636119` is the current observed Windows distribution state; Capcom's 2023-08-14 notice describes that update without a semantic version, and the `dx11_non-rt` branch is retired | Observation | Corroborated | High | P5, S1 |
| `RE2R-003` | A new game chooses Leon or Claire and one of `Assisted`, `Standard` or `Hardcore`; `Standard` has no assists and no ink-ribbon or autosave restriction | Confirmed | Direct | High | P3 |
| `RE2R-004` | Movement, running (toggle or hold), quick turn, camera reset, aim, attack, reload and interact are the documented `Type A` controls | Confirmed | Direct | High | P3 |
| `RE2R-005` | A weapon must be readied before it can fire; the reticle shrinks the longer the player aims, a fully closed reticle makes shots more precise and more powerful, and moving or firing resets it | Confirmed | Direct | High | P3 |
| `RE2R-006` | Reload transfers reserve ammunition into the weapon, and the screen exposes loaded and remaining ammunition while the weapon is readied | Confirmed | Direct | High | P3 |
| `RE2R-007` | An interact icon appears near usable objects, some interactions require a held input, and a key item is applied to its door through the inventory `Use` command or the door prompt | Confirmed | Direct | High | P3 |
| `RE2R-008` | Damage moves the condition from Fine to Caution to Danger, zero health is game over, and a recovery item cannot be used at full health | Confirmed | Direct | High | P3 |
| `RE2R-009` | Picked-up items occupy inventory slots, typed ammunition stacks share a slot, and used key items may be discarded | Confirmed | Direct | High | P3, S4 |
| `RE2R-010` | Autosave writes one auto slot at checkpoints; a typewriter writes one of twenty manual slots shared across modes; `Continue` loads the most recent data; the typewriter cannot be used when enemies are nearby | Confirmed | Direct | High | P3 |
| `RE2R-011` | The map shows only visited places until an area map is acquired, and the current main objective and sub-objectives are inspectable from the map and inventory screens | Confirmed | Direct | High | P3 |
| `RE2R-012` | Leg damage slows a zombie, a headshot can stun it, a grab bites without a sub-weapon counter, and a downed zombie may not be finished | Observation | Corroborated | Medium | P3, S2, S3, S4 |
| `RE2R-013` | Zombies that perceive Leon pursue him, including from room to room, rather than holding fixed positions | Observation | Corroborated | Medium | S2, S3, S4 |
| `RE2R-014` | The Leon opening runs store → back corridor and first zombie → Gas Station Key → key-locked door → exit cutscene → crash → single open street route → station | Observation | Corroborated | High | S2, S3, S4 |
| `RE2R-015` | The Main Hall entry state contains the typewriter and item box at the reception desk, a First Aid Spray and Handgun Ammo, and no hostile; the east shutter lever begins the excluded successor | Observation | Corroborated | High | S2, S3, S4 |
| `RE2R-016` | Arriving at the station settles the `Make it to the police station` objective and its `Welcome to the City of the Dead` achievement before Main Hall control | Observation | Corroborated | High | P7, S3 |
| `RE2R-017` | The Combat Knife and every sub-weapon counter, item combining, wooden boards and the notebook belong to the successor route after the first save | Observation | Corroborated | High | P3, S2, S3, S4 |
| `RE2R-018` | The bounded identity is finite-ammunition zombie evasion under a graded health condition, carried through a key-gated escape and street chase to a settled station arrival retained by a fixture-bound, hostile-free first manual save | Strong Pattern | Corroborated | High | `RE2R-003`–`RE2R-017`, `RE2R-019`, `RE2R-020` |
| `RE2R-019` | The scenario has no chapter or mission structure: the manual's page set names scenarios, modes, saves, controls, screens, inventory, map, files and objectives but no chapter, the objective list advances in place at arrival with no completion screen or documented autosave, and the Main Hall typewriter save is voluntary | Observation | Corroborated | High | P3, S2, S3, S4 |
| `RE2R-020` | A zombie hit is an avoidable live-combat outcome rather than a required interaction, and the Main Hall First Aid Spray lies on the ordinary route whatever the condition, so the restorative decision arises only in the damaged outcome branch | Observation | Corroborated | High | P3, S2, S3, S4 |

## Basic data

- Release / origin: Capcom; released for Windows Steam on 2019-01-24 as a
  ground-up remake of the 1998 game on the RE Engine.
- Platform or physical form: lawfully available English Windows Steam client,
  Standard Edition package `280800`; one offline single-player Leon opening.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-08:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=883710&cc=ua&l=english),
    for title, application, Windows-only support, single-player and Steam
    Cloud categories, developer/publisher, 2019-01-24 release, four purchase
    packages and thirteen DLC applications.
  - `P2` — [Valve Standard Edition package data](https://store.steampowered.com/api/packagedetails?packageids=280800&cc=ua&l=english),
    for package `280800` containing only application `883710`; the Deluxe
    (`281610`), Raccoon City (`597332`) and Trilogy (`1142889`) packages were
    queried separately for their extra applications.
  - `P3` — [official Capcom Resident Evil 2 web manual, Steam English edition](https://game.capcom.com/manual/re2/),
    reached through its age gate to `/manual/re2/en/steam` and read on every
    page: Main Menu (`page/1/1`), Scenario Select (`1/2`), Game Modes (`1/3`),
    Saving/Loading (`1/4`), Controls (`2/1`), Actions (`2/2`), Game Screen
    (`3/1`), Damage Indicator (`3/2`), Inventory (`4/1`), Examining Items
    (`4/2`), Combining Items (`4/3`), The Item Box (`4/4`), The Map (`5/1`),
    Files (`5/2`), Objectives (`5/3`), Bonuses (`6/1`–`6/4`), Loading Tips
    (`7/1`) and Tutorials (`7/2`). The manual is copyright 2022 and precedes
    the current build; no later official rule change is documented.
  - `P4` — [Capcom support "Resident Evil 2 Online Manual" article](https://www.capcom-support.com/hc/en-us/articles/5827719138588-Resident-Evil-2-Online-Manual),
    updated 2026-07-26, which points to the manual above; the Resident Evil 2
    Steam support section holds only a general troubleshooting guide and no
    patch history.
  - `P5` — [Capcom's Steam update notices for the application](https://store.steampowered.com/news/app/883710),
    read through Valve's partner-event feed: the 2022-06-10 system-requirement
    change, the 2022-06-16 `dx11_non-rt` branch, the 2022-10-06 update, the
    2023-04-12 end-of-support notice and the 2023-08-14 update notice.
  - `P6` — [Capcom product catalogue entry for Resident Evil 2](https://www.capcom-games.com/product/en-us/residentevil-2/),
    which links Steam application `4249110`; [Valve application data for `4249110`](https://store.steampowered.com/api/appdetails?appids=4249110&cc=ua&l=english)
    identifies it as `Resident Evil 2 (1998)`, released 2026-04-01, a distinct
    product.
  - `P7` — [Steam achievement list for the application](https://steamcommunity.com/stats/883710/achievements/),
    for the publisher-authored `Welcome to the City of the Dead` achievement
    and the later `Eat This!`, `The Basics of Survival` and `That'll Hold 'Em`
    achievements that mark excluded successor mechanics.
- Corroborating textual sources, accessed 2026-09-08:
  - `S1` — [public SteamCMD info projection](https://api.steamcmd.net/v1/info/883710),
    for public Build `11636119` (built 2023-07-06, updated 2023-08-14) and the
    `dx11_non-rt` branch Build `11055033`; a secondary distribution mirror.
  - `S2` — [PowerPyx full walkthrough](https://www.powerpyx.com/resident-evil-2-remake-full-walkthrough/),
    for the gas-station, street and Main Hall order, the first zombie's
    kill-or-stun choice, the key, the single street path and the typewriter
    and item box at station entry. Its embedded video was not opened.
  - `S3` — [Gamer Guides Leon A prologue](https://www.gamerguides.com/resident-evil-2-2019/guide/walkthrough/leon-a/prologue)
    and [police station](https://www.gamerguides.com/resident-evil-2-2019/guide/walkthrough/leon-a/police-station)
    pages, for the key location, the locked door, the leg-shot and head-shot
    options, the street route, the Main Hall spray and ammunition, the
    `Make it to the police station` objective and the knife handed over only
    after the east wing. Images were not opened.
  - `S4` — [Resident Evil Wiki](https://residentevil.fandom.com/wiki/Resident_Evil_2/gameplay)
    gameplay, [Mizoil Gas Station](https://residentevil.fandom.com/wiki/Mizoil_Gas_Station)
    and [Main Hall](https://residentevil.fandom.com/wiki/Main_Hall) pages,
    read as MediaWiki wikitext, for slot inventory, defensive weapons,
    zombies rising after knockdown, room-to-room pursuit and the Main Hall
    entry contents; community text, never sole support.
- Negative searches, 2026-09-08: the Steam store page exposes no `View
  manual` link; Capcom's support index has no version-history article for
  the product; `residentevil.com` has no product page for this game; Valve's
  `ISteamNews` endpoint returned `404` for the application; IGN's Resident
  Evil 2 wiki covers only the 1998 game; Neoseeker, GameFAQs,
  TrueAchievements and Fandom HTML were bot-blocked, so Fandom was read
  through its API; Evil Resource lists no gas-station key in its item index.
- Reproducible control: `V1` repository-side transition trace across
  `P1`–`P7` and `S1`–`S4` under the declared application, package, build,
  scenario, mode, entry, exclusions and reload terminal; rules reasoning, not
  direct play.
- Claim IDs: `RE2R-001`–`RE2R-020`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk, run and quick-turn Leon through the store, corridor,
  streets and station approach; `ACT-161`: ready the handgun, aim and fire at
  a reachable zombie; `ACT-183`: reload the magazine-fed handgun from reserve;
  `ACT-199`: pick up the Gas Station Key, First Aid Spray and Handgun Ammo
  into inventory slots through the interact prompt; `ACT-131`: in the damaged
  outcome branch, use the one carried First Aid Spray from the paused
  inventory for immediate recovery, or carry it into the retained state;
  `ACT-341`: open the
  store and station doors, apply the key to the locked door, and commit the
  typewriter save.
- Rejected `ACT-164`: only one weapon and no sub-weapon exist before the
  terminal, so no shortcut-slot switch is ever required; an initial `Equip`
  from the inventory, if needed, is the equip branch of `ACT-199`. Rejected
  `ACT-200`: the spray applies immediately from the paused inventory, not as
  an interruptible live cast. Rejected `ACT-202`: the game has no crouch or
  lean. Rejected `ACT-235`, `ACT-425` and `ACT-419`: no stealth
  neutralisation, timed parry or prompted stagger-window close action exists
  in this packet; the
  knife counter is a grab escape that arrives only after Marvin.
- Weapon, item, key, door, room and control-type names are parameters.
  Claims: `RE2R-004`–`RE2R-010`, `RE2R-014`, `RE2R-015`, `RE2R-020`.

### System Behaviour Genes

- Existing `SYS-057`: a zombie that perceives Leon leaves its idle position
  and pursues him, including between rooms, applying its grab and bite on
  contact; `SYS-208`: a shot resolves through aim and struck region, so leg
  hits slow and head hits can stun; `SYS-215`: movement, pursuit, grabs, bites
  and defeat resolve in live time; `SYS-578`: the rule governs one graded health
  condition in every run, but its events are conditional: a bite lowers the
  condition only when an evasion fails, the spray restores the same pool only
  in the damaged branch, and zero health is the documented failure boundary
  that a successful route never reaches; `SYS-369`: `Continue` after game
  over replaces the failed transient state with the most recent save;
  generalised `SYS-776` (`TAXONOMY_CHANGE_040`): sustained aim closes the
  reticle so the accepted shot is more precise and stronger, and moving or
  firing resets it.
- Rejected `SYS-780`, tested clause by clause: arrival is a location trigger,
  not the final required interaction of a bounded authored chapter or mission
  (`RE2R-019`); the objective list advances in place, but no segment
  completion is exposed and no save state is created or accepted at arrival,
  because the typewriter save is a separately chosen action; and the Main Hall
  is a continuation of the same scenario, not a named successor segment. The
  objective's closure is the resolution of `OBJ-026`, disclosed by `INF-125`,
  and the save is `ACT-341` under `CON-621` retained through `TIM-007`.
  Rejected `SYS-373`: zombies have no documented suspicion, search or alert
  escalation; perception leads directly to pursuit. Rejected `SYS-339`: no
  emitted-sound propagation, crowd joining or retained target memory is
  established for this route. Rejected `SYS-749`: the zombies around the
  forecourt and streets are not evidenced as a finite group instantiated by a
  settled trigger rather than authored occupants. Rejected `SYS-755`,
  `SYS-777`, `SYS-778` and `SYS-779`: no breakable supply object, parry,
  stagger follow-up or survival-threshold encounter occurs before the save.
- A downed zombie rising again and the hidden viability of a fallen zombie
  are recorded as parameters of `SYS-215` and `INF-115` rather than a new
  gene; the only primary support is a loading tip, so the boundary is filed
  as a candidate for a later station packet.
- Resolution order: accept movement, aim, fire, reload, interaction, pickup,
  use or save input; validate readiness, ammunition, slot, key, health and
  hostile-proximity predicates; resolve perception and pursuit; resolve shots
  by region; apply bites to the health condition; replace death from the most
  recent save; close the arrival objective as the spatial terminal; write the
  manual slot. Claims: `RE2R-005`–`RE2R-016`, `RE2R-019`.

### Constraint Genes

- Existing `CON-210`: a pickup needs a free slot or a compatible typed
  ammunition stack; `CON-282`: the store, back corridor, key, exit, crash,
  street and station transitions require their authored predecessors;
  `CON-285`: firing requires a readied weapon with loaded rounds and reload
  requires reserve; `CON-296`: the storeroom door opens only with the Gas
  Station Key; `CON-579`: in the damaged branch the spray is usable only
  below full health from finite stock, which is why the undamaged branch
  never exercises it.
- New `CON-621`: a manual save is legal only at a ready designated fixture
  while no hostile is nearby; the fixture pauses the world, imposes no
  cooldown and, on `Standard`, no consumable.
- Rejected `CON-602`: its boundary requires a live exposed interaction
  interval and a fixture cooldown, both absent here. Rejected `CON-262`,
  `CON-331` and `CON-578`: there are no weapon-class slots and the handgun
  runs a magazine-and-reload cycle. Rejected `CON-305`: pursuit legality by
  route and barricade is not exercised. Rejected `CON-394`: items occupy
  fixed slots without footprint or rotation.
- Scarce strategic resources: handgun ammunition, one spray, health condition,
  free slots, distance from zombies and the retained save. Slot count,
  stack caps, damage values and stun thresholds are parameters. Claims:
  `RE2R-005`–`RE2R-010`, `RE2R-014`, `RE2R-020`.

### Information Genes

- Existing `INF-073`: shortcut slots plus loaded and remaining ammunition are
  visible while the weapon is readied; `INF-075`: the Fine, Caution and
  Danger condition is displayed in every run, whatever its value, and the
  damage effect appears only after a bite; together they expose whether
  recovery is needed; `INF-115`: local
  sight and sound expose only nearby zombies and their approach; `INF-125`:
  the map shows visited places and the current objective with its
  sub-objectives; `INF-128`: the interact icon, item name and inventory slots
  expose what a pickup is and where it can go; generalised `INF-303`
  (`TAXONOMY_CHANGE_040`): the reticle visibly closes toward its focused
  state before a shot whose precision and power depend on it.
- Rejected `INF-119`: no build, experience or ability readiness exists.
  Rejected `INF-298`: no incoming-detection escalation is displayed.
  Rejected `INF-132`, `INF-302` and `INF-295`: no recipe, grid or contextual
  stagger-window prompt occurs before the save. Map item and door colours are
  parameters of `INF-125` that only matter after the terminal.
- Claims: `RE2R-005`–`RE2R-012`, `RE2R-015`.

### Objective Genes

- Existing `OBJ-026`: make the station route traversable by carrying the Gas
  Station Key through the locked storeroom door, then navigate Leon along the
  single open street route until arrival settles the authored `Make it to the
  police station` objective; persistence after arrival, a parameter of the
  boundary, is verified by the fresh-slot save and reload in the Main Hall.
  The same boundary already carries DOOM (2016), Half-Life (1998), Prey
  (2017), BioShock Remastered and Tomb Raider (2013) openings that end at a
  reached, retained successor location.
- Rejected `OBJ-155`, tested clause by clause: the packet is not a bounded
  authored chapter or mission but an objective inside one continuous
  scenario; there is no explicit completion display or authored save boundary
  at arrival, only an in-place objective change and an achievement; the
  typewriter save is chosen separately and is not the boundary's save; and
  the Main Hall is the same scenario continuing, not an immediate named
  successor segment (`RE2R-019`). The Resident Evil 4 resemblance is not
  evidence. Rejected `OBJ-029`: no finite hostile set must be defeated.
- Success, evaluation and failure: success is the settled arrival verified by
  reload; game over and `Continue` are recovery; reaching the typewriter
  without the reload check is intermediate. Claims: `RE2R-010`,
  `RE2R-014`–`RE2R-016`, `RE2R-019`.

### Time Genes

- Existing `TIM-003`: zombie approach, grabs, reticle focus, reload and
  damage advance in live time while the player retains input; paused
  inventory, map and save menus add no second clock.
- Existing `TIM-007`: manual slots and the auto slot retain prior states that
  can be loaded so a different route, shot or resource choice replaces the
  observed continuation; the retention check exercises exactly that restore.
- Claims: `RE2R-005`, `RE2R-010`, `RE2R-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh save data at the main menu | Story → New Game → Leon → Standard | Control begins on the forecourt with the handgun and starting ammunition and no unlocked bonus | reproducible entry and mode boundary | `RE2R-001`, `RE2R-003` |
| Leon stands in the store with the weapon readied and a zombie approaching | Hold aim without moving until the reticle closes, then fire | The accepted shot is more precise and stronger; moving or firing before that resets the reticle | delay-for-shot-quality trade-off | `RE2R-005`, `RE2R-006` |
| The magazine is partly spent and reserve remains | Reload | Fire readiness pauses while reserve transfers into the weapon | ammunition is operational time state | `RE2R-006` |
| Conditional: ordinary evasion or shooting has failed and a pursuing zombie has reached Leon while no sub-weapon is carried | No defensive input exists; the player may only keep moving or firing | The grab resolves autonomously into a bite that lowers the condition from Fine toward Caution and Danger; this row is the cost of a failed evasion, not a step of the route | undefended contact cost, reached only when evasion fails | `RE2R-008`, `RE2R-012`, `RE2R-020` |
| A zombie is downed by shots | Pass it or keep firing | A downed zombie may rise again; only continued damage or evasion resolves it | kill-or-evade ammunition decision | `RE2R-012`, `RE2R-013` |
| The Gas Station Key hangs on the wall and a slot is free | Interact | The key enters an inventory slot | prompted pickup into finite slots | `RE2R-007`, `RE2R-009` |
| The storeroom door is locked and the key is carried | Interact or select the key and `Use` | The door opens; without the key it stays locked | authority-gated fixture | `RE2R-007`, `RE2R-014` |
| The crash cutscene ends and zombies occupy the street | Run the single open path | Pursuing zombies follow; reaching the station settles the `Make it to the police station` objective in place and Main Hall control begins | perception-driven pursuit into a settled spatial objective | `RE2R-013`, `RE2R-014`, `RE2R-016`, `RE2R-019` |
| Damaged branch only: a grab has left the condition below Fine and the Main Hall spray is carried | Select the spray and `Use`, or carry it | One spray is consumed and the condition improves, or the lower condition and the spray both enter the retained state; the manual documents refusal at full health, which the undamaged branch never tests | bounded recovery decision inside one ordinary outcome branch | `RE2R-008`, `RE2R-020` |
| Failure boundary: repeated bites have taken the condition to zero before the save | Select `Continue` | The most recent auto or manual data replaces transient state; a successful run never executes this row | documented negative terminal and its recovery | `RE2R-008`, `RE2R-010` |
| The Main Hall typewriter is reachable and no hostile is nearby | Interact and choose a fresh slot | Manual data is written; near an enemy the typewriter refuses | fixture-bound, hostile-free saving | `RE2R-010`, `RE2R-015` |
| A manual slot exists | Quit to menu and `Load Game` on that slot | Leon, `Standard`, the Main Hall label and the successor objective return | persistence of the settled arrival | `RE2R-010`, `RE2R-016` |

## Strategic and experiential structure

- Planning horizon: keep enough handgun ammunition and health to pass the
  first zombie and the street group, and decide whether the Main Hall spray is
  spent before the save or carried into the station.
- Local tactics: wait for the closed reticle or fire at once; shoot legs to
  slow, head to stun, or evade entirely; keep distance because a grab has no
  counter; reload behind cover of distance; do not stop near a zombie when
  the save is the goal; in the damaged branch, weigh a full-health save
  against keeping the spray for the station.
- Medium-term structure: the store teaches aim, focus and the key gate; the
  street teaches pursuit and evasion under a single route; arrival settles
  the objective and the Main Hall save retains it.
- Reversible versus irreversible: movement and aim are revisable; spent
  ammunition, the spray and bites persist within a life; `Continue` and any
  manual slot replace a failed or observed continuation.
- Failure attribution: the reticle, loaded and remaining counts, the
  condition label, the interact icon and the refused typewriter separate
  timing, ammunition, health, route and save-legality failures.
- Player trust: the closed reticle must precede its effect, the locked door
  must refuse without the key, the typewriter must refuse near an enemy and
  the reloaded slot must restore the same Main Hall state. Claims:
  `RE2R-005`–`RE2R-020`.

## Replay and variation

- What changes between attempts: shots fired, focus waits, hits taken,
  whether the first zombie is finished or passed, which street zombies
  pursue, ammunition and condition at the save, and slot choice.
- Randomness or procedural generation: the store, key, door, street route,
  Main Hall contents and objective chain are authored; zombie timing and
  contact vary within that route.
- Multiple viable strategies: kill, stun-and-pass or pure evasion all reach
  the same settled arrival; the control fixes one focused shot and one
  reload, while the spray decision exists only in the damaged branch.
- Typical replay motive: conserve ammunition and health for the station
  or improve clear time; ranks and later routing remain outside this packet.
- Claims: `RE2R-005`, `RE2R-012`–`RE2R-015`, `RE2R-020`.

## Adjacent systems and history

- Direct product corridor: Capcom presents this as a ground-up remake of the
  1998 game and, in 2026, relisted that original separately; the 2023 remake
  of Resident Evil 4 is the reviewed same-series comparator. Both remakes
  share readied aim with a closing reticle, magazine reload, restorative
  legality, authored gates and checkpoint continuation; the Resident Evil 4
  packet ends at an authored chapter boundary with its own completion and
  save handoff, which this opening lacks, and adds an item grid, knife parry,
  stagger follow-ups, crafting and a pressure encounter that it never reaches.
- Similar lower-ID games: Prey (2017) shares direct traversal, aimed fire,
  reload, pickups into typed slots, authority-gated fixtures, live combat,
  one health pool, checkpoint recovery, branchable saves and a reached,
  retained successor location, but hides hostiles as copied props and spends
  foam; Dead Space (2023 remake) shares finite ammunition, restorative
  legality, pickups and live combat but cuts limbs with an oriented tool,
  spends Stasis and ends at an authored chapter; Metro Exodus shares
  perception-driven pursuit and the same survival substrate but spends filter
  time and manipulates light; Alien: Isolation shares fixture-bound saving and
  hunter pursuit but exposes saving to live time and excludes weapons.
- Important differences: this packet's entire pressure is a handgun with a
  closing reticle, undefended grabs, a graded condition, a single key gate and
  a save whose legality depends on hostile absence. Claims: `RE2R-005`–
  `RE2R-020`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-183`, `ACT-199`, `ACT-341` | weapon, key, door, item, room and control-type names |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-776` | focus time, damage, stun, knockdown, pursuit and save values |
| Constraint | `CON-210`, `CON-282`, `CON-285`, `CON-296`, `CON-579`, `CON-621` | slot count, stack cap, magazine, key identity, proximity radius |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-303` | icons, condition labels, map colours and reticle art |
| Objective | `OBJ-026` | objective text, arrival trigger, save slot and persistence check |
| Time | `TIM-003`, `TIM-007` | continuous simulation; twenty manual slots and one auto slot |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `279` (`GAME-0001`–`GAME-0279`).
- Exact genome matches: none.
- Tied near matches: `GAME-0258` — Prey (2017) (`19 / 34 = 0.558824`).
- Supported combination subsets: none.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0258` — Prey (2017) | `ACT-008`, `ACT-161`, `ACT-183`, `ACT-199`, `ACT-341`, `SYS-215`, `SYS-369`, `SYS-578`, `CON-210`, `CON-282`, `CON-285`, `CON-296`, `INF-073`, `INF-115`, `INF-125`, `INF-128`, `OBJ-026`, `TIM-003`, `TIM-007` | Both openings move direct traversal, aimed fire, reload, slot-bounded pickups, an authority-gated fixture, live combat on one health pool, checkpoint recovery and branchable saves toward one reached location whose successor objective is retained and reload-verified. Prey adds weapon selection, weapon-class ammunition slots, hostiles disguised as copied props, finite foam control and a readiness display. Resident Evil 2 instead closes a reticle over sustained aim and discloses it, resolves shots by body region, lets perceived zombies pursue and grab without a counter, grades the condition display, admits a damaged-branch restorative decision and makes the retaining save legal only at a hostile-free fixture. | Near, `0.558824` |

### Preserved research notes

- New genes: `CON-621`.
- Reused genes: `ACT-008`, `ACT-131`, `ACT-161`, `ACT-183`, `ACT-199`,
  `ACT-341`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-776`,
  `CON-210`, `CON-282`, `CON-285`, `CON-296`, `CON-579`, `INF-073`, `INF-075`,
  `INF-115`, `INF-125`, `INF-128`, `INF-303`, `OBJ-026`, `TIM-003` and
  `TIM-007`.
- Classification result: `New gene`.
- Evidence and reasoning: twenty-six boundaries transfer from the reviewed
  corpus, two of them after a wording generalisation that removes the
  Resident Evil 4 stagger-only reading of reticle focus, and the terminal
  reuses the spatial-arrival objective carried by several first-person and
  third-person action openings rather than the chapter-boundary pair. The
  only boundary the corpus lacked is a paused, hostile-proximity-gated fixture
  save with no exposure interval or cooldown.

## Taxonomy impact

- Registry changes: one new Active constraint `CON-621`; `SYS-776` and
  `INF-303` generalised by
  [`TAXONOMY_CHANGE_040`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_040.md)
  so focused aim may improve precision and power as well as stagger or
  critical relations; twenty-four further Active genes gain this game as an
  additional carrier. No lifecycle, ID or earlier reviewed signature changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_040`.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Leon, Claire,
  Mizoil, Raccoon City, Raccoon Police Station, Main Hall, Matilda, First Aid
  Spray, Gas Station Key, typewriter, `Standard`, `Type A` and every
  application, package, build and achievement identifier remain parameters
  or literal product terms.

## Negative results

- No direct-play, entitlement, screenshot, video or audio claim.
- No knife, counterattack, combining, examining, board, item-box, medallion,
  later-station, rank, mode, DLC, platform or 1998-game mechanic is imported.
- `SYS-780`, `OBJ-155`, `SYS-373`, `SYS-339`, `SYS-749`, `CON-602`,
  `CON-262`, `CON-331`, `CON-578`, `CON-305`, `CON-394`, `ACT-164`, `ACT-200`
  and `OBJ-029` are rejected with the smallest counterexamples recorded above;
  the first two were carried by the first calibration pass and removed after
  a clause-by-clause test showed no authored chapter or mission boundary.
- No hit, detour or resource spend is instructed to make a gene legal; the
  restorative genes are admitted only through the damaged outcome branch that
  live combat itself produces.
- A separate downed-zombie recovery gene is not created; its only primary
  support is a loading tip.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current Standard Edition Windows availability,
  the separate 2026 relisting of the 1998 game and the official manual's
  mode, control, aim, reload, interaction, inventory, health, map and save
  rules are fixed in `RE2R-001`, `RE2R-003`–`RE2R-011`.
- [Observation | Corroborated | High] The current branch state, the opening
  route, the Main Hall entry contents, the arrival objective, the absence of a
  chapter structure and the damaged outcome branch are bounded in
  `RE2R-002`, `RE2R-014`–`RE2R-017`, `RE2R-019` and `RE2R-020`.

## New genes

- [Confirmed | Direct | High] `CON-621` isolates a paused, fixture-bound
  manual save that is refused while a hostile is nearby.

## New combinations

- [Observation | Corroborated | High] `No new combinations`; none of the 271
  verified sets is a strict subset of this signature.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_040` generalises `SYS-776`
  and `INF-303`; no prior signature, lifecycle or ID changes.

## New questions

- Does Darkest Dungeon's mandatory Old Road tutorial expose formation slots,
  ability legality, stress and a retained Hamlet successor without importing
  later town management?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0281` — Darkest Dungeon, only under a
  new game-specific calibration prompt after this unit's independent audit.
- Optimisation criterion: replace live survival pressure with turn-ordered
  party combat and persistent roster stress while keeping a retained
  successor terminal.
- Expected information gain: distinguish position-legal abilities and
  affliction stress from the ammunition, health and save boundaries above.
- Backlog impact: advances the recorded 280-to-288 calibration horizon.

## Why this game

- [Hypothesis | Limited | High] The transfer test must succeed on a turn-based
  packet with no shared substrate, so success cannot come from reusing this
  record's shape.
