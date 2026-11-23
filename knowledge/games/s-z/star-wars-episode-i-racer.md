---
game_id: GAME-0632
slug: star-wars-episode-i-racer
game_title: "Star Wars Episode I: Racer"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-840
    - ACT-841
  system:
    - SYS-320
    - SYS-516
    - SYS-1421
  constraint: []
  information:
    - INF-205
    - INF-208
    - INF-586
  objective:
    - OBJ-150
  time:
    - TIM-003
---

# Game: Star Wars Episode I: Racer

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original 1999 European PAL Nintendo 64 commercial
  cartridge, NUS-NEPP-EUR. Use the English menus, regular solo Tournament
  and the first Amateur PodRacing Circuit track. The filmed run identifies
  a PAL copy and uses English text. It does not identify the physical
  pressing, ROM checksum or capture hardware.
- Primary decision loop: steer and build speed on the current racing line,
  use the thrust cue to arm and engage boost, respond to heat or damage,
  and finish the three laps inside the qualifying places.
- Entry: select a fresh tournament slot, Anakin Skywalker and The Boonta
  Training Course. The demonstrated track briefing offers a Skilled
  payout and discloses fourth place or better for progression. Start the
  selected race from the main menu.
- Exit: the actual first-place classification records 3:04.298 and
  1,200 Truguts. The tournament menu exposes Mon Gazza Speedway in
  slot two and the recording starts it. The scope stops at that entry.
- Included: forward thrust and booster arming, speed with heat warning,
  speed-priced repair during a live lap, lap timing and rival position,
  the disclosed qualification threshold, recorded reward and actual
  successor availability.
- Excluded: exact heat or damage units, a destructive boost outcome
  in the observed route, frame rate comparisons, skipped lap checks,
  prize modes other than the displayed Skilled schedule, pit droid
  purchases and upgrade effects, later tracks and modern ports.
- Suggested later scope: a separate threshold-boundary trial with
  fourth and fifth place on the same commercial edition.

## Direct-play status

No direct play was performed. The original PAL booklet identifies
the commercial rules, including the input sequence and the cost of
holding repair. The PAL-labelled N64 Archive trace supplies the actual
race states, first-place result and next track. Only static frames were
inspected. Hardware inputs, audio, the physical pressing of the filmed
copy and the exact failure boundaries were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RAC-001 | The target is the 1999 European Nintendo 64 release NUS-NEPP-EUR, with English text available. The booklet belongs to the same European product family. | Confirmed | Corroborated | High | P1 PDF p. 1, R1, P2. W1 is labelled PAL and its menus are in English. |
| RAC-002 | The first Amateur route is The Boonta Training Course. The briefing discloses fourth or better, and reaching the line advances laps before the third crossing settles the result. The live driving view gives lap, time, position and nearby course shape. | Observation | Corroborated | High | P1 PDF pp. 6, 10–12. W1 1:09–1:17, 2:10–2:20, 3:18–3:22, 4:17–4:23 and 5:19–5:26. |
| RAC-003 | With the ordinary accelerator held, forward stick builds the thrust state. At yellow readiness the player releases and re-engages A to enter red-indicated boost. Letting go, braking or a heavy impact can end it. Continued boost raises heat. | Confirmed | Corroborated | High | P1 PDF pp. 11–12. W1 3:12–3:16 shows a red lamp and temperature warning, then ordinary speed. W1 3:22–3:34 shows another red boost, warning and an overheating indication without a wreck. Exact button timing is documentary. |
| RAC-004 | The two engine diagrams distinguish condition from speed and thrust. The booklet says held R repairs a moving craft while slowing it. During the third lap the actual repair label appears after contact and the car remains in the same race. | Observation | Corroborated | High | P1 PDF p. 11. W1 4:47–4:55 and 5:03–5:07 show the changing engine diagrams, repair and continued timing. An unrepaired fire or explosion is described by P1, but is not part of this run. |
| RAC-005 | The first race is actually classified. Anakin finishes first in 3:04.298, the result awards 1,200 Truguts, and Mon Gazza Speedway is selected and started afterward. | Observation | Corroborated | High | P1 PDF pp. 6, 10 and 13 explain progression and settlement. W1 5:23–5:38 shows finish, results and successor selection. W1 5:52–6:17 shows following course entry. |

