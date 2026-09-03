---
game_id: GAME-0202
slug: naraka-bladepoint
game_title: "NARAKA: BLADEPOINT"
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0200
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-186
    - ACT-190
    - ACT-199
    - ACT-200
    - ACT-223
    - ACT-356
    - ACT-360
    - ACT-361
  system:
    - SYS-208
    - SYS-215
    - SYS-380
    - SYS-381
    - SYS-652
    - SYS-653
    - SYS-654
    - SYS-655
    - SYS-656
    - SYS-657
    - SYS-658
    - SYS-659
  constraint:
    - CON-262
    - CON-269
    - CON-284
    - CON-285
    - CON-286
    - CON-530
    - CON-531
    - CON-532
    - CON-533
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-127
    - INF-128
    - INF-129
    - INF-142
  objective:
    - OBJ-074
  time:
    - TIM-003
---

# Game: NARAKA: BLADEPOINT

## Analysis scope

- Version / ruleset: unmodified Windows Steam public build `24854623`, paired
  with official client `v3.0.2345` and the 2026-08-13 update, reviewed
  2026-08-31; one Survival `BOT Mode`, `Solo`, `Easy` match on the
  single-selected `Wanchu` map, with default free hero Viper Ning.
- Primary decision loop: choose a legal spawn region, search stochastic Stashes
  and ground loot for weapons, Souljades, armour, Grappling Hooks and recovery
  items, then repeatedly reposition, read attack cues, strike, Focus, Counter,
  dodge, grapple, cast Viper Ning's abilities, repair and recover while Shadow
  Corruption contracts the safe region and eliminations reduce the field.
- Entry and exit: entry is Viper Ning's first retained control at the selected
  Wanchu spawn after the preparation countdown. Exit is the complete Survival
  result after final elimination and placement, or the `Victory` / first-place
  result after every other participant is eliminated; stop before account
  rewards, quests, matchmaking or another match.
- Included: Easy BOT matchmaking and AI; Viper Ning with default `Yushan Strike`
  and `Moonbane Control`; spawn-point selection; sampled Wanchu loot; melee and
  ranged weapons; weapon durability and repair; armour and Health; Souljades;
  bag and equipment limits; Healing Berries, Armor Powder and Grappling Hooks;
  parkour, climbing and dodging; common attacks, Blue Focus Strikes, Counters,
  Clash and disarm; one Solo Rebirth; Shadow Corruption; participant count,
  final placement and the complete match result.
- Excluded: Ranked, Quick Match, Immortal War, Duos, Trios, Custom Room,
  Showdown, Rift Traversal and Casual modes; `Morus Isle`, `Holoroth`,
  `The Maelstrom` and rotating events; other heroes, skill variants and
  account-owned Glyph builds; purchases, cosmetics, Hero Cultivation, quests,
  ranks, Battle Pass, Justice Chamber and post-match account progression.
- Potential scoped modules: another hero kit, human Solo, team recovery, another
  Survival map, Showdown, Rift Traversal and temporary modes each require their
  own evidence and terminal contract.
