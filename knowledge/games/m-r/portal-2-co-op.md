---
game_id: GAME-0113
slug: portal-2-co-op
game_title: Portal 2 — Cooperative Campaign
analysis_status: reviewed
reviewed: 2026-09-14
combination_ids:
  - COMB-0033
  - COMB-0112
gene_ids:
  action:
    - ACT-008
    - ACT-047
    - ACT-048
  system:
    - SYS-036
    - SYS-059
    - SYS-060
    - SYS-061
  constraint:
    - CON-078
    - CON-079
    - CON-166
  information:
    - INF-001
    - INF-019
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Portal 2 — Cooperative Campaign

## Analysis scope

- Version / ruleset: the original launch/base two-player cooperative campaign
  in the Windows Steam app `620`, released 2011-04-18, bounded to one ordinary
  authored Standard Co-Op test chamber played online by two separate Windows
  clients. ATLAS and P-body each own a complete two-colour portal pair and must
  both reach their exit receptors.
- Primary decision loop: inspect the shared chamber and the partner's live
  state; assign each owner-specific portal endpoint, body and cube movement;
  place or replace endpoints; traverse or pass the cube through the resulting
  topology while preserving momentum; then coordinate both robots onto the
  exit receptors before changing a still-required route.
- Included: two independently controlled robots, four portal channels, surface
  eligibility, replacement, cross-owner traversal, momentum, cube carrying,
  visible portal views, live physics, remote online cooperation between two
  Windows Steam clients and dual exit completion.
- Excluded: single-player campaign, gels, excursion funnels, light bridges,
  gestures, calibration, story progression, local split-screen, PlayStation 3
  Steamworks, Xbox 360 system link, Peer Review, Perpetual Testing Initiative,
  Nintendo Switch, workshop maps and speedrun exploits.
- Direct-play status: not conducted. Valve's product page establishes app
  `620`, its launch date and the separate complete two-person campaign. The
  original Portal analysis supplies only the shared traversal base; dated Valve,
  PlayStation, Xbox and Nintendo evidence establishes the excluded platform and
  post-launch boundaries without changing the scoped chamber transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `P2C-001` | Portal 2 includes a separate two-player cooperative campaign | Confirmed | Direct | High | P1 |
| `P2C-002` | Each robot owns a distinct portal pair, yielding four persistent channels | Confirmed | Corroborated | High | P1, S1 |
| `P2C-003` | The scoped chamber requires both agents to coordinate topology and reach their exits | Observation | Corroborated | High | P1, S1 |
| `P2C-004` | The analysed target is the Windows Steam app 620 launch/base Standard Co-Op campaign, not a platform-neutral or mechanically equivalent cross-platform ruleset | Confirmed | Direct | High | P1 |
| `P2C-005` | At launch, the PlayStation 3 client used Steamworks for optional PC/Mac cross-platform play, friends, chat, achievements and cloud backup, while retaining PS3-only matchmaking and local split-screen paths | Confirmed | Direct | High | P2, P3 |
| `P2C-006` | Valve added two-controller Standard Co-Op split-screen to the Steam app in 2012 and later added a controller-plus-keyboard/mouse local path and community co-op queue support in 2019 | Confirmed | Direct | High | P4, P5 |
| `P2C-007` | The Xbox 360 edition exposed online, single-console split-screen and system-link co-op, and the current Xbox listing runs that product on Xbox One and Xbox Series X/S rather than naming a native rerelease | Confirmed | Corroborated | High | P6, P7 |
| `P2C-008` | Peer Review added a later co-op track, challenge modes and leaderboards across the 2011 Steam, PS3 and Xbox 360 lines | Confirmed | Corroborated | High | P8, P9 |
| `P2C-009` | Portal: Companion Collection released Portal 2 digitally for Nintendo Switch with local split-screen and online co-op | Confirmed | Direct | High | P10 |

## Basic data

- Release / origin: Valve released the Windows Steam app `620` on 2011-04-18;
  PlayStation 3 and Xbox 360 followed in the launch period, and Nintendo Switch
  received Portal 2 inside Portal: Companion Collection in 2022.
