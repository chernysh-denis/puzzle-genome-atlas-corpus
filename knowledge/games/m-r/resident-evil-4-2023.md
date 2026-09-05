---
game_id: GAME-0249
slug: resident-evil-4-2023
game_title: Resident Evil 4 (2023 remake)
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0247
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-202
    - ACT-235
    - ACT-341
    - ACT-424
    - ACT-425
    - ACT-426
  system:
    - SYS-208
    - SYS-215
    - SYS-300
    - SYS-369
    - SYS-373
    - SYS-755
    - SYS-776
    - SYS-777
    - SYS-778
    - SYS-779
    - SYS-780
  constraint:
    - CON-282
    - CON-285
    - CON-335
    - CON-357
    - CON-394
    - CON-579
    - CON-594
    - CON-595
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-132
    - INF-302
    - INF-303
    - INF-304
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Resident Evil 4 (2023 remake)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `2050650`, base-game package `794618`, public branch Build ID `22377325`,
  built 2026-03-17 and published 2026-03-31, checked 2026-09-05. The build
  identifier and dates are secondary distribution observations. Only Main
  Story → New Game → `Standard` → Chapter 1 is admitted. This is the 2023
  remake, not Resident Evil 4 (2005), the 2014 PC release of that original,
  Gold Edition or another package.
- Entry: use a clean profile with no completed-story unlocks or retrieved bonus
  storage items. Select New Game and Standard, leave aim assist and other
  gameplay options at their normal Standard defaults, then begin at first
  retained control on the wooded approach before the hunter's lodge. Do not
  import New Game Plus equipment, a challenge unlock, paid weapon, charm,
  attaché case or Expanded Treasure Map.
- Primary decision loop: read the current objective and explored map, local
  threats, reticle focus, health, active weapon, loaded and reserve ammunition,
  knife durability, carried item footprints, free case cells and known recipe
  inputs; walk, run or crouch; interact with doors, keys, containers, breakable
  objects and route devices; reposition or rotate an item in the attaché case;
  select, aim, focus, fire and reload a weapon; time one eligible knife parry;
  use a prompted close follow-up after stagger; use one restorative only after
  health loss; craft one currently legal recipe from acquired inputs; survive
  the village pressure event and continue through the authored Chapter 1 gates.
- Positive terminal: complete the final underground authored interaction after
  the Lakeside Settlement, inspect explicit Chapter 1 completion, accept the
  ordinary save opportunity into a fresh slot, continue, and retain first
  controllable Chapter 2 state. Reload that new save once and confirm Chapter
  2, Standard and the successor objective before stopping.
- Negative terminal: health reaching zero ends the current attempt. Select
  Continue from the game-over surface so the most recent autosaved checkpoint
  replaces transient position, health, ammunition, durability, inventory,
  hostile and objective state. A failed reload or a save that returns before
  Chapter 2 rejects the proposed positive terminal.
- Included: one fresh base-game Standard Chapter 1; direct third-person
  traversal and crouch; local sight, sound and hostile awareness; authored
  keys, doors, locks, tripwires, containers, push and gear interactions;
  firearm aim, focus, ammunition and reload; knife attack, reactive parry,
  durability and break boundary; temporary stagger and contextual melee;
  eligible stealth neutralisation; damage and finite immediate healing;
  pickups, breakable containers, rectangular attaché-case occupancy and item
  rotation; one legal ammo or herb recipe; map and objective state; village
  survival-threshold settlement; autosave retry; chapter completion, save and
  retained successor control.
- Excluded: Merchant interaction, weapon repair, upgrades, purchases, sales and
  trades because the first ordinary Merchant belongs to successor Chapter 2;
  Ashley commands and escort state; later chapters, bosses, requests and the
  rest of the campaign; Professional, Hardcore, Assisted, New Game Plus,
  results/rank optimisation, speedrunning and challenge routing; Separate Ways,
  The Mercenaries, Shooting Range, VR Mode, Photo Mode and online statistics;
  Gold/Deluxe content, paid tickets, bonus weapons, costumes, charms, alternate
  cases, Expanded Treasure Map, soundtrack swaps and every other DLC; mods,
  trainers, cheats, glitches, console editions, mobile/macOS ports and the 2005
  game.
