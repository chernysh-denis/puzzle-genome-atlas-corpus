---
game_id: GAME-0201
slug: payday-2
game_title: PAYDAY 2
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0199
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-190
    - ACT-199
    - ACT-241
    - ACT-341
    - ACT-358
    - ACT-359
  system:
    - SYS-208
    - SYS-215
    - SYS-348
    - SYS-373
    - SYS-618
    - SYS-645
    - SYS-646
    - SYS-647
    - SYS-648
    - SYS-649
    - SYS-650
    - SYS-651
  constraint:
    - CON-262
    - CON-269
    - CON-525
    - CON-526
    - CON-527
    - CON-528
    - CON-529
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-246
    - INF-256
    - INF-257
  objective:
    - OBJ-124
  time:
    - TIM-003
---

# Game: PAYDAY 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam client, official Update
  `247.2`, Diesel Engine v3.0, Steam public build `24811639`, built and updated
  `2026-08-19`, checked `2026-08-31`; Offline / Crime.net Offline, Normal,
  base-game one-day `Bank Heist: Cash`, controlling Dallas with three stock AI
  heisters.
- Declared loadout and account boundary: unmodified base-game AMCAR rifle,
  unmodified Chimano 88 pistol, Weapon Butt, Two-piece Suit and one Ammo Bag;
  no skills and no active perk-deck effects. The already available contract and
  equipment are entry predicates, not a claim about a fresh-profile unlock
  sequence. Team-AI boosts, abilities and alternate weapons are disabled.
- Primary decision loop: case the bank and read guards, civilians, cameras,
  vault, drill, van and team state; mask up and deliberately force the alarm;
  control and restrain one civilian; place, run and repair the thermal drill;
  move, aim, fire, reload, recover ammunition and revive or rely on stock bots
  while police cycle through control and assault pressure; bag, route and
  secure one required cash payload; converge on the escape and retain payout.
- Reproducible layout and action trace: restart before retained masked control
  until the legal sample has the vault door on the rear-office side of the fax
  room, the camera room behind the teller room and the escape van in the rear
  parking lot. Enter casing, inspect all three fixtures, mask up, fire one
  unsuppressed AMCAR shot to force loud, order one lobby civilian down and use
  one cable tie, place and assemble the thermal drill, repair every jam that
  occurs, survive until the vault opens, bag the first eligible cash bundle,
  carry or throw it to the rear van, secure it and enter the active escape.
  Jam timing, police composition, civilian path, bot choices, damage, loose
  cash and completion time remain recorded run parameters.
- Entry and exit: begins at first retained Dallas control in casing after the
  accepted layout loads. It ends only when at least one money bag is credited
  in the escape van, the eligible crew occupies the active escape, the contract
  declares success and the payout sequence records contract and loot value;
  stop before spending, skill allocation or another Crime.net contract.
- Included: casing and the one-way mask commitment; detection and deliberate
  alarm; civilians, finite cable ties, hostage retention and police rescue
  pressure; drill placement, autonomous progress, random jams and repair;
  AMCAR/Chimano combat, armour, health, incapacitation, bleed-out, bot revival,
  custody and legal stock-AI hostage return; control/anticipation/assault/fade
  cycling; Ammo Bag placement and ammunition pickup; cash bagging, exclusive
  carry, throwing, securing, one-bag escape gate and retained payout.
- Excluded: stealth completion, pager/body-bag optimisation and preplanning
  assets; every Bank Heist variant except Cash and every other job; online or
  local human co-op, matchmaking and drop-in; Hard and higher difficulties,
  One Down, Crime Spree and Holdout; DLC, community maps, mods, Workshop,
  cheats and exploits; alternate skills, perk decks, weapons, armour or Team-AI
  boosts; optional extra bags and deposit boxes; achievements, cards, Infamy,
  career/story progression, purchases and later account optimisation.
- Potential scoped modules: a declared stealth completion; a second legal
  layout sample; one human four-player crew; another difficulty; `Bank Heist:
  Gold` or `Deposit`; a multi-day job; Crime Spree or Holdout.
