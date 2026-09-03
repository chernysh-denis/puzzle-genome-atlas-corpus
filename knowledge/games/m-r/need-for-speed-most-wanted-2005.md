---
game_id: GAME-0226
slug: need-for-speed-most-wanted-2005
game_title: "Need for Speed: Most Wanted (2005)"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0224
gene_ids:
  action:
    - ACT-130
    - ACT-229
    - ACT-290
    - ACT-292
    - ACT-309
  system:
    - SYS-320
    - SYS-368
    - SYS-515
    - SYS-691
    - SYS-729
  constraint:
    - CON-282
  information:
    - INF-119
    - INF-204
    - INF-205
  objective:
    - OBJ-142
  time:
    - TIM-003
---

# Game: Need for Speed: Most Wanted (2005)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: original standard-edition English Windows retail release
  by EA Black Box, updated only with Electronic Arts' official patch `1.3`.
  This is the 2005 game, not Criterion's distinct 2012 product.
- Platform and lawful artefact boundary: one lawfully owned or lawfully
  acquired original Windows optical-disc copy and valid product key on a
  period-compatible PC. No disc image, downloaded executable, crack,
  widescreen fix, compatibility wrapper, trainer or community patch is
  admitted. Patch `1.3` is the final cumulative official PC state; this unit
  does not claim an untested modern-Windows installation works.
- Mode: offline single-player Career with autosave enabled, automatic
  transmission and ordinary default controls. Black Edition bonus content is
  not used.
- Entry: a fresh Career profile has won the two required opening Sprints and
  the required two-lap Circuit. The bounded packet begins when the next fixed
  story race against Razor releases direct control of the supplied BMW M3 GTR.
  Those three races establish the reproducible gate but their driving choices
  are not unioned into this genome.
- Primary decision loop: read road shape, route cues, speed, gear, relative
  place, rival spacing, nitrous and Speedbreaker readiness; steer, accelerate,
  brake, handbrake, spend nitrous or activate Speedbreaker; let arcade motion,
  collision, the single rival and temporary focus modifiers resolve; continue
  until the fixed oil-leak/engine-failure trigger overrides race completion.
- Evaluation terminal: the Razor event deliberately has no winning finish.
  Allow the breakdown, loss, arrest/release and story transition to settle;
  with the ordinary `$30,000` fresh-profile grant, buy the fixed Lexus IS300,
  follow Mia's route to the safe house and allow autosave to retain the
  starter, remaining cash and Blacklist #15 career state.
- Negative terminal: quitting before the safe-house autosave or failing to
  complete the preceding three tutorial races does not produce the accepted
  terminal. Driving better cannot turn the Razor event into a normal win; its
  breakdown is an authored story result, not ordinary collision damage.
- Included: one supplied car and rival; direct driving; ordinary nitrous;
  Speedbreaker drain, temporary slow-motion/handling change and recharge;
  road contact and collision; race HUD; the authored breakdown and loss;
  `$30,000` start grant; Lexus purchase; safe-house drive and autosave.
- Excluded: the first two Sprints and two-lap Circuit as analysed play; every
  Blacklist event from Sonny onward; live pursuits, Heat, bounty, impound and
  pursuit breakers; tuning and visual customisation; Quick Race, Challenge
  Series, LAN and discontinued online; Black Edition extras; console/portable
  variants; the 2012 game; mods and the full career.
- Potential scoped modules: one Blacklist race, one live pursuit through
  Cooldown, a Speedtrap, Drag, Tollbooth, Challenge Series or later boss
  sequence each needs its own lawful entry and terminal.
