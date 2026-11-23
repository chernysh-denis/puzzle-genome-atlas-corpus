---
game_id: GAME-0579
slug: is-this-seat-taken
game_title: Is This Seat Taken?
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-784
  system:
    - SYS-135
    - SYS-1699
    - SYS-1700
    - SYS-1701
  constraint:
    - CON-001
    - CON-840
  information:
    - INF-001
    - INF-030
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Is This Seat Taken?

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Place each waiting passenger, then check who changed their mind and why.
Confirming enough places to depart can still leave the bus short of Perfect.

## Analysis scope

- Version / ruleset: full paid Android base game released on 7 August 2025,
  Google Play package com.PotiPoti.IsThisSeatTaken, English interface.
  Barcelona level 4, the first city bus outing, ordinary untimed puzzle.
  Exact installed package version is unverified. Do not infer a later
  cloud-save or achievement implementation from 2025 observations.
- Structured analysis target: PLAT-ANDROID, see
  [platform coverage](../../platforms/games.json).
- Entry: open Barcelona's bus after the preceding cinema level. Start with
  the first controllable bus state and the first waiting group. Use the
  original fixed interior, existing riders and passenger preferences.
- Primary decision loop: inspect a passenger's requirements and the current
  seat or standing layout, move one passenger, and check changes in both
  that rider and neighbours. Reassign as needed before Confirm. Resolve
  departures and arrivals and apply the same loop at the remaining stops.
- Positive exit: confirm the fourth allocation and reach the bus result.
  A complete allocation moves the level forward; satisfying every counted
  rider across the four stops yields Perfect. Empty positions can remain.
  Later scenarios and the city bonus unlock condition are outside the unit.
- Negative exit: an unplaced waiting passenger keeps the wave incomplete.
  Conflicting preferences can reduce approval without imposing a timer,
  destroying the board or making a legal full arrangement impossible to
  confirm. An imperfect committed stop matters for the final grade.
- Included: fixed seat and standing positions, assignment and relocation,
  readable passenger attributes and local feedback, paired and positional
  preferences, nearby music or smell, four authored waiting groups, retained occupant positions, confirmation and cumulative approval.
- Excluded: other cities and vehicles, dress and food systems, air
  conditioning, prop-only interactions, optional city bonus scenes,
  prerelease demo, exact release-binary equivalence, platform achievements
  and save synchronisation. No native portrait layout is assumed.
- Potential scoped modules: serving shared food at the wedding dinner or
  configuring an environmental device in a later named scenario.
- Direct-play status: not conducted. Developer release material and
  an Android launch review establish the full title and touch placement.
  Static Android-labelled frames and a separately mobile-labelled perfect
  run corroborate the particular bus and its results. No touch device,
  motion playback, audio playback or package executable was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ST-001 | The full Android game launched on 7 August 2025. The official package presents preferences as an untimed seating problem. | Observation | Corroborated | High | P1, P2, R1 |
| ST-002 | Touch-and-drag relocates one passenger to an individually addressed seat or standing place. The player can inspect the current roster and revise the placement of existing riders before departure. | Observation | Corroborated | High | P2, R1, R2, W1, W2 |
| ST-003 | Local place tags, companion choice or nearness, and disruptive traits can interact. The first wave includes a child seeking another child; later waves include a rider who wants a named companion and has a disruptive trait. | Observation | Corroborated | High | P1, P2, R2, R3, W1 |
| ST-004 | Position changes can resolve or cause complaints for several riders. A sleeper or noise-averse passenger can object to a loud passenger's nearby placement. Complaints and satisfaction feedback expose consequences before confirmation. | Observation | Corroborated | High | P2, R2, R3, W1, W2 |
| ST-005 | A seat or standing place is needed for each waiting passenger. A complete but imperfect assignment still offers Confirm and permits progression. | Observation | Corroborated | High | P3, R2, R4, W2 |
| ST-006 | Confirm advances to the next stop and settles the old allocation. Departures free places, some seated or standing riders remain where placed, and a new roster awaits. Through riders can be moved again. | Observation | Corroborated | High | R2, R3, R5, W1, W2 |
| ST-007 | Approval is banked across the four confirmations. The walkthrough records 40 available thumbs, and a mobile example finishes with the gold Perfect result. The ordinary completed result and perfect grade are separate outcomes. | Observation | Corroborated | Medium | P3, R3, R5, W1, W2 |

## Basic data

- Poti Poti Studio, with Wholesome Games Presents. FAM-001 for a finite
  assignment combining place constraints, required companions and
  aversions to neighbours.
