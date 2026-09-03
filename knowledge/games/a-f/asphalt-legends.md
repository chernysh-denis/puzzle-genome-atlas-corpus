---
game_id: GAME-0242
slug: asphalt-legends
game_title: "Asphalt Legends"
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0240
gene_ids:
  action:
    - ACT-293
    - ACT-309
    - ACT-416
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-691
    - SYS-764
    - SYS-765
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-206
    - INF-208
    - INF-292
  objective:
    - OBJ-150
  time:
    - TIM-003
---

# Game: Asphalt Legends

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam product
  `app 1815780`, public branch Build ID `24370372`, built 2026-07-24 08:42:43
  UTC and observed 2026-09-03. Asphalt 9: Legends and Asphalt Legends Unite are
  historical names of the continuing product, not additional admitted games.
- Platform and lawful artefact boundary: the free current Steam Windows depot
  and a fresh online account after mandatory onboarding. Broadband Internet is
  required; no mobile/console client, private server, modified executable, DLC
  depot or purchase is admitted.
- Entry: after onboarding supplies the stock Mitsubishi Lancer Evolution, open
  permanent Career > Chapter 1: Welcome to Asphalt > Legendary Start 2018 >
  Race 1, confirm the Mitsubishi, keep TouchDrive enabled and commit the Classic
  event on San Francisco route `City Dash`. The packet begins at grid release.
- Primary decision loop: read road geometry, offered TouchDrive paths, speed,
  nitro, place, progress and rivals; choose a prompted branch or manoeuvre,
  brake into a useful drift and spend nitro at a chosen moment; let assisted
  steering/propulsion, arcade traction, collision, ramps and autonomous rivals
  resolve; preserve ordered progress and revise the next choice until finish.
- Positive terminal: complete the route and finish third or better. The result
  marks the Classic goal complete, adds the Career Flag and settles the
  displayed Blueprint, Credits and Reputation before returning to Career.
- Negative terminal: fourth or lower is a valid classified finish but does not
  satisfy the goal or earn its Flag. Quit/restart ends only the current attempt;
  a later retry is a separate trace.
- Included: one stock starter, TouchDrive, one permanent single-player Classic
  race, assisted motion, prompted route/manoeuvre choices, braking/drifting,
  ordinary nitro earning/spending, ramps, road contact/collision, rivals,
  ordered finish validation, live race information, top-three evaluation,
  Career Flag and disclosed post-race rewards.
- Excluded: manual steering; upgrades, import parts, fuel waiting, Garage
  collection and purchases; every other Career race; Time Attack, Hunted and
  other race types; Daily, Seasonal, Special and Limited-Time Events;
  multiplayer, co-op, private lobbies, split-screen, Clubs, Mastery, Legend
  Pass, packs, ads, broader currencies, DLC, other platforms and full Career.
- Reproducible parameterisation: current English Windows Steam public branch,
  Build ID `24370372`, fresh post-onboarding account, stock Mitsubishi Lancer
  Evolution, TouchDrive, Chapter 1, Legendary Start 2018 Race 1, Classic,
  `City Dash`, observed recommended rank `458` and goal third or better. Stop
  after the first retained success or classified lower-place result.
- Potential scoped modules: Manual Drive, secondary-goal race, Time Attack,
  Hunted, multiplayer, event fuel/tickets, upgrades, knockdown-heavy play,
  time-limited season or longer Career progression each needs a separate scope.
