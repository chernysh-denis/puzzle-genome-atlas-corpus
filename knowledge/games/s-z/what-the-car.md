---
game_id: GAME-0644
slug: what-the-car
game_title: "WHAT THE CAR?"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-857
    - ACT-858
  system:
    - SYS-711
    - SYS-1860
    - SYS-1861
    - SYS-1862
  constraint:
    - CON-854
  information:
    - INF-598
  objective:
    - OBJ-133
  time:
    - TIM-003
---

# Game: WHAT THE CAR?

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English commercial iPhone Apple Arcade release
  of WHAT THE CAR?, App Store ID 1534708672, released 4 May 2023.
  The ruleset is the launch-era phone touch route witnessed in the
  recording published that day. Its exact app revision, iOS build
  and phone model are not disclosed.
- Primary decision loop: steer the running car along the elevated
  road, choose when to use the spring action before the next gap
  or obstacle, and adjust the approach after a failed jump.
- Entry: in Episode 1, Jumping, reach the selectable launch for
  Car With Jumps on the island map and use its launcher.
- Exit: cross the marked finish, receive and confirm the timed
  crown, resume map control and start the separately selected
  Jumps With Jumps. The later course's finish is outside scope.
- Included: two independent touch controls, the legged runner,
  speed pads and jump approaches, unsupported falls that end the
  attempt, the timed crown, and map return and successor.
- Excluded: the preceding untimed introduction, other branching
  routes and locomotion variants, other platforms, later layouts,
  exact jump input duration and crown thresholds, power-off
  persistence, leaderboards, level editor and community courses.
- Suggested later scope: repeat the same takeoff with and without
  the pad at matched steering and compare spring usage at landing.

## Direct-play status

No direct play was performed. Apple's storefront, dated launch
announcement and the developer's press kit establish the commercial
iPhone release and its separation from the later Steam release. The
release-day recording is from the Azeemjaffer iPhone Gaming channel,
with a phone-proportioned active capture, home indicator and live
steering wheel and spring controls. The second Apple Arcade capture
corroborates the same course and successor. Its specific device is
undisclosed. A separate firsthand account identifies an iPhone 13 Pro
Max touch session, used only for platform and controls corroboration.
The sampled frames had no audio. The touch contacts themselves,
device logs and exact launch executable were unavailable.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WC-001 | Triband released the commercial Apple Arcade iPhone game on 4 May 2023. The analysis uses the launch-era touch build and the recorded Episode 1 course. | Confirmed | Direct | High | P1 official product and iPhone listing, P2 Apple release and phone image, P3 Triband press kit, W1 release-day capture with iPhone channel attribution. |
| WC-002 | The map is directly navigable. Approaching a course node presents its preview, and the separate launcher transfers the car into the named course. During a run the virtual wheel and the action control are separate. | Observation | Corroborated | High | P5 developer description of separate touch controls. W1 5:56–6:09 and W2 10:11–10:23. R1 confirms touch play on iPhone. |
| WC-003 | On Car With Jumps the legged car keeps advancing along the road during a run. The wheel changes its direction. The separate spring action can lift it above the road, with a changing nearby indicator. | Observation | Corroborated | High | P2 and P3 locomotion and P5 control channels. W1 6:09–6:23 and 7:04–7:14. W2 10:23–10:36. No exact tap length or refill rate is derived. |
| WC-004 | A chevron speed pad and the current jump approach can carry the car over an unsupported break. The far road supplies landing support. Launch heading and timing can still leave the car short or outside the road. | Observation | Corroborated | High | W1 6:58–7:02 contrasts with 7:11–7:17 and 7:23–7:27. W2 10:25–10:40 shows pads and a shorter airborne line. R2 corroborates the pad and jump distinction. |
| WC-005 | Dropping below the far edge ends the attempt. The same cannon prompt returns and a separate launch begins the course again. No finish result is awarded for the fall. | Observation | Direct | High | W1 7:01–7:06 shows fall, failure cue, restored launcher and a new start. W1 6:28–6:32 shows an earlier restart of the same course. |
| WC-006 | The checkered finish settles time into a crown against the course's displayed bands. The same course settles 23.068 seconds with a pale silver crown in W1 and 18.698 seconds with gold in W2. A hidden-card reward is separate from ordinary finish. | Observation | Corroborated | High | W1 7:27–7:34 and W2 10:41–10:47. P4 describes course-local gold times and hidden cards. No new card appears in the fresh W1 result. Exact cutoffs were not isolated. |
| WC-007 | Confirming the result resumes map movement with the completed node visibly marked. The player travels to a separate node, launches Jumps With Jumps and begins that course. | Observation | Corroborated | High | W1 7:34–7:54 and W2 10:47–11:02. W1 advances with a silver crown without an observed new collectible card. The scoped observation ends before the next result. |

