---
game_id: GAME-0260
slug: metro-exodus
game_title: Metro Exodus
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0258
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-202
    - ACT-235
    - ACT-341
    - ACT-406
    - ACT-409
    - ACT-435
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-578
    - SYS-780
    - SYS-796
    - SYS-797
  constraint:
    - CON-210
    - CON-262
    - CON-282
    - CON-285
    - CON-335
    - CON-579
    - CON-603
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-315
    - INF-316
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Metro Exodus

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `412020`, one-app base package `298828`, ordinary public Windows Build ID
  `6544595`, built and published 2021-04-15; checked 2026-09-05. The build ID
  and timestamp are secondary distribution observations, not a publisher
  semantic version. The 2026-08-26 account/store-link update and its
  2026-09-02 Enhanced Edition DLSS follow-up do not establish a different
  ordinary Windows content build or enter this mechanics packet.
- Product boundary: this is the ordinary base application and executable
  `MetroExodus.exe`, not the separately launched PC Enhanced Edition, Gold
  Edition, Expansion Pass, `The Two Colonels`, `Sam's Story`, Exodus SDK, a
  mod, another Metro game, another platform or a franchise union.
- Platform, input and difficulty: Windows, English interface and subtitles,
  keyboard and mouse, fresh base-game `New Game`, default `Normal`. Controller,
  consoles, macOS/Linux, Reader, Easy, Hardcore and Ranger Hardcore are
  separate packets.
- Entry: start a clean profile, choose `New Game` and `Normal`, and accept first
  ordinary control in the opening `Moscow` route as the protagonist returns
  from the surface and approaches the ruined tunnel. Record actual Health,
  weapon, ammunition, medkit and filter stock. Optional diaries, postcards and
  incidental collection are not prerequisites.
- Primary decision loop: inspect the current route cue, local sight, Health,
  active weapon and ammunition, gas-mask/filter time and wristwatch visibility
  state; walk, sprint, crawl or crouch through the authored route; preserve
  finite filters through hazardous surface intervals and replace one before
  exhaustion; select, aim, fire and reload a carried firearm; collect
  compatible ammunition, filters or medkits and heal after damage; toggle the
  personal light, extinguish reachable local lights, wait in shadow, silently
  neutralise an unaware guard or throw one inert can to divert perception;
  operate required doors, train controls, wheels and the fixed explosive
  interaction; survive the enemy-train route and accept the successor chapter.
- Positive terminal: after the hostile train is destroyed and `Moscow` closes,
  let `Winter` begin. Complete only its mandatory opening conversation/radio
  handoff until ordinary control first returns aboard the moving train, before
  interacting with the route map or exploring the cars. Quit, reload the newest
  retained state and verify that this first ordinary `Winter` control and its
  map interaction remain available; stop without starting `The Volga`.
- Negative terminal: zero Health or unprotected hazardous-air exposure can end
  the current attempt; load/continue restores the latest authored checkpoint
  and replaces failed transient position, Health, ammunition, filter, hostile,
  light, detection and route state. Detection, one takedown, boarding the
  locomotive or planting the final explosive without the retained `Winter`
  reload is not success.
- Included: direct first-person movement and posture; one prompted filter
  replacement; installed filter-time drain under hazardous air; finite carried
  filters, ammunition and medkits; one restorative use; weapon selection,
  aim, fire and reload; direct combat and lethal failure; local sight and
  objective cues; personal-light toggle; extinguishable world lights;
  illumination-dependent hostile acquisition; wristwatch visible/shadow state;
  suspicion, detection, combat, inert-can diversion and unaware close
  neutralisation; required companion-follow and boost interactions only as
  authored gates; doors, train controls, wheel and explosive fixture;
  checkpoints and the retained `Moscow`-to-`Winter` handoff.
