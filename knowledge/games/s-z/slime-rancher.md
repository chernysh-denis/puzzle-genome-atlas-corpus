---
game_id: GAME-0307
slug: slime-rancher
game_title: Slime Rancher
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-164
    - ACT-219
    - ACT-467
  system:
    - SYS-889
  constraint:
    - CON-210
  information:
    - INF-073
    - INF-115
    - INF-117
  objective:
    - OBJ-179
  time:
    - TIM-003
---

# Game: Slime Rancher

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Pink Slime,
Pink Plort, Vacpack, Plort Market, Newbucks, High Walls and the starter corral
are parameters or product labels, not gene names.

## Analysis scope

- Version / ruleset: Monomi Park's original English Windows Steam product,
  Adventure mode, unmodified base game and clean local save. The product page
  and current public material were checked 2026-09-19; an installed executable,
  build number and save were not available. Slime Rancher 2, Casual and Rush
  use different product or mode boundaries and are excluded.
- Structured analysis target: original Windows Steam product in Adventure
  mode; see `GAME-0307` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: begin at first ordinary control on the inherited ranch with the
  starter corral, basic four-tank Vacpack and 250 Newbucks. Tutorial prompts
  may explain the controls but are not treated as autonomous completion.
- Primary decision loop: walk between the ranch and nearby Dry Reef; aim the
  Vacpack to vacuum reachable Pink Slimes, compatible food and loose Pink
  Plorts into typed tanks; select a tank and expel Pink Slimes into the starter
  corral, then expel fruit, vegetables or meat where a hungry Pink Slime can
  eat. The creature consumes compatible food and produces a Pink Plort. Vacuum
  that output, inspect the current market value, fire it into the Plort Market
  to receive Newbucks, and repeat until the balance reaches the displayed 350
  High Walls price. Purchase High Walls for the starter corral.
- Positive terminal: High Walls ownership registers on the starter corral
  after at least one Pink Plort sale was required to lift the fresh balance
  from 250 to 350. Stop immediately after the purchase; do not claim that all
  350 Newbucks were earned in the packet or that a save/reload retained it.
- Negative terminal: there is no finite authored failure required before this
  first purchase. Full Vacpack tanks reject excess transfer, incompatible food
  does not satisfy the selected Pink Slime feeding transition, and insufficient
  Newbucks keeps High Walls unavailable. These are recoverable states, not a
  Game Over claim.
- Included: direct walking; aimed suction and expulsion; active tank selection;
  four typed tank stacks with basic capacity 20; locally visible loose
  creatures, food and output; Pink Slime's any-food diet; food consumption and
  one-plort production; visible balance, sell value and High Walls offer;
  plort sale; purchase and registered containment upgrade; continuous creature
  and world motion while the player acts. Exact route, food mix, slime count,
  sale count and changing market value remain parameters.
- Excluded: Garden construction, crop growth, hen breeding, favourite-food
  doubling, Largos, Tarr, Gordo feeding, dangerous slimes, knockout and item
  loss, sleep, day-price optimisation, Vacpack upgrades, ranch expansion,
  Range Exchange, Slime Science, gadgets, story mail, later regions, DLC,
  Secret Styles, Casual, Rush, multiplayer, other platforms and Slime Rancher 2.
- Reproducible parameterisation: create an original-game Adventure save, retain
  the starter 250 Newbucks, and use only the starter corral and nearby Pink
  Slimes/food. Put a manageable set of Pink Slimes in the corral, feed them
  compatible gathered food, vacuum produced Pink Plorts, sell them at the
  ranch market and purchase High Walls only after the displayed balance reaches
  350. Quantity and current unit price may vary; the terminal must include at
  least one completed food-to-plort-to-sale chain.
- Potential scoped modules: direct Windows trace with exact build and save
  reload; changing daily market prices; Garden farming; Largo and favourite
  food multiplication; Tarr risk; automation; later ranch expansion and story.
