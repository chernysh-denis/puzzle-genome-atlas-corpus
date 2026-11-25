---
game_id: GAME-0723
slug: holedown
game_title: "holedown"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-939
  system:
    - SYS-2021
    - SYS-2022
    - SYS-2023
    - SYS-2024
  constraint:
    - CON-020
  information:
    - INF-002
    - INF-654
  objective: []
  time: []
---

# Game: holedown — first Asteroid dig and surface return

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first Asteroid, ball counts and upgrade prices are scoped instances.

## Analysis scope

- Version / ruleset: commercial English Android Google Play base game,
  launched 26 July 2018 according to grapefrukt games. The original
  Android reports bound the fixture. The current listing still identifies
  the same product. Exact Android builds and devices are unverified.
- Structured analysis target: `PLAT-ANDROID`. Start a new solo Asteroid
  dig with its starting allowance. Aim and launch through the shot-limited
  opening shaft. Stop at the first settled shot-exhaustion result and the
  subsequent surface upgrade menu, before buying an upgrade or launching
  a second dig.
- Primary decision loop: read the numbered blocks and the available
  angle. Release one volley, observe the rebounds and the supports that
  disappear, then aim again when the remaining shaft has advanced.
  Decide whether to spend a launch on a difficult fixed block, attack
  a lower support or seek crystals before returning to the surface.
- Included: touch aim, release, wall and block contacts, block resistance,
  support loss and fixed blocks, shift after the last ball, depth and shot
  state, shot-exhaustion settlement and one accessible surface offer.
- Excluded: exact physics and launch-point assignment, crystal contact
  and cargo-limit arbitration, upper-boundary failure reproduction,
  successful core destruction, completed purchases and persistence
  across app restarts, later rocks, endless and other-platform co-op.
- Direct-play status: no personal Android session or app installation.
  Developer descriptions, contemporary Android hands-on reporting and two
  Android-labelled recordings support the scoped rules. Background silent
  frames were reviewed. No executable or input trace was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| HD-001 | grapefrukt games released the paid game for Android on 26 July 2018. The Google Play listing identifies the Android package and developer. | Observation | Corroborated | High | P1, P2, S1 |
| HD-002 | Dragging shows a green aim line. Releasing launches the allocated balls from the upper part of the playfield along the chosen opening direction. | Observation | Corroborated | High | S1, W1 00:35–00:45, W2 00:42–00:52 and 01:06–01:10 |
| HD-003 | Contacts with side walls and block faces redirect the balls. Counted impacts reduce the displayed number. A block can survive a hit or disappear when its remaining resistance is exhausted. | Observation | Corroborated | High | P1, S1, W1 00:35–00:45 and 01:34–01:42 |
| HD-004 | Ordinary blocks can fall away when their lower support breaks. Blocks marked as fixed do not depend on that support and must be cleared by impacts. | Observation | Corroborated | High | P1, S1, W1 01:34–01:42 and 02:17–02:31, W3 00:32–00:39 |
| HD-005 | One release spends one shot independently of its payload. After the balls finish travelling, the shaft shifts upward and the next visible slice can enter. The next procedural slice is not previewed. | Observation | Corroborated | High | P1, P2, S1, W1 01:31–01:36, W2 02:20–02:34 |
| HD-006 | After the last allowed shot resolves without completion, the run ends with a distinct shot-exhaustion result. W1 shows 33 m and 20 shots. W3 separately displays 32 m and two collected crystals. | Observation | Corroborated | High | P1, W1 02:23–02:40, W2 02:54–02:57, W3 01:50–01:57 |
| HD-007 | A surface return makes collected crystals available for offered upgrades. W1 shows the shot allowance at 20 with an affordable offer for 30 shots priced at two crystals. No purchase of that offer was verified. | Observation | Corroborated | High | P1, P2, S1, W1 02:35–02:48, W3 01:52–01:57 |

## Basic data

- Release / origin: Martin Jonasson at grapefrukt games. P1 gives
  the simultaneous original Android and iOS release date; the platform
  chosen here is the Android commercial product identified by P2.
- Platform or physical form: portrait-oriented, touch-controlled
  solo mobile game. The version in the co-op trailer on the press
  site is outside the scope.
