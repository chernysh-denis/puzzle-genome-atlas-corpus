---
game_id: GAME-0244
slug: need-for-speed-heat
game_title: "Need for Speed Heat"
analysis_status: reviewed
reviewed: 2026-09-04
combination_ids:
  - COMB-0242
gene_ids:
  action:
    - ACT-290
    - ACT-292
    - ACT-293
    - ACT-341
    - ACT-418
  system:
    - SYS-299
    - SYS-320
    - SYS-365
    - SYS-366
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-767
    - SYS-768
    - SYS-769
  constraint:
    - CON-438
    - CON-523
    - CON-588
  information:
    - INF-144
    - INF-204
    - INF-205
    - INF-206
    - INF-208
    - INF-294
  objective:
    - OBJ-152
  time:
    - TIM-003
---

# Game: Need for Speed Heat

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: unmodified English Windows Steam `app 1222680`, currently
  sold as Deluxe Edition; public Build ID `10351341`, observed 2026-09-04.
  The official June 9, 2020 PC update supplies the reviewed gameplay boundary;
  the 2023 Steam packaging build is not asserted to be a new gameplay patch.
  Play Solo campaign, Easy difficulty, automatic transmission and default
  keyboard driving controls; no mods or community executable.
- Entry: a fresh campaign after Test Drive, with the selected Nissan 180SX
  Type X '96 starter and unchanged starter parts. The unsuccessful Part Shop
  visit precedes the first night; the nitrous purchase has not occurred.
  Follow Make a Name to its Hard Stop Sprint in Eden Shores. Begin this packet
  when committing that first-night event, at REP level 1, before any other
  night event. The opening daytime race and escort to the marker are setup,
  not additional admitted races. The recorded event recommendation is 120,
  not an enforced minimum performance-class restriction.
- Primary decision loop: read route, speed, place, traffic, vehicle condition,
  night REP, HEAT and police state; steer, accelerate, brake or powerslide
  through the ordered sprint; after classification, choose a safe-house route,
  evade any acquired pursuit, use an eligible drive-through repair or accept
  an offered affordable bribe, then enter the safe house to settle the night.
- Positive terminal: a valid classified Hard Stop finish followed by the
  first eligible safe-house entry, with night REP and its HEAT multiplier
  settled and Make a Name's completion/reward retained. Winning is desirable
  but not the mission's required finish predicate. A police encounter is
  possible, not mandatory; avoiding detection is a valid success route.
- Negative terminal: Busted or Wrecked before voluntary safe-house settlement
  ends this attempt. A bust removes Bank and resets HEAT/multiplier; the record
  does not invent an exact penalty or claim that all base REP is lost. A
  non-pursuit wreck returns to a garage but is not accepted as the positive
  route. Quit/restart similarly supplies no accepted successful trace.
- Included: one starter, difficulty and control profile; one night sprint;
  traffic, rivals, contact and damage; ordered course classification;
  conditional police pursuit, search, reacquisition and evasion; persistent
  night HEAT, REP exposure, finite roadside repairs, the low-HEAT bribe option,
  eligible safe-house entry, reward/REP progression and mission retention.
- Fixed economic parameters: Deluxe's advertised 5% REP and Bank bonuses stay
  active; they are not silently replaced by Standard Edition rates. Start
  without crew bonuses: if assigned to a Starter Crew before event entry,
  use Social > Crews > Members > Leave Crew, as the official manual permits.
  Do not join another crew during the packet. Record entry Bank and the event
  card; do not substitute the community base reward for a measured Deluxe
  payout. A new nightly repair allowance is three; prior daytime repairs do
  not consume it. The exact money, REP rounding and finish field size are not
  asserted as directly measured values.
- Excluded: Play Online, cross-play, crew progression, challenges, collectibles,
  other night events, daytime racing inside the packet, High Heat events,
  deliberate high-HEAT farming, drift/time trials, Black Market deliveries,
  paid or Deluxe cars, installed nitrous/auxiliaries, tuning and purchases,
  later missions, full campaign, other platforms and historical-rule unions.
  An unavoidable ordinary collision or police response is not excluded merely
  because the successful example avoids it.
- Potential scoped modules: one upgraded nitrous loadout, a High Heat event,
  crew-enabled session, day race, Black Market contract or online event.
