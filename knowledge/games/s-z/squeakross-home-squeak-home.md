---
game_id: GAME-0685
slug: squeakross-home-squeak-home
game_title: "Squeakross: Home Squeak Home"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids:
  - COMB-0008
gene_ids:
  action:
    - ACT-007
    - ACT-906
  system:
    - SYS-1960
  constraint:
    - CON-001
    - CON-018
  information:
    - INF-001
    - INF-006
  objective:
    - OBJ-006
    - OBJ-363
  time:
    - TIM-002
---

# Game: Squeakross: Home Squeak Home

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first catalogue chair, its binary grid and the empty room identify the fixture.

## Analysis scope

- Version / ruleset: commercial English base game from the original
  Nintendo Switch eShop, released June 7, 2025. Solo launch-window
  onboarding as shown in W1. The exact executable build and console
  firmware are unverified.
- Structured analysis target: PLAT-NINTENDO-SWITCH in
  [platform coverage](../../platforms/games.json).
- Entry: page 1 of the Home Squeak Home Catalog in a new room.
  Nini directs the player to its upper-left chair puzzle. W1 chooses
  Skip Tutorial on the question about knowing Nonograms. The
  catalogue and furnishing introductions still happen on this route.
- Primary decision loop: read both axes of ordered run lengths on
  the 5×5 board. Mark filled cells and mark known blanks when useful.
  When the grid satisfies the clue sets the game awards the Basic
  Chair. Enter Edit Mode, select that chair, put it down and finish
  the room introduction.
- Exit: ordinary room control with the Basic Chair in its chosen
  position. Stop before opening the next catalogue puzzle.
- Included: binary marks and optional crosses, visible clue lengths,
  simultaneous row and column constraints, automatic acceptance,
  the associated furniture award and its selection, placement,
  relocation and presence outside Edit Mode.
- Excluded: deduction aids and wrong-mark recovery, precise timing
  of feedback, alternative catalogue puzzles, optional color
  variants and challenge modes, later decorating, exact placement
  collision or rotation rules, other editions and any claim about
  reloading the save.
- Potential scoped module: compare one ordinary row deduction with
  a Logic-Assist hint on a different puzzle.
- Direct-play status: no personal Switch execution or binary
  inspection. Nintendo identifies the original Switch commercial
  product. W1 identifies a Switch eShop recording and shows the
  complete local route. Alblune's own walkthrough and launch
  documentation independently support the puzzle and room sequence.
  Only relevant video frames were reviewed in the background,
  with no audio used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SQH-001 | The English single-player Nintendo Switch download is Alblune's June 7, 2025 base game. Its advertised standard puzzle play has no time limit and Logic-Assist is optional. | Confirmed | Direct | High | P1, P2, P3 |
| SQH-002 | The first chair uses a visible 5×5 binary board with ordered clue lengths on both axes. The player marks addressed cells filled, and may cross known blanks separately. W1 shows both marks and accepts the completed picture without crossing all blanks. | Observation | Corroborated | High | W1 3:10–3:59, W2 0:49–1:40, R1 |
| SQH-003 | The accepted chair picture resolves into a 3D Basic Chair award. Returning to the catalogue shows the solved chair entry and leads to the room introduction. | Observation | Corroborated | High | W1 3:58–4:17, W2 1:34–2:05, P1 |
| SQH-004 | In Edit Mode the furniture collection contains the earned Basic Chair. Select it, place it on the floor, then grab and release it in a different room position. The editor displays the floor positions. | Observation | Corroborated | High | W1 4:21–4:37, W2 1:47–2:27 and 7:29 onward, P3 |
| SQH-005 | Using Done leaves Edit Mode and the placed chair remains in the ordinary room view. After the short room interaction introduction, the usual room controls and Play are available. This observation spans the mode transition only. | Observation | Corroborated | High | W1 4:36–4:54, W2 2:07–2:28, P3 |

## Basic data

- Release / origin: Alblune, June 7, 2025. Nintendo Switch English
  download, commercial base game.
- Mechanical families: FAM-001 for deductions from crossing
  constraints and FAM-017 for a credited solution enabling a
  room-placement step.