- Reproducible parameterisation: preserve application, base package, public
  build, clean-profile state, English, keyboard/mouse or default Type A
  controller mapping, New Game, Standard and Chapter 1. Use the first
  typewriter after the lodge for a fresh manual save. In Chapter 1, break one
  ordinary supply container, focus and fire at least one shot, reload, produce
  and accept one stagger-melee prompt, execute one legal knife parry, rotate and
  reposition one acquired rectangular item, use one restorative after damage
  and craft one first legal recipe whose acquired inputs and output are
  recorded. Survive the village encounter without requiring every hostile to
  be defeated, traverse the Farm and Lakeside Settlement gates, complete the
  final underground interaction, save at the chapter boundary, continue and
  verify the retained Chapter 2 save. Exact combat route, optional weapon,
  hostile defeats, item drops, inventory arrangement, recipe, health,
  ammunition, knife durability, completion time and rank are run parameters.
- Potential scoped modules: one other difficulty, one later chapter, one
  Merchant economy packet, one escort segment, Separate Ways, The Mercenaries,
  Shooting Range, VR Mode, a console/mobile port or the 2005 original each
  requires a separate scope.
- Direct-play status: not conducted. Valve and Capcom current product, package,
  release, support and official web-manual material establish lawful
  availability, edition separation, controls, combat, inventory, crafting,
  health, map, objective and save rules. Static written Chapter 1 evidence
  constrains route order, the village pressure settlement, first typewriters,
  final interaction and chapter boundary. This is evidence-backed rules
  reconstruction, not a claimed captured playthrough or entitlement. No video
  or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RE4R-001` | The admitted product is the 2023 Windows Steam remake, app `2050650`, base package `794618`, not the original, Gold Edition or a DLC union | Confirmed | Direct | High | P1–P4 |
| `RE4R-002` | Steam public Build `22377325` is the current observed Windows distribution state | Observation | Corroborated | High | P1, S1 |
| `RE4R-003` | A fresh Main Story New Game can fix Standard as the ordinary difficulty and begins before the hunter's lodge | Confirmed | Corroborated | High | P5, S2 |
| `RE4R-004` | Readied firearm aim, visible reticle focus, finite ammunition and reload form a live accuracy-and-stagger choice | Confirmed | Direct | High | P5 |
| `RE4R-005` | A usable knife can attack, escape a grapple or parry; accepted parries prevent damage, reduce durability and precise timing can greatly stagger the attacker | Confirmed | Direct | High | P5 |
| `RE4R-006` | Eligible stagger exposes a close melee follow-up, while crouched approach can support a quiet knife neutralisation | Confirmed | Direct | High | P5 |
| `RE4R-007` | Carried items occupy an attaché-case grid where they can be moved and rotated; legal known recipes consume compatible acquired inputs into carried output | Confirmed | Direct | High | P5 |
| `RE4R-008` | Health reaching zero is game over; finite recovery items require missing health and restore visible personal state | Confirmed | Direct | High | P5 |
| `RE4R-009` | Checkpoints autosave automatically, typewriters create manual saves and Continue loads the most recent saved state | Confirmed | Direct | High | P5 |
| `RE4R-010` | Chapter 1 orders the lodge, village, Farm and Lakeside Settlement route before a final underground interaction completes the chapter | Observation | Corroborated | High | S2 |
| `RE4R-011` | The village pressure event ends through an authored bell withdrawal after a survival interval rather than requiring the player to defeat every hostile | Observation | Corroborated | High | S2 |
| `RE4R-012` | Chapter completion, a fresh save and verified first Chapter 2 control form a reproducible retained terminal without importing the Merchant economy | Strong Pattern | Corroborated | High | P5, S2, S3 |
| `RE4R-013` | The bounded identity is spatial resource packing and reactive survival combat carried through an authored pressure chapter into retained successor control | Strong Pattern | Corroborated | High | `RE4R-004`–`RE4R-012` |

## Basic data

- Release / origin: Capcom; released for Windows Steam on 2023-03-23; a
  reimagining of the 2005 game rather than that original build.
- Platform or physical form: lawfully available English Windows Steam client,
  base-game package `794618`; one offline single-player Main Story chapter.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=2050650&cc=ua&l=english),
    for current Windows availability, release date, application identity and
    distinct base, Gold and trilogy purchase options.
  - `P2` — [Valve base-package data](https://store.steampowered.com/api/packagedetails?packageids=794618&cc=ua&l=english),
    for the selected package and its one Resident Evil 4 application.
  - `P3` — [Capcom release announcement](https://news.capcomusa.com/2023/03/24/resident-evil-4-is-out-now/),
    for the PC Steam release, explicit remake-of-2005 identity, knife parry,
    escape, grounded knife attack, aimed stagger-follow-up and attaché-case
    resource framing.
  - `P4` — [Capcom Resident Evil 4 support section](https://www.capcom-support.com/hc/en-us/sections/10014121833756-Resident-Evil-4-2023),
    for the explicit 2023 support identity and official online-manual route.
  - `P5` — [official Capcom Resident Evil 4 web-manual data](https://game.capcom.com/manual/re4/locale/data/en.json),
    for Main Story/New Game, Standard difficulty, controls, aim focus, shooting,
    reload, knife combat and parry, stealth and stagger follow-ups, health and
    game over, attaché-case organisation, recipes, map/objectives,
    autosave/typewriter/Continue semantics and mode separation. The human-
    readable entry is the [official web manual](https://game.capcom.com/manual/re4/en/steam/top).
  - `P6` — [Capcom manual support notice](https://www.capcom-support.com/hc/en-us/articles/25949677662996-Online-Manual),
    updated 2026-07-20, for the maintained official manual destination.
- Corroborating textual sources, accessed 2026-09-05:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/2050650/depots/),
    for Windows depots and public Build `22377325`, built 2026-03-17 and
    published 2026-03-31. SteamDB is a secondary distribution mirror.
  - `S2` — [PowerPyx Chapter 1 walkthrough](https://www.powerpyx.com/resident-evil-4-remake-chapter-1-walkthrough/),
    for the written objective order, first typewriter, village survival-and-
    bell settlement, Farm route devices, Lakeside Settlement and final
    interaction that completes Chapter 1.
  - `S3` — [Neoseeker Chapter 1 guide](https://www.neoseeker.com/resident-evil-4-2023/walkthrough/Chapter_1),
    for written corroboration that the bell ends the remaining assault and the
    chapter result permits saving before Chapter 2. The page was search-indexed
    but blocked direct automated retrieval; it is supporting rather than sole
    evidence.
- Claim IDs: `RE4R-001`–`RE4R-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly traverse the authored route; `ACT-202`: crouch
  or stand to alter exposure; `ACT-341`: operate a door, key, container,
  tripwire, push, gear, pickup or chapter-ending object; `ACT-164`: select a
  carried weapon or grenade shortcut; `ACT-161`: aim and commit a knife or
  firearm attack; `ACT-183`: reload a magazine-fed weapon; `ACT-131`: consume
  one immediate restorative after health loss; `ACT-123`: craft one known
  legal carried recipe; `ACT-235`: quietly neutralise one unaware reachable
  hostile when the route exposes that state.
