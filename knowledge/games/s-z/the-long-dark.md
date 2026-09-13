---
game_id: GAME-0285
slug: the-long-dark
game_title: "The Long Dark"
analysis_status: reviewed
reviewed: 2026-09-09
combination_ids:
  - COMB-0272
gene_ids:
  action:
    - ACT-008
    - ACT-164
    - ACT-165
    - ACT-199
    - ACT-214
    - ACT-216
    - ACT-311
    - ACT-364
  system:
    - SYS-327
    - SYS-669
    - SYS-840
  constraint:
    - CON-068
    - CON-281
    - CON-313
    - CON-537
  information:
    - INF-067
    - INF-073
    - INF-075
    - INF-128
  objective:
    - OBJ-125
  time:
    - TIM-003
---

# Game: The Long Dark

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `305620`, installed through the standalone `The Long Dark: Survival Mode`
  package `797627`, default public branch build `22915504`, whose projected
  publication time is 2026-04-23 02:40:49 UTC (`TLD-001a`). The latest official
  release announcement before review names Survival `2.55 (181032)` and was
  published 64 minutes later (`TLD-001b`); the temporal match is corroborating
  distribution evidence, not a Valve-authored mapping between the two build
  numbers. Checked 2026-09-09. The bounded packet is one standard `Hopeless
  Rescue` Challenge attempt from its authored start to a declared success or
  failure result (`TLD-002`–`TLD-004`).
- Primary decision loop: read the remaining seven-day allowance together with
  Warmth, Fatigue, Thirst, Hunger and Condition; choose a direct route and
  whether to keep moving, search a nearby container, change carried clothing or
  supplies, eat, drink or surrender time to sleep; remain light and rested
  enough to traverse the fixed rope route to the summit of Timberwolf Mountain;
  take the Distress Pistol and at least one Flare Shell from its challenge-bound
  crash-site source; cross the intervening regions to the Lighthouse in
  Desolation Point; equip, load and fire the pistol from the top before the
  authoritative allowance expires (`TLD-003`–`TLD-009`).
- Entry: selecting `Hopeless Rescue`, accepting its fixed Challenge rules and
  receiving first control inside Trapper's Homestead in Mystery Lake with the
  seven-day allowance running (`TLD-002`, `TLD-003`). Random starting supplies,
  weather and later container contents remain attempt parameters.
- Positive terminal: after the summit pistol has been recovered, firing a
  loaded Distress Pistol from the top of the Lighthouse while the survivor is
  alive and time remains settles the Challenge completion and its badge
  (`TLD-004`, `TLD-009`, `TLD-011`). Reaching either location, carrying the
  pistol elsewhere or firing before the Lighthouse is insufficient.
- Negative terminal: reaching zero Condition or the end of the seven-day
  allowance before the qualifying signal ends the attempt unsuccessfully;
  failure cannot resume the same one-life route and requires a new Challenge
  attempt (`TLD-005`, `TLD-010`). The death branch follows the product's stated
  Survival rule that the current save is deleted. No successful reload is
  claimed or required.
- Included: direct first-person walking, sprinting, fixed-region transitions and
  fixed-rope traversal; searching containers and taking visible supplies;
  carried weight, clothing/equipment slots and active item selection; consuming
  food and water; sleeping; the four Needs and Condition; activity-, load- and
  environment-driven depletion; hidden changing weather as environmental
  pressure; the Challenge objectives and remaining allowance; the fixed summit
  Distress Pistol source; terminal Lighthouse signal; deadline and death
  failure; the completion badge as result evidence.
- Excluded: free-form Survival, WINTERMUTE and its five episodes, Custom Mode,
  every other Challenge and event, `TALES FROM THE FAR TERRITORY`, soundtrack
  packages, mods and Time Capsule builds; hunting, fishing, harvesting carcasses,
  curing, crafting, repairing, sharpening, cooking, boiling water, fire-starting
  and long-horizon item decay; optional combat and wildlife kills; detailed
  affliction treatment; feats, skills and badges other than the terminal
  `Hopeless Rescue` result; base building, trader or story systems; later
  survival history and arbitrary sandbox stopping.