- Direct-play status: no authenticated match was played. Current official patch,
  mode, map, free-roster and client pages establish the live packet; official
  guides and update notes establish the transitions. Steam depot state fixes
  the public build. The repository trace is rules reasoning, not claimed play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NAR-001` | Public Windows build `24854623` corresponds to official client `v3.0.2345` and the maintained 2026-08-13 rules | Confirmed | Corroborated | High | P1, P2, S1 |
| `NAR-002` | BOT Mode remains a Survival submode with difficulty and Solo selection; Wanchu remains individually selectable | Confirmed | Direct | High | P3, P4 |
| `NAR-003` | Viper Ning is playable on a new free account and has current `Yushan Strike` and `Moonbane Control` labels | Confirmed | Direct | High | P5, P6 |
| `NAR-004` | Preparation exposes hero, spawn-point and map screens before live control, while the match samples loot and AI state | Observation | Corroborated | High | P3, P7, P8 |
| `NAR-005` | Weapons, armour, Souljades, recovery items and Grappling Hooks form a capacity-bound match loadout | Observation | Corroborated | High | P8, P9, P10 |
| `NAR-006` | Grappling Hooks target terrain or opponents to close distance, climb or escape, consuming carried hook stock | Observation | Corroborated | High | P8, P11 |
| `NAR-007` | Melee play distinguishes common attacks, Blue Focus Strikes, Clashes, dodges and Counters that can disarm the attacker | Observation | Corroborated | High | P2, P7, P12 |
| `NAR-008` | Damage crosses armour and Health; consumables restore Health, armour or weapon durability through interruptible use | Observation | Corroborated | High | P9, P10, P13 |
| `NAR-009` | Shadow Corruption repeatedly contracts the safe region and damages participants who remain outside it | Confirmed | Direct | High | P3, P14 |
| `NAR-010` | Solo grants one Rebirth; after it is unavailable, elimination produces final placement and the complete result | Confirmed | Corroborated | High | P7, P15 |
| `NAR-011` | The last surviving Solo participant reaches the first-place Victory result | Confirmed | Corroborated | High | P15, P16 |

## Basic data

- Release / origin: 24 Entertainment / NetEase Games; Windows release 2021;
  free-to-play live service, reviewed at the 2026-08-13 client line.
- Platform or physical form: networked Windows PC client through Steam.
- Puzzle family: spawn-selected melee battle royale under contracting space.
- Primary sources:
  - **[P1]** [official 2026-08-13 update](https://www.narakathegame.com/news/update/20260803/33459_1309834.html),
    for the current update, combat, Easy Battle and Wanchu adjustments.
  - **[P2]** [official download page](https://www.narakathegame.com/download/),
    for client `v3.0.2345` and the 2026-08-13 package date.
  - **[P3]** [official 2026-07-02 update](https://www.narakathegame.com/news/update/20260622/33459_1304994.html),
    for BOT difficulties, Solo selection and Wanchu single selection.
  - **[P4]** [official 2026-06-05 update](https://www.narakathegame.com/news/update/20260527/33459_1301813.html),
    for current Easy Battle starting equipment and durability Omens.
  - **[P5]** [official free-to-play FAQ](https://www.narakathegame.com/news/guide/20230707/35647_1097069.html),
    for free modes, maps and Viper Ning's initial availability.
  - **[P6]** [official terminology update](https://www.narakathegame.com/news/update/20230626/33459_1095154.html),
    for Viper Ning's skill and ultimate plus recovery-item names.
  - **[P7]** [official preparation and BOT update](https://www.narakathegame.com/news/update/20231116/33459_1120384.html),
    for hero/spawn/map preparation screens and difficulty-aware Counters.
  - **[P8]** [official quick-start guide](https://www.narakathegame.com/guide/quickstart/),
    for Grappling Hooks, Souljades, Dark Tide Coins, vendors and mode framing.
  - **[P9]** [official armour update](https://www.narakathegame.com/news/update/20240329/33459_1146145.html),
    for armour capacity and Armor Powder restoration.
  - **[P10]** [official durability update](https://www.narakathegame.com/news/update/20251208/33459_1275244.html),
    for weapon Durability and its zero state.
  - **[P11]** [official accessibility guide](https://www.narakathegame.com/news/guide/20210810/35647_962135.html),
    for Grappling Hook aim/fire and melee targeting controls.
  - **[P12]** [official 2026-08-13 combat notes](https://www.narakathegame.com/news/update/20260803/33459_1309834.html),
    for charged strikes, Quick Counter and Counterstrike terminology.
  - **[P13]** [official 2026-04-16 update](https://www.narakathegame.com/news/update/20260407/33459_1294885.html),
    for recovery-item use restrictions and interruption state.
  - **[P14]** [official Solo update](https://www.narakathegame.com/news/update/20220627/33459_1026343.html),
    for one Rebirth and Shadow Corruption progression in Solo BOT Mode.
  - **[P15]** [official settlement update](https://www.narakathegame.com/news/update/20230103/33459_1061218.html),
    for Solo settlement statistics and the skippable post-win Victory screen.
  - **[P16]** [official Steam product page](https://store.steampowered.com/app/1203220/NARAKA_BLADEPOINT/),
    for Windows, developer/publisher, melee battle royale, combos, parries,
    Counters, parkour, Grappling Hooks, weapons and hero abilities.
- Secondary sources:
  - **[S1]** [SteamDB depot record](https://steamdb.info/app/1203220/depots/),
    observed 2026-08-31, for public build `24854623`, updated 2026-08-21.
- Claim IDs: `NAR-001`–`NAR-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate, climb and parkour; `ACT-161`,
  aim and attack; `ACT-164`, select a carried weapon or item; `ACT-183`, reload
  a ranged weapon; `ACT-186`, drop carried loot; `ACT-190`, cast Viper Ning's
  skill or ultimate; `ACT-199`, collect and equip loot; `ACT-200`, use an
  interruptible recovery or repair item; `ACT-223`, time a Counter against an
  executing Focus Strike; `ACT-356`, commit a freely timed directional dodge.