- Direct-play status: no fresh authenticated playthrough was conducted.
  Starbreeze's current update, product, original base-heist and official
  mechanics material establish the ruleset and phase vocabulary. Current depot
  state, independent Bank Heist references and a repository-side executable
  transition trace corroborate the exact layout, one-bag and terminal packet.
  The declared sampled trace is rules reasoning, not direct observation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PD2-001` | Update `247.2` and Steam public build `24811639` are the current unmodded Windows ruleset | Confirmed | Corroborated | High | P1, P2, S1 |
| `PD2-002` | `Bank Heist: Cash` is a base-game one-day job playable quietly or loud, and Offline fills the remaining crew with stock AI | Confirmed | Direct | High | P2, P3, P5 |
| `PD2-003` | Casing and detection precede an alarm boundary; the declared unsuppressed shot reproducibly commits the loud route | Observation | Corroborated | High | P2, P4, S2, V1 |
| `PD2-004` | A compliant civilian can be tied and moved as a hostage, while police pressure can rescue hostages and hostage state affects the response/trade loop | Confirmed | Corroborated | High | P4, P6, S4 |
| `PD2-005` | Bank Heist requires placing and assembling a thermal drill, waiting through its operation and repairing possible jams until the vault opens | Observation | Corroborated | High | P4, S2, S3 |
| `PD2-006` | After alarm, control and assault intervals alter police arrival and aggression while the drill and contract continue | Confirmed | Corroborated | High | P2, P4, S4 |
| `PD2-007` | Damage crosses armour, health, downing and possible custody; bots can revive and, with a legal hostage, return the human player from custody | Confirmed | Corroborated | High | P5, P6, S5, S6 |
| `PD2-008` | `Bank Heist: Cash` requires exactly one secured money bag for the minimum terminal, after which escape occupancy settles success | Confirmed | Corroborated | High | P3, S2, S3 |
| `PD2-009` | Cash becomes a dedicated heavy bag that can be carried or thrown and counts only in the escape van's secure region | Observation | Corroborated | High | P2, P4, S2, S3 |
| `PD2-010` | The result sequence exposes and retains contract and secured-loot payout while later career allocation remains separable | Observation | Corroborated | High | P2, S2, S7 |
| `PD2-011` | The accepted layout tuple and loud one-bag trace reach the bounded payout terminal without DLC, multiplayer or progression choices | Observation | Direct | High | V1 |

## Basic data

- Release / origin: OVERKILL Software / Starbreeze Studios; published by
  505 Games at the 2013 Windows release and maintained by Starbreeze.
- Platform or physical form: local unmodded Windows PC client, direct
  first-person control with three autonomous heister bots.
- Puzzle family: stealth-to-assault objective execution; interruptible fixture
  defence; civilian/hostage control; spatial loot routing; retained contract
  settlement.
- Primary sources:
  - **[P1]** [official Update 247.2 changelog](https://www.paydaythegame.com/news/payday2/2026/08/payday-2-update-247-2-changelog/),
    dated 2026-08-19, for the current update boundary, unmodded integrity note
    and absence of a Bank Heist rules change.
  - **[P2]** [official PAYDAY 2 product page](https://www.paydaythegame.com/payday2/),
    for quiet/loud bank robbery, police waves, cash escape, solo Offline and AI
    teammates; checked 2026-08-31.
  - **[P3]** [official original PAYDAY 2 beta inventory](https://www.paydaythegame.com/news/payday2/2013/07/the-payday-2-beta-is-live/),
    for `Bank Heist: Cash` as a one-day core job rather than DLC.
  - **[P4]** [official PAYDAY 2 mechanics curriculum](https://www.paydaythegame.com/news/payday2/2014/07/payday-2-community-tips-feature-volunteers-needed/),
    for casing, control/assault phases, loot securing, civilians, cable ties,
    custody, bleed-out, revival, drills, detection, equipment and armour.
  - **[P5]** [official Community Safe / Team AI update](https://www.paydaythegame.com/payday2/updates/communitysafe/),
    for stock AI following, holding and HUD armour/health feedback.
  - **[P6]** [official Crimefest 2015 update](https://www.paydaythegame.com/payday2/updates/crimefest2015/),
    for stock-AI hostage trade after custody and its control/assault timing.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB PAYDAY 2 depots](https://steamdb.info/app/218620/depots/),
    observed 2026-08-31, for Windows public build `24811639`, built and updated
    2026-08-19; official `P1` independently fixes the matching update.
  - **[S2]** [Payday Wiki — Bank Heist](https://payday.fandom.com/wiki/Bank_Heist),
    for one-day objectives, 360-second base drill, legal layout variants,
    Normal guard parameter, one required Cash bag and escape.
  - **[S3]** [Steam Community comprehensive beginner guide](https://steamcommunity.com/sharedfiles/filedetails/?id=336948956),
    for drill setup/defence, vault opening, money-bag carry and van securing.
  - **[S4]** [Payday Wiki — Assault Waves](https://payday.fandom.com/wiki/Assault_Waves),
    for alarm-triggered response phases, hostage timing and visible assault cues.
  - **[S5]** [Payday Wiki — Armors](https://payday.fandom.com/wiki/Armors),
    for armour-before-health application and timed armour regeneration.
  - **[S6]** [Payday Wiki — Police Custody](https://payday.fandom.com/wiki/Police_Custody),
    for repeated downing, custody, failure and legal AI-hostage return.
  - **[S7]** [official Steam product page](https://store.steampowered.com/app/218620/PAYDAY_2/),
    for Single-player support and the maintained base product boundary.
  - **[V1]** repository-side transition trace derived from `P1`–`P6` and
    `S1`–`S7`; executable rules reasoning, not direct play.
- Claim IDs: `PD2-001`–`PD2-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate Dallas; `ACT-161`, aim and attack with
  AMCAR, Chimano 88 or Weapon Butt; `ACT-164`, switch the active weapon or
  equipment slot; `ACT-183`, reload; `ACT-190`, deploy the Ammo Bag;
  `ACT-199`, collect compatible ammunition; `ACT-241`, revive a reachable
  downed bot; `ACT-341`, place, assemble and repair the authored thermal drill.
