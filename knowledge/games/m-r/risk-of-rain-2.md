---
game_id: GAME-0270
slug: risk-of-rain-2
game_title: Risk of Rain 2
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0268
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-190
    - ACT-341
  system:
    - SYS-166
    - SYS-215
    - SYS-578
    - SYS-817
    - SYS-818
  constraint:
    - CON-269
  information:
    - INF-327
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Risk of Rain 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `632360`, base one-app package `172271`; checked 2026-09-06. **No build
  identifier is obtainable.** The public SteamCMD info projection reports
  `_missing_token` for this application and returns an empty depot section, so
  the branch and build data that every earlier unit in this batch used are not
  anonymously exposed at all. What the publisher does supply is a named version:
  the dated announcement `Alloyed Collective Patch 1.4.1` of 2025-12-09. A later
  dated announcement of 2026-02-19 states that a further update was released for
  one platform's controls but names no version. This unit therefore identifies
  the ruleset as the publisher's most recent named version `1.4.1` together with
  that acknowledged later unnamed update, and records the absence of any build
  identifier as a stated limitation rather than substituting a secondary
  observation it could not obtain. This is the exact inverse of `GAME-0268`,
  where the build was known and no version was.
- Product boundary: this is the base **Risk of Rain 2** application. All seven
  DLC apps `1236890`, `1607890`, `1905390`, `2306620`, `2781620`, `3055670` and
  `3055680` are outside this packet, and no DLC content, survivor, item or
  environment is admitted. The store lists a second package `445530` which also
  contains only this app but carries no price; the priced base package `172271`
  is the one this packet uses.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, a single-player run. The product offers three declared difficulty
  settings; this packet fixes the middle setting, `Rainstorm`, because the
  escalation rate this unit analyses is defined against it.
- Setup-only predecessors: the launch menu, the survivor selection and the
  drop-pod arrival. These are non-interactive or single-choice and establish a
  clean run only.
- Entry: accept first ordinary control of the chosen survivor in the first
  environment, immediately after leaving the drop pod, before any interactable
  is used.
- Primary decision loop: move the survivor through the environment and commit
  its declared skills against the hostiles the system creates; read the named
  escalation tier beside the run clock and understand that both the level of
  what is being fought and the price of everything not yet bought are rising
  from the same value; spend the currency that defeated hostiles pay at world
  interactables whose price is computed from that value, taking the permanent
  modifiers they hold; decide when the return on staying has fallen below what
  the escalation is costing; then find and activate the exit fixture, hold its
  disclosed radius for its declared minimum charge while the system sustains
  hostile pressure and a designated boss, defeat that boss, and take the opened
  exit.
- Positive terminal: arrive in the second environment with the run's accumulated
  modifiers, current health state and elapsed escalation carried forward, having
  charged the first environment's exit fixture to completion and defeated its
  designated boss. Verify on arrival that the escalation tier and the retained
  modifier set are the ones the first environment produced, and that the
  environment counter has advanced by one.
- Negative terminal: the survivor's health reaching zero ends the run and no
  transition occurs. Charging the fixture without defeating the designated boss,
  or defeating the boss without completing the charge, does not open the exit
  and is not success.
- Included: survivor movement through the environment; the survivor's declared
  skill set and the readiness gates on it; real-time hostile combat; the single
  health pool and its zero terminal; the permanent run modifiers taken from
  interactables and the events that trigger them; the currency defeated hostiles
  pay; the priced world interactables and the rule that computes their price;
  the escalation value that rises with elapsed run time and steps up per region
  cleared; the named escalation tier shown beside the run clock and the retained
  modifier display; the exit fixture, its disclosed radius, its declared minimum
  charge, the stall when the radius is left, its designated boss and the exit it
  opens; and the state that carries into the second environment.
- Excluded: all seven DLC apps and every survivor, item, environment and rule
  they add; multiplayer and every participant-count term in the escalation
  formula beyond one player; the `Drizzle` and `Monsoon` settings; the artifact
  rules; unlockable survivors, items and challenges outside a single run; the
  looping of environments beyond the first transition; the alternate ending
  routes; the shrine, drone, printer and other interactable classes beyond the
  priced chests this route uses, whose distinct resolutions are named as
  potential scoped modules; all inputs and platforms not declared above;
  screenshots, official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `632360` from package
  `172271`, confirm no DLC is enabled, and start a single-player `Rainstorm` run
  with no artifact selected. Pass the setup-only predecessors. From first
  ordinary control, defeat hostiles for currency, open at least one priced
  interactable and take its modifier, observe the named escalation tier change
  at least once beside the run clock, then activate the exit fixture, remain
  inside its radius for the declared minimum charge while defeating the
  designated boss, and take the opened exit. Then perform the stated arrival
  check. Exact survivor, environment, item identities, hostile composition, gold
  amounts and elapsed time are parameters.
