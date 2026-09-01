---
game_id: GAME-0199
slug: need-for-speed-unbound
game_title: "Need for Speed Unbound"
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0197
gene_ids:
  action:
    - ACT-290
    - ACT-292
    - ACT-293
    - ACT-357
  system:
    - SYS-320
    - SYS-365
    - SYS-366
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-641
    - SYS-642
  constraint:
    - CON-328
    - CON-437
    - CON-438
    - CON-523
  information:
    - INF-144
    - INF-204
    - INF-205
    - INF-206
    - INF-208
    - INF-255
  objective:
    - OBJ-122
  time:
    - TIM-003
---

# Game: Need for Speed Unbound

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: final unmodified Windows Steam base game, official Vol.
  `9.0.2`, public build `16690907`, checked `2026-08-31`; a fresh Story save on
  `Relaxed` difficulty, automatic gearbox and default driving controls; fixed
  `1998 Nissan Silvia K's` starter; prologue night A+ Speed Race `Shopping
  Spree`, buy-in `$0`, displayed reward `$6,000`, one player plus seven
  difficulty-scaled rivals, followed by its mandatory Lakeshore Police
  Department pursuit and return to Rydell's Rydes.
- Primary decision loop: read speed, gear, route, place, rival/traffic spacing,
  Burst Nitrous reserve, cash and Heat; steer, accelerate, brake, drift or spend
  Burst Nitrous; let vehicle, traffic and rival motion resolve; validate every
  route gate and the classified finish; then read police perception, choose a
  route or hiding line, break sight through the complete search interval and
  reach Rydell's Rydes so the event cash and result become retained.
- Entry and exit: begins at the accepted `Shopping Spree` event card after the
  fresh Story starter and `Relaxed` profile are fixed. It ends only after a
  valid ordered finish, mandatory pursuit escape and garage entry expose the
  retained result. Missing a checkpoint prevents classification; a restart
  resets the event attempt; being busted forfeits exposed cash and invalidates
  the accepted success trace rather than serving as its terminal substitute.
- Included: the fixed starter and difficulty; current A+ event card, `$0`
  buy-in, `$6,000` advertised reward and eight-place payout table; seven AI
  rivals; authored street route, ordered checkpoints, traffic and collisions;
  grip/drift, drafting and near-miss inputs that fill Burst Nitrous; Burst
  spending; live place, route, speed, gear, nitrous, cash and Heat information;
  classified finish, cash exposure, event Heat gain, forced police pursuit,
  line-of-sight search, escape and Rydell's Rydes banking/result settlement.
- Excluded: Lakeshore Online, multiplayer, Linkups, playlists, Speed Pass and
  ranked progression; Ultimate Collection, DLC and paid car packs; every car
  except the fixed starter; tuning, wraps, cosmetics and side bets; later Story
  days, other meetups/races, weekly Qualifiers and The Grand; collectibles,
  challenges, deliveries and open-ended free roam; deliberate police combat,
  arrest as an accepted terminal, restarts after the bounded trace and history
  before final Vol. `9.0.2`.
- Potential scoped modules: a paid-buy-in race with one fixed side bet; one
  later high-Heat night; one Qualifier; one Online playlist; one pursuit where
  vehicle takedowns are admitted. Each requires a separate current packet.
