---
game_id: GAME-0730
slug: a-little-to-the-left
game_title: "A Little to the Left"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-947
  system:
    - SYS-2032
  constraint:
    - CON-904
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: A Little to the Left — The first bookshelf

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The nine books, their individual measurements and the awarded stars
are instances of the bounded puzzle.

## Analysis scope

- Version / ruleset: English Nintendo Switch commercial digital base
  game, UK eShop product `70010000051362`, released on November 9,
  2022. Use the ordinary story chapter Home Sweet Home and the
  first bookshelf, Chapter 1 puzzle 7. Exact installed patch and
  recording hardware are unverified.
- Reproducible entry and exit: select the first bookshelf after
  the previous paper stack is solved. With the book puzzle active,
  obtain one accepted order, replay it and obtain the other. Stop
  once both star slots have been credited. The next cartridge
  puzzle is evidence of available progression.
- Primary decision loop: inspect the full row, choose whether to
  compare height or spine thickness, insert books one by one into
  the selected order and read the accepted result. Reopen the
  same puzzle to apply the other comparison.
- Included: one-object insertion, row reflow, visible geometry,
  two independent ordering predicates, automatic result, retry
  and retained star slots. Excluded: earlier and later puzzles,
  campaign achievements, hints, skipping, Daily Tidy, downloadable
  puzzles, exact touch thresholds and reverse-order acceptance.
- Direct-play status: no personal console or emulator session.
  The official listing and developer material establish the
  release target and general control. Released gameplay captures
  and a player guide corroborate the book rules. Video frames
  were inspected in the background with no audio. The source
  traces do not establish an exact Switch patch.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| AL-001 | The commercial Switch base game was released on November 9, 2022. Nintendo supports handheld play and lists the ordinary sorting puzzles separately from additional content. The publisher confirms direct touchscreen support. | Observation | Corroborated | High | P1, P2, P3 |
| AL-002 | The first bookshelf has nine visible books. Dragging one to another position lets the intervening books shift. The insertion retains the other books in their relative order. | Observation | Corroborated | High | W1 01:58–02:14, W2 04:28–04:56 and 05:15–05:36, S1 |
| AL-003 | One accepted row orders the books by height and another by spine thickness. Both descending left-to-right arrangements are visible. The width-ordered row has a shorter book to the left of taller books, separating the predicates. | Observation | Corroborated | High | W1 02:10–02:15, W2 04:54–05:02 and 05:42–05:49, S1 |
| AL-004 | The game checks the settled row without a separate answer submission. On the initial observed height clear, one star fills and the second stays outlined. The next puzzle can open with one star. | Observation | Corroborated | High | W1 02:12–02:22, W2 04:55–05:04, S1 |
| AL-005 | The same shelf can be replayed from its starting order. The shelf selection has separate retained stars. Completing the thickness order in the observed revisit yields a result display with both stars filled. | Observation | Corroborated | High | W2 04:24 and 05:05–05:49, S1, S2 |
| AL-006 | All the book measurements needed for the two comparisons are visible in the settled view. The shelf stays unchanged between decisions until the next drag. No deadline or remaining-move counter is visible in the puzzle. | Observation | Corroborated | High | W1 01:58–02:14, W2 04:29–04:55 and 05:12–05:44 |

## Basic data

- Release / origin: developed by Max Inferno and published by Secret
  Mode as a commercial puzzle game. The analysed target is
  `PLAT-NINTENDO-SWITCH`, English base game.
- Mechanical family: `FAM-006`. Arrange the entire finite object
  set so the common ordering condition holds along the row.