- Direct-play status: not conducted. Current Gameloft product/help text,
  official live-service notices and current static written build/event records
  support this reconstruction. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ASPH-001` | The current product is Gameloft's free Windows Steam app titled Asphalt Legends | Confirmed | Direct | High | P1, P2 |
| `ASPH-002` | The observed public Windows state is Build ID `24370372` in the ordinary Windows depot | Observation | Corroborated | Medium | S1, S2 |
| `ASPH-003` | The product supports single-player Career, TouchDrive/manual control and requires Internet | Confirmed | Direct | High | P1, P2, P3 |
| `ASPH-004` | Career races award Flags for disclosed conditions and may also disclose a Race Reward | Confirmed | Direct | High | P4, P5 |
| `ASPH-005` | Classic success can mean first, second or third according to the race's stated goal | Confirmed | Direct | High | P6 |
| `ASPH-006` | Legendary Start 2018 Race 1 is permanent Classic `City Dash`, rank `458`, goal third or better | Observation | Corroborated | Medium | S3, S4 |
| `ASPH-007` | The fresh-account starter for the first Career races is Mitsubishi Lancer Evolution | Observation | Corroborated | Medium | S4, S5 |
| `ASPH-008` | TouchDrive streamlines steering while preserving prompted manoeuvre, drift and nitro timing | Confirmed | Corroborated | High | P1, P2, P7, S5 |
| `ASPH-009` | Drifts/airborne stunts add ordinary nitro and activation spends it on acceleration | Confirmed | Direct | High | P7, P8, P9 |
| `ASPH-010` | Ordered progress and valid finish classify Classic before Career rewards settle | Observation | Corroborated | High | P4, P5, P6, S3 |
| `ASPH-011` | Seasons, newer tracks, multiplayer/co-op and collection systems are separable mutable modules | Confirmed | Direct | High | P1, P2, P10 |

## Basic data

- Release / origin: developed and published by Gameloft; Steam dates its
  Windows release to 2 August 2022. This unit analyses the current 2026 title.
- Platform or physical form: free-to-play Windows Steam software; one
  online-account single-player Career attempt is admitted.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [Steam product](https://store.steampowered.com/app/1815780/), for
    title, publisher, free Windows availability and separable play modes/IAP.
  - **[P2]** [official game site](https://asphaltlegends.com/), for current
    title, arcade race, nitro, TouchDrive/manual controls and live updates.
  - **[P3]** [official Internet requirement](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/544-do-i-need-to-be-connected-to-the-internet-to-play/).
  - **[P4]** [official Career help](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/section/190-career-mode/),
    for progress, unlocking, Flags, Classic and separate race types.
  - **[P5]** [official Flag rules](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/579-how-do-i-earn-flags/),
    for disclosed conditions, up to three Flags and Race Reward.
  - **[P6]** [official Classic rules](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/580-what-are-the-rules-of-classic-mode/),
    for first/second/third success according to the goal.
  - **[P7]** [official Gameplay help](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/section/193-gameplay-1607072985/),
    for car access, stunts, ordinary nitro and related mechanics.
  - **[P8]** [official Nitro Shockwave rule](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/606-how-do-i-perform-a-nitro-shockwave/).
  - **[P9]** [official Perfect Nitro rule](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/639-how-do-i-perform-a-perfect-nitro/).
  - **[P10]** [official 2026 roadmap](https://asphaltlegends.com/news/roadmap-2026),
    for mutable Mastery, tracks, seasons and account systems outside scope.
- Corroborating sources:
  - **[S1]** [SteamDB app](https://steamdb.info/app/1815780/) and **[S2]**
    [depots](https://steamdb.info/app/1815780/depots/), for build and Windows
    depot observations separated from DLC.
  - **[S3]** [current Chapter 1 database](https://asphalt9.info/asphalt9/game-mode/career/chapter-01-welcome-to-asphalt/),
    for Legendary Start Race 1 type, route, rank and reward parameters.
  - **[S4]** [community Career record](https://asphalt.fandom.com/wiki/Asphalt_Legends/Career_Mode/Chapter_1%3A_Welcome_To_Asphalt/Legendary_Start_2018),
    for first-race location and third-or-better goal.
  - **[S5]** [community starter record](https://asphalt.fandom.com/wiki/Mitsubishi_Lancer_Evolution_X_Final_Edition),
    for starter role and early-Career use only.
- Accessed: all sources 2026-09-03. Claim IDs: `ASPH-001`–`ASPH-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-293`: commit the permanent Career event with its Classic route,
  disclosed goal and result terms.
- Existing `ACT-309`: activate/release finite ordinary nitro for acceleration;
  Perfect Nitro and Shockwave timings are parameters.
- New `ACT-416`: under assisted steering, commit one offered route, drift or
  airborne manoeuvre without acquiring unrestricted steering.
- Parameters: event, car, control scheme, prompt, branch, drift/stunt, nitro,
  timing and release. Claims: `ASPH-006`, `ASPH-008`, `ASPH-009`.

### System Behaviour Genes

- Existing `SYS-320`: integrate arcade motion, road contact, ramps and collision.
- Existing `SYS-515`: advance autonomous rivals and relative place.
- Existing `SYS-516`: accept ordered course progress and classify valid finish.
- Existing `SYS-519`: retain successful event rewards and Career completion.
- Existing `SYS-691`: spend ordinary nitro into bounded acceleration.
- New `SYS-764`: propel/steer along the assisted path and resolve accepted
  prompts into its next trajectory.
- New `SYS-765`: turn eligible drift/airborne manoeuvres into ordinary nitro.
- Resolution: lock event/car/TouchDrive; release start; resolve assisted path,
  prompt/drift/nitro choices, motion/rivals/contact, nitro/place, ordered finish,
  top-three evaluation, Flag/reward, then Career return.
- Claims: `ASPH-004`–`ASPH-010`.

### Constraint Genes

- Existing `CON-438`: the final crossing classifies a result only after accepted
  ordered course completion.
- System-owned steering belongs to `SYS-764`, not a separate content gate.
  Route, place, speed and nitro are scarce parameters; car/rank/rewards are not
  genes. Claims: `ASPH-006`, `ASPH-008`, `ASPH-010`.

### Information Genes

- Existing `INF-204`: speed and road/route geometry support drift/ramp/boost.
- Existing `INF-205`: place, progress and rivals expose the top-three boundary.
- Existing `INF-206`: the event surface exposes type, route, rank, car and goal.
- Existing `INF-208`: result exposes place, goal, Flag and disclosed rewards.
- New `INF-292`: TouchDrive exposes available path/manoeuvre choices and nitro
  during forced progression. Claims: `ASPH-004`–`ASPH-010`.

### Objective Genes

- New `OBJ-150`: satisfy one disclosed place threshold in a finite rival race
  and retain its progression result. First through third, one Career Flag and
  displayed rewards are parameters.
- Third or better after a valid finish is positive; fourth or lower is a
  completed non-success; quit/restart retains neither result.
- Claims: `ASPH-004`–`ASPH-006`, `ASPH-010`.

### Time Genes

- Existing `TIM-003`: car, rivals, contact and progress advance continuously
  while prompt and nitro choices remain live. Claims: `ASPH-008`–`ASPH-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh account owns the stock starter | Open Legendary Start Race 1, confirm Mitsubishi and TouchDrive | `City Dash` Classic loads with rank, goal and reward | exact contract | `ASPH-006`, `ASPH-007` |