- Direct-play status: not conducted. This is a textual evidence-backed rules
  reconstruction, not a claim of local Windows installation or entitlement.
  EA's PC manual, handling/police articles and updates establish mechanics;
  the Steam storefront establishes legal availability, SteamDB identifies the
  observed public build, and written mission records fix the early event.
  A muted, non-autoplay YouTube embed returned Error 153 before playback and
  was closed. No video frames or audio were played, heard, analysed or used;
  there are no video timecodes in the admitted evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HEAT-001` | Steam offers the English Windows Deluxe product with EA activation/client requirements and 5% REP/Bank bonuses | Confirmed | Direct | High | P1 |
| `HEAT-002` | Public build `10351341` is the observed packaging state; the June 2020 PC update is the official gameplay reference | Observation | Corroborated | Medium | P2, S1 |
| `HEAT-003` | Test Drive supplies a starter and a closed Part Shop visit before Make a Name's first-night Hard Stop sprint | Observation | Corroborated | Medium | P2, S2, S3, S4 |
| `HEAT-004` | Easy/automatic controls, direct handling, traffic and AI racing produce a classified sprint finish | Confirmed | Corroborated | High | P3, P4, P2, S2 |
| `HEAT-005` | The early mission accepts race completion followed by safety; further racing is optional and pursuit depends on detection | Observation | Corroborated | High | S2, P3, P5 |
| `HEAT-006` | Night HEAT increases reward exposure and police pressure; eligible garage entry settles multiplied REP, while a bust debits Bank and resets HEAT | Confirmed | Direct | High | P3, P5 |
| `HEAT-007` | Driving through a gas station restores vehicle health, with three repairs shared across one night | Confirmed | Direct | High | P3, P5 |
| `HEAT-008` | An offered low-HEAT bribe spends Bank to disengage without forfeiting the HEAT multiplier | Confirmed | Direct | High | P3, P5 |
| `HEAT-009` | Crew bonuses can affect solo earnings; Leave Crew removes that optional membership before the bounded trace | Confirmed | Direct | High | P3 |
| `HEAT-010` | Update 1.5 explicitly corrected Make a Name reward banking on the first garage return | Confirmed | Direct | High | P6 |

## Basic data

- Release / origin: Ghost Games / Electronic Arts, 2019; Steam release
  June 4, 2020. The scope does not combine Heat with another NFS product.
- Platform or physical form: lawful Windows Steam Deluxe distribution with
  EA account/client activation; no console, mobile or unofficial build.
- Puzzle family: direct vehicle control, real-time adversarial routing and
  resource-risk settlement.
- Primary and official sources, accessed 2026-09-04:
  - `P1` — [Steam product and Deluxe terms](https://store.steampowered.com/app/1222680/),
    for availability, Windows, account/client and edition modifiers.
  - `P2` — [EA June update announcement](https://forums.ea.com/discussions/need-for-speed-franchise-discussion-en/need-for-speed-heat---june-update---update-notes/9471414),
    official EA_David post, for PC release, police/AI fixes and the starter.
  - `P3` — [EA PC text manual](https://www.ea.com/able/resources/need-for-speed/need-for-speed-heat/pc/text-manual),
    especially Controls, Day/Night, Garage, Events, Cops and Crews.
  - `P4` — [Ghost's handling model article](https://www.ea.com/games/battlefield/news/under-the-hood-the-handling-model),
    for direct throttle/brake/steering, grip, powersliding and contact context.
    The current EA URL is categorised under Battlefield, but the article itself
    explicitly concerns Heat and is signed by the Ghost Driving Experience Team.
  - `P5` — [EA police-escape guide](https://www.ea.com/games/battlefield/news/nfs-tips-and-tricks-get-away-from-cops),
    for escape geometry, repair limits, escalating units and low-HEAT bribes.
  - `P6` — [EA update 1.5](https://forums.ea.com/discussions/-/-/9428367),
    for the specific first-night mission-banking correction.
- Corroborating textual sources, accessed 2026-09-04:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/1222680/depots/),
    build `10351341`, built January 18 and made public January 27, 2023.
  - `S2` — [Make a Name mission record](https://nfs.fandom.com/wiki/Make_A_Name),
    mechanical objectives and synopsis only, not its dialogue transcript.
  - `S3` — [Test Drive mission record](https://nfs.fandom.com/wiki/Test_Drive),
    starter choice and unsuccessful pre-night Part Shop visit.
  - `S4` — [Heat event table](https://nfs.fandom.com/wiki/Need_for_Speed%3A_Heat/Race),
    for Hard Stop's REP-1 recommendation, distinguished from the REP-22 variant.
- Claim IDs: `HEAT-001`–`HEAT-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: steer, accelerate, brake and handbrake the dedicated car;
  powersliding changes its line without a separate on-foot/seat-transfer loop.
