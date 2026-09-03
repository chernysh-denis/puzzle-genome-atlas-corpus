---
game_id: GAME-0191
slug: total-war-warhammer-iii
game_title: "Total War: WARHAMMER III"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0189
gene_ids:
  action:
    - ACT-014
    - ACT-189
    - ACT-191
    - ACT-199
    - ACT-281
    - ACT-317
    - ACT-345
    - ACT-346
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-379
    - SYS-554
    - SYS-614
    - SYS-615
    - SYS-616
    - SYS-617
  constraint:
    - CON-273
    - CON-470
    - CON-509
    - CON-510
    - CON-511
  information:
    - INF-244
    - INF-245
  objective:
    - OBJ-114
  time:
    - TIM-003
    - TIM-018
---

# Game: Total War: WARHAMMER III

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam **Total War: WARHAMMER
  III**, official Patch `8.1.1`, Steam public Windows build `24237342`, checked
  2026-08-29; one fresh single-player **The Lost God** prologue with Tutorial
  guidance enabled and its ordinary offered campaign/battle settings unchanged.
- Content boundary: the currently available base-client prologue is the only
  campaign. No downloadable faction, cross-title ownership content or optional
  blood-effects pack is activated or causally required by the bounded route.
- Reproducible route: begin a new The Lost God campaign as Prince Yuri's fixed
  Kislev Expedition; follow the opening guidance, reclaim Kislev Refuge,
  upgrade the camp and commission the instructed Store House, equip the awarded
  item and spend the required available character point, end turns as prompted,
  march toward the Beacon, arrange the admitted army before the first Beacon
  battle, manually fight until the attacking force routs, and accept the
  post-battle return to the campaign layer.
- Primary decision loop: inspect mission, army movement, known terrain,
  treasury, settlement and construction state; choose a reachable campaign
  route, building-chain commitment, item or skill allocation and End Turn;
  when an encounter opens, inspect deployment, formation, terrain, targets and
  morale, issue live movement/attack orders and adapt until the battle settles;
  then read the casualties, rewards and quest state returned to the campaign.
- Entry and exit: begins at the first retained controllable campaign frame of a
  fresh The Lost God prologue. It succeeds only after the first required Beacon
  battle is won manually, the `Rescue` mission settles and the game returns to
  the first retained campaign-control or recruitment-instruction state. The
  recruitment action itself and every later prologue mission are outside scope.
- Included: the fixed Kislev Expedition and early prologue terrain; campaign
  army path and movement allowance; current vision and remembered terrain;
  treasury; Kislev Refuge ownership, upgrade and Store House slot; build
  duration and End Turn; one item equip and one available character point;
  the route to the Beacon; battle preview and pre-battle deployment; unit
  formations, facing, movement and attack orders; visible terrain, melee and
  ranged combat, casualties, leadership, routing and rally; pause/speed control;
  battle result, retained survivors/rewards and Rescue quest settlement.
- Excluded: post-terminal recruitment and the rest of `Rescue`; `Revenge`,
  `Reclaim`, Dervingard and all later The Lost God missions; the complete
  prologue ending; Realm of Chaos, Immortal Empires, multiplayer, ranked or
  custom battles; autoresolve; other factions, legendary lords and start
  positions; diplomacy, technology, agents, corruption, sieges and advanced
  settlement tiers not reached in the bounded segment; DLC, cross-title
  content, Blood effects, mods, Workshop items, console commands, achievements,
  cinematics as mechanics and the product's full live-service history.
- Potential scoped modules: one later prologue mission; one independently
  versioned Realm of Chaos or Immortal Empires start; one siege; one diplomacy
  packet; one multiplayer battle; or one DLC faction only after its own version,
  ownership assumptions, entry and terminal are fixed.