- Excluded: PC Enhanced Edition application `1449560`; Expansion Pass and all
  DLC; Gold/bundle contents, SDK and mods; 2026 account linking, store-page
  links and rating metadata; every difficulty and input configuration not
  declared above; Volga and later chapters, open-region exploration, map-route
  selection, day/night and weather strategy, boats and vehicles; backpack or
  workbench crafting, weapon modification, cleaning, degradation and resource
  conversion; equipment upgrades, repair of mask damage, suppressor loadouts,
  pneumatic pressure, throwing knives and damaging explosives; karma,
  surrender, companion-fate consequences and endings; collectibles,
  achievements, optional car detachment, exhaustive stealth or kills; New Game
  Plus, chapter replay, speedrun skips, cheats, debug tools, screenshots,
  official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `412020` from base package
  `298828`; launch the ordinary Windows executable, choose a clean `New Game`
  on `Normal` and retain default keyboard/mouse bindings. Follow only the
  required `Moscow` route; record incoming resources; collect the fixed early
  magazine, take one bounded hit and use one medkit, replace one filter in an
  eligible safe moment, toggle the personal light once and disable it before
  stealth, extinguish at least one reachable world light, observe both lit and
  shadowed wristwatch states, silently neutralise one unaware guard, throw one
  can toward a reachable diversion point, reload after firing, complete the
  required train controls and enemy-train explosive, then perform the stated
  `Winter` reload check. Exact path, target, damage, ammunition, Health, filter
  duration, pickup, guard, light, diversion point and timing are parameters.
