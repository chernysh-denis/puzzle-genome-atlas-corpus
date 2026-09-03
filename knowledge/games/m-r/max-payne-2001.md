---
game_id: GAME-0238
slug: max-payne-2001
game_title: "Max Payne (2001)"
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0236
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-229
    - ACT-341
    - ACT-407
  system:
    - SYS-215
    - SYS-348
    - SYS-368
    - SYS-369
    - SYS-750
    - SYS-751
  constraint:
    - CON-262
    - CON-269
    - CON-282
    - CON-285
    - CON-579
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Max Payne (2001)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `12140`, public Build ID `252034`, built and published 2014-05-01 and checked
  2026-09-03. This is Remedy's original 2001 PC game, not a sequel, mobile port
  or announced remake. Rockstar's current support record identifies the latest
  full original-PC patch as `v1.05`; the depot's internal executable string was
  not independently inspected, so the patch label is not silently treated as a
  synonym for the Steam Build ID. Only a fresh campaign in default `Fugitive`
  mode and Part I, Chapter 1 `Roscoe Street Station` are admitted.
- Entry: choose New Game on a fresh local profile, retain the default Fugitive
  mode, complete the prologue without imported saves or cheats and keep the
  automatic chapter-start save. The packet begins at first direct control after
  Max leaves the subway car on Platform 5 in `Roscoe Street Station`, before a
  weapon is drawn.
- Primary decision loop: read local third-person sight, pain, carried
  painkillers, Bullet Time, active weapon, magazine and reserve ammunition;
  navigate the authored station; open or activate reachable fixtures; acquire
  compatible weapons and supplies; aim, fire, reload and switch weapons;
  activate Bullet Time or a directional Shootdodge when its finite meter is
  available; consume a painkiller when missing health justifies delayed
  recovery; survive adaptive Fugitive opposition; unlock the control room,
  power Line 2, drive the train through the barrier and cross the fixed next-
  chapter threshold.
- Positive terminal: after powering Line 2 and using the train to break the
  track barrier, settle the remaining required encounter and route gates, follow
  the left branch and enter the authored door that settles Chapter 1. Retain the automatic first
  controllable state of Windows-PC Chapter 2 `One Way or the Other`, the opening
  segment of the broader `Live from the Crime Scene` chapter sequence. The
  intermediate `So Much for Being Subtle` save point is not completion.
- Negative terminal: when the pain bar fills, Max dies and the active attempt
  ends. Load the latest retained automatic or manual save; the failed position,
  health, ammunition, hostile and fixture state is replaced rather than carried
  into success. Deleting or importing saves is outside scope.
- Included: direct third-person walking, running, jumping and route traversal;
  aimed handgun, shotgun and melee attacks; active-weapon selection, magazine
  reload and compatible finite ammunition; reachable weapon, ammunition and
  painkiller acquisition; usable doors, lockers and panels; pain health, death,
  delayed painkiller recovery and eight-unit carried cap; Bullet Time meter
  drain, kill-linked restoration, toggle and directional Shootdodge; visible
  local enemies, weapons, ammunition, pain, special meter and mission objective;
  default Fugitive performance adjustment; the transit officer opening access;
  Line 2 activation, train movement, barrier breach, fixed route and Chapter 2
  transition; ordinary save/checkpoint replacement after failure.
- Excluded: the prologue except as entry provenance; every Chapter 2 action and
  all later chapters; optional televisions, radios, graphic-novel review,
  documents, cabinets, secret rooms and exhaustive pickups; enemy or supply
  counts as genes; Hard-Boiled, Dead on Arrival, New York Minute and The Last
  Challenge; Parental Lock variants; cheats, developer mode, speedrun routes,
  glitches, mods, community compatibility fixes and imported saves; Max Payne 2,
  Max Payne 3, mobile, console and Mac ports, the announced remake project and
  the full campaign or franchise.