- Direct-play status: not conducted. The packet is reconstructed from the
  licensed Prima Official Game Guide, a contemporary written PC walkthrough,
  the contemporary patch notice and Electronic Arts' current availability and
  history material. Relevant PDF pages were text-extracted and visually
  checked. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NFSMW-001` | The product is EA Black Box's original 2005 English Windows standard edition, not Criterion's 2012 game | Confirmed | Direct | High | P1, P2, P3 |
| `NFSMW-002` | The original is absent from EA's current digital catalogue; an original retail disc and key form the lawful artefact boundary | Confirmed | Corroborated | High | P1, P2 |
| `NFSMW-003` | Official PC patch `1.3`, released 2005-12-06, is the final cumulative original-PC update | Confirmed | Corroborated | High | S1, S2 |
| `NFSMW-004` | Fresh Career reaches the Razor race only after two Sprints and one two-lap Circuit are won | Observation | Corroborated | High | P3, S3 |
| `NFSMW-005` | The car exposes direct controls, ordinary regenerating nitrous and a regenerating Speedbreaker resource | Confirmed | Direct | High | P3, S3 |
| `NFSMW-006` | Road, speed, gear, place, route/rival relation and resource gauges support live line and timing choices | Observation | Corroborated | High | P3, S3 |
| `NFSMW-007` | The Razor race cannot finish normally: fixed oil leak and engine failure override performance and remove the supplied car | Observation | Corroborated | High | S3, S4 |
| `NFSMW-008` | The ordinary fresh-profile transition grants `$30,000`, offers affordable starters and directs the purchased car to the safe house | Observation | Corroborated | High | P3, S3, S4 |
| `NFSMW-009` | Buying Lexus IS300, entering the safe house and allowing autosave leaves retained starter/cash/Blacklist #15 state | Observation | Corroborated | Medium | P3, S3, S4 |
| `NFSMW-010` | Blacklist play, live pursuits, other race types, Black Edition extras and the 2012 game are separable from this packet | Confirmed | Corroborated | High | P1, P3, S3 |

## Basic data

- Release / origin: developed by EA Black Box and published by Electronic Arts
  for Windows in November 2005; English PC patch `1.3` followed on 2005-12-06.
- Platform or physical form: legacy Windows optical-disc software; only the
  declared standard-edition offline Career packet is admitted.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and licensed sources:
  - **[P1]** [Electronic Arts' Need for Speed history](https://www.ea.com/games/need-for-speed/need-for-speed-unbound/news/speedhunters-specialfeature-nfshistory),
    for the 2005 identity and separation from later games.
  - **[P2]** [Electronic Arts-hosted availability discussion](https://forums.ea.com/discussions/need-for-speed-franchise-discussion-en/how-do-i-download-nfs-most-wanted-2005-on-my-pcdigital-and-not-a-disc/9517144),
    for absent original digital availability and distinction from 2012.
  - **[P3]** [Prima Official Game Guide](https://www.ogxbox.co.uk/media/com_eshop/attachments/Need_For_Speed_Most_Wanted_Stratgy_Guide_Book.pdf),
    created in November 2005, for controls, nitrous, Speedbreaker, Career
    structure, safe-house role and the original rules surface.
- Preserved and reproducible sources:
  - **[S1]** [contemporary 4Gamer patch notice](https://www.4gamer.net/games/021/G002138/20051207123236/),
    for English `1.3` release date and repair scope.
  - **[S2]** [PCGamingWiki original-PC record](https://www.pcgamingwiki.com/wiki/Need_for_Speed%3A_Most_Wanted),
    for `1.3` as the last cumulative patch and separation of community fixes.
  - **[S3]** [contemporary written PC walkthrough](https://www.nfsplanet.com/data/nfsmw/nfsmw_faq_walkthrough_1.3.pdf),
    for the prologue gate, unfinished Razor race, `$30,000` grant, starter,
    safe-house/save behaviour and exact PC inputs.
  - **[S4]** [StrategyWiki prologue record](https://strategywiki.org/wiki/Need_for_Speed%3A_Most_Wanted/Prologue),
    for the oil-leak breakdown, starter purchase and safe-house route.
- Claim IDs: `NFSMW-001`–`NFSMW-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly drive the supplied BMW and later Lexus.
- Existing `ACT-292`: commit automatic transmission and default controls.
- Existing `ACT-309`: spend ordinary nitrous for directed acceleration.
- Existing `ACT-229`: activate or cancel the ready Speedbreaker ability.
- Existing `ACT-130`: spend post-loss cash on the offered Lexus IS300.
- Parameters: profile, cars, price, road line, controls, nitrous timing and
  Speedbreaker timing.
- Claim IDs: `NFSMW-004`–`NFSMW-009`.

### System Behaviour Genes

- Existing `SYS-320`: integrate arcade motion, traction and collision.
- Existing `SYS-515`: continuously route the single Razor rival.
- Existing `SYS-691`: debit nitrous and apply bounded acceleration; equipped
  charge regenerates during fast driving.
- Existing `SYS-368`: drain Speedbreaker while slow-time/handling modifiers
  apply, then restore readiness through eligible driving.