- Primary product and creator evidence, checked 2026-11-25:
  - **P1:** [Nintendo UK base-game listing](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-download-software/A-Little-to-the-Left-2292011.html).
    Commercial date, platform, language and touch support.
  - **P2:** [Secret Mode’s Nintendo Switch launch announcement](https://wearesecretmode.com/news/a-little-to-the-left-is-out-now--0).
    Publisher confirmation of touchscreen play and sorting activities.
  - **P3:** [Max Inferno press material](https://www.maxinferno.com/press).
    Developer, platform and solution variety. Later additional
    puzzle packs use their own boundaries.
- Recorded and first-hand evidence:
  - **W1:** [Chocoholie’s 2022 release walkthrough](https://www.youtube.com/watch?v=8QTAmtu4y60&t=117s).
    The initial distinct star and immediate successor after
    a height sort. Capture platform and exact patch are unverified.
  - **W2:** [NobleArcade’s two-order shelf trace](https://www.youtube.com/watch?v=QKFV2DOCs2o&t=264s).
    Shows both solved rows and the intermediate retry. Both
    marks already exist on its starting level-selection tile,
    so the initial grant is corroborated separately.
  - **S1:** [Abbilieve’s chapter guide with captured solutions](https://steamcommunity.com/sharedfiles/filedetails/?id=3472623422).
    The Level 7 entry separates height and thickness.
  - **S2:** [Chapter 1 player guide](https://www.trueachievements.com/game/a-little-to-the-left/walkthrough/3).
    First bookshelf completion and repeat-route instructions.
- Claim IDs: AL-001–AL-006. Capture the row and both result slots
  at entry, first clear, retry and the second accepted order.

## Mechanical decomposition

### Action Genes

- New `ACT-947`: remove and insert one book at a different
  rank with automatic movement of the intervening books (AL-002).

### System Behaviour Genes

- New `SYS-2032`: settle the satisfied authored ordering rule
  into its own star slot and preserve prior credit when starting
  the puzzle again (AL-004, AL-005).

### Constraint Genes

- New `CON-904`: use the same comparison attribute and accepted
  direction for every successive pair in the complete row (AL-003).

### Information Genes

- Reuse `INF-001`: the current row and comparative geometry of all
  nine books are visible before each decision (AL-002, AL-006).
  The player still has to infer which attributes the validator accepts.

### Objective Genes

- Reuse `OBJ-006`: satisfy a complete row predicate to finish the
  puzzle. A second replay applies a different accepted predicate
  to the same set (AL-003–AL-005).

### Time Genes

- Reuse `TIM-002`: inspect the current order before the next
  discrete insertion, with no advancing task clock (AL-006).

## Formal state and transitions

The current row is a permutation of nine book identities, each with
a visible height and spine thickness. An insertion deletes one
book from the current order and restores it at the chosen index.
The remaining books keep their relative order. Let the two authored
predicates be height order and thickness order. A settled layout
may resolve a puzzle credit. Replay starts with the original sequence
and the previously awarded credit set. One satisfied predicate permits
entry into the next ordinary puzzle.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Nine books in their starting order | Drag the tallest from near the middle to the left end | The displaced span shifts and the tallest book becomes first | AL-002 |
| Height is correct across the row after the last insertion | Release the final book | The game fills the height star and ordinary progression is available | AL-003, AL-004 |
| Height star credited | Replay this same puzzle | The starting row returns with the credited result retained | AL-005 |
| Same nine books in a new attempt | Insert the books in descending spine thickness | The distinct thickness result is accepted and both star slots can be filled | AL-003, AL-005 |

## Strategic and experiential structure

Hold one visual criterion constant for the entire row. Work from a
clear endpoint, then compare each next remaining spine. The second
star invites the player to discard the first ordering rule and look
at another property of the same objects.

## Replay and variation

A replay restores the witnessed starting order. Both traces use
descending orders. The evidence does not determine the behaviour
of reversed rows, exact tolerances, repeated solved rows or on-device
save persistence after a restart.

## Adjacent systems and history

Home Sweet Home contains other book layouts with distinct predicates.
The next cartridge puzzle and the later height-valley book puzzle
are outside this scope. No behaviour from DLC or Daily Tidy is
admitted here.

## Normalised genome

- Action: ACT-947.
- System Behaviour: SYS-2032.
- Constraint: CON-904.
- Information: INF-001.
- Objective: OBJ-006.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `729` (`GAME-0001`–`GAME-0729`).
- Exact genome matches: none.
- Tied near matches: `GAME-0115` — Unpacking (`3 / 9 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Unpacking (GAME-0115)](../s-z/unpacking.md) | INF-001, OBJ-006, TIM-002 | Both give the player time to inspect objects and satisfy a complete visible arrangement. Unpacking assigns household items to compatible room surfaces. The bookshelf changes only the order of an existing row and preserves separate completion credit for each accepted visual comparison. | Near, `0.333333`. |

## Taxonomy impact

Separate rank insertion from the constraint that every pair follows
one attribute. Record the two persistent solution credits as a system
effect associated with the same replayable puzzle.

## Negative results

- The thickness solution includes a height inversion.
- The next ordinary puzzle is available from one accepted order.
- Changing the visual order uses placement of the same books.
  It does not require choosing a difficulty or different shelf.

## Delta summary

Add a shared shelf that admits two distinct sorts of the same
pieces, each retaining its own completion state.

## New facts

- One dragged book can shift several other positions while leaving
  those books in the same relative order.
- An accepted layout can fill only one visible result slot and
  permit normal progression.
- A later replay can complete the second ordering rule.

## Principles and design implications

Give objects two independently ordered, legible properties to make
a second solution a change of interpretation. Reuse the same pieces
and retain separate credit so each discovered rule stays readable.

## Puzzle or game generation potential

Create a finite set with differing height and width rankings.
Verify that the selected comparison holds across the whole sequence.
Offer a separate replay and preserve prior discoveries across it.

## New genes

- ACT-947
- SYS-2032
- CON-904

## New combinations

None. The full predecessor and combination scan found no admitted combination.

## Taxonomy changes

[Taxonomy Change 476](../../../research/taxonomy-changes/TAXONOMY_CHANGE_476.md).

## Next recommended game

Pengo on its original SEGA arcade cabinet is the next Selection 064 unit.

## Why this game

The first shelf makes alternative accepted solutions observable with
the same pieces, the same controls and different visual comparisons.

## Review status

Reviewed 2026-11-25 for the English Nintendo Switch digital base
game with the first bookshelf as its play boundary.