- New genes: `ACT-358`, intimidate, tie and reposition one civilian;
  `ACT-359`, bag, carry, throw and secure one heavy cash payload.
- Claim IDs: `PD2-003`–`PD2-009`.

### System Behaviour Genes

- `SYS-208` and `SYS-215` resolve firearm/melee effects and live police combat;
  `SYS-348` resolves armour, health, downing and revival; `SYS-373` turns local
  sight/sound suspicion into completed detection; `SYS-618` runs the three
  stock cooperative bots around Dallas.
- `SYS-645` commits completed detection or the declared shot into irreversible
  alarm; `SYS-646` maintains civilian compliance, restraint and police rescue;
  `SYS-647` advances the drill through possible jams and repair; `SYS-648`
  cycles police control and assault pressure; `SYS-649` crosses repeated
  downing into custody and legal hostage return.
- `SYS-650` converts vault cash into carried/thrown/secured loot credit;
  `SYS-651` settles the one-bag escape into retained payout.
- Resolution order: local casing information; mask and detection/alarm;
  civilian and drill interaction; continuous combat, bot and police response;
  vault opening; bag transport and secure credit; escape and payout settlement.
- Claim IDs: `PD2-003`–`PD2-011`.

### Constraint Genes

- `CON-262` bounds weapons, magazines, reserve ammunition and equipment stock;
  `CON-269` gates Ammo Bag deployment by the selected loadout, stock, surface
  and current body state.
- `CON-525` withholds overt heist actions in casing and makes mask commitment
  one-way; `CON-526` requires a live compliant civilian and one finite cable tie;
  `CON-527` requires live reach at the matching drill anchor; `CON-528` gives a
  money bag exclusive carriage and a compatible secure border; `CON-529`
  requires one secured Cash bag before the escape can settle.
- Scarce strategic resources: armour and health, down allowance, cable ties,
  hostage bodies, ammunition, Ammo Bag stock, drill access, control-phase time,
  bot availability and the required cash bag's route.
- Claim IDs: `PD2-003`–`PD2-009`.

### Information Genes

- `INF-073` exposes current weapons, magazines, reserve ammunition and
  equipment; `INF-115` exposes guards, police, civilians and their actions only
  through local sight, sound and effects; `INF-116` exposes bot state and shared
  objective progress; `INF-119` exposes armour, health and down/custody state.
- `INF-246` supplies automatic teammate-danger and incoming-assault cues;
  `INF-256` joins casing/detection, alarm phase, drill, hostage, secured-loot
  and escape feedback; `INF-257` exposes success and retained payout.
- Candidate genes: none.
- Claim IDs: `PD2-003`–`PD2-011`.

### Objective Genes

- `OBJ-124` requires opening the vault, securing at least one Bank Heist: Cash
  money bag and occupying the active escape to reach success/payout.
- Success, evaluation and failure: one secured bag plus legal escape is enough;
  optional bags improve payout but do not change success. All human control in
  custody with no legal AI-hostage return or abandoning/restarting before escape
  fails or leaves the bounded attempt incomplete.
- Claim IDs: `PD2-008`–`PD2-011`.

### Time Genes

