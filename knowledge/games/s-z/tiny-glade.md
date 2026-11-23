---
game_id: GAME-0637
slug: tiny-glade
game_title: "Tiny Glade"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-848
    - ACT-849
  system:
    - SYS-1840
  constraint: []
  information:
    - INF-591
  objective: []
  time:
    - TIM-002
---

# Game: Tiny Glade

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English Windows Steam commercial Tiny Glade
  (App 2198150), released 23 September 2024 by Pounce Light. The
  packet concerns release-era rules. The first-hand illustrated
  guide identifies version 1.8.1. The principal footage was published
  five days after release. Its exact executable revision, OS
  overlay and installed file hashes are not visible.
- Primary decision loop: draw a wall or use an existing compatible
  barrier, aim and paint a surface path into its base, observe the
  opening, and revise the crossing footprint to change the result.
- Entry: an editable glade with an ordinary ground-level wall or
  fence that does not already have a path-driven opening at the
  selected point.
- Exit: a visible opening forms and a comparison on the retained
  structure shows how changing the footprint changes the opening.
  This is an observation boundary in the free-form editor.
- Included: freehand barrier layout, path-brush targeting, persistent
  ground strokes, automatic opening generation and local revision
  without a timed requirement.
- Excluded: demo-only or pre-release behavior, manually mounted
  doors and window-derived doors, manual changes to opening height,
  water grates, later patch features, measured camera passability,
  autosave and imported designs.
- Suggested later scope: test full crossing erasure on different
  wall materials and measure the boundaries at which arches split.

## Direct-play status

No direct play was performed. Pounce Light identifies the commercial
Windows Steam release and describes automatic doors where a path
crosses a building. Release-period player footage was inspected as
silent static frames. The illustrated 1.8.1 player guide documents
partial erasure and shows the same masonry corner with one arch on
each side and with the left arch divided. A second release-window video
shows the full create-and-revise example on one frontage. Exact binary parity,
native input telemetry and direct camera traversal were not tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GLADE-001 | Pounce Light released the commercial editor on Steam on 23 September 2024. Its Windows listing describes gridless building and automatic path-driven doors. There is no imposed completion goal in the editor. | Confirmed | Direct | High | P1 store description, Windows requirements and release date. P2 full-version release announcement. |
| GLADE-002 | The player can trace a durable wall in world space with the wall tool. The wall exists when the player switches to editing a different layer. | Observation | Corroborated | High | P1 gridless building. W1 wall-tool chapters 14:35–19:10. W3 draws a freestanding wall around 0:18–0:29 and switches tools before changing it. |
| GLADE-003 | An aimed brush paints an exposed ground patch; an ordinary paint stroke that stops short of the fence leaves it continuous. Extending the path to its base produces an opening on the retained fence. | Observation | Corroborated | High | W1 19:13–19:42, specifically the strip and solid fence at 19:38–19:40 and opening at 19:42. P1 and W2 describe this property for compatible structures. |
| GLADE-004 | The same editing tool can generate an aperture in the distinct, taller masonry wall after it already exists. The brush circle marks the targeted surface footprint. A wider path relative to the masonry frontage can produce multiple arches. | Observation | Corroborated | High | W1 20:03–20:12 changes the stone wall behind the fence. At 20:24–20:36 several apertures appear under the façade while that structure remains. W2 illustrates width and multi-arch outcomes. W3 around 0:30–1:00. |
| GLADE-005 | Erasing a narrow part of the crossing footprint can restore a dividing pier within the opening. The rest of the wall and the remaining opening persist. | Observation | Corroborated | High | W2, displayed version 1.8.1, Doors, Arches, and Grates (Path Tool). The two adjacent corner images show the same left frontage before and after a one-to-two change; the right arch remains. W4 6:28–6:48 shows a blank target patch, a wide opening created by painting and the narrowing of that same opening while the path eraser is applied on its left edge. |
| GLADE-006 | The player can choose when to continue editing and see a stable geometric result between strokes. The editor has no prescribed winning form or timed end condition. | Observation | Corroborated | High | P1 editor purpose and rules. W1 19:10–20:40 changes state through individual editing gestures while the player pauses to look. |

## Basic data

- Analysis target: `PLAT-WINDOWS-PC`.
- Developer and publisher: Pounce Light.
- Mechanical family: `FAM-014`, world topology and perspective. This
  packet edits geometric openings in a continuous wall.
