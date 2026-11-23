---
game_id: GAME-0584
slug: saturn-bomberman
game_title: Saturn Bomberman
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-270
  system:
    - SYS-037
    - SYS-045
    - SYS-470
    - SYS-755
    - SYS-1045
    - SYS-1723
    - SYS-1724
  constraint:
    - CON-263
    - CON-842
  information:
    - INF-179
    - INF-555
  objective:
    - OBJ-320
  time:
    - TIM-003
---

# Game: Saturn Bomberman

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Open a route with a timed bomb, retreat through an open lane, and stay
in the arena as everyone else is removed and falling blocks fill the floor.

## Analysis scope

- Version / ruleset: original English North American 1997 Sega Saturn
  retail disc 81070. Battle Game → Match Play, Normal field size and
  Single mode on the first stage, Path to Glory. The catalogue code and
  year identify the edition. A precise shipment day and checksum of the
  capture's disc are unverified.
- Structured analysis target: PLAT-SEGA-SATURN.
  See [platform coverage](../../platforms/games.json).
- Entry: set one human and four computer players, Computer Level 3,
  2:00 per battle and three wins per match. Enable No Draw. Disable
  Shuffle, Devil, Mad Bomber and Bonus Game. These are reproduction
  settings, independent of capture settings that are too small to read.
  Start the first round with fresh contestants in their arena positions.
- Primary decision loop: move through open lanes and plant an available
  timed bomb on a legal tile. Make room by breaking soft blocks and
  retreat before the blast travels along its row and column. Take
  exposed pickups if the path is safe, and use longer reach, more
  simultaneous placements or speed to outlast rivals. With No Draw
  enabled, heavy blocks can crush contestants and close lanes as
  the timed round runs on.
- Positive exit: finish the round as the last eligible contestant in
  the arena and count one victory in the individual tally. Stop at the
  first round settlement. Reaching three wins governs the full match,
  outside the boundary of this unit.
- Negative exit: final elimination ends control for that round with Mad
  Bomber off. A remaining opponent can subsequently claim the win.
  The exact same-frame ordering if all remaining contestants are
  eliminated together is unverified.
- Included: local human and CPU navigation, ordinary fuse placements,
  blast topology, clearable and fixed blocks, revealed pickups and
  incremental blast-range, bomb-capacity and movement upgrades, late
  block pressure, live clock, round tally and lone-survivor credit.
- Excluded: Japanese and PAL editions as targets, the Normal Game
  campaign, Master Game, Series, Net Link, Team, Wide, other stages,
  post-match Bomber Catcher, the enabled Mad Bomber and Devil branches,
  and an inventory-wide study of specialised items and mounts.
- Potential scoped modules: Team settlement or Mad Bomber's usable
  perimeter after arena elimination, each under its own settings.
- Direct-play status: not conducted. The original English manual and
  disc images establish the retail scope. Sampled static frames from
  an NTSC English recording verify stage entry, familiar floor
  geometry, timed play and later match settlement. A Japanese edition
  recording corroborates the same stage layout and late pressure only.
  No game executable, video playback or audio was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SB-001 | Hudson's Saturn Bomberman has an original North American Sega Saturn retail release in 1997, code 81070. The studied path is local Battle Game, Match Play, Normal-sized, Single, stage one. | Confirmed | Direct | High | P1, P2, W1, R1 |
| SB-002 | Match setup separates human and CPU entries, CPU difficulty, time, the wins-to-match target and side-rule switches. The in-arena header shows time and each character's wins. Shuffle off preserves starting positions. | Observation | Corroborated | High | P1, W1, W2 |
| SB-003 | In live play a contestant moves and places a bomb locally. Its fuse runs alongside movement. Placed count is constrained by the contestant's concurrent capacity. | Observation | Corroborated | High | P1, W1, W2 |
| SB-004 | Blasts extend along board lanes. Hard blocks remain and bound the affected lanes. Eligible soft blocks can be removed and expose an item. Some blocks contain no item. | Observation | Corroborated | High | P1, W1, W2 |
| SB-005 | Contact acquires exposed items. Firepower, Bomb and Roller Skates are documented Battle items that respectively increase blast reach, simultaneous bomb capacity and movement speed. | Observation | Corroborated | High | P1, W2 |
| SB-006 | No Draw permits heavy blocks to fill the late arena and crush players. They occupy previously usable lanes. No precise onset threshold, fall order or equal-time resolution is claimed. | Observation | Corroborated | High | P1, W2 |
| SB-007 | Battle Game awards the remaining contestant the round, shows individual round wins, and uses the configured win count for the match. With Mad Bomber off, eliminated players have no perimeter attack. | Observation | Corroborated | High | P1, W1, W2 |

