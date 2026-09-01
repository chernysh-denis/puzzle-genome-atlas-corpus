---
game_id: GAME-0214
slug: mafia-2002
game_title: "Mafia (2002)"
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0212
gene_ids:
  action:
    - ACT-008
    - ACT-201
    - ACT-384
  system:
    - SYS-215
    - SYS-320
    - SYS-365
    - SYS-366
    - SYS-369
    - SYS-708
    - SYS-709
  constraint:
    - CON-282
    - CON-288
    - CON-328
    - CON-330
    - CON-429
    - CON-557
  information:
    - INF-119
    - INF-125
    - INF-204
    - INF-273
  objective:
    - OBJ-132
  time:
    - TIM-003
---

# Game: Mafia (2002)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `40990`, public Build ID `2300614`, built and published 2017-11-20, checked
  2026-09-01; one fresh Story profile with default controls and no cheats or
  mods. The official storefront title is `Mafia`; the canonical `(2002)`
  qualifier distinguishes this product from `Mafia: Definitive Edition`.
- Platform and mode: Windows single-player Story, Chapter 2 `The Running Man`.
  The current rerelease has the storefront-declared edited soundtrack, but no
  sound or music enters the rules analysis.
- Entry: first retained player control at the taxi rank at the start of `The
  Running Man`, with Tommy driving the assigned taxi and the first fare ready.
- Primary decision loop: stop for each assigned passenger; read the destination,
  compass, city map, radar, speedometer and police state; choose a road route;
  steer, accelerate, brake, use the handbrake or toggle the speed limiter while
  preserving the passenger and taxi and deciding whether to obey, settle or
  evade visible traffic enforcement. Complete five authored fares. After the
  coffee transition and Morello attack, run evasively through the indicated
  alleys and stairs into Salieri's Bar without Tommy's health reaching zero.
- Positive terminal: Tommy enters Salieri's Bar after the fifth fare and the
  authored escape; the safety/family transition completes and Story advances
  beyond `The Running Man`. A single delivered passenger, an unpaid citation
  or merely reaching the final street is not positive completion.
- Negative terminal: Tommy's health reaches zero, police arrest him, the
  mission-critical passenger/taxi state becomes invalid or he fails the fixed
  escape. Retry restores an authored Story save/checkpoint rather than
  retaining the failed traffic, damage or pursuit state.
- Included: the five fixed taxi pickups and destinations; direct 1930s road-
  vehicle control; ambient traffic and pedestrians; collision and vehicle
  state; speed limiter; signals, speeding and observed road offences; the
  ticket, handcuffs, pursuit/search and arrest states; compass, map, radar,
  objective and health information; the unarmed real-time alley escape; Story
  autosave/retry and the completed chapter transition.
- Excluded: Chapter 1 before the declared entry, Chapter 3 and every later
  campaign mission; player gunplay, weapon inventory, vehicle theft, garage,
  fuel purchase and optional exploration; Free Ride, taxi earnings in Free
  Ride, Free Ride Extreme, Carcyclopedia, race content, Tutorial, mods, cheats,
  achievements, speedruns, console versions, the original licensed soundtrack,
  the wider Mafia series and `Mafia: Definitive Edition`.
- Reproducible parameterisation: use Steam app `40990`, a new Story profile and
  default keyboard/mouse controls. At the Chapter 2 entry, complete all five
  passenger stages, deliberately verify one legal speed-limiter state and one
  observable traffic-law cue without accepting arrest, then survive the fixed
  alley route and enter Salieri's Bar. Accept only the completed transition
  beyond `The Running Man` as the terminal.
- Potential scoped modules: Chapter 1's pursued taxi drive; Chapter 3's first
  armed family job; one later Story mission; the race; one bounded Free Ride
  taxi loop; or Definitive Edition each requires a separate version, entry and
  terminal.