- New `ACT-424`: reposition or rotate a retained item inside the attaché-case
  grid. New `ACT-425`: commit one timed knife parry against an eligible incoming
  attack. New `ACT-426`: perform the prompted close attack while an eligible
  staggered hostile remains reachable.
- Character, weapon, item, recipe, area and objective names are parameters.
  Merchant repair, upgrades, purchases and later escort commands are outside
  the action set. Claims: `RE4R-003`–`RE4R-010`.

### System Behaviour Genes

- Existing `SYS-208`: firearm attacks resolve through aim, obstruction and body
  hit; `SYS-215`: direct attack and hostile response resolve in live time;
  `SYS-300`: compatible carried herb components produce their declared combined
  item; `SYS-373`: local sight, sound and harmful action can escalate hostiles
  into search or combat; `SYS-755`: eligible damage breaks an authored object
  and resolves its collision or contents; `SYS-369`: death and Continue replace
  the failed transient state with the most recent authored checkpoint.
- New `SYS-776`: maintained ready aim focuses the reticle and improves the next
  shot's stagger or critical relation. New `SYS-777`: accepted knife-parry
  timing prevents ordinary damage, spends durability and can strongly stagger
  on a precise window. New `SYS-778`: an eligible hit or precise parry creates
  a temporary contextual close-follow-up state. New `SYS-779`: the village
  pressure encounter settles after its authored survival threshold and
  withdraws remaining threats without total clearance. New `SYS-780`: the
  final interaction closes Chapter 1 into saved successor control.
