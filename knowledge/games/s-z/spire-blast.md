---
game_id: GAME-0657
slug: spire-blast
game_title: "Spire Blast"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-616
    - ACT-868
    - ACT-869
  system:
    - SYS-036
    - SYS-1894
    - SYS-1895
  constraint:
    - CON-164
  information:
    - INF-005
  objective:
    - OBJ-007
  time: []
---

# Game: Spire Blast

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English native iPhone Apple Arcade commercial
  release, App Store ID 1532717034, released 22 January 2021. Two
  portrait recordings posted on release day provide the Level 2
  rule traces. Executable build identifiers and capture devices were
  not disclosed.
- Entry: Level 2 after the opening tutorial. The colored cylinder
  is intact, the score starts at zero and the tutorial shows a
  blue loaded shot and a yellow preview. The ordinary shot stock
  starts at 30.
- Primary decision loop: swipe to view a useful target face, inspect
  the loaded and next shots, swap them when the preview fits better,
  and tap the exposed patch. Observe the resulting support loss
  and re-aim at the changed geometry while shots remain.
- Exit: the colored stack is gone, the base remains, and the
  Level 2 Success panel settles three stars. The onward control
  leads to the map and a playable Level 3 with its own tower.
- Included: the addressed shot, exact next-color preview, a two-slot
  swap, finite launch stock, local same-color removal, falling intact
  bodies, star and score feedback, clearance and successor access.
- Excluded: controller operation, the older prototype, other device
  versions and ports, boosters, complex later objectives, exact
  scoring and contact thresholds, a deliberate zero-stock failure,
  restart persistence and availability of the exact old binary.
- Suggested later scope: measure a deliberate non-matching launch
  and follow a later level whose crate or dragon quota is separate
  from stack clearance.

## Direct-play status

No direct play was performed. The App Store identifies the native
iPhone Apple Arcade product. Orbital Knight explains color matching
and continuous collapse. The two launch-day recordings show the
same Level 2 starting layout, prompted swap, yellow hit, collapse,
result and available Level 3 in the original portrait presentation.
Stills and on-screen text were inspected silently in the background.
The capture hardware, exact app build, finger telemetry, collision
solver and saved-state persistence were not independently verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SB-001 | The selected commercial English iPhone release is the Apple Arcade app that went live on 22 January 2021. The traces show the original portrait Level 2. | Observation | Corroborated | High | P1, P2 and P5 give product, distribution and release date. W1 and W2 were published on launch day and show matching tutorial and tower. Capture hardware and binary were not disclosed. |
| SB-002 | Level 2 prompts a swap between the loaded and upcoming shots. Blue and yellow exchange their positions, with blue preserved next. No launch is spent by the swap. The opening shot changes the displayed stock from 30 to 29. | Observation | Corroborated | High | W1 0:36–0:42, W2 0:51–0:56. The larger loaded shot and smaller preview are both visible. Exact later queue generation and an out-of-ammo trace are unverified. |
| SB-003 | A swipe rotates the view around the fixed tower, exposing a different firing face. Tapping an exposed target commits the loaded shot toward that patch. A matched yellow hit clears a local yellow patch. | Observation | Corroborated | High | P2, P3 and P4 for color matching and orbit. W2 0:19–0:26 for the shared tutorial and W1 0:38–0:43 plus W2 0:53–0:57 for orbit, addressed shot and local opening. No launch-strength setting or deliberate non-match test is claimed. |
| SB-004 | After the match removes support, still-intact blocks of other colors physically tilt and fall. The remainder has a different accessible shape, so another shot can target a different exposed group. | Observation | Corroborated | High | P2 and P3. In W1 0:42–0:49 and W2 0:55–1:04 the yellow effect precedes the tilting multicolored mass. Exact group connectivity, collision damage and settle coefficients were not measured. |
| SB-005 | Star progress can fill before the remaining blocks are gone. The trace then clears the colored stack, leaves the base, and shows the graded Level 2 result. | Observation | Corroborated | High | W1 1:05–1:23 and W2 1:28–1:42. W2 shows three stars with targets still standing and later settles at 16,100 points with three stars. P3 distinguishes level objectives from just toppling a structure. No exact score-to-star threshold is inferred. |
| SB-006 | The result's advance option leads to the map and Level 3. Playable Level 3 presents its own standing tower and loaded shot. | Observation | Corroborated | High | W1 1:21–1:29 and W2 1:41–1:52. Both reach the next tower without spending the remaining Level 2 stock. No persistence after closing the app was tested. |