- Potential scoped modules: a shrine, drone or printer interactable class; a
  second environment and the transition escalation it applies; the looped
  environments; the `Monsoon` setting; an artifact; multiplayer; or a DLC
  application requires its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus the
  current Steam product record establish lawful availability, exact product
  identity, Windows-only support, the two packages and the app each contains,
  the `Action` and `Indie` genres with no Early Access marker, the single- and
  multi-player categories with an adjustable difficulty category, and the seven
  separate DLC apps. The Valve news endpoint establishes the most recent
  publisher-named version and the later dated but unnamed update. The public
  SteamCMD info projection establishes only that this application's depot and
  branch data are not anonymously exposed, which is why no build identifier is
  asserted. The community-maintained product wiki, reached directly, corroborates
  the escalation coefficient and its formula in elapsed minutes, participant
  count, chosen difficulty and completed regions, the named ordered tier bar, the
  monster level formula and the per-level health and damage growth, the director
  spawn credits scaling from the same value, the interactable price and the
  monster gold reward both scaling from it, and the exit fixture's radius,
  minimum charge duration, stall rule, designated boss and completion reward.
  This is an evidence-backed rules reconstruction, not a claimed playthrough or
  entitlement. No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ROR-001` | Steam app `632360` and its priced base package `172271` identify the currently lawfully offered English Windows product, alongside a second unpriced package holding the same app and seven separate DLC apps | Confirmed | Direct | High | P1, P2 |
| `ROR-002` | This application's depot and branch data are not anonymously exposed, so no build identifier is obtainable from the public projection | Observation | Direct | High | S1 |
| `ROR-003` | The publisher's most recent named version is `1.4.1`, announced 2025-12-09; a later dated announcement of 2026-02-19 reports a further platform-controls update without naming a version | Observation | Direct | High | P3 |
| `ROR-004` | The run maintains an escalation coefficient computed from elapsed minutes, participant count and the chosen difficulty, multiplied by a factor raised to the number of regions completed | Observation | Corroborated | High | S2 |
| `ROR-005` | Entering a new environment increases that coefficient by a declared proportion of its current value | Observation | Corroborated | High | S2 |
| `ROR-006` | Hostile level is derived from the same coefficient, and each level above the base adds declared proportions of health and damage | Observation | Corroborated | High | S2 |
| `ROR-007` | The spawn directors' credit budget scales with the same coefficient, so stronger and more numerous hostiles are created as it rises | Observation | Corroborated | High | S2 |
| `ROR-008` | Interactable prices are computed from the same coefficient, and the gold a defeated hostile pays is multiplied by it | Observation | Corroborated | High | S2 |
| `ROR-009` | The interface shows the coefficient as a named ordered tier that changes as the value crosses its bands | Observation | Corroborated | High | S2 |
| `ROR-010` | The exit fixture spawns once per environment and begins its event when it is activated | Observation | Corroborated | High | S3 |
| `ROR-011` | Activation reveals a bounded charge radius; the charge advances while the player is inside it and does not advance while no player is inside | Observation | Corroborated | High | S3 |
| `ROR-012` | The charge takes a declared minimum duration even when the radius is held throughout | Observation | Corroborated | High | S3 |
| `ROR-013` | Hostiles and a designated boss spawn after activation, and completing the event requires both defeating that boss and fully charging the fixture | Observation | Corroborated | High | S3 |
| `ROR-014` | Completing the event drops a reward item, and interacting with the fully charged fixture moves the player to the next environment | Observation | Corroborated | High | S3 |
| `ROR-015` | The bounded identity is a run whose threat and prices are the same rising number, funded by elapsed time alone and stepped up further by each region cleared, whose only exit requires the player to stop moving for a declared interval | Strong Pattern | Corroborated | High | `ROR-004`–`ROR-014` |

## Basic data

- Release / origin: Hopoo Games; published by Gearbox Publishing and 2K, and
  released 2020-08-11.
- Platform or physical form: lawfully offered English Windows Steam application
  `632360`; one single-player `Rainstorm` run from the drop pod to the second
  environment.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=632360&cc=ua&l=english),
    for the exact title, app, Windows-only support, developer and publishers,
    release date, the `Action` and `Indie` genres with no Early Access marker,
    the single- and multi-player categories with an adjustable difficulty
    category, the seven DLC apps, the two packages and the current Ukraine
    offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=172271&cc=ua&l=english),
    for the priced base package `172271` containing only app `632360` and its
    current Ukraine offer, against which the unpriced package `445530` was
    checked.
  - **[P3]** [Valve news endpoint for this application](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=632360&count=25&feeds=steam_community_announcements),
    for the complete publisher announcement list, the 2025-12-09 `Alloyed
    Collective Patch 1.4.1` notes as the most recent named version, and the
    2026-02-19 platform-controls update announced without a version.
- Corroborating textual sources, accessed 2026-09-06:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/632360),
    which returns this application's common data with an empty depot section and
    a missing-token marker. It is cited only as evidence that no branch or build
    identifier is anonymously obtainable, and not as a version claim.
  - **[S2]** [community product wiki, Difficulty](https://riskofrain2.wiki.gg/wiki/Difficulty),
    for the escalation coefficient and its formula in elapsed minutes,
    participant count and chosen difficulty, the per-region multiplier, the named
    ordered tier bar, the monster level formula and its per-level health and
    damage growth, the director credit budget scaling from the same value, and
    both the interactable price and the monster gold reward scaling from it.
  - **[S3]** [community product wiki, Teleporter](https://riskofrain2.wiki.gg/wiki/Teleporter),
    for the fixture spawning once per environment, its activation, the bounded
    charge radius, the charge advancing only while a player is inside it, the
    declared minimum charge duration, the hostiles and designated boss that spawn
    after activation, the requirement to both defeat that boss and fully charge
    the fixture, the reward item and the transition to the next environment.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S3` under the declared app, package, named version,
  platform, input, difficulty setting, clean run, exclusions and terminal; rules
  reasoning, not direct play.