- Resolution order: accept movement, posture, interaction, inventory, recipe,
  weapon, aim, reload, restorative, parry or contextual input; validate
  capacity, compatibility, health, durability, reach and timing; update
  inventory and personal resources; resolve local perception and combat;
  replace death from checkpoint; settle the pressure encounter; advance route
  objectives; close, save and reload the chapter successor. Claims:
  `RE4R-004`–`RE4R-012`.

### Constraint Genes

- Existing `CON-282`: the chapter's lodge, route devices and final interaction
  obey authored dependencies; `CON-285`: shooting and reload require compatible
  active weapon and ammunition state; `CON-335`: a stealth neutralisation
  requires an unaware reachable eligible actor; `CON-357`: a craft requires the
  known recipe and all compatible material quantities; `CON-394`: a carried
  item must fit unoccupied rectangular cells or compatible capacity;
  `CON-579`: an immediate restorative requires missing health and finite stock.
- New `CON-594`: reactive parry requires a usable equipped knife, an eligible
  incoming attack and accepted timing. New `CON-595`: the prompted close
  follow-up requires a living staggered hostile still within reach.
- Scarce strategic resources: health, ammunition, knife durability, healing
  stock, recipe inputs, case cells, safe distance and authored checkpoint
  progress. Exact dimensions, quantities, damage, timing and drops are
  parameters. Claims: `RE4R-004`–`RE4R-012`.

### Information Genes

- Existing `INF-073`: active weapon, loaded/reserve ammunition and carried
  items are visible; `INF-075`: health and knife durability are visible;
  `INF-115`: ordinary sight, sound and spatial effects expose local threats;
  `INF-125`: explored map and current authored objective are inspectable;
  `INF-128`: reachable pickups, carried identity and capacity compatibility are
  visible; `INF-132`: known recipe inputs and output are inspectable.
- New `INF-302`: the attaché case exposes item footprints, orientation,
  occupied cells and free cells. New `INF-303`: the reticle distinguishes
  default and focused aim state. New `INF-304`: local feedback exposes the
  temporary reachable close-follow-up prompt on a staggered hostile.
- Exact icons, colours, grid dimensions, labels, item art and screen positions
  are presentation parameters. Claims: `RE4R-004`–`RE4R-012`.

### Objective Genes

- New `OBJ-155`: satisfy one authored survival-action chapter's mandatory
  route, accept explicit completion and saving, and retain ordinary control in
  its immediate successor chapter.
- The first typewriter, village bell, Farm gate and an autosave are
  intermediate. Death is the negative terminal; verified saved Chapter 2
  control is the positive terminal. Claims: `RE4R-009`–`RE4R-012`.

### Time Genes