- Potential scoped modules: one free-form Survival life; one WINTERMUTE episode;
  one other named Challenge; an authored fire/cooking trace; a wildlife struggle;
  or a `TALES FROM THE FAR TERRITORY` route each requires its own version,
  entry, terminal and evidence contract.
- Reproducible parameterisation: install Steam app `305620` through package
  `797627` on the public branch; choose `Challenges` and `Hopeless Rescue`; begin
  at Trapper's Homestead; travel to the Timberwolf Mountain summit; recover the
  only challenge-valid Distress Pistol source and preserve a shell; then travel
  to the top of the Desolation Point Lighthouse and fire before the displayed
  allowance reaches zero. Exact paths, shelter stops, searched containers,
  clothing, food, water, sleep schedule, weather and wildlife avoidance remain
  bounded attempt parameters. No glitch, out-of-bounds shortcut, DLC item or
  alternate pistol spawn is admitted.
- Direct-play status: not conducted. Valve application and package data establish
  lawful current Windows availability. The public-branch build comes from the
  secondary SteamCMD projection, while Hinterland's announcement independently
  establishes the current Survival version label. The current Steam product
  page still lists `Hopeless Rescue`; Hinterland's original release notes define
  its route and deadline, and official 2019 and 2023 patches independently show
  that the named Challenge and its crash-site Distress Pistol rule persisted
  after launch. Current official support defines the four Needs, Condition and
  death boundary. Current community references corroborate the exact objective
  list, Challenge failure, fixed-rope, load and firing transitions. No video or
  audio was opened, played, heard or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TLD-001a` | Steam package `797627` lawfully supplies Windows app `305620`; the current public branch is projected as build `22915504`, updated 2026-04-23 02:40:49 UTC | Confirmed | Corroborated | High | P1, P2, S1 |
| `TLD-001b` | Hinterland's latest pre-review release announcement names Survival `2.55 (181032)` | Confirmed | Direct | High | P3 |
| `TLD-002` | The current product lists `Hopeless Rescue` among standalone objective-based Challenge Modes | Confirmed | Direct | High | P1 |
| `TLD-003` | The Challenge starts at Trapper's cabin and requires the summit-to-Lighthouse route within seven in-game days | Confirmed | Corroborated | High | P4, S2 |
| `TLD-004` | The ordered objectives are to recover the Distress Pistol at the Timberwolf Mountain summit, reach the Desolation Point Lighthouse, equip the pistol and fire it | Observation | Corroborated | High | P4, P5, S2 |
| `TLD-005` | Warmth, Fatigue, Thirst and Hunger drain or refill, feed Condition loss and recovery, and zero Condition ends the survivor | Confirmed | Direct | High | P1, P6 |
| `TLD-006` | Activity and carried load drain Fatigue; low Fatigue reduces movement and capacity; fixed-rope climbing spends Fatigue and Stamina and can slip or fail | Observation | Corroborated | High | P4, S3–S5 |
| `TLD-007` | Search and inventory interfaces expose supplies, equipment compatibility, active item and carried weight before the player takes, equips or leaves them | Observation | Corroborated | High | P1, P5, S2, S4 |
| `TLD-008` | Sleep spends authoritative world time to restore Fatigue while the same Needs and environmental exposure remain consequential | Observation | Corroborated | High | P4, P6, S3 |
| `TLD-009` | A loaded Distress Pistol fired from the Lighthouse after summit recovery is the explicit positive-settlement command | Confirmed | Corroborated | High | P4, P5, S2, S6 |
| `TLD-010` | Timer expiry or death fails the Challenge; Survival death deletes the current resumable save rather than restoring the same life | Confirmed | Corroborated | High | P1, P6, S2, S7 |
| `TLD-011` | Successful completion records the `Hopeless Rescue` Challenge badge | Observation | Limited | Medium | S2 |

## Basic data

- Release / origin: developed and published by Hinterland Studio Inc.; Steam
  release 2017; reviewed on Windows at the current public build projected on
  2026-04-23 and official Survival `2.55 (181032)`.
- Platform or physical form: first-person single-player Windows survival
  Challenge through Steam.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/305620/The_Long_Dark/),
    for developer, publisher, Windows support, standalone Survival product,
    four Needs, live resource/time pressure, Survival save deletion and the
    current list of Challenge Modes including `Hopeless Rescue`.
  - **[P2]** [Valve app/package metadata](https://store.steampowered.com/api/appdetails?appids=305620&cc=ua&l=english),
    plus [package `797627`](https://store.steampowered.com/api/packagedetails?packageids=797627&cc=ua&l=english),
    for application, package and delivery identities.
  - **[P3]** [official 2026 hotfix announcement](https://store.steampowered.com/news/app/305620/view/1830797770232149),
    for Survival `2.55 (181032)` and its publication time.
  - **[P4]** [Hinterland, `Tireless Menace` original release
    note](https://www.thelongdark.com/time-capsule/tireless-menace/), for the
    Challenge's authored start, summit, Lighthouse, signal and seven-day
    deadline plus the Rest/Fatigue relation. The page labels this archived build
    unsupported; it is used only where P1, P5 and current S2 show the same named
    rule remains present.
  - **[P5]** [Hinterland, version 2.23 Quality of Life
    update](https://store.steampowered.com/news/app/305620/view/5219165352642547673),
    for the later `Hopeless Rescue` fix that removes unintended Distress Pistol
    locations, container search and current Challenge applicability in 2023.
  - **[P6]** [Hinterland Support, Condition and Character
    Status](https://hinterlandgames.zendesk.com/hc/en-us/articles/360042349471-Condition-and-Character-Status),
    for Warmth, Fatigue, Thirst, Hunger, Condition loss/recovery and zero-
    Condition death.
- Reproducible mechanics sources:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/305620),
    observed 2026-09-09, for build `22915504` and Unix update timestamp
    `1776912049`.
  - **[S2]** [current community `Hopeless Rescue`
    reference](https://thelongdark.fandom.com/wiki/Hopeless_Rescue), for the
    start, ordered objective list, seven-day failure, displayed time, route and
    completion badge.
  - **[S3]** [current community Fatigue
    reference](https://thelongdark.fandom.com/wiki/Fatigue), for activity/load
    depletion, sleep recovery, exhaustion and rope-climb interaction.
  - **[S4]** [current community Encumbrance
    reference](https://thelongdark.fandom.com/wiki/Encumbrance), for carried
    weight, Fatigue-linked capacity, movement penalties and rope legality.
  - **[S5]** [current community Rope Climbing
    reference](https://thelongdark.fandom.com/wiki/Rope_Climbing), for fixed
    rope entry, ledges, Stamina/Fatigue loss and slip risk.
  - **[S6]** [current community Distress Pistol
    reference](https://thelongdark.fandom.com/wiki/Distress_Pistol), for the
    equip, load and fire input plus the Challenge-only crash-site source.
  - **[S7]** [current community Challenge
    reference](https://thelongdark.fandom.com/wiki/Challenge), for death and
    objective-failure closure in Survival Challenges.
- Applicability audit: P1 names the Challenge in the current product; P5 is a
  post-split-era official fix to its Distress Pistol placement; P3 defines the
  current version but makes no further `Hopeless Rescue` change; S2–S7 were
  current at review and agree with the surviving official clauses. Archived P4
  is never sole support for a current transition.
- Claim IDs: `TLD-001a`–`TLD-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the controlled survivor by walking,
  sprinting, region transitions and fixed-rope traversal; `ACT-164`, select a
  carried active item; `ACT-165`, consume carried food; `ACT-199`, take, equip,
  replace or load compatible carried supplies; `ACT-214`, commit to sleep;
  `ACT-216`, search one reachable container or wreck; `ACT-311`, consume carried
  water; generalised `ACT-364`, activate the carried Distress Pistol signal in
  its eligible terminal region.