- Potential scoped modules: one later named chapter or open-region objective;
  one workbench or field-crafting packet; one weapon-maintenance packet; one
  companion-outcome route; one Ranger Hardcore route; PC Enhanced Edition; or
  either DLC requires its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application/package data and the
  current Steam/Deep Silver pages establish lawful availability, product
  identity, base/DLC/Enhanced separation and official combat, stealth,
  resource, Moscow hazard and companion framing. The official 2026 patch note
  constrains the current metadata-only update. Steam distribution data supplies
  the secondary build observation. Two independent static written guide
  publications corroborate first control, filter, medkit, darkness, diversion,
  train and `Winter` transitions. This is an evidence-backed rules
  reconstruction, not a claimed playthrough or entitlement. No video or audio
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MEX-001` | Steam app `412020` is the current ordinary base product and one-app package `298828` supplies it, distinct from Gold, DLC, SDK and the PC Enhanced Edition | Confirmed | Direct | High | P1–P4 |
| `MEX-002` | The ordinary public Windows branch reports Build `6544595`, published 2021-04-15, and launches `MetroExodus.exe` | Observation | Direct | High | S1 |
| `MEX-003` | The 2026 update adds Deep Silver Account/store-page linking metadata, while its later DLSS correction explicitly concerns Enhanced Edition | Confirmed | Direct | High | P5 |
| `MEX-004` | `Normal` is the default difficulty and preserves meaningful ammunition, supply, inventory and combat pressure | Observation | Corroborated | High | S3 |
| `MEX-005` | Moscow's irradiated surface requires a gas mask; active protection consumes finite filter duration and a replacement spends compatible carried filter stock | Confirmed | Corroborated | High | P3, P4, S2–S4 |
| `MEX-006` | The current filter interval and replacement need are exposed before exhaustion, allowing a deliberate safe-moment exchange | Observation | Corroborated | High | S2, S4 |
| `MEX-007` | Firearms use finite compatible ammunition and reload, while route pickups and medkits support the same continuous Health attempt | Confirmed | Corroborated | High | P3, P4, S2–S4 |
| `MEX-008` | In Hanza spaces, extinguishing local lights, withholding the flashlight and remaining in shadow reduce visual detection; a wristwatch light exposes current visibility | Observation | Corroborated | High | S2, S4 |
| `MEX-009` | An unaware reachable guard admits lethal or non-lethal close neutralisation, and a thrown inert can can redirect eligible hostile attention | Observation | Corroborated | High | S2, S4 |
| `MEX-010` | Detection can escalate into alarm and live firearm combat without invalidating the chapter; checkpoint load replaces failed transient state | Observation | Corroborated | High | S2, S4 |
| `MEX-011` | Required companion-follow, boost, train-control, wheel and rescue steps form authored dependencies rather than a general companion-command system | Observation | Corroborated | High | P4, S2, S4 |
| `MEX-012` | Boarding the hostile train, traversing or neutralising its guards and accepting the fixed boiler explosive closes `Moscow` | Observation | Corroborated | High | S2, S4 |
| `MEX-013` | `Winter` follows aboard the train; after its opening handoff ordinary control returns before the optional map interaction that would start `The Volga` | Observation | Corroborated | High | S2, S4 |
| `MEX-014` | The bounded identity is a finite breathing interval crossed with light-readable stealth and firearm resource pressure before an authored train escape settles into retained successor control | Strong Pattern | Corroborated | High | `MEX-005`–`MEX-013` |

## Basic data

- Release / origin: 4A Games and Deep Silver; original product released in
  2019, while the current Steam record lists 2020-02-14 for its Steam release.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `412020`; one fresh default-Normal `Moscow` packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=412020&cc=ua&l=english),
    for exact title/app, Windows and English support, single-player, developer,
    publisher, packages, DLC list, current Ukraine offer and Enhanced
    entitlement notice.
  - **[P2]** [Valve base-package data](https://store.steampowered.com/api/packagedetails?packageids=298828&cc=ua&l=english),
    for package `298828` containing only app `412020`, its platform support and
    current Ukraine offer.
  - **[P3]** [current Steam product page](https://store.steampowered.com/app/412020/Metro_Exodus/?l=english),
    for lawful availability, story-driven first-person combat/stealth,
    exploration, scarce resources, gas-mask atmosphere, DLC separation and PC
    Enhanced notice. Embedded media was not opened or used.
  - **[P4]** [official Deep Silver product page](https://www.deepsilver.com/games/metro-exodus),
    for 4A/Deep Silver identity, combat/stealth/survival framing, Moscow surface
    radiation, at-all-times gas-mask requirement, scarce ammunition/supplies,
    Aurora journey and Anna's mission support. Trailer media was not accepted,
    opened or used.
  - **[P5]** [official 2026 Steam patch note](https://store.steampowered.com/news/app/412020/view/1842212951297245),
    for Deep Silver Account features, store-page link clarification and the
    separate Enhanced Edition DLSS correction.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots and configuration](https://steamdb.info/app/412020/depots/),
    for ordinary Windows depots `412021`/`412022`, public Build `6544595`, its
    timestamp and ordinary executable observation. SteamDB is secondary and is
    not treated as the publisher.
  - **[S2]** [GamePressure static Moscow route](https://www.gamepressure.com/metro-exodus/moscow-1/zebe2e),
    including its linked `Visit Sewers`, `A journey with Anna`, `Inside the
    enemy base`, `Hostile Train` and `Winter` pages, for first control, fixed
    magazine, prompted struggle, filter exchange, medkit, shadow/light,
    takedown, can diversion, train controls, explosive, chapter close and
    successor order. Images were not opened or used.
  - **[S3]** [GamePressure static difficulty and filter notes](https://www.gamepressure.com/metro-exodus/what-are-the-differences-in-difficulty-levels/zabe2a),
    together with its linked gas-mask-filter note, for default `Normal`,
    inventory/combat pressure, toxic-air protection and replaceable filter
    stock. Images were not opened or used.
  - **[S4]** [Game of Guides static Moscow route](https://video-game-guide-walkthrough.supersoluce.com/solution/metro-exodus-guide-walkthrough/moscow/),
    including its text-only `VDNKh`, `Hansa's Jammers`, `Stealing a Train`,
    `Fleeing Moscow` and `Winter` pages, for independent first-control,
    magazine, medkit, gas-mask/filter, wristwatch visibility, light, stealth,
    train, explosive, chapter and first-successor-control corroboration. Images
    were not opened or used.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S4` under the declared app, package, build, platform,
  input, difficulty, clean entry, exclusions and retained terminal; rules
  reasoning, not direct play.
- Claim IDs: `MEX-001`–`MEX-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint and traverse the authored tunnel,
  surface, base and train route; `ACT-202`: crouch or crawl through concealment
  and restricted passages; `ACT-161`: aim and fire a firearm or commit the
  admitted close attack; `ACT-164`: select a carried weapon; `ACT-183`: reload
  it from compatible finite ammunition.