- Platform or physical form: Windows Steam online two-client cooperative
  spatial puzzle for the exact analysed target.
- Puzzle family: world topology and agent coordination.
- Primary sources:
  - **[P1]** [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/),
    for app identity, release date, the separate complete two-person campaign,
    current computer systems and published cooperative feature surface.
  - **[P2]** [Valve's PlayStation 3 Steam details](https://store.steampowered.com/oldnews/5302),
    for Steamworks cross-platform matchmaking, play, friends, chat,
    achievements, Steam Cloud and the linked PC/Mac entitlement.
  - **[P3]** [PlayStation Blog interview with Portal 2's project lead](https://blog.playstation.com/2011/04/14/portal-2-pretty-much-every-ps3-question-answered-and-that-cake-thing-too/),
    for the optional-account boundary, PS3 local split-screen, controller-only
    input and the intended PC/Mac/PS3 content lockstep at launch.
  - **[P4]** [Valve's 2012 Portal 2 update](https://store.steampowered.com/oldnews/9423),
    for the addition of two-controller Standard Co-Op split-screen.
  - **[P5]** [Valve's 2019 Portal 2 update](https://store.steampowered.com/oldnews/56268),
    for controller-plus-keyboard/mouse local co-op and the community co-op map
    queue boundary.
  - **[P6]** [Portal 2 Xbox 360 manual scan](https://manuals.plus/m/b86da5d8b3193fb89f11d93e8d749f42fcab2758bbfee1e8523019a67b638115),
    for the original online, single-console split-screen and system-link paths.
  - **[P7]** [current Xbox Portal 2 listing](https://www.xbox.com/en-US/games/store/portal-2/BT2B17V20D1P),
    for the Games on Demand product, co-op mode, Xbox One/Xbox Series hosts and
    Xbox One X enhancement label.
  - **[P8]** [Valve's Peer Review announcement](https://store.steampowered.com/oldnews/6427),
    for the new co-op track, challenge modes and leaderboards.
  - **[P9]** [Valve's 2011 cross-platform Peer Review rollout](https://store.steampowered.com/news/posts/?appids=620&enddate=1317947688),
    for distribution through Steam, Xbox LIVE and PSN to PC, Mac, Xbox 360 and
    PlayStation 3.
  - **[P10]** [Nintendo's Portal: Companion Collection listing](https://www.nintendo.com/us/store/products/portal-companion-collection-switch/),
    for the Switch digital bundle, 2022-06-28 release and local split-screen and
    online co-op modes.
- Secondary sources: **[S1]** [Portal Dialogue Corpus paper](https://arxiv.org/abs/2512.03381).
- Claim IDs: `P2C-001`–`P2C-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates each robot, `ACT-047` places owned endpoints and
  `ACT-048` carries a shared cube.
- Candidate genes: none.
- Claim IDs: `P2C-002`, `P2C-003`.

### System Behaviour Genes

- `SYS-036` resolves physics; `SYS-059`, `SYS-060`, `SYS-061` provide paired
  traversal, momentum redirection and occupancy-held mechanisms.
- Resolution order: endpoint placement; collision / transit; mechanism state; exit.
- Claim IDs: `P2C-003`.

### Constraint Genes

- `CON-078` restricts surfaces, `CON-079` limits one endpoint per channel and
  `CON-166` preserves two owners and four channel identities.
- Scarce strategic resources: four replaceable endpoints and two bodies.
- Claim IDs: `P2C-002`.

### Information Genes

- `INF-001` exposes local chamber state; `INF-019` shows live cross-portal views.
- Candidate genes: none.
- Claim IDs: `P2C-003`.

### Objective Genes

- `OBJ-022` requires both controlled robots to reach the paired exit receptors.
- Success, evaluation and failure: both present; death resets affected state.
- Claim IDs: `P2C-003`.

### Time Genes

- `TIM-003` keeps body and object physics live during coordination.
- Candidate genes: none.
- Claim IDs: `P2C-003`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| ATLAS has blue / purple portals; P-body has orange / red | P-body replaces red | Only P-body's red endpoint moves | owned channel identity | `P2C-002` |
| ATLAS enters its blue endpoint | Continue through topology | ATLAS exits ATLAS purple or linked active pair, preserving momentum | shared traversal law | `P2C-003` |
| Only one robot reaches an exit | Stand on receptor | Chamber remains incomplete | dual-agent completion | `P2C-003` |

## Strategic and experiential structure

- Local decision: choose which owner places which endpoint.
- Medium-term planning: distribute bodies and cube across portal-separated spaces.
- Long-term structure: preserve a four-endpoint route until both exits are occupied.
- Common heuristics: describe colours and avoid replacing a partner's needed route.
- Failure attribution: endpoint ownership is visible; communication errors dominate.
- Player-trust factors: colour / owner distinction needs accessible redundancy.
- Claim IDs: `P2C-002`, `P2C-003`.

## Replay and variation

- What changes between sessions: division of labour and timing.
- Randomness or procedural generation: none in the authored chamber.
- Multiple viable strategies: some chambers permit timing variants.
- Typical replay motive: cooperate with another partner.
- Claim IDs: `P2C-001`.

## Adjacent systems and history

- Direct predecessors: Portal's single-player paired topology.
- Variants: later co-op elements are outside scope.
- Similar games: Portal and synchronized-body puzzles.
- Important differences: four owner-specific portal channels and two required actors.
- Claim IDs: `P2C-002`.

## Platform-variant review notes

- The earlier `Scoped cross-platform ruleset` label was not supported: the
  canonical source is the Windows Steam app, while PS3 and Xbox 360 have
  distinct access, network and local-play surfaces. The target is now the
  dated launch/base Windows Steam Standard Co-Op campaign on two remote clients.
- The target's fourteen-gene signature, two combinations and three families
  remain unchanged. Local split-screen, network identity, cloud backup,
  entitlements, created-content access and compatibility hosts are delivery or
  participation boundaries outside the admitted chamber genome.
- PlayStation 3 Steamworks historically joined PC and Mac players and backed up
  co-op progress to Steam Cloud after account linking; simple PS3 matchmaking
  did not require a Steam account, and the console also supported local
  split-screen. The evidence is explicitly a 2011 launch boundary and does not
  prove that those network services remain live in 2026.
- Windows Steam gained two-controller Standard Co-Op split-screen in 2012. A
  2019 update added mixed controller and keyboard/mouse local input and local
  access to the community co-op queue. Neither path is silently projected back
  into the launch target.
- The Xbox 360 manual documents online, one-console split-screen and system-link
  co-op. The current Xbox store hosts that product on Xbox One and Xbox Series
  X/S and marks it Xbox One X Enhanced; it does not identify a native current-
  generation Portal 2 edition or cross-play with Steam/PS3.
- Peer Review is a later content ruleset with another co-op track, challenge
  modes and leaderboards. Portal: Companion Collection is a separate Switch
  entitlement bundling Portal and Portal 2 and exposing both local split-screen
  and online co-op. Neither is substituted for the original campaign target.
- The sparse comparison makes no claim of current PS3 or Xbox 360 service
  availability, Switch cross-play, exact patch parity, performance parity,
  every input device, every DLC, every community map, every storefront, every
  region or a complete release inventory.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-047`, `ACT-048` | two controllers |
| System Behaviour | `SYS-036`, `SYS-059`, `SYS-060`, `SYS-061` | portal physics |
| Constraint | `CON-078`, `CON-079`, `CON-166` | ownership |
| Information | `INF-001`, `INF-019` | colour / symbol labels |
| Objective | `OBJ-022` | dual exits |
| Time | `TIM-003` | live coordination |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `112` (`GAME-0001`–`GAME-0112`).
- Exact genome matches: none.
- Tied near matches: `GAME-0033` — Portal (`13 / 14 = 0.928571`).
- Supported combination subsets: `COMB-0033`, `COMB-0112`.
- Scan date: 2026-09-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0033`.

## Taxonomy impact

- Registry changes: `CON-166`.
- Taxonomy-change record: none.
- Candidate terms affected: portal ownership.

## Negative results

- `none`.
