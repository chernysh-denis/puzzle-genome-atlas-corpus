---
game_id: GAME-0675
slug: teeny-tiny-trains
game_title: "Teeny Tiny Trains"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-028
    - ACT-900
  system:
    - SYS-1940
    - SYS-1941
    - SYS-1942
    - SYS-1943
  constraint:
    - CON-001
    - CON-102
    - CON-888
  information:
    - INF-001
    - INF-622
  objective:
    - OBJ-355
  time:
    - TIM-009
---

# Game: Teeny Tiny Trains

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Station colours, fixture positions and the value 28 are level
parameters, not separate mechanics.

## Analysis scope

- Version / ruleset: English commercial iOS App Store release, app
  6476918116, launched in March 2024. One original Chapter 2 Level 9
  board as seen in the iOS-attributed launch-window recording dated
  March 28, 2024. The exact app version and handset model were not
  identified. No claim about layout parity with subsequent versions.
- Structured analysis target: PLAT-IOS in
  `knowledge/platforms/games.json`. Solo base-game puzzle. The level
  was already selectable in the reference progress state.
- Entry: select Chapter 2 Level 9 and start from the empty editable
  track grid with red and blue departure sheds, two matched
  destination sheds, scenery obstacles and the 28 Journey cue.
- Primary decision loop: draw and erase track, read the visible route
  and set each marked Flip Flop's initial direction. Give blue a delay
  loop so red can pass through the shared stem first. Start the run,
  watch the automatic switch changes and both arrivals, then inspect
  the completion and journey total. If repeating that board, replay
  returns to the prepared routes and initial switch settings.
- Exit: both trains disappear into their matching destinations without
  a collision. Confirm the solved result, Journey 28 and the gold
  ticket. Replay the same layout once at 7x to check the result and
  stop at the repeated receipt, before entering any later level.
- Included: fixed board and visible colour roles, edit and erase,
  selected initial switch state, automatic switching on passage,
  shared-track timing, collision as an invalid shared occupancy,
  colour-gated arrival, automatic execution, replay and journey credit.
- Excluded: authorship or sharing of community maps, terrain gating
  mechanisms from other levels, wrong-colour terminal animation,
  aggregate scoring for wagons, later placement mode and traffic
  lights, hints, other sections and ports, purchases, ad rules,
  exact tick order and native save/relaunch durability.
- Potential scoped modules: the collision negative case on this exact
  board, a counterfactual mismatched station approach or a controlled
  run above the displayed ticket benchmark.
- Direct-play status: no personal iOS execution or binary inspection.
  The App Store and studio identify the commercial game. The iOS
  capture shows the full level twice with restored layout and the same
  Journey 28 result. A separate early-release walkthrough shows the
  in-game Flip Flop rule and an intersecting-train collision on a
  different board. Muted frames were inspected in the background.
  The device model, exact executable, internal timing and claims
  beyond the recorded room remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TTT-001 | The commercial iOS App Store product is 6476918116. Apple's lookup gives a March 27, 2024 US release timestamp. The studio links that listing and describes connecting tracks from station to station. | Observation | Direct | High | P1, P2, P3 |
