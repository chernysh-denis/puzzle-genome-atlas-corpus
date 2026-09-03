---
game_id: GAME-0232
slug: payday-3
game_title: PAYDAY 3
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0230
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-190
    - ACT-199
    - ACT-241
    - ACT-341
    - ACT-358
    - ACT-359
  system:
    - SYS-208
    - SYS-215
    - SYS-348
    - SYS-384
    - SYS-618
    - SYS-646
    - SYS-647
    - SYS-648
    - SYS-650
    - SYS-651
  constraint:
    - CON-262
    - CON-269
    - CON-526
    - CON-527
    - CON-528
    - CON-529
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-246
    - INF-256
    - INF-257
  objective:
    - OBJ-124
  time:
    - TIM-003
---

# Game: PAYDAY 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded English Windows Steam client, application
  `1272080`, official Update `3.8.1`, Unreal Engine 5 and public build
  `24964769`, built and updated `2026-08-27`, checked `2026-09-03`; Solo Mode,
  base-game Core Heist `Road Rage`, Normal difficulty, no favors and one human
  heister with three stock Crew AI.
- Declared loadout and account boundary: the first legally available unmodified
  base primary firearm, secondary firearm, armour lining and Ammo Bag; no skill
  points, weapon modifications, OVERKILL weapon or account-derived advantage.
  The already available core heist and stock equipment are entry predicates,
  not claims about a fresh-profile unlock route.
- Primary decision loop: read the live objective and local threats; prevent a
  civilian escape, retrieve and activate the EMP, prepare two road gaps, move
  the forklift obstruction and open the gate; install and activate the steering
  device; remain inside the escort circle so the transport advances while
  fighting police; drill the electronics hatch and cut the cables; bag, carry,
  throw and secure five rare-earth payloads; signal and occupy the escape; read
  the retained Heist Results settlement.
- Reproducible trace: from planning select Solo Mode, `Road Rage`, Normal and no
  favors, retain the declared stock loadout and accept first masked control.
  Restrain every civilian able to reach an exit; take the EMP from its marked
  crate, place and activate it before the 90-second arrival limit; install all
  four wheel ramps, move the forklift crate and open the electric gate. After
  the transport stops, retrieve, attach and activate the steering device, then
  keep the human heister in its circle and reactivate it after any prepared
  route stop. At the terminal position drill the electronics hatch, remove the
  drill, open the panel and cut the cables. Bag and secure the first five rare-
  earth payloads, light the flare, wait for the helicopter, enter the marked
  escape and retain the result screen. Enemy, civilian, crate/panel, helicopter-
  side, damage and timing samples remain run parameters.
- Entry and exit: begins at first retained masked control on the bridge after
  the planning countdown. It ends only when five required bags are credited,
  the human player occupies the active escape, the heist declares success and
  Heist Results exposes the retained payout; stop before spending, levelling,
  challenges or another heist.
- Included: one loud-only bridge heist; civilian compliance and finite cable
  ties; EMP, ramps, forklift, gate and steering-device interactions; human-only
  proximity escort; road-obstacle stops and reactivation; continuous firearm
  combat, armour, health, downing and Crew-AI revival; Ammo Bag and ammunition;
  cyclical police pressure; the short hatch drill, cable cut, deposit-box loot,
  five heavy bags, helicopter deposit, escape and payout.
- Excluded: every other heist, difficulty and execution method; all DLC,
  favors, mods and exploits; public/private multiplayer, matchmaking, human
  co-op and drop-in; skill, build, weapon and armour optimisation; optional
  sixth and later bags, loose cash and all deposit boxes; achievements,
  challenges, Infamy, Renown, vendors, cosmetics, Battle Pass or account grind;
  all seasons and the complete live-service history.
- Potential scoped modules: a current human crew, another difficulty, one
  optional-loot stop, another core heist or one reworked heist after its rules
  stabilise.