## Basic data

- Analysis target: `PLAT-IOS`, commercial Apple Arcade iPhone release,
  English UI, App Store ID 1532717034.
- Developer and publisher: Orbital Knight.
- Mechanical families: `FAM-004`, matching and combination, and
  `FAM-007`, physics and object manipulation.
- Checked: 2026-11-23.
- P1: [Apple App Store iPhone listing](https://apps.apple.com/us/app/spire-blast/id1532717034).
  Documents the iPhone edition, developer and English language.
- P2: [Orbital Knight's game page](https://www.orbitalknight.com/games/spire-blast).
  Documents color-matched shooting and structural collapse.
- P3: [Apple's game and objective explainer](https://apps.apple.com/am/iphone/story/id1541032630).
  Documents orbiting the view, local removal, collateral falls
  and the separate need to satisfy the level's objective.
- P4: [Launch interview with Orbital Knight's Karol Drzymala](https://www.shacknews.com/article/122361/spire-blast-interview-bringing-colorful-tower-puzzles-to-apple-arcade?amphtml=1).
  Published the next day. Distinguishes the Apple Arcade product,
  color matching and the later cage, dragon and booster mechanics.
- P5: [Apple's US catalogue metadata for app 1532717034](https://itunes.apple.com/lookup?id=1532717034&country=US).
  The original release date is 22 January 2021, with iPhone support.
  The live catalogue is not a copy of the launch binary.
- W1: [Sold1er187xx's launch-day Apple Arcade run](https://www.youtube.com/watch?v=wru5lIHX7W8&t=33s).
  Level 2 starts at 0:33 and Level 3 follows at 1:25.
- W2: [App Unwrapper's launch-day iOS run](https://www.youtube.com/watch?v=T_Su2RvpoJs&t=48s).
  Separate English portrait run, with the opening tutorial, the same
  Level 2 decision and a visible three-star receipt before Level 3.

## Mechanical decomposition

### Action Genes

- ACT-616: orbit the dolly view around the standing tower to choose
  an exposed face without moving the blocks.
- ACT-868: exchange the current shot and its exact successor, preserving
  both colors and the available shot count.
- ACT-869: tap the exposed block to send the loaded shot toward it.

### System Behaviour Genes

- SYS-036: after release, live gravity and contact move unsupported
  blocks. Intact sections can pivot and fall separately from matched
  removal.
- SYS-1894: a compatible hit removes a local same-color patch and
  changes the support for remaining bodies.
- SYS-1895: running score advances visible star progress, while a
  separate clearance permits the final graded result and successor.

### Constraint Genes

- CON-164: the displayed attempt-local projectile stock decrements
  when a normal shot is launched.

### Information Genes

- INF-005: the next projectile's exact color and symbol are visible
  before the shot or swap; the complete queue is not displayed.

### Objective Genes

- OBJ-007: clear the Level 2 target stack within its shot stock.
  The underlying plinth remains after the successful attempt.

### Time Genes

No independent clock or phase cadence is admitted. The observed
post-hit passage of time belongs to the continuous physics rule.
The exact allowance for another launch while blocks are still
moving was not tested.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Level 2 intact, blue loaded and yellow visible next | Tap the displayed next shot during the prompt | Yellow becomes the active shot. Blue stays as the preview and the finite launch count is preserved | SB-001, SB-002 |
| Yellow shot loaded | Orbit to see the concentrated yellow face and tap that patch | A yellow projectile leaves the launcher, stock falls by one, and a local yellow section is removed | SB-002, SB-003 |
| Opening in the structure | Allow the exposed unsupported bodies to respond | Intact multicolored sections tilt outward, collide and fall, uncovering a different silhouette | SB-004 |
| Three live stars, colored blocks still standing | Keep using matched shots against exposed blocks | In the recorded successful run, the remainder is cleared and the base remains | SB-005 |
| Result accepted | Use the onward control and proceed from the map | Level 3 loads with its own tower and ordinary loaded shot | SB-006 |

## Strategic and experiential structure

The preview matters before the player spends a shot. A target face
is only one part of that decision. A smaller matched patch can be
more useful if losing it exposes a supporting gap and topples a
mixed group. After the collision, a new silhouette changes what is
accessible. A high live grade can precede the last necessary
physical removal.

## Replay and variation

Both launch-day traces start with the same blue and yellow order
and demonstrate the prompted exchange. Later shot order and score
vary. The observed stars do not establish a compulsory exact shot
sequence. Neither route deliberately exhausts the stock or tests
reload persistence.

## Adjacent systems and history

Orbital Knight documents later objective types, including clearing
cages and feeding falling blocks to a dragon. Those cannot be inferred
from ordinary Level 2 clearance. The older prototype, ports and
later commercial changes are outside this packet.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-616, ACT-868, ACT-869 | Orbit, exchange shot order and commit a tap-targeted launch |
| System Behaviour | SYS-036, SYS-1894, SYS-1895 | Settle live bodies, remove a local matching patch and award a star grade |
| Constraint | CON-164 | Spend a finite stock of physical projectiles |
| Information | INF-005 | See the exact immediate successor |
| Objective | OBJ-007 | Clear the tower targets |
| Time | — | Live post-hit physics is in SYS-036 |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `656` (`GAME-0001`–`GAME-0656`).
- Exact genome matches: none.
- Tied near matches: `GAME-0465` — Boom Blox (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Boom Blox (GAME-0465)](../a-f/boom-blox.md) | ACT-616, OBJ-007, SYS-036 | Both expose another face by orbiting and use live collision to clear targets. Boom Blox commits a Wii Remote baseball throw with motion-sampled strength. Spire Blast taps the block, relies on a compatible color and allows the loaded and next shots to swap. | Near, `0.230769` |

## Taxonomy impact

ACT-616 already separates camera orbit from physical motion.
ACT-868 preserves the current and next tokens as an exchange.
ACT-869 commits a projectile by touching the target, rather than
adjusting a sling or launch force under ACT-113. The matched patch
under SYS-1894 changes real support, unlike deleting and refilling
cells on a match board. SYS-036 already covers continuous body
response. SYS-147's material-damage chain is not assumed here.
SYS-1895 separates score-driven grade from target clearance;
SYS-822 expressly excludes tiers mapped from an activity score.

## Negative results

- A selected face does not rotate the physical tower relative to
  its own supports.
- Neither a visible third star nor the first collapse is the
  Level 2 terminal by itself.
- The observed local yellow hit does not certify all adjacency
  ties, collision damage, alternate objectives or save persistence.

## Delta summary

Nine scoped genes include four additions and five reused definitions.

## New facts

- Choosing the previewed color keeps the previous loaded shot in reserve.
- A localized matching effect can remove support for intact blocks of
  several different colors.
- The third star can be visible before the board settles into a clear
  that permits progression.

## Principles and design implications

Keep the camera, shot order and shot commitment as separate controls.
Give the material removed by a direct hit a separate visual signal
from heavier intact bodies tilting afterward. Show the grade as
progress without replacing the clearance condition.

## Puzzle or game generation potential

Expose two colored projectiles and let the player preserve either
one for the next shot. Put a compatible patch next to a larger load
that shares support. Display the updated target surface before the
next decision and settle score separately from the clear.

## New genes

- ACT-868
- ACT-869
- SYS-1894
- SYS-1895

## New combinations

None. All 274 verified combinations were checked for a supported subset.

## Taxonomy changes

[TAXONOMY_CHANGE_403](../../../research/taxonomy-changes/TAXONOMY_CHANGE_403.md).

## New questions

What does a mismatched shot do under a controlled repeated test?
Which local relationship permits neighboring blocks of one color to
clear together? Can a live shot be committed before all intact
bodies settle?

## Next recommended game

This unit closes Selection 055. Select the next subject through the
next separately approved mixed-platform horizon.

## Why this game

A short launch-era tower isolates the interaction between a visible
projectile queue, a directed match and continuous structural collapse,
with a clearly distinct score tier and playable successor.