- Existing `ACT-199`: transfer a compatible magazine, filter, medkit or weapon
  into carried state; `ACT-131`: spend one medkit after Health loss;
  `ACT-341`: operate doors, lights, companion boost, train controls, wheel and
  fixed explosive interaction; `ACT-409`: toggle the personal flashlight.
- Existing `ACT-235`: commit one lethal or non-lethal close neutralisation
  against an unaware reachable guard; `ACT-406`: throw one inert can toward a
  reachable diversion point. New `ACT-435`: deliberately replace the current
  breathing-equipment filter from finite compatible carried stock.
- Names, bindings, actors, weapons, lights, fixtures, cartridge quantities and
  exact timings remain parameters. Claims: `MEX-005`–`MEX-012`.

### System Behaviour Genes

- Existing `SYS-208`: firearm damage resolves at the struck region; `SYS-215`:
  perception, movement, attacks, damage and defeat continue in real time;
  `SYS-578`: damage and medkit recovery change continuous Health and zero ends
  the attempt; `SYS-369`: load restores an authored checkpoint.
- Existing `SYS-373`: local sight, sound, movement or harm escalates suspicion
  into detection/alarm and combat; `SYS-057`: a perceived actor or deliberate
  inert-can stimulus can replace a guard's patrol/search target; `SYS-780`:
  final `Moscow` completion retains ordinary `Winter` successor control.
- New `SYS-796`: hazardous-air occupancy consumes installed filter duration
  before unprotected exposure harms Health. New `SYS-797`: local world and
  carried illumination alter hostile visual acquisition without granting
  intrinsic invisibility.
- Resolution order: movement changes region, sightline and illumination;
  hazardous atmosphere checks mask/filter state and drains duration; a filter
  exchange spends carried stock; weapon inputs validate equipment and
  ammunition before live hit/damage; light, movement and a thrown can update
  perception; contextual train gates advance the authored route; lethal
  failure restores a checkpoint; the final explosive closes the chapter and
  admits retained successor control. Claims: `MEX-005`–`MEX-014`.

### Constraint Genes

- Existing `CON-210`: carried filters, medkits, ammunition and weapons obey
  typed finite capacity; `CON-262`: weapon, magazine and reserve ammunition are
  finite; `CON-285`: fire/reload require compatible weapon, ammunition and
  current action state; `CON-579`: medkit use requires missing Health and
  positive carried stock.
- Existing `CON-335`: a close stealth neutralisation requires an eligible
  unaware guard in the required reach/position; `CON-282`: tunnel, Anna,
  Hanza, locomotive, wheel, pursuit-train, explosive and `Winter` gates require
  their authored predecessors.
- New `CON-603`: safe action in the hazardous atmosphere requires compatible
  worn breathing equipment with positive filter duration; replacement requires
  a carried compatible cartridge.
- Scarce resources: protected-breath duration, carried filters, Health,
  medkits, weapon magazine/reserve, darkness, cover, safe interaction time and
  checkpoint-local progress. Exact values are parameters. Claims:
  `MEX-005`–`MEX-013`.

### Information Genes

- Existing `INF-073`: active weapon and magazine/reserve state are visible;
  `INF-115`: current sight and documented spatial cues expose only local
  threats; `INF-119`: Health and immediate personal state remain visible;
  `INF-125`: current objective and authored route cues expose the next known
  gate; `INF-128`: pickups and carried state expose identity, compatibility and
  available capacity.
- New `INF-315`: the worn gas mask/watch and replacement warning expose
  current protected-breath duration before exhaustion. New `INF-316`: a
  body-carried indicator exposes current lit or shadowed visibility without
  identifying every observer or displaying directional detection progress.