- Direct-play status: not conducted. The official Steam page and Steam-hosted
  text manual establish the product, modes, controls, HUD, road law, saves and
  failure rules; two independent text walkthroughs establish the five-fare and
  fixed escape sequence. The transition trace is evidence-based rules
  reconstruction. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MAF-001` | Steam app `40990` is the original 2002 `Mafia`, not Definitive Edition, and the current rerelease declares an edited soundtrack | Confirmed | Direct | High | P1 |
| `MAF-002` | Public Windows Build `2300614` is the current Steam branch boundary | Confirmed | Corroborated | High | P1, S1 |
| `MAF-003` | Story, Free Ride and Free Ride Extreme are distinct modes; this unit admits only Story Chapter 2 | Confirmed | Direct | High | P2 |
| `MAF-004` | Tommy is directly controlled on foot and in cars through movement, steering, throttle, brake, handbrake and a toggleable speed limiter | Confirmed | Direct | High | P2 |
| `MAF-005` | The HUD exposes health, speed, gear, radar, objective bearing, city map and current task without automatically choosing the road route | Confirmed | Direct | High | P2 |
| `MAF-006` | Observed minor road offences produce a payable ticket; serious, repeated or evaded offences escalate to arrest, pursuit and GAME OVER | Confirmed | Direct | High | P2 |
| `MAF-007` | `The Running Man` requires five successful taxi fares before the authored coffee attack | Observation | Corroborated | High | S2, S3 |
| `MAF-008` | Each fare binds an assigned passenger to a named destination and credits the next stage only after successful arrival | Observation | Corroborated | Medium | S2, S3 |
| `MAF-009` | After the fifth fare, Tommy must evade live incoming fire through a fixed alley/stair route and enter Salieri's Bar | Observation | Corroborated | High | P2, S2, S3 |
| `MAF-010` | Health zero or arrest ends the attempt; Story autosaves at important tasks and retry does not retain failed transient state | Confirmed | Corroborated | High | P2, S3 |
| `MAF-011` | Entering Salieri's Bar after the escape is the bounded positive terminal that advances Story beyond `The Running Man` | Observation | Corroborated | High | S2, S3, V1 |
| `MAF-012` | The repository trace reproduces entry, five fare settlements, road-law branches, escape, failure and retained Story completion | Observation | Direct | High | V1 |

## Basic data

- Release / origin: developed by Illusion Softworks and published by
  Gathering of Developers / Take-Two; original release 2002-08-28. The current
  Steam listing is published by 2K.
- Platform or physical form: third-person single-player action driving and
  on-foot traversal on Windows; only the declared Steam Story packet is scoped.
- Puzzle family: spatial logic and topology; real-time system pressure; ordered
  dependency sequencing; tactical forecast and counterplay.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/40990/Mafia/),
    for title, developer/publisher, release, single-player Windows product,
    authored missions, vehicles with real-time damage and the edited-soundtrack
    rerelease notice.
  - **[P2]** [official Steam-hosted PC manual](https://cdn.akamai.steamstatic.com/steam/apps/40990/manuals/Mafia_-_Manual.pdf?t=1661895807),
    for Story/Free Ride separation, default on-foot and vehicle controls, speed
    limiter, radar/compass/map/objectives, health, traffic offences, ticket,
    arrest, wanted search, autosave and Story mission settlement.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/40990/depots/),
    for public Build `2300614` and its 2017-11-20 branch timestamp.
  - **[S2]** [Walkthrough King text walkthrough](https://www.walkthroughking.com/text/mafia.aspx),
    for the five-fare trigger, attack, fixed alley route and safe-bar terminal.
  - **[S3]** [GameFAQs contemporary PC text walkthrough](https://gamefaqs.gamespot.com/pc/371671-mafia/faqs/19141),
    for the Chapter 2 taxi/speed-limiter boundary, police failure and detailed
    escape route.
- Reproducible control:
  - **[V1]** repository-side transition trace derived from `P1`–`P2` and
    `S1`–`S3`; it is rules reasoning, not a direct-play claim.
- Claim IDs: `MAF-001`–`MAF-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run Tommy through the final alley and stair
  geometry; `ACT-201`: directly steer, accelerate, brake, handbrake and operate
  the embodied taxi.
- New `ACT-384`: toggle the vehicle speed limiter, accepting a bounded maximum
  road speed to reduce violation risk while retaining steering and braking.
- Parameters: control binding, vehicle, seat, route, steering, throttle, brake,
  handbrake, transmission, limiter state, on-foot direction and camera.