- Direct-play status: no authenticated client playthrough was conducted.
  Starbreeze's current update, product, Solo Mode and UI materials establish the
  product, mode and terminal surface; current Road Rage fixes show the route
  remains supported. A detailed Normal written trace corroborates the ordered
  EMP, road preparation, escort, drill, five-bag and escape sequence. The table
  below is rules reconstruction, not direct observation. No video or audio was
  opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PD3-001` | Update `3.8.1` and Steam public build `24964769` are the current unmodded Windows ruleset | Confirmed | Corroborated | High | P1, P2, S1 |
| `PD3-002` | Solo Mode skips matchmaking, admits no human co-op and runs the heist with one human plus stock Crew AI | Confirmed | Direct | High | P3, P4 |
| `PD3-003` | Road Rage is a base Core Heist whose bounded route is loud-only rather than a stealth/loud union | Confirmed | Corroborated | High | P2, P5, S2 |
| `PD3-004` | EMP activation before the arrival limit and preventing civilian escape are early failure gates | Observation | Corroborated | High | P5, S2 |
| `PD3-005` | Four ramps, the movable obstruction and electric gate are route predicates for the overridden transport | Observation | Corroborated | High | P5, S2 |
| `PD3-006` | The transport advances only while a human heister occupies its escort circle, stops at unmet route gates and can be reactivated | Observation | Corroborated | High | P5, S2 |
| `PD3-007` | At route end a short drill, panel opening and cable cut breach the rear doors while live police pressure continues | Observation | Corroborated | High | P5, S2 |
| `PD3-008` | Five secured rare-earth bags enable the Normal escape; further bags are optional | Observation | Corroborated | High | P5, S2 |
| `PD3-009` | The revamped Heist Results screen separates the successful heist settlement from later account choices | Confirmed | Direct | High | P6, P7 |
| `PD3-010` | The declared no-favor Solo trace reaches a bounded success or formal failure result without DLC, human co-op or account optimisation | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Starbreeze Studios; published by Deep Silver at the 2023
  Windows release and currently developed and published by Starbreeze.
- Platform or physical form: local Windows PC client with initial online
  identification, one directly controlled first-person heister and three stock
  cooperative bots.
- Puzzle family: loud objective execution; route preparation and proximity
  escort; civilian control; interruptible fixture work; spatial loot routing;
  retained heist settlement.
- Primary sources:
  - **[P1]** [official Update 3.8.1 changelog](https://www.paydaythegame.com/news/payday3/2026/08/update-3-8-1/),
    dated 2026-08-27, for the live PC update, current integrity guidance and no
    Road Rage rule replacement.
  - **[P2]** [official Update 3.8 changelog](https://www.paydaythegame.com/news/payday3/2026/08/update-3-8/),
    dated 2026-08-25, for the Unreal Engine 5 boundary and current content scope.
  - **[P3]** [official Solo Mode explanation](https://www.paydaythegame.com/news/payday3/2024/06/medicbag-update16/),
    for local execution after identification, skipped matchmaking and the
    prohibition on human co-op inside Solo Mode.
  - **[P4]** [official PAYDAY 3 product page](https://www.paydaythegame.com/payday3/),
    for solo or cooperative heists, firearms, hostages and loot.
  - **[P5]** [official Update 3.4 changelog](https://www.paydaythegame.com/news/payday3/2026/04/update-3-4/),
    for Crew AI bag handling, explicit planning difficulty text and the repaired
    Road Rage second-hole progression gate; checked against later updates.
  - **[P6]** [official Anniversary UI revamp](https://www.paydaythegame.com/payday3/updates/uirevamp/),
    for heist/difficulty planning, preplanning and the revamped result screen.
  - **[P7]** [official Update 2.2.1](https://www.paydaythegame.com/news/payday3/2025/09/update-2-2-1/),
    for current Road Rage bag collision, secure-loot notification and maintained
    route support.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB PAYDAY 3 depots](https://steamdb.info/app/1272080/depots/),
    observed 2026-09-03, for Windows application `1272080`, public build
    `24964769`, built 2026-08-27 06:39:48 UTC and updated 12:35:25 UTC.
  - **[S2]** [Slyther Games Road Rage Normal guide](https://www.slythergames.com/2023/10/09/payday-3-road-rage-heist-guide/),
    for the loud-only boundary, 90-second EMP, civilian gate, four ramps,
    forklift, electric gate, steering device, human escort circle, short drill,
    five required bags and escape. Current official `P1`, `P2`, `P5` and `P7`
    show no later replacement of that route.
  - **[V1]** repository-side transition trace derived from `P1`–`P7` and
    `S1`–`S2`; executable rules reasoning, not direct play.
- Claim IDs: `PD3-001`–`PD3-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`, move the heister; `ACT-161`, aim and fire; `ACT-164`, switch
  weapon or equipment; `ACT-183`, reload; `ACT-190`, deploy the Ammo Bag;
  `ACT-199`, collect ammunition; `ACT-241`, revive a reachable downed bot;
  `ACT-341`, operate EMP, ramps, forklift, gate, steering device, drill, panel,
  cables, flare and deposit boxes; `ACT-358`, intimidate and tie civilians;
  `ACT-359`, bag, carry, throw and secure rare-earth payloads.
- Candidate genes: none. The authored object identities and exact counts are
  parameters, not vocabulary.
- Claim IDs: `PD3-004`–`PD3-008`.

### System Behaviour Genes

- `SYS-208`, firearm and cover resolution; `SYS-215`, live combat; `SYS-348`,
  armour, health, downing and revival; `SYS-618`, stock Crew AI; `SYS-646`,
  civilian compliance and restraint; `SYS-647`, the short interruptible drill;
  `SYS-648`, cyclical police pressure.
- `SYS-384` advances the authored transport from eligible human proximity and
  stops it at missing route preparations; `SYS-650` converts rare-earth sources
  into carried and spatially secured credit; `SYS-651` settles escape into a
  retained payout.
- Resolution order: planning; timed ambush and civilian gates; route preparation;
  override; proximity escort under police pressure; drill/cable breach; bagging
  and secure credit; escape and result settlement.
- Claim IDs: `PD3-004`–`PD3-010`.

### Constraint Genes

- `CON-262` bounds weapons, ammunition and deployable stock; `CON-269` gates
  Ammo Bag placement; `CON-526` requires a compliant reachable civilian and a
  finite cable tie; `CON-527` requires live reach at the drill fixture;
  `CON-528` enforces exclusive heavy-bag carriage and compatible deposit;
  `CON-529` requires five secured bags before escape can settle.
- Scarce strategic resources: the EMP clock, cable ties, human escort presence,
  armour, health, down allowance, ammunition, Ammo Bag charges, safe drill
  access, bag route and time between police-pressure peaks.
- Claim IDs: `PD3-004`–`PD3-008`.

### Information Genes

- `INF-073` shows firearm, ammunition and equipment; `INF-115` limits hostile
  and civilian knowledge to local sight, sound and effects; `INF-116` shows Crew
  AI and shared objective state; `INF-119` shows armour, health and down state;
  `INF-246` supplies teammate-danger and incoming-pressure cues.
- `INF-256` joins current objective, timers, transport circle/route state,
  drill, bag percentage and escape availability; `INF-257` exposes success,
  secured value and payout at Heist Results.
- Candidate genes: none.
- Claim IDs: `PD3-004`–`PD3-010`.

### Objective Genes

- `OBJ-124` requires breaching the declared secured transport, securing the
  five-bag Normal minimum and occupying the active escape for success/payout.
- Success, evaluation and failure: five bags plus legal escape are sufficient;
  optional bags increase value without changing success. Civilian escape before
  EMP commitment, missed EMP timing or loss of the only human control before
  legal recovery produces a failed result or rejected attempt.
- Claim IDs: `PD3-004`, `PD3-008`–`PD3-010`.

### Time Genes

- `TIM-003` advances the EMP deadline, transport, interactions, police phases,
  combat, armour recovery, downing and bots continuously without tactical pause.
- Candidate genes: none.
- Claim IDs: `PD3-004`–`PD3-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First masked bridge control, EMP unplaced and civilians mobile | Restrain exit-capable civilians, carry the EMP to its marker and activate it before 90 seconds | Escaped civilian or expired deadline fails; legal activation commits the ambush and admits the transport | bounded early failure gate | `PD3-004` |
| Transport has not reached the broken route | Install four wheel ramps, move the forklift crate and open the electric gate | Each prepared fixture clears its authored obstruction; an unmet fixture later stops progress | spatial route predicates | `PD3-005` |
| EMP has stopped the transport | Retrieve, attach, hack and reactivate the steering device | The transport enters its authored escort route and exposes the human-presence circle | override-to-escort transfer | `PD3-006` |
| Overridden transport has a clear next segment | Keep the human heister inside its circle while fighting | It advances; leaving the circle or reaching an unmet route fixture stops it, and Crew AI presence alone is insufficient | proximity-driven autonomous transport | `PD3-006` |
| Transport reaches the terminal ramp | Place the drill, wait, remove it, open the panel and cut the cables | Retained drill progress exposes the cable interaction and the rear doors open | interruptible fixture chain | `PD3-007` |
| Deposit boxes are open and the helicopter is available | Bag, carry or throw the first five rare-earth payloads into the secure region | Each compatible crossing increments secured progress; the fifth enables escape while later bags remain optional | spatial value credit and greed boundary | `PD3-008` |
| Five required bags are secure | Occupy the marked escape and accept Heist Results | The heist closes successfully and the result exposes retained payout before later account choices | bounded positive terminal | `PD3-009`, `PD3-010` |

