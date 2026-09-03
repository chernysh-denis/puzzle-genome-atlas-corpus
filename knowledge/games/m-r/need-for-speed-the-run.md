---
game_id: GAME-0235
slug: need-for-speed-the-run
game_title: "Need for Speed: The Run"
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0233
gene_ids:
  action:
    - ACT-290
    - ACT-291
    - ACT-292
    - ACT-309
    - ACT-350
  system:
    - SYS-320
    - SYS-365
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-691
    - SYS-746
  constraint:
    - CON-282
    - CON-438
    - CON-577
  information:
    - INF-204
    - INF-205
    - INF-208
    - INF-286
  objective:
    - OBJ-146
  time:
    - TIM-003
---

# Game: Need for Speed: The Run

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: original unmodified English Windows retail executable
  `1.0.0.0`, the lawfully acquired pre-delisting standard edition, operated
  offline on a period-compatible Windows 7 installation. Patch `1.1` is not
  admitted because no primary release provenance was established for this
  packet. EA removed the title from digital stores on 2021-05-31 and retired
  online services on 2021-08-31; the official notice says offline features
  remain playable.
- Platform and mode: PC, keyboard, The Run single-player campaign, Normal
  difficulty, automatic transmission, base-game stock BMW M3 GTS selected from
  the fresh-profile Stage 1 choice. No online service or account-derived unlock
  is required.
- Entry: choose `Start New`, Normal, automatic transmission and the BMW M3 GTS;
  retain the fixed story introduction and car choice, then begin at the first
  accepted vehicle input for the Stage 1 West Coast route in San Francisco.
- Primary decision loop: read the route, race objective, current place,
  checkpoint-reset stock, speed and nearby traffic/rivals; steer, brake,
  accelerate or spend nitrous; preserve a valid line through ordered route
  gates; pass the required rivals before each event finish; accept the result
  and continue into the next required Stage 1 event.
- Positive terminal: complete the three required Stage 1 West Coast driving
  events, advance from 211th to the retained 195th route position, settle the
  stage and expose Stage 2. Stop before beginning Stage 2. Remaining resets may
  add the manual's declared stage-end bonus XP, but neither a perfect reset
  stock nor an Autolog comparison is required.
- Negative terminal: spending the final available checkpoint reset fails the
  current event; abandoning, failing an event target or stopping before Stage 1
  settlement is non-completion. Retry is permitted only inside the declared
  event and does not itself satisfy the terminal.
- Included: one stock eligible Tier 4 car; Normal AI and five checkpoint resets
  per race; dedicated car input; road/traffic/rival contact; ordinary nitrous;
  event objectives, route gates and finishes; three ordered events; Driver XP;
  cumulative route-position advancement; Stage 1 completion and Stage 2 access.
- Excluded: the scrapyard on-foot/QTE interaction as a signature mechanic;
  later stages and the complete San Francisco-to-New York campaign; Stage
  Select replay; Challenge Series; online Multiplayer and Playgroups; Autolog,
  SpeedWall and friend comparison; Limited Edition cars, DLC and promotional
  unlocks; patch `1.1`; console/portable versions; community executables,
  compatibility wrappers, mods, cracks or abandonware.
- Reproducible parameterisation: use a lawful original PC retail entitlement,
  clean `1.0.0.0` files, Windows 7 compatibility, network unavailable before
  launch, fresh profile, English, keyboard, Normal, automatic and stock BMW M3
  GTS. Complete Stage 1 once, retain the 195th-position settlement and Stage 2
  access, exit, relaunch offline and verify that Stage 2 remains available.
- Potential scoped modules: one later stage, one Survival or Battle event, one
  Challenge Series entry or one lawful patched retail build each needs its own
  fixed entry and terminal. Retired online modes cannot enter this packet.