- Parameters: route, speed, region exit, fixed rope, item, clothing slot,
  carried weight, food, water, sleep duration, searched container, pistol,
  Flare Shell, loading state and Lighthouse activation region.
- Rejected `ACT-089`: generic visible supply and Distress Pistol pickup are
  already the lower-ID `ACT-199`, while concealed contents require the separate
  `ACT-216` search first. Rejected `ACT-161`: the terminal shot is admitted as a
  signal command, not combat. Rejected `ACT-362` and `ACT-363`: the route uses
  authored fixed ropes, not freely targeted surface grip or player-deployed
  climbing aids.
- Claim IDs: `TLD-003`, `TLD-004`, `TLD-007`–`TLD-009`.

### System Behaviour Genes

- Existing genes: generalised `SYS-327`, continuously update Condition,
  calories, hydration, Warmth and Fatigue from activity, rest, equipment and
  environment; generalised `SYS-669`, convert the eligible Lighthouse signal
  into Challenge completion and the result surface.
- New gene: `SYS-840`, delete the failed one-life attempt's resumable state at
  death while retaining only profile-level records allowed outside that attempt.
- Resolution order: update the authoritative allowance and survival state;
  accept movement, search, inventory, consumption or sleep; resolve load,
  Fatigue and environmental costs; expose objective and survival feedback;
  after summit recovery, test the Lighthouse signal predicates; settle success,
  let deadline expiry settle failure, or delete the resumable attempt state at
  lethal Condition.