- Direct-play status: not conducted. No installed Windows build, entitlement,
  save file or local run was available. The official Steam product page
  directly establishes the original product, Adventure mode and the broad
  collect/feed/sell/upgrade loop. Independent original-game written references
  corroborate the starter state, four by twenty tanks, Pink Slime diet, market
  transfer and 350-Newbuck High Walls purchase. This is a source-bounded
  reconstruction, not a claim of observed inputs, price rolls or persistence.
  No video or audio was opened, played or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SLR-001` | The target is the original Windows Steam product by Monomi Park, released 2017-08-01, with Adventure among its modes | Confirmed | Direct | High | P1 |
| `SLR-002` | The official product premise joins Vacpack collection, slime feeding, plort-market income and ranch or equipment upgrades | Confirmed | Direct | High | P1 |
| `SLR-003` | A fresh Adventure ranch begins with a starter corral and 250 Newbucks | Observation | Corroborated | Medium | S1, S2 |
| `SLR-004` | The basic Vacpack stores up to four types in separate stacks of 20 and can vacuum or expel compatible world entities | Observation | Corroborated | Medium | S1, S3 |
| `SLR-005` | Pink Slimes accept fruit, vegetables or meat and produce Pink Plorts after compatible feeding | Observation | Corroborated | Medium | S1, S4 |
| `SLR-006` | Firing Pink Plorts into the market removes them and increases Newbucks by the shown current value | Observation | Corroborated | Medium | S1, S2 |
| `SLR-007` | High Walls cost 350 Newbucks and increase the starter corral's containment boundary | Observation | Corroborated | Medium | S2, S5 |
| `SLR-008` | No installed build, direct attempt, exact price sequence or reload retention was observed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Monomi Park developed and published Slime Rancher; the
  original Windows product left Early Access on 2017-08-01.
- Platform or physical form: Windows Steam single-player first-person sandbox,
  clean local Adventure save and unmodified base product.
- Puzzle family: inventory and fixture dependencies; real-time system pressure;
  ordered dependency sequencing.
- Primary and official source, accessed 2026-09-19:
  - **[P1]** [Slime Rancher on Steam](https://store.steampowered.com/app/433340/SlimeRancher?l=english),
    for original product identity, release, developer/publisher, Adventure mode
    and the Vacpack, crop, feeding, Plort Market and upgrade premise.
- Corroborating written sources, accessed 2026-09-19:
  - **[S1]** [Slime Rancher For Dummies](https://steamcommunity.com/sharedfiles/filedetails/?id=606079290),
    for the original-game fresh ranch, Pink Slime diet, feeding, plort output,
    Vacpack interaction and Plort Market receiver.
  - **[S2]** [original-game new-player guide](https://steamcommunity.com/app/433340/discussions/0/133260909500839513/),
    for the early Pink Slime sale loop and 350-Newbuck High Walls target.
  - **[S3]** [Vacpack reference](https://slimerancher.fandom.com/wiki/Vacpack_%28Slime_Rancher%29),
    for original-game suction/expulsion, four typed tanks and basic 20-unit
    capacity; this community reference is not treated as an official manual.
  - **[S4]** [Pink Slime reference](https://slimerancher.wiki.gg/wiki/Pink_Slime_%28SR%29),
    for the original game's any-food diet and Pink Plort output.
  - **[S5]** [original-game corral guide](https://steamcommunity.com/sharedfiles/filedetails/?id=607216765),
    for the 350-Newbuck High Walls price and doubled barrier height.
- Research record: **[R1]** 2026-09-19 local preflight found no installed
  Slime Rancher executable, entitlement or saved trace; no direct play or
  reload occurred.
- Claim IDs: `SLR-001`–`SLR-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008` covers direct ranch/Dry Reef traversal. `ACT-164` selects one of
  the visible Vacpack tanks. New `ACT-467` owns aimed suction from the world
  and expulsion from the active tank into the corral or market receiver.
  `ACT-219` converts owned Pink Plorts at the accepting market fixture, while
  `ACT-130` buys the displayed High Walls asset once affordable. Claims:
  `SLR-002`, `SLR-004`, `SLR-006`, `SLR-007`.

### System Behaviour Genes

- New `SYS-889` consumes compatible food reached by a ready Pink Slime and
  produces a loose Pink Plort without a second player command. Suction and
  expulsion remain player actions rather than part of this automatic rule.
  Claim: `SLR-005`.
- Resolution order: collect creature and food; place creature in corral; offer
  compatible food; creature eats and creates output; collect output; sell;
  balance updates; purchase High Walls. No crop, favourite-food or automation
  transition is inserted.

### Constraint Genes

- `CON-210` bounds each transfer by the selected compatible tank and its basic
  stack capacity. An occupied tank does not accept another type, and a full
  stack leaves excess in the world. Price sufficiency is already part of the
  purchase action rather than a metaprogression prerequisite gene. Claim:
  `SLR-004`.

### Information Genes

- `INF-073` exposes all four tank contents, counts and the selected tank.
  `INF-115` limits world knowledge to locally seen or heard creatures, food and
  output. `INF-117` exposes current Newbucks, market values and the High Walls
  offer before sale or purchase. Claims: `SLR-004`, `SLR-006`, `SLR-007`.

### Objective Genes

- New `OBJ-179` ends this open-ended game at a reproducible first enclosure
  upgrade: food becomes creature output, output becomes spendable Newbucks and
  the balance admits High Walls. Starting money is acknowledged, not mislabelled
  as earned income. Claims: `SLR-003`, `SLR-005`–`SLR-007`.

### Time Genes

- `TIM-003` covers continuous creature motion and world physics while the
  player walks, aims, transfers and buys. The packet has no turn boundary or
  finite deadline. Claims: `SLR-002`, `SLR-004`, `SLR-005`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Adventure control with starter ranch and 250 Newbucks | Inspect corral, HUD and market | Four empty tanks, starter enclosure, balance and current offers are available | exact source-bounded entry | `SLR-003`, `SLR-004` |
| Reachable Pink Slime or food and compatible tank space | Hold suction while aiming | Entity leaves the world and enters one typed active tank up to capacity | aimed transfer differs from contact pickup | `SLR-004` |
| Pink Slime and food occupy separate tanks | Select and expel them into the starter corral | World-located creature and food reappear at the aimed positions | stored types become addressed world inputs | `SLR-004` |
| Hungry Pink Slime reaches compatible food | Wait without another feeding command | Food disappears and one Pink Plort appears | autonomous diet-to-output rule | `SLR-005` |
| Pink Plort is loose and tank space is compatible | Vacuum it, select its tank and fire into market | Plort is removed and Newbucks increase by the displayed current value | owned output becomes currency | `SLR-006` |
| Balance is below 350 | Attempt High Walls purchase | Offer remains unavailable; no upgrade registers | recoverable affordability boundary | `SLR-007` |
| At least one sale has raised balance to 350 or more | Purchase High Walls for starter corral | Currency is debited and the higher boundary registers | selected positive terminal | `SLR-003`, `SLR-006`, `SLR-007` |

## Strategic and experiential structure

- Local decision: choose which nearby slime, food or output to collect and keep
  enough compatible tank space to separate their types.
- Medium-term planning: keep Pink Slimes contained, route food to them, then
  recover loose plorts instead of filling every tank with one input class.
- Long-term structure: repeat the care-and-sale chain only until the first
  concrete containment upgrade becomes affordable; wider fortune building is
  outside this bounded objective.
- Common heuristics: reserve separate tanks for slime, food and plorts; use
  Pink Slimes because their diet accepts every ordinary food class; read the
  current sale value and balance before returning to the corral upgrade panel.
- Failure attribution: wrong active tank, incompatible occupied stack, full
  tank, unreachable loose item, unfed slime or insufficient balance each blocks
  a different edge and remains recoverable.
- Player trust: tank icons/counts, visible loose objects, eating/output feedback,
  market prices, Newbucks and upgrade offer expose each critical transition.

## Replay and variation

- What changes: encountered Pink Slimes and food, tank allocation, feeding
  positions, market value, required plort count and elapsed live time.
- Randomness or procedural generation: the packet does not claim a procedural
  ranch layout; nearby spawn availability and current prices can vary.
- Multiple viable strategies: collect wild Pink Plorts or feed contained Pink
  Slimes, provided the terminal trace includes one complete feeding-produced
  plort that is sold before High Walls is bought.
- Replay motive: optimise income, expand the ranch or explore later systems;
  those aims are excluded from this first-upgrade signature.

## Adjacent systems and history

- Nearby corpus cases: DREDGE sells gathered typed catch at visible prices,
  DAVE THE DIVER turns stocked ingredients into service revenue, and Minecraft
  uses typed carried stacks and active quick slots. Slime Rancher differs in
  using one aimed suction/expulsion tool to move an autonomous creature, its
  compatible food and the creature-produced sale output through the same tanks.
- Later systems: crop production, favourite-food doubling, Largos, automation
  and Slime Science amplify the economy but are not back-projected into the
  first High Walls purchase.
- Version caution: public documentation establishes original-game rules, not
  an observed installed 2026 Windows build. No platform-parity claim follows.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-164`, `ACT-219`, `ACT-467` | travel, tank select, suction/expulsion, sale, purchase |
