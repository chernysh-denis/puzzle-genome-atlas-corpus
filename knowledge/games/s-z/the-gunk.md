---
game_id: GAME-0707
slug: the-gunk
game_title: "The Gunk"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-542
  system:
    - SYS-1986
    - SYS-1987
  constraint: []
  information:
    - INF-644
  objective:
    - OBJ-026
  time: []
---

# Game: The Gunk

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Aim the suction arm at contamination attached around an early ridge
passage. Finish clearing the local obstruction and walk beneath the
open rock arch into the restored area.

## Analysis scope

- Version / ruleset: English Xbox Series X|S commercial base game,
  product 9P008L2LS87F, published by Thunderful and developed by
  Image & Form Games. The original commercial release is dated
  December 16, 2021. The witnesses do not establish an exact
  installed build or console settings.
- Structured analysis target: PLAT-XBOX-SERIES in
  [platform coverage](../../platforms/games.json).
- Entry: the `Climb up the ridge` objective during Looking for a Signal.
  Begin on the rocky shelf reached via the first previously grown
  mushroom steps. The arm is already repaired. Black nodules and
  strands with red highlights occupy parts of the shelf and arch.
- Primary decision loop: approach the adhered mass, aim and hold
  suction, and sweep or reposition to engage the portions still
  attached. When the last visible residue is gone, let the
  restoration resolve and walk through the opened arch.
- Positive terminal: Rani passes the arch and comes under player
  control inside the stone area where the green fissure is visible.
  Crossing uses the cleared rock approach. Regrown nearby plants
  are visible, and the sampled crossing does not use them as platforms.
- Included: direct navigation, targeted held suction, visible
  engagement and partial removal, grouped restoration and the
  cleared ground route. Excludes the repair, earlier fissure,
  crafting, growing the starting mushroom stairs, subsequent
  seed transport and growth, optional scans and loot, combat,
  the rest of Looking for a Signal and other platforms.
- Potential scoped module: transport a Mycelium Coil from its plant
  to a particular Energy Fissure and use the resulting steps.
- Direct-play status: no personal Xbox session, button telemetry,
  executable inspection or collision probing. Two independent
  chapter captures were examined as silent frames. Console and
  build attributions have the limits given below.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TG-001 | Xbox lists the commercial single-player product for Xbox Series X and Series S and dates the release December 16, 2021. | Confirmed | Direct | High | P1, P2 |
| TG-002 | The scoped encounter is on the shelf above the first grown mushroom steps, with black and red growth around a rocky passage, a clear landmark in both witnesses. | Observation | Corroborated | High | W1 13:05–13:14; W2 10:12–10:20 |
| TG-003 | Holding suction with the tool aimed at eligible growth pulls it toward the arm. The tool can be swept between parts and re-aimed while the massive obstruction remains. | Observation | Corroborated | High | P2; W1 13:15–13:36; W2 10:22–10:46 |
| TG-004 | During suction, visible stretching strands and particles link the engaged area to the gauntlet. In W1 an aim prompt shows LT for precision. The display does not establish an exact suction radius or count. | Observation | Corroborated | High | W1 13:23–13:35; W2 10:36–10:46 |
| TG-005 | The last visible attached remains disappear, a restoration wave or particle burst follows, and vegetation becomes visible on the surrounding stone. Partial removal before that leaves the site visibly contaminated. | Observation | Corroborated | High | P1–P2; W1 13:36–13:41; W2 10:47–10:52 |
| TG-006 | Rani then moves along the former obstruction's shelf and enters the opening. Neither recorded run plants a new seed between the suction and the crossing. | Observation | Corroborated | High | W1 13:40–13:44; W2 11:00–11:07 |

## Basic data

- Release / origin: Image & Form Games, Thunderful, Xbox Series X|S
  commercial base product. This unit analyses one ridge route.
- Family: FAM-014. Clearing attached material changes the available
  route at fixed world geometry.