- P1: [Poti Poti Studio press kit](https://www.potipoti.studio/itst/presskit).
  Identifies the release date, store, developer and scenarios.
- P2: [Official Android listing](https://play.google.com/store/apps/details?id=com.PotiPoti.IsThisSeatTaken).
  Establishes the package, no-timer design and sleepy passenger versus
  nearby loud music. Its later cloud-save update is excluded.
- P3: [Developer interview with Aftermath](https://aftermath.site/is-this-seat-taken-impressions-indie-direct/).
  Separates putting everyone in a place from meeting their personal
  requirements for a perfect outcome. The demo referenced in the interview
  is not this unit's release target.
- R1: [Pocket Tactics Android hands-on review](https://www.pockettactics.com/is-this-seat-taken/mobile-review).
  Corroborates selection and repositioning by touch on the native platform.
- R2: [GamesRadar release review](https://www.gamesradar.com/games/puzzle/is-this-seat-taken-review/).
  Describes stops, locally projected traits, visual clues and seating
  the entire roster. Its later objects and environment controls are excluded.
- R3: [Full-release community solution](https://steamcommunity.com/sharedfiles/filedetails/?id=3546751669)
  and [Bonus Action's four-stop solution](https://bonus-action.com/guides/is-this-seat-taken-walkthrough-all-puzzles-secret-levels/).
  Two written solutions locate standing positions, retain several riders
  across stops and separate sleepers from unwanted influences. They do
  not establish a unique placement or exact neighbour radius.
- R4: [Play Critically's launch-month play account](https://playcritically.com/2025/08/18/is-this-seat-taken-review/).
  Reports that placing everyone and confirming can pass despite unsolved
  preferences. Paired with P3 and the visible Confirm state in W2.
- R5: [Neoseeker, Barcelona level 4](https://www.neoseeker.com/is-this-seat-taken/walkthrough/Barcelona_-_Level_4)
  lists a persistent occupant roster and a 40-thumb ceiling. Exact per-stop
  counter arithmetic was not independently extracted from the game binary.
- W1: [Dmun Games' Android-labelled full-release recording](https://www.youtube.com/watch?v=jl0PJXv64qE&t=400s).
  Static frames from about 6:40 to 9:20 show the fixed first bus, touching
  a passenger to inspect preferences, approval during departure, retained
  riders, later boards and complaints. Source says Android; exact build and
  unsampled intermediate gestures are unverified.
- W2: [Nevaran's mobile Barcelona recording](https://www.youtube.com/watch?v=U9z0M-25ufQ&t=640s).
  Static frames from about 10:40 to 14:50 show a four-stop sequence on
  the same bus. Around 11:40 the Confirm control coexists with
  unresolved complaints. The final frame shows Perfect. The recording
  title lists both mobile platforms and does not identify the device.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-784 is moving one identifiable rider to a selected seat or marked
  standing position, including editing a rider already in the bus.
  Their intrinsic requirements and traits travel with them (ST-002, ST-003).

### System Behaviour Genes

- SYS-135 reevaluates the currently revealed requirements as edits change
  the shared seating answer. A previously good placement can create a
  complaint after a new neighbour is placed. At settlement a stop is
  scored, then its active answer is replaced by the next roster
  (ST-003–ST-006).
- SYS-1699 links a disruptive influence to its current rider and
  position. The nearby receiver's aversion and not the emitter alone
  determines whether the effect lowers satisfaction (ST-003, ST-004).
- SYS-1700 carries through riders at their current positions, removes
  departing occupants, and introduces the new waiting roster
  (ST-006).
- SYS-1701 banks approval from a committed layout across the route.
  The result can recognise full satisfaction without using it as a
  gate to all further progression (ST-005–ST-007).

### Constraint Genes

- CON-001 covers finite seating and marked standing places with separate
  addressable occupancy. An empty seat is allowed, and the player does not
  lay out new seats in this packet (ST-002, ST-005).
- CON-840 closes the current assignment for departure only when all
  required waiting passengers occupy a usable place. Even filled places
  may create unmet soft requirements (ST-005).

### Information Genes

- INF-001 admits the complete current placement surface and inspectable
  requirements of the current roster. It does not reveal every later
  arrival in advance (ST-002, ST-003, ST-006).
- INF-030 covers current local satisfaction or the reason for objection
  while the seating configuration remains editable. This feedback does
  not guarantee the final perfect result (ST-004).

### Objective Genes

- OBJ-006 is the declared perfect assignment target at each stop. For the
  top grade, all counted preferences must be satisfied together when that
  stop is confirmed. Ordinary completion needs only full legal occupancy
  of the roster and all four confirmations (ST-005, ST-007).

### Time Genes

- TIM-002 covers self-paced edits and player-committed departure.
  Ambient animation and waiting do not force the next roster or reduce
  approval (ST-001, ST-005, ST-006).

## Reproducible transitions

| Before | Action or event | Result to check | Claims |
| --- | --- | --- | --- |
| First stop, a child needs a child neighbour | Inspect their card and place the two children in a shared pair | The appropriate relation becomes satisfied; the other pair can still need a different arrangement | ST-002, ST-003 |
| A seated or standing passenger makes noise | Move a susceptible sleeper into then beyond the affected neighbourhood | A nearby placement can draw a complaint; moving apart can remove it | ST-003, ST-004 |
| An existing passenger is in a usable position but a better arrangement is needed | Move that same rider to a free suitable position | Identity and requirements persist; the former position becomes free | ST-002, ST-004 |
| A waiting passenger still has no place | Leave otherwise usable positions unassigned | The allocation cannot be confirmed | ST-005 |
| Everyone is placed but a passenger still complains | Confirm | The bus can depart. The grade can lose approval for that stop | ST-005, ST-007 |
| First or later accepted allocation | Advance to the next stop | Some current riders remain in their assigned places, others leave and fresh passengers wait | ST-006 |
| All required passengers approve at each of the four stops | Confirm the last arrangement | The gold Perfect result recognises the accumulated approvals | ST-007 |

## Strategic and experiential structure

A seat can be legal yet a poor fit. Try satisfying specific pairs first,
leave room to separate disruptive riders from those bothered by them, and
recheck prior placements after new passengers board. Reassigning a
retained rider can satisfy a new relationship without throwing away the
entire seating plan. Confirm closes the current scoring opportunity,
so a later better arrangement does not replace the earlier stop's result.

## Replay and variation

The stop sequence and geometry are authored. A different seating order, use
of a standing place or early confirmation can yield another result without
changing the goal, scenery, roster script or input timing. The written
solutions give reproducible examples rather than a proof of uniqueness.

## Adjacent systems and history

The developer's original concept began with a bus seating prototype.
The release generalises placements to social venues. An authored change
of vehicle, menu achievements and the later addition of cloud saving do
not become bus-timing or roster genes.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-784 | one identifiable passenger and destination |
| System Behaviour | SYS-135, SYS-1699, SYS-1700, SYS-1701 | local revalidation, moving influence, roster transition and banked approval |
| Constraint | CON-001, CON-840 | fixed onboard positions and full-roster confirmation |
| Information | INF-001, INF-030 | visible positions, inspectable clues and local feedback |
| Objective | OBJ-006 | perfect assignment at each settled stop |
| Time | TIM-002 | untimed draft with voluntary departure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `578` (`GAME-0001`–`GAME-0578`).
- Exact genome matches: none.
- Tied near matches: `GAME-0062` — Hexologic (`5 / 14 = 0.357143`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0062` *Hexologic* | CON-001, INF-001, INF-030, OBJ-006 and TIM-002. Both offer fixed positions, inspectable clues, local feedback, a fully satisfying target and self-paced revision. | Hexologic sets pips in intersecting lines and checks exact totals and full assignments. The bus relocates independent passengers with changing local effects, permits departure with unmet soft preferences, and carries selected occupants and credited approval through four stops. | `5 / 14 = 0.357143`; closest earlier match. |

### Preserved research notes

- New genes: ACT-784, CON-840 and SYS-1699–SYS-1701.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_325](../../../research/taxonomy-changes/TAXONOMY_CHANGE_325.md)
  separates individual placement, departure eligibility, a local disruptive
  footprint, retained riders and accumulated approval. Earlier genomes and
  definitions stay intact.

## Negative results

- ACT-007 places a symbol from a legal domain, not one retained passenger
  record with a movable disruptive influence. ACT-574 seats a complete
  waiting party at a table and does not admit repeated solo reseating.
- Do not import SYS-136. This bus wave can advance without validating every
  soft requirement, whereas that gene requires an all-valid answer to
  reveal the next rule.
- A partner, child, window location, loud music or smell configures a
  predicate or footprint. No genre label, number of stops, shape or named
  passenger becomes an independent gene.
- No exact distance for cross-aisle chatter or mixed noisy/smelly zones,
  swap ordering, saved-state restoration or preference uniqueness is asserted.

## Delta summary

## New facts

- [Observation | Corroborated | High] A place for everyone enables
  departure. The dynamic local preference checks and score give a
  second reason to rearrange a legally full roster.

## New genes

- [Observation | Corroborated | Medium] Five boundaries, including
  retained placement between stops and per-stop approval accounting.

## New combinations

- [Observation | Corroborated | High] No new verified combination proposed.
  Existing supported subsets are owned by the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_325.

## New questions

- A native probe could check exact footprints on each standing spot,
  interactions across the central aisle, and small counter changes after
  repeating the same stop with one unmet preference.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0580, Viewtiful Joe on GameCube.
- Optimisation criterion: move from wholly self-paced evaluation to
  author-controlled alterations of a live action stage.

## Why this game

- [Hypothesis | Limited | Medium] A single complete bus outing presents
  retained place assignments and two independent measures of success,
  with concrete interactions among different kinds of preferences.
