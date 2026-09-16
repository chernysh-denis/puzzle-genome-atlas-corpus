---
game_id: GAME-0297
slug: monster-hunter-rise
game_title: 'MONSTER HUNTER RISE'
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-245
    - ACT-247
    - ACT-378
  system:
    - SYS-215
    - SYS-403
    - SYS-404
    - SYS-405
    - SYS-407
    - SYS-688
    - SYS-864
    - SYS-865
  constraint:
    - CON-210
    - CON-282
    - CON-354
    - CON-356
    - CON-358
    - CON-634
  information:
    - INF-073
    - INF-075
    - INF-125
    - INF-157
    - INF-339
    - INF-340
  objective:
    - OBJ-174
  time:
    - TIM-003
---

# Game: MONSTER HUNTER RISE

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1446780`, one-app base package `626191`, default public branch Build ID
  `17920865`, built 2025-03-31 and projected updated 2025-07-15; checked
  2026-09-13. Capcom's latest public gameplay patch in the located official
  notes is `Ver.16.0.2.0`, dated 2024-01-22. The later Valve build is retained
  as the distribution boundary without inferring an unsupported semantic
  version.
- Product boundary: Capcom's released Windows base game. MONSTER HUNTER RISE:
  SUNBREAK, every DLC/add-on content entitlement, beta branch, mod, Defender
  or Black Belt acceleration, platform achievement and cosmetic replacement
  are excluded.
- Platform, mode and setup: English Windows client, keyboard and mouse, fresh
  `New Game`, offline single-player Village Quests. Keep the supplied starter
  Palico and Palamute as the two Buddies and explicitly equip the base
  `Kamura Blade I` Long Sword with unupgraded starter armour. Do not claim the
  weapon was selected by default; the item-box choice is part of the setup.
- Entry and predecessor chain: first ordinary Kamura control after character,
  Palico and Palamute creation. Complete required training quest `Back to
  Basics`, then the two fixed one-star Village Key Quests `Fungal Frustrations`
  and `Roly-poly Lanterns`. Accept urgent Village Quest `Great Izuchi, Great
  Pain`, take only ordinary quest supplies and depart for Shrine Ruins.
- Primary decision loop: read the large-monster mark and route context, ride
  and directly steer the Palamute toward the target, dismount, then alternate
  positioning, Long Sword attacks, evasion and finite healing or stamina items.
  Spend individually recovering Wirebug units on one sheathed Wiredash, one
  weapon-drawn Silkbind and, after one eligible knockback, one Wirefall. Touch
  one reachable green Spiribird so its quest-duration health increase resolves
  under the equipped Petalace cap. Reacquire Great Izuchi after migration,
  sharpen during a safe interval and repeat while both Buddies act
  autonomously.
- Positive terminal: slay Great Izuchi before `50:00` or the third faint, use
  the post-completion window for at least one eligible carve, accept the
  result-screen materials and `900 z` reward, regain Kamura control and accept
  one manual save. A future direct reproduction must then quit and reload that
  save to confirm the retained result; this unavailable reload is not claimed
  as performed.
- Failure and asymmetry: time expiry or the third faint fails the quest. Each
  earlier faint returns the hunter to camp and consumes one allowance. Abandon
  reverts quest-acquired state, while `Return from Quest` retains eligible
  acquisitions but is not the positive hunt terminal.
- Included: mandatory opening progression; the chosen two gathering Key
  Quests; one solo urgent hunt; Long Sword attacks; health, stamina and
  sharpness; ordinary supplies; Wirebug Gauge, Wiredash, Silkbind and Wirefall;
  one wild Wirebug when reachable; one green Spiribird and Petalace cap;
  direct Palamute riding; autonomous Palico and Palamute support; visible
  large-monster map marks; migration, faint, carve, result settlement and
  manual save.
- Excluded: Hub, Join Request, multiplayer, Arena, Event and Rampage quests;
  capture, traps, tranq items and optional large-monster detours; Wyvern Riding,
  Great Wirebugs, Hunting Helpers and generated endemic-life dependence;
  forging, upgrading, later Village ranks, High Rank, Master Rank, Sunbreak,
  followers, anomaly/endgame systems, speedruns, mods, screenshots, official
  artwork, third-party images, video and audio.
- Reproducible parameterisation: install application `1446780` through package
  `626191` on public Build ID `17920865`; create one fresh English character
  and fixed starter Buddies; equip `Kamura Blade I`; complete the named
  training and two named gathering Key Quests; accept `Great Izuchi, Great
  Pain`; record the initial unknown or identified large-monster map mark,
  Wirebug units and Petalace state. During the hunt perform the three required
  Wirebug action classes, mount/dismount the Palamute, touch one green
  Spiribird, sharpen once after degradation and follow the target after one
  migration. Slay, carve, settle `900 z`, save in Kamura, reload and confirm
  the urgent completion. Route, damage, item consumption, target zones,
  migration timing, Wirefall-producing attack, rewards and terminal stocks are
  run parameters.
- Direct-play status: not conducted. No local Steam manifest, installation,
  executable, save or matching userdata was found. Valve fixes the application,
  package and public-build boundary. Capcom's maintained web manual and support
  pages establish Village isolation, quest rules, Wirebug actions, Palamute
  control, Buddies, endemic-life buffs, map disclosure and saving. Two
  independent written references corroborate the exact opening quest chain and
  first large-monster packet. This is an evidence-backed rules reconstruction,
  not a claimed playthrough, entitlement, save, terminal or reload. No
  audiovisual evidence was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MHR-001` | App `1446780` and package `626191` identify the Windows base game | Confirmed | Direct | High | P1 |