- `TIM-003` advances detection, civilians, drill progress/jams, police phases,
  combat, armour recovery, bleed-out, custody and bot behaviour continuously
  without a tactical pause.
- Candidate genes: none.
- Claim IDs: `PD2-003`–`PD2-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Dallas has retained casing control in the accepted legal layout | Inspect the vault, camera room, van and nearby population without masking | Casing preserves limited actions while exposing the sampled fixture and detection state | bounded entry and layout parameter | `PD2-003`, `PD2-011` |
| Casing inspection is complete | Mask up and fire one unsuppressed AMCAR shot | Overt weapon fire commits alarm; the contract cannot return to unalerted casing and law response starts | reproducible stealth-to-loud transfer | `PD2-003` |
| One living lobby civilian is reachable and a cable tie remains | Shout until compliant, tie and move the civilian away from police access | One tie is consumed and the body enters retained hostage state until rescued or traded | embodied hostage resource | `PD2-004` |
| The matching vault anchor is reachable | Place, assemble and start the thermal drill; repair it whenever jammed | Progress advances only while operating and is retained across each repaired stop until the vault opens | interruptible autonomous objective | `PD2-005` |
| Alarm is active while the vault remains closed | Hold the bank through control, anticipation, assault and fade cues | Police density/aggression changes by phase while bots, damage and drill state continue | cyclical pressure around one objective | `PD2-006`, `PD2-007` |
| The vault is open and the first cash source is eligible | Bag it, carry or throw the bag to the rear van and deposit it | The payload alternates carrier/world state; van entry permanently increments secured Cash bags to one | spatial transport to objective credit | `PD2-008`, `PD2-009` |
| One required money bag is secured | Enter the active escape and accept the result sequence | The contract settles success and records contract/loot payout before later career choices | bounded positive terminal | `PD2-008`, `PD2-010`, `PD2-011` |

## Strategic and experiential structure

- Local decision: balance sightlines, civilian command, drill access, aimed
  fire, reload, ammunition recovery and bot rescue against the current police
  phase and the cash bag's location.
- Medium-term planning: place the hostage away from police access, preserve a
  defensible route between drill and Ammo Bag, repair during lower pressure and
  stage the single required bag toward the rear van.
- Long-term structure: convert casing knowledge into a deliberate loud plan,
  endure the complete vault delay, then stop greed after one secured bag and
  turn that credited value into a retained result.
- Common heuristics: do not fight indefinitely during assault; use cover until
  fade, repair promptly but not through lethal pressure, keep bots reachable,
  throw the bag across safe segments and leave as soon as the minimum terminal
  is open.
- Failure attribution: detection bars, alarm/assault banner, drill/jam prompt,
  team frames, armour/health, hostage and secured-bag cues distinguish reveal,
  machine neglect, combat collapse, rescued hostage and incomplete deposit.
- Player-trust factors: a detected overt action must not silently restore
  stealth; drill progress must survive a repaired jam; only van deposit may
  increment the bag requirement; payout must reflect the settled contract.
- Claim IDs: `PD2-003`–`PD2-011`.

## Replay and variation

- What changes between sessions: vault/camera-room/van placement, door and
  camera samples, guard/civilian paths, drill jams, police composition, bot
  decisions, damage, bag route and optional loot.
- Randomness or procedural generation: the accepted tuple bounds layout before
  retained control; later jam and response samples remain legal parameters.
- Multiple viable strategies: the broader job admits stealth, alternate
  equipment and extra loot, but this packet deliberately forces loud and one
  bag so every required system is exercised in one reproducible trace.
- Typical replay motive: improve drill defence and bag routing, preserve more
  hostages, take optional loot or compare another layout/difficulty module.
- Claim IDs: `PD2-003`–`PD2-010`.

## Adjacent systems and history

- Direct predecessor: PAYDAY: The Heist established four-player bank robbery,
  police assault phases, hostages, custody and secured loot.
- Variants: stealth changes detection and pager/body handling; higher
  difficulties change enemies, timing and down pressure; other jobs replace
  the drill, loot route and terminal dependency graph.
- Similar games: Left 4 Dead 2 shares one human with stock cooperative bots,
  real-time gun pressure, incapacitation and revival; Rainbow Six Siege shares
  information-sensitive breaching and objective interaction; GTA V shares
  authored heists and wanted combat but not this persistent drill/hostage/bag
  terminal.
- Important differences: enemies are not a finite clearance objective;
  survival exists to keep an autonomous drill and transported cash chain live,
  and one secured bag plus escape—not enemy defeat—settles success.
- Claim IDs: `PD2-002`–`PD2-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-199`, `ACT-241`, `ACT-341`, `ACT-358`, `ACT-359` | direct control, drill, civilian and bag operations |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-348`, `SYS-373`, `SYS-618`, `SYS-645`, `SYS-646`, `SYS-647`, `SYS-648`, `SYS-649`, `SYS-650`, `SYS-651` | detection, bots, hostage, drill, waves, custody, loot and payout |
| Constraint | `CON-262`, `CON-269`, `CON-525`, `CON-526`, `CON-527`, `CON-528`, `CON-529` | capacity, casing, reach, restraint, bag and escape gates |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-246`, `INF-256`, `INF-257` | local combat, team, heist phase and result cues |
| Objective | `OBJ-124` | open, secure one Cash bag and escape |
| Time | `TIM-003` | continuous drill, police, combat and custody time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `200` (`GAME-0001`–`GAME-0200`).
- Exact genome matches: none.
- Tied near matches: `GAME-0192` — Left 4 Dead 2 (`18 / 51 = 0.352941`).
- Supported combination subsets: `COMB-0199`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0192` — Left 4 Dead 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-241`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-348`, `SYS-618`, `CON-262`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-246`, `TIM-003` | Both put one controlled shooter beside three stock bots under live damage, down/revive pressure and partial team information. Left 4 Dead 2 routes a Survivor party through Director-selected threats and an authored panic event to collective safe-room closure; PAYDAY 2 makes casing/alarm irreversible, manages civilians as hostage resources, protects an interruptible drill, cycles police phases, transports one heavy cash bag and settles a retained payout | Near, `0.352941` |

### Preserved research notes

- New genes: `ACT-358`, `ACT-359`, `SYS-645`–`SYS-651`, `CON-525`–`CON-529`,
  `INF-256`, `INF-257` and `OBJ-124`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`,
  `ACT-199`, `ACT-241`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-348`,
  `SYS-373`, `SYS-618`, `CON-262`, `CON-269`, `INF-073`, `INF-115`,
  `INF-116`, `INF-119`, `INF-246` and `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the scope retains exactly one current base-game
  contract and one positive terminal. Optional stealth, loot and account layers
  do not expand the signature merely because they exist elsewhere in PAYDAY 2.

