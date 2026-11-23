---
game_id: GAME-0542
slug: excite-truck
game_title: Excite Truck
analysis_status: reviewed
reviewed: 2026-11-18
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-308
    - ACT-379
    - ACT-739
    - ACT-740
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-1564
    - SYS-1565
    - SYS-1566
    - SYS-1567
    - SYS-1568
    - SYS-1569
    - SYS-1570
  constraint:
    - CON-068
  information:
    - INF-205
    - INF-206
    - INF-208
    - INF-524
  objective:
    - OBJ-300
  time:
    - TIM-003
---

# Game: Excite Truck

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The controller, course, two laps, star schedule and three-minute allowance
are parameters of this original Wii packet.

## Analysis scope

- Version / ruleset: original English North American Wii retail game,
  November 2006, single-player Excite Race on ordinary Excite difficulty.
  Nintendo's original English booklet establishes the control contract.
  The exact disc revision and engine coefficients were not measured.
- Entry: use a fresh profile after the mandatory Basics tutorial. Select
  Bronze Cup, Mexico: Greenhorn Gulch, and the initial Boulder pickup
  in its default red colour. Start at the displayed event terms before
  the countdown. No later truck or custom music changes the packet.
- Primary decision loop: steer by tilting the sideways Wii Remote,
  manage throttle, brake and heat-limited turbo, choose a road or tree
  line and adjust pitch in flight. Time takeoff boost, align the
  landing, exploit eligible terrain triggers and collect stunt stars
  while five CPU trucks and the race clock advance.
- Positive exit: complete two laps within the displayed three-minute
  allowance, settle the place bonus, and reach at least 70 stars for
  B. A 90-star total is S. Stop at the result before another race.
  A lower score or expired attempt is a failed branch.
- Included: live ground and aerial handling, turbo and thermal lockout,
  collision and prompted recovery, the authored forks and triggers,
  POW, the available stunt classes, lap finish, score, grade and HUD.
- Excluded: player-profile creation, completing tutorials, other trucks,
  later cups and vehicle unlocks, whole-cup progression, Super Excite,
  Mirror, Challenge, Versus, exact save behaviour, water cooling on
  other courses, launch-timing tricks and undocumented physics constants.
- Potential scoped modules: a complete cup award, one timed Gate Challenge,
  or the effect of water on thermal control in a different course.
- Direct-play status: no disc, console, executable or save was used.
  The original booklet's diagrams and screenshots were inspected
  alongside two independent written course routes and release-era
  play accounts. No audio or video was played. A native success/failure
  trace and exact sensor calibration were not reproduced.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ET-001 | The ordinary first Mexico event is two laps with a three-minute limit, B at 70 stars and S at 90. Excite Race has five CPU rivals. | Observation | Corroborated | High | P1, S1, S2 |
| ET-002 | Hold the Remote sideways. Tilt left/right to steer. 2 accelerates, 1 brakes or reverses, and the Control Pad requests turbo. Pitch and lateral input remain useful in flight. | Confirmed | Corroborated | High | P1, S1, S3 |
| ET-003 | Ground turbo builds heat. Release and airborne travel cool the engine. Overheating temporarily slows the truck and disables turbo until it cools, without ending the race. | Observation | Corroborated | High | P1, S1, S4 |
| ET-004 | A turbo press around takeoff increases flight. Bringing all four wheels down together gives a landing boost. Neither assistance directly adds stars. A braking/boost/tilt input can initiate aerial rotation. | Observation | Corroborated | High | P1, S1, S3, S5 |
| ET-005 | Contact with a ! trigger can change the course and reveal rings. Mexico has a ring trigger, a hill-raising trigger and a later falling-rock effect. A side path offers POW and trees. | Observation | Corroborated | High | P1, S1, S2 |
| ET-006 | Recognised driving feats award stars. The declared classes include air, drift, tree run, air spin, truck throw, jump combo, truck smash, nice crash and rings. POW temporarily raises speed and permits breaking through trees. | Observation | Corroborated | High | P1, S1, S2, S3 |
| ET-007 | A crash interrupts ordinary handling. Repeated 2 inputs return the truck to the race with a boost while the race remains active. | Confirmed | Corroborated | High | P1, S3 |
| ET-008 | Finish position adds a separate bonus to earned stunt stars before course grading. First place adds 50, second 25, then 15, 10, 5 and 0. Passing depends on the total. | Confirmed | Corroborated | High | P1, S3, S4, S5 |
| ET-009 | Pre-race terms state the lap, time and star requirement. The HUD separates position, current lap, clock, track map, earned and required stars, live stunt credit and temperature. | Confirmed | Direct | High | P1 |
| ET-010 | The two Mexico guides disagree on whether the final falling-rock effect can actually hit a rival. The trigger and visual obstruction agree; collision authority for these rocks remains unverified. | Observation | Conflicting | Medium | S1, S2 |

