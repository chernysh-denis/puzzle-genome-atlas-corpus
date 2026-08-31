---
game_id: GAME-0194
slug: mount-and-blade-ii-bannerlord
game_title: "Mount & Blade II: Bannerlord"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0192
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-189
    - ACT-199
    - ACT-232
    - ACT-238
    - ACT-317
    - ACT-347
    - ACT-348
    - ACT-349
  system:
    - SYS-215
    - SYS-297
    - SYS-342
    - SYS-362
    - SYS-379
    - SYS-554
    - SYS-616
    - SYS-625
    - SYS-626
  constraint:
    - CON-269
    - CON-282
    - CON-284
    - CON-470
    - CON-514
  information:
    - INF-119
    - INF-125
    - INF-128
    - INF-248
    - INF-249
  objective:
    - OBJ-117
  time:
    - TIM-003
---

# Game: Mount & Blade II: Bannerlord

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam **Mount & Blade II:
  Bannerlord** base game, official stable `v1.4.8`, Steam public build
  `24573425`, checked 2026-08-29. The later `v1.5.0` announcement is an opt-in
  beta and is not the reviewed live branch.
- Reproducible start packet: fresh single-player `Campaign`, tutorial enabled,
  ordinary default difficulty and base-game modules only. Use an Empire
  culture character, otherwise fixed declared appearance/name and one fixed
  legal set of childhood, adolescence, youth and adult background answers;
  retain the resulting starting skills and equipment. Complete the training
  field only as far as required to continue, then begin the campaign tutorial.
- Reproducible route: travel to Tevea; recruit the maximum currently offered
  tutorial troops, buy the six available sacks of grain after speaking with
  Headman Deltisos, defeat the three marked six-raider parties with the fixed
  troop group ordered to charge while the avatar joins the fight, take all
  compatible loot and release ordinary prisoners, allow campaign time to heal
  if required, enter the revealed Radagos hideout, order the troop group to
  charge, clear every bandit group and choose **fight with the troops** rather
  than the optional solo duel. Confirm the declared family name, clan banner
  and colours after Radagos is defeated.
- Primary decision loop: inspect campaign quest, map, party speed, food,
  denars, troop count, health and equipment; commit a route, settlement
  recruitment/purchase or wait state; on hostile contact inspect terrain,
  troops and targets, choose formation/order, mount state, weapon, attack or
  directional block and resolve the real-time encounter; settle casualties,
  skills and loot back into the same party, then advance the next tutorial gate.
- Entry and exit: begins at the first retained character-configuration gate of
  a fresh Campaign. It succeeds only after Radagos and the remaining hideout
  bandits are defeated, the family/clan identity gate is confirmed, the
  tutorial closes and the same party reaches the first retained controllable
  campaign-map state. Merely revealing or entering the hideout, defeating the
  ordinary bandits or seeing the clan editor is not the terminal.
- Included: culture/background starting-state choices; campaign-map route and
  pause/play time; settlement recruitment and grain purchase; party food,
  denars, speed, troop count and health recovery; direct walking and riding;
  one-handed, shield and bow equipment present in the fixed packet; aimed live
  attacks and directional blocking; troop selection, charge, movement and
  formation orders; three raider encounters; casualties, skill-use progress,
  result, prisoners and loot; hideout scene; visible enemy highlighting; the
  troops-assisted Radagos confrontation; tutorial quest flags; family name,
  banner/colour confirmation and retained campaign return.
- Excluded: Sandbox mode; any campaign continuation after the first returned
  map state; `Rebuild Your Clan`, `Rescue Your Family`, Neretzes' Folly and
  every later quest; Galter's later hideout; kingdom, clan-tier, diplomacy,
  politics, trade profit, crafting, workshops, caravans, fiefs, sieges and
  large-army systems; companion recruitment; upgrading troops after results;
  keeping prisoners; the optional solo Radagos duel; death/permadeath options;
  War Sails and every DLC; `v1.5.0` beta; multiplayer, Custom Battle, mods,
  Workshop content, console commands, cheats, achievements and version history.
- Potential scoped modules: one separately fixed later campaign quest, one
  ordinary non-tutorial field battle, a siege, a kingdom-management interval,
  Sandbox, multiplayer or War Sails only after its own build, start packet,
  primary loop and positive terminal are declared.
