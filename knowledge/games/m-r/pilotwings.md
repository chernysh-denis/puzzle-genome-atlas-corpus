---
game_id: GAME-0661
slug: pilotwings
game_title: "Pilotwings"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-876
  system:
    - SYS-556
    - SYS-1902
  constraint:
    - CON-472
  information:
    - INF-609
  objective:
    - OBJ-350
  time:
    - TIM-003
---

# Game: Pilotwings

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The game-specific guide colour, names and point weights are parameters.

## Analysis scope

- Version / ruleset: original English commercial North American Super
  Nintendo release from 1991, physical Game Pak SNS-PW-USA.
  The two records use the English SNES rules. Neither recorded
  cartridge was independently matched by ROM checksum.
- Structured analysis target: PLAT-SUPER-NINTENDO in
  `knowledge/platforms/games.json`. Nintendo Switch Online is a separate
  legal way to access the title and is outside the evidence boundary.
- Entry: start a new game, open Lesson 1 in Flight Area 1, select
  Light Plane before Skydiving and open its curriculum. Start the
  powered approach with the aircraft already airborne.
- Primary decision loop: adjust heading, pitch and power in view
  of the green approach guide, changing ground-relative height
  display and runway. Once the aircraft touches down, brake to a
  complete stop. The quality report uses both contact and rest.
- Exit: the flight is credited at the graded landing. The lesson
  summary retains the Light Plane result and presents Continue,
  Retry and End. The second task and lesson qualification are
  separate milestones.
- Included: the briefing, approach, live height and guidance,
  powered control, the runway and stopping phase, four-category
  point settlement and the immediate lesson continuation choices.
- Excluded: powered takeoff, later biplane ring courses, wind as
  a variable in Lesson 1, solo Skydiving mechanics, the full
  licence cycle, other vehicles, unpublished formula coefficients,
  resets from password and later releases.
- Potential scoped modules: Flight Area 1 Skydiving, a subsequent
  biplane lesson with ring credit, or a controlled same-touchdown
  comparison with different stopping positions.

## Direct-play status

No direct play. The original North American booklet and two
attributed English runs were checked. Full-resolution stills and
screen text were inspected in the background without playing audio
or opening a foreground player. The runs bracket accepted landing
quality and beam credit. Exact controller events, failure branches,
hardware on the first recording and ROM revisions were unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PL-001 | Nintendo's original Pilotwings is an SNES release from 1991, with the North American physical Game Pak catalogued as SNS-PW-USA. | Observation | Corroborated | High | P1 cover, P2 p. 6, H1 cartridge and its label scan. |
| PL-002 | Lesson 1 has two events and a 120-point qualification total. Light Plane can be attempted first, with its own runway briefing and result. | Observation | Corroborated | High | P1 pp. 4–5, W1 0:40–0:56 and 1:52–2:01, W2 1:12–1:27 and 2:17–2:26. |
| PL-003 | The ascent or descent input moves the nose, left and right turn the aircraft, A raises throttle and B reduces throttle before touchdown. The first trial opens level and airborne at 300 feet and 51% throttle without wind. Low power can cause a stall and higher speed reduces turn responsiveness. | Observation | Corroborated | High | P1 pp. 7–8, W1 0:56–1:25 and W2 1:27–1:55. The stall warning is from the booklet. |
| PL-004 | Landing accuracy uses both position at touchdown and where the aircraft stops, relative to the white centreline. Touchdown angle is a separate factor and bouncing can lower it. | Observation | Corroborated | High | P1 p. 16, W1 1:37–1:55, W2 2:02–2:20. The footage compares accepted outcomes without isolating individual variables. |
| PL-005 | A spatial green guide indicates the descent and the right-edge height scale appears at or below 200 feet and enlarges at or below 50 feet. | Observation | Corroborated | High | P1 pp. 8, 16, W1 1:10–1:34 and W2 1:47–1:59. Exact cutoffs are documented, with visible samples on both sides. |
| PL-006 | B applies the brake after contact. The airplane rolls on the runway at zero altitude before the settled landing message, then the attempt is graded. | Observation | Corroborated | High | P1 pp. 7–8, W1 1:37–1:52 and W2 2:02–2:17. The booklet establishes input mapping. |
| PL-007 | Four score rows are accuracy, time, angle and beam. W1 earns 35/50, 10/20, 18/20 and 0/10 for 63. W2 earns 50/50, 18/20, 20/20 and 8/10 for 96. The lesson shows 57 and 24 still needed respectively. | Observation | Corroborated | High | W1 1:52–2:01, W2 2:17–2:26, P1 pp. 4–5 and 16. |

## Basic data

- Release / origin: Nintendo's original 1991 North American
  Super Nintendo release, single-player, Game Pak SNS-PW-USA.
- Puzzle families: physics and object manipulation (FAM-007)
  for the relationship between power, pitch, height and contact.
  Real-time system pressure (FAM-010) applies because movement and
  score time continue through the manual approach and rollout.
