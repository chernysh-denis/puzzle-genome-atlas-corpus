---
game_id: GAME-0332
slug: heroes-of-might-and-magic-iii-complete
game_title: "Heroes of Might and Magic III: Complete"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-140
    - ACT-189
    - ACT-191
    - ACT-281
    - ACT-345
    - ACT-347
    - ACT-483
    - ACT-484
  system:
    - SYS-299
    - SYS-305
    - SYS-614
    - SYS-616
    - SYS-942
    - SYS-943
    - SYS-944
    - SYS-945
    - SYS-946
  constraint:
    - CON-273
    - CON-270
    - CON-509
    - CON-510
    - CON-514
    - CON-652
    - CON-653
  information:
    - INF-244
    - INF-361
  objective:
    - OBJ-195
  time:
    - TIM-001
    - TIM-018
---

# Game: Heroes of Might and Magic III: Complete

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Christian,
Caryatid, Plinth, Mirham, Trailia, Terraneus, Castle, Dungeon and named
creatures are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: current official English GOG Windows **Heroes of Might
  and Magic III: Complete**, unmodded and offline, using only the original
  *The Restoration of Erathia* campaign. Exact installed GOG build, wrapper,
  operating-system revision and account entitlement were not observed.
- Structured analysis target: licensed GOG Windows Complete product; see
  `GAME-0332` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: `Long Live the Queen` campaign, first scenario `Homecoming`, fixed
  Easy difficulty, `14 Pikemen` starting bonus, from the first ordinary
  Adventure Map decision through the victory settlement caused by capturing
  the underground town Terraneus.
- Entry: choose `Homecoming`, commit the `14 Pikemen` bonus and begin; the first
  retained decision frame has Christian beside the owned Castle town Caryatid
  in the southeast of the surface map.
- Primary decision loop: inspect date, resources, hero movement, fog, army and
  town state; assign reachable hero routes; claim loose resources, mines and
  towns; construct at most one legal structure per owned town and day; recruit,
  merge, split or transfer same-type creature troops among seven-slot armies
  and garrisons; End Turn to settle rivals, daily income and refreshes, with
  first-day-of-week dwelling growth; in contact, use speed-ordered troop turns
  to move, attack, wait or defend on a hex battlefield; preserve enough army
  strength to descend underground and capture Terraneus.
- Positive terminal: the player's hero defeats any Terraneus defenders and
  enters the town, changing it to player territory; the scenario records the
  capture victory and identifies the four strongest eligible heroes for the
  next scenario. The next scenario itself does not begin.
- Failure terminal: the player simultaneously has no owned town and no hero.
- Included: the fixed surface and subterranean maps; Christian and recruited
  heroes; movement points, routes, terrain costs and fog; loose resources,
  controlled mines and daily income; owned towns, prerequisites, resource
  costs and one structure per town per day; creature dwellings and weekly
  growth; purchased recruitment; seven same-type troop slots; split, merge and
  garrison transfer; battle entry, hex movement, melee/ranged attacks, wait,
  defend, first surviving retaliation, stack-count damage and casualties;
  battle experience, level advancement and one of two offered secondary-skill
  improvements; town capture; Terraneus objective, level-six cap and four-hero
  successor selection.
- Reproducible parameterisation: retain fixed Easy difficulty and choose
  `14 Pikemen`; use any legal surface route, town-building order, recruited
  heroes and battle tactics that preserve at least one hero and town until a
  hero captures Terraneus. Exact random damage, morale, luck, secondary-skill
  offers, AI routes, optional fights, casualties and completion day are
  bounded parameters. Only mechanics encountered or causally available on the
  successful route enter the genome.
- Excluded: the two later `Long Live the Queen` scenarios; every other
  Restoration of Erathia campaign; *Armageddon's Blade* and *The Shadow of
  Death* campaigns or additions; random maps; single scenarios; multiplayer;
  map editor; unofficial HD Mod, Horn of the Abyss, VCMI, cheats and fan maps;
  alternate starting bonuses; exhaustive surface clearance; Grail excavation;
  spell-system, artifact-set and war-machine catalogues not required by this
  route; exact AI, probability, damage-table or GOG patch-history claims; HD
  Edition, macOS, Linux, console, remake and later-series rules.