- Existing `TIM-003`: movement, enemy perception and attack, aim focus, reload,
  parry windows, stagger opportunities, hostile pressure and damage progress in
  continuous live time. Paused inventory, map, save and chapter-result surfaces
  do not introduce another decision clock. Claims: `RE4R-004`–`RE4R-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean base-game profile is at Main Story | Select New Game and Standard | First control begins on the wooded Chapter 1 approach without retained bonus equipment | reproducible entry and edition boundary | `RE4R-001`–`RE4R-003` |
| One acquired rectangular item is retained and free case cells exist | Select, move and rotate it to a different legal footprint | The case accepts only an unoccupied fit and preserves the new orientation | spatial carried-capacity decision | `RE4R-007` |
| A firearm is readied and no interrupting action occurs | Hold aim until the reticle focuses, then fire at one reachable hostile | The accepted shot uses the focused accuracy and increased stagger/critical relation while ammunition decreases | delay-for-shot-quality trade-off | `RE4R-004` |
| The active magazine is partly empty and compatible reserve remains | Reload | Fire readiness pauses and reserve ammunition transfers into the magazine | ammunition is operational time state | `RE4R-004` |
| A living hostile begins an eligible incoming attack and knife durability remains | Commit the parry in the accepted contact window | Ordinary damage is prevented, knife durability decreases and precise timing can apply a stronger stagger | durability-backed reactive defence | `RE4R-005` |
| A living hostile is staggered and the contextual prompt is reachable | Commit the close follow-up before recovery | A close melee attack resolves against the target and eligible nearby actors; the opportunity then closes or changes | temporary stagger conversion | `RE4R-006` |
| Health is below maximum and a compatible restorative is carried | Use the restorative | One finite item is consumed and health increases only to its cap | bounded recovery trade-off | `RE4R-008` |
| A known recipe and all compatible inputs are present | Commit one ammo craft or herb combination and record inputs/output | Inputs are consumed and the declared carried output is created if case capacity accepts it | resource conversion inside inventory pressure | `RE4R-007` |
| The village pressure encounter is active and the player remains alive | Move, evade, use buildings or fight until the authored threshold settles | The bell event withdraws remaining attackers and reopens onward traversal without requiring total clearance | bounded survival encounter | `RE4R-011` |
| The Farm route gear and its authored destination are reachable | Obtain and apply the route item, then operate the mechanism | The next route gate opens and Chapter 1 objective progression continues | ordered authored interaction | `RE4R-010` |
| Health reaches zero before chapter settlement | Select Continue from game over | The most recent autosaved checkpoint replaces transient health, position, resources, hostiles and objective state | reproducible negative terminal | `RE4R-008`, `RE4R-009` |
| The final underground Chapter 1 interaction is reachable | Interact, inspect completion, save in a fresh slot and continue | Chapter 1 closes and first Chapter 2 control becomes active | authored positive terminal | `RE4R-010`, `RE4R-012` |
| First Chapter 2 control has been saved | Load the new slot once | Chapter 2, Standard and successor objective return as retained state | terminal retention verification | `RE4R-009`, `RE4R-012` |

## Strategic and experiential structure

- Planning horizon: preserve enough health, ammunition, usable knife
  durability and case space for the next authored gate while deciding which
  pickups to carry, how to place them and when a recipe reduces or increases
  spatial pressure.
- Local tactics: hold aim for a better shot or fire immediately; create and
  exploit a stagger; spend knife durability on a safe parry or keep distance;
  evade, route through buildings or fight during the village survival phase;
  spend a restorative now or preserve it for later.
- Medium-term structure: the lodge teaches authored interaction, the first
  typewriter creates a manual baseline, the village tests live survival, the
  Farm combines item and mechanism dependencies, and the Lakeside Settlement
  carries remaining resources into the final chapter interaction and save.
- Reversible versus irreversible: movement, aim, posture and legal case layout
  can be revised; spent ammunition, healing, recipe inputs and knife durability
  constrain the remaining route; a broken tool or discarded item removes an
  option; Continue replaces a failed branch; accepted chapter completion
  advances the save.
- Failure attribution: health, ammunition, knife durability, reticle focus,
  stagger prompt, item footprint, free cells, recipe dependencies, current
  objective, checkpoint and chapter/save labels distinguish execution,
  resource, capacity, route and retention failures.
- Player trust: focused aim and stagger feedback must precede their consequences;
  parry must spend the disclosed durability; case placements must obey visible
  cells; the village must settle without false total-clearance requirements;
  Chapter 2 must survive reload. Claims: `RE4R-004`–`RE4R-013`.

## Replay and variation

- What changes between attempts: movement line, time spent in the village,
  enemies fought or evaded, shot timing, parry success, stagger follow-ups,
  damage, health use, ammunition, knife durability, pickups, random container
  contents, case layout, crafted recipe, checkpoint state, completion time and
  displayed rank.
- Randomness or procedural generation: the chapter geometry, objectives and
  mandatory gates are authored. Some container contents and live hostile
  positions or responses can vary within that route.
- Multiple viable strategies: the village permits fighting, movement and
  building use until settlement; optional weapons and pickups can change the
  inventory plan. This packet nevertheless fixes Standard, the required
  mechanic samples and the retained Chapter 2 terminal.
- Typical replay motive: improve route efficiency, resource conservation or
  chapter result. Rank optimisation, challenge unlocks, speedrunning and later
  campaign progression remain outside this unit.
- Claims: `RE4R-003`–`RE4R-012`.

## Adjacent systems and history

- Direct product corridor: Capcom explicitly presents this as a 2023 remake of
  the 2005 game. The selected Steam base package remains separate from Gold,
  Separate Ways, The Mercenaries and paid item DLC; no original-game mechanic
  is imported without remake evidence.
- Similar lower-ID games: DOOM (2016) shares a bounded authored route, live
  aimed combat, temporary contextual attack opportunity, breakable supply
  objects and retained successor control; Max Payne (2001) shares chapter
  progression, firearm scarcity, live damage and finite healing; Path of Exile
  2 shares rectangular inventory placement and recipe decisions; NARAKA:
  BLADEPOINT shares weapon durability and timed counterplay; Fallout 4 shares
  fresh-story traversal, pickups, crafting resources and checkpoints.
- Important differences: Resident Evil 4 couples focused aim and temporary
  melee openings to a knife parry that spends durability, makes exact
  rectangular case fit a continuing survival resource, settles one pressure
  event without total clearance and requires a saved chapter-to-chapter
  terminal. Claims: `RE4R-004`–`RE4R-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-123`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-235`, `ACT-341`, `ACT-424`, `ACT-425`, `ACT-426` | item, recipe, weapon, route and timing values |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-300`, `SYS-369`, `SYS-373`, `SYS-755`, `SYS-776`, `SYS-777`, `SYS-778`, `SYS-779`, `SYS-780` | focus, damage, durability, stagger, pressure and save values |
| Constraint | `CON-282`, `CON-285`, `CON-335`, `CON-357`, `CON-394`, `CON-579`, `CON-594`, `CON-595` | inputs, case cells, health, weapon, attack and reach |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-132`, `INF-302`, `INF-303`, `INF-304` | icons, labels, grid, reticle, prompt and objective |
| Objective | `OBJ-155` | chapter, final interaction, save, successor and retention |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `248` (`GAME-0001`–`GAME-0248`).
- Exact genome matches: none.
- Tied near matches: `GAME-0247` — Dishonored (2012) (`17 / 54 = 0.314815`).
- Supported combination subsets: `COMB-0247`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0247` — Dishonored (2012) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-202`, `ACT-235`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-125`, `TIM-003` | Both route one directly controlled body through live stealth/combat, authored interactions and recoverable checkpoints. Dishonored adds mana-backed previewed relocation and a learned non-lethal target disposition before conduct settlement; Resident Evil 4 adds rectangular carried space, focused firearm stagger, durability-spending reactive parry, a non-clearance pressure event and a saved chapter transition. | Near, `0.314815` |

### Preserved research notes

- New genes: `ACT-424`, `ACT-425`, `ACT-426`, `SYS-776`, `SYS-777`,
  `SYS-778`, `SYS-779`, `SYS-780`, `CON-594`, `CON-595`, `INF-302`,
  `INF-303`, `INF-304` and `OBJ-155`.
- Reused genes: `ACT-008`, `ACT-123`, `ACT-131`, `ACT-161`, `ACT-164`,
  `ACT-183`, `ACT-202`, `ACT-235`, `ACT-341`, `SYS-208`, `SYS-215`,
  `SYS-300`, `SYS-369`, `SYS-373`, `SYS-755`, `CON-282`, `CON-285`,
  `CON-335`, `CON-357`, `CON-394`, `CON-579`, `INF-073`, `INF-075`,
  `INF-115`, `INF-125`, `INF-128`, `INF-132` and `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing movement, attack, reload, healing, crafting,
  authored interaction, stealth, perception, rectangular capacity, checkpoint
  and route boundaries fit without revision. New labels isolate case
  manipulation, focused aim, durability-backed reactive parry, non-guaranteed
  stagger follow-up, non-clearance pressure settlement and a generic retained
  chapter handoff. Character, weapon, item, recipe, location, chapter and
  numeric values remain parameters.
