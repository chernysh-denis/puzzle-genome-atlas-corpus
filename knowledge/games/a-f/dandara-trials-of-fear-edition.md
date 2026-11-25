---
game_id: GAME-0738
slug: dandara-trials-of-fear-edition
game_title: "Dandara: Trials of Fear Edition"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-341
    - ACT-951
  system:
    - SYS-2049
    - SYS-2050
  constraint:
    - CON-907
  information:
    - INF-179
    - INF-666
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Dandara: Trials of Fear Edition — The Void to Crib of Creation

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The salt bands, orange target and doorway instantiate different
movement, shot and transition rules.

## Analysis scope

- Version / ruleset: English commercial Android Google Play app
  `com.rawfury.longhathouse.Dandara`, the Trials of Fear Edition
  ruleset published in March 2020 within the original title.
  Google Play identifies the Android app. The recorded touch
  presentation and exact Android build are separate evidence.
- Reproducible entry and exit: start an ordinary new game. Begin
  when the first `Leap` control is available in The Void. Take
  the first forward route across the salt bands, hit the orange
  target, reach the open wall doorway and enter Crib of Creation.
  Stop at the first controlled position inside that room.
- Primary decision loop: aim and release between valid footholds,
  use the new orientation to choose the next leap, reach a
  support with an upward shot to the target, then take the
  separately enabled exit.
- Included: touch leap and shot selection, support eligibility,
  preview and orientation, first target clearance and door entry.
  Excluded: exact aim tolerance and range coefficients, attack
  charge thresholds, later rooms, optional tutorial skip, added
  challenge areas, checkpoint economy, enemies, other editions
  and platform-specific performance.
- Direct-play status: no personal Android or emulator session.
  The publisher and Google Play identify the app, and Long Hat
  House dates this edition. The mobile recording verifies touch
  overlays and the first route but does not identify the host OS
  or installed build independently. An independent controller
  recording corroborates the main route and separate door.
  Only silent background frames were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DF-001 | The Google Play Android app distributes the commercial Trials of Fear Edition. Long Hat House dates the edition to March 2020, and the publisher describes support for touch and gamepad. | Observation | Corroborated | High | P1, P2, P3 |
| DF-002 | The initial movement sends the body between marked white salt surfaces by aimed touch leap. The landing is a supported stance, including on the underside of a horizontal band. | Observation | Corroborated | High | P1, W1 00:23–00:36, W2 01:25–01:36, S1 |
| DF-003 | A faint raw aim line and a brighter corrected guide can point along different directions while the character stays on its origin. The guide identifies an eligible landing before the leap is committed. | Observation | Corroborated | High | W1 00:24–00:32, W2 01:28–01:38, P4 |
| DF-004 | A committed leap visibly crosses intervening space and settles against the selected band. The next action starts relative to the receiving face. Ordinary landing requires eligible salt support rather than any wall. | Observation | Corroborated | High | W1 00:25–00:43, W2 01:28–01:43, S1, S2 |
| DF-005 | A separate held touch control aims and visibly prepares a shot at the orange target. From the last lower strip, releasing it sends the shot upward, destroys the target and makes the side doorway available. Dandara remains on the firing strip after the shot. | Observation | Corroborated | High | P4, W1 00:46–00:51, W2 01:54–01:57 |
| DF-006 | After the hit, a separate leap reaches the wall strip at the door. The doorway cue and crossing are distinct from the target hit. The successor room is labelled Crib of Creation in the English touch capture. | Observation | Corroborated | High | P4, W1 00:51–01:04, W2 01:57–02:08 |

## Basic data

- Release / origin: Long Hat House, Raw Fury, Android Google Play
  app `com.rawfury.longhathouse.Dandara`. Trials of Fear Edition
  is dated March 2020 by the developer. The analysis target is
  `PLAT-ANDROID`.
- Mechanical families: `FAM-017` for the ordered leap, target
  and doorway dependencies, and `FAM-007` for aiming and
  executing separate jumps between spatially qualified supports.