- New `SYS-729`: override ordinary race continuation with the fixed breakdown,
  remove the supplied car and advance starter acquisition plus safe-house
  autosave into retained early Career state.
- Resolution order: gate the race; release both cars; integrate driving, rival,
  collision and optional resources; trigger failure; settle loss and grant;
  validate purchase; restore driving; accept safe-house entry and autosave.
- Claim IDs: `NFSMW-004`–`NFSMW-009`.

### Constraint Genes

- Existing `CON-282`: two Sprints and the two-lap Circuit gate the Razor race;
  loss, starter purchase and safe-house entry remain ordered.
- Scarce strategic resources: route distance, speed, rival spacing, nitrous,
  Speedbreaker and the fixed post-loss cash grant.
- Claim IDs: `NFSMW-004`, `NFSMW-005`, `NFSMW-008`, `NFSMW-009`.

### Information Genes

- Existing `INF-204`: driving view exposes speed, gear, road and route cues.
- Existing `INF-205`: race HUD exposes place, progress and nearby rival.
- Existing `INF-119`: nitrous and Speedbreaker gauges expose resource state.
- Claim IDs: `NFSMW-005`, `NFSMW-006`.

### Objective Genes

- New `OBJ-142`: complete one forced-loss driving prologue, acquire the fixed
  replacement starter and reach retained early-campaign control.
- Success, evaluation and failure: completion is the autosaved safe-house
  state, not beating Razor; quitting earlier fails the analytical terminal.
- Claim IDs: `NFSMW-004`, `NFSMW-007`–`NFSMW-009`.

### Time Genes

- Existing `TIM-003`: motion, rival spacing, resource drain/recharge and route
  transitions advance continuously while driving choices remain live.
- Claim IDs: `NFSMW-005`–`NFSMW-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Career has won two Sprints and one two-lap Circuit | Continue the fixed prologue | Razor race loads and releases the supplied BMW against one rival | exact gated entry | `NFSMW-004` |
| Both cars are live | Steer, accelerate, brake or handbrake | Arcade motion, collision and rival spacing update | direct race authority | `NFSMW-005`, `NFSMW-006` |
| Nitrous is charged | Hold its input | Charge is spent and acceleration applies until release or depletion | finite boost | `NFSMW-005` |
| Speedbreaker has charge | Activate, steer, then cancel or exhaust | Time slows, handling changes and charge later regenerates | reversible focus | `NFSMW-005`, `NFSMW-006` |
| Authored trigger is reached | Continue driving regardless of pace | Engine failure overrides the race; no normal win settles | forced loss | `NFSMW-007` |
| Story loss and release settle | Accept the ordinary fresh-profile grant | `$30,000` and an affordable starter set become available | reset resources | `NFSMW-008` |
| Starter set is open | Buy Lexus IS300 | Price is debited and Lexus becomes the persistent starter | replacement choice | `NFSMW-008` |
| Safe-house route is active | Drive the Lexus to the marker | Entry exposes early Blacklist state and autosave retains it | evaluation terminal | `NFSMW-009` |
| Player quits before autosave | Leave the packet | No accepted retained terminal is established | arbitrary stop rejected | `NFSMW-009` |

## Strategic and experiential structure

- Local decision: choose braking/steering lines and time two performance
  resources against current rival spacing.
- Medium-term planning: preserve speed while balancing separately regenerating
  nitrous and Speedbreaker.
- Long-term structure: an apparent rival race becomes a fixed story loss, then
  converts prologue earnings into a replacement car and retained Career state.
- Common heuristics: brake before sharp steering; spend nitrous on a stable
  exit; reserve Speedbreaker for high-speed correction; after the reset follow
  the marked route rather than extending into open free roam.
- Failure attribution: HUD and road contact explain driving outcomes, while the
  fixed breakdown makes clear that losing the supplied car is not line error.
- Player-trust factors: resource gauges update; exceptional failure is
  consistent; starter price/cash are visible; safe-house autosave exposes
  retention.
- Claim IDs: `NFSMW-005`–`NFSMW-009`.

## Replay and variation

- What changes between attempts: line, contact, pace, resource timing and
  elapsed time to the trigger.
- Randomness or procedural generation: route, rival, breakdown, grant and
  terminal are authored; live trajectories vary with input and contact.
- Multiple viable strategies: clean grip lines, aggressive cornering, early or
  late nitrous and corrective Speedbreaker reach the same story transition.
- Typical replay motive: practise the route; no winning Razor branch exists.
- Claim IDs: `NFSMW-005`–`NFSMW-009`.

## Adjacent systems and history

- Direct predecessor: Underground 2 supplies franchise context but none of its
  tuning or progression enters this packet.
- Variants: Black Edition, consoles and portables are distinct artefacts;
  Criterion's 2012 Most Wanted is a separate game.
- Similar games: Need for Speed Underground shares direct arcade racing and an
  early Career state; Unbound shares street-race HUD and boost; Payback shares
  an authored driving mission with story-controlled transitions.
- Important differences: no normal finish settles this event. A fixed failure
  removes the car, and completion is a later replacement-car checkpoint rather
  than a finish reward, pursuit or delivery victory.
- Claim IDs: `NFSMW-001`, `NFSMW-004`–`NFSMW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-130`, `ACT-229`, `ACT-290`, `ACT-292`, `ACT-309` | cars, price, bindings and timing are parameters |
| System Behaviour | `SYS-320`, `SYS-368`, `SYS-515`, `SYS-691`, `SYS-729` | handling, recharge and trigger are parameters |
| Constraint | `CON-282` | predecessor races and story steps are parameters |
| Information | `INF-119`, `INF-204`, `INF-205` | HUD geometry is presentation |
| Objective | `OBJ-142` | rival, replacement and safe house are parameters |
| Time | `TIM-003` | frame rate and cutscene duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `225` (`GAME-0001`–`GAME-0225`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`7 / 23 = 0.304348`).
- Supported combination subsets: `COMB-0224`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` — Need for Speed Underground | `ACT-290`, `ACT-292`, `SYS-320`, `SYS-515`, `INF-204`, `INF-205`, `TIM-003` | Underground commits and wins a disclosed two-lap Circuit, validates an ordered finish and retains Bank. This packet instead admits nitrous and Speedbreaker, follows an authored story gate, denies normal finish authority, removes the supplied car and ends only after replacement purchase plus safe-house autosave. | Near, `0.304348` |