- Direct-play status: no authenticated current Windows Steam fresh prologue was
  conducted. Current official patch, product, manual, Academy and support
  evidence establish the executable and enduring campaign/battle rules;
  maintained route references establish the bounded tutorial sequence. The
  transition table is rules reasoning, not a claim of captured play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TWW3-001` | Patch 8.1.1 and public Windows build 24237342 are the reviewed current Steam rules boundary | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| `TWW3-002` | The Lost God remains an available single-player prologue in the current Total War: WARHAMMER III client | Confirmed | Direct | High | P3, P6, P7 |
| `TWW3-003` | The prologue fixes Prince Yuri's Kislev Expedition and teaches campaign movement, settlement and battle through an authored mission sequence | Observation | Corroborated | High | P4, S2, S3 |
| `TWW3-004` | A campaign army follows a world-map route under a replenishing per-turn movement allowance and current terrain or encounter limits | Confirmed | Direct | High | P4, P5 |
| `TWW3-005` | Kislev Refuge provides owned settlement slots whose prepaid building-chain commitments complete across campaign turns | Observation | Corroborated | High | P4, P5, S2, S3 |
| `TWW3-006` | End Turn settles queued campaign progress and returns refreshed authority after the opposing/world turn sequence | Confirmed | Direct | High | P4, P5 |
| `TWW3-007` | The first Beacon encounter admits pre-battle placement and then live unit formation, movement and attack commands | Observation | Corroborated | High | P4, P5, S2, S4 |
| `TWW3-008` | Battle casualties, facing, terrain, attacks and leadership can cause units to rout while surviving models remain alive | Confirmed | Direct | High | P4, P5 |
| `TWW3-009` | Current allied vision discloses live hostile state while unexplored or no-longer-observed campaign terrain limits decisions | Confirmed | Direct | High | P4, P5 |
| `TWW3-010` | Manually resolving the Beacon encounter transfers surviving units, losses, rewards and result back to the persistent campaign | Observation | Corroborated | High | P4, S2, S4 |
| `TWW3-011` | The bounded terminal is the first returned campaign state after the Beacon victory settles Rescue, before the prompted recruitment action | Observation | Corroborated | High | P7, S2, S4 |
| `TWW3-012` | The repository trace joins the early campaign economy and route to one manual battle without claiming later prologue or live-service systems | Observation | Direct | High | P1–P7, S1–S4, V1 |

## Basic data

- Release / origin: developed by Creative Assembly and published by SEGA;
  released for Windows in 2022 and maintained as a live strategy product.
- Platform or physical form: one current single-player Windows Steam client;
  a turn-based campaign map opens a separate pausable real-time battle.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Patch 8.1.1 hotfix notes](https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/14865-total-war-warhammer-iii-hotfix-8-1-1),
    for the current 2026-07-15 rules boundary.
  - **[P2]** [official Patch 8.1 release notes](https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/101-total-war-warhammer-iii-patch-8-1-release-notes),
    for the immediately preceding named public patch and changed systems.
  - **[P3]** [official Steam product page](https://store.steampowered.com/app/1142710/Total_War_WARHAMMER_III/),
    for the current title, Windows client, single-player campaigns and paired
    campaign/battle product boundary.
  - **[P4]** [official Total War: WARHAMMER III manual](https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/1142710/manuals/TWW3_PC_STEAM_MANUAL_EN.pdf?t=1740719956),
    for campaign turns, movement, settlements, construction, characters,
    deployment, formation command, battle, leadership, routing and results.
  - **[P5]** [official Total War Academy basics](https://academy.totalwar.com/category/basics/),
    for current official campaign and battle instruction across armies,
    settlements, construction, fog, deployment, formations and morale.
  - **[P6]** [official SEGA Total War: WARHAMMER III FAQ](https://support.sega.com/hc/en-gb/articles/4417717186833-TOTAL-WAR-WARHAMMER-III-FAQ),
    for Windows/Steam, single-player and campaign/multiplayer boundaries.
  - **[P7]** [official SEGA ownership and campaign FAQ](https://support.sega.com/hc/en-gb/articles/41283401991697-Total-War-WARHAMMER-I-2-Immortal-Empires-Unlock-FAQ),
    for current The Lost God availability alongside Immortal Empires and the
    separability of cross-title ownership content.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1142710/depots/),
    for public Windows build `24237342` dated 2026-07-16; SteamDB supplies only
    the store build identifier.
  - **[S2]** [maintained The Lost God quest reference](https://totalwarwarhammer.fandom.com/wiki/The_Lost_God),
    for Prince Yuri, the Kislev Expedition and the ordered `Respite` / `Rescue`
    mission boundary.
  - **[S3]** [independent prologue walkthrough](https://www.gry-online.pl/poradniki/total-war-warhammer-3/prolog/z91c302),
    for reclaiming and upgrading Kislev Refuge, the Store House instruction,
    item/character decisions and the route toward the Beacon.
  - **[S4]** [Creative Assembly Beacon support record](https://community.creative-assembly.com/total-war/total-war-warhammer/help/169-prologue-campaign-stuck-after-first-battle-at-beacon),
    used only to corroborate the authored first Beacon battle and its following
    recruitment instruction, not to claim that the historical defect persists.
  - **[V1]** repository-side transition trace derived from `P1`–`P7` and
    `S1`–`S4`; executable rules reasoning, not direct play.
- Claim IDs: `TWW3-001`–`TWW3-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-014`, commit Prince Yuri's campaign army to a reachable
  strategic destination; `ACT-189`, issue a selected battle formation a live
  destination, attack or attack-move order; `ACT-191`, spend one available
  character-development point; `ACT-199`, equip one compatible awarded item;
  `ACT-281`, end the current faction's multi-command campaign turn; `ACT-317`,
  set formation, facing and stance for a selected battle unit group.
- New genes: `ACT-345`, commission a legal building-chain entry in a Kislev
  Refuge slot; `ACT-346`, arrange controlled units inside the assigned
  pre-battle deployment zone.
- Parameters: army, campaign destination, movement allowance, item, character
  point, settlement, slot, building, treasury cost, turn, deployment region,
  unit group, formation, facing, stance, battle destination and target.
- Claim IDs: `TWW3-003`–`TWW3-007`, `TWW3-012`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded live hostile combat;
  `SYS-297`, execute selected-unit pathing and attack acquisition; `SYS-305`,
  propagate allied vision, fog and detection; `SYS-379`, retain mission and
  reward flags between ordered prologue gates; `SYS-554`, move a multi-model
  unit through its commanded formation.
- New genes: `SYS-614`, spend a campaign army's movement allowance through a
  strategic route; `SYS-615`, advance prepaid settlement construction at End
  Turn; `SYS-616`, instantiate a campaign encounter as a live battle and return
  its losses/result to campaign; `SYS-617`, convert leadership modifiers into
  routing and possible rally while models remain alive.
- Resolution order: accept campaign movement, settlement, item and character
  choices; End Turn advances construction and refreshes later authority;
  reaching the Beacon instantiates deployment and battle state; battle time
  resolves formation pathing, attacks, casualties and morale; victory returns
  surviving unit and mission state to the campaign.
- Parameters: campaign route, terrain, movement cost, turn refresh,
  construction duration, battle instance, deployment, model count, health,
  leadership, rout, rally, casualty, reward and returned quest state.
- Claim IDs: `TWW3-004`–`TWW3-012`.

### Constraint Genes

- Existing genes: `CON-273`, current vision and detection gate actionable
  hostile information; `CON-470`, live group movement and attacks obey terrain,
  space, formation, visibility and range.
- New genes: `CON-509`, campaign routes require remaining movement and
  strategic reachability; `CON-510`, settlement construction requires
  ownership, a compatible chain slot, prerequisites and treasury; `CON-511`,
  every initial battle formation must fit the assigned deployment zone.
- Scarce strategic resources: campaign movement allowance, campaign turns,
  treasury, building slots and time, character point, health/model count,
  leadership, formation space, attack range and safe terrain.
- Claim IDs: `TWW3-004`–`TWW3-009`.

### Information Genes

- Existing genes: none; lower-ID campaign, city and RTS information records
  either assume a hex civilization, a national theatre or simultaneous
  resource-production queues outside this bounded strategic layer.
- New genes: `INF-244`, expose campaign army movement, known map, settlement,
  treasury, construction and quest state; `INF-245`, expose battle deployment,
  unit formation, orders, health/model count, leadership and routing state.
- Claim IDs: `TWW3-003`–`TWW3-011`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-114`, manually complete the first Beacon rescue and regain
  retained campaign authority after Rescue settlement.