- Direct-play status: not conducted. Official EA product, accessibility,
  features and Under the Hood material pins the current Story settings,
  Burst-Nitrous loop, risk/Heat/cash structure and police escape. The maintained
  Story record and current unmodified event recording pin `Shopping Spree`, the
  prologue pursuit/garage terminal, route card and eight-place race surface.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NFSU-001` | Vol. `9.0.2` / public build `16690907` is the final reviewed Windows Steam rules state | Confirmed | Corroborated | High | P1, P2, S1 |
| `NFSU-002` | Story difficulty offers Relaxed, Challenging and Intense; Relaxed fixes 150% vehicle health, ten restarts, less-challenging cops and less-competitive rivals | Confirmed | Direct | High | P3 |
| `NFSU-003` | A fresh Story prologue fixes one selected starter and makes `Shopping Spree` the only available night event before a required post-race police escape and garage return | Observation | Corroborated | High | S2, S3 |
| `NFSU-004` | The current `Shopping Spree` card is an A+ Speed Race with `$0` buy-in, `$6,000` displayed reward, one player and seven classified rivals | Observation | Direct | High | S3 |
| `NFSU-005` | Direct driving, traffic, seven rivals and ordered route progress produce an eight-place classified result | Observation | Corroborated | High | P4, S3 |
| `NFSU-006` | Grip/drift actions and drafting fill Burst Nitrous, which can be spent for tactical acceleration | Confirmed | Direct | High | P4, P5 |
| `NFSU-007` | Racing builds Heat; police pressure escalates with Heat and escape requires breaking perception through the search state | Confirmed | Direct | High | P4, P6 |
| `NFSU-008` | Race earnings remain exposed until an eligible garage return, while a bust loses the exposed cash | Confirmed | Direct | High | P6 |
| `NFSU-009` | Online, Speed Pass, later Qualifiers, DLC cars and open-ended campaign play are separable from this one base-game Story event | Confirmed | Direct | High | P1, P2, P4 |

## Basic data

- Release / origin: `2022`, Criterion Games / Electronic Arts; final content
  line reached official Vol. `9.0.2` in December 2024 and EA announced the end
  of updates in February 2025.
- Platform or physical form: unmodified Windows PC base game through Steam;
  PlayStation 5, Xbox Series X|S and Online modes are outside the asserted run.
- Puzzle family: real-time vehicle control, adversarial route optimisation,
  temporary performance-resource timing and pursuit-risk settlement.
- Primary and official sources:
  - `P1` — [official Vol. 9.0.2 patch notes](https://www.ea.com/pl/games/need-for-speed/need-for-speed-unbound/news/vol9-0-2-patch-notes),
    for the final official patch boundary.
  - `P2` — [official Need for Speed series page](https://www.ea.com/games/need-for-speed),
    for current base-game availability and EA's End of Kaizen statement that no
    further Unbound updates are planned.
  - `P3` — [official accessibility resource](https://www.ea.com/able/resources/need-for-speed-unbound?isLocalized=true),
    for PC controls/HUD, the three Story difficulties and exact Relaxed health,
    restart, police and rival parameters.
  - `P4` — [official features page](https://www.ea.com/en/games/need-for-speed/need-for-speed-unbound/features),
    for Story racing, risk, Burst Nitrous, Heat, police pressure and escape.
  - `P5` — [official Run These Streets systems article](https://forums.ea.com/discussions/need-for-speed-unbound-discussion-en/need-for-speed%E2%84%A2-unbound-under-the-hood---run-these-streets/9398552),
    for grip/drift and drafting contributions to Burst Nitrous, burst spending,
    off-road traction consequences and police evasion.
  - `P6` — [official Risk & Reward systems article](https://forums.ea.com/discussions/need-for-speed-unbound-discussion-en/under-the-hood-turn-up-the-heat---risk--reward-in-need-for-speed-unbound/9397803),
    for event Heat, escalating police tactics, cash exposure, bust loss and
    garage banking.
- Secondary and reproducible sources:
  - `S1` — [Steam public-depot record](https://steamdb.info/app/1846380/depots/),
    observed `2026-08-31`, for public build `16690907` only.
  - `S2` — [maintained Story prologue record](https://nfs.fandom.com/wiki/Need_for_Speed:_Unbound/Story/Prologue),
    for starter choices, `Shopping Spree` as the only available night event,
    its required LPD pursuit and return to Rydell's Rydes.
  - `S3` — [current unmodified `Shopping Spree` recording](https://www.dailymotion.com/video/x8xn2ve),
    inspected `2026-08-31`, for the A+ Speed Race card, `$0` buy-in, `$6,000`
    displayed reward, eight-place field, route, HUD, finish and pursuit.
- Claim IDs: `NFSU-001`–`NFSU-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate, brake, reverse and use the
  handbrake of the fixed Silvia without an enter/exit loop.
- Existing `ACT-292`: commit the `Relaxed` Story difficulty and automatic
  gearbox profile before event entry.
- Existing `ACT-293`: commit the available `Shopping Spree` marker and its
  route, class, `$0` buy-in, field and result rules.
- New `ACT-357`: spend the currently accumulated Burst Nitrous reserve for a
  tactical acceleration burst during race or pursuit.