- Rejected `SYS-345`: it explicitly excludes deleting the attempt save and
  permits a retained world with another character. Rejected `SYS-513`: its
  radiation, bleeding and quick-use compound is not this route. Rejected
  `SYS-661` and `SYS-663`: they resolve PEAK's freely targeted surface grip and
  affliction-obstructed climb bar, not fixed-rope travel under The Long Dark's
  separate Fatigue and Stamina states. Rejected `SYS-782`: it requires a
  persistent hub and metaprogression resources and excludes complete attempt-
  save deletion.
- Claim IDs: `TLD-005`, `TLD-006`, `TLD-009`, `TLD-010`.

### Constraint Genes

- Existing genes: generalised `CON-068`, the seven-day authoritative allowance
  expires into failure; generalised `CON-281`, the route remains viable only
  while climate protection, calories, hydration, Fatigue, Stamina, carried load
  and Condition stay recoverable; `CON-313`, death cannot resume the same
  survivor life; generalised `CON-537`, completion requires a living survivor,
  the required route progress, the Lighthouse region and a usable loaded signal
  item at the same time.
- Scarce strategic resources: remaining in-game hours; daylight and shelter;
  Warmth, Fatigue, Thirst, Hunger, Condition and Stamina; carried-weight margin;
  food, water, clothing and sleep time; the one required Distress Pistol and at
  least one preserved Flare Shell.
- Rejected `CON-210` and `CON-284`: ordinary TLD pickup is governed by carried
  weight and mobility, not Minecraft-style typed stack/slot rejection or
  PUBG-style backpack bulk plus weapon slots. Rejected `CON-312`: the sources
  prove exposure during elapsed sleep, but not its interruption semantics.
  Rejected `CON-435`: it bundles bleeding and radiation and permits prior-save
  restoration. Rejected `CON-534`–`CON-536`: they govern PEAK's free grip and
  deployed aids, not this authored fixed-rope route.
- Claim IDs: `TLD-003`, `TLD-005`, `TLD-006`, `TLD-009`, `TLD-010`.

### Information Genes

- Existing genes: `INF-067`, expose ordered Challenge requirements, remaining
  allowance, completion reward and failure consequence; `INF-073`, expose
  carried and active equipment state; `INF-075`, expose the four Needs,
  Condition, Stamina and relevant equipment state; `INF-128`, expose reachable
  loot identity, equipment compatibility, current load and replacement choice.