## Basic data

- Hudson Soft, Sega Saturn, North American English commercial release,
  1997. FAM-009 for planting threats while preserving escape routes
  against responsive opponents, FAM-010 for overlapping fuse, clock
  and closure pressure.
- P1: [Sega's North American Saturn Bomberman instruction manual](https://segaretro.org/images/a/ae/Saturnbomberman_sat_us_manual.pdf).
  Consulted the original booklet with its
  [searchable mirror](https://manualzz.com/doc/23194932/sega-saturn-bomberman-video-game-instruction-manual).
  Its control, Battle Game, Match Play and item sections separate
  the countdown, solids, item classes, legal modes, win settings and
  optional perimeter play. The manual's general item catalogue does
  not establish the drop table of one arena.
- P2: [Scans of the original North American retail product](https://www.satakore.com/sega-saturn-game%2C%2C81070%2C%2CSaturn-Bomberman-USA.html).
  The disc, back and spine identify product 81070 and the English
  North American release. The archive's calendar entry is unnecessary
  for the mechanical scope.
- W1: [LongplayArchive, NTSC Saturn run](https://www.youtube.com/watch?v=iD0dd8g0SzI&t=6864s).
  At 1:54:40–1:55:20, sampled frames show the English title, Battle
  options and roster. At 1:55:30–1:57:10 they show the initial arena,
  removal of soft blocks and the live top strip. The match-level
  Victory screen is visible at 1:57:30. Do not read the finest menu
  switches or individual hits from these small frames.
- W2: [Yamishitsuji, first arena in the Japanese edition](https://www.youtube.com/watch?v=C0c1wiTcrOU&t=41s).
  The author provides the 2:00, three-win, four-opponent setup with
  the pressure setting enabled. At 0:50–1:30 frames show the board
  opening and orthogonal blasts. At 1:50–2:00 pressure blocks occupy
  the outer lanes. By 2:20 the top strip shows a credited first
  round. The menu is Japanese, and the capture leaves Bomber Catcher
  on. It corroborates visible geometry and transitions rather than
  provenance of the English disc or exact timing parity.
- R1: [Ragey's arena guide](https://randomhoohaas.flyingomelette.com/bomb/sat-1/battle.html).
  Identifies the English name of the first main arena and its ordinary
  soft-block layout separately from hidden variant selections.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 steers the active contestant along open routes. ACT-270
  commits a legal charge to a tile and starts its fuse while movement
  remains available (SB-003).

### System Behaviour Genes

- SYS-045 moves CPU-controlled rivals without waiting for player input.
  SYS-1045 computes the orthogonal blast reach subject to blockers.
  SYS-470 resolves the fuse and effect on eligible bodies and geometry
  (SB-002–SB-004).
- SYS-755 removes a struck soft block and exposes its item if present.
  SYS-037 acquires an exposed collectible on contact. SYS-1724
  applies the typed increase after collection (SB-004, SB-005).
- SYS-1723 lands additional solid pressure blocks in the late No Draw
  interval, shrinking the usable floor and threatening characters on
  impacted cells (SB-006).

### Constraint Genes

- CON-842 binds concurrently placed ordinary bombs to the current
  owner's capacity. Fuse resolution frees a slot (SB-003, SB-005).
- CON-263 removes defeated contestants from active control for the
  rest of the round under the chosen settings (SB-007).

### Information Genes

- INF-179 exposes the current lanes, hard and soft blocks, planted
  bombs and revealed items. INF-555 shows remaining time and wins
  by character (SB-002, SB-004, SB-007).

### Objective Genes

- OBJ-320 credits the last eligible contestant in the arena with
  one round win (SB-007).

### Time Genes

- TIM-003 keeps opponent decisions, movement and bomb fuses running
  during a timed battle (SB-002, SB-003, SB-006).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Fresh field and spare concurrent capacity | Place an ordinary bomb on an open tile, then retreat perpendicular to a blast lane | The bomb stays in place until its fuse resolves. Movement is available during the wait. | SB-003, SB-004 |
| A ray faces a hard block on one axis and a reachable soft block on another | Let the ordinary fuse run out | The hard block survives and shields its far side. The soft block leaves a new open tile, with an item if it contained one. | SB-004 |
| An exposed Firepower or Bomb item is reachable | Walk over the item and attempt the next ordinary placement | Firepower changes reach, while Bomb changes concurrent capacity. Taking one does not itself confer the other. | SB-005 |
| Several contestants survive into late No Draw play | Keep moving after blocks land on outer lanes | Landing changes legal routes and can remove exposed contestants; movement continues in usable cells. | SB-006 |
| Only two contestants remain and one is finally eliminated | Let the remaining character resolve the bout | The last contestant receives one win. The removed player cannot act before the following round. | SB-007 |

## Strategic and experiential structure

A bomb can open a route and remove an escape route at the same time.
The current range and solid blockers determine which route remains safe.
Collectible upgrades improve offensive and movement options, but reaching
them requires surviving the same intersecting lanes. Once heavy blocks
land, previously reliable retreats may close. Eliminations, rather than a
set of enemies with a required exit, control settlement.

## Replay and variation

Turning Mad Bomber on would restore a limited perimeter attack to a
defeated participant and invalidate a no-control assumption. No Draw
scopes the continuing fill of the board. Exact item layouts, CPU decision
policy, simultaneous knockouts and partial pressure behaviour with No
Draw off are left to controlled runs.

## Adjacent systems and history

The same commercial release has a cooperative-oriented Normal Game
campaign, separate Master Game and configured multiplayer modes. The
English manual lists specialised gloves, kicks, mounts and ailments.
Their full per-arena availability, acquisition order and timing are
outside the basic match route admitted here.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-270 | direct movement and local fuse placement |
| System Behaviour | SYS-037, SYS-045, SYS-470, SYS-755, SYS-1045, SYS-1723, SYS-1724 | CPU movement, blocked blast rays, timed effect, block removal, pickup contact, typed growth and pressure blocks |
| Constraint | CON-263, CON-842 | individual concurrent capacity and elimination until next round |
| Information | INF-179, INF-555 | visible arena and personal bout tally beside the clock |
| Objective | OBJ-320 | one round win for the surviving contestant |
| Time | TIM-003 | running inputs, fuse and clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `583` (`GAME-0001`–`GAME-0583`).
- Exact genome matches: none.
- Tied near matches: `GAME-0387` — Super Bomberman (`9 / 20 = 0.450000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Super Bomberman (`GAME-0387`) | ACT-008, ACT-270, INF-179, SYS-037, SYS-045, SYS-470, SYS-755, SYS-1045, TIM-003 | Both games clear soft terrain with live fuses and blocked blast rays. The original SNES campaign needs required hostile clearance and a hidden exit. The Saturn round closes lanes with heavy blocks and awards its last remaining contestant the win. | `9 / 20 = 0.450000` |

### Preserved research notes

- New genes: SYS-1723, SYS-1724, CON-842, INF-555 and OBJ-320.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_330](../../../research/taxonomy-changes/TAXONOMY_CHANGE_330.md)
  separates late space closure, typed upgrades, concurrent placement,
  visible individual tally and round settlement.

## Negative results

- Reject CON-068 as a substitute for the pressure rule. Late blocks
  change the route geometry before round settlement.
- Reject OBJ-071 for the active objective. The round follows the
  remaining eligible contestant, without a separate bomb objective
  or attack/defence sides.
- Reject SYS-911. There is no finite stock of same-round respawns
  after final elimination with Mad Bomber off.
- No chain-reaction timing, first-round special item table, or exact
  soft-block initial distribution is inferred from the sampled frames.
  No separate gene for the characters, three-win parameter, action
  button glyphs or arena decoration.

## Delta summary

## New facts

- [Observation | Corroborated | High] Within the time-bound
  free-for-all, soft-block clearance, the fuse geometry and the
  late occupation of floor cells impose different route conditions.

## New genes

- [Observation | Corroborated | Medium] Five additions in TAXONOMY_CHANGE_330.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are listed in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- Verify simultaneous final hits and the individual pressure-block
  order in a controlled run with the English North American disc.
- Record an exact first-arena special-item availability table, plus
  legal chain timing and bomb re-entry, separately from the manual's
  Battle-wide catalogue.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0585, native Meta Quest 2
  Into the Radius. Bound the first released supply excursion and its
  safe return, then close the selected nine-game batch.
- Optimisation criterion: compare how constrained safe movement and
  resources work in an extraction route rather than an arena round.

## Why this game

- [Hypothesis | Limited | Medium] A full first-battle boundary
  distinguishes timed resource placement, occupancy changes and
  eligibility-based settlement within the same visible playfield.
