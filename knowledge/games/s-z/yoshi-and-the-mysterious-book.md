---
game_id: GAME-0671
slug: yoshi-and-the-mysterious-book
game_title: "Yoshi and the Mysterious Book"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-894
  system:
    - SYS-1922
    - SYS-1923
    - SYS-1924
    - SYS-1925
  constraint: []
  information:
    - INF-618
  objective:
    - OBJ-353
  time:
    - TIM-003
---

# Game: Yoshi and the Mysterious Book

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Foods, colours, sizes, numbers of stars and stage geometry are instance parameters.

## Analysis scope

- Version / ruleset: English commercial base game for Nintendo Switch 2,
  released May 21, 2026. Ordinary solo chapter play in Chapter 1, Wildwoods,
  Glubbit Habitat. Use the recorded retail rules as the baseline. The
  captures do not show the executable version number.
- Structured analysis target: PLAT-NINTENDO-SWITCH-2 in
  `knowledge/platforms/games.json`. Exclude demo and demo-save transfer.
- Entry: start the open Glubbit Habitat and approach a green Glubbit
  with its normal cyan bubbles. The playable reference comes after
  the entrance dialogue.
- Primary decision loop: approach a Glubbit and use Tail Flick to carry
  it. Observe the small cyan bubbles that rise as it is moved. Jump up
  into the apple branch with the passenger. After it eats the fruit,
  continue moving and watch the fed animal release a larger yellow
  bubble. Confirm the one-star apple fact, then inspect the written
  result on the creature's pages.
- Exit: verify the illustrated apple entry via Check Pages during
  the expedition or on the same creature spread after the return.
  The change in emitted bubbles and the retained entry are required
  for the reference trace. The habitat's separate rescue is not a
  prerequisite for the apple entry.
- Included: direct locomotion and jumps, back carry, bubble release
  on sustained running with the passenger, apple-conditioned change
  in output, bubble capture and rise, live discovery feedback and
  access to the retained single discovery.
- Excluded: all-stars or flower cleanup, naming as a requirement,
  resolving the separate habitat rescue, other food and mud variants,
  eating the creature for egg stock, combat, later chapter gates,
  save/reload and exact transport coefficients. These may occur
  between the credited fact and the final clean book view in W1.
- Potential scoped modules: the authored main rescue in this habitat,
  or one other food-dependent use followed through a matching note.

## Direct-play status

No personal Switch 2 installation or direct play. Nintendo's retail
listing and movement guide establish the platform, edition and action
vocabulary. A retail recording shows the apple at the carried creature's
mouth, the subsequent yellow bubble and the illustrated page entry.
Independent retail recordings show the same live discovery or the page
before leaving. Static frames were inspected in the background without
audio. The captures do not establish the binary revision, controller
preset, exact feed collision or sprint threshold, bubble lifetime or
whether an interrupted session preserves an unbanked entry.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| YMB-001 | Nintendo released the English commercial Switch 2 game on May 21, 2026. The bounded trace takes place in the Wildwoods Glubbit Habitat. | Observation | Corroborated | High | P1, P2, W1 45:31–47:05, W2 57:36–59:00 |
| YMB-002 | Tail Flick moves a reachable creature onto Yoshi's back. Running with a Glubbit can make it emit multiple bubbles along the route while still carried. | Observation | Corroborated | High | P2, P3, W1 46:50–47:30, W2 58:40–59:10 |
| YMB-003 | A normal Glubbit bubble rises and can enclose a contacting body, lifting it. Cyan ordinary bubbles are visible before the apple treatment, including with the earlier carried creature. | Observation | Corroborated | High | P3, W1 46:53–47:24 and 47:56–47:59, W2 59:00–59:40 |
| YMB-004 | In W1 the carried creature meets an apple at the branch, changes from green to orange and emits a bigger yellow bubble. Earlier cyan bubbles remain independently visible. The book notices the size and colour change. | Observation | Corroborated | High | W1 47:58–48:07, W2 59:45–60:15, W3 05:46–05:53 |
| YMB-005 | The game registers the food effect as a distinct one-star fact about the creature. Its live notice does not settle the habitat's separate goal. The same illustrated result is readable in the book during the visit and after the return. | Observation | Corroborated | High | P1, P2, W1 48:04–48:12 and 54:25–54:29, W2 69:39–69:46, W3 05:50–05:55 |
| YMB-006 | The exact software build, bubble emission cadence and internal persistence across load were not measured. Nintendo records later fixes, including demo-save import and an Index-page issue. | Observation | Direct | High | P4, limits of W1–W3 |

## Basic data

- Release / origin: Nintendo's 2026 Switch 2 commercial game.
  This analysis covers one solo creature experiment.
- Families: FAM-003 for changing what a carried source produces
  through a local reagent; FAM-007 for deliberately generating and
  intercepting buoyant objects; FAM-012 for turning an enacted result
  into inspectable creature knowledge.