- Parameters: starter, controls, gearbox, difficulty, route, throttle, brake,
  steering, drift/grip line, Burst amount and activation timing.
- Claim IDs: `NFSU-002`–`NFSU-006`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the fixed car's input, road/off-road contact,
  traffic collision and vehicle damage.
- Existing `SYS-365`: route ambient Lakeshore traffic through race and pursuit
  space while collisions remain mechanically live.
- Existing `SYS-366`: convert event-built Heat into matching LPD pursuit,
  perception, search and clearance.
- Existing `SYS-515`: drive seven route rivals under the Relaxed profile.
- Existing `SYS-516`: validate ordered course progress and the complete
  eight-place finish result.
- Existing `SYS-519`: retain the valid event result and declared cash only when
  the bounded garage settlement succeeds.
- New `SYS-641`: convert grip/drift driving, drafting and other eligible skill
  events into Burst Nitrous reserve, then convert an activation into temporary
  acceleration.
- New `SYS-642`: hold classified race earnings as exposed cash through the
  forced pursuit, then bank them on eligible garage entry or remove them on a
  bust.
- Resolution order: validate event/car/profile; instantiate route, traffic and
  rival field; integrate driving and eligible Burst gains/spending; accept
  ordered checkpoints; classify finish and expose payout/Heat; instantiate
  police pressure; resolve perception and search; clear pursuit; validate
  Rydell's Rydes entry; retain result and cash.
- Claim IDs: `NFSU-004`–`NFSU-008`.

### Constraint Genes

- Existing `CON-328`: the LPD search clears only after the car leaves active
  police perception and stays undiscovered through the required interval.
- Existing `CON-437`: `Shopping Spree` admits only the fixed eligible A+ Story
  car packet.
- Existing `CON-438`: every route checkpoint must be crossed in order before
  the finish can classify.
- New `CON-523`: exposed event cash cannot become retained while police pursuit
  remains active; valid garage entry is gated by escape.
- Scarce strategic resources: route position, speed, Burst reserve, vehicle
  health, finite Relaxed restarts, exposed cash, Heat and unseen search time.
- Claim IDs: `NFSU-002`, `NFSU-004`–`NFSU-008`.

### Information Genes

- Existing `INF-144`: map/minimap guidance and current LPD pursuit/search state
  expose evasion routes and police perception.
- Existing `INF-204`: driving view exposes speed, gear, route and braking cues.
- Existing `INF-205`: race HUD exposes place, course progress, time and nearby
  rivals.
- Existing `INF-206`: event card exposes A+ class, route, `$0` buy-in, payout
  table, `$6,000` reward and Heat gain before commitment.
- Existing `INF-208`: result/garage transitions expose classified performance
  and retained cash separately from live race position.
- New `INF-255`: the live interface jointly exposes Burst Nitrous reserve,
  current Heat, exposed cash and police perception/search state.
- Claim IDs: `NFSU-004`–`NFSU-008`.

### Objective Genes

- New `OBJ-122`: complete and classify `Shopping Spree`, evade its mandatory
  LPD pursuit and enter Rydell's Rydes with the event result retained.
- Success, evaluation and failure: any valid classified place may continue the
  bounded trace, but the accepted terminal requires escape plus garage entry.
  Missing a gate or restarting yields no result; a bust loses exposed cash and
  invalidates the success trace.
- Claim IDs: `NFSU-003`–`NFSU-008`.

### Time Genes

- Existing `TIM-003`: vehicle, traffic, rivals, Burst opportunities, police and
  search state advance in continuous time while driving decisions remain live.