## Basic data

- Monster Games and Nintendo, original Wii retail game. North American
  release 19 November 2006. The regional UK release followed in February
  2007 and is not the selected disc.
- Families: physics and object manipulation, and real-time system pressure.
- Sources accessed 2026-11-18:
  - **P1** — [Nintendo-hosted original English booklet](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_Excite_Truck?_a=BATCtdAA0),
    printed pp. 4–9. The operation diagram, starting-vehicle page,
    stunt/boost spread and live HUD were visually inspected.
  - **P2** — [Nintendo's product page](https://www.nintendo.com/en-gb/Games/Wii/Excite-Truck-281122.html),
    for product identity, tilt steering and changing course geometry.
    Its February date belongs to the UK release.
  - **S1** — [Deathborn_668's Wii guide](https://gamefaqs.gamespot.com/wii/933000-excite-truck/faqs/49000),
    ordinary Excite Mexico route, introductory actions and aerial input.
    Its tutorial prose accidentally calls 2 the brake; P1's diagram and
    other sources establish 1 as brake and 2 as throttle.
  - **S2** — [SPV999's independent Wii route](https://www.supercheats.com/wii/walkthroughs/excitetruck-walkthrough01.txt),
    ordinary Mexico thresholds, three trigger effects and the tree path.
    Its later Super Excite entries have different thresholds.
  - **S3** — [Worthplaying's December 2006 play review](https://worthplaying.com/article/2006/12/18/reviews/38517-wii-review-excite-truck/),
    live handling, landing, recovery and stars. Its description of a
    draining boost bar is superseded by the booklet and thermal accounts.
  - **S4** — [GameSpot's November 2006 play review](https://www.gamespot.com/reviews/excite-truck-review/1900-6161717/),
    North American date, non-destructive overheating, airborne cooling
    and the distinction between stunt total and finish position.
  - **S5** — [Kikizo's original Wii play account](https://games.kikizo.com/reviews/wii/excite_truck_p1.asp),
    controller handling, five competitors and score-first passing.
- Claim IDs: ET-001–ET-010.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-290` for direct steering, throttle, brake and reverse.
  The physical sensor is the input device parameter.
- Reuse `ACT-308` for deliberate aerial pitch and rotation. The player
  can extend the flight or descend earlier toward a safe landing.
- Reuse `ACT-379` for directing contact into a competing truck.
- Add `ACT-739` for requesting sustained heat-limited turbo with a
  temporary non-destructive overheat response.
- Add `ACT-740` for repeated input while a crash has suspended
  ordinary steering. This input does not restart the whole race.
- Claim IDs: ET-002–ET-004, ET-006, ET-007.

### System Behaviour Genes

- Reuse `SYS-320` for occupied vehicle motion and collision,
  `SYS-515` for the five-CPU field and `SYS-516` for the
  two-lap finish and classified position.
- Add `SYS-1564`: heat accumulates during ordinary ground turbo,
  cooling makes it usable again, and overheating temporarily restricts
  speed and turbo. `SYS-1421` instead includes destructive overheating
  and cannot transfer unchanged.
- Add `SYS-1565`: a contacted trigger changes its authored geometry
  or linked fixtures. An opponent occupying rising terrain can be
  thrown by that change. The later rock effect remains visual evidence
  without an assumed damaging collision.
- Add `SYS-1566`: accumulate stars for the nine declared feat classes.
  A Tree Run measures close passage, while a Truck Smash depends on
  contact. A Nice Crash can add a star while wasting racing time.
- Add `SYS-1567`: POW pickup immediately changes speed and permits
  passing through ordinary tree obstacles for a limited interval.
  Exact duration and the reported Tree Run suppression after touching
  a tree were not independently verified.
- Add `SYS-1568`: qualified takeoff input and an aligned four-wheel
  landing supply movement assistance. Additional flight can create
  scoring opportunities, while the assistance itself earns no stars.
- Add `SYS-1569`: repeated crash input restores local driving with
  boost. No finite retry debit or reset of the whole race is asserted.
- Add `SYS-1570`: after a valid finish, add the place bonus and
  classify the combined total against the local B/S thresholds.
- Claim IDs: ET-001–ET-008, ET-010.

### Constraint Genes

- Reuse `CON-068`: the finite event deadline bounds the attempt.
  Reaching the displayed star requirement before finishing does
  not itself complete the race.
- Claim IDs: ET-001, ET-008, ET-009.

### Information Genes

- Reuse `INF-206` for the event card, `INF-205` for race progress
  and local rivals, and `INF-208` for the classified result.
- Add `INF-524` for earned stars, the passing target, current
  feat credit and the live heat display.
- Claim IDs: ET-008, ET-009.

### Objective Genes

- Add `OBJ-300`: finish the bounded laps before expiry and
  settle a total at or above the passing threshold. First place
  without sufficient total stars is not enough.
- Claim IDs: ET-001, ET-008.

### Time Genes

- Reuse `TIM-003`: the clock, trucks, flight and contact continue
  while steering, boost and recovery inputs are accepted. The
  ordinary pause menu is available outside active progression.
- Claim IDs: ET-002–ET-009.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Bronze Mexico is selected with Boulder | Accept the event terms | Begin two laps against five trucks under the three-minute allowance | Later difficulty thresholds do not apply | ET-001 |
| The truck approaches a jump with usable turbo | Request turbo at takeoff, then pitch backward or forward | The takeoff burst changes flight and pitch changes hang time or descent | An aerial line competes with the approach to the next bend | ET-002–ET-004 |
| Engine heat is below the boundary | Continue turbo too long, then release and cool | Overheat temporarily removes turbo and speed before normal availability returns | Heat does not destroy the vehicle or consume a nitro stock | ET-003 |
| The ring trigger has not yet been hit | Drive through it | A five-ring route becomes available above the following hill | Trigger response changes opportunities during the same lap | ET-005 |
| A rising hill is about to be triggered and another truck occupies it | Contact the trigger | The surface rises and can throw the other truck | Geometry can affect more than the collecting vehicle | ET-005, ET-006 |
| The shortcut offers POW near trees | Collect it and drive along the tree line | Temporary speed and obstacle-breaking apply | Close passage scoring and destroying an obstacle are different conditions | ET-005, ET-006 |
| The truck is airborne before a landing | Align for all four tyres to touch together | Receive Nice Landing boost without direct star credit | Movement assistance and stunt scoring have different triggers | ET-004, ET-006 |
| A collision has suspended ordinary movement | Repeatedly press 2 | Return locally with a boost | A crash recovery is inside the same attempt | ET-007 |
| Two laps finish within time with a given stunt tally | Add the position bonus and inspect the result | The combined total determines B or S against the selected track thresholds | Position and stunt contribution settle together | ET-001, ET-008 |

These transitions reconstruct documented rules rather than a newly
executed disc trace.

## Strategic and experiential structure

A longer flight can earn stars and reduce heat while increasing the risk
of overshooting the next turn. Pitching forward can give up airtime to
recover a usable road line. The tree fork offers scoring proximity and
POW but also exposure to obstacles. Deliberate contact can create a
Truck Smash, while triggering rising ground with a rival above it creates
a Truck Throw through a different cause.

A first-place bonus contributes 50 toward the 70-star minimum. Thus a
fast, low-stunt line and a slower, high-stunt line can settle differently.
The exact arithmetic thresholds are documented. No guaranteed route or
claim of optimal lap time is inferred.

## Replay and variation

The course, forks and named trigger responses are authored. The player's
line, flight, stunt extent, crashes, recovery speed and rival order can
vary. Exact opponent catch-up logic, sensor dead zone, respawn position,
repeat-trigger persistence between laps and simultaneous finish/expiry
priority were not measured. Native boundary tests could refine those
claims without treating them as established rules now.

## Adjacent systems and history

Original MotorStorm uses held boost with a destructive heat boundary.
Excite Truck temporarily removes turbo at overheat and couples airborne
cooling with scoring opportunities. SSX Tricky uses landed tricks to feed
adrenaline in its downhill race. Here live feats feed a race score and
finish place supplies a separate terminal bonus.

Aerial ring passages are optional score opportunities. They do not
replace the route's lap validation with a requirement to pass every ring.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-290`, `ACT-308`, `ACT-379`, `ACT-739`, `ACT-740` | Direct driving, aerial orientation, contact, thermal boost and crash input |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-1564`, `SYS-1565`, `SYS-1566`, `SYS-1567`, `SYS-1568`, `SYS-1569`, `SYS-1570` | Motion, rivals, laps, heat, triggers, feats, power, assisted takeoff/landing, recovery and grade |
| Constraint | `CON-068` | Finite race deadline |
| Information | `INF-205`, `INF-206`, `INF-208`, `INF-524` | Event terms, race view, result, stars and heat |
| Objective | `OBJ-300` | Finished laps with the passing star total before expiry |
| Time | `TIM-003` | Live race progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `541` (`GAME-0001`–`GAME-0541`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`8 / 28 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0217` — Need for Speed Underground | `ACT-290`, `SYS-320`, `SYS-515`, `SYS-516`, `INF-205`, `INF-206`, `INF-208`, `TIM-003` | Both have a directly driven lap race, live CPU rivals and event/results information. Underground spends finite nitrous and requires first place in its opening event. Excite Truck uses thermal turbo, active terrain triggers and a combined star passing threshold. | Near, `0.285714` |

### Preserved research notes

- New genes: `ACT-739`, `ACT-740`, `SYS-1564`–`SYS-1570`,
  `INF-524`, `OBJ-300`.
- Classification result: New gene.
- Evidence and reasoning: the packet adds trigger-driven course changes
  and score-first race settlement with a non-destructive heat loop.

## Taxonomy impact

- Registry changes: eleven new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_289](../../../research/taxonomy-changes/TAXONOMY_CHANGE_289.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] Greenhorn Gulch combines two laps
  and a deadline with a total-star passing predicate. ET-001, ET-008.

## New genes

- [Observation | Corroborated | High] Eleven additions separate heat,
  course triggers, live stars, temporary power and graded settlement.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_289`.

## New questions

- Does the final falling-rock effect in the original Mexico race
  have a collision response, or only visual obstruction?

## Next recommended game

- [Hypothesis | Limited | Medium] Xbox Series X|S Keeper in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: change from timed driving to environmental interaction.
- Expected information gain: light-driven changes and a bounded traversal.
- Backlog impact: advance to `GAME-0543`.

## Why this game

- [Hypothesis | Limited | Medium] A light-driven environment should
  expose decisions distinct from managing racing line, heat and stars.