- Claim IDs: `MAF-004`, `MAF-006`–`MAF-009`, `MAF-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve live enemy fire, Tommy movement, damage and
  defeat during the escape; `SYS-320`: integrate taxi motion, collision and
  damage; `SYS-365`: route ambient traffic and pedestrians; `SYS-366`:
  escalate eligible observed offences into police pursuit/search and clear it
  only after successful evasion; `SYS-369`: restore the authored Story
  save/checkpoint after failure.
- New `SYS-708`: board the current authored passenger, assign the named
  destination, settle successful arrival and expose the next fixed fare until
  the five-fare count is complete.
- New `SYS-709`: classify an observed road offence into a stoppable citation
  or arrest tier; stopping and exiting permits fine settlement, while serious,
  repeated or evaded offences escalate to arrest pressure and GAME OVER.
- Resolution order: admit the current passenger; reveal destination; integrate
  vehicle input, traffic and collision; evaluate observed road legality and
  police response; settle a legal destination arrival; advance the fare count;
  after five settlements switch to on-foot attack; resolve movement, hostile
  fire and health; entering Salieri's Bar settles Story completion.
- Claim IDs: `MAF-004`–`MAF-012`.

### Constraint Genes

- Existing `CON-282`: the five fares and escape obey authored order;
  `CON-288`: taxi operation requires a viable driver seat, vehicle and road
  geometry; `CON-328`: an active wanted search clears only after Tommy remains
  unseen; `CON-330`: passenger, taxi, Tommy and permitted mission area must
  remain viable; `CON-429`: direction, signals and speed bound lawful driving.
- New `CON-557`: one fare credits only when its assigned passenger reaches the
  named destination in the still-valid taxi; an earlier or unrelated location
  cannot advance the chain.
- Scarce strategic resources: taxi condition, passenger viability, Tommy's
  health, legal speed margin, police sight/search time, route clearance and
  distance to the current destination or safe bar.
- Claim IDs: `MAF-005`–`MAF-012`.

### Information Genes

- Existing `INF-119`: Tommy's health is visible; `INF-125`: city map, current
  task and authored mission gates are inspectable; `INF-204`: speed, gear,
  compass/map cues and local driving state guide route and braking choices.
- New `INF-273`: radar colours, ticket/handcuff icon, wanted bar and current
  mission cues expose nearby traffic/police, offence severity and whether
  pursuit is active without revealing future patrol paths.
- Claim IDs: `MAF-005`, `MAF-006`, `MAF-009`–`MAF-012`.

### Objective Genes

- New `OBJ-132`: complete all five authored taxi fares, survive the resulting
  unarmed escape and enter Salieri's Bar so Story retains completion of `The
  Running Man`.
- A delivered fare, cleared ticket, hidden pursuit or arrival on the final
  street is intermediate. Death, arrest or checkpoint retry is not success.
- Claim IDs: `MAF-007`–`MAF-012`.

### Time Genes

- Existing `TIM-003`: taxi motion, traffic, police observation/search, hostile
  fire, health loss and escape distance advance continuously while player
  input remains live outside menus and authored transitions.
- Claim IDs: `MAF-004`–`MAF-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New Story has reached Chapter 2 | Accept first retained taxi control | First passenger stage and destination become active | exact bounded entry | `MAF-003`, `MAF-007` |
| Passenger is aboard and destination is known | Read compass/map and drive | Direct input, traffic, collision and route choice advance continuously | authored destination does not automate travel | `MAF-004`, `MAF-005`, `MAF-008` |
| Taxi is below the regulated cap | Toggle speed limiter | Maximum road speed is bounded while steering and braking remain direct | compliance is an explicit control choice | `MAF-004`, `MAF-006` |
| Police observe a minor road offence | Stop and exit as instructed | Ticket state settles as a fine rather than arrest | citation is recoverable inside the mission | `MAF-006` |
| Ticket is active or a serious offence is observed | Flee or repeat violations | Police escalate to arrest pursuit; successful arrest produces GAME OVER | law pressure has a severity branch | `MAF-006`, `MAF-010` |
| Police pursue but lose sight | Stay unseen through the wanted interval | Wanted state fades and clears if no new offence is observed | evasion is time- and perception-dependent | `MAF-006` |
| Correct destination is reached with valid taxi/passenger | Stop in the admitted arrival area | Passenger exits, fare settles and the next fixed stage is exposed | each fare is an ordered delivery gate | `MAF-007`, `MAF-008` |
| Fifth fare has settled | Allow coffee transition | Morello attack begins and control returns to unarmed Tommy | authored vehicle-to-foot handoff | `MAF-007`, `MAF-009` |
| Attackers have line of fire | Run, zig-zag and follow alley arrows | Real-time movement and incoming damage determine whether the fixed route remains viable | escape is live evasion, not a cutscene | `MAF-009` |
| Salieri's Bar entrance is reached alive | Enter the bar | Safety/family transition completes and Story advances beyond Chapter 2 | explicit positive terminal | `MAF-011`, `MAF-012` |
| Health reaches zero, arrest occurs or critical state fails | Retry | Latest authored Story state returns without failed transient traffic or damage | rollback is not completion | `MAF-010` |