- Claim IDs: `ROR-001`–`ROR-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: move the survivor, one persistent controllable agent,
  through the environment's traversable geometry.
- Existing `ACT-190`: commit one of the survivor's declared skills and supply its
  aim. The Dota 2 boundary already covers activating one learned skill or carried
  item active with its legal vector or no-target input, so four survivor skill
  slots are parameters of that boundary. `ACT-161` was rejected because it
  requires an equipped combat tool that the player selects and can change, while
  these attacks belong to the survivor's own declared skill set.
- Existing `ACT-130`: spend the run's currency at a priced world interactable to
  take the modifier it offers.
- Existing `ACT-341`: address the exit fixture as a reachable authored object and
  commit its activation, and later its transition.
- Survivor, environment, item and hostile names remain parameters. Claims:
  `ROR-008`, `ROR-010`, `ROR-014`.

### System Behaviour Genes

- New `SYS-817`: one escalation value rises continuously with elapsed run time
  and steps up by a declared factor per region cleared, raising hostile level,
  health and damage together with the budget the system spends creating hostiles,
  the price the world's priced fixtures ask and the reward each defeated hostile
  pays. `TAXONOMY_CHANGE_030` added the last two, which `ROR-008` establishes at
  the same grade as the rest and which the gene had omitted while a Constraint
  delegated them to it. This is the packet's whole question. `SYS-054` escalates on completing another
  traversal of a closed route, `SYS-572` releases authored waves at scheduled
  stage minutes without a value that also prices the world, `SYS-378` scales to
  the character's own level, and `SYS-178` accumulates pressure from expansion
  and exploitation; none makes elapsed time itself the source of the escalation.
- New `SYS-818`: the region's only exit is opened by an activated fixture whose
  charge advances solely while the survivor is inside its disclosed radius, over
  a declared minimum duration, under sustained hostile pressure including a
  designated boss whose defeat is also required. `SYS-085` opens an exit on
  exhausting a finite target set, `SYS-383` and `SYS-384` resolve a contested
  capture or an escorted vehicle against an opposing side, and `SYS-061` holds a
  mechanism open only while a region is occupied without any pressure or exit
  consequence.
- Split-first review of `SYS-818`, required by `BATCH_015_GENE_AUDIT_001`
  finding `A-13`, compared its five clauses against the lower-ID registry.
  `SYS-703` and `SYS-561` accumulate progress an opposing side can reverse;
  `SYS-383` converts area control into an escort phase; `SYS-442` is shared
  repair progress that several participants add and that regresses when they
  stop. All four are now named in the gene's `Excludes` beside the three the
  record already rejected. The gene is retained on an atomicity argument
  stronger than "these happen during the same event": one activation fixes every
  term at once — the radius, the minimum duration, the stall rule, the hostile
  pressure and the designated boss — and the player has exactly one authority
  here, `ACT-341` addressing the fixture, after which the only input that matters
  is remaining inside a radius the activation itself disclosed. Splitting the
  charge from the pressure would produce a charge clause indistinguishable from
  an ordinary occupied-area timer and a pressure clause with no exit consequence,
  which is precisely the pair `SYS-061` and a timed defence already cover
  separately and which the record already rejects.
- Existing `SYS-166`: the modifiers taken from interactables persist for the run
  and apply automatically whenever a matching event occurs.
- Existing `SYS-215`: directly controlled combat resolves in real time against
  hostiles that acquire and receive targets.
- Existing `SYS-578`: one continuous health pool, whose zero closes the run.
- Resolution order: elapsed time and completed regions recompute the escalation
  value; that value fixes the level of every hostile created and the budget spent
  creating them, the price of every interactable and the gold each defeat pays;
  combat resolves in real time against those hostiles; taken modifiers apply at
  their matching events; and the exit fixture's charge advances only while the
  survivor holds its radius, with completion requiring both a full charge and the
  designated boss's defeat. Claims: `ROR-004`–`ROR-014`.

### Constraint Genes

- Existing `CON-269`: a skill resolves only when its target, range, charges and
  readiness gates are satisfied.
- No purchase-legality Constraint is carried by this packet.
  [`TAXONOMY_CHANGE_030`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_030.md)
  deprecated `CON-613`, which
  [`TAXONOMY_CHANGE_028`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_028.md)
  had restated one unit earlier, because the two halves of it belong elsewhere.
  Its automatic coefficient-to-price and coefficient-to-reward computation is a
  system response and is now stated inside `SYS-817`, whose evidence `ROR-008`
  always was. What that left behind was a bare affordability gate, and this
  record does not evidence one: `ROR-008` establishes that prices rise with the
  coefficient and that defeated hostiles pay more, while the transition table
  records only the successful purchase — "enough currency is held, pay at the
  interactable" — and no claim or row establishes a refusal for want of gold.
  The lower-ID Constraint registry was rescanned for a portable remainder:
  `CON-177` and `CON-210` bound carried capacity, `CON-248` requires a recurring
  balance, `CON-261` a buy window and location, `CON-417` city unlocks and
  capacity, and none states a bare balance gate. `ACT-130`, already in this
  signature, carries the purchase the record does evidence, so the honest result
  is subtraction rather than a replacement gene. The absent refusal evidence is
  recorded as a gap.
- Scarce resources: the health pool, the run's currency, the skills' readiness,
  and above all the elapsed time, which is the only resource that can be spent
  without being earned. Exact values are parameters. Claims: `ROR-006`–`ROR-008`.

### Information Genes

- `INF-236` was originally reused here and is removed by
  [`TAXONOMY_CHANGE_028`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_028.md).
  That gene's definition is conjunctive: it requires the clock, a kill count,
  level and experience progress, the retained weapon and passive-item build, and
  item levels available for inspection. This record's ledger establishes none of
  the kill count, the retained weapon display or inspectable item levels — no
  claim covers the run HUD's contents at all beyond `ROR-009`, which covers the
  escalation tier. Matching selected clauses of a conjunctive boundary is not
  carrying it, so `BATCH_015_GENE_AUDIT_001` finding `A-03` is upheld.
- No replacement Information gene is created, because none of this record's
  evidence establishes a general run-HUD disclosure. What the evidence does
  establish is the tier, and `INF-327` already carries it. The absence of a
  run-HUD claim is recorded as an evidence gap in Negative results rather than
  filled by a gene the ledger cannot support. Generalising or splitting
  `INF-236` was rejected outright: it would rewrite the boundary of a gene whose
  only remaining carrier, `GAME-0183` Vampire Survivors, does satisfy every
  clause.
- New `INF-327`: the interface additionally names the run's current escalation as
  an ordered tier beside that clock, so the player can read how far the world has
  already been strengthened and see it change, without being told the value or
  the formula. `INF-064` forecasts an authored weather phase and its hostility
  tier from a schedule; `INF-247` reports a settled reward grade after the fact;
  neither exposes a continuously rising live value as readable states.
- Exact tier names, band boundaries and bar rendering are presentation
  parameters. Claims: `ROR-009`.

### Objective Genes

- New `OBJ-164`: complete the attempt by opening the region's gated exit, taking
  it, and arriving in the next region with the run's accumulated modifiers,
  health state and escalation carried forward. `OBJ-107` survives a declared
  duration, `OBJ-029` clears a finite hostile set, `OBJ-026` reaches a location
  that needs no event, and `OBJ-080` crosses a threshold opened by defeating a
  guardian alone; none is satisfied by a transition that also carries the run's
  own accumulated cost forward.
- Charging without defeating the boss, or defeating the boss without completing
  the charge, is not success. Claims: `ROR-013`–`ROR-015`.

### Time Genes

- Existing `TIM-003`: the decision state advances on a real-time schedule
  throughout, and input remains accepted; there is no pause in which the
  escalation stops.
- The packet carries one time structure, and `SYS-817` is what makes that
  structure expensive. Claims: `ROR-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A clean run has completed only the setup-only predecessors | Accept ordinary control after the drop pod | The run begins in the first environment with no modifiers and the escalation at its opening value | fixed clean entry | `ROR-004` |