| Start releases the field | Allow assisted propulsion | TouchDrive propels/steers the car while rivals progress | divided authority | `ASPH-008` |
| A route/manoeuvre prompt appears | Commit one offer | Assisted steering resolves that branch/manoeuvre | live local choice | `ASPH-008` |
| The car enters a corner | Apply brake/drift | Rotation trades speed for exit trajectory; eligible drift adds nitro | technique/resource | `ASPH-009` |
| Nitro is available | Activate, time and release | Charge is debited; acceleration changes route/rival relation | resource spend | `ASPH-009` |
| Ordered route is complete | Cross finish | Final place is classified | evaluation boundary | `ASPH-010` |
| Place is first through third | Accept result | Goal, Flag and rewards persist; Career returns | positive terminal | `ASPH-004`–`ASPH-006`, `ASPH-010` |
| Place is fourth or lower | Allow result | Finish is visible; goal and Flag stay unsatisfied | negative terminal | `ASPH-005`, `ASPH-010` |

## Strategic and experiential structure

- Local: choose an offer, start a recoverable drift, and spend or retain nitro.
- Medium-term: chain path, drift and boost decisions so carried speed improves
  place before the finite finish rather than producing an isolated stunt.
- Long-term: convert assisted local choices into top-three classification,
  Career Flag and retained rewards.
