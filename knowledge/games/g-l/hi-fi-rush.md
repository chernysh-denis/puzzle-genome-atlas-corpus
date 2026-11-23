---
game_id: GAME-0516
slug: hi-fi-rush
game_title: Hi-Fi RUSH
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-341
    - ACT-356
    - ACT-709
  system:
    - SYS-215
    - SYS-369
    - SYS-409
    - SYS-578
    - SYS-736
    - SYS-799
    - SYS-822
    - SYS-1386
    - SYS-1459
    - SYS-1460
    - SYS-1461
    - SYS-1462
    - SYS-1463
    - SYS-1464
    - SYS-1465
    - SYS-1466
  constraint:
    - CON-282
    - CON-402
  information:
    - INF-142
    - INF-334
    - INF-501
  objective:
    - OBJ-029
    - OBJ-080
  time:
    - TIM-003
---

# Game: Hi-Fi RUSH

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Track names, button labels, sounds, enemies and beat counts are parameters.

## Analysis scope

- Version / ruleset: released English Xbox Series X|S base campaign,
  release-era documentary reference from January 2023. Fresh Normal start,
  ordinary controller inputs, no timing automation, no replay equipment.
  Showing the optional visual beat aid belongs to the ordinary ruleset.
  Xbox product ID `9NFTC552K3GJ` identifies the product, not an executable build.
- Structured analysis target: `PLAT-XBOX-SERIES`.
- Primary decision loop: cross the authored factory route and clear its sealed
  Choruses. Read the music pulse and enemy warnings, select attack types and
  gaps, time inputs for stronger hits or a Beat Hit, evade incoming attacks,
  and spend earned Reverb when useful. Read how each fight settled, then
  use the openings left by QA-1MIL to finish the first Track.
- Entry and exit: first ordinary control in the assembly line after Chai's
  operation. End after the QA-1MIL clear, first Track results and arrival at
  the Hideout, before using any Hideout service or starting Track 2.
- Included: light and heavy input timing, tutorial and actual enemy encounters,
  learned Beat Hits, ordinary and timed evasion, double jumping and moving
  platforms, attacks on breakable fixtures, the required generator prompt,
  Power Chord and collectible Reverb batteries, tough-enemy stability,
  eight Chorus outcomes and reduced score for repeated moves, normal
  checkpoint continues, and QA-1MIL's hand openings and optional head exposure
  after two successful counters during the mandatory boss encounter.
- Excluded: post-clear replay, spending Gear, permanent upgrades, parry and
  deployable partners learned later, optional collectible completion, replay
  doors, Rhythm Master, Arcade and other modes, and any later patch or port
  rules. Exact damage, scoring coefficients, input windows and thresholds
  are outside the evidence.
- Potential scoped modules: later learned parry sequences, partner and Jam
  Combo economy, and postgame rank-gated survival each need separate review.
- Direct-play status: no native executable, console or controller was used.
  The launch Xbox announcement and two developer transcripts support ordinary
  rhythm rules. Published practical routes and the launch Xbox play report
  support the sequence and grades. The official gameplay deep dive's published
  result-frame description corroborates grading labels. No video or audio was
  played. The installed patch and exact Normal tuning were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| HR-001 | The base game was released for Xbox Series on 25 January 2023. | Confirmed | Direct | High | P1, P2 |
| HR-002 | The system aligns an accepted ordinary attack's impact with the beat even after an off-beat press. Pressing on beat can improve the attack. | Observation | Corroborated | High | P2, P3, P4, R2 |
| HR-003 | Light and heavy use distinct beat spacing. Supported input order and intentional rests select different attack chains. An eligible chain offers a distinct timed Beat Hit. | Observation | Corroborated | High | P2, P3, R2, R3, R5 |
| HR-004 | The route teaches attacks and Beat Hits in stages and interleaves sealed encounters with authored traversal. Successful rhythmic inputs restart the required generator. | Observation | Corroborated | High | R1, R2, R3 |
| HR-005 | The battery introduces Reverb and Power Chord. Beat Hits can produce collectible Reverb batteries. Tough enemies can resist interruption until their visible Stun Gauge is depleted. | Observation | Corroborated | Medium | R1, R2, R3, R5, R9 |
| HR-006 | A missed slam can leave an attackable hand. The boss changes attack patterns by phase. Qualifying damage to each hand enables a separate timed counter. Completing both fully exposes the head. | Observation | Corroborated | High | R2, R4, R5 |
| HR-007 | Chorus settlement reports Score, Just Timing and Clear Time. Repeated manoeuvres can score less. The Normal story can advance without an S grade. A Continue can affect the Track result. | Observation | Corroborated | High | P2, R2, R6, R7, R8 |
| HR-008 | Movement, jump, dodge and attack commands remain live. Attack cues, the music pulse and the optional visual beat guide offer different timing information. | Observation | Corroborated | High | P3, P4, R2, R6 |
| HR-009 | Exact Normal damage, input tolerance and grade coefficients remain unresolved by the sources. | Observation | Limited | High | P1–P4, R1–R9 |