- New genes: `ACT-360`, choose one legal spawn region during preparation;
  `ACT-361`, aim and fire one carried Grappling Hook at terrain or a combatant.
- Parameters: spawn cell, movement surface, weapon, attack string, Focus charge,
  Counter timing, dodge direction, hook target, item, cast, ability and Rage.
- Claim IDs: `NAR-004`–`NAR-008`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged shots through cover and armour;
  `SYS-215`, resolve live hostile combat; `SYS-380`, resolve the typed effects
  of `Yushan Strike` and `Moonbane Control`; `SYS-381`, build and spend Rage for
  the ultimate.
- New genes: `SYS-652`, initialise a spawn-selected bot Survival match;
  `SYS-653`, resolve Grappling Hook travel and pull; `SYS-654`, resolve common,
  Focus, Clash and Counter relations; `SYS-655`, apply damage through armour
  before Health; `SYS-656`, consume, zero and restore weapon Durability;
  `SYS-657`, resolve recovery-item casts; `SYS-658`, contract Shadow Corruption
  and damage participants outside safety; `SYS-659`, route elimination through
  one available Rebirth or final placement and Victory settlement.
- Resolution order: fix hero, mode, difficulty and map; sample participants,
  spawn/loot and Easy Omens; commit a spawn; run continuous movement, search,
  combat and ability state; advance Shadow Corruption; route the first eligible
  elimination through Rebirth; settle later elimination or last survival.
- Parameters: AI difficulty, participant count, spawn and loot seed, weapon
  relation, armour/Health, Rage, ability, durability, cast, zone schedule,
  Rebirth availability, survivors, placement and result.
- Claim IDs: `NAR-002`–`NAR-011`.

### Constraint Genes

- Existing genes: `CON-262`, typed weapon, ammunition and item capacity;
  `CON-269`, skill/ultimate legality; `CON-284`, bag and equipment capacity;
  `CON-285`, compatible weapon and ammunition state; `CON-286`, uninterrupted
  recovery-item use.
- New genes: `CON-530`, one preparation spawn must fit the legal selectable
  region and current occupancy rules; `CON-531`, common, Focus and Counter
  inputs have mutually specific timing and weapon-state gates; `CON-532`, one
  Solo Rebirth must remain available and occur before its cutoff; `CON-533`, a
  Grappling Hook requires carried stock and a valid reachable anchor or target.
- Scarce strategic resources: safe-region travel time, Health, armour, weapon
  Durability, Rage, ability readiness, Grappling Hooks, recovery items,
  compatible loot capacity and the one Rebirth.
- Claim IDs: `NAR-004`–`NAR-010`.

### Information Genes

- `INF-073` exposes active weapons and items; `INF-115` limits remote opponents
  to local sight and sound; `INF-119` exposes Health, armour, Rage, ability and
  recovery resources; `INF-127` exposes spawn and Shadow Corruption map state;
  `INF-128` exposes loot identity, quality and bag compatibility; `INF-129`
  exposes survivor count, eliminations, placement and result; `INF-142` exposes
  the animation, colour and sound cues needed for dodge and Counter timing.