- Potential scoped modules: one later campaign scenario, one spell-centred
  battle packet, one random-map packet, one siege-specialist packet and each
  expansion campaign require independent version, entry, loop, evidence and
  terminal boundaries.
- Direct-play status: not conducted. No licensed install, executable, save,
  screenshot, video, audio or input trace was used. GOG establishes the current
  product identity; the original New World Computing manual establishes the
  enduring strategic, town and combat rules; two independent scenario records
  establish `Homecoming` entry and terminal. This is source-bounded rules
  reconstruction, not a claimed playthrough or installed-build parity test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `H3C-001` | The packet is the current unmodded GOG Windows Complete product, while only original Restoration of Erathia content is admitted | Confirmed | Direct | High | P1 |
| `H3C-002` | On each strategic day players take sequential open turns; after all turns, controlled mines and towns add resources and a new day begins | Confirmed | Direct | High | P2, P3 |
| `H3C-003` | A hero follows a reachable route under a replenishing movement allowance affected by terrain and current army state | Confirmed | Direct | High | P2, P4 |
| `H3C-004` | Reaching loose resources grants them once, while capturing mines or towns transfers persistent economic or territorial benefit | Confirmed | Direct | High | P2, P5 |
| `H3C-005` | An owned town permits one prerequisite-valid, resource-paid structure per day and immediately applies the completed building's benefits | Confirmed | Direct | High | P2, P6 |
| `H3C-006` | Creature dwellings add recruit stock on the first day of each week and recruitment spends resources into a garrison or hero army | Confirmed | Direct | High | P2, P3, P7 |
| `H3C-007` | A hero or garrison holds at most seven troops, each troop contains one creature type, and same-type troops can be split, merged or transferred | Confirmed | Direct | High | P2, P8, P9 |
| `H3C-008` | Contact transfers armies to a hex battlefield where one action per troop per round is ordered by speed and can be move, attack, wait or defend | Confirmed | Direct | High | P2, P10, P11 |
| `H3C-009` | A surviving defender normally retaliates against the first melee attacker in a round; stack count and creature statistics determine casualties | Confirmed | Direct | High | P2, P12 |
| `H3C-010` | Battle victory awards hero experience; thresholds advance one primary skill and present two secondary-skill improvements under an eight-skill capacity | Confirmed | Direct | High | P2, P13 |
| `H3C-011` | Homecoming fixes Easy difficulty, starts with Christian/Caryatid, wins on Terraneus capture, loses without towns and heroes, caps heroes at level six and carries the four strongest onward | Confirmed | Corroborated | High | S1, S2 |
| `H3C-012` | The repository trace reaches the Terraneus settlement without importing later scenarios, expansions, mods or optional system catalogues | Observation | Direct | High | P1–P13, S1–S3, V1 |

## Basic data

- Release / origin: developed by New World Computing and originally published
  by The 3DO Company in 1999; the scoped current package is GOG's maintained
  DRM-free Complete Windows product.
- Platform or physical form: licensed single-player Windows GOG product;
  alternating strategic-day turns open separate discrete tactical battles.
- Puzzle family: tactical forecast and counterplay; agent routing and
  coordination; resource transformation and logistics; ordered dependency
  sequencing; knowledge and evidence progression.