## Strategic and experiential structure

- Local decision: trade escort-circle exposure, cover, aimed fire, reload,
  ammunition recovery and bot rescue against the next route interaction.
- Medium-term planning: prepare the bridge before the truck reaches each gap,
  preserve the human escort body, place supplies near the route, and stage five
  bags toward the helicopter without chasing optional value.
- Long-term structure: convert a timed ambush into controlled transport, turn
  proximity and road preparation into a breach, then stop greed at the exact
  minimum and settle the retained payout.
- Common heuristics: activate EMP first, clear all route gates during the wait,
  re-enter the circle after fighting, interact during lower pressure, throw bags
  in safe relays and escape immediately after the fifth credit.
- Failure attribution: objective text, deadline, civilian markers, obstruction
  prompts, escort circle, drill state, team frames, armour/health, bag percentage
  and result screen distinguish route, combat, credit and terminal failures.
- Player-trust factors: prepared obstacles must stay cleared; Crew AI must not
  impersonate required human escort presence; the fifth secured bag must enable
  escape; result payout must follow the credited bags.
- Claim IDs: `PD3-004`–`PD3-010`.

## Replay and variation

- What changes between sessions: civilian paths, marked crate/panel placement,
  enemy composition, damage, Crew-AI choices, helicopter side and bag routing.