- Lower-ID scan: reject `ACT-349` and `SYS-625`, because the parry is an
  undirected reactive timing input rather than an aimed directional guard;
  reject `ACT-383`, because no sustained guard state is admitted; reject
  `ACT-419`, `SYS-770`, `CON-589` and `INF-295`, because the prompted Resident
  Evil 4 melee is not a guaranteed defeating finisher or recovery-drop
  exchange; reject `SYS-656`, because the selected chapter admits durability
  loss and break but excludes the later repair loop; reject `SYS-611`, because
  no required boss set or chapter guardian defines this transition; reject
  `SYS-622`, because a closed cooperative safe room is not the terminal.

## Taxonomy impact

- Registry changes: fourteen new Active genes use portable mechanical language
  and game-scoped examples; no existing definition, lifecycle or reviewed
  signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Resident Evil 4,
  Leon, Chapter 1, Standard, attaché case, Combat Knife, Perfect Parry,
  Village, Farm, Lakeside Settlement, typewriter and Merchant remain parameters
  or literal interface/product terms.

## Negative results

- No direct-play, local-entitlement, screenshot, video or audio claim.
- No original-game, Gold/Deluxe, DLC, Merchant, escort, later-chapter, rank,
  challenge, speedrun, platform or mode union.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the forty-two-gene signature. None fit completely. `COMB-0247` is
  added as the strict inventory-grid, focused-shot, reactive-parry,
  stagger-follow-up, pressure-settlement and retained-chapter core; it omits
  general traversal, health, firearm resolution, checkpoints and map state.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current base-package Windows availability,
  remake identity and official Main Story mechanics are fixed in `RE4R-001`–
  `RE4R-009`.