- P1: [Xbox store page for The Gunk](https://www.xbox.com/en-us/games/store/the-gunk/9P008L2LS87F).
  Establishes the product, release and Series X|S support. The
  publisher describes vegetation recovering when corruption clears.
- P2: [Thunderful's Xbox Wire release-day account](https://news.xbox.com/en-us/2021/12/16/play-the-gunk-today-with-xbox-game-pass/).
  Identifies the arm as Pumpkin and describes suction and restoration.
  Its separate cloud controller explanation does not establish the
  witnesses' local hardware setup.
- W1: [Skycaptin5, Xbox Series X playthrough](https://www.youtube.com/watch?v=qmmdzy_PLCs&t=785s).
  Shows the orange gauntlet, retargeting and the first pass beneath
  the arch. The video's broader chapter markers are approximate.
- W2: [Richard Tharp, Series X/S chapter capture](https://www.youtube.com/watch?v=K5MVC-_HNtQ&t=612s).
  Independently shows the matching approach, the break-up of the
  obstruction and the restored shelf before entering. The listing
  groups Series X and Series S. The exact model is unverified.
- Claim IDs: TG-001–TG-006.

### Reproducible fixture evidence

1. After repairing the arm and using the earlier mushroom steps,
   approach the shelf leading toward the low arch. The black mass
   and lit red seams are visible in W1 at 13:09 and W2 at 10:16.
2. Hold the suction command and aim at an attached part. Turn
   toward the remaining portions to continue removing them. W1
   around 13:35 shows the active strand, glove intake and precision
   cue. W2 between 10:22 and 10:46 changes position and aim around
   the same still-contaminated rock lip.
3. Continue until the remaining contamination releases. W1 around
   13:38 shows the restoration effect. W2 shows the transition
   at 10:48–10:52, when the stone is no longer covered by the
   dark growth and pink shelves and green vegetation are visible.
4. Walk through the opening at W1 13:40–13:44 or W2 11:02–11:07.
   The green fissure is visible ahead. No new seed is applied to
   that fissure before the avatar enters the area.

## Mechanical decomposition

### Action Genes

- ACT-008: approach, reposition along the shelf and move through
  the cleared stone approach into the next bounded area.
- ACT-542: aim and hold the arm's vacuum on an attached deposit.
  The scoped deposit is removed from the world without a separate
  item placement or combat attack.

### System Behaviour Genes

- SYS-1986: suction deforms and removes material in the engaged
  portion while unengaged sections can persist. Retargeting the
  live deposit can continue the removal.
- SYS-1987: completing the local contamination removal restores
  surrounding vegetation and leaves the addressed path clear.

### Constraint Genes

The new route state follows from the local restoration rule. The
scope does not establish a second inventory, clock or combat gate.

### Information Genes

- INF-644: the contact feedback changes with the engaged material.
  A stretched strand or particles point back to the arm and
  unengaged attached residue is still visible. The tutorial shows
  a separate precision-aim hint.

### Objective Genes

- OBJ-026: after making the through-route clear, reach the stone
  area past the arch by walking it under player control.

### Time Genes

The player can hold the removal action and see its progress.
No independent binding deadline or other time-gated decision
was established for this scoped crossing.

### Parameters

Suction direction, effective contact, residual attached material,
local restored area, and the exposed stone route are relevant.
The witnesses do not measure a fixed radius, exact internal
component count, contact geometry or required hold duration.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Repaired arm and visible contamination on the shelf | Aim and hold suction toward a reachable portion | Local strands and particles show material drawing into the intake | TG-002–TG-004 |
| Part of the growth has been removed | Position and aim toward the remaining growth | Another portion clears while visible untouched residue can remain | TG-003–TG-005 |
| Last visible residue is removed | Let the restoration response run | The growth clears around the opening and vegetation returns to the shelf | TG-005 |
| Rock arch has cleared | Walk through the opening | Rani reaches the area with the visible green fissure without planting a seed | TG-006 |

## Strategic and experiential structure

Removing a section in front of the arm may leave other material
around the approach. Re-aim to finish the local clearance, watch
the restoration, then enter the opening. Plant growth is part of
the world-state response. In this fixture the actual crossing
runs on rock under the arch.

## Replay and variation

Both witnesses show local restoration after the held suction work.
Their facing, path around the black growth and elapsed cleanup
differ. That is observed variation in execution, not evidence of
a random arrangement or a universal suction threshold.

## Adjacent systems and history

The earlier mushroom staircase grows after a transported seed enters
an energy fissure. It is entry context only. Planting and stepping on
seed-grown supports is a separate action and route dependency.
The two processes are not interchangeable in this fixture.

## Normalised genome

- Action: ACT-008, ACT-542.
- System Behaviour: SYS-1986, SYS-1987.
- Constraint: none.
- Information: INF-644.
- Objective: OBJ-026.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `706` (`GAME-0001`–`GAME-0706`).
- Exact genome matches: none.
- Tied near matches: `GAME-0700` — Planet of Lana II: Children of the Leaf (`2 / 9 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Planet of Lana II (GAME-0700)](../m-r/planet-of-lana-ii.md) | ACT-008, OBJ-026 | Both traverse a route after changing its availability. Lana crosses a plant shelf held by Mui's pressure-plate occupancy, then recalls Mui. Rani clears an attached deposit, the site regrows and the rock arch remains open for the crossing. | Near, `0.222222`. |

## Taxonomy impact

Reuse local movement, directed vacuum input and arrival after
establishing the route. Isolate partial environmental removal,
grouped habitat and route restoration, and the live directional
feedback for a stationary deposit undergoing removal.

## Negative results

- Clearing a visible portion can leave the local area contaminated
  until the residual growth is removed.
- The restored shelf does not require another seed before crossing.
- The two recordings do not determine exact contact distance or show
  every possible order of clearing parts of the deposit.

## Delta summary

This unit records two linked resolutions: portion-by-portion
removal from a fixed location and a later local restoration that
opens a stone passage.

## New facts

- The suction response identifies a local point of engagement.
- Nearby greenery returns at full local clearance.
- The next reachable space is evidenced by a separate walking
  transition after the final removal and restoration effect.

## Principles and design implications

Show partial work spatially and provide a distinct state change
for complete clearance. Give that completion a route consequence
that can be checked by moving through the level.

## Puzzle or game generation potential

Set an obstruction around a rock arch with independently reachable
parts. Provide an aimed held tool and a visible indication of the
section now engaged. After its remaining prohibited material is gone,
settle the local habitat state and permit ordinary travel across the
opening. Verify that partial work alone does not finish the route.

## New genes

- INF-644
- SYS-1986
- SYS-1987

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 453](../../../research/taxonomy-changes/TAXONOMY_CHANGE_453.md).

## New questions

- Which off-angle residues can be removed from the initial approach?
- Which later restored sites require growing a fresh support before
  the player can traverse them?

## Next recommended game

Continue Selection 061 with Rampart on the original Atari Games
three-player trackball arcade release. Follow the solo cannon and
rebuild cycle to a witnessed enclosure decision.

## Why this game

The first ridge clearing makes individual vacuum removal,
area restoration and successful traversal three observable events.