- P1: [Scanned original Nintendo instruction booklet](https://manuals.plus/m/398c8ba08affb9fd0127af3f68a97a8cdc15811dd7468c1bba02f5541f7dc228.pdf),
  with [readable transcription](https://world-of-nintendo.com/manuals/super_nes/pilotwings.shtml).
  Printed pp. 4–5 explain lesson flow, pp. 7–8 fixed-wing
  inputs and guided approach, and p. 16 instruments and scoring.
  These are two formats of the same source.
- P2: [Nintendo's series history](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/3DS_Pilotwings?_a=DATC1RAAZAA0),
  printed p. 6 of the Pilotwings Resort booklet, confirms the
  original 1991 SNES release. The [Nintendo Classics catalogue](https://www.nintendo.com/us/store/products/super-nintendo-entertainment-system-nintendo-classics-switch/)
  lists the separate modern availability.
- H1: [SNES Central cartridge catalogue and scans](https://snescentral.com/article.php?id=0005),
  identifies the North American cart, physical labels and publisher.
- W1: [LongplayArchive, Retro Game Spacko credited](https://www.youtube.com/watch?v=dvBbQPMGmiM&t=40s),
  0:40–2:01. Attributed SNES recording. The first flight
  settles with 63 points while earning no beam credit.
- W2: [BitsAndGlory, original SNES Jr listed](https://www.youtube.com/watch?v=gTb5g-cxxQw&t=72s),
  1:12–2:26. The author describes the hardware and successful
  attempts presented in segments. Its finished first flight
  settles with 96 points and returns to the lesson choice.
- Claim IDs: PL-001–PL-007.

### Reproducible route evidence

1. Start a new game and open Lesson 1. The lesson map shows
   a runway and a separate skydiving target. Select Light Plane.
   The flight briefing directs the pilot to use the green approach
   and land on the runway. W1 0:40–0:53 shows these screens.
2. Start the trial with Start. The plane enters already airborne.
   W1 0:56 shows 300 feet and 51% throttle. Pitch down to
   descend or up to raise the nose, and use left or right to
   correct alignment. Adjust throttle with A or B as required.
   P1 p. 7 documents the stall risk with low power and the
   slower turning response at high speed.
3. Follow the visible approach guide toward the white runway line.
   Monitor the altitude and the right-edge scale. W1 1:13 to
   1:16 moves from 203 to 180 feet and the scale appears.
   W2 1:53 shows 56 feet with the regular scale, followed by
   40 feet with the enlarged scale at 1:56. W2 also shows a
   guide marker changing colour in this interval. The precise
   contact or beam-credit formula is outside the trace.
4. Make runway contact without an excessive angle and slow to a
   full stop with B, watching where the plane actually stops.
   W2 2:02 has zero altitude but the markings still move
   beneath the plane. At 2:11 Landing OK is visible with the
   aircraft steady on the white line. W1 stops offset from
   the centreline and also receives Landing OK at about 1:46.
5. Read the four scores. W2 shows 50/50 accuracy, 18/20 time,
   20/20 angle and 8/10 beam for 96 points. At 2:26 the lesson
   reports 24 more required and offers Continue, Retry and End.
   W1's reported 63 includes 0/10 beam, with 57 more needed.
   This difference shows how guidance score and the credit for
   one settled flight can vary independently.

## Mechanical decomposition

### Action Genes

- ACT-008: turn and pitch one live aircraft through the scene
  using local controls. It is never sent to a destination to
  fly there automatically. PL-003.
- ACT-876: A and B change airborne power. B becomes the runway
  brake on contact. PL-003, PL-006.

### System Behaviour Genes

- SYS-556: pitch, power, speed and height evolve in a fixed-wing
  model through contact and rollout. This is the shared causal
  structure at the arcade game's evidenced fidelity. There
  is no inference about simulated subsystems or coefficients.
  PL-003, PL-006.
- SYS-1902: settle runway accuracy from the two positions and
  report distinct time, approach angle and guide credit.
  PL-004, PL-006, PL-007.

### Constraint Genes

- CON-472: powered descent and the live runway stop depend on
  speed, attitude, ground clearance, alignment and room to
  brake. Reuse is limited to the relevant approach envelope.
  Full departure, weather and stall outcomes were untested.
  PL-003, PL-004, PL-006.

### Information Genes

- INF-609: the visible spatial guide and near-ground scale help
  the pilot judge the approach while still manually in control.
  The scale is distinct from the always-visible altitude value.
  PL-003, PL-005.

### Objective Genes

- OBJ-350: land, roll to a full stop and bank the graded
  powered-flight result. The 120-point two-event qualification
  remains open after either run. PL-002, PL-006, PL-007.

### Time Genes

- TIM-003: choose how to turn, adjust power and brake while the
  flight and clock run through the attempt. Time contributes
  to the outcome independently of geometry. PL-003, PL-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Light Plane curriculum | Start | Powered, level approach at 300 feet | PL-002, PL-003 |
| Airborne above the low scale range | Descend into the low height range | Ground-relative scale visible, then enlarged nearer the runway | PL-005 |
| Approach above runway | Wheels make contact | Zero altitude, rolling aircraft and B available as brake | PL-004, PL-006 |
| Runway rollout | Bring the plane to rest | Accepted landing message | PL-006 |
| Accepted landing | Score is presented | Accuracy, time, angle and beam settle, score carries into the lesson decision | PL-007 |

## Strategic and experiential structure

Set the approach before descending too far. A faster approach can
reduce turn response and make useful corrections harder. A late,
precise touchdown still leaves a stopping decision. Losing guide
credit can reduce the result without preventing the flight from
counting. A shorter approach scores independently of alignment.

## Replay and variation

The lesson decision includes Retry after the result. W1 and W2
are distinct accepted traces with different alignment and point
splits. No inference is made about repeated retry scoring or
exact penalties after bouncing or stopping outside the runway.

## Adjacent systems and history

Skydiving is the separate second event. Later Light Plane
curricula may award ring credit. Nintendo's SNES original,
Pilotwings 64 and Pilotwings Resort are distinct games. Only the
first powered approach on the original cartridge enters this genome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-876 | Steer and pitch locally, then use phase-dependent power and braking |
| System Behaviour | SYS-556, SYS-1902 | Continue powered dynamics into ground contact and settle the multi-part result |
| Constraint | CON-472 | Respect the approach and runway envelope |
| Information | INF-609 | Follow the suggested glide path and read the near-ground scale |
| Objective | OBJ-350 | Complete the graded powered landing through a full stop |
| Time | TIM-003 | Act while the attempt and its elapsed time advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `660` (`GAME-0001`–`GAME-0660`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](../s-z/uncharted-2-among-thieves.md) | ACT-008, TIM-003 | The top numerical match shares only direct navigation and continuous progression. The train escape uses unstable climbing geometry. Pilotwings uses throttle, alignment and runway braking. | Near, `0.181818` |

## Taxonomy impact

The powered-flight model and runway envelope from
[Microsoft Flight Simulator 2024](microsoft-flight-simulator-2024.md)
apply at the evidenced fidelity. The Cessna starts parked and ends
with a shutdown and logbook entry, while Pilotwings grades an
already airborne approach and stop. ACT-008 represents local direction and pitch.
ACT-321's independently specified fixed-wing control axes are
not established in this two-axis input mapping. ACT-803 is a
held glider flare and does not brake rolling wheels. SYS-1774
has passed-gate credit and landing impact, which differs from
separate guide, angle, elapsed time and a two-position runway
accuracy check. INF-565 groups relative target bearing, ring
acknowledgment and thermals. OBJ-326 settles one scored route
with a badge threshold. The Light Plane result settles before
the second event and has no demonstrated separate badge threshold.

## Negative results

- An accepted landing earned zero beam points in W1, so credit
  for following the guide is not an eligibility gate.
- Zero altitude at first contact precedes the Landing OK message.
  The contact frame alone cannot establish a completed landing.
- W2's 96 points leave 24 required in the second event, with no
  full Lesson 1 licence awarded for the observed landing.
- No checksum, exact input trace, unsuccessful landing path or
  independent perturbation of scoring inputs was established.

## Delta summary

Eight scoped genes, four new boundaries and four existing
ones. No earlier signature or verified combination is changed.

## New facts

- One control changes from reducing thrust to braking the rolling plane.
- Runway accuracy samples both touchdown position and stopped position.
- The approach aid and height magnification help guide control without
  making the guide award a requirement for accepting a landing.

## Principles and design implications

Judge a landing across contact and the end of the rollout to keep
braking meaningful. Present a narrower display near the ground,
when small height changes matter. Give guidance credit its own row
so a recoverable route error stays distinct from losing the attempt.

## Puzzle or game generation potential

Give a short virtual approach two ways to gain correction time and
one runway with limited room to stop. Sample the first contact and
the final position separately. Award a small optional guidance
bonus while preserving readable outcome feedback.

## New genes

- ACT-876
- INF-609
- OBJ-350
- SYS-1902

## New combinations

No subset of the scoped genes supports any of the 274 verified combinations.

## Taxonomy changes

[TAXONOMY_CHANGE_407](../../../research/taxonomy-changes/TAXONOMY_CHANGE_407.md).

## New questions

How are stopping and contact deviations weighted? Where do the
observed marker colour changes correspond to guide credit? What
state changes when a bounced landing still ends in a valid stop?

## Next recommended game

Batman: Arkham Shadow, the full commercial Meta Quest 3 release.
Find an opening encounter with a clearly recorded objective and
terminal handoff, then separate the player's VR actions from the
game's contact, information and evaluation rules.

## Why this game

The first powered flight makes the differences between guidance,
actual flight, runway contact, control during rollout and a scored
stop visible within one short assessment.