- Candidate genes: none.
- Claim IDs: `NAR-004`–`NAR-011`.

### Objective Genes

- Existing gene: `OBJ-074`, remain the last living Solo participant.
- Success, evaluation and failure: first place and `Victory` satisfy the
  objective; final elimination after Rebirth is unavailable ends the attempt
  and records placement. Kills, loot, Souljades and survival time do not
  independently satisfy the objective.
- Claim IDs: `NAR-010`, `NAR-011`.

### Time Genes

- Existing gene: `TIM-003`, live input under combat, ability, recovery,
  durability, AI and Shadow Corruption clocks without tactical pause.
- Candidate genes: none.
- Claim IDs: `NAR-006`–`NAR-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Viper Ning, Easy BOT Solo and Wanchu are fixed in preparation | Select one legal spawn region and let the countdown finish | The match instantiates Viper Ning at the committed region with sampled bots, loot and Easy Omen state | reproducible entry and bounded random initialisation | `NAR-002`, `NAR-004` |
| A reachable Stash contains compatible equipment | Open it, transfer one weapon, armour, Souljade and supplies | Capacity accepts legal items, equips chosen slots and leaves rejected excess outside | match-local build and capacity | `NAR-005` |
| One Grappling Hook remains and a wall or opponent is valid | Aim and fire the hook | The hook consumes stock, attaches and pulls Viper Ning toward the target until collision, release or arrival | consumable vertical and combat traversal | `NAR-006` |
| An opponent begins a Blue Focus Strike | Commit Counter inside the valid window | A successful Counter defeats the Focus relation, disarms the weapon and exposes a Counterstrike; mistiming leaves Viper Ning vulnerable | core melee counterplay | `NAR-007` |
| Viper Ning has missing Health, armour or weapon Durability | Channel the matching carried recovery item | Completion consumes the item and restores its declared meter; sprint, attack, damage or another cancelling state prevents completion | live repair opportunity cost | `NAR-008` |
| A new safe region is shown beyond Viper Ning | Rotate late or continue searching | Shadow Corruption contracts on schedule and drains survival state outside safety until entry, recovery or elimination | forced spatial deadline | `NAR-009` |
| Viper Ning is eliminated while the one Solo Rebirth remains legal | Accept Rebirth and choose the allowed return | Rebirth is consumed and live control returns; later elimination cannot use the same allowance | recoverable first elimination | `NAR-010` |
| Two participants remain and Viper Ning wins the final exchange | Deliver legal lethal damage and survive settlement | Survivor count reaches one, first place and Victory are displayed, and the bounded match closes | positive terminal | `NAR-011` |

## Strategic and experiential structure

- Local decision: decide whether the visible strike permits dodge, Clash,
  Counter, skill interruption or disengagement, and whether recovery or looting
  is safe before the opponent or zone closes the window.
- Medium-term planning: turn the selected spawn into a compatible melee weapon,
  armour, recovery reserve, Souljades and Grappling Hook route before the next
  Shadow Corruption deadline.
- Long-term structure: preserve Rebirth, armour, Durability and hooks while
  rotating toward safety, then convert fewer survivors into a final melee
  information contest rather than chasing every elimination.
- Common heuristics: avoid duplicate overcapacity loot, keep at least one hook
  for vertical escape, do not Counter ordinary attacks, repair before zero
  Durability and rotate before the safe boundary removes climbable approaches.
- Failure attribution: colour/animation cues, armour/Health, Durability, hook
  count, ability/Rage, map boundary, Rebirth state, survivor count and result
  distinguish timing, resource, route and final-combat failures.
- Player-trust factors: exact future loot and bot choices remain hidden; legal
  spawn, current equipment, attack cues, zone, Rebirth and terminal placement
  must remain legible.
- Claim IDs: `NAR-004`–`NAR-011`.

## Replay and variation

- What changes between sessions: spawn competition, bots, Easy Omen, Stash and
  ground loot, weapon/Souljade build, encounters and safe-region sequence.
- Randomness or procedural generation: authored Wanchu geometry receives
  bounded match-local participant, loot and zone samples.
- Multiple viable strategies: early or remote spawn, melee or mixed-range kit,
  pursuit or concealment, aggressive Counter pressure or hook-led disengagement.
- Typical replay motive: improve reading of the melee relation, looting speed,
  vertical rotation and Rebirth preservation under new samples.
- Claim IDs: `NAR-004`–`NAR-011`.

## Adjacent systems and history

- Direct predecessors: battle-royale survival and melee fighting lineages; this
  record does not assign unreviewed predecessor mechanics.
- Variants: human Quick Match changes opponent policy; Duos/Trios add team
  recovery; other maps and heroes change traversal, loot and ability state.
- Similar games: PUBG shares sampled loot, capacity, ranged combat, shrinking
  safety and Solo survival; Apex Legends shares hero abilities, armour and Ring
  pressure; Brawlhalla shares dodge/counter timing; Black Myth: Wukong shares
  live melee reads, healing and ability readiness.
- Important differences: the packet begins with a direct spawn-region choice,
  makes consumable grappling part of both travel and engagement, centres the
  common/Focus/Counter relation, permits exactly one Solo Rebirth and settles
  all of it within one bot-filled Survival result.
- Claim IDs: `NAR-002`–`NAR-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-186`, `ACT-190`, `ACT-199`, `ACT-200`, `ACT-223`, `ACT-356`, `ACT-360`, `ACT-361` | exact controls, weapons and spawn cell are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-380`, `SYS-381`, `SYS-652`–`SYS-659` | AI, loot and numeric effects are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-284`–`CON-286`, `CON-530`–`CON-533` | capacities, timing windows and cutoff are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-127`–`INF-129`, `INF-142` | visual styling and exact values are presentation |
| Objective | `OBJ-074` | participant count is a parameter |
| Time | `TIM-003` | cast, cooldown and zone durations are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `201` (`GAME-0001`–`GAME-0201`).
- Exact genome matches: none.
- Tied near matches: `GAME-0154` — Apex Legends (`23 / 70 = 0.328571`).
- Supported combination subsets: `COMB-0200`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0154` — Apex Legends | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-199`, `ACT-200`, `SYS-208`, `SYS-215`, `SYS-380`, `CON-262`, `CON-269`, `CON-284`, `CON-285`, `CON-286`, `INF-073`, `INF-115`, `INF-119`, `INF-127`, `INF-128`, `INF-129`, `TIM-003` | Both build a random match loadout around hero abilities, armour, live combat, bounded local information and a shrinking safe region. Apex uses a three-person squad, dropship insertion, attachments, downing, revival and banner/Core return before a last-squad terminal; NARAKA commits a ground spawn, consumes hooks, resolves common/Focus/Counter melee, repairs weapon Durability and gives one Solo Rebirth before placement or last-survivor Victory | Near, `0.328571` |