| TTT-002 | Chapter 2 Level 9 starts with two launch sheds, two differently marked destination sheds and a bounded grid. The player draws connections and can remove and restore portions before pressing Play. | Observation | Direct | High | W1 00:05–00:35 |
| TTT-003 | Tapping a Flip Flop in planning changes its initial direction. A train passing it changes the setting for a subsequent traversal. At the shared destination fork the red train departs on its branch, then the blue setting is visible before the second arrival. | Observation | Corroborated | High | P4, W2 01:04–01:08, W1 00:43–00:51 |
| TTT-004 | One Play starts both trains on the laid tracks. The blue loop delays it relative to the red train at the shared trunk. Red clears the middle branch into its red destination, then blue uses the middle trunk and the blue branch. Editing controls are absent in that running view. | Observation | Direct | High | W1 00:35–00:53 |
| TTT-005 | Valid shared occupancy requires the trains to be separated at common route elements. The scoped attempt clears safely. An early release capture shows collision at an intersecting route and no success in a separate tutorial-level experiment. | Observation | Corroborated | High | W1 00:41–00:53, W2 02:04–02:11 |
| TTT-006 | The visible Journey cue is 28 before launch. The running counter advances along the traversal. The two matching arrivals resolve to a solved notice showing Journey 28 and a gold ticket. | Observation | Direct | High | W1 00:06, 00:42–00:53, 00:54–00:58 |
| TTT-007 | Replay from this result restores the same route geometry and starting switch configuration with both trains back at their origins. The faster attempt shows 7x while in motion and reaches the same displayed Journey 28 and gold ticket. | Observation | Direct | High | W1 00:58–01:13 |
| TTT-008 | The 28 count is consistent with the reconstructed 12 red and 16 blue cell transitions including station arrival. This supports a sum of distance rather than elapsed real time for this run. | Pattern | Corroborated | High | W1 00:37–00:58 and 01:01–01:13, R1 |

## Basic data

- Release / origin: Short Circuit Studio; storefront seller Short Circuit
  Studios AB. English App Store software for iOS, launched March 2024.
- Puzzle families: FAM-005 for route construction, FAM-008 for designing
  and then evaluating a programmed layout, and FAM-015 for coordinating
  two independently moving trains over shared segments.