- Product and primary rules sources, accessed 2026-09-21:
  - **[P1]** [official GOG product page](https://www.gog.com/en/game/heroes_of_might_and_magic_3_complete_edition),
    for current Complete identity, Windows availability, offline/DRM-free
    operation and inclusion of the base game plus both expansions.
  - **[P2]** [official original New World Computing player manual preserved by Steam](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/297000/manuals/BONUS_Heroes_of_Might_and_Magic_III_HDEdition_OldManual1999_EN.pdf?t=1699009789),
    for campaign, Adventure Map, hero, troop, town, combat and time rules.
  - **[P3]** [manual page 13 transcription](https://heroes.wikioasis.org/wiki/Restoration_of_Erathia_Manual_Page_13),
    for sequential daily turns, daily resource income and weekly creature
    production.
  - **[P4]** [manual movement reference](https://heroes.thelazy.net/index.php/Movement),
    for daily movement-point refresh, terrain/direction costs and exhaustion.
  - **[P5]** [manual page 17 transcription](https://heroes.thelazy.net/index.php/Restoration_of_Erathia_Manual_Page_17),
    for loose-resource pickup, mine capture, daily production and town capture.
  - **[P6]** [manual page 50 transcription](https://heroes.thelazy.net/index.php/Restoration_of_Erathia_Manual_Page_50),
    for structure prerequisites, resource price, immediate effect and one
    structure per town per day.
  - **[P7]** [manual page 52 transcription](https://heroes.wikioasis.org/wiki/Restoration_of_Erathia_Manual_Page_52),
    for weekly dwelling growth and priced recruitment into the town garrison.
  - **[P8]** [manual page 28 transcription](https://homm.fandom.com/wiki/Restoration_of_Erathia_Manual_Page_28),
    for seven hero-army slots, troop counts and battlefield slot position.
  - **[P9]** [manual page 29 transcription](https://heroes.wikioasis.org/wiki/Restoration_of_Erathia_Manual_Page_29),
    for dismissal, upgrade, same-type merge, split and slot movement.
  - **[P10]** [manual page 40 transcription](https://heroes.wikioasis.org/wiki/Restoration_of_Erathia_Manual_Page_40),
    for battle transfer, seven single-type troops, speed order, one action per
    round, legal action classes, victory and town conquest.
  - **[P11]** [manual page 41 transcription](https://heroes.thelazy.net/index.php/Restoration_of_Erathia_Manual_Page_41),
    for battlefield hexes, initial formation and troop-slot placement.
  - **[P12]** [manual page 43 transcription](https://heroes.thelazy.net/index.php/Restoration_of_Erathia_Manual_Page_43),
    for wait, defend, first surviving counterattack, stack-scaled damage and
    carried intra-battle creature health.
  - **[P13]** [manual page 33 transcription](https://heroes.thelazy.net/index.php/Restoration_of_Erathia_Manual_Page_33),
    for battle experience, level threshold, primary-skill increment and the
    two-option secondary-skill advancement.
- Scenario and route sources, accessed 2026-09-21:
  - **[S1]** [Homecoming scenario record](https://heroes.thelazy.net/index.php/Homecoming),
    for exact victory/loss predicates, bonus set, fixed difficulty, level cap,
    carried hero count, starting hero/town and Terraneus location.
  - **[S2]** [Celestial Heavens campaign guide](https://www.celestialheavens.com/homm3/HoMM%20III%20Campaigns.pdf),
    for independent `Homecoming` objective, bonus, difficulty, map and carryover
    corroboration.
  - **[S3]** [Gamer Walkthroughs Long Live the Queen route](https://gamerwalkthroughs.com/heroes-of-might-and-magic-3/long-live-the-queen/),
    for independent surface start, recruitment/economy route and underground
    Terraneus terminal corroboration.
  - **[V1]** repository-side transition trace from P1–P13 and S1–S3; rules
    reasoning, not direct play.
- Claim IDs: `H3C-001`–`H3C-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- `ACT-140`: commit the `14 Pikemen` option from Homecoming's three starting
  bonuses before the scenario state is instantiated.
- `ACT-189`: select a hero and commit a currently reachable Adventure Map
  destination whose path then executes to allowance, contact or cancellation.
- `ACT-191`: choose one of the two legal secondary-skill improvements exposed
  when a hero crosses a level threshold.
- Revised `ACT-281`: end the current kingdom's open strategic turn after any
  legal subset of hero, town and army-management commands.
- Revised `ACT-345`: choose one legal owned-town structure or chain upgrade and
  pay its displayed resource cost.
- Revised `ACT-347`: choose a creature type and quantity from current dwelling
  stock, pay its price and place recruits into an eligible garrison or army.
- New `ACT-483`: move, split or merge one same-type creature troop among legal
  hero-army and town-garrison slots.
- New `ACT-484`: on the active troop's battle turn, commit one legal hex move,
  melee/ranged attack, wait or defend command.
- Claims: `H3C-002`, `H3C-003`, `H3C-005`–`H3C-010`.

### System Behaviour Genes

- `SYS-299`: battle experience crossing a threshold advances the hero and
  opens the declared primary/secondary skill result, bounded by level six.
- `SYS-305`: hero position and controlled territory update current sight while
  explored terrain remains distinguished from unseen map state.
- `SYS-614`: follow the committed hero route, spend terrain-adjusted movement
  points and retain the reached position or contact.
- Revised `SYS-616`: adventure contact instantiates a separate tactical battle
  from participating armies and terrain, then returns survivors, casualties,
  experience, result and ownership consequences to the strategic map.
- New `SYS-942`: reaching an eligible Adventure Map location consumes a loose
  reward once or transfers a mine/town into persistent ownership and exposes
  its continuing benefit.
- New `SYS-943`: after every kingdom has ended its turn, advance one day, apply
  controlled income and hero-movement refreshes, restore each town's daily
  construction capacity and, on the first day of a week, add dwelling growth.
- New `SYS-944`: each combat round activates troops once in speed order;
  waiting defers the troop, defending ends its action with a defensive bonus,
  and a surviving troop normally retaliates against its first melee attacker.
- New `SYS-945`: compute attack damage from creature and hero modifiers plus
  the attacking stack count, spend it through defender health and creature
  count, and let casualties reduce that troop's later output.
- New `SYS-946`: Terraneus capture settles Homecoming and selects up to the
  four strongest eligible heroes under the level-six cap for the next campaign
  scenario, without beginning that successor.
- Resolution order: strategic commands alter provisional hero, army, town and
  resource state; End Turn advances rival authority and day/week settlement;
  contact instantiates battle; speed-ordered troop actions settle damage and
  casualties; victory returns retained state; Terraneus ownership triggers the
  scenario and carryover settlement.
- Claims: `H3C-002`–`H3C-012`.

### Constraint Genes

- `CON-273`: decisions cannot rely on exact hero, army, site or terrain state
  still concealed by unexplored fog.
- `CON-270`: a level-six cap, eight-secondary-skill capacity and current
  two-option offer bound each hero's skill development.
- `CON-509`: a hero route requires traversable terrain and enough current
  movement allowance, subject to map contact and obstruction.
- Revised `CON-510`: town construction requires ownership, unused daily build
  capacity, prerequisites and enough typed resources.
- Revised `CON-514`: recruitment requires current dwelling stock, enough gold
  or other cost and an eligible destination troop slot or same-type stack.
- New `CON-652`: every hero army or town garrison has at most seven troop
  slots; each occupied slot contains one creature type, compatible types merge
  and a field hero must retain at least one troop.
- New `CON-653`: a battle troop may act only on its scheduled turn and only
  through reachable unblocked hexes or a legal target within its current move,
  melee/ranged, ammunition and state restrictions.
- Scarce strategic resources: hero movement, days, one town build per day,
  gold, wood, ore, mercury, sulfur, crystal, gems, dwelling stock, seven troop
  slots, current creatures, battlefield actions, retaliation and health.
- Claims: `H3C-003`, `H3C-005`–`H3C-010`.

### Information Genes

- Revised `INF-244`: Adventure Map, town and hero surfaces expose known map and
  fog, date, resources, selected route and movement, town ownership/buildings,
  dwelling stock, army stacks, hero progression and scenario objective.
- New `INF-361`: the battle view exposes battlefield hexes and obstacles,
  active troop, creature identity/count/health, speed, movement reach,
  ammunition, legal targets and resolved damage without disclosing the exact
  future random roll.
- Claims: `H3C-002`–`H3C-011`.

### Objective and Time Genes

- New `OBJ-195`: capture the named underground town Terraneus before losing
  every town and hero, settle Homecoming and preserve the declared four-hero
  successor selection.
- `TIM-001`: each committed battle troop action resolves completely before the
  next scheduled troop accepts a command.
- Revised `TIM-018`: one kingdom at a time receives an open multi-command
  strategic turn; End Turn passes authority, and the day settles only after all
  kingdoms have acted.
- Claims: `H3C-002`, `H3C-008`, `H3C-009`, `H3C-011`, `H3C-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Homecoming setup is open | choose `14 Pikemen` and begin | the fixed Easy map instantiates Christian, Caryatid, rivals and the chosen troop bonus | exact entry | `H3C-011` |
| Christian has movement and a reachable route | commit a visible surface destination | the hero follows the route, spends terrain-adjusted movement and retains the reached position or contact | allowance-bound travel | `H3C-003` |
| A loose resource or unowned mine is reachable | move Christian onto it and resolve any guard | the loose object enters the shared pool once, or the mine changes flag and contributes on later days | visit versus ownership | `H3C-004` |
| Caryatid has build capacity, prerequisites and resources | commission one legal Hall or dwelling structure | cost is removed, the structure appears and benefits apply; a second structure is rejected that day | daily town build gate | `H3C-005` |
| A dwelling has stock and the player can pay | select a legal creature quantity | stock and resources decrease while the matching troop enters an eligible garrison/army slot | bounded recruitment | `H3C-006`, `H3C-007` |
| Two compatible troop slots or a town/visiting-hero pair are open | split, merge or transfer the selected troop | counts and slots update without changing creature identity or creating an eighth slot | explicit army composition | `H3C-007` |
| Optional commands are complete | choose End Turn | rival turns resolve; after all kingdoms, date, income, movement and daily capacity refresh; weekly boundary adds dwelling population | nested day/week economy | `H3C-002`, `H3C-006` |
| A hero contacts a defended site or town | accept the encounter | current armies and terrain instantiate a separate hex battle | strategic/tactical transfer | `H3C-008` |
| One troop is active in the speed schedule | move, attack, wait or defend | the legal command resolves; melee may trigger first surviving retaliation and the scheduler advances | troop turn grammar | `H3C-008`, `H3C-009` |
| An attack lands on a multi-creature troop | allow damage to settle | current stack size scales output; damage removes creature health/count and later output reflects casualties | stack-count combat | `H3C-009` |
| Battle victory crosses a hero threshold | choose one offered secondary-skill improvement | primary skill rises automatically, the chosen legal secondary improvement persists and the level-six cap remains | hero progression | `H3C-010` |
| A surviving hero reaches defended Terraneus | win the battle and enter the town | Terraneus changes ownership, Homecoming settles and the four strongest eligible heroes are selected for the successor | exact positive terminal | `H3C-011`, `H3C-012` |

## Edge-case audit

- `ACT-483` is not inventory transfer: troop count, same-type merge and one of
  seven battlefield-start slots are causal; no carried-item stack is moved.
- `ACT-484` is not `ACT-189`: an active battle troop receives one scheduled
  discrete action, while a strategic hero receives a route that autonomous
  pathing follows through movement points.
- `SYS-943` is not ordinary recurring income alone: the same all-kingdom
  boundary advances the calendar, resets hero and town authority and contains
  the weekly dwelling-growth subcycle.
- `SYS-944` is not visible initiative queue `SYS-356` or rolled initiative
  `SYS-388`: original unmodded Heroes III orders by current speed, exposes no
  full modern queue, permits Wait/Defend and embeds one normal retaliation.
- `SYS-945` is not a single-body health bar: a troop is one battlefield unit
  whose current creature count multiplies output and whose internal casualties
  change the same battle's later turns.
- `CON-652` is not inventory or party-headcount capacity: seven typed troop
  stacks can each represent many creatures and their slot order sets initial
  battlefield placement.
- `OBJ-195` is not generic town capture or full enemy elimination: only named
  Terraneus capture triggers the positive terminal, while other enemies or
  surface objectives may remain.
- Spell casting, morale, luck, siege machines and creature special abilities
  are evidenced rules but not separately gene-coded because the fixed source-
  bounded route does not require one exact instance for terminal reachability.

## Strategic and experiential structure

- Local decision: choose a route tile, resource pickup, town structure,
  recruit quantity, troop split or active battle command while reading
  movement, stock, slot and current casualties.
- Medium-term planning: turn mines and Hall upgrades into enough daily income,
  time dwellings around weekly growth, concentrate stacks on a strong hero and
  preserve garrisons or alternate heroes against the loss condition.
- Long-term structure: convert a surface foothold into economic ownership and
  hero progression, then cross the subterranean threshold and settle the map by
  capturing one named town rather than clearing every hostile.
- Common heuristics: spend each hero's daily movement deliberately; claim
  recurring income before optional one-time rewards; build income and creature
  dwellings early; recruit after weekly growth; merge fragile identical troops
  while retaining useful tactical slots; use speed, range, Wait and first
  retaliation when choosing contact order; do not trigger Terraneus before the
  desired four heroes are ready to carry.
- Failure attribution: resource bar, Hall prerequisites, dwelling stock, route
  arrows, movement allowance, seven slots, active troop highlighting, counts,
  damage messages and explicit victory/loss text separate most causes.
- Player-trust factors: the interface discloses current legal choices and
  retained consequences, while fog, AI routes, random damage, luck/morale and
  level-up offers preserve bounded uncertainty.
- Claims: `H3C-002`–`H3C-012`.

## Replay and variation

- What changes between sessions: route order, recruited heroes, mine/town
  timing, building order, troop allocation, fights, casualties, level offers,
  AI movement, completion day and which four heroes rank strongest.
- Randomness or procedural generation: the authored map, towns and objective
  remain fixed; combat damage, morale/luck events, secondary-skill offers and
  opposing choices are bounded state-dependent variation.
- Multiple viable strategies: rapid underground capture, broader surface
  conquest, economy-first consolidation and multi-hero development can all
  reach the same Terraneus terminal.
- Typical replay motive: optimise completion time, preserve more troops, train
  a different carryover set or choose another starting bonus. Only the fixed
  `14 Pikemen` packet is canonical here.
- Claims: `H3C-002`–`H3C-012`.

## Adjacent systems and history

- Civilization VI shares sequential whole-polity turns, fog, resources,
  settlements and End Turn, but its units act directly on one persistent hex
  world and cities accumulate production instead of opening a separate
  speed-ordered stack battle and one-build-per-day town screen.
- Total War: WARHAMMER III shares hero-led strategic routes, settlements and
  campaign-to-battle return, but its battle is pausable real time with regiment
  formation/morale and its construction advances over turns rather than
  applying immediately under a daily capacity.
- Mount & Blade II: Bannerlord shares paid local recruitment into a persistent
  mobile force, but recruits are individual party bodies under a party-size
  limit rather than seven same-type creature stacks whose counts drive damage.
- Warcraft III shares a hero, experience, fog, selected-unit commands and army
  combat, but all of its scoped route is live RTS time and lacks strategic
  days, separate tactical rounds and town/dwelling weekly economy.
- Important difference: one End Turn crosses daily income, replenished route
  authority and a nested weekly recruit cycle, while every strategic contact
  can instantiate a separate battle whose casualties return to that same map.
- Claims: `H3C-002`–`H3C-012`.

## Normalised genome

The front matter is canonical. The complete signature contains 29 Active
genes: eight Action, nine System Behaviour, seven Constraint, two Information,
one Objective and two Time genes. Carrier labels such as Terraneus, Pikemen,
Castle, Easy and Christian remain parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `331` (`GAME-0001`–`GAME-0331`).
- Exact genome matches: none.
- Tied near matches: `GAME-0191` — Total War: WARHAMMER III (`12 / 44 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0191` — Total War: WARHAMMER III | `ACT-189`, `ACT-191`, `ACT-281`, `ACT-345`, `SYS-305`, `SYS-614`, `SYS-616`, `CON-273`, `CON-509`, `CON-510`, `INF-244`, `TIM-018` | Both join hero-led strategic routes, fog, owned-settlement construction, development, polity turns and campaign-to-battle return. Total War uses delayed slot construction and pausable real-time regiment battles with deployment and morale; Heroes III uses immediate one-per-day construction, dwelling stock, seven typed creature stacks, speed-ordered hex rounds, nested weekly growth and ranked scenario carryover. | Near, `12 / 44 = 0.272727` |

## Taxonomy impact

This unit tests whether earlier strategic-map, settlement and recruitment
boundaries generalise beyond their first real-time or single-party carriers.
`TAXONOMY_CHANGE_076` revises only wording and parameters for `ACT-281`,
`ACT-345`, `ACT-347`, `SYS-616`, `CON-510`, `CON-514`, `INF-244` and `TIM-018`;
no lower-ID signature changes. Eleven genuinely unsupported boundaries remain
new: two Actions, five Systems, two Constraints, one Information and one
Objective.

## Negative results

- No verified combination is registered from a single new supporter.
- No complete-product union is accepted: expansion content and optional
  catalogues remain outside the Homecoming packet.
- No direct-play, exact build, exact AI, exact damage probability, save/reload
  or audiovisual claim is made.
- No existing inventory-stack, visible-initiative, real-time battle or city-
  production boundary is stretched to absorb seven-slot creature troops,
  speed rounds or immediate daily construction.

## Delta summary

## New facts

- One fixed Homecoming route now supplies an exact strategic-day, weekly-growth,
  town-economy, troop-stack, tactical-battle and named-town terminal trace.
- Current GOG Complete identity is separated from the original Restoration of
  Erathia rules packet and from unofficial modern extensions.

## New genes

- `ACT-483`, `ACT-484`, `SYS-942`–`SYS-946`, `CON-652`, `CON-653`, `INF-361`
  and `OBJ-195` isolate the eleven new boundaries listed above.

## New combinations

- None. Recurrence remains evidence-driven.

## Taxonomy changes

- `TAXONOMY_CHANGE_076` generalises eight lower-ID definitions without changing
  their prior carriers or signatures.

## New questions

- Does another classic campaign strategy game reproduce the same nested
  day/week economy and separate speed-ordered stack battle strongly enough to
  support a recurring combination?
- Should a later spell-centred packet isolate one-per-round hero casting, mana
  and persistent spell acquisition without bloating this scenario signature?

## Next recommended game

`GAME-0333` — *Sonic the Hedgehog*, original North American Sega Genesis,
fresh `Green Hill Zone Act 1`, is the next and final reserved unit in the active
nine-game Goal horizon.

## Why this game

It closes the PC strategy slot with a widely recognised campaign ruleset and
stress-tests three existing boundaries at once: whole-polity turns,
campaign-to-battle state transfer and paid recruitment. Its differentiator is
not fantasy theme but the causal join between daily movement/economy, weekly
dwelling growth and seven-slot speed-ordered troop combat.

## Completion checklist

- [x] Exact current product and base-campaign scenario boundary fixed.
- [x] Entry, positive terminal, failure terminal and exclusions stated.
- [x] Primary/manual and independent scenario evidence separated.
- [x] Direct-play and installed-build claims explicitly disclaimed.
- [x] Candidate genes compared against lower-ID boundaries.
- [ ] Deterministic indexes, full comparison and taxonomy artifacts regenerated.
- [ ] Reviewed Ukrainian, presentation, platform, families, salience and plain-language integrated.
- [ ] Original artwork and responsive variants integrated.
- [ ] Repository, localisation, build, browser and accessibility gates passed.

## Search-demand continuation

The unit fulfils `GAME-0332` from
[`SEARCH_DEMAND_GAME_SELECTION_022`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_022.md).
`GAME-0333` remains reserved and unstarted until this game's focused acceptance
and one local commit are complete.