- Randomness or procedural generation: the fixed bridge and ordered objective
  chain remain stable; local spawn and combat samples are retained parameters.
- Multiple viable strategies: route preparation can be reordered and bags can
  be relayed differently, but this packet fixes Solo, Normal, no favors and the
  five-bag stop.
- Typical replay motive: improve simultaneous road preparation, circle uptime,
  drill defence or bag relay; compare another declared crew/difficulty module.
- Claim IDs: `PD3-004`–`PD3-009`.

## Adjacent systems and history

- Direct predecessor: PAYDAY 2 established casing/loud transitions, police
  phases, civilians, drills, Crew AI, heavy loot and retained contract payout.
- Variants: other PAYDAY 3 heists can admit stealth, different fixtures and
  optional routes; current reworks are separate rulesets.
- Similar games: Marvel Rivals and Team Fortress 2 share proximity-driven
  objective vehicles but add opposing contest, team roles and match scoring;
  Left 4 Dead 2 shares one human with three bots, live combat and revival.
- Important differences: Road Rage begins masked and loud, makes the human body
  rather than the whole team the escort key, requires authored bridge repair,
  and ends through five spatially credited bags plus escape rather than route
  arrival, enemy clearance or match score.
- Claim IDs: `PD3-002`–`PD3-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-199`, `ACT-241`, `ACT-341`, `ACT-358`, `ACT-359` | direct movement, combat, fixtures, civilians and bags |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-348`, `SYS-384`, `SYS-618`, `SYS-646`, `SYS-647`, `SYS-648`, `SYS-650`, `SYS-651` | combat, bots, escort, drill, police, loot and payout |
| Constraint | `CON-262`, `CON-269`, `CON-526`, `CON-527`, `CON-528`, `CON-529` | capacity, restraint, reach, carriage and terminal gates |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-246`, `INF-256`, `INF-257` | local combat, team, objective, transport, loot and result cues |
| Objective | `OBJ-124` | breach, secure five required payloads and escape |
| Time | `TIM-003` | continuous ambush, escort, combat and fixture time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `231` (`GAME-0001`–`GAME-0231`).
- Exact genome matches: none.
- Tied near matches: `GAME-0201` — PAYDAY 2 (`34 / 39 = 0.871795`).
- Supported combination subsets: `COMB-0230`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0201` — PAYDAY 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-199`, `ACT-241`, `ACT-341`, `ACT-358`, `ACT-359`, `SYS-208`, `SYS-215`, `SYS-348`, `SYS-618`, `SYS-646`, `SYS-647`, `SYS-648`, `SYS-650`, `SYS-651`, `CON-262`, `CON-269`, `CON-526`, `CON-527`, `CON-528`, `CON-529`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-246`, `INF-256`, `INF-257`, `OBJ-124`, `TIM-003` | Both use one human with three stock bots, live firearm/down pressure, civilian restraint, an interruptible drill, cyclical police response, heavy bags, minimum-loot escape and retained payout. PAYDAY 2 begins in casing and makes detection/alarm irreversible; PAYDAY 3 Road Rage begins loud, removes the stealth commitment, and instead requires a prepared bridge plus human-only proximity escort before its five-bag terminal | Near, `0.871795` |

### Preserved research notes

- New genes: none; existing labels and definitions are broadened only where the
  second-game evidence confirms the same transportable boundary.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: genre similarity does not union all PAYDAY systems.
  The loud-only packet omits stealth/detection commitment and retains exactly
  the route, combat, civilian, drill, five-bag and payout dependencies exercised.

## Taxonomy impact

- Registry changes: `ACT-359`, `SYS-384`, `SYS-650`, `SYS-651`, `INF-256`,
  `INF-257` and `OBJ-124` gain PAYDAY 3 support and broader wording without
  changing any earlier reviewed signature or lifecycle.
- Taxonomy-change record: none.
- Candidate terms affected: one-sided proximity escort, route preparation,
  bagged valuables and heist settlement are retained known-gene parameters.

## Negative results

- No Rest for the Wicked was rejected because official Update 3.4 reworked its
  objectives and randomisation; it is not silently combined with Road Rage.
- Road Rage's fixed bridge is one heist, not evidence for every current or
  historical PAYDAY 3 contract.
- Optional sixth and later bags are payout variation, not part of the bounded
  terminal objective.
- Police kills regulate space and survival; they are not a finite-clearance win.
- No video evidence was used, so no audiovisual claim or timestamp enters the ledger.