- Rejected `INF-091`: future weather is not forecast and is intentionally
  uncertain. Rejected `INF-202` and `INF-240`: their radiation/quick-use and
  sanity/partner-state compounds exceed the solo Challenge packet. Rejected
  `INF-259`: the lower-ID `INF-067` owns the objective/deadline/result surface;
  no PEAK biome/campfire report exists here.
- Claim IDs: `TLD-003`–`TLD-011`.

### Objective Genes

- Existing generalised `OBJ-125`: complete one bounded survival route through a
  location-bound signal. Here the required progress is summit recovery followed
  by a live, in-time Lighthouse firing; the exact regions, item and deadline are
  parameters.
- Rejected `OBJ-026`: reaching the summit or Lighthouse alone cannot settle the
  Challenge. No new quest-named Objective is introduced.
- Success, evaluation and failure: the loaded Lighthouse signal while alive and
  before expiry settles completion and its badge; death or allowance expiry
  settles failure; any non-terminal route state remains incomplete.
- Claim IDs: `TLD-003`, `TLD-004`, `TLD-009`–`TLD-011`.

### Time Genes

- Existing `TIM-003`: world time, deadline, Needs, weather, movement and
  wildlife continue while ordinary route input is accepted; sleep changes the
  rate and relinquishes control without creating a different clock.
- Rejected a new time gene: the seven-day quantity and sleep acceleration are
  parameters of the already separated real-time progression and deadline
  boundaries.