| The survivor is alive and no region has been cleared | Wait without advancing | The escalation value rises with elapsed time alone and the named tier eventually changes | time-funded escalation | `ROR-004`, `ROR-009` |
| The escalation value has risen | Observe a newly created hostile | Its level, health and damage are higher than an equivalent hostile created earlier | escalation reaches the world | `ROR-006` |
| The escalation value has risen | Observe the directors' output | More and stronger hostiles are created for the same event | budget scaling | `ROR-007` |
| The escalation value has risen | Approach a priced interactable | Its price is higher than the same class cost earlier, while defeated hostiles pay more gold | shared economy and threat | `ROR-008` |
| Enough currency is held | Pay at the interactable | The currency is spent and one permanent run modifier is taken | priced acquisition | `ROR-008` |
| A modifier has been taken and its trigger event occurs | Continue | Its declared effect applies without a separate command | persistent modifiers | `ROR-004` |
| The exit fixture has been found | Activate it | A bounded charge radius is revealed and hostiles with a designated boss begin to spawn | gated exit | `ROR-010`, `ROR-011`, `ROR-013` |
| The event is running and the survivor leaves the radius | Continue | The charge stops advancing while the hostile pressure continues | stationary requirement | `ROR-011` |
| The radius is held throughout | Wait | The charge still requires its declared minimum duration | irreducible standing cost | `ROR-012` |
| The charge is complete but the designated boss lives | Interact with the fixture | The exit does not open | joint completion | `ROR-013` |
| The charge is complete and the boss is defeated | Interact with the fixture | The exit opens and the survivor arrives in the second environment | reproducible positive terminal | `ROR-014` |
| The second environment has been entered | Read the interface | The retained modifiers and the escalation the first environment produced are carried forward, and the region step has been applied | carried run state | `ROR-005`, `ROR-015` |