| System Behaviour | `SYS-889` | diet-triggered plort production |
| Constraint | `CON-210` | four typed tanks, stack capacity 20 |
| Information | `INF-073`, `INF-115`, `INF-117` | tank HUD, local world state, market and balance |
| Objective | `OBJ-179` | first paid containment upgrade |
| Time | `TIM-003` | live creatures and world |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `306` (`GAME-0001`–`GAME-0306`).
- Exact genome matches: none.
- Tied near matches: `GAME-0237` — Serious Sam HD: The First Encounter (`5 / 20 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0237` — Serious Sam HD: The First Encounter | `ACT-008`, `ACT-164`, `INF-073`, `INF-115`, `TIM-003` | Both Windows packets directly traverse a continuously moving world, select a visible carried slot and act from locally perceived state. Serious Sam uses that structure for finite-ammunition combat, trigger-released hostile groups and an authored level exit. Slime Rancher instead vacuums creatures, food and output through typed tanks, lets feeding produce a sale item, converts it at a visible market and ends at a paid enclosure upgrade with no combat or level-clear terminal. | Tied near, `5 / 20 = 0.250000` |

### Preserved research notes

- New genes: `ACT-467`, `SYS-889`, `OBJ-179`.
- Classification result: new genes with reused navigation, quick-slot,
  transaction, inventory-capacity, local-information and real-time boundaries.
- Evidence and reasoning: suction/expulsion is a reversible aimed transfer, not
  contact pickup; the creature consumes compatible food and emits a loose
  output without a second command; the bounded objective joins that output to
  a specific paid containment result instead of generic wealth maximisation.

## Taxonomy impact

- Registry changes: three new Active definitions; no earlier signature,
  existing definition or lifecycle changes.
- Taxonomy-change record: none; no earlier boundary is rewritten.
- Candidate terms affected: Pink Slime, Pink Plort, Vacpack, Plort Market,
  Newbucks, High Walls and corral remain instance labels.

## Negative results

- The broad product premise does not prove exact installed prices or current
  spawn sequences. High Walls and the fresh entry are retained at Corroborated
  Medium, and the route allows variable sale count.
- No direct play or reload trace exists, so persistence after quit, exact price
  fluctuation and failure recovery are not asserted.
- Garden growth, Largos, Tarr, favourite multipliers, automation and the wider
  campaign are excluded rather than inferred from the product description.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original Windows product expressly connects
  Vacpack collection, hungry-slime care, the Plort Market and purchased ranch
  improvements (`SLR-001`, `SLR-002`).
- [Observation | Corroborated | Medium] Original-game references specify the
  250-to-350 starter affordability edge and typed tank/feed/sale sequence
  (`SLR-003`–`SLR-007`).

## New genes

- [Observation | Corroborated | Medium] `ACT-467`, `SYS-889` and `OBJ-179`
  isolate aimed tank transfer, creature-consumption output and the bounded
  care-to-upgrade terminal.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is asserted;
  the final subset scan is recorded above.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier canonical gene or game signature is
  changed by this addition.

## New questions

- Which exact Windows build and day-one Pink Plort prices occur on a new local
  Adventure save, and does the purchased High Walls state survive quit/reload?
- Does a direct trace expose any tutorial gate that delays the same starter
  transfer and purchase loop?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0308` — Bloodborne (PS4), scoped to the
  first fresh Hunter's Dream/Yharnam cycle and first persistent lamp return.
- Optimisation criterion: contrast creature-care production with a finite
  combat/recovery loop while preserving the selected platform rotation.
- Backlog impact: `GAME-0308` remains the next recorded unit; no later game is
  started inside this commit.

## Why this game

- [Hypothesis | Limited | Medium] The first unit opens the new nine-game page
  with a widely recognised non-combat management loop and tests whether the
  atlas can distinguish aimed creature/item transfer from ordinary inventory
  pickup while ending an open sandbox at one observable paid upgrade.