- Reproducible parameterisation: install the current English Windows Steam
  branch without third-party files; use default keyboard/mouse bindings and a
  fresh local profile; begin New Game in the only initially available Fugitive
  mode; retain the chapter-start save after the prologue. Search the opening
  room, survive the fixed encounters using ordinary movement, firearms, reload,
  Bullet Time or Shootdodge and painkillers as needed; follow the transit officer
  to the unlocked control area, activate Line 2, board and operate the train,
  cross its broken barrier and enter the next chapter. Exact aim, weapon choice,
  ammunition, item use, adaptive response, damage, save frequency and completion
  time are run parameters.
- Potential scoped modules: the prologue as its own tutorial packet; Chapter 2
  `One Way or the Other` through a later named save point; one fixed higher-
  difficulty chapter; New York Minute as a separately timed ruleset. None is
  imported here.
- Compatibility status: the product remains lawfully sold for Windows, but its
  official store requirements name legacy Windows versions and Valve currently
  marks Steam Deck support as unresolved. This unit therefore establishes the
  current unmodified distribution and stable authored ruleset, not an unsupported
  claim that it launches unchanged on every current Windows 10/11 host.
- Direct-play status: not conducted. The current Steam product, Rockstar product
  and support records, official PC manual, distribution metadata and two
  independent written PC routes establish the declared identity, controls,
  systems, entry, gates and terminal. The trace below is evidence-backed rules
  reconstruction, not a claimed captured playthrough. No video or audio was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MP1-001` | The admitted product is Remedy's original 2001 Windows Max Payne, current Steam app `12140`, not a sequel, port or remake | Confirmed | Direct | High | P1, P2 |
| `MP1-002` | The public Steam branch is Build ID `252034`, built and updated 2014-05-01; Rockstar currently preserves the original PC `v1.05` patch record | Confirmed | Corroborated | High | P3, S1 |
| `MP1-003` | Fugitive is the only initially available mode and adjusts hostile behaviour and performance according to player effectiveness | Confirmed | Direct | High | P2 |
| `MP1-004` | Chapter 1 starts with direct control on Platform 5 at Roscoe Street Station and ends at the fixed Chapter 2 transition | Observation | Corroborated | High | S2, S3 |
| `MP1-005` | Direct traversal, aimed attacks, weapon switching, finite ammunition and reload resolve against live hostile movement and damage | Confirmed | Corroborated | High | P1, P2, S2, S3 |
| `MP1-006` | Bullet Time drains a finite visible meter, slows surrounding action while aim remains real-time and regains charge from eligible enemy defeats | Confirmed | Direct | High | P2 |
| `MP1-007` | Direction plus Bullet Time input commits a slow-motion Shootdodge and spends charge; without charge the same request becomes an ordinary roll | Confirmed | Direct | High | P2 |
| `MP1-008` | Painkillers are capped at eight, consume one unit, mark a recoverable pain portion and take several seconds to settle while later damage remains additive | Confirmed | Direct | High | P2 |
| `MP1-009` | Reachable lockers, cabinets, world supplies and defeated hostiles provide compatible ammunition, weapons or painkillers | Observation | Corroborated | High | P2, S2, S3 |
| `MP1-010` | The ordered route requires the transit officer's access, control-room activation, Line 2 power and operation of the train through its barrier | Observation | Corroborated | High | S2, S3 |
| `MP1-011` | Pain-bar completion produces death; loading a retained save replaces the failed attempt's transient state | Confirmed | Corroborated | High | P2, P4, S2 |
| `MP1-012` | Entering the final track door closes Roscoe Street Station and reaches the Windows-PC Chapter 2 `One Way or the Other` state | Observation | Corroborated | High | S2, S3 |
| `MP1-013` | The transferable identity is authored third-person firearm routing whose finite slow-time resource, non-blocking delayed medicine and adaptive opposition remain coupled until a mechanical train breach opens the next chapter | Strong Pattern | Corroborated | High | MP1-003–MP1-012 |

## Basic data

- Release / origin: developed by Remedy Entertainment, produced by 3D Realms
  and currently published by Rockstar Games; original Windows release
  2001-07-25; current Steam distribution checked 2026-09-03.
- Platform or physical form: authored single-player third-person action game;
  only one early chapter on the current unmodified English Windows Steam branch.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/12140/Max_Payne/),
    for current lawful Windows sale, app `12140`, original 2001 identity,
    single-player scope and official Bullet Time framing.
  - **[P2]** [official English PC manual](https://cdn.akamai.steamstatic.com/steam/apps/12140/manuals/manual_en.pdf),
    for default Fugitive adaptive difficulty, controls, usable fixtures,
    weapons, magazines, reload, pain health/death, eight-painkiller cap,
    delayed additive recovery, Bullet Time drain/kill recovery, Shootdodge,
    objective review, save/load and excluded modes.
  - **[P3]** [Rockstar Support original-PC patch record](https://support.rockstargames.com/articles/3IxigHHyFE1ZrS3hiSkf2V/patch-info-max-payne),
    observed 2026-09-03, for the preserved full `v1.05` patch boundary; no
    equivalence to the Steam Build ID is inferred.
  - **[P4]** [Rockstar Support save-location record](https://support.rockstargames.com/articles/3cegi0lpJbDSec7iV8pkmR/location-of-max-payne-save-games-on-pc),
    for original Windows save persistence in the current user's documents.
  - **[P5]** [official Rockstar product record](https://www.rockstargames.com/games/maxpayne),
    for publisher-maintained product identity; its dynamic page provides no
    additional chapter-level claim.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/12140/depots/), observed
    2026-09-03, for public Build ID `252034`, built and updated 2014-05-01,
    Windows depot `12141`, English depot `12142` and unresolved Steam Deck
    support. SteamDB identifies itself as unaffiliated with Valve.
  - **[S2]** [StrategyWiki Chapter 1 route](https://strategywiki.org/wiki/Max_Payne/Chapter_1:_Roscoe_Street_Station),
    for Platform 5 entry, opening supplies, ordered station route, officer,
    control-room/Line 2 interactions, train barrier and next-chapter branch.
    Embedded video was not loaded or used.
  - **[S3]** [GameFAQs PC written walkthrough](https://gamefaqs.gamespot.com/pc/913964-max-payne/faqs/27523),
    for independent Windows-PC chapter labels, first control, weapon/painkiller
    acquisition, Shootdodge use, save points, Line 2 activation, train breach
    and the Chapter 2 `One Way or the Other` transition.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S3` under the fixed app/build, Fugitive, fresh-profile
  entry, chapter boundary and exclusions; no direct-play or audiovisual claim.