- Existing `ACT-292`: commit Easy rivals and automatic transmission.
- Existing `ACT-293`: commit the available first-night Hard Stop marker.
- Existing `ACT-341`: activate the reachable eligible safe-house entrance.
- New `ACT-418`: accept a currently offered affordable disengagement payment.
- Parameters: starter, inputs, road line, difficulty, event, safe house and
  bribe offer; no car, mission name or currency amount becomes a gene.
- Claims: `HEAT-003`–`HEAT-009`.

### System Behaviour Genes

- Existing `SYS-299`: apply settled REP to retained level/unlock thresholds.
- Existing `SYS-320`: integrate vehicle motion, traction, contact and damage.
- Existing `SYS-365`: advance collidable ambient road traffic.
- Existing `SYS-366`: acquire and escalate police pursuit, then resolve loss
  of perception, search and clearance. This reuses pursuit/search behaviour,
  not an assertion that the separate night HEAT meter disappears on evasion.
- Existing `SYS-515`: drive the Easy autonomous racing field.
- Existing `SYS-516`: validate ordered sprint progress and classify finish.
- Existing `SYS-519`: retain the accepted driving mission and declared rewards.
- New `SYS-767`: retain session notoriety after encounters and apply its
  multiplier when banking reputation; capture instead resets that multiplier
  and applies the declared financial penalty.
- New `SYS-768`: a drive-through service trigger restores vehicle condition
  and consumes one use from the shared session repair allowance.
- New `SYS-769`: settle an accepted bribe into a debit and disengagement while
  preserving accumulated session notoriety/reward exposure.
- Resolution: commit settings/event; integrate input, rivals, traffic and
  checkpoint order; classify race and accrue night REP/HEAT; route toward safety;
  resolve any perception, pursuit, collision, repair or bribe; accept eligible
  safe-house entry; settle REP, level effects and mission state. Capture or
  wreck settles a negative attempt instead. Claims: `HEAT-004`–`HEAT-010`.

### Constraint Genes

- Existing `CON-438`: missed or out-of-order route gates do not give a valid
  sprint finish; a recommendation of 120 is not the same as a hard class gate.
- Existing `CON-523`: if a pursuit has started, exposed race gains cannot be
  voluntarily banked while police pursuit/search remains active. A run that
  avoids police needs no artificial chase before its eligible entrance.
- New `CON-588`: roadside restoration requires a live vehicle at the service
  trigger and remaining shared session allowance; another station does not
  bypass the exhausted allowance.
- Scarce parameters: condition, route position, Bank, unbanked REP, HEAT,
  repair uses and the brief affordable bribe opportunity. No new numeric
  difficulty, car-rating or reward-threshold gene is admitted.
- Claims: `HEAT-004`–`HEAT-008`.

### Information Genes

- Existing `INF-144`: map, route and police/search information support evasion.
- Existing `INF-204`: speed, gear and road guidance support line control.
- Existing `INF-205`: current place, progress and rivals explain race position.
- Existing `INF-206`: event/map information exposes the selected sprint terms.
- Existing `INF-208`: result and garage screens distinguish finish from retained
  rewards and progress.
- New `INF-294`: live condition, session notoriety and exposed reputation,
  together with available service/payment feedback, explain the return risk.
- Claims: `HEAT-004`–`HEAT-010`.

### Objective Genes

- New `OBJ-152`: classify one night race and voluntarily bank the session's
  reputation at an eligible refuge; avoid or resolve encounters on the way.
- Neither a first-place-only predicate nor a mandatory chase is imported from
  another game. Bust/wreck, restart and an unbanked race finish are not the
  accepted positive terminal. Claims: `HEAT-005`, `HEAT-006`, `HEAT-010`.

### Time Genes

