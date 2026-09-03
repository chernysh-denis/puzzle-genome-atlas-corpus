---
game_id: GAME-0233
slug: 7-days-to-die
game_title: 7 Days to Die
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0231
gene_ids:
  action:
    - ACT-008
    - ACT-122
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-402
  system:
    - SYS-161
    - SYS-208
    - SYS-215
    - SYS-223
    - SYS-327
    - SYS-328
    - SYS-741
  constraint:
    - CON-210
    - CON-281
    - CON-297
    - CON-496
    - CON-573
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-132
    - INF-282
  objective:
    - OBJ-145
  time:
    - TIM-003
---

# Game: 7 Days to Die

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `251570`, official `V3.2.0 Stable`, public Build ID `24994517`, built
  2026-08-28 and placed on the public branch 2026-08-31, checked 2026-09-03;
  one new local single-player save on the shipped hand-authored `Navezgane`
  world with the default `Adventurer` sandbox preset and no customisation.
- Entry: create a genuinely fresh Navezgane save, accept the first controllable
  survivor state in the Pine Forest and open the current `Basics of Survival`
  challenge group. No old save, imported character, console command or retained
  challenge progress is admissible.
- Primary decision loop: inspect the challenge ledger, current survival state,
  carried items and recipes; harvest the exact local Plant Fiber, Wood and Small
  Stone requirements; personally queue the taught primitive recipes; equip the
  Primitive Outfit; use the Stone Axe for the separately counted harvest;
  craft the Wooden Club, Primitive Bow and Stone Arrow; redeem each completed
  challenge; collect the group completion reward that creates `Journey to
  Settlement`; then follow its map and compass marker to the nearest White
  River Outpost while avoiding or directly fighting only unavoidable local
  threats.
- Positive retained terminal: enter the marked trader radius so `Journey to
  Settlement` settles, the Stone Shovel reward is credited and the quest no
  longer remains active; leave through the ordinary menu, reload the same local
  save and confirm the credited shovel plus completed tutorial/trader-route
  state. Merely crafting the last arrow, turning every row green, receiving the
  trader quest or arriving outside its completion radius is intermediate.
- Negative evaluation terminal: survivor death before the verified trader
  settlement rejects that fresh attempt rather than importing the respawned
  state. A missing trader destination, a quest that does not settle on entry or
  a reload that loses the reward also rejects the run and records the exact
  observed state instead of choosing an arbitrary sandbox stop.
- Included: one current Navezgane spawn; direct first-person movement; local
  resource harvesting; inventory capacity and hotbar selection; Stone Axe wear;
  personal timed crafting; the eight mechanical Basics requirements plus their
  opening and redemption entries; Primitive Outfit equipment; incidental
  stamina, hunger, thirst, health and local zombie risk only while they can
  block this route; challenge completion and manual reward claims; the generated
  nearest-outpost marker; one walk to its trader radius; explicit quest reward
  and one verification reload.
- Reproducible parameterisation: use Steam public `V3.2.0` / Build `24994517`,
  English, Local Game, Navezgane, a new save name and unchanged Adventurer
  preset; retain the shipped tutorial and trader options; gather 10 Plant Fiber,
  10 Wood and 5 Small Stone, craft the required primitive items and repeat the
  Stone Axe harvest of 10 Wood and 5 Small Stone as the ledger requests; redeem
  every green row, accept the resulting trader route and stop after the verified
  `Journey to Settlement` reward. Exact spawn, pickup pose and walking line may
  vary without changing the predicates.
- Excluded: Random Gen and pre-generated worlds; multiplayer, dedicated servers,
  crossplay and Twitch integration; every non-Adventurer preset, custom sandbox
  code, mods, console/debug/creative tools and save editing; Homesteading,
  Advanced Survival, Crafting, Traders / Quests and every later challenge group;
  trader dialogue, buying, selling and jobs; first POI clearance; land claims,
  bedrolls, campfires, bases, farming, vehicles and biome progression; death and
  respawn; Blood Moon preparation or history; DLC, cosmetics, achievements and
  the continuing open-world survival sandbox.
- Potential scoped modules: one fixed trader job from offer through returned
  reward, one Blood Moon defence, one biome-survival group or one persistent
  base packet each needs its own build, entry, terminal and exclusions.
- Direct-play status: no client session was played. Current official product,
  stable-release and save-location material establish product, build channel,
  lawful platform and local-save boundary. The current V3.2 data extracts and
  official wiki establish the challenge predicates, reward claim, trader route
  and quest reward. The transition trace is evidence-based rules reasoning. No
  video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `7DTD-001` | `V3.2.0 Stable` and Steam public Build `24994517` are the reviewed Windows release | Confirmed | Corroborated | High | P1, P2, S1 |