- Claim IDs: `MP1-001`–`MP1-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run, walk and jump through the platforms,
  corridors, control rooms, train and final tunnel; `ACT-161`: aim and commit a
  legal melee or firearm attack; `ACT-164`: select an owned weapon; `ACT-183`:
  reload the active magazine from compatible reserve; `ACT-199`: transfer a
  reachable compatible weapon, ammunition or painkiller into carried state.
- Existing `ACT-229`: activate/toggle Bullet Time when ready, including its
  direction-parametrised Shootdodge form; `ACT-341`: open or activate reachable
  doors, lockers, panels, Line 2 control and train control.
- New `ACT-407`: consume one carried painkiller without suspending direct
  movement, aiming or attack authority, beginning its delayed recovery.
- Shootdodge is not a game-named gene: its direction, displacement, slow-motion
  form and zero-meter fallback are parameters of special activation and
  movement. Exact weapons, inputs, pickups and fixture labels are parameters.
- Claim IDs: `MP1-005`–`MP1-010`.

### System Behaviour Genes

- Existing `SYS-215`: resolve Max and hostile firearm/melee exchanges in real
  time; `SYS-348`: apply damage through visible pain to death; `SYS-368`: drain
  the active Bullet Time meter, apply temporary time/combat modifiers and
  restore charge through eligible defeats; `SYS-369`: replace a failed attempt
  with the selected retained chapter save.
- New `SYS-750`: after accepted medicine use, settle the marked recoverable pain
  portion over several seconds while newer damage remains additive; new
  `SYS-751`: Fugitive evaluates recent effectiveness and adjusts eligible enemy
  behaviour/performance without a new difficulty choice.
- Resolution order: accept movement, fixture, weapon, special or medicine input;
  validate weapon, ammunition, special meter, missing health and stock; resolve
  combat and local actor motion; drain or restore Bullet Time; apply damage and
  pending pain recovery; update Fugitive response; persist or load the current
  save after failure; propagate officer, panel, train and barrier gates; crossing
  the final door hands control to Chapter 2.
- Claim IDs: `MP1-003`, `MP1-005`–`MP1-012`.

### Constraint Genes

- Existing `CON-262`: carried weapons, magazines, reserve ammunition and
  consumables are finite; `CON-269`: Bullet Time activation requires available
  resource/readiness; `CON-282`: officer access, control panels, powered train,
  barrier breach and successor follow authored order; `CON-285`: firing,
  switching and reload require compatible live weapon/ammunition state.
- New `CON-579`: painkiller use requires eligible missing health and positive
  carried stock, consumes one unit and cannot restore above cap.
- Scarce strategic resources: pain/health margin, painkillers, loaded and
  reserve ammunition, Bullet Time charge, safe sightline, movement space and a
  retained save origin.
- Claim IDs: `MP1-006`–`MP1-011`.

### Information Genes

- Existing `INF-073`: active weapon, magazine/reserve and carried medicine are
  inspectable; `INF-115`: third-person local sight and explicit spatial effects
  reveal nearby enemies, projectiles, pickups and route fixtures rather than an
  omniscient chapter state; `INF-119`: the pain silhouette, pending faded
  recovery and Bullet Time meter expose personal resources; `INF-125`: F2
  mission objective and authored route cues expose the current gate.
- Audio is not evidence for this unit. Exact icon art, reticle, colour, camera
  offset and numeric run values remain parameters.
- Claim IDs: `MP1-005`–`MP1-010`.

### Objective Genes

- Existing `OBJ-026`: make the chapter route traversable through officer,
  control-panel and train state, then reach its designated final door and
  retain the named Chapter 2 control state.
- One fight, pickup, control-room unlock, Line 2 activation, barrier breach or
  intermediate save is not the positive terminal. Full campaign completion is
  outside scope.
- Claim IDs: `MP1-004`, `MP1-010`, `MP1-012`.

### Time Genes

- Existing `TIM-003`: enemies, projectiles, Bullet Time drain, delayed recovery
  and adaptive combat continue on a real-time schedule while the player moves,
  aims, fires or operates the route. Slow motion changes rate, not turn order.
- Menus, graphic-novel transitions and save loading do not define another time
  model.
- Claim IDs: `MP1-005`–`MP1-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh local profile has completed the prologue in default Fugitive mode | Accept first control after the subway car opens at Platform 5 | Roscoe Street Station becomes active with its chapter-start save and no initially drawn weapon | exact entry and mode | `MP1-003`, `MP1-004` |
| Blood trail leads to the reachable transit room | Enter and approach the authored scene | Max draws the supplied handgun; compatible ammunition and one painkiller become collectible | authored equipment start | `MP1-005`, `MP1-009` |
| A compatible firearm is active and a hostile is locally exposed | Aim and fire, then reload when tactically safe | Loaded ammunition falls; hit/damage/defeat and hostile action resolve continuously; reload transfers reserve into the magazine | direct live firearm kernel | `MP1-005` |
| Bullet Time meter is positive during an exposed encounter | Activate in place or with a movement direction | Surrounding action slows while aim remains real-time; the meter drains, and directional activation commits Shootdodge | finite tempo intervention | `MP1-006`, `MP1-007` |
| Bullet Time is depleted and a directional special request is entered | Commit the same direction plus special input | No slow-motion dive is legal; an ordinary rolling dodge replaces it | resource-gated fallback | `MP1-007` |
| Max has eligible missing health and carries a painkiller | Consume one during live control | Stock falls by one; a faded recoverable portion settles over seconds while movement and combat continue | non-blocking delayed recovery | `MP1-008` |
| Recovery remains pending and a hostile attack lands | Remain exposed | New damage is added over the faded recovery state before the prior item has fully settled | healing does not erase live risk | `MP1-008` |
| Recent play becomes persistently weak or strong under Fugitive | Continue through later eligible encounters | Enemy behaviour/performance shifts in the stated favourable or challenging direction within the same selected mode | adaptive opposition | `MP1-003` |
| The transit officer is alive at the personnel room | Clear the immediate threat and follow him | He opens access to the upper control area before the authored death scene | actor-gated route change | `MP1-010` |
| The control room is reachable but Line 2 is unpowered | Activate the required control panel | Line 2 receives power and the train below becomes operable | switch-to-route dependency | `MP1-010` |
| The powered train is available before the blocked track | Board and operate its control | The train advances through the barrier, converting the blocked track into the final traversable route | mechanical breach gate | `MP1-010` |
| The final track branch is open | Follow it and enter the authored door | Chapter 1 closes, an automatic save settles and Windows-PC Chapter 2 `One Way or the Other` grants first control | reproducible positive terminal | `MP1-012` |
| Pain reaches its full threshold before the chapter transition | Load the latest retained save | Failed position, pain, stock, ammunition, enemies and fixtures are replaced with the saved state | reproducible failed-attempt recovery | `MP1-011` |