- Direct-play status: no authenticated Windows Steam fresh Campaign was
  conducted. Current official patch/product and versioned TaleWorlds API
  documentation establish the live build, product mechanics and continued
  tutorial quest classes; a current independently maintained tutorial trace
  fixes the exact route and terminal. Repository transitions are rules
  reasoning, not captured direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BANNERLORD-001` | Stable base-game v1.4.8 / public build 24573425 is the reviewed live Windows branch, while v1.5.0 is beta-only | Confirmed | Corroborated | High | P1, P2, S1 |
| `BANNERLORD-002` | The product joins persistent character development and campaign travel to direct first/third-person fighting alongside commanded troops | Confirmed | Direct | High | P2 |
| `BANNERLORD-003` | Current v1.4.8 code documentation retains the TutorialPhase classes for recruitment, grain, village dialogue, travel, traveller rescue and finding the hideout | Confirmed | Direct | High | P3 |
| `BANNERLORD-004` | The current tutorial route recruits troops and grain at Tevea, then requires three marked raider-party victories before revealing Radagos's hideout | Observation | Corroborated | High | P3, S2 |
| `BANNERLORD-005` | Campaign time consumes party provisions and permits wounded-character recovery while the party remains a persistent map object | Observation | Corroborated | High | P2, S2 |
| `BANNERLORD-006` | Each declared contact expands the campaign party into real-time avatar-plus-troop combat and returns casualties, prisoners, loot and progression to the party | Observation | Corroborated | High | P2, S2 |
| `BANNERLORD-007` | The avatar can directly ride and fight while issuing group charge, movement and formation orders to surviving troops | Confirmed | Corroborated | High | P2, S2 |
| `BANNERLORD-008` | Weapon attack direction and matching block direction materially mediate the scoped real-time melee exchange | Confirmed | Direct | High | P2 |
| `BANNERLORD-009` | `FindHideoutTutorialQuest` remains present in v1.4.8 and distinguishes `Victory` from `Retreated` and `Defeated` | Confirmed | Direct | High | P4 |
| `BANNERLORD-010` | After the hideout groups, the player may choose troops-assisted combat or a solo duel with Radagos; this trace fixes troops-assisted combat | Observation | Corroborated | High | S2 |
| `BANNERLORD-011` | Radagos victory followed by family name, banner and colour confirmation closes the tutorial into retained Campaign state | Observation | Corroborated | High | P4, S2 |
| `BANNERLORD-012` | The repository trace reproduces recruitment, provisions, campaign/battle transfer, direct and group combat, loot and tutorial settlement without claiming later campaign systems | Observation | Direct | High | P1–P4, S1–S2, V1 |

## Basic data

- Release / origin: developed and published by TaleWorlds Entertainment;
  released for Windows in 2022 and maintained through the stable 2026 base-game
  patch reviewed here.
- Platform or physical form: one unmodded single-player Windows Steam Campaign;
  campaign time and menus surround separate real-time field/hideout scenes.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; inventory and resource conversion; ordered
  dependency sequencing.
- Primary sources:
  - **[P1]** [official BL v1.4.8 patch announcement](https://store.steampowered.com/news/posts/?appids=261550),
    dated 2026-08-10, for stable base-game `v1.4.8`, its separation from War
    Sails and the current official patch boundary; the same feed marks later
    `v1.5.0` as beta.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/),
    for the official title, Windows Campaign product, character development,
    riding, recruitment, army command, first/third-person real-time battles and
    skill-based directional combat.
  - **[P3]** [official v1.4.8 TutorialPhase API namespace](https://apidoc.bannerlord.com/v/1.4.8/namespace_story_mode_1_1_quests_1_1_tutorial_phase.html),
    for the current `RecruitTroops`, `PurchaseGrain`, `TalkToTheHeadman`,
    `TravelToVillage`, `LocateAndRescueTraveller` and `FindHideout` tutorial
    quest classes.
  - **[P4]** [official v1.4.8 FindHideoutTutorialQuest API reference](https://apidoc.bannerlord.com/v/1.4.8/class_story_mode_1_1_quests_1_1_tutorial_phase_1_1_find_hideout_tutorial_quest.html),
    for the hideout quest object, retained quest lifecycle and explicit
    `None`, `Retreated`, `Defeated`, `Victory` battle-end states.
- Secondary and reproducible sources:
  - **[S1]** [current public-branch build metadata](https://api.steamcmd.net/v1/info/261550),
    for Steam public build `24573425`, built 2026-08-05 and published
    2026-08-10; used only for the build identifier and timestamps.
  - **[S2]** [current maintained Tutorial 2 route](https://www.ludo.guide/guide/mount-and-blade-ii-bannerlord/campaign/tutorial),
    updated 2026-06-02, for Tevea, six grain, maximum recruits, three
    six-raider parties, charge orders, post-battle settlement, hideout reveal,
    healing through campaign time, bandit groups, the Radagos choice and the
    family/clan identity terminal.
  - **[V1]** repository-side transition trace derived from `P1`–`P4` and
    `S1`–`S2`; executable rules reasoning, not direct play.
- Claim IDs: `BANNERLORD-001`–`BANNERLORD-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly move the avatar on foot through field and
  hideout space; `ACT-161`, aim and commit the current melee or ranged attack;
  `ACT-189`, issue the campaign party or selected troop group a destination,
  attack or charge order; `ACT-199`, transfer and equip compatible battle loot;
  `ACT-232`, commit the headman and Radagos quest responses; `ACT-238`, confirm
  the fixed culture/background capability packet; `ACT-317`, set the selected
  troop group's formation and stance.