- Mechanical family: `FAM-007`. Aim, wall collisions, different
  block faces and lost support determine the effect of one launch.
- Primary sources accessed 2026-11-25:
  - **P1:** [grapefrukt games press kit](https://presskit.grapefrukt.com/holedown/),
    developer, release date, procedural shaft, fixed blocks, limited shots
    and surface improvements.
  - **P2:** [official Google Play listing](https://play.google.com/store/apps/details?id=com.grapefrukt.games.bore),
    Android product and developer descriptions of the action and upgrades.
- Independent and recorded sources:
  - **S1:** [KickMyGeek July 2018 Android review](https://kickmygeek.com/test-jeu/android/holedown),
    direct Android observations and stills for touch aim, numbered
    resistance, wall-fixed blocks and clearance through support removal.
    Its current availability banner was not used to infer release status.
  - **W1:** [Android-attributed gameplay recording](https://www.youtube.com/watch?v=d5dD83lpKRA),
    aim and block contacts around 00:35–00:45, marked and ordinary blocks
    around 01:34–01:42, exhaustion at 02:31 and upgrade menu around
    02:43–02:48. Cropped capture excludes parts of the HUD.
  - **W2:** [All About Android hands-on](https://www.youtube.com/watch?v=qA5BWcaLkdg),
    Android product page, handheld touch input and repeated volleys
    from 00:34 through the exhaustion screen around 02:56.
  - **W3:** [Independent companion recording](https://www.youtube.com/watch?v=kPiEl9c8nWA),
    complementary full-field footage. The channel covers Android,
    but this clip does not identify the captured handset or operating
    system. Used for corroboration, with Android attribution grounded
    in S1, W1 and W2.
- Claim IDs: `HD-001`–`HD-007`. To reproduce the signature,
  record the launched ball count, remaining shots, counters on the
  impacted and supported blocks, depth and the first terminal screen.
  Then inspect the surface offers without purchasing one.

## Mechanical decomposition

### Action Genes

- New `ACT-939`: drag to aim and release the current allocation
  of balls on one initial launch line (`HD-002`, `HD-005`).

### System Behaviour Genes

- New `SYS-2021`: balls rebound and reduce finite resistance each
  time a counted block contact occurs (`HD-003`).
- New `SYS-2022`: removing a supporting block clears dependent
  ordinary blocks while wall-fixed ones require direct hits (`HD-004`).
- New `SYS-2023`: the shaft advances once the committed volley
  settles and deeper geometry can become visible (`HD-005`).
- New `SYS-2024`: settlement preserves eligible crystals for
  priced improvements on the surface (`HD-006`, `HD-007`).

### Constraint Genes

- Reuse `CON-020`: the finite shot count reaches a losing terminal
  after the last volley settles without completion (`HD-005`, `HD-006`).

### Information Genes

- Reuse `INF-002`: the procedural slice entering after a launch
  is not shown in advance (`HD-005`).
- New `INF-654`: the live aim line, block numbers and separate
  shot and ball counters inform the choice of a volley
  (`HD-002`, `HD-003`, `HD-005`).

### Objective Genes

No separate new objective gene. Reaching and destroying the
planetary core is the described broader goal, beyond the witnessed
terminal used here.

### Time Genes

No separate time gene. The decisive phase boundary is already
captured by the volley-settlement rule in `SYS-2023`.

## Formal state and transitions

The state tracks the depth, current shaft slice, block positions
and remaining hits, ordinary versus fixed support, current aim and
launcher availability, active balls, remaining shots and carried
crystals. Launch spends one shot and commits the payload to the
chosen direction. Contacts update ball directions, block numbers
and support. Ending the last flight updates the shaft once, or
settles the attempt at terminal. The surface retains crystals as
a separate resource for offered changes to later attempts.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Idle with shots available | Drag and release an aimed shot | The current allocation of balls launches from the top | HD-002, HD-005 |
| A ball reaches a vertical wall or a numbered block | Resolve its contact | The ball redirects and a block contact reduces resistance | HD-003 |
| An ordinary upper block still has hit points | Break the lower support | The dependent block can fall away while a fixed block remains | HD-004 |
| Balls are live and blocks remain | Wait for the last ball to finish | The shaft moves upward and a deeper slice can enter | HD-005 |
| The final allowed volley ends before the goal | Observe the result and return to surface | Shot exhaustion closes the dig and collected crystals can enable an offer | HD-006, HD-007 |

## Strategic and experiential structure

An early aim can go through a side gap and reach a lower support
that is expensive to hit straight on. Compare the shape of the
remaining group, its marked fixed blocks and the shot budget.
The distinct ball and shot counts keep the size of the next
volley separate from the number of remaining decisions.

## Replay and variation

The exact rows, final depths and earned crystals differ across
recordings. The developer identifies the layouts as procedural.
The invariant being compared is the route from a visible slice,
through one committed volley, to changed geometry or settlement.

## Adjacent systems and history

The press kit also describes cores, deeper planets, a larger
crystal capacity and later platform releases with co-op.
The scoped first return shows an offer, not the effect of a purchase.

## Normalised genome

- Action: ACT-939.
- System Behaviour: SYS-2021, SYS-2022, SYS-2023, SYS-2024.
- Constraint: CON-020.
- Information: INF-002, INF-654.
- Objective: none.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `722` (`GAME-0001`–`GAME-0722`).
- Exact genome matches: none.
- Tied near matches: `GAME-0009` — Royal Match (`2 / 22 = 0.090909`); `GAME-0109` — Candy Crush Saga (`2 / 22 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Royal Match (GAME-0009)](../m-r/royal-match.md) | CON-020, INF-002 | Both spend actions under a terminal limit and reveal unknown future geometry after resolution. Royal Match commits discrete adjacent swaps against target quantities and refills cells. Holedown spends an aimed volley, counts rebounds and removes vulnerable supports before the next slice enters. | Near, `0.090909`. |
| [Candy Crush Saga (GAME-0109)](../a-f/candy-crush-saga.md) | CON-020, INF-002 | Both ration moves around an unknown future slice or refill. Candy Crush Saga tests matches, cascades and objective orders after a swap. Holedown uses an angle, repeated counted impacts and the loss of a lower support. | Near, `0.090909`. |

## Taxonomy impact

The current payload is not a finite stock of one acquired
projectile per shot. The block result is also distinct from
a generic ballistic cascade: resistance can survive a strike,
ordinary blocks can clear through support loss, and wall-fixed
blocks persist independently. The visible aim and resource
counters are separate from actual physical resolution.

## Negative results

- A positive remaining hit count does not guarantee an ordinary
  block survives the loss of its support.
- A marked fixed block does not clear simply because
  neighbouring blocks disappear.
- A ball rebound does not require another shot.
- A visible and affordable upgrade does not prove a purchase.
- The two recorded exhaustion screens do not establish a
  fixed depth or crystal count for the first run.

## Delta summary

Record a limited-shot opening shaft with repeated impacts,
support-dependent clearance, advancement after a volley and a
retained resource after failure.

## New facts

- One chosen line controls the starting angle of the entire volley.
- Choosing a support can remove blocks that still show resistance.
- Shot exhaustion can leave usable crystals for later attempts.

## Principles and design implications

Distinguish the intended angle, the live contact outcome
and the opening created by a removed support. A finite launch
budget makes the number and arrangement of supports consequential.

## Puzzle or game generation potential

Use a bounded vertical shaft with side rebounds, visible
resistance and a small count of launches. Provide both fixed
and supported blocks so a bank shot can change the order in
which sections of the shaft become reachable.

## New genes

- ACT-939
- SYS-2021
- SYS-2022
- SYS-2023
- SYS-2024
- INF-654

## New combinations

None. No verified combination matched the scoped opening dig.

## Taxonomy changes

[Taxonomy Change 469](../../../research/taxonomy-changes/TAXONOMY_CHANGE_469.md).

## Next recommended game

Frequency on PlayStation 2 is the next Selection 063 unit.

## Why this game

Its first dig joins visible block resistance with positional
support, player-chosen rebounds and the value of a failed attempt.

## Review status

Reviewed 2026-11-25 for the commercial Android opening dig
through shot-exhaustion settlement and its surface follow-up.