## Strategic and experiential structure

- Planning horizon: the named tier, the current health pool and the modifiers
  already held decide how much longer the environment is worth searching before
  the exit event must be started.
- Local tactics: fight where the terrain limits how many hostiles can reach at
  once, spend currency as it arrives rather than saving it against prices that
  are still rising, and start the exit event with enough health to survive
  standing in one place for its declared minimum.
- Medium-term structure: the run is a wager against its own clock. Every minute
  spent enriching the survivor strengthens the world by the same value, and the
  exit event is the moment that wager is settled, because it forces the player to
  stop moving for a fixed interval at whatever escalation they have accumulated.
- Reversible versus irreversible: position, aim and which hostiles are engaged
  are freely revised; spent currency, elapsed time and a taken modifier are not,
  and the escalation never falls.
- Failure attribution: the named tier, the run clock and the modifier row are all
  visible before the exit event is started, so a loss traces to a decision to
  keep searching rather than to an unseen rule.
- Player trust: the escalation is disclosed as a readable tier before it is felt,
  the exit fixture's radius and its minimum charge are shown before the event is
  committed, and the reward the completed event pays is the same whenever it is
  taken.

## Replay and variation

- What changes: which survivor is chosen, which environment is generated, where
  the exit fixture and the interactables lie, which modifiers the interactables
  hold, which hostiles and boss the directors create, and how long the
  environment takes.