## Taxonomy impact

- Registry changes: seventeen new active genes; existing records gain PAYDAY 2
  evidence only where their definitions already admit the same boundary.
- Taxonomy-change record: none; no existing reviewed signature changed.
- Candidate terms affected: casing commitment, civilian hostage state,
  interruptible objective drill, cyclical assault pressure, custody trade,
  heavy-bag deposit and heist payout settlement.

## Negative results

- The random layout is a parameter, not a union of all Bank Heist maps. The
  accepted tuple and pre-control restart rule produce one repeatable sample.
- Optional extra bags are not a separate optimisation objective in this packet;
  one secured bag owns the positive terminal.
- Killing police is not a finite-clearance objective. It regulates survival and
  space while the drill, bag and escape chain remains primary.
- No earlier registered combination was assumed from genre resemblance; the
  exhaustive subset scan is validator-backed.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Поточний `Bank Heist: Cash` поєднує
  незворотний перехід від розвідки до тривоги, заручника, бур, хвилі поліції,
  просторове перенесення однієї сумки та втечу з виплатою (`PD2-001`–`PD2-011`).

## Нові гени

- [Observation | Corroborated | High] `ACT-358`, `ACT-359`, `SYS-645`–`SYS-651`,
  `CON-525`–`CON-529`, `INF-256`, `INF-257`, `OBJ-124`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0199`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; підписи раніше
  рецензованих ігор не змінено.

## Нові питання

- Чи утворює окремий тихий прохід цього самого контракту повторювану комбінацію
  керування підозрою, пейджерами та мішками без циклу поліцейських штурмів?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] NARAKA: BLADEPOINT.
- Optimisation criterion: contrast one bot-supported objective heist with a
  current solo battle-royale melee survival terminal.
- Expected information gain: test weapon/ability mobility, parry interaction,
  shrinking space, revival and last-survivor settlement against the corpus.
- Backlog impact: continue the authorised demand-led Goal.

## Чому саме вона

- [Hypothesis | Limited | High] Це наступний записаний unit `GAME-0202`; він
  змінює і контрольовану групу, і структуру термінала після контрактної втечі.