| `MHR-002` | Public Build ID `17920865` is the frozen distribution boundary; official gameplay notes identify `Ver.16.0.2.0` | Confirmed | Corroborated | High | P2, S1 |
| `MHR-003` | `Back to Basics` unlocks ★1 Village Quests; any two of three Key Quests unlock `Great Izuchi, Great Pain` | Observation | Corroborated | High | S2, S3 |
| `MHR-004` | Village Quests are solo-only, and a fresh character receives one Palico and one Palamute | Confirmed | Direct | High | P3, P4 |
| `MHR-005` | `Great Izuchi, Great Pain` targets Great Izuchi in Shrine Ruins with `50` minutes and `900 z` | Observation | Corroborated | High | S2, S3 |
| `MHR-006` | Sheathed Wirebug actions produce directional Wiredashes; drawn-weapon actions produce weapon-specific Silkbinds; Wirefall recovers from eligible knockback | Confirmed | Direct | High | P5 |
| `MHR-007` | Each Wirebug action consumes a variable gauge amount, exhausted units recover over time, and one wild Wirebug temporarily adds a unit | Confirmed | Direct | High | P5 |
| `MHR-008` | A Palamute can be called, mounted, steered, dashed and dismounted, including item or whetstone use while riding | Confirmed | Direct | High | P6 |
| `MHR-009` | Touching a green Spiribird raises maximum health for the quest up to the equipped Petalace's declared cap | Confirmed | Direct | High | P7 |
| `MHR-010` | Long Sword combat, supplies and whetstone maintenance resolve in real time while two Buddies independently follow, attack or gather | Confirmed | Direct | High | P4, P6, P8 |
| `MHR-011` | Time expiry or the third faint fails the quest; an earlier faint returns the hunter to camp | Confirmed | Corroborated | High | P3, S3 |
| `MHR-012` | Slay exposes carves; reward acceptance settles completion and Kamura permits a manual save | Confirmed | Direct | High | P3, P9 |
| `MHR-013` | No local install or save existed, so play, exact run values and reload are not claimed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: developed and published by CAPCOM Co., Ltd.; Windows
  release 2022-01-12.