- Randomness or procedural generation: the environment is selected from an
  authored set and its interactable and fixture placements vary; the modifiers
  and hostile composition are drawn from authored tables against the current
  budget. The escalation formula itself is deterministic.
- Multiple strategies: the environment admits an immediate exit event with few
  modifiers at a low tier, a long search with many modifiers at a high tier, or
  anything between. The control demonstrates a single completed transition rather
  than making any amount of enrichment the terminal.
- Typical replay motive: reach the same transition at a lower tier, or hold more
  modifiers at the same one.

## Adjacent systems and history

- Hades is the selected near neighbour and the closest structural relative: both
  move one survivor through a generated region under real-time combat, take
  permanent run modifiers from priced or offered sources that trigger at matching
  events, gate skills on readiness and end the run at one health pool's zero.
  Hades escalates by chamber and by a chosen persistent difficulty, and its
  clock costs nothing; this packet makes elapsed time itself the source of both
  the threat and the prices, which is exactly the difference the selection asked
  about.
- Vampire Survivors shares the run clock, the build display and the survival
  pressure, but its pressure is an authored wave schedule indexed to stage
  minutes rather than one value that also prices the world, and its objective is
  to survive a fixed duration rather than to leave.
- Slay the Spire shares the persistent run modifiers exactly, and its escalation
  is by act and node rather than by any clock.
- Deep Rock Galactic shares a gathering phase closed by a departure event, but
  its pressure is a hostile population responding to the objective rather than a
  value that rises on its own.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-190`, `ACT-341` | survivor, skills, item and environment names are parameters |
| System Behaviour | `SYS-166`, `SYS-215`, `SYS-578`, `SYS-817`, `SYS-818` | escalation rate, per-region factor, radius, charge duration and boss composition are parameters |
| Constraint | `CON-269` | readiness gates are parameters |
| Information | `INF-327` | tier names, band boundaries and bar rendering are parameters |
| Objective | `OBJ-164` | region identity and the state that must carry forward are parameters |
| Time | `TIM-003` | frame pacing and spawn cadence are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `269` (`GAME-0001`–`GAME-0269`).
- Exact genome matches: none.
- Tied near matches: `GAME-0251` — Hades (`8 / 35 = 0.228571`).
- Supported combination subsets: `COMB-0268`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0251` — Hades | `ACT-008`, `ACT-130`, `ACT-190`, `SYS-166`, `SYS-215`, `SYS-578`, `CON-269`, `TIM-003` | Both move one survivor through a generated region, commit declared skills gated on readiness, resolve combat in real time, spend a run currency on offered sources whose permanent modifiers trigger at matching events, and end the run when one health pool reaches zero. Hades escalates by chamber and by a chosen persistent difficulty setting, so its run clock is free and a careful player is rewarded for taking time. This packet derives one escalation value from elapsed time itself, uses that same value to set hostile level, spawn budget, interactable price and gold reward together, and gates the region's only exit behind a charge that requires standing still for a declared minimum. The shared core is the run-and-modifier substrate; what the two products do with a clock is the opposite. | Near, `0.228571` |

### Preserved research notes

- New genes: `SYS-817`, `SYS-818`, `INF-327`, `OBJ-164`. `CON-613` was also
  created here and was deprecated by `TAXONOMY_CHANGE_030`.
- Reused genes: `ACT-008`, `ACT-130`, `ACT-190`, `ACT-341`, `SYS-166`, `SYS-215`,
  `SYS-578`, `CON-269`, `TIM-003`. `INF-236` was reused at integration and
  removed by `TAXONOMY_CHANGE_028`.
- Classification result: `New gene`.
- Lower-ID scan: this unit's selection asked whether a run whose difficulty rises
  with elapsed time alone, before any progress is made, is a distinct system
  boundary.
  The scan answers yes, and narrowly: the entire run-and-modifier substrate was
  reused from Hades, Slay the Spire and Vampire Survivors without change, and
  only the escalation itself, its economic consequence, its disclosure, the
  stationary exit gate and the transition objective required new genes. Reject
  `SYS-054`, `SYS-572`, `SYS-378` and `SYS-178` for the escalation, `SYS-085`,
  `SYS-383`, `SYS-384` and `SYS-061` for the exit event, `CON-177` and `CON-210`
  for the pricing, `INF-064` and `INF-247` for the disclosure, and `OBJ-107`,
  `OBJ-029`, `OBJ-026` and `OBJ-080` for the objective. Reject `ACT-161` for the
  survivor's skills. Reject a survivor-, item-, environment- or hostile-named
  gene.