## Strategic and experiential structure

- Planning horizon: preserve loaded rounds, compatible reserve, medicine and
  Bullet Time across several fixed station encounters while recognising that
  Fugitive may alter later opposition from recent performance.
- Local tactics: choose handgun or shotgun by range; reload behind geometry;
  spend Bullet Time before several firing lines overlap; direct Shootdodge into
  a useful landing position; take medicine early enough for delayed recovery to
  settle instead of treating it as invulnerability.
- Medium-term structure: combat opens an officer dependency, the officer opens
  a control route, Line 2 activates a vehicle, and the vehicle transforms a
  physical barrier before the next-chapter threshold is reachable.
- Failure attribution: weapon/ammunition, pain, faded pending recovery, special
  meter, local enemy position and objective state separate poor aim, unsafe
  reload, late healing, exhausted slowdown and missed fixture order.
- Player-trust factors: the manual discloses Fugitive adaptation and every
  special/healing rule admitted here; required control changes produce visible
  route consequences; a named next-chapter state replaces an arbitrary stopping
  point.
- Claim IDs: `MP1-003`–`MP1-013`.

## Replay and variation

- What changes between attempts: weapon emphasis, ammunition pickup and spend,
  aim, hostile position, adaptive response, Bullet Time timing, Shootdodge
  direction, medicine timing, pain, route tempo and manual save placement.