## Basic data

- Analysis target: `PLAT-IOS`, native iPhone.
- Developer and publisher: Triband.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Official App Store listing for product 1534708672](https://apps.apple.com/gb/app/what-the-car/id1534708672).
- P2: [Apple Arcade launch announcement, 4 May 2023](https://www.apple.com/au/newsroom/2023/05/apple-launches-20-fun-new-games-for-its-award-winning-apple-arcade-service/).
- P3: [Triband's WHAT THE CAR? press kit](https://triband.notion.site/WHAT-THE-CAR-Press-Kit-9b5179fb587d41acb40b436bbdd15577)
  and [developer product page](https://whatthegames.com/car).
- P4: [Apple's iPhone feature on time crowns and hidden cards](https://apps.apple.com/pl/iphone/story/id1676522716).
  Its example time target is for a different course.
- P5: [Triband support on wheel and action controls](https://what-the-car-faq.instantdocsbase.com/help/how-can-i-play-what-the-car-with-my-friends).
  The later support page corroborates the separation already shown in the launch footage.
- W1: [Azeemjaffer iPhone Gaming, first Apple Arcade gameplay, 4 May 2023](https://www.youtube.com/watch?v=VQzgcOqSuK8&t=358s),
  primary release-era phone trace.
- W2: [Dinsun, Apple Arcade Episode 1 All Gold](https://www.youtube.com/watch?v=H9SZrXjx4rQ&t=611s),
  same course with gold. The lower-left branded card is a persistent
  video overlay and is not evidence of a pickup.
- R1: [Factornews firsthand account on iPhone 13 Pro Max and other devices](https://www.factornews.com/article/le-guide-factor-apple-arcade-partie-34-page-1-50093.html),
  version 3.5.0, corroborating landscape touch play only.
- R2: [Rowan Jones, player-authored Car With Jumps route](https://twinfinite.net/guides/what-the-car-walkthrough-gold-on-all-levels-guide/).
  The later route guide distinguishes pad acceleration and jumping.
  The iPhone footage owns all active route and result claims.

## Mechanical decomposition

### Action Genes

- ACT-008: navigate the controllable car on the episode map to the
  course launch points.
- ACT-857: steer the running car during the course with the virtual
  wheel while retaining the separate action.
- ACT-858: initiate the spring jump during the approach to a bend,
  obstacle or break in support.

### System Behaviour Genes

- SYS-711: evaluate elapsed time in the valid finish against the
  course-local crown bands.
- SYS-1860: carry the motion gained from the pad into a nearby
  separately chosen jump.
- SYS-1861: close a fallen run and return to the same launcher for
  a new attempt with fresh course progress.
- SYS-1862: accept a settled result, restore map control, mark the
  completed node and allow the separate successor launch.

### Constraint Genes

- CON-854: an ordinary gap jump needs reachable solid support
  at its destination. The water gap itself is unsupported.

### Information Genes

- INF-598: read the live spring indication separately from elapsed
  time, medal bands and crown on the settled result.

### Objective Genes

- OBJ-133: finish the selected official course and settle its timed
  rating. No intermediate time checkpoint is visible on this course
  and a gold crown is not necessary for ordinary progression.

### Time Genes

- TIM-003: real-time motion continues while the player chooses
  steering and the moment to use the spring.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Episode map with reachable course marker | Move to the marker and operate the launcher | The named Car With Jumps starts and the touch wheel and spring become available | WC-002, WC-003 |
| Running car near the chevrons and striped edge | Steer through the pad and trigger a jump aligned to the far road | The car can clear the gap and continue from its landing | WC-004 |
| Car falls below the far deck | Let the attempt end | The failure message appears and the same launcher returns without a crown | WC-005 |
| Same course's restored launcher | Use the action control again | A fresh approach starts at the beginning of the same course | WC-005 |
| Car reaches the checkered finish | Cross and let the result settle | Time and crown are awarded separately from the track's collectible card | WC-006 |
| Result with red retry and green confirm controls | Confirm, traverse the map and separately launch the next marker | Active play resumes in Jumps With Jumps with the first node marked | WC-007 |

## Strategic and experiential structure

Steering selects the corner line and landing direction, while
the spring selects when to leave it. A speed pad changes the
approach without removing the need for a valid landing. A fast
cut across the route competes with the risk of falling and
starting again.

## Replay and variation

The first recording falls short of an elevated deck and returns
to the course launcher. Its later complete run settles
23.068 seconds with a silver crown. The second recording uses
a shorter airborne route near the last bend and settles
18.698 seconds with a gold crown. Both return to the map and
start the same successor. These results support timed evaluation
and onward travel after silver. They do not identify an exact
gold cutoff for every build.

## Adjacent systems and history

This packet concerns one launch-era Episode 1 route. It does not
extend to earlier tutorial variants or later layouts with the
same track title. Other starting routes can select other forms.
The independent course card, released episode updates, leaderboard,
community editor and later platforms are outside the observed clear.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-857, ACT-858 | Navigate the map, steer the runner and initiate a spring jump |
| System Behaviour | SYS-711, SYS-1860, SYS-1861, SYS-1862 | Settle crown, carry momentum into a jump, restart after fall and accept into map continuation |
| Constraint | CON-854 | Require a landing surface within reach |
| Information | INF-598 | Keep spring state and finish result visible in their respective views |
| Objective | OBJ-133 | Finish the selected course and settle the timed rating |
| Time | TIM-003 | Act during continuous motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `643` (`GAME-0001`–`GAME-0643`).
- Exact genome matches: none.
- Tied near matches: `GAME-0216` — Trackmania (`3 / 19 = 0.157895`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Trackmania (GAME-0216)](trackmania.md) | OBJ-133, SYS-711, TIM-003 | Both settle a live official course into an elapsed rating. The scoped Trackmania course requires ordered checkpoints and can return a result within its driving session. Car With Jumps uses a legged runner with a separate touch spring, open gaps and a confirmed return to the navigable map before the next course. | Near, `0.157895` |

## Taxonomy impact

Six additions isolate touch steering, spring action, speed-pad
carry, launcher retry, map continuation and the two information
views. Five existing definitions cover direct map navigation,
landing support, elapsed rating, official course completion and
real-time decision timing.

## Negative results

- The in-run spring indicator does not display elapsed seconds.
- A pad or a jump can leave the car short of support. The falling
  attempt is replaced before a timed finish.
- Silver suffices for the witnessed onward route. The sequence
  does not require a gold result or a new card.
- The newly playable course and the prior reward marker were
  observed on the running app. No persistent reload was tested.

## Delta summary

Eleven scoped genes, six new and five reused. Only the first
witnessed Car With Jumps clear and immediate map successor are
admitted to the genome.

## New facts

- A spring jump can be timed while steering remains separate.
- The same route exposes the difference between a valid landing
  and a fall that returns to its launcher.
- The crown result and the playable hub successor are distinct
  observed states.

## Principles and design implications

Let timing of a jump and direction be separate decisions. Give
players a repeatable start after failure. A lower timed rating can
leave a clear valid while leaving a clear improvement target.

## Puzzle or game generation potential

Prototype a running car on a short offshore route. Place a speed
pad before an open gap and let the player choose a safe longer
turn or a faster jump. Grade only completed runs and restore the
map on accepting the result.

## New genes

ACT-857, ACT-858, SYS-1860, SYS-1861, SYS-1862 and INF-598.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_390](../../../research/taxonomy-changes/TAXONOMY_CHANGE_390.md).

## New questions

How much of the landing difference comes from approach speed,
spring use and steering at takeoff in one same-build comparison?

## Next recommended game

Analyse the original English North American Game Boy Color
Wario Land 3 from key to matching chest and its map effect.

## Why this game

The continuous run, independently timed spring and distinct
settled result make the unusual locomotion consequential.