- Heuristics: prefer a recoverable branch exit; drift only as much as needed;
  spend well-timed nitro where acceleration survives the next contact/corner.
- Failure attribution: prompt, geometry, speed, nitro, place, progress, rivals
  and result separate poor branch, overlong drift, wasted boost and a valid
  below-threshold finish.
- Trust: goal is disclosed before entry; live place/prompts explain opportunity;
  result separates finish from completed goal and retained reward.

## Replay and variation

- Attempts vary by prompt, drift, nitro, contact, rival spacing, time and place.
- Route, goal and rewards are not procedural; live rival/contact trajectories
  may vary while the observed contract remains fixed.
- Different offered branches and conservative/aggressive drift/boost timing can
  reach the accepted place set. Replay converts lower place into first success;
  the canonical trace stops at that first retained result.

## Adjacent systems and history

- The current title continues the formerly named Asphalt 9: Legends / Asphalt
  Legends Unite product; only the observed current branch is admitted.
- Need for Speed Underground shares an opening Career race, rivals, ordered
  finish and retained reward; Unbound shares technique-informed boost choices;
  Trackmania shares a finite route but resolves solo time/medal.
- TouchDrive owns steering/propulsion while the player owns prompted decisions.
  Success extends through third place; there is no first-place-only Underground
  rule, Unbound police/garage settlement or Trackmania medal threshold.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-293`, `ACT-309`, `ACT-416` | event, nitro and assisted prompt commitment |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-691`, `SYS-764`, `SYS-765` | motion, rivals, finish/reward, nitro and assisted path |
| Constraint | `CON-438` | ordered course before finish |
| Information | `INF-204`, `INF-205`, `INF-206`, `INF-208`, `INF-292` | driving, race, event, result and TouchDrive prompt state |
| Objective | `OBJ-150` | threshold place with retained progression |
| Time | `TIM-003` | continuous race pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `241` (`GAME-0001`–`GAME-0241`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`11 / 21 = 0.523810`).
- Supported combination subsets: `COMB-0240`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` — Need for Speed Underground | `ACT-293`, `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Both commit an opening Career race, resolve rivals over an ordered route and retain a result. Asphalt assigns steering/propulsion to TouchDrive, exposes prompted manoeuvres, uses ordinary nitro and accepts top three; Underground grants direct steering and requires first place. | Near, `0.523810` |

### Preserved research notes

- Result: `New gene` and `New combination of known and new genes`.
  No existing control gene preserves discrete prompted authority while the
  system steers, and no existing race objective accepts a disclosed place set
  broader than first while retaining progression.

## Combination status

- `COMB-0240` is a strict subset joining assisted prompts, technique-filled
  nitro, rivals, ordered finish and retained threshold result. Event commitment
  and generic speed/event/result surfaces stay outside its core.
- All `239` prior combinations are tested mechanically; none is inferred from
  genre or franchise similarity.

## Taxonomy impact

- Five new Active portable genes and one verified combination; no earlier
  definition, lifecycle, signature or taxonomy decision changes.
- Product, car, route, rank, build, place set and rewards remain parameters.

## Negative results

- Reject `ACT-290`: TouchDrive does not give the player direct steering,
  acceleration and braking authority. `ACT-416` captures retained prompts.
- Reject `OBJ-134`: that boundary requires first place; this event accepts top
  three. Reject `SYS-641`/`ACT-357`: ordinary nitro is not Unbound Burst.
- Seasons, events, alternate controls, collection economy and the whole Career
  are excluded instead of being merged into a live-service super-ruleset.