## Basic data

- Analysis target: `PLAT-NINTENDO-64`.
- Developer and publisher: LucasArts.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Original European LucasArts booklet NUS-P-NEPP-NEU6](https://emulation64.fr/pdf/N64%20-%20Star%20Wars%20Episode%20I%20-%20Racer%20%28Francais%29.pdf),
  with French instructions in the scanned pages. Page references count
  PDF pages from the cover.
- P2: [Lucasfilm's history of the original Nintendo 64 release](https://www.starwars.com/news/star-wars-episode-i-racer-legacy).
  It also discusses later reissues. They are separate products.
- R1: [European cartridge and language inventory](https://www.nintendo64ever.com/Nintendo-64-Game-Data-Sheet%2C817%2CStar-Wars-Episode-I-Racer.html).
- W1: [N64 Archive PAL Tournament recording](https://www.youtube.com/watch?v=_KmXM8Y3Xks&t=69s).

## Mechanical decomposition

### Action Genes

- ACT-290: steer, accelerate and brake the dedicated racing craft.
- ACT-840: build forward thrust to the readiness signal, then
  re-engage the accelerator to commit boost. This preparation is
  repeatable within the race.
- ACT-841: hold repair on the damaged craft at a speed cost
  while staying in the active race.

### System Behaviour Genes

- SYS-320: ordinary steering and thrust move the hover vehicle.
  Contact can slow it and affect engine condition.
- SYS-516: settle lap progress and final classification at
  the finish. The exact penalty for skipping track segments remains
  outside the observed trajectory.
- SYS-1421: boost raises attainable speed and engine heat.
  Disengaging allows the temperature pressure to abate. The manual
  records a destructive consequence if the severe state goes unresolved.
  The demonstrated route recovers without that outcome.

### Constraint Genes

The thrust prerequisite belongs to ACT-840. The disclosed fourth-place
qualification belongs to OBJ-150. No separate course-access or initial
boost warm-up constraint is counted.

### Information Genes

- INF-205: the live race view shows lap, elapsed time, position and
  nearby course context.
- INF-208: the finish report settles place, exact time and prize.
  The track menu shows the next selectable event.
- INF-586: thrust readiness and engaged boost have their own cues.
  The heat warning and two engine condition diagrams expose risks
  independently of the current speed number.

### Objective Genes

- OBJ-150: complete the event within the disclosed accepted places
  and retain the classified result, reward and successor access.

### Time Genes

- TIM-003: steering, boost and repairs occur while the lap timer and
  rival field continue. Repair creates a pacing decision within the
  race rather than halting it.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Fresh English Tournament slot | Select Anakin and the first Amateur track | The Boonta briefing names the fourth-place threshold and three-lap record | RAC-002 |
| Ordinary acceleration with a clear line | Push forward and reapply A at yellow readiness | Red boost cue, higher speed and heat warning during the recorded lap | RAC-003 |
| Boost is warning or the craft hits the canyon wall | Disengage or lose boost on contact | Ordinary drive continues. The third-lap timer stays live | RAC-003, RAC-004 |
| Impact and engine diagrams are visible | Hold the documented repair control | The repair state appears at 4:53 as the craft continues at reduced speed | RAC-004 |
| The final lap finishes | Cross the finish line and advance the result | First of twelve, 3:04.298 and 1,200 Truguts | RAC-005 |
| Classification is settled | Advance and select slot two | Mon Gazza Speedway is selectable and the next race loads | RAC-005 |

## Strategic and experiential structure

A long clear segment permits a prepared boost but continuing near a
bend can combine heat with impact risk. The thrust and engine
indicators answer different questions. One shows whether the acceleration
action is ready or active. The others show a reason to disengage or
repair. Choosing a place to slow may preserve the craft at the cost
of a lead against rivals who continue moving.

## Replay and variation

The observed run wins. Fourth or better is shown in the briefing
and explained in the manual, rather than measured in a separate
fourth-place attempt. The same booklet describes replay and reward
limits. No result from a below-threshold run or destructive overheat
was inspected.

## Adjacent systems and history

The next track and continued career access are in scope. The droid and
parts menus, progression across later circuits and vehicle unlock
criteria are separable modules. Lucasfilm's reissue history discusses
modernized controls, so its newer-platform features are outside the
original PAL input contract.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-290, ACT-840, ACT-841 | Drive, arm boost, and pay speed to repair |
| System Behaviour | SYS-320, SYS-516, SYS-1421 | Integrate motion and damage, classify the race, and resolve heat |
| Constraint | None | Boost eligibility and placing are owned by their actions and outcome |
| Information | INF-205, INF-208, INF-586 | Show race, outcome, thrust and engine evidence |
| Objective | OBJ-150 | Finish within the qualifying places and retain progression |
| Time | TIM-003 | Make all decisions within the running race |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `631` (`GAME-0001`–`GAME-0631`).
- Exact genome matches: none.
- Tied near matches: `GAME-0276` — Forza Horizon 5 (`6 / 17 = 0.352941`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Forza Horizon 5 (GAME-0276)](../a-f/forza-horizon-5.md) | ACT-290, INF-205, INF-208, SYS-320, SYS-516, TIM-003 | Both translate live vehicle control and ordered laps into a displayed classification. Forza's road packet requires winning the standalone race and allows a rewind. Racer uses a set of qualifying places, recurring thrust preparation, engine heat and repair that gives up speed without rewinding. | Near, `0.352941` |

## Taxonomy impact

ACT-840 isolates preparing a recurring thrust state and re-engaging
the normal throttle. ACT-841 isolates holding a speed-priced repair
while the attempt continues. INF-586 makes the repeatable boost
cue and separate warning and engine condition available for decisions.

## Negative results

- The recorded completed race does not demonstrate an explosion,
  reset or fourth-place boundary trial.
- The thrust cue is not a consumable boost reservoir or an initial
  stage lock that lasts only until the first lap.
- Race result credit precedes the next menu; pit purchases do not
  explain why slot two is selectable.

## Delta summary

The new Nintendo 64 packet admits eleven genes, including three
new definitions. No earlier genome or tracked combination changes.

## New facts

- Forward thrust readiness alone does not engage boost. The established
  control sequence re-engages the accelerator once ready.
- Repair and race progress coexist in the same attempt.
- One actually qualifying finish records a result, a prize and
  the next available course.

## Principles and design implications

- Make readiness, thermal risk and sustained damage visible as different
  reasons to act.
- Let recovery cost momentum while the competition continues.
- Disclose the accepted finish places before a race and show the
  retained progression directly afterward.

## Puzzle or game generation potential

A design experiment could use short loops with a small number of
safe thrust intervals. Vary corner spacing and recovery cost, then
compare a strict win condition with a top-place set that permits
a deliberate repair. This is a proposed experiment.

## New genes

ACT-840, ACT-841 and INF-586.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_378](../../../research/taxonomy-changes/TAXONOMY_CHANGE_378.md).

## New questions

On the same commercial PAL ruleset, how do fourth and fifth place
differ in retained progression and prize settlement?

## Next recommended game

Analyse the first observed creature charm and flock entry in the
commercial Xbox Series X|S release of Flock.

## Why this game

The first race places acceleration, thermal risk and rolling repair
inside one sequence with a concrete threshold, recorded payout and
new course. This supports comparison without admitting the entire
upgrade economy or campaign.