- Exact dial, colour, icon, prompt wording, units and UI position are
  presentation parameters. Claims: `MEX-005`–`MEX-010`.

### Objective Genes

- Existing `OBJ-155`: survive and complete the ordered `Moscow` survival-action
  segment, accept its explicit chapter boundary and retain reloadable ordinary
  control in immediate successor `Winter` before map interaction.
- One filter change, stealth route, alarm, captured locomotive, explosive or
  unverified cutscene is not success. Claims: `MEX-011`–`MEX-014`.

### Time Genes

- Existing `TIM-003`: filter drain, movement, illumination, perception,
  attacks, reload, healing exposure and train traversal advance in real time.
- Existing `TIM-007`: a retained checkpoint or successor state can be restored
  so another movement, light, diversion, filter or combat choice replaces the
  failed future; this is not an in-world rewind command.
- Claims: `MEX-005`–`MEX-014`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean profile has `New Game` and `Normal` selected | Accept first ordinary control on the opening Moscow route | The authored tunnel state begins with no imported later equipment or chapter history | fixed fresh entry | `MEX-001`, `MEX-004` |
| A fixed early body holds a compatible magazine | Collect it and inspect the active weapon | The magazine enters compatible carried ammunition state up to capacity | finite route pickup | `MEX-007` |
| The route enters hazardous surface air with protection active | Remain exposed for a bounded interval | Installed filter duration decreases while direct atmospheric harm is withheld | live protective reserve | `MEX-005`, `MEX-006` |
| Remaining protected duration approaches the warning threshold and a filter is carried | Reach a safe eligible moment and replace the filter | One carried cartridge is spent and installed protected duration increases | deliberate filter exchange | `MEX-005`, `MEX-006` |
| Health is below its cap and one medkit is carried | Use the medkit | One unit leaves stock and Health rises without rewinding the route | bounded restorative use | `MEX-007` |
| A Hanza route position is illuminated | Extinguish its reachable light and keep the personal flashlight off | Current light exposure falls and visual acquisition pressure is reduced, not eliminated | controllable stealth illumination | `MEX-008` |
| The wristwatch visibility indicator is restored | Move once into a lit position and once into shadow | Its state distinguishes current visible and shadowed exposure before a specific guard necessarily detects the actor | actionable illumination feedback | `MEX-008` |
| One guard is unaware and reachable from the required position | Commit a close lethal or non-lethal neutralisation | The guard is removed from active perception/combat without an ordinary exchange of fire | awareness-gated neutralisation | `MEX-009` |
| A guard watches the intended route and an inert can is available | Throw the can toward another reachable point | The audible landing can replace the guard's current attention/search target | positioned perception diversion | `MEX-009` |
| A guard completes visual or audible detection | Hide, move, neutralise or fight | Suspicion becomes alarm/combat; chapter progress remains recoverable rather than automatically failing | stealth-to-combat transition | `MEX-008`–`MEX-010` |
| Health reaches zero before the chapter transition | Continue/load the latest checkpoint | Failed position, Health, ammunition, filters, light and hostile state are replaced by the retained snapshot | reproducible negative recovery | `MEX-010` |
| Anna and Yermak have been recovered | Operate the controls and complete the required wheel interaction | The locomotive becomes the crew's authored escape platform and the pursuit sequence begins | fixed companion/fixture chain | `MEX-011` |
| The hostile train is boarded and its boiler is reached | Accept the fixed explosive interaction and return | The pursuing train is destroyed and `Moscow` closes | explicit segment completion | `MEX-012` |
| `Winter` begins after the opening handoff | Wait until ordinary control returns aboard the train, then quit and reload | The same first controllable `Winter` state returns with the map still unused and `The Volga` unopened | reproducible positive terminal | `MEX-013`, `MEX-014` |

## Strategic and experiential structure