- Success, evaluation and failure: success requires the manual battle victory,
  mission settlement and returned campaign state. A campaign defeat, abandoned
  route or lost required battle fails this trace; recruiting after return or
  continuing the prologue does not extend the objective.
- Claim IDs: `TWW3-002`, `TWW3-010`–`TWW3-012`.

### Time Genes

- Existing genes: `TIM-018`, the campaign grants one faction an open
  multi-command interval before End Turn settles progress and passes authority;
  `TIM-003`, deployment commitment opens a pausable real-time battle in which
  formations, hostiles, attacks and morale continue while commands are issued.
- New genes: none; `SYS-616` owns the persistent transition between the two
  already distinct timing structures.
- Claim IDs: `TWW3-004`–`TWW3-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current Patch 8.1.1 client is at the main menu | Start a fresh The Lost God campaign with Tutorial guidance | The authored prologue fixes Prince Yuri and the Kislev Expedition and reaches the first retained campaign-control frame | current bounded entry | `TWW3-001`–`TWW3-003` |
| Prince Yuri is selected with movement available | Commit the next prompted reachable campaign destination | The army follows the strategic route, consumes terrain-adjusted movement and retains the reached position | campaign movement is allowance-bound | `TWW3-004` |
| The route reaches ruined Kislev Refuge | Move into the admitted settlement interaction | Ownership and the Respite state expose the settlement panel and its next instructed upgrade | movement can change persistent strategic ownership | `TWW3-003`, `TWW3-005` |
| Kislev Refuge has the required legal slot and treasury | Commission the camp upgrade and instructed Store House | Treasury is paid, the chain entry occupies its slot and a remaining-turn duration is recorded | building is prepaid and slot-bound | `TWW3-005` |
| A campaign construction or movement refresh is pending | Choose End Turn | Queued progress advances and the next player campaign interval restores eligible movement and commands | campaign authority is turn-settled | `TWW3-006` |
| An awarded compatible item and point are available | Equip the declared item and spend the point on an eligible node | Character modifiers persist into the later army and battle state | early progression is a retained campaign choice | `TWW3-003` |
| The Rescue marker and route to the Beacon are disclosed | March the Kislev Expedition to the encounter | Movement and contact bind the participating army and local terrain into the required battle transition | authored campaign route causes battle entry | `TWW3-004`, `TWW3-007` |
| The first Beacon battle is awaiting start | Arrange each controlled formation inside the legal zone and commit battle start | Unit position, facing, width and group become the initial live battle state | deployment is editable but bounded | `TWW3-007` |
| Battle time is live and hostiles are visible | Issue movement, formation and attack orders | Units path, preserve or reform geometry, acquire legal targets and exchange live attacks | command is indirect and formation-scale | `TWW3-007`, `TWW3-008` |
| A hostile formation takes losses or adverse pressure | Continue legal flank, ranged or melee pressure | Leadership falls; at the break condition the unit routs despite surviving models and may rally only if conditions recover | morale changes command authority | `TWW3-008` |
| All required attackers are defeated or routing beyond recovery | Allow the battle result to settle | Surviving models, casualties, experience, rewards and victory are transferred back to the campaign | battle is not a disconnected scenario | `TWW3-010` |
| The victorious campaign state is restored | Wait for Rescue settlement and the next recruitment instruction | The mission records completion and returns retained campaign authority; the scope stops before any recruitment input | exact bounded terminal | `TWW3-011`, `TWW3-012` |

## Strategic and experiential structure

- Local decision: spend remaining campaign movement, choose the legal building
  slot or End Turn; in battle, change formation, facing, target or path while
  reading terrain, losses and leadership.
- Medium-term planning: convert treasury and turns at Kislev Refuge into a
  stronger persistent expedition, preserve movement for the mission route and
  deploy complementary formations before live contact.
- Long-term structure: carry one authored tutorial chain from strategic-map
  ownership and construction through a manually commanded battle and back into
  a persistent campaign result.
- Common heuristics: finish the instructed settlement state before marching;
  keep ranged units behind a protective line; face the likely approach; avoid
  stretching formations through bad terrain; concentrate pressure until an
  enemy routes; confirm returned quest state rather than stopping at the
  battlefield victory banner.
- Failure attribution: insufficient movement, illegal slot, missing treasury,
  premature End Turn, invalid deployment, obstructed formation, exposed flank,
  falling leadership, unresolved hostile or premature terminal are separable.
- Player-trust factors: explicit tutorial missions, visible movement pips and
  construction timers, bounded deployment geometry, unit cards, order arrows,
  health/leadership feedback and a post-battle campaign return.
- Claim IDs: `TWW3-003`–`TWW3-012`.

## Replay and variation

- What changes between sessions: exact route clicks, item/skill selection,
  construction timing, deployment width, groups, target order, casualties,
  rout timing and battle duration. The campaign, faction and terminal are fixed.
- Randomness or procedural generation: the early prologue geography and mission
  sequence are authored; live combat timing and incidental damage variation do
  not replace the declared rules or terminal.
- Multiple viable strategies: formations can use different widths and approach
  vectors, and targets may be focused in different orders; the canonical trace
  requires manual victory rather than one exact tactical script.
- Typical replay motive: execute a cleaner battle or continue the prologue.
  Later missions and broader campaigns are separate packets.

## Adjacent systems and history

- Direct predecessor: earlier Total War games share the campaign/battle form,
  but this record fixes only the current WARHAMMER III prologue and client.
- Variants: Realm of Chaos, Immortal Empires, other factions, multiplayer,
  custom battles, DLC, cross-title content and later patches need their own
  bounded scope contracts.
- Similar games: Age of Empires II: Definitive Edition shares selected group
  pathing, formations, fog and live combat; Sid Meier's Civilization VI shares
  open multi-command faction turns and settlement development; Hearts of Iron
  IV shares campaign-scale army, fog and pausable war information.
- Important differences: Age of Empires II keeps construction, economy and
  battle simultaneous on one map; Civilization VI resolves combat on the same
  sequential hex layer; Hearts of Iron IV never expands an encounter into a
  separately deployed real-time regiment battle whose casualties return.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-189`, `ACT-191`, `ACT-199`, `ACT-281`, `ACT-317`, `ACT-345`, `ACT-346` | campaign movement, item/skill, settlement, turn, deployment and battle command |