- Claim IDs: `TLD-003`, `TLD-005`, `TLD-008`, `TLD-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| `Hopeless Rescue` is selected | Accept the Challenge and take first control | The attempt begins at Trapper's Homestead with the authored objectives and seven-day allowance active | fixed entry and rules packet | `TLD-002`, `TLD-003` |
| The survivor is outside with Needs above zero | Walk or sprint toward the next shelter or region exit | Authoritative time advances; activity, load and environment change Fatigue, Warmth, calories, hydration and Condition | route movement is survival expenditure | `TLD-005`, `TLD-006` |
| A reachable closed container lies on the route | Search it, inspect revealed supplies, take or leave one item | Search reveals a bounded sample; carried weight and equipment compatibility change the value of accepting it | scavenging trades time and mobility for resilience | `TLD-007` |
| Hunger or Thirst is low and compatible stock is carried | Select and consume food or water | The chosen item is spent and its declared Need rises; time and other Needs still advance | separate consumables repair separate meters | `TLD-005`, `TLD-007` |
| Fatigue is low at an eligible rest location | Choose a sleep duration | Direct control is surrendered; world time and exposure advance while Fatigue recovers according to the sleep interval | rest is recovery bought with deadline time | `TLD-006`, `TLD-008` |
| The fixed summit rope is reachable while load and Fatigue permit ascent | Traverse the rope, using a ledge if needed | Stamina and Fatigue drain; insufficient state slows or prevents the climb and can cause a slip | the mountain route has an embodied capacity gate | `TLD-006` |
| The summit crash-site source is reached | Search or inspect it and take the Distress Pistol plus a Flare Shell | The Challenge-valid signal item enters carried state; unintended pistol locations are not part of the packet | first ordered objective and unique route resource | `TLD-004`, `TLD-007` |
| The living survivor is atop the Lighthouse with time remaining and a loaded pistol | Equip, aim and fire upward | The signal predicate passes; the Challenge completion and badge settle | positive terminal requires route, place, life, time and item | `TLD-009`, `TLD-011` |
| Condition reaches zero or the allowance expires first | Permit terminal resolution | The current attempt fails; death additionally deletes its resumable one-life save, while either branch requires a new Challenge attempt | explicit negative terminal | `TLD-005`, `TLD-010` |

## Strategic and experiential structure

- Local decision: keep moving or spend time on a container, clothing change,
  food, water or sleep before the next exposed segment or rope.
- Medium-term planning: reach the summit early enough that the return across
  several regions remains possible, while avoiding so much carried weight that
  the required climb and long traversal become slower than the supplies save.
- Long-term structure: convert a survival substrate into two ordered authored
  dependencies — acquire the only valid signal source, then deliver its usable
  state to a fixed terminal region before a shared clock expires.
- Common heuristics: carry only what supports the next leg, recover Fatigue
  before fixed ropes, warm indoors rather than opening optional systems, keep at
  least one shell unused and treat every sleep interval as deadline spending.
- Failure attribution: the objective list and allowance distinguish route
  progress from expiry; Needs, Condition, load and active-item surfaces expose
  resource failure; weather and container contents remain bounded uncertainty.
- Player-trust factors: the Challenge must not imply a safe forecast or a
  guaranteed optional supply. The fixed start, unique pistol source, objective
  order, terminal region and failure rules must remain stable and legible.
- Claim IDs: `TLD-003`–`TLD-010`.

## Replay and variation

- What changes: weather, container contents, chosen route, rest stops, carried
  load, wildlife encounters and time remaining at each objective.
- What stays authored: Challenge name, start, seven-day allowance, summit
  recovery, Lighthouse signal and success/failure predicates.
- Multiple viable strategies: direct low-load travel, more scavenging for safer
  needs, longer recovery before the climb or deliberately accepting limited
  Condition loss to preserve time.
- Typical replay motive: learn inter-region topology and reduce time spent on
  supplies until the two-stage signal route closes reliably.
- Claim IDs: `TLD-003`, `TLD-006`–`TLD-011`.

## Adjacent systems and history

- Direct predecessors: open-world survival and timed rescue-challenge lineages;
  this record does not assign unreviewed historical influence.
- Variants: free-form Survival removes the authored positive terminal; Custom
  changes difficulty; WINTERMUTE adds narrative missions; other Challenges
  replace the objective and deadline contract.
- Similar games: 7 Days to Die shares needs, inventory and real-time exposure;
  Subnautica shares food, water and environment-bound survival; Project Zomboid
  shares Fatigue, sleep and one-life risk; PEAK shares the location-bound carried
  signal terminal.
- Important differences: this packet is neither an indefinite life nor a
  generated climb. It fixes a seven-day cross-region retrieval-and-delivery
  route and makes one explicit fired signal the success command.
- Claim IDs: `TLD-002`–`TLD-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-164`, `ACT-165`, `ACT-199`, `ACT-214`, `ACT-216`, `ACT-311`, `ACT-364` | exact route, supplies, sleep interval, pistol and shell are parameters |
| System Behaviour | `SYS-327`, `SYS-669`, `SYS-840` | depletion rates, weather, result animation and retained profile fields are parameters |
| Constraint | `CON-068`, `CON-281`, `CON-313`, `CON-537` | seven days, load thresholds, region and signal item are parameters |
| Information | `INF-067`, `INF-073`, `INF-075`, `INF-128` | layout, units and presentation are parameters |
| Objective | `OBJ-125` | start, intermediate summit and terminal Lighthouse are parameters |
| Time | `TIM-003` | real-time rate, pause and sleep acceleration are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `284` (`GAME-0001`–`GAME-0284`).
- Exact genome matches: none.
- Tied near matches: `GAME-0203` — PEAK (`12 / 44 = 0.272727`).
- Supported combination subsets: `COMB-0272`.
- Scan date: 2026-09-09.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0203` — PEAK | `ACT-008`, `ACT-164`, `ACT-165`, `ACT-199`, `ACT-364`, `SYS-669`, `CON-537`, `INF-073`, `INF-075`, `INF-128`, `OBJ-125`, `TIM-003` | Both traverse a bounded real-time survival route, manage carried supplies, preserve a portable signal and explicitly activate it alive in a location-bound terminal. PEAK builds its route around free-surface grip, climb stamina, injury afflictions, cooking, deployable climbing aids and a generated dated island whose signal calls a helicopter. The Long Dark instead uses authored region crossings and fixed ropes under continuously coupled Warmth, Fatigue, Thirst, Hunger, load and Condition, spends a seven-day deadline on travel and sleep, requires a summit retrieval followed by a separate Lighthouse delivery, and deletes the resumable attempt save at death. | Near, `0.272727` |