| `7DTD-002` | Steam app `251570` is the released Windows product, distinct from its 2013 Early Access entry and console editions | Confirmed | Direct | High | P2 |
| `7DTD-003` | A shipped Navezgane local game uses a prefabricated vanilla world and keeps its single-player state under the local save boundary | Confirmed | Direct | High | P3, S2 |
| `7DTD-004` | The current Basics group has ten entries: an opening tutorial entry, eight mechanical gather/craft/equip/harvest requirements and a final reward-redemption entry | Observation | Corroborated | High | S3 |
| `7DTD-005` | The mechanical requirements use explicit quantities, recipes, equipment and a second tool-qualified harvest rather than one generic progress counter | Observation | Direct | High | S3 |
| `7DTD-006` | Completed challenge rewards must be redeemed, and redeeming every row yields the group's Trader Quest reward | Observation | Direct | High | S3 |
| `7DTD-007` | `Journey to Settlement` marks the nearest White River Outpost and settles a Stone Shovel when its trader-radius objective is reached | Observation | Direct | High | S4 |
| `7DTD-008` | The tutorial-directed trader is a protected early service destination; actual buying, selling and jobs begin a different loop | Observation | Corroborated | High | S4, S5 |
| `7DTD-009` | Personal crafting, harvesting, equipment, survival meters and live threats remain mechanically active during the bounded route | Observation | Corroborated | High | P2, S3, S5 |
| `7DTD-010` | Quest settlement plus the credited reward supplies a positive system-authored terminal that does not depend on elapsed sandbox time | Confirmed | Corroborated | High | S3, S4, V1 |
| `7DTD-011` | Normal exit and reload of the same local save is the acceptance test for retained completion, while death before it rejects the scoped fresh attempt | Observation | Corroborated | Medium | P3, V1 |

## Basic data

- Release / origin: The Fun Pimps developed and published 7 Days to Die; the
  released product left Early Access on 2024-07-25, and the reviewed stable
  update is `V3.2.0` dated 2026-08-26.
- Platform or physical form: local single-player first-person survival,
  harvesting and crafting on the Windows Steam client; one prefabricated-world
  onboarding route.
- Puzzle family: real-time system pressure; resource transformation and
  production; inventory and fixture dependencies; ordered dependency
  sequencing.