- P1: [US App Store listing](https://apps.apple.com/us/app/teeny-tiny-trains/id6476918116).
  Product, English availability and mobile edition.
- P2: [Apple lookup for app 6476918116](https://itunes.apple.com/lookup?id=6476918116&country=us).
  US catalog release timestamp, seller and bundle identity. Current
  lookup version is not the version of the 2024 capture.
- P3: [Short Circuit Studio game page](https://www.shortcircuitstudio.com/teeny-tiny-trains).
  Confirms the station-to-station construction goal.
- P4: [Developer response on the Australian App Store](https://apps.apple.com/au/app/teeny-tiny-trains/id6476918116).
  The May 28, 2024 response specifies touching the Flip Flop sticker
  before starting a run to select the red arrow direction.
- W1: [Anotherkellydown, attributed iOS Chapter 2 Level 9 capture](https://www.youtube.com/watch?v=PQ2YMvw265w).
  Published March 28, 2024. The iOS attribution, App Store link and home
  indicator corroborate the device family. Complete scope at 00:05–01:13.
- W2: [dinalt, early Chapter 1 walkthrough](https://www.youtube.com/watch?v=0m2EFG992cM&t=64s).
  Published April 10, 2024, with an App Store link. The Flip Flop
  tutorial around 01:05 establishes intended switching. The colliding
  crossing in its Level 7 segment is only a negative corroboration
  of that rule family. The recording's device is unidentified.
- R1: [HannahBarbarian's later distance-scoring guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3572664650).
  Secondary cross-platform corroboration for summing route travel.
  Later builds, wagons and the guide's other optimisation rules are
  outside this analysis.
- Claim IDs: TTT-001–TTT-008.

### Reproducible route evidence

1. Inspect the separate red and blue starts and destination sheds,
   the empty finite grid and the Journey 28 cue. Confirm the top-left
   Chapter 2 Level 9 labels at approximately 00:06.
2. From 00:10–00:26, draw the two main approaches and form the shared
   trunk and destination fork. Run blue's outer approach through the
   small loop. A portion is removed and restored around 00:31–00:35.
   The placement screen exposes the junction markers and the Play
   state. Set the destination fork so the first traversal from the
   trunk leads to red. The image near 01:01 shows the restored
   route from above.
3. Start at 1x around 00:37. Red covers the long outer bend while
   blue enters the loop at about 00:42. Red enters the shared stem
   and the red branch around 00:45–00:47. Blue finishes the loop and
   approaches the same stem after red has left it. Around 00:47.50
   the destination fork indication has changed toward blue.
4. Red's locomotive enters its own shed before blue enters the
   second branch. The blue arrival is visible around 00:53. The
   solved result appears at approximately 00:54, and the fixed total
   and ticket are visible around 00:57.
5. The reconstructed paths contain twelve red and sixteen blue cell
   transitions, including each arrival. The red route approaches
   the shared branch from one outer side. The blue route passes the
   delay loop and approaches from the other side, then both use the
   same short stem at different times. This supports the observed
   sum of 28 without assuming the engine's internal tick order.
6. Replay restores both starts, earlier flip markers and the same
   trace geometry. Launch again and observe 7x around 01:05.75.
   The same result and ticket are shown at approximately 01:11.50.
   Treat speed here as a runtime control for this replay, not a
   different topology or route-distance rule.

## Mechanical decomposition

### Action Genes

- ACT-028: place, redraw or clear connected track geometry on the
  editable board, then keep it for a simulation. TTT-002.
- ACT-900: tap a marked junction's initial red alignment during
  planning without replacing its rail geometry. TTT-003.

### System Behaviour Genes

- SYS-1940: dispatch multiple locomotives with one run command and
  advance each along its connected line until a destination receipt
  or invalid event. TTT-004, TTT-006.
- SYS-1941: passing a Flip Flop changes the selected continuation
  for the next encounter. TTT-003, TTT-004.
- SYS-1942: replay restores the chosen track and initial alignments
  while resetting traversers and their run state. TTT-007.
- SYS-1943: judge the completed Journey total against the displayed
  gold-ticket benchmark. Here twelve and sixteen transitions total
  28 and settle as gold. TTT-006–TTT-008.

### Constraint Genes

- CON-001: the board is a finite addressed grid with authored
  station locations and fixed obstructions. TTT-002.
- CON-102: trains must avoid conflicting occupancy at shared rails
  within the same run. The safe delay and separate collision witness
  delimit the claim. TTT-004, TTT-005.
- CON-888: a locomotive's displayed colour must match its assigned
  destination. The two valid pairings are observed. The exact rejection
  animation for an invalid approach is outside scope. TTT-002,
  TTT-006, R1.

### Information Genes

- INF-001: visible tracks, fixtures, locomotive colours, required
  destinations and starting switch alignments support planning.
  TTT-002, TTT-003.
- INF-622: show the target journey value before the run, the growing
  count during it and the final ticket receipt. TTT-006–TTT-008.

### Objective Genes

- OBJ-355: complete the run by receiving every required locomotive
  at its matching separate endpoint without a collision. TTT-004,
  TTT-006.

### Time Genes

- TIM-009: plan without motion, commit a run and revise only after
  execution stops or settles. The captured speed control changes
  playback/advancement without providing separate steering. TTT-002,
  TTT-004, TTT-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Fixed exposed board, no connected route | Draw segments and revise erroneous pieces | Same board, connected plan and readable junction stickers | TTT-002 |
| Flip Flop in editable plan | Select its initial direction | Initial continuation marked on the same track | TTT-003 |
| Complete plan, both locomotives waiting | Press Play once | Two trains advance concurrently along their paths | TTT-004 |
| Train traverses marked junction | Complete the passage | Switch selection changes for next travel through it | TTT-003 |
| Red clears the shared middle stem | Blue finishes its delay loop and enters after red | Both traverse the shared path at non-conflicting times | TTT-004 |
| Only one train has arrived | Remaining colour-matched train enters its shed | Solved result, Journey 28 and gold ticket | TTT-006 |
| Solved layout with changed runtime switches | Choose Replay | Original starting states and same authored routes | TTT-007 |

## Strategic and experiential structure

Topological connectivity alone does not establish a valid simulation.
The choice of initial fork direction matters because the second
arrival sees a different direction. The delay loop trades distance
for temporal separation. The interface allows the player to see and
retest the causal order without steering the trains during execution.

## Replay and variation

The primary and accelerated replays recover the same geometry,
origins and initial switch markers. Both yield 28 and the same gold
receipt. The measured facts concern those two runs. Alternative shapes,
wrong-colour behavior and a changed journey budget would need their
own trace.

## Adjacent systems and history

Railbound in the Atlas sends numbered carriages to a common
locomotive in order. In this packet the players schedule separate
coloured locomotive arrivals, and crossing a Flip Flop changes the
next applicable branch. Later Teeny Tiny Trains revisions added
controls and levels outside this launch-window reconstruction.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-028, ACT-900 | Lay persistent track and set initial junction direction |
| System Behaviour | SYS-1940, SYS-1941, SYS-1942, SYS-1943 | Execute, flip, replay and settle the journey result |
| Constraint | CON-001, CON-102, CON-888 | Fixed positions, time-separated occupancy and matching endpoints |
| Information | INF-001, INF-622 | Read the board and benchmark or current journey value |
| Objective | OBJ-355 | Finish every separate delivery |
| Time | TIM-009 | Plan, commit and observe the locked run |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `674` (`GAME-0001`–`GAME-0674`).
- Exact genome matches: none.
- Tied near matches: `GAME-0056` — Railbound (`5 / 16 = 0.312500`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Railbound (GAME-0056)](../m-r/railbound.md) | ACT-028, CON-001, CON-102, INF-001, TIM-009 | Both edit a visible finite rail layout, then schedule safe concurrent movement in a locked run. Railbound couples numbered carriages to one locomotive in order with finite rail pieces. This level delivers two independently coloured locomotives to separate stations, flips the shared fork after a traversal and evaluates combined travel. | Near, `0.312500` |

## Taxonomy impact

Eight admissions distinguish pre-run switch selection, subsequent
automatic switching, autonomous matching arrivals, replay, the
distance-based receipt, station colour eligibility, journey feedback
and successful multi-station delivery. Five existing boundaries
describe the editable layout, finite board, collision constraint,
visible current state and stopped planning/run phase boundary.

## Negative results

- Faster playback does not lower the observed Journey 28.
- A route drawn all the way to the destinations can still be invalid
  if its trains try to use one shared locus simultaneously.
- A station accept/deny animation for wrong colour and an over-budget
  Chapter 2 Level 9 result were not isolated.
- Both observed runs use the same two trains. The separate
  Chapter 1 material does not establish a second scoped solve.

## Delta summary

Thirteen genes. Eight new and five reused. One launch-window iOS
board and its internally observed safe repeat through the solved
receipt.

## New facts

- This valid route uses geometric delay to isolate occupancy of the
  same track and permit the right junction transitions.
- The completed journey distance holds constant when the observed
  run uses a faster speed setting.

## Principles and design implications

Make the current position and the next switch state visible separately.
Reward reaching each distinct destination, then use a travel benchmark
to distinguish efficient valid schedules. A short loop can make a
route feasible even when both visible endpoints are already connected.

## Puzzle or game generation potential

Build a new small graph with different endpoints and a shared segment.
Vary initial switches and the available lengths of alternate routes.
Validate that each moving token has an eligible destination and avoids
temporally overlapping occupancy before assigning a distance target.

## New genes

- ACT-900
- CON-888
- INF-622
- OBJ-355
- SYS-1940
- SYS-1941
- SYS-1942
- SYS-1943

## New combinations

None. All 274 verified combinations were checked as proper subsets. Railbound’s COMB-0056 requires its finite inventory, coupling and ordered receiver objective, which this level does not support.

## Taxonomy changes

[TAXONOMY_CHANGE_421](../../../research/taxonomy-changes/TAXONOMY_CHANGE_421.md).

## New questions

- How does the exact launch build handle the first wrong-colour arrival?
- What is the first over-budget ticket result on this layout family?
- Can the same 28 trips be realised by a differently shaped delay?

## Next recommended game

Selection 057 ends at this iOS level. The next game requires its own
approved selection.

## Why this game

It exposes the difference between connecting a rail graph and
scheduling safe occupation while each automatic passage changes a
subsequent routing choice.