- What remains fixed: product/build, Fugitive selection, authored station
  geometry, officer/control/Line 2/train dependency and final chapter door.
- Multiple viable strategies: cautious corner play, aggressive Shootdodge,
  earlier shotgun use and different medicine timing can reach the same terminal;
  optional exploration is not required.
- Typical replay motive: improve ammunition efficiency, tempo-control timing,
  exposure management or completion speed; New York Minute is a separate mode.
- Claim IDs: `MP1-003`–`MP1-012`.

## Adjacent systems and history

- Direct franchise corridor: Max Payne 2 and Max Payne 3 retain related names
  but change combat, health, content and platform contracts; the announced
  remake is not the 2001 executable.
- Similar lower-ID games: Call of Juarez: Gunslinger shares direct firearm
  routing, magazine reload, a finite slow-time special and checkpoint recovery,
  but adds combo progression, a duel and narrator-authored state replacement.
  Mafia (2002) shares a fixed story chapter with third-person combat and route
  gates, but its bounded terminal follows taxi work and a safe-location escape.
  Half-Life 2 shares authored combat routing and physical gate interactions in
  first person but has no player-controlled time-rate resource or delayed
  medicine layer.
- Important difference: the same early chapter couples meter-funded time-rate
  control, live delayed restorative settlement and undisclosed performance-
  responsive opposition with a physical transit dependency chain.