### Preserved research notes

- New genes: `ACT-360`, `ACT-361`, `SYS-652`–`SYS-659` and `CON-530`–`CON-533`.
- Reused genes: 28 existing action, combat, inventory, ability, information,
  objective and real-time boundaries; no earlier signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing battle-royale and live-combat genes preserve
  genuine reuse. Spawn selection, hook pull, Focus/Counter resolution, weapon
  Durability, one Rebirth and the NARAKA result boundary remain distinct.

## Taxonomy impact

- Registry changes: fourteen bounded Active genes and `COMB-0200`; reuse and
  evidence extensions do not change any earlier reviewed signature.
- Taxonomy-change record: none.
- Candidate terms affected: spawn contention, neutral attack, Blue Focus,
  Counter, Clash, Souljade, Shadow Corruption and Rebirth.

## Negative results

- `Wanchu` is used because the current official rotation allows its individual
  selection; `Morus Isle` no longer satisfies that reproducibility boundary.
- One available Rebirth prevents reuse of PUBG's permanent-first-death rule;
  final elimination is modelled only after that allowance is unavailable.
- Easy Omens, bot behaviour, loot and zone samples are parameters inside one
  ruleset, not a union of difficulties, maps or rotating modes.
- No earlier verified combination was accepted from genre resemblance; the
  proper-subset scan remains validator-owned.