## Taxonomy impact

- Registry changes: add `SYS-817`, `SYS-818`, `INF-327`, `OBJ-164` and
  `COMB-0268`, plus independent evidence for nine reused genes. `CON-613` was
  added here too and has since been deprecated by `TAXONOMY_CHANGE_030`.
- Taxonomy-change records:
  [`TAXONOMY_CHANGE_028`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_028.md)
  removed the `INF-236` reuse from this signature, which fell from fifteen genes
  to fourteen. `SYS-818` was reviewed split-first and retained with four further
  named exclusions.
  [`TAXONOMY_CHANGE_030`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_030.md)
  then corrected that record's false statement that `SYS-817` already carried the
  price and reward computation: it did not, so `SYS-817` was expanded to state
  what `ROR-008` establishes, and `CON-613` was deprecated by
  `TAXONOMY_CHANGE_030` because the bare
  affordability gate left over is not evidenced here. The signature falls again,
  to thirteen genes. `GAME-0183` keeps `INF-236` unchanged, and no ID was retyped
  or reused.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, survivor, item,
  environment, hostile, app and package names remain parameters.

## Negative results

- No video or audio evidence was used; only official product data, the Valve news
  endpoint and a community-maintained product wiki support this packet.
- **No build identifier is asserted, and none could be obtained.** This is a
  fifth distinct version situation for the batch and the exact inverse of
  `GAME-0268`: there the build was known and no publisher statement named a
  version; here the publisher names version `1.4.1` and acknowledges a later
  unnamed update, while the distribution projection every earlier unit relied on
  exposes no depot or branch data for this application at all. The record states
  the limitation rather than substituting a secondary observation it does not
  have.
- Multiplayer is excluded although the escalation formula contains participant
  terms, because admitting it would change the coefficient, the boss composition
  and the charge rate at once and would require its own bounded scope.
- The `Drizzle` and `Monsoon` settings are excluded because the escalation rate
  this unit analyses is defined against the middle setting; the setting is a
  declared multiplier and naming a different one would change every quantity in
  the packet.
- Shrines, drones, printers and the other interactable classes are excluded and
  named as potential scoped modules, because their distinct resolutions are not
  required by the declared route and admitting them would add rules the terminal
  does not test.
- Environment looping and the alternate ending routes are excluded because they
  lie beyond a single transition.

## Delta summary

## New facts

- [Observation | Corroborated | High] `ROR-001`–`ROR-015`: a run whose threat and
  prices are the same rising number, funded by elapsed time alone and stepped
  up further by each region cleared, whose only exit requires the player to stop
  moving for a declared interval.

## New genes

- [Observation | Corroborated | High] `SYS-817`, `SYS-818`, `INF-327`,
  `OBJ-164` — escalation funded by elapsed time alone before any progress and pricing
  the world from the same value, an exit gated behind a stationary charge under
  sustained pressure, that value disclosed as a named tier, and a transition
  objective that carries the run's own cost forward. `CON-613` was created here
  as a fifth and was deprecated by `TAXONOMY_CHANGE_030`.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0268` — a run in which staying
  strengthens the world and leaving requires standing still.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Does a second product reuse `SYS-817`, or is escalation funded by elapsed time
  rather than by progress specific to this run model?

## Next recommended game

- [Hypothesis | Limited | High] None; this unit closes the recorded 261-to-270
  horizon. The next unit is `SEARCH_DEMAND_BATCH_015_AUDIT`.
- Optimisation criterion: not applicable; the batch audit resolves the recorded
  open questions before a further selection is made.
- Expected information gain: the audit's own findings.
- Backlog impact: completes the recorded horizon.

## Why this game

- [Hypothesis | Limited | High] The selection asked whether a run whose
  difficulty rises with elapsed time, rather than with progress, is a distinct
  system boundary. The completed decomposition answers yes, and shows exactly how
  narrow the distinction is: ten of the fifteen genes came unchanged from
  already-reviewed run-based products, and what the escalation actually adds is
  that the same value which strengthens the opposition also prices everything the
  player might buy, so a player cannot save their way out of it — and that the
  only exit demands the one behaviour that escalation punishes.