- Direct-play status: not conducted. The official PC manual, official EA
  product/news and service-retirement material establish the product, controls,
  HUD, reset rules, event grammar and offline boundary. Two secondary textual
  route references corroborate the exact Stage 1 order, targets and terminal.
  No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NFSTR-001` | The admitted artefact is the original 2011 Windows Need for Speed: The Run, not another Need for Speed game or a console/portable port | Confirmed | Direct | High | P1, P2, P3 |
| `NFSTR-002` | EA removed the product from digital stores on 2021-05-31, retired online services on 2021-08-31 and retained offline features | Confirmed | Direct | High | P4, P5 |
| `NFSTR-003` | The scoped executable is the clean retail `1.0.0.0`; later patch provenance is not strong enough for admission | Observation | Corroborated | Medium | S1, S2 |
| `NFSTR-004` | PC exposes direct steering, throttle, braking, handbrake, camera, gear, nitrous and checkpoint-reset controls | Confirmed | Direct | High | P1 |
| `NFSTR-005` | The HUD exposes objective, timer, route/minimap, place, resets, speed, gear, nitrous and Driver XP | Confirmed | Direct | High | P1 |
| `NFSTR-006` | Wreck or manual reset restores the last passed checkpoint; reset stock is difficulty-dependent and exhausting the last reset fails the event | Confirmed | Direct | High | P1 |
| `NFSTR-007` | Normal supplies five resets per race; remaining resets at stage end grant bonus XP | Observation | Corroborated | High | P1, S3, S4 |
| `NFSTR-008` | Stage 1 West Coast begins at rank 211, consists of three required driving events and ends at retained rank 195 | Observation | Corroborated | High | S3, S5 |
| `NFSTR-009` | A fresh Stage 1 lets the player choose an eligible Tier 4 car; the base-game BMW M3 GTS is available from the beginning | Observation | Corroborated | Medium | S3, S6 |
| `NFSTR-010` | Stage 1 uses race objectives that require passing rivals and completing ordered route segments before Stage 2 becomes available | Observation | Corroborated | High | P1, S3, S5 |
| `NFSTR-011` | Ordinary nitrous is available in the campaign, consumes a gauge and refills under its ability rules | Observation | Corroborated | Medium | P1, S4, S5 |
| `NFSTR-012` | The product frames The Run as a high-stakes San Francisco-to-New York race against 200 drivers | Confirmed | Direct | High | P2, P3 |

## Basic data

- Release / origin: EA Black Box; Electronic Arts; original Windows release in
  November 2011.
- Platform or physical form: real-time single-player PC driving campaign;
  exactly one fixed three-event opening stage is analysed.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official EA PC manual](https://eaassets-a.akamaihd.net/eahelp/manuals/need-for-speed-the-run-manuals_PC.pdf),
    for controls, HUD, checkpoint resets, stage-end XP, Driver Abilities and
    single-player event types.
  - **[P2]** [official EA European car trailer article](https://www.ea.com/news/need-for-speed-the-run-european-car-trailer-released),
    for product identity, Jack's entry and the 200-driver San Francisco-to-New
    York premise.
  - **[P3]** [official EA cast and product article](https://www.ea.com/news/hendricks-and-faris-enter-the-run),
    for the Windows-era product, Frostbite 2 and cross-country campaign scope.
  - **[P4]** [official EA retirement announcement](https://forums.ea.com/discussions/need-for-speed-franchise-discussion-en/an-announcement-about-some-older-nfs-titles-/9487315),
    for delisting, online retirement and retained offline features.
  - **[P5]** [official EA service-update register](https://www.ea.com/legal/service-updates/i-q),
    for the retired Need for Speed: The Run online service boundary.
- Corroborating textual sources:
  - **[S1]** [PCGamingWiki product record](https://www.pcgamingwiki.com/wiki/Need_for_Speed%3A_The_Run),
    for the original PC release, delisted state, offline-launch risk and
    separation of clean retail from later community compatibility changes.
  - **[S2]** [contemporaneous `1.0.0.0` crash record](https://forums.tomshardware.com/threads/need-for-speed-the-run-error-please-help.100197/),
    for the original application-version string only.
  - **[S3]** [Need for Speed Wiki Stage 1 record](https://nfs.fandom.com/wiki/Need_for_Speed%3A_The_Run/The_Run/Stage_1),
    for West Coast event order, 211th-to-195th advancement, Tier 4 entry and
    Normal reset count.
  - **[S4]** [contemporaneous manual mirror](https://www.manualshelf.com/manual/electronic-arts/ea-need-for-speed-the-run-14633195873/ea-need-for-speed-the-run-manual/page-4.html),
    for the official manual's stage-end reset bonus and Driver Ability text.
  - **[S5]** [GameFAQs PC route guide](https://gamefaqs.gamespot.com/pc/628145-need-for-speed-the-run/faqs/63357),
    for the three early route segments, pass targets and Stage 1 continuation.
  - **[S6]** [StrategyWiki car table](https://strategywiki.org/wiki/Need_for_Speed%3A_The_Run/Cars),
    for base-game BMW M3 GTS Tier 4 availability from the beginning.
- Claim IDs: `NFSTR-001`–`NFSTR-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: steer, accelerate, brake and handbrake the assigned BMW
  M3 GTS continuously through each event.