- [Observation | Corroborated | High] Chapter 1's route, village survival
  settlement and chapter boundary are bounded in `RE4R-010`–`RE4R-012`.

## New genes

- [Confirmed | Corroborated | High] `ACT-424`–`ACT-426`, `SYS-776`–`SYS-780`,
  `CON-594`, `CON-595`, `INF-302`–`INF-304` and `OBJ-155` isolate transferable
  carried-grid, focused-shot, reactive-defence, stagger, pressure-settlement
  and retained-chapter boundaries.

## New combinations

- [Observation | Corroborated | High] `COMB-0247` captures a resource-packed
  authored pressure chapter where focused attacks and durability-backed parry
  decisions survive into retained successor control.

## Taxonomy changes

- [Observation | Corroborated | High] None; no prior signature, definition or
  lifecycle state changes.

## New questions

- Does Tomb Raider's bounded early story segment preserve authored
  survival-action routing while replacing rectangular inventory and reactive
  knife timing with traversal tools, environmental hazards and salvage?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0250` — Tomb Raider (2013, current Game
  of the Year package).
- Optimisation criterion: retain one bounded authored action route and saved
  successor checkpoint while changing its movement and resource grammar.
- Expected information gain: distinguish climb/traversal dependencies and
  environmental interactions from carried-grid and knife-parry pressure.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Tomb Raider keeps a checkpointed authored
  survival-action segment near-constant while replacing Resident Evil 4's
  spatial case, crafting and parry loop with explicit traversal-tool and
  environmental sequencing.