- Existing `TIM-003`: movement, rivals, traffic, police and opportunities advance
  continuously during unpaused driving. No separate fictional overnight clock
  or fixed countdown-to-dawn is asserted. Claims: `HEAT-004`–`HEAT-008`.

## Reproducible transitions

These are source-backed state tests, not fabricated local play observations.
Exact trajectories and amounts vary; the conditional resolution is the test.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh first-night starter, Easy/automatic, no installed kit or crew bonus | Commit Hard Stop in Make a Name | The REP-1 sprint begins under fixed controls and event terms | reproducible entry, not REP-22 variant | `HEAT-001`, `HEAT-003`, `HEAT-009` |
| A required route gate is ahead | Cross in order, or miss it | Valid progress advances; a missed gate cannot become a valid finish merely by reaching the end | route legality | `HEAT-004` |
| Road contact or a rival blocks the chosen line | Brake, steer or powerslide | Traction, collision, condition and relative position resolve live | direct control rather than TouchDrive | `HEAT-004` |
| The ordered sprint is complete | Cross the finish at a valid classified place | The mission proceeds toward safety with night REP/HEAT still awaiting settlement | finish is not banking or a mandatory win | `HEAT-005`, `HEAT-006` |
| No patrol has acquired the car | Drive to an eligible safe house | A successful return does not require provoking police | conditional pursuit | `HEAT-005` |
| Police have acquired the car | Break perception and avoid reacquisition | Active pursuit/search clears, but accumulated night HEAT still matters | encounter clearance differs from session reset | `HEAT-006` |
| Live damaged car, repair use remains | Drive through an eligible gas station | Condition is restored and one shared nightly use is spent | restorative route detour | `HEAT-007` |
| All three nightly service uses were spent | Visit another gas station | No fourth nightly restoration becomes legal | global session quota, not per-station stock | `HEAT-007` |
| Affordable bribe is offered at low HEAT | Accept it within the offer window | Bank is debited, cops disengage, multiplier remains | paid disengagement is not capture | `HEAT-008` |
| Valid race finished and safe-house entry is eligible | Enter the safe house | Night REP and its multiplier settle, HEAT resets, mission reward and progress persist | positive retained terminal | `HEAT-006`, `HEAT-010` |
| Cops box in or wreck the car during pursuit | Resolve Busted | Bank penalty, HEAT reset and forced garage return end the attempt | negative settlement, not successful banking | `HEAT-006` |

## Strategic and experiential structure

- Local decision: trade corner speed against contact, pick a route around
  traffic, and decide whether a repair detour or affordable bribe reduces risk.
- Medium-term planning: preserve condition across the race and return, read
  police coverage and avoid using a scarce repair while little recovery is needed.
- Long-term structure: within this packet only, convert one classified sprint
  into retained reputation and first-night mission completion.
- Common heuristics: distinguish finish from safety; do not provoke an extra
  chase merely to satisfy a walkthrough; separate pursuit clearance from the
  still-retained night multiplier; check condition before passing a service.
- Failure attribution: gate progress, place, health, police state and settlement
  feedback distinguish driving error, detection, exhausted repairs and capture.
- Player-trust factors: the event and difficulty are fixed; the return has an
  observable settlement; the official mission-reward fix is included rather
  than treating a launch bug as intended design. Claims: `HEAT-004`–`HEAT-010`.

## Replay and variation

- What changes: driving line, traffic/rival interaction, place, police contacts,
  repair/payment choices and retained amounts. Product, starter, event,
  difficulty and first-night terminal do not change.
- Randomness: authored course and rules coexist with varying agents; this
  record makes no deterministic traffic-seed or fixed chase-duration claim.
- Viable strategies: clean detection avoidance, evasive routing, a repair
  detour or an affordable low-HEAT payment can preserve the same return goal.
- Replay motive: better race place and more reliable banking without expanding
  the packet into another event. Claims: `HEAT-004`–`HEAT-010`.

## Adjacent systems and history

- Unbound provides a meaningful race-to-garage corridor, but its analysed
  prologue forces a pursuit and exposes cash rather than Heat's multiplied REP.
- Underground's first-place reward and Asphalt's disclosed top-three goal are
  distinct from this mission's finish-then-return predicate.
- Payback's delivery, The Run's three-event rank and Most Wanted's opening
  race do not establish Heat's session economy by franchise resemblance.