## Strategic and experiential structure

- Planning horizon: compare direct and safer road routes, decide where a lower
  speed reduces enforcement/collision risk, and preserve enough taxi condition
  and health to reach the next authored phase.
- Local tactics: brake for traffic and signals, toggle the limiter before a
  regulated stretch, decide whether to settle a ticket or risk escalation, and
  vary running line under fire rather than taking a straight alley trajectory.
- Long-term structure: five small destination settlements accumulate into one
  irreversible phase change; the final escape converts ordinary employment
  into the next Story state.
- Reversible versus irreversible: road choice, speed and local police search
  can recover; a credited fare advances the fixed chain; arrest/death rolls
  back; completed bar entry persists.
- Failure attribution: speedometer, limiter state, traffic, radar colours,
  ticket/handcuff icon, wanted bar, health and objective text expose whether
  failure came from driving, enforcement, route or hostile fire.
- Player trust: the compass gives bearing rather than a solved road path, so
  the player retains route authority while visible law and damage cues explain
  consequences.

## Replay and variation

- What changes: chosen streets, speed profile, traffic interactions, police
  contact, collision recovery and exact alley movement.
- Randomness or procedural generation: fares, destinations, attack and escape
  geometry are authored; ambient traffic and local pursuit positioning vary.
- Multiple viable strategies: cautious limiter-led driving, faster route
  optimisation and lawful recovery from a ticket can reach the same terminal;
  the final escape permits different evasive lines inside the fixed corridor.
- Typical replay motive: cleaner taxi routing, fewer offences/collisions or a
  damage-free escape; later campaign and Free Ride are separate modules.

## Adjacent systems and history

- Direct successors or variants: `Mafia: Definitive Edition` re-authors the
  product and cannot be used as evidence for app `40990`; later Mafia games,
  console releases and the original licensed soundtrack are excluded.
- Similar games: Grand Theft Auto V shares an authored crime city, direct
  vehicles, traffic, police pursuit and on-foot missions; Red Dead Redemption 2
  adds witnesses, bounty and honour; Euro Truck Simulator 2 shares lawful road
  movement and fines; Need for Speed Payback shares ordered driving set pieces.
- Important differences: Mafia's scoped packet delivers five fixed passengers
  before a compulsory unarmed escape. Its minor offence can remain a payable
  roadside citation, whereas GTA V moves directly through wanted stars and ETS2
  immediately debits a tariff without a stop-or-arrest branch.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-201`, `ACT-384` | on-foot route, embodied taxi control and speed-limiter toggle |
| System Behaviour | `SYS-215`, `SYS-320`, `SYS-365`, `SYS-366`, `SYS-369`, `SYS-708`, `SYS-709` | incoming fire, vehicle/traffic, pursuit, retry, fares and citation escalation |
| Constraint | `CON-282`, `CON-288`, `CON-328`, `CON-330`, `CON-429`, `CON-557` | authored order, vehicle, wanted, mission, road-law and fare gates |
| Information | `INF-119`, `INF-125`, `INF-204`, `INF-273` | health, map/objective, driving and offence/police state |
| Objective | `OBJ-132` | settle five fares, escape and enter Salieri's Bar |
| Time | `TIM-003` | continuous traffic, pursuit and escape |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `213` (`GAME-0001`–`GAME-0213`).
- Exact genome matches: none.
- Tied near matches: `GAME-0145` — Grand Theft Auto V (`14 / 56 = 0.250000`).
- Supported combination subsets: `COMB-0212`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0145` — Grand Theft Auto V | `ACT-008`, `ACT-201`, `SYS-215`, `SYS-320`, `SYS-365`, `SYS-366`, `SYS-369`, `CON-282`, `CON-288`, `CON-328`, `CON-330`, `INF-119`, `INF-125`, `TIM-003` | Both directly join on-foot action, road vehicles, traffic, police pursuit/search and authored checkpointed missions. GTA V adds three switchable protagonists, firearms, cover, specials, heist planning and a star-based modern wanted system. Mafia instead fixes one driver, five passenger destinations, a toggleable speed cap, traffic-law citation versus arrest and an unarmed alley terminal. | Near, `0.250000` |