- P1: [Nintendo's US Switch product listing](https://www.nintendo.com/us/store/products/squeakross-home-squeak-home-switch/).
  Establishes developer, language support, platform, solo play,
  the unconstrained puzzle clock and optional aids.
- P2: [Nintendo's UK Switch release listing](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-download-software/Squeakross-Home-Squeak-Home-2850493.html).
  Dates and identifies the Nintendo Switch download.
- P3: [Alblune's launch press release](https://www.gamespress.com/SOLVE-PUZZLES-AND-DECORATE-YOUR-SPACE-IN-SQUEAKROSS-HOME-SQUEAK-HOME-O)
  and [developer's FAQ](https://steamcommunity.com/app/2871440/discussions/0/4339861173664011339/).
  The FAQ separates the required short placement introduction from
  subsequent optional decorating. Its Steam context does not
  establish the Switch controller layout.
- W1: [NintenDaan's Nintendo Switch eShop recording](https://www.youtube.com/watch?v=XBvohnj1UY4&t=174s),
  June 30, 2025. Use 2:54–4:54 for the catalogue, grid, award
  and room. The platform identification comes from this recording
  and Nintendo's listings.
- W2: [Alblune's gameplay overview](https://www.youtube.com/watch?v=Lg_ZAxJ6kY8&t=49s),
  June 9, 2025. Use the First Puzzle and Home Decor Tutorial
  chapters and the later home-decor chapter from 7:29. Supports
  the loop independently without establishing the capture platform.
- R1: [Nintendo World Report's Switch review](https://nintendoworldreport.com/reviewmini/71476/squeakross-switch-review).
  Corroborates the filled and crossed marks and that automatic
  crossing can be configured.
- Claim IDs: SQH-001–SQH-005.

### Reproducible fixture evidence

1. Open the first catalogue page. At 2:54–3:07 in W1 the selected
   entry shows a chair outline. Follow Nini's first-puzzle prompt.
   The board is visible by 3:11.
2. The row clues (top to bottom) are `4 / 4 / 1 1 / 5 / 1 1 1`.
   The columns (left to right) are `5 / 2 1 / 2 2 / 4 / 2`.
   Begin with the five-cell first column and fourth row. The
   remaining rows and columns constrain the assignment together.
3. The observed fill is `11110 / 11110 / 10010 / 11111 / 10101`.
   At 3:47–3:57 in W1 filled cells are gold and a crossed blank
   is red. The last required fill settles the un-crossed blanks
   without an extra submit step in this capture.
4. At 3:59–4:07 inspect the reward preview and the Basic Chair
   label. Continue back to the catalogue. At 4:11 the same
   chair entry shows its acquired form.
5. At 4:21–4:37 open the furniture collection from the new
   room's Edit Mode. Place the Basic Chair, grab it, then
   release it at a different position. Choose Done. At
   4:43–4:54 the chair is still visible outside the editor;
   the room tutorial gives way to ordinary control.

## Mechanical decomposition

### Action Genes

- ACT-007: fill an addressed cell or explicitly mark a known
  blank in the working assignment. SQH-002.
- ACT-906: select earned furniture in the editor, place the chair
  and move it to the preferred floor position. SQH-004.

### System Behaviour Genes

- SYS-1960: accepting the picture awards its depicted furnishing
  and makes that item available in the room editor. SQH-003–SQH-004.

### Constraint Genes

- CON-001: each of the fixed 25 board positions holds one cell
  state at a time. SQH-002.
- CON-018: every filled cell contributes to both orthogonal ordered
  run descriptions. Only the complete compatible assignment
  closes the puzzle. SQH-002.

### Information Genes

- INF-001: the whole current board, entered marks and both banks
  of clues remain visible together during deduction. SQH-002.
- INF-006: the edge numbers disclose ordered lengths of filled
  runs without giving their positions. SQH-002.

### Objective Genes

- OBJ-006: reach the binary assignment that satisfies every
  published line. SQH-002–SQH-003.
- OBJ-363: complete the room introduction with the chair from that
  puzzle visibly placed and ordinary room control available.
  SQH-003–SQH-005.

### Time Genes

- TIM-002: inspect clues and set marks at the player's pace. The
  time-spent display is separate from the completion condition.
  SQH-001–SQH-002.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Page 1 before first clear | Follow Nini to the upper-left chair | Blank 5×5 grid with both clue axes visible | SQH-002 |
| Visible grid with incomplete marks | Complete the run constraints on both axes | Accepted pixel assignment, then Basic Chair reward | SQH-002–SQH-003 |
| Reward acknowledged in the catalogue | Enter room Edit Mode and select Basic Chair | The awarded chair can be placed on the room floor | SQH-003–SQH-004 |
| Chair in its initial spot | Grab, relocate and release the chair, then choose Done | Chair at the chosen position outside Edit Mode | SQH-004–SQH-005 |
| Room introduction with the placed chair | Finish the local room prompts | Ordinary room control with the placed chair present | SQH-005 |

## Strategic and experiential structure

A full row and column give fixed marks. Each remaining proposition
affects two ordered clue lists. The evidence shows a useful cross
among unmarked blanks, so crosses communicate deductions without
requiring an extra mark in every blank. The solution makes the chair
available; placement lets the player choose its eventual room position.

## Replay and variation

W1 observes a relocation within a single furnishing edit.
The developer documents optional aids and subsequent optional
decoration. This scope does not establish how replaying a solved
puzzle affects duplicates or retains furniture across a restart.

## Adjacent systems and history

The first board instantiates the same five-gene interaction as
Nonogram. Squeakross records the clear as a furnishing the player
may place, giving the solved shape a role outside the board.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-007, ACT-906 | Set cell marks and position an earned furnishing |
| System Behaviour | SYS-1960 | Grant the corresponding usable furniture object |
| Constraint | CON-001, CON-018 | Bound occupancy and couple orthogonal clue runs |
| Information | INF-001, INF-006 | Expose the board and ordered run lengths |
| Objective | OBJ-006, OBJ-363 | Satisfy the clue lists and complete chair placement |
| Time | TIM-002 | Allow self-paced deduction |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `684` (`GAME-0001`–`GAME-0684`).
- Exact genome matches: none.
- Tied near matches: `GAME-0008` — Nonogram (`7 / 10 = 0.700000`).
- Supported combination subsets: `COMB-0008`.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Nonogram (GAME-0008)](../m-r/nonogram.md) | ACT-007, CON-001, CON-018, INF-001, INF-006, OBJ-006, TIM-002 | Both assign binary cells and satisfy orthogonal clue runs. Nonogram ends at the accepted assignment. Squeakross makes the pictured furnishing available in a separate editor and teaches the player to place it. | Near, `0.700000` |

## Taxonomy impact

Three admissions distinguish the edit action using earned stock,
the grant of the grid's corresponding furnishing and the
onboarding outcome after leaving Edit Mode. Seven existing
definitions cover the deduction board itself. ACT-612 and
CON-739 concern purchased furnishings and later approach or
use in a different household simulation. This fixture witnesses
a puzzle award and one valid relocation.

## Negative results

- Viewing the chair outline does not grant the furniture.
- Crosses alone do not satisfy the required filled runs.
- The acceptance sequence in W1 does not require a cross in every blank.
- Owning the chair does not itself put it in the room.
- The room tutorial is distinct from subsequent optional decorating.
- Persistence across a restart was not observed.

## Delta summary

Ten genes, three new. The standard cross-clued assignment supports
one existing combination. Its result grants the furniture used in
the separate first placement task.

## New facts

- The first chair clues cover both axes of a 5×5 board.
- Its accepted assignment produces the Basic Chair reward.
- The chair can be selected and relocated in the room editor.
- The selected place remains visible outside the editor.

## Principles and design implications

Keep the reward identity legible across the puzzle, collection and
placement modes. The shape serves as a concrete explanation of the
prize when the player changes from deduction to room arrangement.

## Puzzle or game generation potential

Build an original small studio where solving a pixel grid unlocks
a workbench lamp. Let the player place it where it lights the
next reading nook while keeping that choice separate from the
grid's unique assignment.

## New genes

- ACT-906
- OBJ-363
- SYS-1960

## New combinations

None admitted. [COMB-0008](../../combinations/COMB-0008.md)
gains corroborated additional support. All 274 verified
combination sets were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 431](../../../research/taxonomy-changes/TAXONOMY_CHANGE_431.md).

## New questions

- What board errors do different Logic-Assist settings expose?
- Which footprints and overlaps does the room editor reject?
- What happens to catalogue credit when replaying the same grid?

## Next recommended game

Continue Selection 059 with `GAME-0686`, Maniac Mansion, on
the original Commodore 64 release.

## Why this game

Its visible two-axis deduction has a direct and recognisable
consequence in a separate editable room.