- Planning horizon: current route and objective identify the next gate, but
  filter time, Health, ammunition and light exposure determine whether to cross
  now, replace protection, remain in shadow, divert or fight.
- Local tactics: exchange the filter before exhaustion in a safe position,
  extinguish reachable lights, read the wristwatch before leaving shadow,
  preserve the flashlight, wait for an unaware relation and direct the can
  stimulus away from the intended path.
- Medium-term structure: the route alternates hazardous surface intervals,
  companion-authored traversal, scarce-resource combat and light-sensitive
  infiltration, then commits train fixtures and a pursuit sequence into a
  named chapter boundary rather than an arbitrary stop.
- Reversible versus irreversible: movement, posture and light toggles can be
  changed; a filter exchange, medkit and ammunition spend finite stock; a
  takedown, alarm and train interaction alter the attempt; checkpoint load
  replaces failure; `Winter` retention persists.
- Failure attribution: weapon/ammunition, Health, pickup capacity, filter
  warning, wristwatch exposure, current light, local perception and objective
  state separate exhausted protection, unsafe illumination, missing resource,
  failed stealth and lethal combat.
- Player trust: the filter interval visibly approaches exhaustion, darkness
  changes the wearable visibility signal, accepted fixtures advance their
  route and a reloaded successor chapter verifies settlement.

## Replay and variation

- What changes: route timing, filter replacement point, ammunition, reload,
  Health, medkit use, light state, guard awareness, diversion point, stealth or
  combat choice and checkpoint use.
- Randomness or procedural generation: topology, major actors, fixtures and
  chapter order are authored. Minor encounter timing and drops may vary, but no
  random-generation claim enters this packet.
- Multiple strategies: some guards may be bypassed, disabled, killed or fought
  after detection. This control deliberately demonstrates one light change,
  one visibility reading, one takedown and one inert diversion without making
  a no-alert or no-kill outcome the terminal.
- Typical replay motive: conserve filters, ammunition and Health while finding
  a cleaner shadow route through the same train escape.

## Adjacent systems and history

- Crysis Remastered shares first-person firearm pressure, posture, detection,
  checkpoints and an authored chapter handoff. Its four Nanosuit modes compete
  for one rechargeable energy pool; Metro Exodus instead spends replaceable
  breathing time and lets ambient/carried light shape ordinary perception.
- Far Cry 3 shares firearm stealth, an inert thrown diversion, unaware close
  neutralisation and alert-to-combat recovery. Its camera produces retained
  actor marks and the outpost becomes an allied service node; Metro Exodus uses
  a personal light-exposure indicator and a chapter-successor train boundary.
- S.T.A.L.K.E.R. 2: Heart of Chornobyl shares finite survival resources,
  radiation pressure, firearm combat and authored checkpoints. It couples a
  detector to anomalies/artifacts and branching evidence; Metro Exodus couples
  a replaceable air filter to light-sensitive infiltration in one linear
  opening chapter.
- Fallout 4 shares fresh-start first-person combat, pickups, healing and a
  retained early quest terminal. Its character attributes and open-world quest
  state dominate the packet; Metro Exodus fixes a preconfigured protagonist
  and converts filters, shadow and authored train fixtures into settlement.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-406`, `ACT-409`, `ACT-435` | actor, route, filter, weapon, light, guard, can and fixture names are parameters |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`, `SYS-780`, `SYS-796`, `SYS-797` | drain, harm, light, perception and checkpoint values are parameters |