- P1: [Nintendo US retail product](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/).
  Platform, English availability, release date and the experiment loop.
- P2: [Official Play Nintendo guide](https://play.nintendo.com/news-tips/tips-tricks/yoshi-and-the-mysterious-book-tips-tricks/).
  Actions, Tail Flick back carry and fact recording through interaction.
- P3: [Nintendo's creature-discovery notes](https://www.nintendo.com/en-ca/whatsnew/crack-open-the-latest-trailer-for-yoshis-next-adventure/)
  and [movement guide](https://www.nintendo.com/us/whatsnew/crack-open-yoshis-next-adventure/).
  The example supplies the suggested name. The movement guide
  distinguishes Tail Flick from running with a passenger.
- P4: [Nintendo software update history](https://www.nintendo.com/en-gb/Support/Purchases-Subscriptions/Games/How-to-Update-Yoshi-and-the-Mysterious-Book-3118426.html).
  Documents post-release changes and distinguishes full retail saves
  from the demo. No exact capture build is inferred from upload date.
- W1: [RetroArchive, recorded Switch 2 Wildwoods run](https://www.youtube.com/watch?v=2k49e3eaghk&t=2878s).
  Glubbit entry begins at 45:31. Frame inspection covers the ordinary
  bubbles, apple branch and yellow emission, then the entry at 54:25–54:29.
- W2: [BeardBear, independent Switch 2 Wildwoods run](https://www.youtube.com/watch?v=DOjvrrlx-p0&t=4183s).
  Enters at 57:36, shows the new bubble by 60:10 and displays the apple
  entry with Check Pages before resuming the habitat at about 70:01.
- W3: [Derrek's Gaming, Glubbit Habitat reference](https://www.youtube.com/watch?v=8XciKJtP1OU&t=350s).
  The live discovery caption is visible at roughly 05:51.
- Claim IDs: YMB-001–YMB-006.

### Reproducible route evidence

1. Enter Glubbit Habitat in Wildwoods and reach its first accessible
   green bubble-blower. Use Tail Flick nearby and take the creature
   onto Yoshi's back. Move left or right while carrying it. Its ordinary
   cyan bubbles rise, and Yoshi can intercept a bubble after it is loose.
   W1 shows the baseline and an initial lift at 46:50–47:24.
2. Bring a carried green Glubbit to the red apple branch below the stone
   ledge. Rise through the reachable fruit. W1 at 47:59–48:00 shows a
   red fruit at the passenger's mouth as the pair descend past the
   branch. Its colour has changed by 48:01.
3. Continue moving right. W1 shows the large yellow emission at
   48:02–48:04 alongside still-separate cyan bubbles around the route.
   The local discovery placard and the book's comment follow. W3
   independently shows the caption for the apple result near 05:51
   while ordinary movement continues.
4. Inspect Check Pages, then turn to the recorded apple result if
   needed. W2 at 69:44–69:45 shows the apple, orange creature, big
   bubble and single star, before the run resumes in the habitat.
   W1 at 54:25–54:29 shows the same illustrated one-star result after
   the group of later discoveries and the return to the book.

## Mechanical decomposition

### Action Genes

- ACT-008: steer and jump Yoshi along the local shelves and toward
  the apple branch. YMB-002–YMB-004.
- ACT-894: put the reachable live creature onto the moving actor's
  back so it can be brought to a new interaction. YMB-002, YMB-004.

### System Behaviour Genes

- SYS-1922: sustained movement causes the retained passenger to
  emit separate field objects without throwing the passenger. YMB-002.
- SYS-1923: accepted food changes the producer's state and subsequent
  bubble output. Ordinary bubbles already emitted are unchanged. YMB-003,
  YMB-004.
- SYS-1924: an enacted experimental effect adds a discrete discovery to
  the creature's record. Reading the record reveals what has already
  been registered. YMB-004, YMB-005.
- SYS-1925: an untethered rising bubble catches a compatible contact
  and raises it with the bubble. YMB-003.

### Constraint Genes

- None added. Reach, food identity and compatibility are inputs to
  the carry, feeding and bubble rules. No second independent budget,
  quota or hard time limit is needed for the selected fact.

### Information Genes

- INF-618: the experiment produces immediate feedback and a readable
  retained entry identified by creature and property. The latter can
  be checked independently of the visible bubble. YMB-004, YMB-005.

### Objective Genes

- OBJ-353: elicit a previously unrecorded creature property and obtain
  its evidenced discovery entry. The scoped apple fact does not
  require the separately labelled rescue. YMB-004, YMB-005.

### Time Genes

- TIM-003: choose motion and intercept contacts as emitted bubbles
  rise independently. The opportunity advances in real time without
  an overall deadline for the discovery. YMB-002, YMB-003.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Reachable green Glubbit with no passenger on Yoshi | Flick the tail toward it | Creature moves onto Yoshi's back and stays there through ordinary locomotion | YMB-002 |
| Green passenger and room to run | Continue moving in one direction | Live release of ordinary rising cyan bubbles while the creature remains carried | YMB-002, YMB-003 |
| Ordinary bubble rises toward a compatible body | Intersect the bubble | Bubble encloses and lifts the body | YMB-003 |
| Green passenger carried up to the branch | Let it reach and eat a red apple | Orange passenger and larger yellow output upon continued movement | YMB-004 |
| Qualifying output while the apple fact is new | Watch the book's response and keep playing | Immediate discovery notice while the expedition remains playable | YMB-004, YMB-005 |
| The transient notice has gone | Read the creature's pages | A separate illustrated, one-star apple entry is readable | YMB-005 |

## Strategic and experiential structure

Carry determines where the creature can interact. Motion after the feed
turns an invisible rule into a visible comparison with the ordinary
cyan output. Intercepting an old or new bubble is a spatial decision
under live movement. The book preserves the experimental result after
the individual output drifts off screen, so a player can distinguish
observing a larger bubble from confirming that the fact was recorded.

## Replay and variation

Both long captures record the apple fact at different times relative to
other small findings. Other incidental discoveries in one recording
are outside this experiment. Source material does not establish a
required duration of the run or a maximum count per bubble. No replay
reward or persistence across a software restart was tested.

## Adjacent systems and history

The Nintendo guide treats running, eating and Tail Flick as separate
actions. The scoped experiment uses the carried creature's eating
reaction. Yoshi's own swallow-to-egg interaction and the later rescue
objective are separate investigations.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-894 | Local movement and live back carry |
| System Behaviour | SYS-1922, SYS-1923, SYS-1924, SYS-1925 | Passenger emission, food-conditioned output, experiential registration and buoyant contact |
| Constraint | None | Compatibility belongs to the causal rules |
| Information | INF-618 | Immediate and retained creature-property feedback |
| Objective | OBJ-353 | Prove one creature property and verify its accepted record |
| Time | TIM-003 | Act while emitted bubbles rise |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `670` (`GAME-0001`–`GAME-0670`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 12 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Uncharted 2: Among Thieves (GAME-0391)](uncharted-2-among-thieves.md) | ACT-008, TIM-003 | Both steer an avatar and commit movement while a present opportunity changes in real time. Uncharted 2 uses the bounded collapsing-train escape to reach the authored safe route. Yoshi uses sustained motion with a live passenger, modifies the emitted bubble with food and validates a written discovery. | Near, `0.166667` |

## Taxonomy impact

The new boundaries separate transport of a living source, triggering
its emission, changing its output, interception of the result and
acquiring a recorded fact. The distinction between registering the
fact, reading its feedback and achieving the experiment is kept
separate across system, information and objective genes. Existing
local movement and live timing remain unchanged.

## Negative results

- A green Glubbit on the back still produces ordinary cyan bubbles.
  Back carry alone does not make a yellow bubble.
- The new orange state alters subsequent emission. Ordinary cyan
  bubbles are simultaneously visible and are not recoloured by it.
- The one-star note does not settle the separate habitat rescue.
  During W2 the page is accessible before the expedition ends.
- The selected trace gives no basis for claiming persistence across
  a restart, a precise collision threshold or required complete
  discovery and flower coverage.

## Delta summary

Nine genes, seven newly admitted and two reused. One optional,
verified apple discovery in the commercial Switch 2 rules.

## New facts

- The same carried source produces larger yellow bubbles after a
  reachable apple and sustained movement.
- The interface preserves that particular food effect as a one-star
  creature entry. Other nearby observations have distinct records.

## Principles and design implications

An initially ordinary effect gives the player a direct comparator
for a modified effect. The local notice ties the stronger output
to its cause, and the persistent entry lets the player confirm it
without refinding the moving bubble.

## Puzzle or game generation potential

Let the player carry a live source along a short route. Place one
reachable reagent on an optional branch and make untreated output
available for comparison. Tie the tested change to a separate recorded
fact with a legible result.

## New genes

- ACT-894
- INF-618
- OBJ-353
- SYS-1922
- SYS-1923
- SYS-1924
- SYS-1925

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_417](../../../research/taxonomy-changes/TAXONOMY_CHANGE_417.md).

## New questions

- Does the discovery survive an abandoned visit or software restart?
- What are the exact sprint and bubble interception windows?
- Which output modifiers can coexist and which replace one another?

## Next recommended game

Devil's Crush on TurboGrafx-16. Follow one bonus-table entry through
its result and the return to the ordinary table.

## Why this game

It separates creating a physical effect from changing the next
emission and from crediting the resulting authored fact.
