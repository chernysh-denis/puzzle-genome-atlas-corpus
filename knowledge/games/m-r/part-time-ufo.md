---
game_id: GAME-0703
slug: part-time-ufo
game_title: "Part Time UFO"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
  system:
    - SYS-036
    - SYS-1981
    - SYS-1982
  constraint:
    - CON-556
  information:
    - INF-641
  objective:
    - OBJ-369
  time:
    - TIM-003
---

# Game: Part Time UFO

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Hover over a crate, grip it with a retractable claw and lower it onto
the truck. The first farm job accepts a plain delivery and separately
pays for optional loading work and the finish time.

## Analysis scope

- Version / ruleset: the English commercial Nintendo Switch eShop
  base game developed by HAL Laboratory and released by Nintendo on
  October 28, 2020. The launch-day and November 2020 captures are
  attributed to Switch, show the English Joy-Con tutorial and start
  from the farm opening. Their installed patches are unavailable.
- Structured analysis target: PLAT-NINTENDO-SWITCH in
  [platform coverage](../../platforms/games.json).
- Entry: the solo opening farm job after the farmer asks for help,
  with the fixed truck bed, two required orange crates and loose
  optional cargo. Use the ordinary starting claw and finish with the
  first displayed `Your Pay` settlement.
- Primary decision loop: fly above the cargo and leave room for the
  claw to lower. Grip, carry and release individual objects, letting
  the bed and its load settle. Decide whether to spend time arranging
  optional cargo and orienting boxes before the final required crate.
- Positive terminal: both marked crates count as loaded, the job
  reports completion, and the pay screen resolves the time and medal
  entries. Optional cargo and medals can be missing at ordinary clear.
- Included: flying, grip eligibility, load motion, marked cargo count,
  progress-linked time credit, the live reward clock and separate
  completion/pay outcomes for the first job.
- Excluded: later jobs and harder variants, co-op, costumes, shop,
  Tower of Infinity, Treasure Island, mobile versions, save state,
  exact collision and timing implementation, and outcomes after
  exhausting the bonus clock other than the displayed tutorial rule.
- Potential scoped module: replay Farm 1 after selecting a costume
  and measure which controls, carry limits or results change.
- Direct-play status: no personal Nintendo Switch session or input
  telemetry. The Nintendo and HAL pages identify the released product.
  Two independent launch-window Switch captures were inspected as
  short silent frame sequences. Neither authenticates the exact patch.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PTU-001 | HAL Laboratory and Nintendo released this Nintendo Switch edition on October 28, 2020. Nintendo lists English and distinguishes optional local co-op from the solo job. | Confirmed | Direct | High | P1, P2, P3 |
| PTU-002 | The introductory Joy-Con panel shows flight and lowering the claw from above. It forbids deploying the claw when the UFO is too close to a grabbable object and explains separate release. Transported and dropped objects can tilt or move. | Observation | Corroborated | High | P3; W1 0:45–1:08, 1:28–1:35; W2 0:44–0:59, 1:29–1:34 |
| PTU-003 | The tutorial identifies blinking objects as required cargo. The counter starts at two, falls to one after the first orange crate is accepted and stays at one when the green basket is credited. | Observation | Corroborated | High | W1 1:09–1:18, 1:34–1:50; W2 1:04–1:10, 1:34–1:35, 1:58–2:01 |
| PTU-004 | First crate acceptance displays a clock with +20 and credits the existing ticking timer. The bonus clock starts at 100 and can exceed that initial display. Tutorial text says that finishing late loses the time bonus. | Observation | Corroborated | High | W1 1:18–1:40; W2 1:11–1:39 |
| PTU-005 | The second marked crate changes the remaining count to zero and freezes the visible timer. A later completion cue precedes the itemized pay screen. The capture with sideways cargo and one uncollected large orange clears. | Observation | Corroborated | High | P3; W1 2:48–3:01; W2 2:22–2:34 |
| PTU-006 | An observed three-medal result pays 2,490, including 190 for 38 time units. Another ordinary clear pays 1,390, including 290 for 58 time units and only the clock medal. The basket and crate-configuration medals are separate. | Observation | Corroborated | High | P1, P3; W1 3:00–3:09; W2 2:34–2:42 |
| PTU-007 | The basket and crate configurations earn their own pictured credits. The exact handling of tipped or displaced accepted crates before final closure is untested. | Observation | Corroborated | Medium | W1 2:48–3:09; W2 2:23–2:42; S1, S2 |