- Checked: 2026-11-22.
- P1: [Pounce Light, commercial Steam listing](https://store.steampowered.com/app/2198150/Tiny_Glade/).
- P2: [Pounce Light, commercial launch announcement](https://steamcommunity.com/ogg/2198150/announcements/detail/4708039771686448127).
- P3: [Pounce Light, patch 1.8.1 announcement](https://steamcommunity.com/ogg/2198150/announcements/detail/4708039771691220346). The separately introduced window-based behavior is outside scope.
- W1: [freakout3516, release-period editor guide](https://www.youtube.com/watch?v=-lthWN4B3i8&t=1153s), 28 September 2024.
- W2: [Zaiquiri Daiquiri, first-hand illustrated doors and arches guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3336778388), posted 23 September and updated 27 September 2024. Its two left-frontage states accompany the eraser explanation.
- W3: [JaruS Creations, wall and arch demonstration](https://www.youtube.com/watch?v=zV_xAA8zlBw&t=18s), 27 October 2024. The interface in this supplementary source is German.
- W4: [Move The Mouse, release-window tips](https://www.youtube.com/watch?v=1KA-Y4g-PZ8&t=388s), 25 September 2024. Same roof, left door and vine-covered façade remain in view while the right opening forms at 6:37–6:38 and narrows under the red path eraser at 6:43–6:48.

## Mechanical decomposition

### Action Genes

- ACT-848: trace a retained wall or fence with the wall tool.
- ACT-849: change the surface path's footprint with the path or
  matching eraser brush.

### System Behaviour Genes

- SYS-1840: crossing geometry creates an aperture where the path
  reaches the base of a compatible barrier. The altered crossing
  can change the shape or number of apertures in that same wall.

### Constraint Genes

No independent constraint gene is needed. Compatibility and
overlap are conditions of the documented transformation.

### Information Genes

- INF-591: a projected outline reveals the active brush footprint
  on the ground and lets the player target a local change.

### Objective Genes

The packet has no game-imposed objective. A desired form is chosen
by the builder and can be edited again after the checkpoint.

### Time Genes

- TIM-002: decide when to paint, inspect and revise without a
  required timing window or time-driven wall state change.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| An editable region of the glade has no wall there | Trace a barrier with the wall tool | A wall follows the stroke and remains when the active tool changes | GLADE-002 |
| A continuous fence stands next to an unpainted area | Paint a path beside it and stop short | A ground patch appears while the fence stays continuous | GLADE-003 |
| The fence still blocks the intended crossing | Extend the brush stroke to its base | The fence develops an opening at the crossing | GLADE-003 |
| Existing masonry encloses a second spot | Paint the ground stroke through the wall | An aperture appears in that wall, and further nearby path paint can make multiple openings | GLADE-004 |
| The front wall has no opening at the right-hand ivy patch | Paint a path to that patch, then erase its left edge | The new arch remains open with a narrower width, and the adjacent left door stays in place | GLADE-005 |
| A wide path runs through the left opening of a masonry corner | Erase a narrow section of the crossing footprint | The guide's example shows a pier between two smaller left openings. The separate right arch remains | GLADE-005 |

## Strategic and experiential structure

The wall and path are editable inputs in different tools. The
resulting shape at their intersection is computed automatically.
Branching the path or erasing a local strip can change wall
geometry without repositioning the wall. The brush outline makes
the affected ground region visible without promising exact output
geometry in advance.

## Replay and variation

Observed cases include a wooden fence, masonry wall and a building
frontage. The examples show one opening or several. No particular
brush width, universal material rule or exact condition for a
single spanning arch has been established.

## Adjacent systems and history

Patch 1.8.1 also documents a way to turn windows into doors near a
base. That separately operated tool is excluded. The water grate
visible later in W1 has a different environmental condition and
is outside the packet.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-848, ACT-849 | Trace the barrier and paint or erase the path |
| System Behaviour | SYS-1840 | Derive the opening from crossing geometry |
| Constraint | — | Cover compatibility within the transformation |
| Information | INF-591 | Show the brush footprint |
| Objective | — | Support the player's chosen form |
| Time | TIM-002 | Allow untimed revision |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `636` (`GAME-0001`–`GAME-0636`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 9 = 0.111111`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [SET (GAME-0064)](set.md) | TIM-002 | Both permit player-paced decisions. SET tests a discrete subset against a relation and an objective. Tiny Glade edits overlapping continuous geometry and leaves the design goal to the player. | Near, `0.111111` |

## Taxonomy impact

Four definitions cover the freehand structural stroke, the path
footprint edit, the derived opening and the active brush outline.
Self-paced timing applies as written. A photographic building
aesthetic is not a mechanical family.

## Negative results

- The ground can be painted without opening the adjacent fence when
  the paint does not reach the crossing.
- A path-driven opening can change after a local footprint edit.
  The evidence for revision establishes the recorded narrowing, the illustrated partial split
  and the retained surrounding structure.
- The records do not establish what happens for every barrier when
  its entire crossing is erased, or how the geometric thresholds
  for stable single and multiple arch spans are calculated.

## Delta summary

Five genes capture a bounded free-form building interaction.
Four are new and one is reused. Earlier definitions and signatures
are unchanged.

## New facts

- An editable wall can remain between successive brushes.
- A surface-only edit can generate a separate change to the wall.
- A local erasure can divide a derived arch without deleting the
  rest of the wall.

## Principles and design implications

- Let independent edit layers produce readable combined geometry.
- Expose the brush's affected area while the geometry responds.
- Preserve adjacent parts when a footprint changes locally.

## Puzzle or game generation potential

Prototype a direct-edit garden model with separate path and wall
layers. Provide a visible brush footprint and allow a local
erasure to recover a wall pier. An authored target can be added
to the prototype independently of the game being analysed.

## New genes

ACT-848, ACT-849, SYS-1840 and INF-591.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_383](../../../research/taxonomy-changes/TAXONOMY_CHANGE_383.md).

## New questions

For which materials and ground geometries does complete removal
return an entirely unbroken wall? How do two nearby footprints
merge or split their corresponding openings?

## Next recommended game

Analyse the original commercial Amiga Lemmings 2: The Tribes
through its first verified rescue and actual campaign successor.

## Why this game

A builder edits the ground and immediately sees the independently
authored wall respond. A subsequent local edit can change the
same opening again.