### Preserved research notes

- New genes: `SYS-840` only.
- Reused genes: twenty lower-ID movement, item, sleep, survival, deadline,
  one-life, signal, information, objective and time boundaries.
- Generalised genes: `ACT-364`, `SYS-327`, `SYS-669`, `CON-068`, `CON-281`,
  `CON-537` and `OBJ-125`; no earlier reviewed signature changes.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: one current product, one Challenge, one ordered route
  and explicit terminals are separated from the excluded survival sandbox.

## Taxonomy impact

- Registry changes: one new Active System Behaviour, seven bounded
  generalisations, `COMB-0272`, supporting-carrier annotations and reviewed
  Ukrainian equivalents.
- Taxonomy-change records:
  [`TAXONOMY_CHANGE_051`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_051.md)
  generalises the signal-owned terminal cluster;
  [`TAXONOMY_CHANGE_052`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_052.md)
  generalises deadline time from wall clock to authoritative attempt time; and
  [`TAXONOMY_CHANGE_053`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_053.md)
  generalises the survival-state pair to hydration, Fatigue and carried load.
- Candidate terms affected: authoritative attempt deadline, location-bound
  signal settlement, one-life attempt erasure, survival Fatigue and fixed-rope
  load gate.

## Combination scan

- All `271` combinations present before this unit were tested as strict proper
  subsets of the scoped signature. None qualified.
- New `COMB-0272` is the strict four-gene signal-settlement subset shared with
  `GAME-0203` PEAK; every survival, climb, inventory and deadline difference
  remains outside it.
- No genre-similarity subset was admitted.

## Negative results

- The historical `Tireless Menace` page is not treated as a current build. Its
  route clauses are admitted only where current product and later official or
  current community evidence still expose the same named mechanics.
- Current public build `22915504` and official Survival `2.55 (181032)` are
  reported as separate distribution facts; their nearby timestamps do not prove
  an exact internal-build mapping.
- No fire, hunting, crafting, repair, detailed injury treatment, weather
  forecast or long-horizon decay gene is included merely because it exists in
  the product.
- Optional wildlife combat is not required by the route and contributes no
  Action or combat System gene.
- Fixed-rope travel is a movement parameter under `ACT-008`; PEAK's free-grip,
  free-surface physics and deployable-aid genes are not reused.
- The Distress Pistol's item name, summit source, Lighthouse, seven days and
  badge remain game-scoped parameters, never canonical labels.
- No earlier reviewed game signature changes. Every generalised lower-ID gene
  remains true for all prior carriers under the wider wording.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] `TLD-001a`–`TLD-011`: one current standard
  `Hopeless Rescue` attempt binds cross-region survival, a fixed deadline and an
  ordered summit-to-Lighthouse signal route to explicit success or failure.

## New genes

- [Observation | Corroborated | High] `SYS-840` deletes a failed one-life
  attempt's resumable state at death without pretending that a checkpoint
  restores it or that deadline expiry uses the same storage transition.

## New combinations

- [Pattern | Corroborated | High] `COMB-0272` isolates the portable four-gene
  relation between a carried signal command, its terminal response, the
  life/place/item gate and the bounded survival-route objective.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_051`–`053` generalise
  seven existing labels or definitions without changing any earlier signature.

## New questions

- Which bounded DOOM Eternal campaign packet exposes its Glory Kill, resource
  conversion and arena-lock dependencies without importing the whole campaign?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0286` — DOOM Eternal, under the fixed
  first stable story-mission boundary recorded in Selection 017.

## Why this game

- [Hypothesis | Limited | Medium] It should replace long-route survival scarcity
  with short-horizon aggressive combat-resource conversion while preserving a
  bounded authored mission terminal.