- Claim IDs: `NFSU-005`–`NFSU-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Story setup is open | Select Relaxed, automatic gearbox and the 1998 Nissan Silvia K's | The prologue retains one fixed health/restart/cop/rival profile and starter | exact participant packet | `NFSU-002`, `NFSU-003` |
| Prologue night exposes its only event | Open and commit `Shopping Spree` | A+ Speed Race, `$0` buy-in, displayed `$6,000` reward, route and eight-place field instantiate | exact event contract | `NFSU-003`, `NFSU-004` |
| Start releases the eight cars | Steer, accelerate, brake and choose grip/drift lines | Physics, traffic and seven Relaxed rivals advance while speed, place and route update | live race authority | `NFSU-005` |
| Draft, grip/drift action or another eligible skill event resolves | Continue the manoeuvre, then activate Burst Nitrous | Reserve fills from the eligible event and spending it produces temporary acceleration | earned tactical boost | `NFSU-006` |
| A required checkpoint lies ahead | Cross it in authored order | Course progress advances; bypassing it prevents later finish classification | ordered route validity | `NFSU-005` |
| Final checkpoint chain is valid | Cross the finish | Complete place table settles, payout becomes exposed cash and event Heat is applied | race result is not yet banked | `NFSU-004`, `NFSU-007`, `NFSU-008` |
| Mandatory LPD pursuit is active | Break sight and remain outside perception through search | Direct pursuit becomes spatial search and then clears only after the unseen interval | bounded escape | `NFSU-007` |
| Pursuit has cleared | Follow the route and enter Rydell's Rydes | Garage accepts entry and retains the event result/cash | bounded positive terminal | `NFSU-008` |
| Police complete a bust before garage entry | Allow bust settlement | Exposed cash is removed and the accepted success trace is invalid | risk has consequence | `NFSU-008` |

## Strategic and experiential structure

- Local decision: brake or commit to a line, draft or pass a rival, earn Burst
  through a riskier manoeuvre, spend it now, or preserve it for exit speed.
- Medium-term planning: trade a shorter line against traffic/contact risk;
  preserve vehicle health and route position; after finish, trade direct speed
  against breaking sight and choosing a low-exposure path to the garage.
- Long-term structure: turn one event commitment into a classified race result,
  survive the resulting Heat and convert exposed winnings into retained cash.
- Common heuristics: enter corners below loss-of-grip speed; drift only when the
  exit supports it; draft before spending Burst; avoid off-road grip loss; in a
  pursuit, break line of sight before hiding rather than stopping while seen.
- Failure attribution: missed-gate state, place list, speed/gear, Burst meter,
  damage, Heat, police markers/search and exposed cash distinguish route error,
  poor boost timing, collision, failed evasion and bust.
- Player-trust factors: event terms are disclosed before entry; ordered gates
  explain classification; the pursuit/search transition is visible; garage
  entry visibly separates exposed from retained earnings.
- Claim IDs: `NFSU-004`–`NFSU-008`.

## Replay and variation

- What changes between attempts: grid interaction, rival/traffic trajectories,
  line, Burst generation/spending, finish place, police contacts, escape route
  and retained amount. Car, event, difficulty and terminal remain fixed.
- Randomness or procedural generation: route and event table are authored;
  AI/traffic behaviour and police encounters vary inside the fixed packet.
- Multiple viable strategies: grip-biased clean racing, controlled drifting,
  drafting passes, early or late Burst expenditure and speed- or concealment-
  biased escape can reach the same garage terminal.
- Typical replay motive: improve place, payout, line, Burst efficiency and
  escape reliability. Later Story progression is outside this one trace.
- Claim IDs: `NFSU-003`–`NFSU-008`.

## Adjacent systems and history

- Direct predecessors: earlier Need for Speed games establish the franchise
  format but do not supply evidence for Unbound's final Burst, Heat or Story
  packet.
- Variants: later events add buy-ins/side bets and higher Heat; Qualifiers add
  campaign gates; Online changes authority and progression; Volumes and DLC add
  content but are excluded from this base-game event.
- Similar games: Forza Horizon 6 shares direct car control, difficulty-scaled
  rivals and ordered result validation; Grand Theft Auto V shares traffic,
  wanted pursuit and unseen search; Rocket League shares a spendable vehicle
  acceleration reserve; BeamNG.drive shares route validation but not rivals,
  police or cash risk.
- Important differences: `Shopping Spree` couples one classified street race
  to a mandatory police phase and delays durable reward until escape plus
  garage entry. Burst is earned through driving technique rather than collected
  from fixed arena pads.
- Claim IDs: `NFSU-005`–`NFSU-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-292`, `ACT-293`, `ACT-357` | fixed direct drive, difficulty/event commitment and Burst spending |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-366`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-641`, `SYS-642` | car/traffic/rivals, route, Heat pursuit, Burst and at-risk cash |
| Constraint | `CON-328`, `CON-437`, `CON-438`, `CON-523` | unseen escape, A+ eligibility, ordered route and garage gate |
| Information | `INF-144`, `INF-204`–`INF-206`, `INF-208`, `INF-255` | route/race/event/result plus Burst, Heat and cash state |
| Objective | `OBJ-122` | classify, escape and retain at Rydell's Rydes |
| Time | `TIM-003` | continuous race and pursuit |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `198` (`GAME-0001`–`GAME-0198`).
- Exact genome matches: none.
- Tied near matches: `GAME-0171` — Forza Horizon 6 (`15 / 35 = 0.428571`).
- Supported combination subsets: `COMB-0197`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Forza Horizon 6 (`GAME-0171`) | `ACT-290`, `ACT-292`, `ACT-293`, `SYS-320`, `SYS-365`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-437`, `CON-438`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Both fix a driving profile and eligible event, then couple direct car control, traffic, difficulty-scaled rivals, ordered course validation and a retained result. Forza permits route selection, car switching and Rewind while converting multiple event results into Festival points and a mandatory Invitational/Wristband gate; Unbound fixes one car/event, earns and spends Burst, carries event Heat into a mandatory LPD pursuit and withholds cash retention until unseen escape plus garage entry. | Near, `0.428571` |