## Basic data

- Release / origin: Tango Gameworks, full Xbox Series X|S release on
  25 January 2023. Bethesda Softworks published the original release. The
  storefront now identifies KRAFTON, Inc.
- Platform or physical form: digital base Xbox Series game with controller.
- Puzzle family: tactical forecast and counterplay, and real-time system
  pressure. Enemy anticipation, beat phase and a limited counterattack
  opportunity affect action choice inside freely navigable arenas.
- Primary sources:
  - P1 [Xbox Store product](https://www.xbox.com/en-US/games/store/hi-fi-rush/9nftc552k3gj).
  - P2 [Xbox launch announcement](https://news.xbox.com/en-us/2023/01/25/hi-fi-rush-reveal-out-now-game-pass/).
  - P3 [John Johanas launch interview transcript](https://news.xbox.com/en-us/podcast/hi-fi-rush-redfall-and-the-developer_direct/).
  - P4 [Developer oral history](https://news.xbox.com/en-us/2023/10/04/hi-fi-rush-exclusive-oral-history/).
- Corroboration and evidence limits:
  - R1 [Track 1 route order](https://hifi-rush.fandom.com/wiki/Track_1:_A_Fresh_Start),
    used for traversal, instructions and encounter order.
  - R2 TrueAchievements authors' [Track 1 route](https://www.trueachievements.com/game/HiFi-Rush/walkthrough/4),
    [combat reference](https://www.trueachievements.com/game/HiFi-Rush/walkthrough/2)
    and [story assessment](https://www.trueachievements.com/game/HiFi-Rush/walkthrough/3).
    The [first-person achievement account](https://www.trueachievements.com/a382232/does-that-say-weakpoint-achievement)
    details the two fist interactions.
    Relevant indexed excerpts were accessible; full pages were not.
  - R3 [Neoseeker practical route](https://www.neoseeker.com/hi-fi-rush/walkthrough/Track_One),
    cross-check from indexed tutorial, production line and boss excerpts.
  - R4 [Launch-period QA-1MIL encounter account](https://www.gamepur.com/guides/how-to-defeat-the-qa-1mil-boss-in-hi-fi-rush),
    for the missed slam, later attacks and optional head exposure.
  - R5 [AE_EBYS first-person route notes](https://note.com/ae_ebys/n/n40c7a03a5e89?hl=en),
    higher-difficulty practice evidence used for shared move and boss
    structure only. D-rank failure, loadout, margins and route optimisations
    from that difficulty are outside scope.
  - R6 [Launch-day Xbox play report](https://www.windowscentral.com/gaming/hi-fi-rush-review),
    for the separate factors in the assessment and the timing aid.
  - R7 [Developer deep-dive result frame description](https://playcraft.space/gallery/e/hi-fi-rush-final-result-chorus-1-score-20-178-grade-b-just-timing-50-grade-c-clear-time-52s-grade-s-each-row-with-its-bonus/),
    attributed frame at 307 seconds. No sample values or demonstration
    equipment are treated as fresh Track 1 defaults.
  - R8 [XboxAchievements scoring observations](https://www.xboxachievements.com/game/hi-fi-rush/guide/),
    checks repetition against the distinct timing and speed grades.
  - R9 [Launch-period Reverb observations](https://tryhardguides.com/how-to-charge-up-reverb-gauge-in-hi-fi-rush/),
    corroborates the battery pickups. Sources differ on whether some
    ordinary accurate strikes also directly credit Reverb.
- Claim IDs: HR-001–HR-009.

## Mechanical decomposition

### Action Genes

- `ACT-008` directs Chai through the factory and within each arena.
- `ACT-161` selects and commits the current weapon attack against a reachable
  robot or strikeable object. The light and heavy Xbox inputs are X and Y.
- `ACT-223` reacts to a signalled attack by dodging or jumping while that
  response can still avoid it. Track 1 does not give Chai the later parry.
- `ACT-341` interacts with a reachable fixture, including starting the
  generator's prompt. Interaction and the subsequent rhythm sequence differ.
- `ACT-356` commits a directional dodge. Evasion can create room to approach
  again, with timed follow-up dodges available.
- `ACT-709` makes the distinct prompted attack press at a Beat Hit opportunity
  after a supported chain. The regular chain has already been executed.
- Claim IDs: HR-002–HR-006, HR-008.

### System Behaviour Genes

- `SYS-215` resolves reaches, hits, damage, interruptions and defeat in live
  combat. `SYS-578` updates Chai's health through incoming damage and pickups.
  `SYS-369` restores the authored checkpoint after choosing to continue.
- `SYS-1459` aligns the committed ordinary impact with the beat while the
  animation is already in motion. `SYS-1460` grades the press for increased
  damage. An off-beat press can therefore lead to an on-beat ordinary impact
  without earning the input-time bonus.
- `SYS-1461` evaluates typed attack order and authored rests. The first
  lessons use a one-beat light and longer two-beat heavy spacing. A deliberate
  rest after an eligible light input can select a different string.
- `SYS-736` advances the staged practice when its instruction predicate is
  met. `SYS-1464` uses a timed sequence at the generator to restore the
  route. It is a required fixture interaction, with a different consequence
  from missing a Beat Hit during ordinary combat.
- `SYS-1386` allows an extra jump before landing and resets it on support.
  `SYS-1465` lets a successful Beat Hit release battery pickups before
  defeat. Collecting them fills Reverb. After the route unlocks Power Chord,
  an available charge can be spent on that attack. The sources differ on
  additional sources of Reverb. `SYS-409` converts the tough enemy's depleted stability
  into an opening for interruption and continued attacks.
- `SYS-1462` leaves a reachable attack component temporarily exposed after
  a missed slam. `SYS-799` changes the boss's attack patterns as its health
  crosses phases. Damage to each embedded hand can expose that hand’s
  contextual rhythm prompt. Under `SYS-1463`, each successful counter uses
  the hand to remove part of the faceplate. Both successes fully expose
  the head. Ordinary hand damage remains available after a missed prompt.
- `SYS-1466` reduces the score credit for repeating the same manoeuvre
  consecutively. The live Rhythm Gauge also weights scoring. `SYS-822`
  settles each Chorus and the Track into evaluated results. Score,
  accuracy relative to the beat, and clear time have distinct reports.
  A Continue can affect the Track's assessment.
- Claim IDs: HR-002–HR-009.

### Constraint Genes

- `CON-282` holds mandatory route stages behind completed authored gates.
  The generator must be restored before the downstream production route.
- `CON-402` withholds arena departures until the required finite groups
  are defeated. Movement between encounters remains possible once released.
- Claim IDs: HR-004, HR-006.

### Information Genes

- `INF-142` uses attack motion and timing prompts. A boss wind-up guides
  evasion. The convergence at a Beat Hit guides the offensive press.
- `INF-334` discloses the engaged tough enemy's remaining ability to
  withstand interruption through its separate Stun Gauge.
- `INF-501` gives a shared rhythm reference through musical and synchronized
  visual pulses, including an optional beat guide. This reference remains
  useful across different chosen actions, without any required note chart.
- Claim IDs: HR-003, HR-005, HR-006, HR-008.

### Objective Genes

- `OBJ-029` clears the required finite enemy group in each normal Chorus.
- `OBJ-080` defeats the mandatory QA-1MIL after completing its access route
  and crosses the Track boundary to the Hideout.
- Success and evaluation are separate. Ordinary clearance advances the
  Normal story, while the interface exposes differences in performance.
- Claim IDs: HR-004, HR-006, HR-007.

### Time Genes

- `TIM-003` allows movement and combat while the threats, attacks, moving
  platforms and beat progress in real time. Longer attack animations and a
  deliberate rest change the timing of the next choice.
- Claim IDs: HR-002, HR-003, HR-008.

## First Track route checkpoints

1. Reach the first group of melee robots and clear it. Complete the separate
   light and heavy instruction before the second fight.
2. Clear the second fight and take the diversion after the door closes.
   The third fight precedes reaching Peppermint and 808. Complete the
   Beat Hit instruction and take the launch lift into the fourth fight.
3. Leave the rooftop, strike the bridge control and descend through the
   side-view crossing. Reach the battery that unlocks Power Chord, then
   clear the ranged robots in the fifth fight.
4. Traverse the press and conveyor route. When it loses power, address the
   generator, read the rhythm prompts and restore the line. Defeat the
   tough robot in the sixth fight. Optional practice entrances can be passed.
5. Cross the moving platforms to the mixed seventh group and clear it to
   open access to QA. The eighth fight is QA-1MIL. Resolve the boss,
   accept the Track results and reach the Hideout.

The encounters, traversals and teaching stages are sequentially authorised.
The exact Normal enemy counts after the first Chorus are outside the
documentary claims. HR-004–HR-007.

## Reproducible transitions

| Before | Action | Result | What it establishes | Claim |
|---|---|---|---|---|
| First free movement after the operation | Navigate to the campus fight | A finite group of three basic robots seals the first arena, then clearance advances to attack teaching | Traversal leads to a discrete scored encounter and a teaching stage | HR-004 |
| An ordinary reachable target is idle between beats | Press a light or heavy attack off beat | A valid ordinary attack can still land on a beat, without the same reward as a correctly timed press | Impact alignment and input accuracy differ | HR-002 |
| The taught string has reached a Beat Hit prompt | Press when the rings meet, then compare with omitting the press | The correct input produces the added finisher. Omitting it does not undo the ordinary strikes | Optional follow-up has its own commitment | HR-003 |
| Chai meets 808 after the early campus fights | Complete the prompted Beat Hit instruction | The learned finish becomes available for later ordinary fights | Teaching changes what can be executed | HR-003, HR-004 |
| Power Chord and Reverb have been unlocked in the battery room | Land a Beat Hit, collect a generated battery and later spend available Reverb | The pickup credits the reserve before a separate special-attack spend | Battery appearance differs from credit and expenditure | HR-005 |
| Production platforms lose power after Chorus 5 | Interact with the generator and complete the prompted rhythm input | The line restarts and traversal can continue | A timed action can gate traversal without hostile damage | HR-004 |
| BA-B00 or its later group resists interruption | Attack until the separate Stun Gauge gives way | The target can be interrupted and pressured during the opening | Tough-enemy stability and health are distinct | HR-005 |
| QA-1MIL winds up a downward fist strike | Evade the strike, approach the hand while it is stuck, then attack | Damage is possible before the hand withdraws | Opponent action itself creates the opening | HR-006 |
| An embedded hand has taken qualifying damage | Complete that hand’s contextual timing sequence, then do the same for the other hand | Each successful counter breaks its side of the faceplate. Both successes fully expose the head. A missed sequence leaves the hand route available | Two optional counters expand the target set for later attacks | HR-006 |
| A supported attack has just scored | Repeat it consecutively and compare with selecting an equally safe different attack | The repeated move can receive reduced credit | Style decisions can affect score independently of damage or elapsed time | HR-007 |
| The eighth Chorus ends with the boss defeated | Accept the results and proceed | The first Track settles and the story reaches the Hideout | There is a mandatory clear and a separate aggregate assessment | HR-007 |

## Strategic and experiential structure

A lighter attack leaves a shorter interval before the next input. A heavy
attack, deliberately rested string or uninterrupted finisher trades time
against damage and opportunity. The pulse gives a common reference, while
enemy cues determine when holding that offensive sequence would be unsafe.
At the boss, avoiding the attack positions Chai for a counterattack against
the exposed hand. Reverb introduces a second trade-off between keeping an
earned reserve and spending it on an opening. Normal continues can rescue
progress at the cost of assessment. HR-002–HR-009.

## Replay and variation

The ordinary route, teaching order and fight roles are authored. Variation
comes from timing, target order, attack strings, optional Beat Hits, use of
Reverb and recovery. A second result can be better in time and worse in
timing. No exact rank formula, enemy randomisation or post-clear record
merging is inferred. HR-003, HR-004, HR-007, HR-009.

## Adjacent systems and history

`GAME-0372` Guitar Hero III evaluates matching inputs against the authored
note chart. In Hi-Fi RUSH a missed beat need not void an ordinary attack.
The player selects attacks and targets in a live arena while the soundtrack
supplies a shared clock. These are
boundary comparisons. No design lineage is claimed. HR-002, HR-003, HR-008.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-223, ACT-341, ACT-356, ACT-709 | Move, strike, dodge or jump, use fixture, add a Beat Hit |
| System Behaviour | SYS-215, SYS-369, SYS-409, SYS-578, SYS-736, SYS-799, SYS-822, SYS-1386, SYS-1459, SYS-1460, SYS-1461, SYS-1462, SYS-1463, SYS-1464, SYS-1465, SYS-1466 | Hit alignment, accuracy, typed strings and rests, scored fights, boss openings and generator |
| Constraint | CON-282, CON-402 | Route order and required hostile clearance |
| Information | INF-142, INF-334, INF-501 | Attack prompts, enemy stability and shared beat |
| Objective | OBJ-029, OBJ-080 | Clear encounter groups, defeat QA-1MIL and enter the Hideout |
| Time | TIM-003 | Live rhythm, movement and adversarial progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `515` (`GAME-0001`–`GAME-0515`).
- Exact genome matches: none.
- Tied near matches: `GAME-0303` — Sifu (`11 / 43 = 0.255814`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0303` Sifu | ACT-008, ACT-161, ACT-223, SYS-215, SYS-409, SYS-578, CON-282, INF-142, INF-334, OBJ-080, TIM-003 | Both opening routes use live attacks, signalled responses and target stability before a required boss. Sifu trades Structure, Focus, age and same-place revival. Hi-Fi RUSH aligns normal impacts to music, rewards accurate inputs and grades each Chorus. The stuck hand opens through the boss's miss. | Near, `0.255814` |

## Taxonomy impact

- [TAXONOMY_CHANGE_263](../../../research/taxonomy-changes/TAXONOMY_CHANGE_263.md)
  records ten additions and twenty unchanged transfers.

## Negative results

- A rhythm-aligned impact does not establish that its input was timed.
- The practical sources agree on the attackable hands and optional head
  exposure. The detailed route and achievement accounts specify both
  hand counters for full exposure. The launch summary compresses this
  into one event. Exact health thresholds and timed caps on Normal are open.
- The ordinary Normal release evidence does not establish the separate
  low-rank failure condition from Rhythm Master routes.

## Delta summary

## New facts

- [Observation | Corroborated | High] The ordinary impact is aligned to the
  beat independently of the timing bonus. HR-002.
- [Observation | Corroborated | High] An accepted command rhythm can finish
  a chain, reactivate a fixture or expose a different target. Those
  outcomes have different eligibility predicates. HR-003, HR-004, HR-006.

## New genes

- ACT-709, SYS-1459, SYS-1460, SYS-1461, SYS-1462, SYS-1463, SYS-1464, SYS-1465, SYS-1466 and INF-501.

## New combinations

- None. All verified combinations were scanned as proper subsets.

## Taxonomy changes

- Ten added stable definitions. No prior definition, game signature or
  published mapping changes.

## New questions

- How do grade thresholds and Continue effects vary by Normal release
  patch and by individual Chorus? This requires a controller capture with
  known build and settings.

## Next recommended game

- `GAME-0517` Homeworld, original released Windows base game from 1999.

## Why this game

- [Hypothesis | Limited | Medium] Free positioning inside a shared musical
  clock can separate attack execution, input accuracy and outcome evaluation
  in a way that a fixed rhythm chart cannot. Test the separation again in
  another action-led game with documented off-beat inputs.