- Existing `ACT-291`: choose the eligible stock BMW M3 GTS from the Stage 1
  Tier 4 starter set before the event locks its assigned car.
- Existing `ACT-292`: commit Normal opponent difficulty and automatic
  transmission for the fresh campaign packet.
- Existing `ACT-309`: hold or release ordinary nitrous, spending its visible
  gauge to add forward acceleration.
- Existing `ACT-350`: request the authorised checkpoint reset while the current
  race remains unfinished; wreck-triggered recovery shares the same resolution
  but is not a separate player action.
- Parameters: car identity, available starter set, difficulty, transmission,
  key bindings, line, braking, nitrous timing, reset request and event state.
- Claim IDs: `NFSTR-004`, `NFSTR-006`, `NFSTR-007`, `NFSTR-009`, `NFSTR-011`.

### System Behaviour Genes

- Existing `SYS-320`: rigid vehicle motion, road contact, collision, wreck and
  usable control resolve continuously.
- Existing `SYS-365`: authored city and highway traffic occupies the route and
  resolves collision without becoming a competitive participant.
- Existing `SYS-515`: Normal difficulty drives the required autonomous rival
  field along the same event routes.
- Existing `SYS-516`: each event accepts ordered course progress and settles
  its finish only after the required route and rival target are satisfied.
- Existing `SYS-519`: valid event results retain Driver XP, cumulative route
  position, Stage 1 completion and the Stage 2 unlock.
- Existing `SYS-691`: ordinary nitrous activation debits the current gauge and
  applies bounded car acceleration until release or depletion.
- New `SYS-746`: an accepted manual request or qualifying wreck spends one
  checkpoint reset and restores the assigned car to the last passed checkpoint;
  the final spent reset instead fails the event.
- Resolution order: accept live input; integrate car/rival/traffic motion;
  validate route and target progress; on recovery request or wreck, test reset
  stock, debit it and restore or fail; on valid finish settle XP/rank; after the
  third result retain 195th and expose Stage 2.
- Claim IDs: `NFSTR-004`–`NFSTR-011`.

### Constraint Genes

- Existing `CON-282`: the three Stage 1 events and their authored transition
  gates must be cleared in order before the Stage 2 successor is legal.
- Existing `CON-438`: route progress and finish remain invalid until required
  ordered checkpoints have been accepted.
- New `CON-577`: each race admits only the difficulty-fixed reset stock; on
  Normal the fifth reset is terminal rather than another restored attempt.
- Scarce strategic resources: reset stock, nitrous charge, road distance and
  remaining rival target. Exact route names, five resets and the BMW are
  instance parameters, not canonical gene labels.
- Claim IDs: `NFSTR-006`–`NFSTR-010`.

### Information Genes

- Existing `INF-204`: speed, gear, minimap and authored route cues make the
  next braking and steering decision readable.
- Existing `INF-205`: live place/target, checkpoint/course progress, timer and
  nearby rivals expose whether the current event can still settle.
- Existing `INF-208`: each result transition exposes performance, Driver XP,
  route-position advancement and the retained next-stage unlock.