### Preserved research notes

- New genes: `ACT-357`, `SYS-641`, `SYS-642`, `CON-523`, `INF-255`,
  `OBJ-122`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing driving, race-result, traffic, pursuit and
  campaign-settlement records cover the reusable corridor. New records isolate
  only Unbound's earned Burst activation, at-risk earnings through forced
  pursuit, the garage-after-escape gate, joint risk HUD and exact terminal.

## Taxonomy impact

- Registry changes: six new Active definitions; new Unbound support for
  eighteen existing records. Generic driving-event, Heat and result wording is
  widened without changing any earlier reviewed signature.
- Taxonomy-change record: none; no prior game signature changes.
- Candidate terms affected: Burst Nitrous, grip/drift gain, drafting, street
  race, buy-in, payout table, Heat, pursuit, search, bust, exposed cash and
  garage banking.

## Negative results

- Rocket League's `ACT-309` and boost-pad system genes are rejected because
  Unbound earns Burst through driving events rather than spatial pad pickup.
- Forza campaign-point and Wristband genes are rejected because this one event
  ends before any Qualifier gate and admits no campaign threshold.
- BeamNG soft-body and mission-recovery genes are rejected because Unbound uses
  conventional vehicle damage and bounded Story restarts.
- GTA protagonist/weapon/crime-action genes are rejected because Heat arises
  from the selected race packet and direct weapon combat is excluded.
- Side bets, paid entry, tuning, weekly progression and Online rank are excluded
  parameters, not latent genes.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Relaxed fixes health, restart, police and rival
  parameters; `Shopping Spree` then forces a pursuit before garage settlement
  (`NFSU-002`, `NFSU-003`, `NFSU-008`).
- [Observation | Direct | High] The current event card fixes A+, `$0` buy-in,
  `$6,000` displayed reward and an eight-place field (`NFSU-004`).

## Нові гени

- [Observation | Corroborated | High] Six genes isolate earned Burst spending,
  exposed-cash settlement, pursuit-gated garage entry, joint risk information
  and the race-to-garage objective.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0197` records the strict subset that
  couples a classified street race, technique-earned Burst, Heat pursuit and
  garage-only retention.

## Зміни таксономії

- [Observation | Direct | High] Раніше перевірені сигнатури не змінено;
  узагальнено лише докази для повторно використаних автомобільних меж.

## Нові питання

- Which later arcade racer reuses technique-earned Burst and a classified
  route while falsifying the pursuit-gated cash terminal?

## Наступна рекомендована гра

- [Confirmed | Corroborated | High] `GAME-0200` Delta Force.
- Optimisation criterion: continue the recorded Selection 008 order after one
  complete local game commit.
- Expected information gain: test a changing large-team attack/defend packet
  against the current shooter and vehicle corridors.
- Backlog impact: advances the active 198-to-207 Goal by one bounded unit.

## Чому саме вона

- [Confirmed | Corroborated | High] Delta Force is the next recorded selection;
  starting any other title would violate the ordered horizon.