- Claim IDs: `MP1-003`–`MP1-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-229`, `ACT-341`, `ACT-407` | Max, Shootdodge, painkiller, weapon and fixture names are parameters |
| System Behaviour | `SYS-215`, `SYS-348`, `SYS-368`, `SYS-369`, `SYS-750`, `SYS-751` | damage, recovery rate, time scale and adaptation values are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-579` | eight items, ammunition values and exact ordered gates are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125` | icon art, screen position, colour and labels are presentation |
| Objective | `OBJ-026` | chapter and successor names are parameters |
| Time | `TIM-003` | frame rate, slow-time scale and load duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `237` (`GAME-0001`–`GAME-0237`).
- Exact genome matches: none.
- Tied near matches: `GAME-0222` — Call of Juarez: Gunslinger (`18 / 34 = 0.529412`).
- Supported combination subsets: `COMB-0236`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0222` — Call of Juarez: Gunslinger | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-229`, `SYS-215`, `SYS-348`, `SYS-368`, `SYS-369`, `CON-262`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Gunslinger adds combo scoring, experience and skill progression, a formal duel, narrator-authored state replacement and an episode objective. Max Payne instead binds combat to an operated fixture chain, live consumable use with delayed recovery under continuing damage, opposition that adapts to recent player effectiveness, finite-resource gates and a fixed transit successor. | Near, `0.529412` |

### Preserved research notes

- New genes: `ACT-407`, `SYS-750`, `SYS-751`, `CON-579`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`,
  `ACT-229`, `ACT-341`, `SYS-215`, `SYS-348`, `SYS-368`, `SYS-369`,
  `CON-262`, `CON-269`, `CON-282`, `CON-285`, `INF-073`, `INF-115`,
  `INF-119`, `INF-125`, `OBJ-026`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new
  genes`.
- Evidence and reasoning: generic movement, combat, equipment, slow-time,
  checkpoint, authored order and interface boundaries fit unchanged. New
  boundaries isolate a restorative committed without a cast, its overlapping
  delayed health transition, its legal stock/health gate and performance-driven
  enemy adjustment. No game-specific quest, character, item, vehicle or number
  enters a canonical label.

## Taxonomy impact

- Registry changes: four new Active genes with portable names and game-scoped
  examples; no existing definition, lifecycle or reviewed signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: non-blocking restorative use, delayed additive
  recovery and performance-responsive hostile adjustment are accepted; named
  chapter, character, medicine, special, train and numeric parameters remain
  local.

## Negative results

- `ACT-356` and `SYS-456` are rejected: Brawlhalla's protected dodge and cooldown
  boundary does not describe a vulnerable firearm dive funded by the same
  resource as free-standing slow time. Shootdodge remains the directional form
  of `ACT-229`/`SYS-368`, not a branded gene.
- `ACT-131` is rejected because its held item's effect resolves immediately;
  `ACT-200`, `SYS-319` and `CON-286` require an interruptible use channel. Max
  commits medicine without suspending combat and then settles recovery over time.
- `SYS-479` is rejected: Bullet Time does not place and resolve Dead Eye marks;
  the generic finite special-resource slowdown remains `SYS-368`.
- `SYS-515` is rejected: Fugitive reacts to player performance inside one mode,
  not one fixed selected opponent-difficulty value.
- `CON-177` is rejected: the medicine cap is a typed count, not a set of slots
  requiring disposal. `CON-579` records only legal use; eight is a parameter.
- Optional media interactions, graphic-novel review, secrets, exhaustive
  searching and whole-campaign narrative are outside the causal packet.
- No previous reviewed signature changes.

## Combination subset scan

- Every verified pre-unit combination will be tested as a proper subset of the
  25-gene signature after registration. `COMB-0236` is reserved for the strict
  slow-time/adaptive-combat/delayed-recovery chapter core and excludes ordinary
  equipment and presentation support.
- Comparison and subset scan date: 2026-09-03.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] The current legally sold Windows product, default
  Fugitive adaptation, Bullet Time, Shootdodge, pain/recovery and save semantics
  are fixed by `MP1-001`–`MP1-003` and `MP1-005`–`MP1-011`.
- [Observation | Corroborated | High] Platform 5 entry, officer/control/Line 2
  dependencies, train breach and Chapter 2 terminal are fixed by `MP1-004`,
  `MP1-009`, `MP1-010` and `MP1-012`.

## Нові гени