- Primary and official sources:
  - **[P1]** [official V3.2.0 Stable notes](https://7-days-to-die.zendesk.com/hc/en-us/articles/52927476667924-V3-2-0-Stable),
    for the current stable version, release date, public maintenance context and
    unchanged trader-progression support.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/251570/7_Days_to_Die/),
    for app identity, Windows availability, developer/publisher, 2024 release,
    earlier Early Access date, local single-player and the survival, crafting,
    voxel-world and Navezgane product boundary.
  - **[P3]** [official save-location help](https://7-days-to-die.zendesk.com/hc/en-us/articles/48520694260628-Locating-or-moving-your-save-file),
    for vanilla prefabricated-world handling and the Windows local single-player
    save boundary.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/251570/depots/), for
    public Build `24994517`, the Windows depot, build timestamp and default
    public-branch update timestamp.
  - **[S2]** [current V3.2 Navezgane map reference](https://www.7dtd.tools/map),
    for the hand-authored fixed-world boundary and distinction from Random Gen.
  - **[S3]** [current V3.2 challenge data](https://www.7dtd.tools/challenges),
    for all ten Basics entries, exact quantities, personal recipes, armour
    equipment, reward-redemption rules and the Trader Quest group reward.
  - **[S4]** [current V3.2 quest data](https://www.7dtd.tools/quests), for the
    `Journey to Settlement` nearest-outpost marker, trader-radius objective and
    Stone Shovel reward.
  - **[S5]** [official wiki trader reference](https://7daystodie.wiki.gg/wiki/Traders),
    for tutorial direction to the nearest trader, protected compound and the
    separate buying, selling and job systems excluded here.
- Reproducible control: **[V1]** repository-side transition and evaluation trace
  across `P1`–`P3` and `S1`–`S5` under the fixed client, world, preset, local
  save and terminal contract; no audiovisual playback or direct-play claim.
- Claim IDs: `7DTD-001`–`7DTD-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: choose the walking line from spawn through local resource
  targets to the marked outpost; `ACT-122`: hold the compatible harvest command
  on grass, wood and stone; `ACT-123`: request each known primitive recipe;
  `ACT-164`: select the Stone Axe or other carried item; `ACT-199`: move the
  crafted Primitive Outfit into its compatible equipment slot; `ACT-161`: aim
  and strike only an unavoidable hostile on the live route.
- New `ACT-402`: redeem a recorded completed challenge reward from the ledger.
- Parameters: resource class, required quantity, target, tool, recipe,
  ingredients, craft quantity, queue, item, equipment slot, challenge row,
  completion state, reward and route marker.
- Claim IDs: `7DTD-004`–`7DTD-009`.

### System Behaviour Genes

- Existing `SYS-161`: deplete each finite local resource source; `SYS-208` and
  `SYS-215`: resolve any unavoidable direct combat through local geometry and
  live hostile state; `SYS-223`: reduce Stone Axe or weapon durability;
  `SYS-327`: advance health, hunger, thirst and activity state; `SYS-328`:
  consume ingredients and complete personal craft requests over live time.
- New `SYS-741`: record independently completed challenge predicates, settle
  their manual reward claims and issue the guided destination quest only after
  every required row has been redeemed.
- Resolution order: sample movement, harvesting, crafting, equipment, reward or
  combat input; update survival and hostile activity; validate reach, tool,
  inventory, recipe and current challenge predicate; resolve yield, craft or
  equipment state; record the matching challenge; accept a legal reward claim;
  after the final row issue `Journey to Settlement`; update its marker; settle
  the trader radius and credit the shovel.
- Claim IDs: `7DTD-004`–`7DTD-011`.

### Constraint Genes

- Existing `CON-210`: carried stacks and slots bound harvested inputs and
  crafted outputs; `CON-281`: health, hunger, thirst, stamina and equipment wear
  must remain recoverable; `CON-297`: each primitive craft requires a known
  recipe and sufficient compatible ingredients; `CON-496`: harvest credit
  requires reach, eligible target and the specified bare hand or Stone Axe.
- New `CON-573`: one row reward requires its own recorded completion, while the
  group destination reward requires every mandatory row to be redeemed.
- Scarce strategic resources: required Plant Fiber, Wood and Small Stone;
  carried capacity; Stone Axe durability; crafting and walking time; stamina,
  food, water and health only until the trader terminal.
- Claim IDs: `7DTD-004`–`7DTD-010`.

### Information Genes

- Existing `INF-073`: expose hotbar, stacks and active item; `INF-075`: expose
  personal survival and wear; `INF-115`: reveal only currently perceived local
  threats; `INF-128`: expose carried identity, quantity and equipment
  compatibility; `INF-132`: expose known recipes, ingredients, queue and output;
  `INF-125`: expose the accepted trader quest and its map/compass destination.
- New `INF-282`: expose each challenge requirement, live count, completed state,
  redeemable reward and group-claim readiness before commitment.
- Hidden future hostile positions, later trader stock and later challenge
  groups do not enter the information set.
- Claim IDs: `7DTD-004`–`7DTD-010`.

### Objective Genes

- New `OBJ-145`: complete and redeem one survival-onboarding checklist, follow
  its newly issued world-service destination, settle its spatial objective and
  retain the explicit route reward.
- Success, evaluation and failure: green rows without redemption and issued
  route without trader-radius settlement are intermediate. Shovel credit plus
  verified retained quest closure is positive; death, missing destination,
  non-settlement or lost reload state rejects the fresh attempt.
- Claim IDs: `7DTD-006`, `7DTD-007`, `7DTD-010`, `7DTD-011`.

### Time Genes

- Existing `TIM-003`: personal crafting, stamina and survival changes, hostile
  motion, combat and traversal continue in real time rather than waiting for a
  separate turn.
- Claim IDs: `7DTD-005`, `7DTD-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh survivor; Basics ledger open | Acknowledge the opening tutorial entry | Its own completion is recorded and the remaining visible requirements stay independently inspectable | tutorial is a checklist, not one opaque quest | `7DTD-004` |
| Reachable grass, wood and stone; counts below target | Harvest by hand | Compatible yields enter carried stacks until 10 Plant Fiber, 10 Wood and 5 Small Stone are recorded | exact resource predicates gate later craft | `7DTD-005` |
| Stone Axe recipe known; inputs carried | Commit one personal craft | Ingredients are reserved and the axe enters inventory when its queue time completes | craft request and timed resolution differ | `7DTD-005`, `7DTD-009` |
| Stone Axe active; separate harvest rows incomplete | Strike compatible wood and stone sources | Tool-qualified yields advance the 10 Wood and 5 Small Stone counters while axe wear advances | owning the tool is not harvest completion | `7DTD-005` |
| Primitive Outfit crafted and carried | Equip it to the compatible body slot | Worn state satisfies the separate Wear Armor predicate | crafting and equipment are independent | `7DTD-005` |
| Ingredients available | Craft Wooden Club, Primitive Bow and Stone Arrow | Each completed output records its own challenge predicate | dependencies may be routed but all outcomes are required | `7DTD-005` |
| One row is green but unclaimed | Commit its Redeem action | The individual reward is credited and the row becomes redeemed | completion does not auto-claim value | `7DTD-006` |
| Every Basics row has been redeemed | Claim the group completion | The system issues `Journey to Settlement` and marks the nearest White River Outpost | complete checklist creates a world route | `7DTD-006`, `7DTD-007` |
| Trader quest active; destination marked | Walk to the outpost's objective radius | The route settles and one Stone Shovel is credited | spatial arrival supplies the positive terminal | `7DTD-007`, `7DTD-010` |
| Trader route settled and reward carried | Exit normally, reload the same save and inspect quest/inventory | Retained closure and shovel accept the run; missing state rejects it | explicit evaluation replaces arbitrary stopping | `7DTD-011` |
| Survivor reaches lethal health before verification | Do not continue the respawned state | The current fresh attempt is rejected | respawn belongs to a different packet | `7DTD-009`, `7DTD-011` |

## Strategic and experiential structure

- Local decision: choose the nearest eligible source, active tool, recipe order,
  equipment transfer or safe route while reading exact ledger progress.
- Medium-term planning: avoid consuming the required Wood, Stone or Plant Fiber
  in excluded crafts; queue dependent primitive gear and redeem each completed
  row before committing to the marked walk.
- Long-term structure: independent survival predicates become claimed row
  rewards; all claims issue a spatial service quest; arrival converts that
  route into one explicit retained item and closed objective.
- Common heuristics: harvest shared ingredients before queueing, keep the axe
  active for its counted rows, redeem green entries immediately and follow the
  authoritative marker instead of searching the whole map.
- Failure attribution: missing counts, recipe ingredients, queue state,
  equipment slot, unredeemed row, absent group readiness, route marker and
  active quest distinguish the local failure causes.
- Player-trust factors: the exact spawn and resource pose may vary, but the fixed
  Navezgane map, explicit counts, visible claims, generated destination marker
  and item reward make the terminal auditable.
- Claim IDs: `7DTD-004`–`7DTD-011`.

## Replay and variation

- What changes between sessions: Navezgane spawn point, nearby resource poses,
  incidental loot, hostile encounters, craft order and walking line.
- Randomness or procedural generation: the admitted Navezgane geography is
  shipped and fixed; only the selected spawn, local population and incidental
  state vary. Random Gen is excluded.
- Multiple viable strategies: ingredient and route order can change, but every
  challenge claim and trader-radius settlement remains mandatory.
- Typical replay motive: compare a safer collection order or faster walk while
  retaining the same system terminal. Later survival history is outside scope.
- Claim IDs: `7DTD-003`–`7DTD-010`.

## Adjacent systems and history

- Direct predecessors: historical Alpha and 1.x tutorial quests are excluded;
  the V3.2 challenge group and current `Journey to Settlement` data own this
  packet.
- Variants: Random Gen, custom Sandbox Options, multiplayer and later trader
  jobs can materially change world, risk and progression and are separate.
- Similar games: No Man's Sky shares taught gathering and personal crafting
  before a guided early destination; Don't Starve Together, Rust, Minecraft and
  Project Zomboid share embodied harvesting, inventory, crafting and live
  survival pressure.
- Important differences: the current Basics ledger exposes multiple
  independently redeemable requirements, makes the group reward itself issue a
  nearest-trader route, and ends at a spatial quest reward instead of ship
  repair, a time horizon, server wipe, boss ending or arbitrary survival day.
- Claim IDs: `7DTD-004`–`7DTD-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-402` | route, resource, recipe, equipment, row and reward |
| System Behaviour | `SYS-161`, `SYS-208`, `SYS-215`, `SYS-223`, `SYS-327`, `SYS-328`, `SYS-741` | finite sources, live survival/combat, craft queue and checklist settlement |
| Constraint | `CON-210`, `CON-281`, `CON-297`, `CON-496`, `CON-573` | capacity, viability, recipe, harvest and claim legality |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-132`, `INF-282` | carried, survival, local, map, recipe and challenge state |
| Objective | `OBJ-145` | claimed tutorial through retained trader-route reward |
| Time | `TIM-003` | continuously advancing local world |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `232` (`GAME-0001`–`GAME-0232`).
- Exact genome matches: none.
- Tied near matches: `GAME-0141` — Rust (`20 / 59 = 0.338983`).
- Supported combination subsets: `COMB-0231`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0141` — Rust | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `SYS-208`, `SYS-215`, `SYS-223`, `SYS-327`, `SYS-328`, `CON-210`, `CON-281`, `CON-297`, `INF-073`, `INF-075`, `INF-115`, `INF-128`, `INF-132`, `TIM-003` | Both join direct survival, resource extraction, personal crafting, equipment, durability, finite inventory, local combat information and live world pressure. Rust instead creates a procedural shared server world with respawn, construction privilege, research, upkeep, offline raiding and a scheduled wipe. This packet fixes shipped Navezgane, rejects respawn and stops when separately redeemed onboarding rows create and settle one retained trader route. | Near, `0.338983` |

### Preserved research notes

- New genes: `ACT-402`, `SYS-741`, `CON-573`, `INF-282`, `OBJ-145`.
- Reused genes: `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`,
  `ACT-199`, `SYS-161`, `SYS-208`, `SYS-215`, `SYS-223`, `SYS-327`,
  `SYS-328`, `CON-210`, `CON-281`, `CON-297`, `CON-496`, `INF-073`,
  `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-132` and `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: existing movement, harvesting, inventory crafting,
  equipment, survival, combat, capacity and route information retain portable
  boundaries. New records isolate manual challenge redemption, all-row group
  settlement, its claim legality, ledger information and the resulting
  onboarding-to-service objective.

## Taxonomy impact

- Registry changes: `ACT-402`, `SYS-741`, `CON-573`, `INF-282`, `OBJ-145`; no
  earlier reviewed signature or lifecycle changes.
- Revised portable wording: `ACT-199` now explicitly covers a compatible
  carried item regardless of whether it was found or crafted; its action
  boundary and all earlier signatures are unchanged.
- Taxonomy-change record: none.
- Candidate terms affected: challenge row, redeem, group completion, trader
  quest, nearest service destination and retained route reward.

## Negative results

- `SYS-213` and `SYS-326` are rejected: this packet uses shipped Navezgane,
  not a newly generated Random Gen world.
- `SYS-736` is rejected: the Basics ledger exposes independently completable
  rows, not one hidden future instruction advanced in a strict sequence.
- `SYS-216` is rejected: death ends evaluation instead of admitting respawn.
- Building, trader economy, trader jobs, Blood Moons, later challenges and
  long-world persistence are excluded rather than unioned into onboarding.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Поточний `V3.2.0 Stable` має групу
  `Basics of Survival`, де виконані вимоги треба окремо забрати, а повністю
  забрана група видає маршрут до найближчого торговця (`7DTD-001`,
  `7DTD-004`–`7DTD-007`).
- [Confirmed | Corroborated | High] `Journey to Settlement` завершується в
  позначеній зоні торговця й видає Stone Shovel, тому ранній пакет має
  системний позитивний terminal без довільної sandbox-зупинки (`7DTD-007`,
  `7DTD-010`).

## Нові гени

- [Observation | Corroborated | High] `ACT-402`, `SYS-741`, `CON-573`,
  `INF-282`, `OBJ-145`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0231`.

## Зміни таксономії

- [Observation | Direct | High] Окремого taxonomy-change немає; попередні
  сигнатури й lifecycle не змінено, а `ACT-199` лише уточнено переносно.

## Нові питання

- Чи повторює інша survival-гра групову винагороду за окремо забрані навчальні
  вимоги, що сама створює просторовий маршрут до сервісного вузла?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0234` — Battlefield 2042.
- Optimisation criterion: перейти від одиночного survival onboarding до одного
  актуального звичайного Conquest ruleset від deployment до match settlement.
- Expected information gain: перевірити секторний контроль, tickets,
  розгортання й Specialist/loadout без Portal, Hazard Zone, events або всього
  live-service history.
- Backlog impact: продовжити активний Goal, не починаючи `GAME-0234` у цьому
  unit.

## Чому саме вона

- [Hypothesis | Limited | High] Це остання записана гра Batch 011 і навмисний
  контраст між позитивним навчальним маршрутом та багатокористувацьким
  командним матчевим terminal.