- Primary evidence checked 2026-11-25:
  - **P1:** [Google Play's official Android product](https://play.google.com/store/apps/details?hl=en_US&id=com.rawfury.longhathouse.Dandara).
    Identifies the package, publisher, released edition and
    touchscreen capability.
  - **P2:** [Long Hat House's edition page](https://www.longhathouse.com/games/dandara-tof/).
    Gives March 2020 and native touch and gamepad support.
  - **P3:** [Raw Fury's game page](https://rawfury.com/games/dandara/).
    Distinguishes the original game from the additional edition
    content and describes travel across different orientations.
  - **P4:** [Developer update notes on the companion App Store listing](https://apps.apple.com/us/app/dandara-trials-of-fear-edition/id1168013926).
    The 1.2.0 notes name The Void and the first target opening the
    door. Earlier notes document the landing aim helper. The
    platform-specific version number is not assigned to Android.
  - **W1:** [andro-games' English touch recording](https://www.youtube.com/watch?v=yGu2p1nsiUQ&t=23s).
    At 00:24–00:32 the light aim guide, upper landing and return
    are visible. Around 00:47–00:50 the Shoot direction rises
    and the gold target disappears. Around 00:52–01:04 the
    wall landing, door transition and room name appear.
  - **W2:** [Ishigami's Trials of Fear playthrough](https://www.youtube.com/watch?v=QeApYK58yJw&t=85s).
    At 01:25–01:43, the controller and French presentation
    establish the same supports. The target remains while the
    avatar repositions at 01:43–01:55. Its removal is followed
    by a separate doorway approach and room transition by 02:03.
- Independent descriptions:
  - **S1:** [Published research on Dandara's traversal](https://discovery.ucl.ac.uk/id/eprint/10225134/1/Folkloresque-GAME-accepted-final.pdf).
    Describes jumps between white salt edges as the ordinary route.
  - **S2:** [Android Central on the released Android game](https://www.androidcentral.com/dandara-android-game-week).
    Distinguishes the Android touch input and controller option.
- Claim IDs: DF-001–DF-006.

## Mechanical decomposition

### Action Genes

- New `ACT-951`: aim and release one direct leap from a current foothold to an accepted support (DF-002–DF-004).
- Reuse `ACT-161`: aim the separate shot from the final floor band and hit the orange target (DF-005).
- Reuse `ACT-341`: use the now-eligible doorway after reaching its wall-side interaction (DF-006).

### System Behaviour Genes

- New `SYS-2049`: attach and reorient the body at the receiving surface after visible travel (DF-002, DF-004, DF-006).
- New `SYS-2050`: a projectile hit on a distinct target unlocks the linked doorway while leaving entry as a separate step (DF-005, DF-006).

### Constraint Genes

- New `CON-907`: ordinary leap destinations are reachable marked support, with the shot target and bare masonry outside that set (DF-002–DF-004).

### Information Genes

- Reuse `INF-179`: the visible field differentiates footholds, the target and door geometry (DF-002, DF-005, DF-006).
- New `INF-666`: correct the shown direction to the accepted landing point separately from the current aim input (DF-003).

### Objective Genes

- Reuse `OBJ-026`: reach and cross the designated doorway after enabling its route (DF-005, DF-006).

### Time Genes

- Reuse `TIM-003`: the held shot visibly prepares in live time while its aiming input is available; after release, flight advances to contact (DF-005).

## Formal state and transitions

Track the current support and its orientation, the aim vector,
accepted landing point, traversal phase, target state and linked
door state. The release commits a leap through the indicated
space and changes the supported origin on contact. A shot is
another action from the current support. The first target hit
latches the door available. Arrival at that door and its use
perform the transition separately.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Attached to the first lower salt band | Aim at the higher salt band | Accepted endpoint guide appears before bodily movement | DF-002, DF-003 |
| Valid guide shown at a ceiling band | Release the leap control | Cross the gap and anchor upside down on the new support | DF-002, DF-004 |
| The orange target is intact above the final floor band | Leap to the lower strip and direct a shot up | Remove the target and enable the separate door, while staying on the firing strip | DF-005 |
| The side door is enabled | Take the wall-side leap and use the doorway | Cross and regain control in Crib of Creation | DF-006 |

## Strategic and experiential structure

The destination is selected in relation to visible support, so
the closest unmarked wall is not a substitute for a safe landing.
The same geometry sets the angle of the shot. Keep the upward
shot from the final low strip separate from the later move to
the doorway.

## Replay and variation

The mobile and controller traces use the same authored target
and distinct exit. Their exact aiming behavior and inputs can
differ. The controller trace takes extra repositioning before
firing. Neither trace licenses an inference about the current
Android package's timing, hardware or aim tolerances.

## Adjacent systems and history

The edition includes optional routes and a documented tutorial
skip. That route uses a different target after the first one;
this record stops inside the standard Crib of Creation arrival.
It does not admit later rooms, checkpoint rules or expanded
Trials areas.

## Normalised genome

- Action: ACT-161, ACT-341, ACT-951.
- System Behaviour: SYS-2049, SYS-2050.
- Constraint: CON-907.
- Information: INF-179, INF-666.
- Objective: OBJ-026.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `737` (`GAME-0001`–`GAME-0737`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-341, INF-179, OBJ-026, TIM-003 | Both use visible geometry, a prepared input and actual arrival at a route destination. Skate Story teaches an Ollie, tests it at four crests and opens a portal on the resulting objective credit. Dandara needs a reachable marked surface to settle each leap and opens its first doorway by hitting a separate target. | Near, `0.266667`. |

## Taxonomy impact

Separate the intended and accepted landing, the physical
attachment and the door's state. The target unlocks the route
but does not settle the player's arrival.

## Negative results

- The orange target is not an ordinary leap support.
- Aiming alone does not perform the leap.
- Destroying the first target leaves Dandara on the firing strip.
- Opening the door alone does not enter the successor room.

## Delta summary

Record the Void's marked-surface movement, a separately
addressed target and the first Crib of Creation handoff.

## New facts

- The landing guide can differ visibly from the raw aim line.
- The landing reorients the body after a visible leap.
- An upward shot and a subsequent door move serve different
  parts of the progress condition.

## Principles and design implications

Show the accepted movement endpoint early enough to support
the intended leap. Keep a distinct target and the exit state
separate so the player's last route decision remains legible.

## Puzzle or game generation potential

Build a short chain of eligible horizontal and vertical
supports, a target reachable from one separate firing position
and a linked exit. Check target hit, door availability and
actual crossing as separate transitions.

## New genes

- ACT-951
- CON-907
- INF-666
- SYS-2049
- SYS-2050

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 484](../../../research/taxonomy-changes/TAXONOMY_CHANGE_484.md).

## Next recommended game

Selection 064 ends at this unit. A new list awaits an explicit
maintainer instruction.

## Why this game

The surface that permits a leap also determines the next
firing origin. The first door makes it possible to distinguish
physical arrival from a progress flag in one short route.

## Review status

Reviewed 2026-11-25 for the released Google Play ruleset and
the bounded touch-controls witness described above.