- New `INF-286`: the campaign surface exposes remaining checkpoint resets
  together with the current cumulative route rank and stage target, so a
  recovery decision and multi-event progress are visible before settlement.
- Autolog and friend comparison are not admitted information channels.
- Claim IDs: `NFSTR-005`–`NFSTR-010`.

### Objective Genes

- New `OBJ-146`: pass the required rivals across all three ordered Stage 1
  events, advance the campaign rank from 211th to 195th and retain Stage 2
  access after relaunch.
- One pass, checkpoint, event finish or Driver Level is intermediate. Winning
  the complete cross-country Run is outside the bounded terminal.
- Claim IDs: `NFSTR-008`–`NFSTR-010`.

### Time Genes

- Existing `TIM-003`: vehicle, rivals, traffic, timer and collision continue
  while the player reads and supplies live driving input.
- Claim IDs: `NFSTR-004`–`NFSTR-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh profile has reached Stage 1 car choice | Select the eligible stock BMW M3 GTS and accept Normal | The selected Tier 4 car and five-reset event profile become active | exact participant and ruleset | `NFSTR-007`, `NFSTR-009` |
| The first event releases control at rank 211 | Accelerate, steer and brake toward the disclosed target | Vehicle, traffic and Normal rivals resolve continuously | bounded live entry and competitive field | `NFSTR-004`, `NFSTR-005`, `NFSTR-008` |
| Ordinary nitrous charge is visible | Hold nitrous on a chosen line | Gauge decreases while bounded forward acceleration is applied | finite acceleration decision | `NFSTR-005`, `NFSTR-011` |
| Four Normal resets remain and the last checkpoint is recorded | Request reset or trigger a qualifying wreck | One reset is consumed and the car resumes at the last passed checkpoint | recoverable local route error | `NFSTR-006`, `NFSTR-007` |
| One Normal reset remains | Trigger another accepted reset | The last reset is consumed and the current event fails | explicit negative terminal | `NFSTR-006`, `NFSTR-007` |
| Current event route and pass target are complete | Cross its valid finish | Result, Driver XP and cumulative rank advance; the next authored Stage 1 event opens | event settlement inside the stage | `NFSTR-008`, `NFSTR-010` |
| All three Stage 1 results are valid | Accept the final West Coast settlement | Position 195 and Stage 2 access are retained | positive terminal | `NFSTR-008`, `NFSTR-010` |
| Stage 2 is exposed | Exit and relaunch offline | The successor remains selectable from retained campaign state | persistence check | `NFSTR-002`, `NFSTR-008` |

## Strategic and experiential structure

- Planning horizon: trade immediate overtake pace against a stable line and
  finite recovery stock, while preserving enough progress to clear the current
  target and the two successor events.
- Local tactics: brake before sharp city geometry, choose a safe passing side,
  deploy nitrous on straights and reserve resets for unrecoverable wrecks or
  missed route state.
- Long-term structure: three separately settled event targets reduce the same
  cross-country rank from 211th to 195th and unlock the next stage.
- Reversible versus irreversible: steering and nitrous timing are local;
  checkpoint reset rewinds only to a recorded route state at a finite cost;
  event results, cumulative rank and Stage 2 access persist.
- Failure attribution: route, objective, place, timer and reset stock distinguish
  a missed line, insufficient rival progress and exhausted recovery allowance.
- Player trust: the official manual discloses the reset rule, the HUD exposes
  its stock and each result makes cumulative progress visible.

## Replay and variation

- What changes between attempts: line, traffic/rival contact, pass timing,
  nitrous use, reset spend, elapsed time and XP bonus.
- Randomness or procedural generation: event order, routes, rank targets and
  stage terminal are authored; live trajectories vary under control and contact.
- Multiple viable strategies: clean grip driving, more aggressive overtakes or
  earlier/later nitrous use can satisfy the same targets.
- Typical replay motive: stage-time/Autolog optimisation, but all online and
  repeated stage comparison is excluded after the first retained completion.

## Adjacent systems and history

- Direct franchise corridor: Most Wanted (2005), Underground, Payback and
  Unbound share dedicated arcade driving, rivals and HUD state, but their
  reviewed packets settle one race, heist or forced loss rather than a
  cumulative three-event cross-country rank stage.
- Similar games: Forza Horizon 6 shares car selection, assists/difficulty,
  ordered races and retained campaign unlocks; Trackmania shares ordered route
  validity but has no rivals, finite checkpoint recovery or stage rank.
- Important differences: The Run makes recovery a difficulty-sized finite
  resource whose last use fails an event, then carries several event results
  into one persistent route rank. The BMW, San Francisco routes and numeric
  rank are scoped parameters, not gene names.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-291`, `ACT-292`, `ACT-309`, `ACT-350` | stock BMW, Normal, automatic, keys and timing are parameters |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-691`, `SYS-746` | traffic, rival target, XP and route rank are parameters |
| Constraint | `CON-282`, `CON-438`, `CON-577` | three events and five Normal resets are parameters |
| Information | `INF-204`, `INF-205`, `INF-208`, `INF-286` | HUD layout and numeric rank are presentation/parameters |
| Objective | `OBJ-146` | West Coast, 211th, 195th and Stage 2 are parameters |
| Time | `TIM-003` | frame rate and transition duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `234` (`GAME-0001`–`GAME-0234`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`11 / 24 = 0.458333`).
- Supported combination subsets: `COMB-0233`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` — Need for Speed Underground | `ACT-290`, `ACT-292`, `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-208`, `TIM-003` | Underground fixes one Easy two-lap race whose first-place result retains Bank. This packet chooses a Stage 1 car, admits ordinary nitrous and a difficulty-sized checkpoint-reset stock whose last use fails, then carries three event results into cumulative route rank and Stage 2 access. | Near, `0.458333` |