### Preserved research notes

- New genes: `ACT-384`, `SYS-708`, `SYS-709`, `CON-557`, `INF-273`,
  `OBJ-132`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: existing direct movement, vehicle, traffic, wanted,
  retry, mission, road-law, map and real-time boundaries absorb the generic
  layer. No lower-ID record represents a toggleable speed cap, ordered player-
  driven passenger fares, roadside citation-to-arrest escalation and the
  five-fare-to-unarmed-escape terminal as these separate causal boundaries.

## Combination status

- `COMB-0212` is a strict subset of the complete genome, coupling direct taxi
  routing, speed control, road-law response, fixed passenger settlement and the
  resulting on-foot escape terminal.
- Every earlier verified combination will be tested deterministically after
  registration; proper-subset results remain validation-controlled.

## Taxonomy impact

- Registry changes: six new Active genes, evidence links on reused genes,
  `COMB-0212` and existing family memberships.
- Taxonomy-change record: none; no earlier reviewed signature, lifecycle or
  stable definition changes.
- Candidate terms affected: speed-limiter toggle, authored taxi fare,
  citation-to-arrest escalation, police-state HUD and fare-to-escape terminal.

## Negative results

- `ACT-290` is not reused: Tommy occupies and can leave an embodied world taxi;
  the car is not a dedicated race-event body.
- `SYS-507` is not reused: Mafia does not immediately debit an abstract traffic
  fine while driving; the police first require a stop and can escalate arrest.
- `INF-144` is not reused: Mafia's compass supplies bearing and its map supplies
  destination context, not a calculated GPS road route.
- Free Ride taxi income, refuelling, garage retention, weapon systems and later
  Story combat do not enter the signature merely because the product has them.

## Delta summary

## Нові факти

- [Confirmed/Observation | Direct/Corroborated | High] The current original
  Steam release supports one reproducible Chapter 2 packet with five taxi
  fares, explicit road-law decisions and a bounded unarmed escape terminal
  (`MAF-001`–`MAF-012`).

## Нові гени

- [Confirmed/Observation | Direct/Corroborated | High] Added `ACT-384`,
  `SYS-708`, `SYS-709`, `CON-557`, `INF-273` and `OBJ-132` for the limiter,
  fare chain, citation branch, delivery gate, police HUD and complete terminal.

## Нові комбінації

- [Observation | Corroborated | High] Added `COMB-0212`, joining lawful direct
  taxi service to an authored real-time escape.

## Зміни таксономії

- Added one bounded 2002 Story packet and its new/reused evidence; no earlier
  signature, lifecycle or stable definition changed.

## Family classification

- `FAM-009` Tactical forecast and counterplay.
- `FAM-010` Real-time system pressure.
- `FAM-014` Spatial logic and topology.
- `FAM-017` Ordered dependency sequencing.

## Plain-language interpretation

This is not simply five drives followed by a cutscene. Every passenger gives a
destination but not a solved road route, so the player reads the city, controls
the taxi and manages traffic law. A minor mistake can still be settled as a
ticket; fleeing or committing a serious offence can turn it into arrest and
mission failure. Only after all five fares does the ruleset deliberately remove
the taxi and ask the same vulnerable protagonist to survive a live alley escape
to Salieri's Bar.

## New questions

- Which other game turns a recoverable roadside citation into terminal arrest
  only after player noncompliance or higher offence severity?
- When does a fixed series of individually driven passenger fares deserve the
  same objective gene without sharing Mafia's later escape phase?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0215` — It Takes Two.

## Чому саме вона

- It is the next recorded Batch 009 unit and contrasts one vulnerable solo
  driver/runner with a bounded mandatory two-player co-operative chapter.
- Backlog impact: advances the active Goal without starting `GAME-0215` here.