## Basic data

- Release / origin: HAL Laboratory, Nintendo eShop, Nintendo Switch,
  October 2020. The first Farm 1 single-player engagement only.
- Mechanical family: FAM-007. Carry and dispose of individual loads
  that swing in transit and physically settle on supports at release.
- P1: [Nintendo eShop product](https://www.nintendo.com/us/store/products/part-time-ufo-switch/).
  Identifies the English release, extendable claw, arrangement, jobs
  and separate timed and pictured objectives.
- P2: [HAL Laboratory's Switch release record](https://www.hallab.co.jp/eng/works/detail/003484/).
  Identifies the Switch edition, developer involvement and release date.
- P3: [Nintendo's Switch mechanics overview](https://www.nintendo.com/jp/switch/azd8a/index.html).
  The Japanese publisher diagrams separate grip, transport, stacking,
  completion on the required load and three extra pay tasks.
- W1: [AbdallahSmash Switch walkthrough, Farm 1](https://www.youtube.com/watch?v=VUDmnuL1CHA&t=17s).
  The November 10, 2020 recording shows three credited medals and its
  final result. The opening shows the Switch controller tutorial.
- W2: [Super Nintendad Switch gameplay](https://www.youtube.com/watch?v=Kbf8UECHYZU&t=36s).
  The October 28, 2020 Switch launch footage reproduces the same start
  and records a one-medal ordinary clear.
- S1: [SuperParent Switch launch hands-on](https://www.superparent.com/part-time-ufo-on-switch-a-superparent-first-look/).
  Its independent play describes the physically swinging load and the
  optional basket, orientation and timed credits.
- S2: [Gamepur's Switch medal list](https://www.gamepur.com/guides/how-to-earn-every-medal-in-part-time-ufo).
  Its launch-day play lists upright arrow-marked boxes and the basket
  with small fruit supporting the large fruit as the extra conditions.
- Claim IDs: PTU-001–PTU-007.

### Reproducible fixture evidence

1. Let the introduction reach the help request and the first load
   instruction. Observe the two required objects counter with 100
   time units before active work.
2. Fly over a required orange crate while leaving vertical clearance.
   Lower the jaws, carry the load to the open bed and release. Check
   the crate as it rotates and comes into the receiver. In W2 the
   counter moves from two at 1:34 to one near 1:35. A clock icon with
   +20 appears beside the delivered crate. The timer is 087 at 1:35
   and 104 at 1:38, while work continues.
3. Move optional cargo before the second crate. In W2 the green basket
   arrives around 1:59 while the required count remains one. W1 places
   two small fruits in the basket before adding the large fruit. In
   W2 the large orange seen by the final crate is still outside the
   truck during the last pickup. The first crate remains sideways.
4. Place the second required crate into the truck. W1 changes from one
   remaining around 2:49 to zero with 038 at 2:50. W2 changes from one
   with 059 at 2:23 to zero with 058 at 2:24. Both then show a separate
   `Good Work!` cue before the pay panel.
5. Observe the complete settlement. W1 displays base pay 1,200, time
   190, medal values 500 + 500 + 100 and total 2,490 at 3:04. W2 displays
   base pay 1,000, time 290, only the 100 clock medal and total 1,390
   at 2:39. The checks permit two materially distinct results.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the hovering carrier to approach cargo and place it
  over the truck.
- ACT-048: take one object through the claw, move it while held, and
  release it back into the physical scene.

### System Behaviour Genes

- SYS-036: a suspended box can swing; after release, objects keep
  moving under contact and gravity until supported.
- SYS-1981: initial nonterminal delivery of required cargo credits
  time to the remaining clock while work continues.
- SYS-1982: the cleared job pays its delivery amount, retained time
  and independently credited optional staging or timing medals.

### Constraint Genes

- CON-556: claw use depends on spatial eligibility, with the tutorial
  specifically warning against being too close to a grabbable object.

### Information Genes

- INF-641: blinking cargo says what counts, while the remaining count
  and separate clock show completion progress and timed reward state.

### Objective Genes

- OBJ-369: finish the fixed receiver's quota of marked movable cargo.
  Additional cargo and its configuration can alter pay and medals.

### Time Genes

- TIM-003: while the live clock advances, adjust cargo and choose
  whether to do optional work before committing the last required load.

### Parameters

Required cargo count, truck-bed acceptance, claw clearance and held
geometry, initial time, time credit, optional contents and orientation,
time multiplier and medal values are fixture parameters.

## Reproducible transitions

| Entry state | Input | Expected next state | Evidence |
| --- | --- | --- | --- |
| Truck empty and two required crates visible | Hover above the first with room to lower the claw and grip | One physical crate follows the carrier and can swing | PTU-002 |
| First crate held over bed, two more required | Release the crate into the receiving bed | First crate is credited; one more remains and time is added | PTU-003–PTU-004 |
| One required crate remains and optional cargo is available | Place optional cargo before the final box | Pay or configuration can improve; ordinary goal count remains one | PTU-003, PTU-006–PTU-007 |
| One required crate remains while the bonus clock advances | Release and settle the final crate on the bed | Remaining count reaches zero and the timer freezes | PTU-005 |
| Job clears with a credited load and frozen time | Let the result settle | Delivery pay, time pay and optional medals total separately | PTU-006 |

## Strategic and experiential structure

The second required crate acts as a commitment. Load and arrange
optional cargo first if the medals matter. The alternative is to
stop early with the required cargo already present and earn more
remaining-time pay. A tilted load can still meet the ordinary
receiver quota, as W2 shows.

## Replay and variation

One witness prioritizes a complete fruit basket and upright crates.
The other puts fewer optional items in the receiver and clears faster
with the first crate turned. Both finish on the same two-crate goal,
with different pay and medal outcomes. A zero-clock run and a later
retry under the harder variant were not performed.

## Adjacent systems and history

HAL's original mobile edition is separate from the scoped eShop build.
Nintendo's Switch release adds Joy-Con controls, local co-op and
console-specific features. Co-op, costumes, replay unlocks and other
jobs use distinct states beyond the first pay settlement.

## Normalised genome

- Action: ACT-008, ACT-048.
- System Behaviour: SYS-036, SYS-1981, SYS-1982.
- Constraint: CON-556.
- Information: INF-641.
- Objective: OBJ-369.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `702` (`GAME-0001`–`GAME-0702`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`4 / 13 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Human: Fall Flat (GAME-0112)](../g-l/human-fall-flat.md) | ACT-008, ACT-048, SYS-036, TIM-003 | Both move an agent carrying a rigid object whose position changes under gravity and contact. Human: Fall Flat uses the crate as a foothold to climb to an exit. The farm job uses a suspended claw and closes on two marked crates at the same receiver, with optional loading, orientation and time affecting pay. | Near, `0.307692`. |

## Taxonomy impact

Reuse agent navigation, portable-object acquisition and release,
continuous body mechanics, situational tool eligibility and live
input. Admit a quota of marked cargo distinct from optional freight,
the independent visibility of progress and bonus time, the
nonterminal time credit and the itemized farm pay settlement.

## Negative results

- The optional green basket can be credited without advancing the
  orange-crate quota.
- One missing fruit and an incorrectly oriented crate do not prevent
  the demonstrated ordinary clear. The reduced result receives the
  clock medal alone.
- The tutorial explains losing the time bonus when late. Neither
  witness directly tests an expired timer or a late recovery.

## Delta summary

The scoped task uses one tool to move physically independent
objects, separating ordinary delivery from a higher-paid configuration.

## New facts

- The first required receipt advances the count and adds time without
  resetting the displayed remainder.
- The last required crate stops active reward time before the result
  animates.
- The two witnessed clear states keep their own delivery, remaining-time
  and medal contributions.

## Principles and design implications

Make mandatory objects and the stopping condition visible. Put optional
spatial work and limited-time pay in tension. A player can choose whether
to arrange fragile cargo or end the attempt by delivering the last crate.

## Puzzle or game generation potential

Give a floating two-jaw carrier a fixed receiver and a small quota of
marked objects. Use one interim delivery to credit more reward time.
Allow optional objects and poses to affect an itemized result. Validate
both an ordinary early finish and a more valuable balanced load.

## New genes

- INF-641
- OBJ-369
- SYS-1981
- SYS-1982

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 449](../../../research/taxonomy-changes/TAXONOMY_CHANGE_449.md).

## New questions

- What happens to the count when an already credited crate bounces out?
- Does the exact claw clearance change under any later costume?

## Next recommended game

Continue Selection 061 with Alien Crush on the North American TurboGrafx-16
HuCard. Observe one controlled main-table ball through a bounded outcome.

## Why this game

A short task gives visible examples of optional cargo, the irreversible
finish and a score that differs even when the completion predicate is equal.