### Preserved research notes

- New genes: `SYS-746`, `CON-577`, `INF-286`, `OBJ-146`.
- Reused genes: `ACT-290`, `ACT-291`, `ACT-292`, `ACT-309`, `ACT-350`,
  `SYS-320`, `SYS-365`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-691`,
  `CON-282`, `CON-438`, `INF-204`, `INF-205`, `INF-208`, `TIM-003`.
- Classification result: `New gene`, supported reuse and one new verified
  interaction combination.
- Evidence and reasoning: generic vehicle input, rival/traffic simulation,
  ordered finish, nitrous and retained driving settlement already have exact
  lower-ID boundaries. Finite last-checkpoint recovery, its terminal stock,
  the joint reset/rank display and the cumulative stage terminal do not.

## Combination status

- `COMB-0233` is a verified strict subset of this genome. It couples assigned-
  car control, finite checkpoint recovery and a multi-event rival-rank terminal;
  car choice, generic traffic, nitrous and low-level route guidance stay outside.
- All `232` earlier verified combinations are scanned mechanically against this
  genome; none is assumed from franchise or racing similarity.

## Taxonomy impact

- Registry changes: add `SYS-746`, `CON-577`, `INF-286`, `OBJ-146`,
  `COMB-0233` and relevant existing family memberships.
- Taxonomy-change record: none; no earlier reviewed-game signature changes.
- Candidate terms affected: checkpoint reset, last passed checkpoint,
  difficulty-sized recovery stock, cumulative route rank and stage settlement.

## Negative results

- `SYS-369` is rejected: it restores a mission checkpoint after declared
  protagonist/mission failure and chosen retry, while this ruleset also permits
  a live manual vehicle reset and debits a dedicated stock before failure.
- `ACT-293` and `INF-206` are rejected: a fresh Stage 1 is an authored campaign
  chain, not a player-selected world-map event marker with a disclosed reward.
- `OBJ-134` is rejected: this terminal is a three-event cumulative rank stage,
  not one first-place rival race and its reward.
- Police vehicles and roadblocks remain authored hazards; no clearable wanted/
  search state is admitted, so `SYS-366` is rejected.
- Patch `1.1`, current Windows wrappers, DLC cars, retired online services and
  friend comparisons are excluded rather than silently merged.