- Launch bugs, later missions and online balance are not merged into the
  observed Windows packet. Claims: `HEAT-001`–`HEAT-010` and prior records.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-292`, `ACT-293`, `ACT-341`, `ACT-418` | car, profile, event, refuge, offer |
| System Behaviour | `SYS-299`, `SYS-320`, `SYS-365`, `SYS-366`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-767`, `SYS-768`, `SYS-769` | REP, HEAT, modifier, penalty, service |
| Constraint | `CON-438`, `CON-523`, `CON-588` | route order, pursuit, repair allowance |
| Information | `INF-144`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `INF-294` | visible driving and exposure state |
| Objective | `OBJ-152` | one classified sprint and retained night |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `243` (`GAME-0001`–`GAME-0243`).
- Exact genome matches: none.
- Tied near matches: `GAME-0199` — Need for Speed Unbound (`17 / 33 = 0.515152`).
- Supported combination subsets: `COMB-0242`.
- Scan date: 2026-09-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0199` — Need for Speed Unbound | `ACT-290`, `ACT-292`, `ACT-293`, `SYS-320`, `SYS-365`, `SYS-366`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-438`, `CON-523`, `INF-144`, `INF-204`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Unbound forces a pursuit and Burst-driven exposed-cash return; Heat allows detection avoidance, retains session REP/HEAT and admits quota-limited repair or bribe before banking | Near, `0.515152` |

### Preserved research notes

- New genes: `ACT-418`, `SYS-767`, `SYS-768`, `SYS-769`, `CON-588`,
  `INF-294`, `OBJ-152`.
- Classification result: `New gene`.
- Evidence and reasoning: new boundaries concern transferable session
  settlement, repair allowance and paid disengagement, not a named quest.
- Lower-ID scan: reuse `SYS-366` for the active pursuit/search layer only;
  retain night HEAT separately in `SYS-767`. Reject `CON-328`, whose wanted
  level itself clears after search, `CON-437`, whose class restriction is hard,
  `SYS-642`, whose exposed cash crosses mandatory pursuit, and `OBJ-122`,
  whose chase is mandatory. Reject `OBJ-134`/`OBJ-150` as place-threshold goals,
  and `ACT-357`/`SYS-641`/`INF-255` as Unbound Burst mechanics. `SYS-753` uses
  a finite fixture reservoir, unlike a global session allowance. `SYS-476`
  preserves a jurisdictional bounty, not an extraction multiplier. No prior
  signature or definition is broadened to force these reuses.

## Taxonomy impact

- Registry changes: seven new transferable boundaries and `COMB-0242`.
- Taxonomy-change record: none; no prior label, definition or signature changes.
- Candidate terms affected: no mission/car/reward parameter promoted to a label.

## Negative results

- None requiring a separate claim rejection record; the local reuse exclusions
  above are admission decisions, not invalidation of earlier research.

## Delta summary

## New facts

- [Confirmed | Direct | High] Capture and garage settlement have distinct
  financial and reputation effects; first-night banking includes the official
  mission-reward correction. `HEAT-006`, `HEAT-010`.

## New genes

- [Observation | Corroborated | High] Seven boundaries above distinguish
  session exposure, shared repair allowance, paid disengagement and voluntary
  banking without a forced chase.

## New combinations

- [Observation | Corroborated | High] `COMB-0242` joins direct racing,
  conditional pursuit, notoriety-weighted REP and finite repairs before return.

## Taxonomy changes

- [Confirmed | Direct | High] No taxonomy changes to earlier records.

## New questions

- How does installed nitrous change the race/return trade-off in a separate
  fixed-loadout packet without importing Unbound's Burst rules?
- Does a measured later high-HEAT trace add a distinct extraction boundary,
  or only new parameters to the same session structure?

## Next recommended game

- [Hypothesis | Limited | Medium] DOOM (2016), `GAME-0245`.
- Optimisation criterion: follow approved selection 013 with a bounded early
  combat/resource route rather than another NFS.
- Expected information gain: compare aggressive resource recovery with existing
  real-time combat and ordered-route signatures.
- Backlog impact: eight approved games remain before the independent audit.

## Why this game

- [Hypothesis | Limited | Medium] Primary-supported current availability and
  a reproducible first-night terminal separate Heat's risk economy from its
  already reviewed franchise neighbours.