- [Observation/Confirmed | Direct | High] `ACT-407`, `SYS-750`, `SYS-751` and
  `CON-579` separate portable live-use recovery and adaptive opposition from
  painkiller, Fugitive, character and chapter parameters.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0236` joins direct firearm routing,
  finite special-rate control, delayed live recovery, adaptive opposition and
  an authored successor threshold.

## Зміни таксономії

- [Observation | Corroborated | High] No earlier definition, lifecycle,
  signature or maintainer decision changed.

## Нові питання

- Does another action game expose a restorative whose effect remains visibly
  pending while later damage is added without an interruptible use cast?
- Does a later Max Payne ruleset retain player-performance adaptation, or does
  it replace this original Fugitive response with fixed difficulty parameters?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0239` — Half-Life (1998).
- Optimisation criterion: preserve an original Windows authored combat route
  while removing player-controlled slow time and delayed medicine.
- Expected information gain: compare environmental interaction, suit resources,
  scripted hazards and one retained chapter transition against Max Payne's
  adaptive third-person gunfight loop.
- Backlog impact: continues `SEARCH_DEMAND_GAME_SELECTION_012` in order; Max
  Payne sequels and modules remain deferred.

## Чому саме вона

- [Hypothesis | Limited | Medium] The next original PC campaign should retain a
  fixed authored route and direct combat while shifting perspective, health
  economy, world-fixture dependencies and systemic hazards enough to test which
  Roscoe Street genes transfer.

## Family classification

- `FAM-009` Tactical forecast and counterplay.
- `FAM-010` Real-time system pressure.
- `FAM-014` World topology and perspective.
- `FAM-017` Ordered dependency sequencing.

## Plain-language interpretation

Roscoe Street Station is not merely a corridor of gunfights. The player spends
finite ammunition and one rechargeable slow-time resource while the default
mode quietly adjusts enemy performance. Medicine can be consumed without
stopping, but its marked health returns over several exposed seconds and new
damage still counts. Progress then depends on an authored transit chain: protect
the route long enough to reach the officer, power Line 2, drive the train through
the barrier and cross the one door that proves the chapter is over.

## Ukrainian localisation review

- `verified`: exact product/build/mode/chapter identifiers, entry and terminal,
  all reused gene meanings, sources and exclusions.
- `corrected`: every new Ukrainian game, gene, combination, presentation,
  salience and plain-language field is reviewed for complete causal parity and
  natural syntax in this unit; no pre-existing owner field requires correction.
- `retained-with-reason`: `Max Payne`, `Windows`, `Steam`, `12140`, `252034`,
  `v1.05`, `Fugitive`, `Bullet Time`, `Shootdodge`, `Roscoe Street Station`,
  `Platform 5`, `So Much for Being Subtle`, `Line 2`, `One Way or the Other`,
  `Live from the Crime Scene`, `Hard-Boiled`, `Dead on Arrival`, `New York
  Minute`, `The Last Challenge`, `Parental Lock`, `Max Payne 2` and `Max Payne
  3` are evidence-relevant official identifiers retained in Latin script.
- Routed candidate decision: inspect the generated audit after all fields are
  present; generic English vocabulary is not deferred to the batch audit.

## Structural metrics

- Protocol: `STRUCTURAL_METRICS_001`; exact measured values are recorded in the
  unit research-log entry.
- Active minutes: evidence and scope `45`; taxonomy, lower-ID and combination
  scans `35`; canonical analysis `40`; localisation and artwork `40`;
  validation, build and browser review `50`; total `210`.
- Files: `42` focused paths touched; `27` edited manually. Four new Active
  genes and twenty-one reused genes form the twenty-five-gene signature.
- Active-singleton share: `0.753590`; latest-nine new-gene rate: `4.777778`;
  single-support combination share: `0.923729`.
- Complete Python gate: `63` tests in `24.0 s`; production build: `26.9 s`
  before evidence recording and `5,286` pages / `5,284` localised HTML pages
  after recording. No payload threshold triggered.
- Manual derived-count edits: `scripts/test_taxonomy_health.py`,
  `web/tests/corpus.test.ts`, `web/tests/legacy-import.test.ts`,
  `web/tests/localisation-audit.test.ts` and
  `web/tests/static-corpus.test.ts`.

## References

- `P1`–`P5`, `S1`–`S3` and `V1` as listed in Basic data.