### Preserved research notes

- New genes: `SYS-729`, `OBJ-142`.
- Classification result: `New gene`.
- Evidence and reasoning: race-result genes require a valid finish or retained
  reward. Here breakdown overrides classification, removes the supplied car
  and makes the replacement-car safe-house checkpoint the terminal.

## Taxonomy impact

- Registry changes: add `SYS-729` and `OBJ-142`.
- Taxonomy-change record: none; no earlier game signature changes.
- Candidate terms affected: scripted driving loss and replacement-car reset.

## Negative results

- A race-win terminal was rejected because the event is authored not to
  finish. The loss is admitted only because starter purchase and autosave give
  it an explicit bounded evaluation state.
- The current EA Most Wanted product is the inadmissible 2012 game. Community
  executables and fixes are rejected as artefact substitutions.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Патч `1.3` є останнім накопичувальним
  оновленням оригінальної Windows-версії 2005 року (`NFSMW-003`).
- [Observation | Corroborated | High] Гонка проти Razor завершується заданою
  поломкою, а не звичайним фінішем (`NFSMW-007`).
- [Observation | Corroborated | Medium] Купівля Lexus IS300 і вхід до safe
  house утворюють збережений ранній стан кар'єри (`NFSMW-009`).

## Нові гени

- [Observation | Corroborated | High] `SYS-729` — перевести задану поломку
  автомобіля в збережений перезапуск кампанії.
- [Observation | Corroborated | High] `OBJ-142` — завершити пролог із
  неминучою поразкою та здобути збережене раннє керування кампанією.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0224` — керована гонка з двома
  ресурсами швидкості переходить через задану поломку до збереженої заміни.

## Зміни таксономії

- [Observation | Direct | High] Підписів раніше перевірених ігор не змінено.

## Нові питання

- Який окремий Blacklist-пакет найкраще ізолює живу поліцейську погоню та
  Cooldown, не об'єднуючи всю кар'єру?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | Medium] `GAME-0227` — Fortnite.
- Optimisation criterion: one current unranked Zero Build Solo match.
- Expected information gain: deployment, loot, storm, elimination and
  placement inside one live-service ruleset.
- Backlog impact: advances Batch 011 without consuming a reserve or the
  protected Need for Speed: The Run anchor.