- New genes: `ACT-347`, hire available settlement recruits into the persistent
  party; `ACT-348`, mount, directly steer and dismount an available battle
  horse; `ACT-349`, hold a weapon or shield block toward one incoming attack
  direction.
- Parameters: character packet, campaign route, settlement, recruit, denars,
  party capacity, troop group, order, formation, horse, weapon, attack target,
  attack direction, block direction, dialogue response, loot and equipment.
- Claim IDs: `BANNERLORD-002`–`BANNERLORD-008`, `BANNERLORD-010`–`BANNERLORD-012`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded avatar combat;
  `SYS-297`, execute the party/troop group's ordered path and target
  acquisition; `SYS-342`, add eligible use progress to matching personal
  skills; `SYS-362`, award bounded encounter loot and progression; `SYS-379`,
  retain tutorial flags across dialogue, map and hideout gates; `SYS-554`, move
  ordered troops through the chosen formation; `SYS-616`, instantiate each
  campaign contact as a battle and return survivors, casualties, rewards and
  result to the campaign party.
- New genes: `SYS-625`, resolve attack direction against weapon/shield block
  direction into deflection or health damage; `SYS-626`, consume party food and
  advance wounded-character recovery while campaign time runs.
- Resolution order: campaign commands advance the party and time; food and
  health update; settlement commitments change party inventory/roster; hostile
  contact instantiates the participating bodies and terrain; direct and troop
  commands resolve in real time; battle settlement returns casualties, loot,
  skill and quest state; final hideout victory opens clan identity and retained
  campaign control.
- Claim IDs: `BANNERLORD-004`–`BANNERLORD-012`.

### Constraint Genes

- Existing genes: `CON-269`, attacks and orders require compatible equipment,
  target, reach and live readiness; `CON-282`, every tutorial encounter
  requires its authored predecessor, location and party state; `CON-284`,
  carried loot obeys inventory capacity and compatible equipment slots;
  `CON-470`, troop-group movement and attacks obey terrain, formation space,
  visibility and weapon range.
- New gene: `CON-514`, hiring requires an available settlement recruit, enough
  denars and free party capacity.
- Scarce strategic resources: denars, recruit availability, party slots, food,
  campaign time, avatar/troop health, living troop count, horse availability,
  equipment, attack range and valid tutorial flags.
- Claim IDs: `BANNERLORD-004`–`BANNERLORD-010`.

### Information Genes

- Existing genes: `INF-119`, expose avatar health, equipment and learned skill
  state; `INF-125`, expose the campaign map, marked raider/hideout destinations
  and current tutorial instruction; `INF-128`, expose loot identity, equipment
  compatibility and carried state.