- Platform or physical form: lawfully offered Windows Steam application
  `1446780`, base package `626191`; one fresh offline Village opening through
  the first urgent large-monster slay, settled reward and manual save.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1446780&cc=ua&l=english),
    for title, Windows platform, developer, publisher, release, base package
    and DLC-separated product boundary.
  - **[P2]** [official `Ver.16.0.2.0` update notes](https://store.steampowered.com/news/app/1446780/view/3970553140557253784),
    for Capcom's last located semantic gameplay patch in the base ruleset.
  - **[P3]** [Capcom manual: accepting and resolving quests](https://game.capcom.com/manual/Multi-Platform/en/windows/page/6/1),
    for Village isolation, objectives, time/faint failure, supplies, return,
    abandon, carving and reward settlement.
  - **[P4]** [Capcom manual: Palicoes and Palamutes](https://game.capcom.com/manual/Multi-Platform/en/windows/page/12/1),
    for fresh-character Buddies, quest assistance and autonomous actions.
  - **[P5]** [Capcom manual: Wirebug Actions](https://game.capcom.com/manual/Multi-Platform/en/windows/page/10/1),
    for Wiredash, Silkbind, Wirefall, gauge consumption, recharge and temporary
    wild-Wirebug capacity.
  - **[P6]** [Capcom manual: riding Palamutes](https://game.capcom.com/manual/Multi-Platform/en/windows/page/12/2),
    for call, mount, steering, dash, dismount and mounted item use.
  - **[P7]** [Capcom manual: Petalaces and Spiribirds](https://game.capcom.com/manual/Multi-Platform/en/windows/page/9/3),
    for touched Permabuffer statistics, quest lifetime and Petalace-specific
    increment and cap.
  - **[P8]** [Capcom manual: weapons and armour](https://game.capcom.com/manual/Multi-Platform/en/windows/page/9/1),
    for close-range sharpness loss, deflection risk and whetstone restoration.
  - **[P9]** [Capcom manual: save data](https://game.capcom.com/manual/Multi-Platform/en/windows/page/2/2),
    for autosave and the retained save boundary, together with the Start Menu
    rule that manual save is available in Kamura.
  - **[P10]** [Capcom support: detailed map and monster icons](https://www.capcom.co.jp/support/faq/platform_switch_monsterhunter_rise_0148358.html),
    for unknown large-monster marks before first contact, identity revelation
    on encounter and exact icons from quest start after a prior hunt.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/1446780),
    for Build ID `17920865` and its public-branch timestamps.
  - **[S2]** [Game8 opening progression](https://game8.co/games/Monster-Hunter-Rise/archives/323940),
    for `Back to Basics`, the three ★1 Key choices, two-clear requirement and
    Great Izuchi urgent unlock.
  - **[S3]** [Gamer Guides quest record](https://www.gamerguides.com/monster-hunter-rise/guide/village-quests/2-star-quests/urgent-great-izuchi-great-pain),
    for Shrine Ruins, target, first-large-monster context, `50` minutes,
    `900 z`, camp supplies and migration.
  - **[S4]** [Kiranico Long Sword data](https://mhrise.kiranico.com/data/weapons?view=3),
    for the base `Kamura Blade I` name and separation from Defender gear.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P10`, `S1`–`S4` and `R1`; written-evidence reasoning, not direct play.
- Research record: **[R1]** local preflight on 2026-09-13 found no application,
  manifest, install, save, matching userdata or executable.
- Claim IDs: `MHR-001`–`MHR-013`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-245`, `ACT-247`
  and `ACT-378` own direct navigation, supply use, Long Sword attacks, the
  three active Wirebug ability classes, carving, directly steered Palamute
  travel and field sharpening. Wiredash direction, Silkbind move and Wirefall
  context are parameters of an active capability, not three duplicate Action
  genes.

### System Behaviour Genes

- Existing `SYS-215`, `SYS-403`, `SYS-404`, `SYS-405`, `SYS-407` and `SYS-688`
  own live combat, monster migration, camp return on faint, hunt settlement,
  two autonomous Buddies and cycling sharpness. New `SYS-864` spends and
  independently recharges Wirebug units; new `SYS-865` converts touched
  Permabuffer pollen into a quest-duration stat increase capped by Petalace.

### Constraint Genes

- Existing `CON-210`, `CON-282`, `CON-354`, `CON-356` and `CON-358` own pouch
  capacity, the required opening chain, compatible combat state, timer/faint
  failure and finite carve legality. New `CON-634` requires a ready Wirebug unit
  and the action-specific sheathed, drawn-weapon or knockback context.

### Information, Objective and Time Genes

- Existing `INF-073`, `INF-075`, `INF-125` and `INF-157` expose items and
  equipment, hunter gauges, authored quest/map gates and the hunt state. New
  `INF-339` exposes every current large-monster position before identity is
  necessarily known; new `INF-340` exposes each available or recharging
  Wirebug unit. New `OBJ-174` owns the fixed Kamura opening and retained first
  large-monster Village-hunt result; `TIM-003` owns uninterrupted live field
  resolution.

## Reproducible transitions

| Before | Action | Bounded resolution | Claim |
|---|---|---|---|
| Fresh Kamura control and starter Buddies exist | Equip `Kamura Blade I` and complete `Back to Basics` | ★1 Village Key Quests become available without Hub participation | `MHR-003`, `MHR-004` |
| ★1 Village board is open | Complete `Fungal Frustrations` and `Roly-poly Lanterns` | Two fixed Key clears unlock urgent `Great Izuchi, Great Pain` | `MHR-003` |
| Urgent quest is accepted solo | Depart with both starter Buddies | Shrine Ruins loads with one Great Izuchi target, `50:00`, three-faint failure and supplies | `MHR-004`, `MHR-005` |
| Large monsters occupy the locale before first contact | Read the map | Each current position is marked; an unknown species uses a common mark until encounter reveals its icon | `MHR-005`, `MHR-010` |
| Palamute is nearby and callable | Mount, steer and dash toward the target, then dismount | Direct control transfers to mounted travel and back while both Buddies remain in the quest | `MHR-008`, `MHR-010` |
| One green Spiribird is reachable below the Petalace cap | Touch it | The creature is acquired and maximum health rises by the Petalace-defined amount until quest end | `MHR-009` |
| Weapon is sheathed and one Wirebug unit is ready | Aim and commit one Wiredash | Hunter moves along the chosen direction and the spent unit begins its action-specific recharge | `MHR-006`, `MHR-007` |
| Long Sword is drawn and one required unit is ready | Commit one starting Long Sword Silkbind | The weapon-specific move resolves and spent Wirebug unit or units begin recharge | `MHR-006`, `MHR-007` |
| An eligible Great Izuchi hit has knocked the hunter back | Commit Wirefall while a unit is ready | Hunter regains composure through Wirebug movement and that unit begins recharge | `MHR-006`, `MHR-007` |
| Repeated attacks have lowered sharpness | Complete one whetstone use in a safe interval | The close-weapon gauge rises while quest time and hostile action remain live | `MHR-010` |
| Great Izuchi leaves the current zone alive | Follow the current monster mark | The same target persists at its updated connected-zone position | `MHR-005`, `MHR-010` |
| Hunter health reaches zero with allowance remaining | Resolve the faint | Hunter returns to camp and one finite faint allowance is consumed | `MHR-011` |
| Two faints have already settled | Reach zero health again before target defeat | The third faint fails the quest and no positive result settles | `MHR-011` |
| Great Izuchi remains alive at time expiry | Let the clock reach zero | Time-up independently fails the quest | `MHR-011` |
| Great Izuchi reaches lethal state first | Resolve the slay and carve once during the completion window | Body becomes a finite eligible material source and the completed carve consumes one yield | `MHR-012` |
| Completion countdown closes | Accept materials and `900 z`, regain Kamura control and save | Urgent completion and rewards enter retained save state; a future reload verifies persistence | `MHR-005`, `MHR-012`, `MHR-013` |

## Strategic and experiential structure

- Planning horizon: monster marks, route geometry, health, stamina, sharpness,
  item stocks and individual Wirebug recovery determine the next safe
  commitment without revealing exact Great Izuchi health.
- Local tactics: preserve one Wirebug unit for Wirefall rather than spending
  both on mobility or Silkbind, sharpen while the target or companions create
  distance, and use the Palamute to reduce pursuit time between migrations.
- Medium-term structure: optional Spiribird detours trade clock and contact
  risk for quest-duration maximum statistics; the fixed control samples one
  green pickup without turning a full endemic-life route into a requirement.
- Irreversibility: item use, damage, target damage, carve opportunities and
  time advance inside the attempt; quest settlement writes rewards and urgent
  completion, whereas abandon is not an equivalent terminal.

## Replay and variation

- Great Izuchi's initial area, migration, attacks, Wirefall opening, drops,
  rewards and exact consumable use can vary while the authored predecessor
  chain and terminal predicates remain fixed.
- The route admits one reachable wild Wirebug but does not require a particular
  spawn path. It deliberately fixes one green Spiribird, one base Long Sword
  and both starter Buddy types so their causal roles stay auditable.

## Adjacent systems and history

- Monster Hunter: World shares the timed solo hunt, Palico, supplies,
  sharpness, migration, faints, carving and result settlement. Its target route
  is built from collected traces and scoutflies, and Great Jagras can feed;
  Rise instead begins with large-monster positions and spends Wirebug units on
  traversal, weapon ability and recovery.
- Monster Hunter Wilds shares live hunt settlement and a mount, but Seikret
  follows a selected target route and carries a second weapon. Rise's Palamute
  is directly steered, while the first-hunt packet has no Focus Mode, wounds,
  weather cycle or smithy step.
- Elden Ring shares a directly steered personal mount and real-time combat but
  has no posted Village quest, two-Buddy hunt, finite faint allowance, carve
  window or Wirebug recovery economy.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-245`, `ACT-247`, `ACT-378` | route, item, attack, Wirebug action, carve, mount and sharpening |
| System Behaviour | `SYS-215`, `SYS-403`, `SYS-404`, `SYS-405`, `SYS-407`, `SYS-688`, `SYS-864`, `SYS-865` | combat, migration, faints, rewards, Buddies, sharpness, charges and buff |
| Constraint | `CON-210`, `CON-282`, `CON-354`, `CON-356`, `CON-358`, `CON-634` | pouch, prerequisites, combat state, clock, carve and Wirebug legality |
| Information | `INF-073`, `INF-075`, `INF-125`, `INF-157`, `INF-339`, `INF-340` | items, gauges, quest, hunt, monsters and Wirebug state |
| Objective | `OBJ-174` | first urgent Village-hunt settlement and save |
| Time | `TIM-003` | live hunt cadence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `296` (`GAME-0001`–`GAME-0296`).
- Exact genome matches: none.
- Tied near matches: `GAME-0207` — Monster Hunter: World (`21 / 32 = 0.656250`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0207` — Monster Hunter: World | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-245`, `ACT-378`, `SYS-215`, `SYS-403`, `SYS-404`, `SYS-405`, `SYS-407`, `SYS-688`, `CON-210`, `CON-282`, `CON-354`, `CON-356`, `CON-358`, `INF-073`, `INF-075`, `INF-125`, `INF-157`, `TIM-003` | Both packets join direct movement, supplies, close attacks, sharpness, autonomous Palico pressure, migration, bounded faints, carving and retained quest settlement. World builds target reacquisition from traces and adds interruptible monster feeding. Rise starts with every large-monster position, directly steers a Palamute, and spends independently recovering Wirebug units across movement, weapon capability and knockback recovery while one Petalace-capped endemic contact changes quest statistics. | Near, `0.656250` |

## Taxonomy impact

- New genes: `SYS-864`, `SYS-865`, `CON-634`, `INF-339`, `INF-340` and
  `OBJ-174`.
- Existing wording: `ACT-247` is generalised from a spectral field mount to a
  personal field mount while keeping direct steering, mount/dismount and
  mounted actions as the invariant. No earlier signature changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_072`.
- Candidate terms affected: MONSTER HUNTER RISE, Kamura, Shrine Ruins, Great
  Izuchi, Kamura Blade I, Palico, Palamute, Buddy, Wirebug, Wiredash, Silkbind,
  Wirefall, Spiribird, Petalace and quest names remain product, actor, route,
  interface or game parameters.

## Negative results

- `INF-158` is rejected because Rise exposes current large-monster positions
  without trace-fed scoutfly acquisition; species identity may initially be
  unknown, but position does not depend on collected evidence.
- `COMB-0205` is unsupported because the packet lacks both trace-fed target
  reacquisition and an observable monster feeding-recovery loop. `COMB-0149`
  is unsupported because it requires Seikret routing, two carried weapons,
  wounds, Focus Mode, changing ecology and smithy progression.
- `SYS-037` and `SYS-222` do not own Spiribird contact: no score/progression
  collectible or carried inventory stack is credited; Petalace instead caps a
  temporary quest statistic.
- Wyvern Riding, Great Wirebugs, capture, forging and Sunbreak systems are not
  admitted merely because later game states can expose them.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `MHR-001`–`MHR-013`:
  one solo Village opening binds direct Palamute pursuit, a shared rechargeable
  Wirebug economy and one Petalace-capped endemic buff to the first retained
  large-monster quest result.

## New genes

- [Observation | Corroborated | High] `SYS-864`, `SYS-865`, `CON-634`,
  `INF-339`, `INF-340` and `OBJ-174` isolate six portable boundaries not owned
  by lower-ID genes.

## New combinations

- [Observation | Direct | High] None proposed; deterministic subset validation
  decides whether any existing verified combination is supported.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_072` generalises
  `ACT-247` to directly steered personal field mounts and adds Palamute support
  without changing the Elden Ring signature.

## Inferences

- [Strong Pattern | Corroborated | High] Rise shifts the early Monster Hunter
  search problem from evidence accumulation to charge-budgeted interception:
  current monster positions are visible, but Wirebug recovery and direct
  Palamute travel govern how safely and quickly the hunter converts that
  knowledge into contact.

## Open questions

- Exact build display, quest seed/state, Wirefall-producing hit, wild-Wirebug
  availability, reward rolls, terminal stocks and reload result await lawful
  local access and performed reproduction.

## Contradictions

- None within the declared public build, solo Village and first-hunt boundary.

## New questions

- Does a later fixed weapon packet make Wirebug-unit opportunity cost stronger
  through two-unit Silkbind moves without importing Switch Skills or Sunbreak?

## Next recommended game

- [Hypothesis | Limited | High] No next game ID is reserved. Complete an
  independent post-horizon selection review before allocating `GAME-0298`.
- Optimisation criterion: preserve mechanical distance after two adjacent
  hunt-corridor comparisons while keeping a lawfully reproducible released
  product boundary.
- Expected information gain: decide whether the first reserve, Nioh 2 — The
  Complete Edition, remains preferable after the completed 289–297 horizon.
- Backlog impact: close the reserved nine-game selection-018 batch without
  starting publication, tagging or deployment.

## Why this game

- [Hypothesis | Limited | High] Rise closes the planned contrast by separating
  map knowledge, direct mounted pursuit, shared ability charges and
  quest-duration endemic buffs from the World and Wilds hunt packets.

## Confidence and unresolved questions

- Confidence: High for product, branch projection, official Wirebug, Buddy,
  quest, save and Spiribird boundaries; Medium for exact unperformed route
  values and secondary-source opening sequence details.
- Resolution path: run the declared public build from a clean profile, record
  the setup and each named transition, then quit and reload the accepted Kamura
  save without enabling DLC or acceleration gear.
- Consequence: exact action timing, area order, rewards and terminal stocks
  remain parameters rather than observations.