| System Behaviour | `SYS-215`, `SYS-297`, `SYS-305`, `SYS-379`, `SYS-554`, `SYS-614`, `SYS-615`, `SYS-616`, `SYS-617` | fog, route, construction, formation, combat, morale and cross-layer persistence |
| Constraint | `CON-273`, `CON-470`, `CON-509`, `CON-510`, `CON-511` | vision, terrain, movement, slot, treasury and deployment legality |
| Information | `INF-244`, `INF-245` | campaign economy/route and battle formation/morale state |
| Objective | `OBJ-114` | settle first Beacon rescue into returned campaign control |
| Time | `TIM-003`, `TIM-018` | pausable live battle nested after multi-command campaign turns |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `190` (`GAME-0001`–`GAME-0190`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`9 / 47 = 0.191489`).
- Supported combination subsets: `COMB-0189`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-189`, `ACT-317`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-554`, `CON-273`, `CON-470`, `TIM-003` | both expose fog-limited live formations whose pathing, facing, terrain, range and attack orders resolve in real time, but Age of Empires II keeps workers, construction, queues and combat simultaneous on one map until civilization-wide Conquest; Total War prepares one persistent army and fixed-slot settlement across campaign turns, enters a separately bounded deployment/battle layer with leadership routing, then returns casualties and Rescue state to the campaign | Near, `0.191489` |