- New genes: `INF-248`, expose campaign party speed, denars, food, roster,
  health and current settlement/quest state; `INF-249`, expose selected troop
  group, formation, current order, casualties, visible hostiles and direct
  combat cues during a field or hideout battle.
- Claim IDs: `BANNERLORD-004`–`BANNERLORD-012`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-117`, complete the first Radagos tutorial hideout and confirm
  family/clan identity into retained Campaign control.
- Success, evaluation and failure: success requires `Victory`, the identity
  confirmation and returned campaign state. Retreat, defeat, abandoning the
  Campaign or stopping before the clan gate fails this trace; a wounded avatar
  may recover on the map and failed optional-duel logic is excluded by fixing
  the troops-assisted choice.
- Claim IDs: `BANNERLORD-003`–`BANNERLORD-004`, `BANNERLORD-009`–`BANNERLORD-012`.

### Time Genes

- Existing gene: `TIM-003`, campaign recovery/provision time and battle motion,
  attacks and troop orders advance continuously while unpaused; compatible
  menus and pause state suspend the relevant live layer.
- New genes: none.
- Claim IDs: `BANNERLORD-005`–`BANNERLORD-008`, `BANNERLORD-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Stable v1.4.8 client is at the main menu | Start fresh Campaign with tutorial and the declared defaults | The current base-game Campaign opens its mandatory character packet without War Sails, mods or beta code | exact live entry | `BANNERLORD-001`–`BANNERLORD-003` |
| Character packet is open | Confirm Empire culture and the declared background answers | Starting skills/equipment persist and the training/campaign tutorial becomes available | character configuration is causal | `BANNERLORD-002`, `BANNERLORD-012` |
| First campaign control is retained | Select Tevea and let campaign time run | The party routes to the village while food/health and map time advance | strategic travel and provisions share time | `BANNERLORD-004`, `BANNERLORD-005` |
| Tevea exposes recruits and trade | Hire the maximum offered troops and buy the six tutorial grain after speaking with Deltisos | Denars and offer capacity decrease; roster and food inventory increase; the raider objective becomes current | settlement state prepares combat | `BANNERLORD-004` |
| A marked six-raider party is reachable | Commit contact | Campaign bodies and local terrain instantiate a live battle with returned party state pending | campaign-to-battle boundary | `BANNERLORD-006` |
| Troops await an order | Select the group, set the declared formation and order charge | Surviving troops form, path and acquire legal hostile targets while remaining independently damageable | direct group authority | `BANNERLORD-007` |
| Avatar is mounted or beside an available horse | Mount, steer, strike and dismount as required | Horse motion changes reach/speed while the same avatar remains the direct combatant | riding is embodied, not a map token | `BANNERLORD-002`, `BANNERLORD-007` |
| An enemy attack direction is readable | Hold the matching weapon/shield block direction | Correct opposed geometry deflects the eligible strike; mismatch permits the attack to damage health | directional defence is mechanical | `BANNERLORD-008` |
| Raider party is defeated | Settle result, release ordinary prisoners and take all compatible loot | Casualties, skills, loot and quest progress return to the persistent party | battle consequences cross layers | `BANNERLORD-006` |
| Three marked parties have settled | Resolve the tutorial prisoner dialogue | Radagos's hideout is revealed as the next authored map gate | victories unlock the hideout | `BANNERLORD-004`, `BANNERLORD-009` |
| Party health is below the desired state | Run campaign time before entering the hideout | Food is consumed and eligible wounded health advances toward recovery | recovery competes with provisions | `BANNERLORD-005` |
| Revealed hideout is entered | Order troops to charge and clear every bandit group | Group and direct combat settle until the Radagos confrontation response appears | authored instance retains party command | `BANNERLORD-007`, `BANNERLORD-009` |
| Radagos offers the terminal combat choice | Choose to fight with the troops and win | The quest records `Victory` and advances to family/clan identity | fixed branch avoids duel ambiguity | `BANNERLORD-009`, `BANNERLORD-010` |
| Family/clan identity gate is active | Confirm declared family name, banner and colours | Tutorial closes and the same party regains first retained Campaign-map control | positive bounded terminal | `BANNERLORD-011`, `BANNERLORD-012` |