| Constraint | `CON-210`, `CON-262`, `CON-282`, `CON-285`, `CON-335`, `CON-579`, `CON-603` | capacities, compatibility, reach, order and quantities are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-315`, `INF-316` | watch art, colours, warnings, units and UI layout are parameters |
| Objective | `OBJ-155` | chapter, train, successor and retained state are parameters |
| Time | `TIM-003`, `TIM-007` | drain, detection, combat and load time are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `259` (`GAME-0001`–`GAME-0259`).
- Exact genome matches: none.
- Tied near matches: `GAME-0259` — Dead Space (2023 remake) (`25 / 48 = 0.520833`).
- Supported combination subsets: `COMB-0258`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0259` — Dead Space (2023 remake) | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-780`, `CON-210`, `CON-262`, `CON-282`, `CON-285`, `CON-579`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `OBJ-155`, `TIM-003`, `TIM-007` | Both move finite ammunition, healing, pickups and authored interactions through live survival combat, checkpoint recovery and a reload-verified successor chapter. Dead Space turns an oriented cutter into visible regional severance and uses finite Stasis plus limited circuit capacity for tram repair. Metro Exodus instead spends replaceable breathing-filter time, exposes the actor's own illumination and lets controlled lights, shadow and inert diversion shape hostile perception before a train escape. | Near, `0.520833` |

### Preserved research notes

- New genes: `ACT-435`, `SYS-796`, `SYS-797`, `CON-603`, `INF-315`,
  `INF-316`.
- Reused genes: `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`,
  `ACT-199`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-406`, `ACT-409`,
  `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`,
  `SYS-780`, `CON-210`, `CON-262`, `CON-282`, `CON-285`, `CON-335`,
  `CON-579`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`,
  `OBJ-155`, `TIM-003`, `TIM-007`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Lower-ID scan: reject `SYS-327`, which integrates several open-survival
  metabolism/environment meters rather than an installed finite filter before
  harm; reject `SYS-754`/`SYS-791`, whose light reserve changes while Metro's
  necessary new relation is light-to-hostile acquisition; reject `INF-298`,
  which exposes direction and escalation of a particular incoming detection
  rather than actor-centred current illumination; reject a generic companion
  command because Anna/Yermak steps are fixed authored gates.

## Taxonomy impact

- Registry changes: add six Active genes, `ACT-435`, `SYS-796`, `SYS-797`,
  `CON-603`, `INF-315` and `INF-316`, plus `COMB-0258`; add independent support
  to reused genes. No existing definition, lifecycle or earlier signature
  changes.
- Taxonomy-change record: none; no split, merge, deprecation or broadening.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, actor,
  chapter, faction, item, fixture, app, package and build names remain
  parameters.

## Negative results

- No video or audio evidence was used; only official static text/data and
  static written routes support this packet.
- PC Enhanced Edition, DLC, Volga, later crafting/maintenance, karma and the
  2026 account/store-link surface are excluded even though the current product
  exposes them elsewhere.
- The opening quick-time prompt is an authored reflex gate, not a new planning
  gene; companion follow/boost behaviour is fixed route state, not a general
  command system.
- `SYS-796` enters only because installed filter duration prevents atmospheric
  harm until depletion; `SYS-797` enters only because player-controlled world
  and carried light state changes hostile acquisition.
- A filter change, quiet base crossing or enemy-train explosion is not the
  terminal; reload-verified first ordinary `Winter` control is required.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `MEX-001`–`MEX-014`:
  one opening chapter couples finite protected breath, actor-visible light
  exposure and recoverable stealth/combat with an authored train escape.

## New genes

- [Confirmed/Observation | Corroborated | High] Added `ACT-435`, `SYS-796`,
  `SYS-797`, `CON-603`, `INF-315` and `INF-316`.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0258` — filter-bounded hazardous
  passage and light-readable infiltration feed a retained train-escape chapter.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Six portable genes are added; no
  prior definition, lifecycle or reviewed signature changes.

## New questions

- Does The Last of Us Part I retain the same authored survival-action and
  light/stealth skeleton while replacing breathing equipment with listening,
  crafting and companion encounter state?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0261` — The Last of Us Part I.
- Optimisation criterion: preserve a bounded early authored survival-action
  terminal while varying the information and preparation channels.
- Expected information gain: distinguish personal environmental exposure from
  listening-mediated stealth, crafted scarcity and companion scripting.
- Backlog impact: advances the approved batch-014 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] The Last of Us Part I keeps authored,
  resource-constrained stealth/combat but changes what the player can inspect,
  prepare and retain through an early successor boundary.