### Preserved research notes

- New genes: `ACT-345`, `ACT-346`, `SYS-614`, `SYS-615`, `SYS-616`, `SYS-617`,
  `CON-509`, `CON-510`, `CON-511`, `INF-244`, `INF-245` and `OBJ-114`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: ordinary character allocation, equipment, campaign
  turns, formation commands, live combat/pathing, fog, quest persistence and
  existing timing structures reuse safely. Slot-prepaid turn construction,
  strategic movement allowance, legal deployment, morale routing and the
  campaign/battle/campaign transfer are absent as lower-ID boundaries.

## Combination status

- `COMB-0189` is a verified strict twenty-four-gene subset of the twenty-seven-
  gene genome, coupling campaign movement, settlement construction and End
  Turn to legal deployment, formation-scale live combat, morale and returned
  Rescue state.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: twelve new Active genes, `COMB-0189` and four existing
  family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. Reused definitions retain their prior boundaries.
- Candidate terms affected: slot-prepaid turn construction, strategic army
  movement allowance, bounded pre-battle deployment, live unit routing and
  persistent campaign-to-battle result transfer.

## Negative results

- `ACT-139`, `SYS-550` and `CON-466` are not reused: Kislev Refuge uses fixed
  settlement slots and a turn countdown, not spatial foundations built by
  staffed live workers.
- `ACT-275` is not reused: the Store House spends treasury before a declared
  turn duration instead of consuming a city's yield toward one production
  target.
- `ACT-316`, `SYS-551` and `CON-467` are not reused: recruitment begins only at
  the terminal instruction and no unit is queued inside this scope.
- `INF-184`, `INF-190`, `INF-224` and `INF-225` are not reused: their hex-map or
  simultaneous RTS boundaries do not jointly represent this campaign layer or
  regiment-morale battle view.
- `OBJ-103` is not reused: Beacon success defeats one authored encounter rather
  than eliminating a recoverable opposing civilization.
- Autoresolve, the later prologue and broader live-service systems are not
  admitted merely because the current client exposes them.