## Strategic and experiential structure

- Local decision: choose campaign destination or time state; inspect recruit,
  food and loot offers; select troop group, formation and order; mount or
  dismount; aim an attack or align the current directional block.
- Medium-term planning: buy enough grain and recruits before repeated contacts,
  preserve troop bodies across three fights, accept campaign-time food cost to
  recover health and enter the hideout with a viable commanded group.
- Long-term structure: convert one configured persistent character into a
  provisioned party, settle repeated campaign contacts into retained state and
  use the resulting group to complete the first hideout and clan identity gate.
- Common heuristics: recruit before pursuing marks; retain grain; avoid solo
  overextension; issue charge only after confirming the intended group; join
  troop pressure from a safe flank; block toward the visible attack; recover
  before the hideout; verify clan confirmation rather than stopping at victory.
- Failure attribution: insufficient denars/capacity, depleted food, wrong map
  target, missing troop order, blocked path, unmatched guard direction,
  casualty attrition, unresolved bandit group, wrong Radagos response or
  premature terminal remain distinguishable.
- Player-trust factors: visible route markers, party values, recruit/loot
  offers, formation/order feedback, attack animations, result screens and
  explicit tutorial/clan transitions connect every decision to retained state.
- Claim IDs: `BANNERLORD-004`–`BANNERLORD-012`.

## Replay and variation

- What changes between sessions: culture/background packet, appearance,
  training use, exact recruit offer, route timing, damage, riding, formation,
  attack direction, loot, prisoners, casualties and Radagos response. The
  canonical trace fixes the capability packet and troops-assisted terminal.
- Randomness or procedural generation: early tutorial objectives and terminal
  are authored; combat timing, individual casualties and some reward details
  may vary without changing the rules or positive endpoint.
- Multiple viable strategies: direct melee, ranged attacks, mounted pressure
  and different troop formations can clear encounters; the optional solo duel
  is a valid variant but excluded from the canonical trace.
- Typical replay motive: test another culture/build or execute a lower-loss
  tutorial before continuing into the full campaign. Neither continuation nor
  another build is part of this unit.
- Claim IDs: `BANNERLORD-002`, `BANNERLORD-004`–`BANNERLORD-012`.

## Adjacent systems and history

- Direct predecessor: Mount & Blade: Warband establishes the series form but
  is not evidence for this v1.4.8 Campaign tutorial or current client.
- Variants: Sandbox, Custom Battle, multiplayer, War Sails, beta v1.5.0, mods,
  later quests and kingdom-scale systems require separate scope contracts.
- Similar games: Skyrim Special Edition shares persistent character creation,
  direct movement/combat, equipment, skill-use progress, quest gates and an
  opening tutorial that returns open-world control; Total War: WARHAMMER III
  shares campaign contact, group orders, formation movement, real-time battle
  and returned casualties; XCOM 2 shares a bounded persistent troop roster and
  mission casualties but uses personal turn authority rather than live command.
- Important differences: Bannerlord puts the same player inside the live fight
  while also commanding recruited troops, uses provisions and healing on a
  continuous campaign map and resolves directional weapon defence before each
  battle returns its survivors and loot to the party.
- Claim IDs: `BANNERLORD-002`–`BANNERLORD-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-189`, `ACT-199`, `ACT-232`, `ACT-238`, `ACT-317`, `ACT-347`–`ACT-349` | exact background, route, recruit, formation, weapon, horse and response |
| System Behaviour | `SYS-215`, `SYS-297`, `SYS-342`, `SYS-362`, `SYS-379`, `SYS-554`, `SYS-616`, `SYS-625`, `SYS-626` | pathing, combat, skill, loot, quest, formation, cross-layer, direction and provisions |
| Constraint | `CON-269`, `CON-282`, `CON-284`, `CON-470`, `CON-514` | equipment, authored gates, capacity, terrain/range and recruitment legality |
| Information | `INF-119`, `INF-125`, `INF-128`, `INF-248`, `INF-249` | personal, campaign, loot, party and battle-command state |
| Objective | `OBJ-117` | Radagos victory plus clan confirmation and retained return |
| Time | `TIM-003` | pausable continuous campaign and battle time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `193` (`GAME-0001`–`GAME-0193`).
- Exact genome matches: none.
- Tied near matches: `GAME-0190` — The Elder Scrolls V: Skyrim Special Edition (`12 / 46 = 0.260870`).
- Supported combination subsets: `COMB-0192`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0190` — The Elder Scrolls V: Skyrim Special Edition | `ACT-008`, `ACT-161`, `ACT-199`, `SYS-215`, `SYS-342`, `SYS-379`, `CON-269`, `CON-282`, `INF-119`, `INF-125`, `INF-128`, `TIM-003` | both begin with a configured persistent character and carry direct movement, equipment, live combat, skill use and ordered quest gates into retained campaign control; Skyrim fixes one authored escort through perception, magic, lock and save/reload dependencies, while Bannerlord buys a provisioned troop roster, rides an available battle horse, combines aimed directional defence with live formation orders, transfers casualties and loot through repeated campaign contacts and stops only after the Radagos victory plus clan-identity gate | Near, `0.260870` |

### Preserved research notes

- New genes: `ACT-347`–`ACT-349`, `SYS-625`, `SYS-626`, `CON-514`,
  `INF-248`, `INF-249` and `OBJ-117`.
- Classification result: `New gene`, supported reuse and a new verified
  interaction combination.
- Evidence and reasoning: campaign travel, direct combat, group pathing,
  formations, inventory, quest progress, skill use and battle/campaign transfer
  reuse lower-ID boundaries. Instant settlement recruitment, non-persistent
  battle-horse control, opposed directional block, party provision/recovery,
  combined party/command information and the Radagos-clan terminal do not.

## Combination status

- `COMB-0192` is a verified strict subset of this genome, coupling campaign
  recruitment and provisions to direct-plus-commanded live combat, retained
  battle settlement and the Radagos/clan terminal.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: nine new Active genes, `COMB-0192` and five existing family
  memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. Reused definitions retain their prior boundaries.
- Candidate terms affected: recruit, grain, charge, hideout, Radagos and clan
  banner are game-specific parameters inside the isolated genes.

## Negative results

- `ACT-271`, `SYS-471`–`SYS-473` and `INF-181` are not reused: Bannerlord's
  scoped battle horse is an available mount rather than Red Dead Redemption 2's
  called persistent individual with saddle cargo, bond and core meters.
- `SYS-614` and `CON-509` are not reused: Bannerlord's party traverses a
  continuous pausable campaign map rather than spending a faction-turn movement
  allowance.
- `SYS-617` and `INF-245` are not required: morale/routing and regiment-model
  information are not necessary to reproduce the small tutorial encounters.
- `CON-323` is not reused: it fixes a small turn-based active-character party,
  not a Campaign troop roster whose battlefield formation depends on survivors.
- Broader clan, kingdom, economy, siege, War Sails and live-service history are
  rejected because none is causal to the declared tutorial terminal.

## Delta summary

## Нові факти

- [Confirmed/Observation | Direct/Corroborated | High] Stable v1.4.8 / build
  24573425 preserves a bounded Campaign tutorial from character setup through
  Tevea, three raider parties and Radagos to confirmed clan identity
  (`BANNERLORD-001`–`BANNERLORD-012`).

## Нові гени

- [Observation | Corroborated | High] Nine new genes isolate instant recruit
  hiring, available battle-horse control, directional weapon defence, party
  provisions/recovery, campaign/battle information and the exact positive
  tutorial terminal (`BANNERLORD-004`–`BANNERLORD-012`).

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0192` couples a provisioned recruited
  party to avatar-plus-formation combat and retained hideout settlement
  (`BANNERLORD-004`–`BANNERLORD-012`).

## Нові зв'язки

- [Observation | Corroborated | High] Skyrim Special Edition is the nearest
  lower-ID signature: both carry an opening RPG character through live combat
  and authored gates, while only Bannerlord adds recruits, provisions,
  formations and repeated campaign/battle return (`BANNERLORD-002`–`BANNERLORD-012`).

## Зміни таксономії

- [Observation | Corroborated | High] New bounded records extend the vocabulary
  without changing any prior reviewed signature or lifecycle record.
